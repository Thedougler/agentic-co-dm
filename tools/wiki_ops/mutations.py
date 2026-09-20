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
from typing import Any, Mapping

from .index_ops import ENTRY_RE, insert_index_entry, parse_index, remove_index_entry, replace_index_entry

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LINK_RE = re.compile(r"(!?\[\[)([^\]|#]+)(#[^\]|]*)?(\|[^\]]+)?(\]\])")
HASH_RE = re.compile(r"^[0-9a-fA-F]{64}$")
FRONTMATTER_KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_.-]*$")


class MutationError(ValueError):
    """An actionable, stable mutation rejection."""

    def __init__(self, code: str, detail: str | None = None):
        self.code = code
        self.detail = detail or code
        super().__init__(self.detail)


def _fail(code: str, detail: str | None = None) -> None:
    raise MutationError(code, detail)


def atomic_write(path: Path, text: str) -> None:
    """Write one UTF-8 file through a fsynced temporary sibling and rename."""
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


def _newline(text: str) -> str:
    if "\r\n" in text:
        return "\r\n"
    return "\n"
def _read_text(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


def _normalise_block(content: Any, newline: str, *, terminate: bool = True) -> list[str]:
    value = str(content or "").replace("\r\n", "\n").replace("\r", "\n")
    if not value:
        return []
    value = value.replace("\n", newline)
    if terminate and not value.endswith(newline):
        value += newline
    return value.splitlines(keepends=True)


def _frontmatter_lines(text: str) -> tuple[list[str], int, int]:
    """Return lines and frontmatter bounds, rejecting an unterminated block."""
    lines = text.splitlines(keepends=True)
    if not lines:
        return lines, -1, -1
    first = lines[0].lstrip("\ufeff").strip()
    if first != "---":
        return lines, -1, -1
    for index in range(1, len(lines)):
        if lines[index].strip() in {"---", "..."}:
            return lines, 0, index
    _fail("malformed_frontmatter", "frontmatter opening delimiter has no closing delimiter")
    raise AssertionError("unreachable")


def _frontmatter_entries(text: str) -> tuple[list[str], int, int, dict[str, list[int]]]:
    lines, start, end = _frontmatter_lines(text)
    if start < 0:
        return lines, start, end, {}
    entries: dict[str, list[int]] = {}
    for index in range(start + 1, end):
        line = lines[index]
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or line[:1].isspace():
            continue
        if ":" not in line:
            _fail("malformed_frontmatter", f"line {index + 1} is not a key/value entry")
        key, _ = line.split(":", 1)
        key = key.strip()
        if not FRONTMATTER_KEY_RE.fullmatch(key):
            _fail("malformed_frontmatter", f"invalid frontmatter key: {key!r}")
        entries.setdefault(key, []).append(index)
    return lines, start, end, entries


def _strip_eol(value: str) -> str:
    return value.rstrip("\r\n")


def _plain_value(value: str) -> str:
    value = _strip_eol(value).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def frontmatter_fields(text: str) -> dict[str, str]:
    lines, start, _, entries = _frontmatter_entries(text)
    if start < 0:
        return {}
    result: dict[str, str] = {}
    for key, indexes in entries.items():
        # Inspection is deterministic; mutations reject duplicate selectors.
        index = indexes[-1]
        result[key] = _plain_value(lines[index].split(":", 1)[1])
    return result


def _field_end(lines: list[str], start: int, end: int) -> int:
    index = start + 1
    while index < end:
        line = lines[index]
        if not line.strip():
            break
        if not line[:1].isspace() and (":" in line or line.strip().startswith("#")):
            break
        index += 1
    return index


def _field_region(lines: list[str], start: int, end: int) -> str:
    return "".join(lines[start:_field_end(lines, start, end)])


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
        if isinstance(heading_path, str):
            _fail("malformed_selector", "heading_path must be a list of headings")
        wanted = tuple(str(item).strip() for item in heading_path if str(item).strip())
        if not wanted:
            _fail("selector_not_found", "heading_path is empty")
        matches = [section for section in self if section.heading_path == wanted]
        if not matches:
            matches = [section for section in self if len(section.heading_path) >= len(wanted) and section.heading_path[-len(wanted):] == wanted]
        if not matches:
            _fail("selector_not_found", f"heading path not found: {' > '.join(wanted)}")
        if len(matches) > 1:
            _fail("selector_ambiguous", f"heading path is not unique: {' > '.join(wanted)}")
        return matches[0]


def _heading_text(raw: str) -> str:
    value = raw.strip()
    return re.sub(r"\s+#+\s*$", "", value).strip() or value


def parse_sections(source: str | Path) -> SectionSet:
    """Parse Markdown headings while ignoring frontmatter and fenced code."""
    if isinstance(source, Path):
        text = _read_text(source)
    elif isinstance(source, str) and "\n" not in source and Path(source).is_file():
        text = _read_text(Path(source))
    else:
        text = str(source)
    lines = text.splitlines(keepends=True)
    headings: list[tuple[int, str, int]] = []
    fence: tuple[str, int] | None = None
    in_frontmatter = bool(lines and lines[0].lstrip("\ufeff").strip() == "---")
    for index, line in enumerate(lines):
        stripped = line.lstrip()
        if in_frontmatter:
            if index > 0 and line.strip() in {"---", "..."}:
                in_frontmatter = False
            continue
        fence_match = re.match(r"(`{3,}|~{3,})", stripped)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            continue
        if fence is not None:
            continue
        match = HEADING_RE.match(_strip_eol(line))
        if match:
            headings.append((len(match.group(1)), _heading_text(match.group(2)), index))
    sections = SectionSet()
    stack: list[tuple[int, str]] = []
    for number, (level, heading, start) in enumerate(headings):
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, heading))
        end = len(lines)
        for next_level, _, next_start in headings[number + 1:]:
            if next_level <= level:
                end = next_start
                break
        sections.append(Section(tuple(item[1] for item in stack), level, heading, start, start + 1, end, "".join(lines[start + 1:end])))
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
            _fail("malformed_mutation", "mutation requires kind and target")
        selector = value.get("selector") or {}
        payload = value.get("payload") or {}
        if not isinstance(selector, dict) or not isinstance(payload, dict):
            _fail("malformed_mutation", "selector and payload must be objects")
        return cls(str(value["kind"]), str(value["target"]), dict(selector), dict(payload))

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
    if not isinstance(relative, str) or not relative or "\x00" in relative or "\n" in relative or "\r" in relative:
        _fail("malformed_target", "target must be a non-empty vault-relative path")
    requested = Path(relative)
    if requested.is_absolute():
        _fail("malformed_target", "target must be vault-relative")
    root = vault.resolve()
    path = (root / requested).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        _fail("malformed_target", "target escapes vault")
    return path


def _hash_value(value: str) -> str:
    value = str(value).strip()
    if value.lower().startswith("sha256:"):
        value = value[7:]
    if not HASH_RE.fullmatch(value):
        _fail("malformed_hash", "content hash must be a SHA-256 hexadecimal digest")
    return value.lower()

def _identity_gate(root: Path, op: MutationOp) -> None:
    if op.kind not in {"rename_page", "merge_page", "rename_or_merge_page"}:
        return
    from .identity import resolve_identity

    try:
        identity = resolve_identity(root, op.target)
    except (OSError, ValueError):
        return
    if identity.signals.get("redirect_match") or identity.signals.get("canonical_path"):
        _fail("identity_redirect", f"redirect stubs are not canonical mutation targets: {op.target}")
    if identity.status != "ambiguous":
        return
    metadata = op.payload.get("identity_resolution", op.selector.get("identity_resolution"))
    accepted = False
    selected = None
    if isinstance(metadata, dict):
        accepted = metadata.get("status") in {"accepted", "resolved"} or bool(metadata.get("accepted"))
        selected = metadata.get("candidate") or metadata.get("canonical_path") or metadata.get("path")
    elif isinstance(metadata, str):
        accepted = bool(metadata.strip())
        selected = metadata
    if not accepted:
        _fail("identity_ambiguous", f"explicit identity_resolution is required for {op.target}")
    if selected and str(selected) not in {candidate["path"] for candidate in identity.candidates}:
        _fail("identity_candidate_mismatch", f"identity_resolution does not select a known candidate for {op.target}")


def _expected_hash(op: MutationOp) -> str | None:
    for container in (op.selector, op.payload):
        for key in ("content_hash", "expected_hash", "file_hash"):
            if key in container and container[key] is not None:
                return _hash_value(str(container[key]))
    return None


def _verify_hash(op: MutationOp, current: str, candidates: list[str], *, required: bool = False) -> None:
    expected = _expected_hash(op)
    if expected is None:
        if required:
            _fail("hash_required", "semantic mutation requires content_hash")
        return
    hashes = [section_hash(value) for value in [current, *candidates]]
    if expected not in hashes:
        _fail("hash_mismatch", f"expected {expected}, current {section_hash(current)}")


def _validate_document(text: str) -> None:
    _frontmatter_entries(text)
    parse_sections(text)


def _replace_section(text: str, op: MutationOp) -> str:
    section = parse_sections(text).find(op.selector.get("heading_path", []))
    if "content" not in op.payload:
        _fail("malformed_payload", "replace_section requires payload.content")
    replacement = _normalise_block(op.payload.get("content"), _newline(text), terminate=text.endswith(("\n", "\r")) or section.end < len(text.splitlines(keepends=True)))
    lines = text.splitlines(keepends=True)
    lines[section.body_start:section.end] = replacement
    result = "".join(lines)
    if result != text:
        _verify_hash(op, text, [section.content], required=True)
        _validate_document(result)
    return result


def _delete_section(text: str, op: MutationOp) -> str:
    section = parse_sections(text).find(op.selector.get("heading_path", []))
    _verify_hash(op, text, [section.content], required=True)
    lines = text.splitlines(keepends=True)
    del lines[section.start:section.end]
    result = "".join(lines)
    _validate_document(result)
    return result


def _insert_section(text: str, op: MutationOp) -> str:
    after = op.selector.get("after_heading_path")
    before = op.selector.get("before_heading_path")
    if bool(after) == bool(before):
        _fail("malformed_selector", "insert_section requires exactly one anchor")
    anchor_values: list[str] | tuple[str, ...] = ()
    if isinstance(after, (list, tuple)):
        anchor_values = tuple(str(item) for item in after)
    elif isinstance(before, (list, tuple)):
        anchor_values = tuple(str(item) for item in before)
    else:
        _fail("malformed_selector", "heading anchor must be a list of headings")
    anchor = parse_sections(text).find(anchor_values)
    heading = str(op.payload.get("heading", "")).strip()
    if not heading or "\n" in heading or "\r" in heading or heading.startswith("#"):
        _fail("malformed_payload", "insert_section requires one Markdown heading")
    level = anchor.level
    try:
        level = int(op.payload.get("level", anchor.level))
    except (TypeError, ValueError):
        _fail("malformed_payload", "heading level must be an integer from 1 to 6")
    if not 1 <= level <= 6:
        _fail("malformed_payload", "heading level must be an integer from 1 to 6")
    newline = _newline(text)
    block = [f"{'#' * level} {heading}{newline}"] + _normalise_block(op.payload.get("content", ""), newline)
    lines = text.splitlines(keepends=True)
    index = anchor.end if after else anchor.start
    if index and not lines[index - 1].endswith(("\n", "\r")):
        lines[index - 1] += newline
    lines[index:index] = block
    result = "".join(lines)
    # Replaying an insertion that already exists is an accepted no-op.
    body = "".join(block[1:])
    if any(item.level == level and item.heading == heading and item.content == body for item in parse_sections(text)):
        return text
    _verify_hash(op, text, [anchor.content])
    _validate_document(result)
    return result


def _encode_frontmatter_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(_encode_frontmatter_value(item) for item in value) + "]"
    if isinstance(value, dict):
        return json.dumps(value, sort_keys=True, separators=(",", ":"))
    value = str(value).replace("\r", " ").replace("\n", " ")
    return value


def _replace_field_line(line: str, value: Any) -> str:
    eol = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
    raw = _strip_eol(line)
    colon = raw.find(":")
    prefix = raw[:colon + 1]
    suffix = raw[colon + 1:]
    spacing = suffix[: len(suffix) - len(suffix.lstrip())]
    comment = ""
    comment_match = re.search(r"\s+#.*$", suffix)
    if comment_match:
        comment = comment_match.group(0)
    return f"{prefix}{spacing}{_encode_frontmatter_value(value)}{comment}{eol}"


def _set_frontmatter(text: str, field: str, value: Any) -> str:
    field = str(field or "").strip()
    if not FRONTMATTER_KEY_RE.fullmatch(field):
        _fail("malformed_selector", "field must be a valid frontmatter key")
    lines, start, end, entries = _frontmatter_entries(text)
    newline = _newline(text)
    if start < 0:
        result = f"---{newline}{field}: {_encode_frontmatter_value(value)}{newline}---{newline}" + text
        _validate_document(result)
        return result
    indexes = entries.get(field, [])
    if len(indexes) > 1:
        _fail("selector_ambiguous", f"frontmatter field is duplicated: {field}")
    if not indexes:
        insertion = f"{field}: {_encode_frontmatter_value(value)}{newline}"
        lines.insert(end, insertion)
    else:
        index = indexes[0]
        region_end = _field_end(lines, index, end)
        lines[index:region_end] = [_replace_field_line(lines[index], value)]
    result = "".join(lines)
    if result != text:
        _validate_document(result)
    return result


def _remove_frontmatter(text: str, field: str, expected: Any = None) -> str:
    field = str(field or "").strip()
    lines, start, end, entries = _frontmatter_entries(text)
    if start < 0 or field not in entries:
        _fail("selector_not_found", f"frontmatter field not found: {field}")
    if len(entries[field]) > 1:
        _fail("selector_ambiguous", f"frontmatter field is duplicated: {field}")
    index = entries[field][0]
    actual = _plain_value(lines[index].split(":", 1)[1])
    if expected is not None and actual != _plain_value(str(expected)):
        _fail("value_mismatch", f"expected {expected!r}, current {actual!r}")
    del lines[index:_field_end(lines, index, end)]
    result = "".join(lines)
    _validate_document(result)
    return result


def _split_inline_items(value: str) -> list[str]:
    body = value.strip()[1:-1].strip()
    if not body:
        return []
    items: list[str] = []
    current: list[str] = []
    quote: str | None = None
    escaped = False
    for char in body:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\" and quote == '"':
            current.append(char)
            escaped = True
        elif quote:
            current.append(char)
            if char == quote:
                quote = None
        elif char in {"'", '"'}:
            quote = char
            current.append(char)
        elif char == ",":
            items.append(_plain_value("".join(current)))
            current = []
        else:
            current.append(char)
    items.append(_plain_value("".join(current)))
    return [item.strip() for item in items if item.strip()]


def _tag_key(value: str) -> str:
    return _plain_value(value).strip().lstrip("#").casefold()


def _tag_data(text: str) -> tuple[list[str], list[str], int, int, str] | None:
    lines, start, end, entries = _frontmatter_entries(text)
    if start < 0 or "tags" not in entries:
        return None
    indexes = entries["tags"]
    if len(indexes) > 1:
        _fail("selector_ambiguous", "frontmatter field is duplicated: tags")
    index = indexes[0]
    region_end = _field_end(lines, index, end)
    raw = _strip_eol(lines[index].split(":", 1)[1]).strip()
    if raw.startswith("[") and raw.endswith("]"):
        return _split_inline_items(raw), lines, index, region_end, "inline"
    if not raw:
        tags = []
        for line in lines[index + 1:region_end]:
            stripped = line.strip()
            if stripped.startswith("-"):
                tags.append(_plain_value(stripped[1:].strip()))
        return tags, lines, index, region_end, "block"
    return [_plain_value(raw)], lines, index, region_end, "scalar"


def _render_tag(value: str) -> str:
    value = value.lstrip("#")
    return value if re.fullmatch(r"[A-Za-z0-9_./:-]+", value) else json.dumps(value, ensure_ascii=False)


def _mutate_tag(text: str, op: MutationOp, *, add: bool) -> str:
    raw_tag = op.payload.get("tag", op.payload.get("value", op.selector.get("tag")))
    tag = str(raw_tag or "").strip()
    if not tag or "\n" in tag or "\r" in tag:
        _fail("malformed_payload", "tag is required")
    data = _tag_data(text)
    newline = _newline(text)
    if data is None:
        if not add:
            return text
        lines, start, end, _ = _frontmatter_entries(text)
        if start < 0:
            result = f"---{newline}tags: [{_render_tag(tag)}]{newline}---{newline}" + text
        else:
            lines.insert(end, f"tags: [{_render_tag(tag)}]{newline}")
            result = "".join(lines)
        _verify_hash(op, text, [])
        _validate_document(result)
        return result
    tags, lines, index, region_end, style = data
    keys = {_tag_key(item) for item in tags}
    present = _tag_key(tag) in keys
    if (add and present) or (not add and not present):
        return text
    if add:
        tags.append(tag.lstrip("#"))
    else:
        tags = [item for item in tags if _tag_key(item) != _tag_key(tag)]
    if style == "block":
        indent = "  "
        for line in lines[index + 1:region_end]:
            if line.strip().startswith("-"):
                indent = line[: len(line) - len(line.lstrip())]
                break
        replacement = [_strip_eol(lines[index]).rstrip() + newline]
        replacement.extend(f"{indent}- {_render_tag(item)}{newline}" for item in tags)
    else:
        prefix = _strip_eol(lines[index]).split(":", 1)[0] + ":"
        replacement = [prefix + " [" + ", ".join(_render_tag(item) for item in tags) + "]" + ("\r\n" if lines[index].endswith("\r\n") else "\n" if lines[index].endswith("\n") else "")]
    lines[index:region_end] = replacement
    result = "".join(lines)
    _verify_hash(op, text, [_field_region(data[1], index, region_end)])
    _validate_document(result)
    return result


def _link_target_matches(target: str, old: str) -> bool:
    target_stem = target.removesuffix(".md").lstrip("./")
    old_stem = old.removesuffix(".md").lstrip("./")
    if target_stem == old_stem:
        return True
    # Obsidian commonly omits the path for a unique page; retain that useful form.
    return "/" not in target_stem and target_stem.rsplit("/", 1)[-1] == old_stem.rsplit("/", 1)[-1]


def _rewrite_links(text: str, old: str, new: str) -> str:
    old = str(old or "").strip()
    new = str(new or "").strip()
    if not old or not new:
        _fail("malformed_payload", "link repair requires old_target and new_target")

    def replace(match: re.Match[str]) -> str:
        target = match.group(2)
        if not _link_target_matches(target, old):
            return match.group(0)
        target_has_ext = target.endswith(".md")
        replacement = new
        if target_has_ext and not replacement.endswith(".md"):
            replacement += ".md"
        elif not target_has_ext and replacement.endswith(".md"):
            replacement = replacement[:-3]
        if "/" not in target and "/" in replacement:
            replacement = replacement.rsplit("/", 1)[-1]
        return f"{match.group(1)}{replacement}{match.group(3) or ''}{match.group(4) or ''}{match.group(5)}"

    return LINK_RE.sub(replace, text)


def _repair_links(text: str, op: MutationOp) -> str:
    mapping = op.payload.get("mapping", op.payload.get("links"))
    pairs: list[tuple[str, str]] = []
    if isinstance(mapping, dict):
        pairs = [(str(old), str(new)) for old, new in sorted(mapping.items(), key=lambda item: str(item[0]))]
    elif isinstance(mapping, list):
        for item in mapping:
            if not isinstance(item, dict) or not item.get("old_target") or not item.get("new_target"):
                _fail("malformed_payload", "link mapping entries require old_target and new_target")
            pairs.append((str(item["old_target"]), str(item["new_target"])))
    else:
        old = op.payload.get("old_target", op.selector.get("old_target"))
        new = op.payload.get("new_target", op.selector.get("new_target"))
        if old and new:
            pairs = [(str(old), str(new))]
    if not pairs:
        _fail("malformed_payload", "repair_links requires a link mapping")
    result = text
    for old, new in pairs:
        result = _rewrite_links(result, old, new)
    if result != text:
        _verify_hash(op, text, [])
        _validate_document(result)
    return result


def _manifest_transition_text(text: str, page: str, transition: str, target: str | None = None, reason: str | None = None, timestamp: str | None = None) -> str:
    data: Any = None
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        _fail("malformed_manifest", str(exc))
    if not isinstance(data, dict):
        _fail("malformed_manifest", "manifest root must be an object")
    if transition not in {"merged_into", "renamed_to", "archived"}:
        _fail("malformed_payload", f"invalid identity transition: {transition}")
    rows = data.setdefault("page_identity_transitions", [])
    if not isinstance(rows, list):
        _fail("malformed_manifest", "page_identity_transitions must be a list")
    identity = {"page_path": page, "transition": transition}
    if target is not None:
        identity["target"] = target
    if reason is not None:
        identity["reason"] = reason
    for row in rows:
        if isinstance(row, dict) and all(row.get(key) == value for key, value in identity.items()):
            return text
    item = dict(identity)
    if timestamp:
        item["timestamp"] = timestamp
    rows.append(item)
    if timestamp:
        data["last_updated"] = timestamp
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def _update_manifest_identity(text: str, op: MutationOp) -> str:
    page = str(op.payload.get("page_path", op.selector.get("page_path", op.target)))
    transition = str(op.payload.get("transition", op.selector.get("transition", "")))
    target = op.payload.get("target", op.selector.get("target"))
    reason = op.payload.get("reason", op.selector.get("reason"))
    timestamp = op.payload.get("timestamp", op.selector.get("timestamp"))
    return _manifest_transition_text(text, page, transition, str(target) if target is not None else None, str(reason) if reason is not None else None, str(timestamp) if timestamp else None)

def resolve_mutation(vault: str | Path, op: MutationOp, text: str | None = None) -> tuple[str, str]:
    root = Path(vault).resolve()
    path = _target(root, op.target)
    current = text if text is not None else _read_text(path)
    kind = op.kind
    result = current
    if kind == "replace_section":
        result = _replace_section(current, op)
    elif kind == "delete_section":
        result = _delete_section(current, op)
    elif kind == "insert_section":
        result = _insert_section(current, op)
    elif kind == "set_frontmatter":
        result = _set_frontmatter(current, str(op.selector.get("field", op.payload.get("field", ""))), op.payload.get("value"))
        expected = op.selector.get("expected_value")
        if expected is not None and _plain_value(frontmatter_fields(current).get(str(op.selector.get("field")), "")) != _plain_value(str(expected)):
            _fail("value_mismatch", f"expected {expected!r}")
        if result != current:
            _verify_hash(op, current, [])
    elif kind == "remove_frontmatter":
        result = _remove_frontmatter(current, str(op.selector.get("field", "")), op.selector.get("expected_value"))
        if result != current:
            _verify_hash(op, current, [])
    elif kind in {"add_tag", "remove_tag"}:
        result = _mutate_tag(current, op, add=kind == "add_tag")
    elif kind in {"repair_links", "rewrite_links"}:
        result = _repair_links(current, op)
    elif kind == "replace_index_entry":
        result = replace_index_entry(current, str(op.selector.get("slug", "")), str(op.payload.get("new_entry", "")))
    elif kind == "remove_index_entry":
        result = remove_index_entry(current, str(op.selector.get("slug", "")))
    elif kind == "insert_index_entry":
        result = insert_index_entry(current, str(op.payload.get("entry", "")))
    elif kind == "delete_file":
        _verify_hash(op, current, [], required=False)
        result = ""
    elif kind in {"rename_page", "merge_page", "rename_or_merge_page"}:
        _fail("unsupported_context", f"{kind} requires apply_mutation for multi-file semantics")
    else:
        _fail("unsupported_kind", f"unsupported mutation kind: {kind}")
    diff = "".join(difflib.unified_diff(current.splitlines(True), result.splitlines(True), fromfile=op.target, tofile=op.target))
    if kind in {"replace_index_entry", "remove_index_entry", "insert_index_entry", "update_manifest_identity"} and result != current:
        _verify_hash(op, current, [])

    return result, diff

def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _collect_markdown(root: Path) -> list[Path]:
    return sorted((path for path in root.rglob("*.md") if path.is_file()), key=lambda path: _relative(root, path))


def _diff_for(path: Path, root: Path, before: str, after: str) -> str:
    return "".join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile=_relative(root, path), tofile=_relative(root, path)))


def _atomic_commit(changes: dict[Path, str], deletes: set[Path], originals: Mapping[Path, str | None]) -> None:
    if set(changes) & deletes:
        _fail("overlap", "a path cannot be both written and deleted")
    paths = sorted(set(changes) | deletes, key=lambda path: str(path))
    for path in paths:
        original = originals.get(path)
        if original is None:
            if path.exists():
                _fail("target_changed", f"target appeared during mutation: {path}")
        elif not path.is_file() or _read_text(path) != original:
            _fail("hash_mismatch", f"target changed during mutation: {path}")
    staged: dict[Path, str] = {}
    replaced: list[Path] = []
    try:
        for path, value in sorted(changes.items(), key=lambda item: str(item[0])):
            path.parent.mkdir(parents=True, exist_ok=True)
            fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
            with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
                handle.write(value)
                handle.flush()
                os.fsync(handle.fileno())
            staged[path] = name
        for path in sorted(changes, key=lambda item: str(item)):
            os.replace(staged[path], path)
            replaced.append(path)
        for path in sorted(deletes, key=lambda item: str(item)):
            if path.exists():
                path.unlink()
            else:
                _fail("target_changed", f"target disappeared during mutation: {path}")
    except BaseException:
        # Roll back every touched path; callers still receive a rejection and no partial state.
        for path in replaced:
            original = originals.get(path)
            if original is None:
                try:
                    path.unlink()
                except FileNotFoundError:
                    pass
            else:
                atomic_write(path, original)
        for path in deletes:
            original = originals.get(path)
            if original is not None and not path.exists():
                atomic_write(path, original)
        raise
    finally:
        for name in staged.values():
            try:
                os.unlink(name)
            except FileNotFoundError:
                pass


def _accepted(op: MutationOp, *, dry_run: bool, changed: bool, diff: str, detail: str = "changed", **extra: Any) -> dict[str, Any]:
    result: dict[str, Any] = {"status": "dry_run" if dry_run else "applied", "kind": op.kind, "target": op.target, "dry_run": dry_run, "accepted": True, "changed": changed, "detail": detail, "diff": diff}
    result.update(extra)
    return result


def _rejected(op: MutationOp, *, dry_run: bool, error: str, detail: str | None = None, **extra: Any) -> dict[str, Any]:
    result: dict[str, Any] = {"status": "rejected", "kind": op.kind, "target": op.target, "dry_run": dry_run, "accepted": False, "error": error, "detail": detail or error}
    result.update(extra)
    return result


def _rename_changes(root: Path, op: MutationOp) -> tuple[dict[Path, str], set[Path], dict[Path, str | None], str]:
    source = _target(root, op.target)
    new_target = op.payload.get("new_target", op.payload.get("canonical_path", op.payload.get("target", op.selector.get("new_target"))))
    if not new_target:
        _fail("malformed_payload", "rename_page requires payload.new_target")
    destination = _target(root, str(new_target))
    if source == destination:
        _fail("target_exists", "rename source and destination are identical")
    if not source.is_file():
        if destination.is_file():
            expected = _expected_hash(op)
            if expected is not None:
                destination_text = _read_text(destination)
                _verify_hash(op, destination_text, [])
            return {}, set(), {}, _relative(root, destination)
        _fail("file_not_found", f"target file not found: {_relative(root, source)}")
    if destination.exists():
        _fail("target_exists", f"destination already exists: {_relative(root, destination)}")
    source_text = _read_text(source)
    _verify_hash(op, source_text, [])
    changes: dict[Path, str] = {destination: source_text}
    originals: dict[Path, str | None] = {source: source_text, destination: None}
    deletes = {source}
    if op.payload.get("rewrite_backlinks", False):
        old = _relative(root, source)
        new = _relative(root, destination)
        moved = _rewrite_links(source_text, old, new)
        if moved != source_text:
            changes[destination] = moved
        for path in _collect_markdown(root):
            if path == source:
                continue
            value = _read_text(path)
            rewritten = _rewrite_links(value, old, new)
            if rewritten != value:
                changes[path] = rewritten
                originals[path] = value
    return changes, deletes, originals, _relative(root, destination)


def _merge_index(text: str, source: str, canonical: str) -> str:
    parse_index(text)
    old_slug = Path(source).stem
    canonical_slug = Path(canonical).stem
    lines = text.splitlines(keepends=True)
    has_canonical = any((match := ENTRY_RE.match(_strip_eol(line))) and match.group(1).rsplit("/", 1)[-1] == canonical_slug for line in lines)
    result: list[str] = []
    found = False
    for line in lines:
        match = ENTRY_RE.match(_strip_eol(line))
        if match and match.group(1).rsplit("/", 1)[-1] == old_slug:
            found = True
            if has_canonical:
                continue
            result.append(_rewrite_links(line, source, canonical))
        else:
            result.append(line)
    return "".join(result) if found else text


def _merge_already_applied(root: Path, source: str, canonical: str) -> bool:
    manifest = root / ".manifest.json"
    if manifest.is_file():
        try:
            data = json.loads(_read_text(manifest))
            for row in data.get("page_identity_transitions", []):
                if isinstance(row, dict) and row.get("page_path") == source and row.get("transition") == "merged_into" and row.get("target") == canonical:
                    return True
        except (OSError, json.JSONDecodeError):
            return False
    for path in _collect_markdown(root):
        value = _read_text(path)
        if value != _rewrite_links(value, source, canonical):
            return False
    index = root / "index.md"
    return not index.is_file() or Path(source).stem not in _read_text(index)


def _merge_changes(root: Path, op: MutationOp) -> tuple[dict[Path, str], set[Path], dict[Path, str | None], str, str]:
    payload = op.payload
    source_name = payload.get("obsolete_path", op.selector.get("obsolete_path", op.target))
    canonical_name = payload.get("canonical_path", payload.get("new_target", op.selector.get("canonical_path")))
    if not canonical_name:
        _fail("malformed_payload", "merge_page requires canonical_path")
    source = _target(root, str(source_name))
    canonical = _target(root, str(canonical_name))
    source_rel = _relative(root, source)
    canonical_rel = _relative(root, canonical)
    if source == canonical:
        _fail("identity_ambiguous", "source and canonical page are identical")
    if not source.is_file():
        if canonical.is_file() and _merge_already_applied(root, source_rel, canonical_rel):
            return {}, set(), {}, source_rel, canonical_rel
        _fail("file_not_found", f"obsolete page not found: {source_rel}")
    if not canonical.is_file():
        _fail("file_not_found", f"canonical page not found: {canonical_rel}")
    source_text = _read_text(source)
    canonical_text = _read_text(canonical)
    _verify_hash(op, source_text, [])
    canonical_hash = payload.get("canonical_hash", op.selector.get("canonical_hash"))
    if canonical_hash is not None:
        probe = MutationOp(op.kind, op.target, {"content_hash": canonical_hash}, {})
        _verify_hash(probe, canonical_text, [])
    changes: dict[Path, str] = {}
    originals: dict[Path, str | None] = {source: source_text, canonical: canonical_text}
    canonical_content = payload.get("canonical_content", payload.get("content"))
    deletes = {source}
    if canonical_content is not None and str(canonical_content) != canonical_text:
        changes[canonical] = str(canonical_content)
    if payload.get("rewrite_backlinks", True):
        for path in _collect_markdown(root):
            if path == source:
                continue
            value = _read_text(path)
            rewritten = _rewrite_links(value, source_rel, canonical_rel)
            if rewritten != value:
                changes[path] = rewritten
                originals[path] = value
    index = root / "index.md"
    if index.is_file():
        index_text = _read_text(index)
        rewritten_index = _merge_index(index_text, source_rel, canonical_rel)
        if rewritten_index != index_text:
            changes[index] = rewritten_index
            originals[index] = index_text
    manifest = root / ".manifest.json"
    if manifest.is_file():
        manifest_text = _read_text(manifest)
        rewritten_manifest = _manifest_transition_text(manifest_text, source_rel, "merged_into", canonical_rel, payload.get("reason"), payload.get("timestamp"))
        if rewritten_manifest != manifest_text:
            changes[manifest] = rewritten_manifest
            originals[manifest] = manifest_text
    return changes, deletes, originals, source_rel, canonical_rel


def apply_mutation(vault: str | Path, op: MutationOp | dict[str, Any], *, dry_run: bool = False) -> dict[str, Any]:
    root = Path(vault).resolve()
    if not isinstance(op, MutationOp):
        raw = op if isinstance(op, dict) else {}
        try:
            op = MutationOp.from_dict(raw)
        except MutationError as exc:
            return {
                "status": "rejected",
                "kind": str(raw.get("kind", "")),
                "target": str(raw.get("target", "")),
                "dry_run": dry_run,
                "accepted": False,
                "error": exc.code,
                "detail": exc.detail,
            }
    try:
        _identity_gate(root, op)
        if op.kind == "rename_page":
            changes, deletes, originals, destination = _rename_changes(root, op)
            diff = "".join(
                _diff_for(path, root, originals.get(path) or "", value)
                for path, value in sorted(changes.items(), key=lambda item: str(item[0]))
            )
            diff += "".join(
                _diff_for(path, root, originals.get(path) or "", "")
                for path in sorted(deletes, key=lambda item: str(item))
            )
            if changes or deletes:
                if not dry_run:
                    _atomic_commit(changes, deletes, originals)
                return _accepted(
                    op, dry_run=dry_run, changed=True, diff=diff,
                    new_target=destination,
                    changed_files=sorted({_relative(root, path) for path in set(changes) | deletes}),
                )
            return _accepted(op, dry_run=dry_run, changed=False, diff="", detail="no_op", new_target=destination, changed_files=[])
        if op.kind in {"merge_page", "rename_or_merge_page"}:
            changes, deletes, originals, source, canonical = _merge_changes(root, op)
            diff = "".join(
                _diff_for(path, root, originals.get(path) or "", value)
                for path, value in sorted(changes.items(), key=lambda item: str(item[0]))
            )
            diff += "".join(
                _diff_for(path, root, originals.get(path) or "", "")
                for path in sorted(deletes, key=lambda item: str(item))
            )
            if changes or deletes:
                if not dry_run:
                    _atomic_commit(changes, deletes, originals)
                return _accepted(
                    op, dry_run=dry_run, changed=True, diff=diff,
                    obsolete_path=source, canonical_path=canonical,
                    changed_files=sorted({_relative(root, path) for path in set(changes) | deletes}),
                )
            return _accepted(op, dry_run=dry_run, changed=False, diff="", detail="no_op", obsolete_path=source, canonical_path=canonical, changed_files=[])
        path = _target(root, op.target)
        if op.kind == "delete_file":
            if not path.is_file():
                _fail("file_not_found", f"target file not found: {op.target}")
            current = _read_text(path)
            _verify_hash(op, current, [])
            if not dry_run:
                _atomic_commit({}, {path}, {path: current})
            diff = _diff_for(path, root, current, "")
            return _accepted(op, dry_run=dry_run, changed=True, diff=diff, changed_files=[op.target])
        if not path.is_file():
            _fail("file_not_found", f"target file not found: {op.target}")
        current = _read_text(path)
        result, diff = resolve_mutation(root, op, current)
        if result == current:
            return _accepted(op, dry_run=dry_run, changed=False, diff="", detail="no_op", changed_files=[])
        originals = {path: current}
        if not dry_run:
            _atomic_commit({path: result}, set(), originals)
        return _accepted(op, dry_run=dry_run, changed=True, diff=diff, changed_files=[op.target])
    except MutationError as exc:
        return _rejected(op, dry_run=dry_run, error=exc.code, detail=exc.detail)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return _rejected(op, dry_run=dry_run, error="io_error", detail=str(exc))
    except (TypeError, ValueError) as exc:
        return _rejected(op, dry_run=dry_run, error="malformed_mutation", detail=str(exc))


def validate_non_overlapping(ops: list[MutationOp]) -> list[str]:
    failures: set[str] = set()
    for index, left in enumerate(ops):
        for right in ops[index + 1:]:
            if left.target != right.target:
                continue
            left_path = tuple(left.selector.get("heading_path", ()))
            right_path = tuple(right.selector.get("heading_path", ()))
            if left_path and right_path and (left_path == right_path or left_path[:len(right_path)] == right_path or right_path[:len(left_path)] == left_path):
                failures.add(f"overlap: {left.target}")
                continue
            left_anchor = tuple(left.selector.get("after_heading_path", left.selector.get("before_heading_path", ())))
            right_anchor = tuple(right.selector.get("after_heading_path", right.selector.get("before_heading_path", ())))
            if left.kind == right.kind == "insert_section" and left_anchor and left_anchor == right_anchor:
                failures.add(f"overlap: {left.target}")
    return sorted(failures)


def merge_operations(source: str, canonical: str) -> list[MutationOp]:
    return [
        MutationOp("rewrite_links", source, payload={"old_target": source.rsplit("/", 1)[-1].removesuffix(".md"), "new_target": canonical.rsplit("/", 1)[-1].removesuffix(".md")}),
        MutationOp("update_manifest_identity", ".manifest.json", payload={"page_path": source, "transition": "merged_into", "target": canonical}),
        MutationOp("remove_index_entry", "index.md", selector={"slug": source.rsplit("/", 1)[-1].removesuffix(".md")}),
    ]
