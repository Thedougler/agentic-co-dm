"""Deterministic page identity resolution before lint or mutation."""
from __future__ import annotations

import json
import os
import re
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


from .scope import Scope, SKIP_DIRS, _frontmatter

RESERVED_PAGES = {"index.md", "log.md", "hot.md"}
IDENTITY_BATCH_TIMEOUT_SECONDS = 60


def _content_similarity(
    left: str,
    right: str,
    left_counts: Counter[str],
    right_counts: Counter[str],
) -> float:
    if not left or not right:
        return 0.0
    if 2 * sum((left_counts & right_counts).values()) / (len(left) + len(right)) <= 0.6:
        return 0.0
    matcher = SequenceMatcher(None, left, right)
    if matcher.quick_ratio() <= 0.6:
        return 0.0
    return round(matcher.ratio(), 4)

_SIMILARITY_ROWS: list[dict[str, Any]] = []
_SIMILARITY_PROFILES: dict[str, Counter[str]] = {}


def _init_similarity_worker(
    rows: list[dict[str, Any]], profiles: dict[str, Counter[str]]
) -> None:
    global _SIMILARITY_ROWS, _SIMILARITY_PROFILES
    _SIMILARITY_ROWS = rows
    _SIMILARITY_PROFILES = profiles


def _similarity_batch(pairs: list[tuple[int, int]]) -> list[tuple[tuple[str, str], float]]:
    return [
        (
            tuple(sorted((_SIMILARITY_ROWS[left]["path"], _SIMILARITY_ROWS[right]["path"]))),
            _content_similarity(
                _SIMILARITY_ROWS[left]["body"],
                _SIMILARITY_ROWS[right]["body"],
                _SIMILARITY_PROFILES[_SIMILARITY_ROWS[left]["path"]],
                _SIMILARITY_PROFILES[_SIMILARITY_ROWS[right]["path"]],
            ),
        )
        for left, right in pairs
    ]

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


def _resolve_row_identity(
    rows: list[dict[str, Any]],
    row: dict[str, Any],
    provenance: dict[str, set[str]],
    transitions: dict[str, str],
    similarity_cache: dict[tuple[str, str], float],
    content_profiles: dict[str, Counter[str]],
) -> PageIdentity:
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
        key = tuple(sorted((row["path"], other["path"])))
        similarity = similarity_cache.get(key)
        if similarity is None:
            similarity = _content_similarity(
                row["body"],
                other["body"],
                content_profiles[row["path"]],
                content_profiles[other["path"]],
            )
            similarity_cache[key] = similarity
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


def _similarity_cache(
    rows: list[dict[str, Any]], profiles: dict[str, Counter[str]]
) -> dict[tuple[str, str], float]:
    cache: dict[tuple[str, str], float] = {}
    candidates: list[tuple[int, int]] = []
    groups: dict[str, list[int]] = {}
    for index, row in enumerate(rows):
        if row["type"] and not row["redirects_to"]:
            groups.setdefault(row["type"], []).append(index)
    for indexes in groups.values():
        for offset, left in enumerate(indexes):
            for right in indexes[offset + 1:]:
                key = tuple(sorted((rows[left]["path"], rows[right]["path"])))
                cache[key] = 0.0
                left_body = rows[left]["body"]
                right_body = rows[right]["body"]
                if left_body and right_body and 2 * sum(
                    (profiles[rows[left]["path"]] & profiles[rows[right]["path"]]).values()
                ) / (len(left_body) + len(right_body)) > 0.6:
                    candidates.append((left, right))
    if not candidates:
        return cache
    chunks = [candidates[start:start + 512] for start in range(0, len(candidates), 512)]
    if len(candidates) > 2000:
        workers = min(4, os.cpu_count() or 1, len(chunks))
        pool = ProcessPoolExecutor(
            max_workers=workers,
            initializer=_init_similarity_worker,
            initargs=(rows, profiles),
        )
        try:
            futures = [pool.submit(_similarity_batch, chunk) for chunk in chunks]
            for future in futures:
                for key, similarity in future.result(timeout=IDENTITY_BATCH_TIMEOUT_SECONDS):
                    cache[key] = similarity
        except Exception:
            terminate = getattr(pool, "terminate_workers", None)
            if terminate:
                terminate()
            else:
                pool.shutdown(wait=False, cancel_futures=True)
        else:
            pool.shutdown()
            return cache
    for chunk in chunks:
        for left, right in chunk:
            key = tuple(sorted((rows[left]["path"], rows[right]["path"])))
            cache[key] = _content_similarity(
                rows[left]["body"],
                rows[right]["body"],
                profiles[rows[left]["path"]],
                profiles[rows[right]["path"]],
            )
    return cache


def resolve_identity(vault: str | Path, path_or_slug: str) -> PageIdentity:
    root = Path(vault).resolve()
    if not root.is_dir():
        raise ValueError(f"vault does not exist or is not a directory: {root}")
    target = _path_for(root, path_or_slug)
    rows = _pages(root)
    target_rel = target.relative_to(root).as_posix()
    row = next((item for item in rows if item["path"] == target_rel), None) or _row(target, root)
    provenance, transitions = _manifest_signals(root)
    profiles = {item["path"]: Counter(item["body"]) for item in rows}
    if row["path"] not in profiles:
        profiles[row["path"]] = Counter(row["body"])
    return _resolve_row_identity(rows, row, provenance, transitions, {}, profiles)


def scan_identities(vault: str | Path, *, scope: Scope | None = None) -> list[PageIdentity]:
    root = Path(vault).resolve()
    rows = _pages(root)
    selected = set(scope.resolved_files) if scope else None
    provenance, transitions = _manifest_signals(root)
    profiles = {item["path"]: Counter(item["body"]) for item in rows}
    similarity_cache = _similarity_cache(rows, profiles)
    return [
        _resolve_row_identity(rows, row, provenance, transitions, similarity_cache, profiles)
        for row in rows
        if selected is None or row["path"] in selected
    ]


