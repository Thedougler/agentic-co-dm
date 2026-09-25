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


from . import lint_cache
from .scope import Scope, SKIP_DIRS, _frontmatter

RESERVED_PAGES = {"index.md", "log.md", "hot.md"}


def _is_moc_page(path: Path) -> bool:
    return path.name == "_index.md" or path.stem.endswith("-index")
IDENTITY_BATCH_TIMEOUT_SECONDS = 60


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value).casefold())


def _aliases(fields: dict[str, str]) -> list[str]:
    raw = fields.get("aliases", "")
    if raw.startswith("[") and raw.endswith("]"):
        return [item.strip().strip("\"'") for item in raw[1:-1].split(",") if item.strip()]
    return [raw.strip("\"'")] if raw else []


def _body(text: str) -> str:
    return re.sub(r"\A(?:\ufeff)?---\r?\n.*?\r?\n---\s*(?:\r?\n|$)", "", text, count=1, flags=re.S)



ROW_FIELDS = (
    "size", "mtime_ns", "content_sha256", "stem", "title", "type",
    "aliases", "redirects_to", "body_len", "profile",
)


def _walk(root: Path) -> list[str]:
    """List vault-relative Markdown paths with ``os.scandir`` (stat only, no reads)."""
    found: list[str] = []
    stack = [root]
    while stack:
        directory = stack.pop()
        try:
            entries = list(os.scandir(directory))
        except OSError:
            continue
        for entry in entries:
            if entry.is_dir(follow_symlinks=False):
                if entry.name not in SKIP_DIRS:
                    stack.append(Path(entry.path))
            elif (
                entry.name.endswith(".md")
                and entry.name.casefold() not in RESERVED_PAGES
                and entry.name not in SKIP_DIRS
                and entry.is_file()
            ):
                found.append(Path(entry.path).relative_to(root).as_posix())
    return sorted(found, key=lambda rel: tuple(rel.split("/")))


def _path_for(vault: Path, raw: str, paths: list[str] | None = None) -> Path:
    candidate = (vault / raw).resolve()
    try:
        candidate.relative_to(vault)
    except ValueError as exc:
        raise ValueError(f"path escapes vault: {raw}") from exc
    if candidate.is_file() and candidate.suffix.casefold() == ".md":
        return candidate
    stem = Path(raw).stem.casefold()
    listed = _walk(vault) if paths is None else paths
    matches = [vault / rel for rel in listed if Path(rel).stem.casefold() == stem]
    if len(matches) != 1:
        raise ValueError(f"page not found or ambiguous: {raw}")
    return matches[0]


@dataclass
class PageIdentity:
    path: str
    stem: str
    title: str
    type: str | None = None
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


def _row_fields(path: Path, root: Path) -> tuple[dict[str, Any], str]:
    """Read one page and return its index row (without stat/hash) plus its body."""
    text = path.read_text(encoding="utf-8")
    fields = _frontmatter(text)
    body = _body(text)
    return {
        "stem": path.stem,
        "title": fields.get("title", path.stem).strip("\"'") or path.stem,
        "type": (fields.get("type") or fields.get("kind") or "").strip("\"'") or None,
        "aliases": _aliases(fields),
        "redirects_to": fields.get("redirects_to", "").strip("\"'"),
        "body_len": len(body),
        "profile": dict(Counter(body)),
    }, body


def _index_row(root: Path, rel: str, stat: os.stat_result, sha: str) -> dict[str, Any]:
    row, _ = _row_fields(root / rel, root)
    return {"size": stat.st_size, "mtime_ns": stat.st_mtime_ns, "content_sha256": sha, **row}


def _refresh_index(root: Path, index: dict[str, Any]) -> tuple[list[str], dict[str, int]]:
    """Bring index rows up to date (research R4 steps 1-3); return listed paths and hit counts."""
    paths = _walk(root)
    old = index.get("rows") or {}
    rows: dict[str, dict[str, Any]] = {}
    hits = misses = 0
    for rel in paths:
        if _is_moc_page(Path(rel)):
            continue
        path = root / rel
        stat = path.stat()
        row = old.get(rel)
        valid = isinstance(row, dict) and all(key in row for key in ROW_FIELDS)
        if valid and row["size"] == stat.st_size and row["mtime_ns"] == stat.st_mtime_ns:
            rows[rel] = row
            hits += 1
            continue
        sha = lint_cache.sha256_file(path)
        if valid and row["content_sha256"] == sha:
            rows[rel] = {**row, "size": stat.st_size, "mtime_ns": stat.st_mtime_ns}
            hits += 1
            continue
        rows[rel] = _index_row(root, rel, stat, sha)
        misses += 1
    index["rows"] = rows
    index["manifest_sha256"] = lint_cache.manifest_sha256(root)
    return paths, {"hits": hits, "misses": misses}


def _run_rows(index: dict[str, Any]) -> list[dict[str, Any]]:
    return [{"path": rel, **row} for rel, row in index["rows"].items()]


def _profile(row: dict[str, Any], cache: dict[str, Counter[str]]) -> Counter[str]:
    counter = cache.get(row["path"])
    if counter is None:
        counter = cache[row["path"]] = Counter(row["profile"])
    return counter


def _prefilter(left: dict[str, Any], right: dict[str, Any], profiles: dict[str, Counter[str]]) -> bool:
    if not left["body_len"] or not right["body_len"]:
        return False
    shared = sum((_profile(left, profiles) & _profile(right, profiles)).values())
    return 2 * shared / (left["body_len"] + right["body_len"]) > 0.6


def _pair_key(left: dict[str, Any], right: dict[str, Any]) -> str:
    return "|".join(sorted((left["content_sha256"], right["content_sha256"])))


def _ratio(left: str, right: str) -> float:
    """Full similarity for a pair that already passed the profile prefilter."""
    if not left or not right:
        return 0.0
    matcher = SequenceMatcher(None, left, right)
    if matcher.quick_ratio() <= 0.6:
        return 0.0
    return round(matcher.ratio(), 4)


_SIMILARITY_BODIES: dict[str, str] = {}


def _init_similarity_worker(bodies: dict[str, str]) -> None:
    global _SIMILARITY_BODIES
    _SIMILARITY_BODIES = bodies


def _similarity_batch(pairs: list[tuple[str, str, str]]) -> list[tuple[str, float]]:
    return [(key, _ratio(_SIMILARITY_BODIES[left], _SIMILARITY_BODIES[right])) for key, left, right in pairs]


def _fill_pairs(root: Path, needed: dict[str, tuple[str, str]], pairs: dict[str, float]) -> None:
    """Run SequenceMatcher only for uncached pairs, reading only their bodies (R4 step 6)."""
    missing = [(key, left, right) for key, (left, right) in needed.items() if key not in pairs]
    if not missing:
        return
    bodies: dict[str, str] = {}
    for _, left, right in missing:
        for rel in (left, right):
            if rel not in bodies:
                bodies[rel] = _body((root / rel).read_text(encoding="utf-8"))
    chunks = [missing[start:start + 512] for start in range(0, len(missing), 512)]
    if len(missing) > 2000:
        workers = min(4, os.cpu_count() or 1, len(chunks))
        pool = ProcessPoolExecutor(max_workers=workers, initializer=_init_similarity_worker, initargs=(bodies,))
        try:
            futures = [pool.submit(_similarity_batch, chunk) for chunk in chunks]
            for future in futures:
                for key, similarity in future.result(timeout=IDENTITY_BATCH_TIMEOUT_SECONDS):
                    pairs[key] = similarity
        except Exception:
            terminate = getattr(pool, "terminate_workers", None)
            if terminate:
                terminate()
            else:
                pool.shutdown(wait=False, cancel_futures=True)
        else:
            pool.shutdown()
            return
    for key, left, right in missing:
        if key not in pairs:
            pairs[key] = _ratio(bodies[left], bodies[right])


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
        row["aliases"],
        status,
        sorted(candidates, key=lambda item: item["path"]),
        signals,
    )
    return result


class _Context:
    """Candidate selection over index rows (research R4 steps 4-7)."""

    def __init__(self, root: Path, index: dict[str, Any]) -> None:
        self.root = root
        self.index = index
        self.rows = _run_rows(index)
        self.provenance, self.transitions = _manifest_signals(root)
        self.groups: dict[str, list[dict[str, Any]]] = {}
        for row in self.rows:
            if row["type"] and not row["redirects_to"]:
                self.groups.setdefault(row["type"], []).append(row)
        self.profiles: dict[str, Counter[str]] = {}
        self.compared: set[str] = set()
        self.plans: dict[str, list[tuple[dict[str, Any], dict[str, bool], str | None]]] = {}
        self.needed: dict[str, tuple[str, str]] = {}

    def plan(self, row: dict[str, Any]) -> None:
        """Select candidates from cached fields; queue similarity pairs that passed the prefilter."""
        self.compared.add(row["path"])
        if row["redirects_to"] or not row["type"]:
            return
        row_sources = self.provenance.get(row["path"], set())
        row_target = self.transitions.get(row["path"])
        row_title = _norm(row["title"])
        row_aliases = {_norm(item) for item in row["aliases"]}
        planned = []
        for other in self.groups.get(row["type"], []):
            if other["path"] == row["path"]:
                continue
            title_match = row_title == _norm(other["title"])
            alias_match = row_title in {_norm(item) for item in other["aliases"]} or _norm(other["title"]) in row_aliases
            shared_source = bool(row_sources & self.provenance.get(other["path"], set()))
            merge_match = (
                row_target in {other["path"], other["stem"], f"{other['stem']}.md"}
                or self.transitions.get(other["path"]) == row["path"]
            )
            stem_match = shared_source and SequenceMatcher(
                None, row["stem"].casefold(), other["stem"].casefold()
            ).ratio() > 0.7
            prefilter = _prefilter(row, other, self.profiles)
            if not (title_match or alias_match or stem_match or merge_match or prefilter):
                continue
            key = None
            if prefilter:
                key = _pair_key(row, other)
                # SequenceMatcher is not symmetric: compare in vault path order, as the walk lists pages.
                self.needed[key] = tuple(sorted((row["path"], other["path"]), key=lambda rel: tuple(rel.split("/"))))
            flags = {
                "title_match": title_match,
                "alias_match": alias_match,
                "manifest_provenance": shared_source,
                "merge_history": merge_match,
                "stem_match": stem_match,
            }
            planned.append((other, flags, key))
            self.compared.add(other["path"])
        self.plans[row["path"]] = planned

    def identity(self, row: dict[str, Any]) -> PageIdentity:
        redirect_target = row["redirects_to"]
        if redirect_target:
            canonical = next(
                (
                    item for item in self.rows
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
        pairs = self.index["pairs"]
        candidates: list[dict[str, Any]] = []
        max_similarity = 0.0
        signals: dict[str, Any] = {
            "title_match": False,
            "alias_match": False,
            "manifest_provenance": False,
            "merge_history": False,
            "qmd_content_similarity": 0.0,
        }
        for other, flags, key in self.plans.get(row["path"], []):
            similarity = pairs.get(key, 0.0) if key else 0.0
            if flags["title_match"] or flags["alias_match"] or similarity > 0.6 or flags["stem_match"] or flags["merge_history"]:
                candidates.append(_candidate(other))
                for name in ("title_match", "alias_match", "manifest_provenance", "merge_history"):
                    signals[name] |= flags[name]
                max_similarity = max(max_similarity, similarity)
        signals["qmd_content_similarity"] = max_similarity
        return _identity(row, status="ambiguous" if candidates else "resolved", candidates=candidates, signals=signals)


def _persist(root: Path, persist: bool | None) -> bool:
    return lint_cache.identity_index_path(root).is_file() if persist is None else persist


def resolve_identity(vault: str | Path, path_or_slug: str, *, persist: bool | None = None) -> PageIdentity:
    """Resolve one page from the identity index (mutation gate)."""
    root = Path(vault).resolve()
    if not root.is_dir():
        raise ValueError(f"vault does not exist or is not a directory: {root}")
    index = lint_cache.load_identity_index(root)
    paths, _ = _refresh_index(root, index)
    target = _path_for(root, path_or_slug, paths)
    target_rel = target.relative_to(root).as_posix()
    context = _Context(root, index)
    row = next((item for item in context.rows if item["path"] == target_rel), None)
    if row is None:
        stat = target.stat()
        row = {"path": target_rel, **_index_row(root, target_rel, stat, lint_cache.sha256_file(target))}
    context.plan(row)
    _fill_pairs(root, context.needed, index["pairs"])
    if _persist(root, persist):
        lint_cache.save_identity_index(root, index)
    return context.identity(row)


def scan_identity_report(
    vault: str | Path,
    *,
    scope: Scope | None = None,
    persist: bool | None = None,
) -> tuple[list[PageIdentity], dict[str, Any]]:
    """Scan selected pages from the identity index; return identities and index stats."""
    root = Path(vault).resolve()
    index = lint_cache.load_identity_index(root)
    _, stats = _refresh_index(root, index)
    selected = set(scope.resolved_files) if scope else None
    context = _Context(root, index)
    chosen = [row for row in context.rows if selected is None or row["path"] in selected]
    for row in chosen:
        context.plan(row)
    _fill_pairs(root, context.needed, index["pairs"])
    if _persist(root, persist):
        lint_cache.save_identity_index(root, index)
    results = [context.identity(row) for row in chosen]
    return results, {"scanned": len(chosen), "compared": len(context.compared), "index": stats}


def scan_identities(
    vault: str | Path,
    *,
    scope: Scope | None = None,
    persist: bool | None = None,
) -> list[PageIdentity]:
    return scan_identity_report(vault, scope=scope, persist=persist)[0]
