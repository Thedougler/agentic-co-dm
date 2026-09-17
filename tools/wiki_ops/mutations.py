"""Typed markdown mutations with semantic selectors and hash preconditions."""
from __future__ import annotations

import difflib
import hashlib
import json
import os
import re
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .index_ops import insert_index_entry, remove_index_entry, replace_index_entry
from .manifest_ops import ManifestTransition, apply_transition

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LINK_RE = re.compile(r"(!?\[\[)([^\]|#]+)(#[^\]|]*)?(\|[^\]]+)?(\]\])")


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    except BaseException:
        try:
            os.unlink(name)
        except FileNotFoundError:
            pass
        raise


def _frontmatter_lines(text: str) -> tuple[list[str], int, int]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return lines, -1, -1
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return lines, 0, index
    return lines, -1, -1


def frontmatter_fields(text: str) -> dict[str, str]:
    lines, start, end = _frontmatter_lines(text)
    if start < 0:
        return {}
    result: dict[str, str] = {}
    for line in lines[start + 1:end]:
        if ":" in line and not line[:1].isspace():
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("\"'")
    return result


@dataclass(frozen=True)
class Section:
    heading_path: tuple[str, ...]
    level: int
    heading: str
    start: int
    body_start: int
    end: int
    content: str

    @property
    def hash(self) -> str:
        return section_hash(self.content)


class SectionSet(list[Section]):
    def find(self, heading_path: list[str] | tuple[str, ...]) -> Section:
        wanted = tuple(heading_path)
        matches = [section for section in self if section.heading_path == wanted]
        if not matches and wanted:
            matches = [section for section in self if section.heading_path[-len(wanted):] == wanted]
        if not matches:
            raise ValueError("selector_not_found")
        if len(matches) > 1:
            raise ValueError("selector_ambiguous")
        return matches[0]


def parse_sections(source: str | Path) -> SectionSet:
    if isinstance(source, Path):
        text = source.read_text(encoding="utf-8")
    elif isinstance(source, str) and "\n" not in source and Path(source).is_file():
        text = Path(source).read_text(encoding="utf-8")
    else:
        text = str(source)
    lines = text.splitlines(keepends=True)
    headings: list[tuple[int, str, int]] = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line.rstrip("\r\n"))
        if match:
            headings.append((len(match.group(1)), match.group(2).strip(), index))
    sections = SectionSet()
    for number, (level, heading, start) in enumerate(headings):
        end = len(lines)
        for next_level, _next_heading, next_start in headings[number + 1:]:
            if next_level <= level:
                end = next_start
                break
        stack = [(item_level, item_heading) for item_level, item_heading, item_start in headings[:number] if item_start < start]
        path: list[str] = []
        for item_level, item_heading in stack:
            while len(path) >= item_level:
                path.pop()
            path.append(item_heading)
        while len(path) >= level:
            path.pop()
        path.append(heading)
        body_start = start + 1
        content = "".join(lines[body_start:end])
        sections.append(Section(tuple(path), level, heading, start, body_start, end, content))
    return sections


def section_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class MutationOp:
    kind: str
    target: str
    selector: dict[str, Any] = field(default_factory=dict)
    payload: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "MutationOp":
        if not isinstance(value, dict) or not value.get("kind") or not value.get("target"):
            raise ValueError("mutation requires kind and target")
        return cls(str(value["kind"]), str(value["target"]), dict(value.get("selector") or {}), dict(value.get("payload") or {}))

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class RepairPlan:
    actions: list[dict[str, Any]]
    scope: dict[str, Any] | None = None
    source_findings: int = 0
    human_only: int = 0
    diagnostic_only: int = 0

    def to_dict(self) -> dict[str, Any]:
        data = {"scope": self.scope or {}, "source_findings": self.source_findings, "deterministic_actions": len(self.actions), "human_only": self.human_only, "diagnostic_only": self.diagnostic_only, "actions": self.actions}
        data["hash"] = "sha256:" + hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        return data


def _target(vault: Path, relative: str) -> Path:
    path = (vault / relative).resolve()
    try:
        path.relative_to(vault.resolve())
    except ValueError as exc:
        raise ValueError("target escapes vault") from exc
    return path


def _replace_section(text: str, op: MutationOp) -> str:
    section = parse_sections(text).find(op.selector.get("heading_path", []))
    expected = op.selector.get("content_hash")
    if expected and section_hash(section.content) != expected:
        raise ValueError(f"hash_mismatch: expected {expected}, got {section_hash(section.content)}")
    lines = text.splitlines(keepends=True)
    content = str(op.payload.get("content", ""))
    if content and not content.endswith(("\n", "\r")):
        content += "\n"
    newline = "\r\n" if lines and lines[0].endswith("\r\n") else "\n"
    replacement = lines[section.start]
    if content:
        replacement += content
    elif section.start + 1 < len(lines):
        replacement += newline
    lines[section.start:section.end] = [replacement]
    return "".join(lines)


def _delete_section(text: str, op: MutationOp) -> str:
    section = parse_sections(text).find(op.selector.get("heading_path", []))
    expected = op.selector.get("content_hash")
    if expected and section_hash(section.content) != expected:
        raise ValueError("hash_mismatch")
    lines = text.splitlines(keepends=True)
    del lines[section.start:section.end]
    return "".join(lines)


def _insert_section(text: str, op: MutationOp) -> str:
    sections = parse_sections(text)
    anchor = op.selector.get("after_heading_path") or op.selector.get("before_heading_path")
    if not anchor:
        raise ValueError("selector_not_found")
    section = sections.find(anchor)
    lines = text.splitlines(keepends=True)
    heading = str(op.payload.get("heading", "")).strip()
    level = int(op.payload.get("level", section.level))
    content = str(op.payload.get("content", ""))
    if content and not content.endswith("\n"):
        content += "\n"
    block = f"{'#' * level} {heading}\n" + content
    index = section.end if op.selector.get("after_heading_path") else section.start
    lines.insert(index, block)
    return "".join(lines)


def _set_frontmatter(text: str, field: str, value: Any) -> str:
    lines, start, end = _frontmatter_lines(text)
    if start < 0:
        lines = ["---\n", "---\n"] + lines
        start, end = 0, 1
    encoded = str(value)
    for index in range(start + 1, end):
        if lines[index].split(":", 1)[0].strip() == field:
            newline = "\r\n" if lines[index].endswith("\r\n") else "\n"
            lines[index] = f"{field}: {encoded}{newline}"
            return "".join(lines)
    lines.insert(end, f"{field}: {encoded}\n")
    return "".join(lines)


def _remove_frontmatter(text: str, field: str, expected: Any = None) -> str:
    lines, start, end = _frontmatter_lines(text)
    if start < 0:
        raise ValueError("selector_not_found")
    for index in range(start + 1, end):
        key, _, value = lines[index].partition(":")
        if key.strip() == field:
            if expected is not None and value.strip().strip("\"'") != str(expected):
                raise ValueError("value_mismatch")
            del lines[index]
            return "".join(lines)
    raise ValueError("selector_not_found")


def _rewrite_links(text: str, old: str, new: str) -> str:
    def replace(match: re.Match[str]) -> str:
        target = match.group(2)
        stem = target[:-3] if target.endswith(".md") else target
        if stem.rsplit("/", 1)[-1] != old:
            return match.group(0)
        prefix = target.rsplit("/", 1)[0] + "/" if "/" in target else ""
        suffix = ".md" if target.endswith(".md") else ""
        return f"{match.group(1)}{prefix}{new}{suffix}{match.group(3) or ''}{match.group(4) or ''}{match.group(5)}"
    return LINK_RE.sub(replace, text)


def resolve_mutation(vault: str | Path, op: MutationOp, text: str | None = None) -> tuple[str, str]:
    root = Path(vault).resolve()
    path = _target(root, op.target)
    current = text if text is not None else path.read_text(encoding="utf-8")
    kind = op.kind
    if kind == "replace_section":
        result = _replace_section(current, op)
    elif kind == "delete_section":
        result = _delete_section(current, op)
    elif kind == "insert_section":
        result = _insert_section(current, op)
    elif kind == "set_frontmatter":
        result = _set_frontmatter(current, str(op.selector.get("field")), op.payload.get("value"))
    elif kind == "remove_frontmatter":
        result = _remove_frontmatter(current, str(op.selector.get("field")), op.selector.get("expected_value"))
    elif kind == "rewrite_links":
        result = _rewrite_links(current, str(op.payload.get("old_target", "")), str(op.payload.get("new_target", "")))
    elif kind == "replace_index_entry":
        result = replace_index_entry(current, str(op.selector.get("slug")), str(op.payload.get("new_entry", "")))
    elif kind == "remove_index_entry":
        result = remove_index_entry(current, str(op.selector.get("slug")))
    elif kind == "insert_index_entry":
        result = insert_index_entry(current, str(op.payload.get("entry", "")))
    elif kind == "update_manifest_identity":
        result = current
    else:
        raise ValueError(f"unsupported mutation kind: {kind}")
    diff = "".join(difflib.unified_diff(current.splitlines(True), result.splitlines(True), fromfile=op.target, tofile=op.target))
    return result, diff


def apply_mutation(vault: str | Path, op: MutationOp, *, dry_run: bool = False) -> dict[str, Any]:
    root = Path(vault).resolve()
    try:
        path = _target(root, op.target)
        if not path.is_file():
            raise ValueError("file_not_found")
        if op.kind == "rename_page":
            destination = _target(root, str(op.payload.get("new_target", "")))
            if destination.exists():
                raise ValueError("target_exists")
            if dry_run:
                return {"status": "dry_run", "kind": op.kind, "target": op.target, "new_target": str(op.payload.get("new_target")), "dry_run": True}
            destination.parent.mkdir(parents=True, exist_ok=True)
            os.replace(path, destination)
            return {"status": "applied", "kind": op.kind, "target": op.target, "new_target": str(op.payload.get("new_target")), "dry_run": False}
        result, diff = resolve_mutation(root, op)
        if not dry_run:
            atomic_write(path, result)
        return {"status": "dry_run" if dry_run else "applied", "kind": op.kind, "target": op.target, "diff": diff, "dry_run": dry_run}
    except (OSError, ValueError) as exc:
        return {"status": "rejected", "kind": op.kind, "target": op.target, "error": str(exc), "dry_run": dry_run}

def validate_non_overlapping(ops: list[MutationOp]) -> list[str]:
    ranges: dict[str, list[tuple[int, int]]] = {}
    failures: list[str] = []
    for op in ops:
        path = op.target
        if op.kind not in {"replace_section", "delete_section"}:
            continue
        try:
            # Range collision is detected by heading paths; a parent and child overlap.
            current = tuple(op.selector.get("heading_path", []))
            for other_start, other_end in ranges.get(path, []):
                if current[:other_start] == current[:other_end] or other_start == len(current):
                    failures.append(f"overlap: {path}")
            ranges.setdefault(path, []).append((len(current), len(current)))
        except Exception:
            failures.append(f"overlap: {path}")
    for index, left in enumerate(ops):
        for right in ops[index + 1:]:
            if left.target == right.target and left.selector.get("heading_path") and right.selector.get("heading_path"):
                a, b = tuple(left.selector["heading_path"]), tuple(right.selector["heading_path"])
                if a == b or a[:len(b)] == b or b[:len(a)] == a:
                    failures.append(f"overlap: {left.target}")
    return sorted(set(failures))


def merge_operations(source: str, canonical: str) -> list[MutationOp]:
    return [
        MutationOp("rewrite_links", source, payload={"old_target": source.rsplit("/", 1)[-1].removesuffix(".md"), "new_target": canonical.rsplit("/", 1)[-1].removesuffix(".md")}),
        MutationOp("update_manifest_identity", ".manifest.json", payload={"page_path": source, "transition": "merged_into", "target": canonical}),
        MutationOp("remove_index_entry", "index.md", selector={"slug": source.rsplit("/", 1)[-1].removesuffix(".md")}),
    ]
