"""Deterministic page identity resolution before lint or mutation."""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from .scope import Scope, SKIP_DIRS, _frontmatter

RESERVED_PAGES = {"index.md", "log.md", "hot.md"}


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value).casefold())


def _aliases(fields: dict[str, str]) -> list[str]:
    raw = fields.get("aliases", "")
    if raw.startswith("[") and raw.endswith("]"):
        return [item.strip().strip("\"'") for item in raw[1:-1].split(",") if item.strip()]
    return [raw.strip("\"'")] if raw else []


def _body(text: str) -> str:
    return re.sub(r"\A(?:\ufeff)?---\r?\n.*?\r?\n---\s*(?:\r?\n|$)", "", text, count=1, flags=re.S)


def _path_for(vault: Path, raw: str) -> Path:
    candidate = (vault / raw).resolve()
    try:
        candidate.relative_to(vault)
    except ValueError as exc:
        raise ValueError(f"path escapes vault: {raw}") from exc
    if candidate.is_file() and candidate.suffix.casefold() == ".md":
        return candidate
    stem = Path(raw).stem.casefold()
    matches = [
        path for path in vault.rglob("*.md")
        if path.is_file()
        and path.name.casefold() not in RESERVED_PAGES
        and not SKIP_DIRS.intersection(path.relative_to(vault).parts)
        and path.stem.casefold() == stem
    ]
    if len(matches) != 1:
        raise ValueError(f"page not found or ambiguous: {raw}")
    return matches[0]


@dataclass
class PageIdentity:
    path: str
    stem: str
    title: str
    type: str | None = None
    lifecycle: str | None = None
    aliases: list[str] = field(default_factory=list)
    status: str = "distinct"
    candidates: list[dict[str, Any]] = field(default_factory=list)
    signals: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.status not in {"resolved", "ambiguous", "distinct"}:
            raise ValueError(f"invalid identity status: {self.status}")
        if self.status == "ambiguous" and not self.candidates:
            raise ValueError("ambiguous identity requires candidates")
        for candidate in self.candidates:
            if not candidate.get("path"):
                raise ValueError("identity candidate requires path")
        similarity = self.signals.get("qmd_content_similarity", 0.0)
        if not 0.0 <= float(similarity) <= 1.0:
            raise ValueError("qmd_content_similarity must be between 0.0 and 1.0")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _row(path: Path, root: Path) -> dict[str, Any]:
    rel = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8")
    fields = _frontmatter(text)
    return {
        "path": rel,
        "stem": path.stem,
        "title": fields.get("title", path.stem).strip("\"'") or path.stem,
        "type": (fields.get("type") or fields.get("kind") or "").strip("\"'") or None,
        "lifecycle": (fields.get("lifecycle") or fields.get("status") or "").strip("\"'") or None,
        "aliases": _aliases(fields),
        "redirects_to": fields.get("redirects_to", "").strip("\"'"),
        "body": _body(text),
        "fields": fields,
    }


def _pages(vault: Path) -> list[dict[str, Any]]:
    rows = []
    for path in sorted(vault.rglob("*.md")):
        rel = path.relative_to(vault)
        if (
            not path.is_file()
            or path.name.casefold() in RESERVED_PAGES
            or SKIP_DIRS.intersection(rel.parts)
        ):
            continue
        rows.append(_row(path, vault))
    return rows


def _manifest_signals(vault: Path) -> tuple[dict[str, set[str]], dict[str, str]]:
    path = vault / ".manifest.json"
    if not path.is_file():
        return {}, {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}, {}
    provenance: dict[str, set[str]] = {}
    for source, entry in (data.get("sources") or {}).items():
        if not isinstance(entry, dict):
            continue
        for page in entry.get("pages_produced", []) or []:
            provenance.setdefault(str(page).replace("\\", "/").lstrip("./"), set()).add(str(source))
    transitions: dict[str, str] = {}
    for item in data.get("page_identity_transitions", []) or []:
        if isinstance(item, dict) and item.get("page_path") and item.get("target"):
            transitions[str(item["page_path"])] = str(item["target"])
    return provenance, transitions


def _content_similarity(left: str, right: str) -> float:
    if not left or not right:
        return 0.0
    return round(SequenceMatcher(None, left, right).ratio(), 4)


def _candidate(row: dict[str, Any]) -> dict[str, Any]:
    return {"path": row["path"], "title": row["title"], "type": row["type"]}


def _identity(
    row: dict[str, Any],
    *,
    status: str,
    candidates: list[dict[str, Any]],
    signals: dict[str, Any],
) -> PageIdentity:
    signals.setdefault("qmd_content_similarity", 0.0)
    result = PageIdentity(
        row["path"],
        row["stem"],
        row["title"],
        row["type"],
        row["lifecycle"],
        row["aliases"],
        status,
        sorted(candidates, key=lambda item: item["path"]),
        signals,
    )
    return result


def resolve_identity(vault: str | Path, path_or_slug: str) -> PageIdentity:
    root = Path(vault).resolve()
    if not root.is_dir():
        raise ValueError(f"vault does not exist or is not a directory: {root}")
    target = _path_for(root, path_or_slug)
    rows = _pages(root)
    target_rel = target.relative_to(root).as_posix()
    row = next((item for item in rows if item["path"] == target_rel), None) or _row(target, root)
    provenance, transitions = _manifest_signals(root)
    redirect_target = row["redirects_to"]
    if redirect_target:
        canonical = next(
            (
                item for item in rows
                if item["path"].replace(".md", "").casefold().endswith(
                    redirect_target.replace(".md", "").casefold()
                )
            ),
            None,
        )
        signals = {"redirect_match": bool(canonical), "qmd_content_similarity": 0.0}
        if canonical:
            signals["canonical_path"] = canonical["path"]
        # Preserve legacy reporting for callers, but mutations still reject
        # redirect pages as non-canonical in their safety gate.
        return _identity(row, status="resolved", candidates=[], signals=signals)

    if not row["type"]:
        return _identity(row, status="distinct", candidates=[], signals={"qmd_content_similarity": 0.0})

    candidates: list[dict[str, Any]] = []
    max_similarity = 0.0
    signals: dict[str, Any] = {
        "title_match": False,
        "alias_match": False,
        "manifest_provenance": False,
        "merge_history": False,
        "qmd_content_similarity": 0.0,
    }
    row_sources = provenance.get(row["path"], set())
    row_target = transitions.get(row["path"])
    for other in rows:
        if other["path"] == row["path"] or other["type"] != row["type"] or other["redirects_to"]:
            continue
        title_match = _norm(row["title"]) == _norm(other["title"])
        alias_match = (
            _norm(row["title"]) in {_norm(item) for item in other["aliases"]}
            or _norm(other["title"]) in {_norm(item) for item in row["aliases"]}
        )
        similarity = _content_similarity(row["body"], other["body"])
        shared_source = bool(row_sources & provenance.get(other["path"], set()))
        merge_match = row_target in {other["path"], other["stem"], f"{other['stem']}.md"} or transitions.get(other["path"]) == row["path"]
        stem_similarity = SequenceMatcher(None, row["stem"].casefold(), other["stem"].casefold()).ratio()
        if title_match or alias_match or similarity > 0.6 or (shared_source and stem_similarity > 0.7) or merge_match:
            candidates.append(_candidate(other))
            signals["title_match"] |= title_match
            signals["alias_match"] |= alias_match
            signals["manifest_provenance"] |= shared_source
            signals["merge_history"] |= merge_match
            max_similarity = max(max_similarity, similarity)
    signals["qmd_content_similarity"] = max_similarity
    return _identity(row, status="ambiguous" if candidates else "resolved", candidates=candidates, signals=signals)


def scan_identities(vault: str | Path, *, scope: Scope | None = None) -> list[PageIdentity]:
    root = Path(vault).resolve()
    rows = _pages(root)
    selected = set(scope.resolved_files) if scope else None
    results = []
    for row in rows:
        if selected is not None and row["path"] not in selected:
            continue
        results.append(resolve_identity(root, row["path"]))
    return results
