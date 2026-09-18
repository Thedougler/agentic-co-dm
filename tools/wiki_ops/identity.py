"""Deterministic page identity resolution."""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from .scope import Scope, SKIP_DIRS, _frontmatter

RESERVED_PAGES = {"index.md", "log.md", "hot.md"}


def _aliases(fields: dict[str, str]) -> list[str]:
    raw = fields.get("aliases", "")
    if raw.startswith("[") and raw.endswith("]"):
        return [item.strip().strip("\"'") for item in raw[1:-1].split(",") if item.strip()]
    return [raw.strip("\"'")] if raw else []


def _body(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def _path_for(vault: Path, raw: str) -> Path:
    candidate = (vault / raw).resolve()
    if vault not in candidate.parents and candidate != vault:
        raise ValueError(f"path escapes vault: {raw}")
    if candidate.is_file():
        return candidate
    stem = Path(raw).stem.casefold()
    matches = [p for p in vault.rglob("*.md") if p.is_file() and p.name.casefold() not in RESERVED_PAGES and not SKIP_DIRS.intersection(p.relative_to(vault).parts) and p.stem.casefold() == stem]
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
    redirects_from: list[str] = field(default_factory=list)
    status: str = "distinct"
    candidates: list[dict[str, Any]] = field(default_factory=list)
    signals: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _pages(vault: Path) -> list[dict[str, Any]]:
    rows = []
    for path in sorted(vault.rglob("*.md")):
        rel = path.relative_to(vault)
        if not path.is_file() or path.name.casefold() in RESERVED_PAGES or SKIP_DIRS.intersection(rel.parts):
            continue
        text = path.read_text(encoding="utf-8")
        fields = _frontmatter(text)
        rows.append({"path": rel.as_posix(), "stem": path.stem, "title": fields.get("title", path.stem), "type": fields.get("type") or fields.get("kind"), "lifecycle": fields.get("lifecycle") or fields.get("status"), "aliases": _aliases(fields), "redirects_to": fields.get("redirects_to", ""), "body": _body(text), "fields": fields})
    return rows


def _identity(row: dict[str, Any], *, status: str, candidates: list[dict[str, Any]], signals: dict[str, Any], redirects_from: list[str] | None = None) -> PageIdentity:
    return PageIdentity(row["path"], row["stem"], row["title"], row["type"], row["lifecycle"], row["aliases"], redirects_from or [], status, candidates, signals)


def resolve_identity(vault: str | Path, path_or_slug: str) -> PageIdentity:
    root = Path(vault).resolve()
    rows = _pages(root)
    target = _path_for(root, path_or_slug)
    row = next(item for item in rows if item["path"] == target.relative_to(root).as_posix())
    redirects_from = [item["path"] for item in rows if item["redirects_to"].strip("\"'").replace(".md", "").casefold().endswith(row["stem"].casefold())]
    redirect_target = row["redirects_to"].strip("\"'")
    if redirect_target:
        canonical = next((item for item in rows if item["path"].replace(".md", "").casefold().endswith(redirect_target.replace(".md", "").casefold())), None)
        if canonical:
            return _identity(row, status="resolved", candidates=[], redirects_from=redirects_from, signals={"redirect_match": True, "canonical_path": canonical["path"]})
    candidates: list[dict[str, Any]] = []
    signals: dict[str, Any] = {"redirect_match": bool(redirects_from)}
    for other in rows:
        if other["path"] == row["path"] or row["type"] != other["type"]:
            continue
        title_match = _norm(row["title"]) == _norm(other["title"])
        alias_match = _norm(row["title"]) in {_norm(item) for item in other["aliases"]} or _norm(other["title"]) in {_norm(item) for item in row["aliases"]}
        overlap = SequenceMatcher(None, row["body"], other["body"]).ratio() if row["body"] and other["body"] else 0.0
        if title_match or alias_match or overlap > 0.6:
            candidates.append({"path": other["path"], "title": other["title"], "type": other["type"]})
            signals.update({"title_match": title_match, "alias_match": alias_match, "content_overlap": round(overlap, 4)})
    status = "ambiguous" if candidates else "resolved"
    return _identity(row, status=status, candidates=candidates, redirects_from=redirects_from, signals=signals)


def scan_identities(vault: str | Path, *, scope: Scope | None = None) -> list[PageIdentity]:
    root = Path(vault).resolve()
    rows = _pages(root)
    selected = set(scope.resolved_files) if scope else None
    results: list[PageIdentity] = []
    for row in rows:
        if selected is not None and row["path"] not in selected:
            continue
        results.append(resolve_identity(root, row["path"]))
    return results
