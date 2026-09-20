"""Deterministic per-file checker cache for the agent-facing wiki CLI."""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Mapping, TypedDict, cast

CACHE_NAME = "lint-cache.json"


class CacheEntry(TypedDict):
    """The reusable checker output for one vault-relative file."""

    content_sha256: str
    config_digest: str
    extracts: dict[str, Any]
    results: dict[str, Any]


class LintCache(TypedDict):
    """On-disk lint cache document."""

    config_digest: str
    entries: dict[str, CacheEntry]


def cache_path(vault: str | Path) -> Path:
    """Return the derived cache location for *vault*."""
    return Path(vault).expanduser().resolve() / "_meta" / CACHE_NAME


def sha256_file(path: str | Path) -> str:
    """Hash file bytes without decoding or normalising them."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


# Explicit aliases make the byte-hash seam easy to discover at call sites.
content_sha256 = sha256_file
file_sha256 = sha256_file


def digest_config(config: Any) -> str:
    """Return a stable SHA-256 digest for JSON-compatible checker config."""
    if isinstance(config, bytes):
        payload = config
    else:
        if isinstance(config, os.PathLike):
            config = os.fspath(config)
        payload = json.dumps(
            config,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


config_sha256 = digest_config

RULE_FILES = (
    ".vale.ini",
    ".vale.yaml",
    "tools/lint_wiki.py",
    "scripts/wiki-lint",
    "rules/registry.yml",
    "rules/bundles.yml",
)
RULE_DIRS = ("styles", "wiki/templates/contracts", "tools/creative_lint")
RULE_SUFFIXES = {".ini", ".yml", ".yaml", ".py", ".md"}
SKIP_DIR_NAMES = {"__pycache__", ".git"}


def _repo_relative(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.name


def digest_rules(root: str | Path, extra: Mapping[str, Any] | None = None) -> str:
    """Hash the rules state applied to a lint: Vale, structural sources, contracts, flags."""
    base = Path(root)
    files: dict[str, str] = {}
    for relative in RULE_FILES:
        path = base / relative
        if path.is_file():
            files[_repo_relative(base, path)] = sha256_file(path)
    for relative in RULE_DIRS:
        directory = base / relative
        if not directory.is_dir():
            continue
        for child in sorted(directory.rglob("*")):
            if SKIP_DIR_NAMES.intersection(child.parts) or not child.is_file():
                continue
            if child.suffix.lower() in RULE_SUFFIXES or child.name in {".vale.ini", ".vale.yaml"}:
                files[_repo_relative(base, child)] = sha256_file(child)
    return digest_config({"extra": dict(extra or {}), "files": files})



def _empty_cache() -> LintCache:
    return {"config_digest": "", "entries": {}}


def _relative_key(vault: Path, raw_path: str | Path) -> str:
    root = vault.expanduser().resolve()
    candidate = Path(raw_path).expanduser()
    resolved = candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve()
    try:
        relative = resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"cache path must be vault-relative: {raw_path!s}") from exc
    if not relative.parts:
        raise ValueError("cache path must name a file")
    return relative.as_posix()


def _valid_entry(raw: Any) -> CacheEntry | None:
    if not isinstance(raw, Mapping):
        return None
    content = raw.get("content_sha256")
    config = raw.get("config_digest")
    extracts = raw.get("extracts")
    results = raw.get("results")
    if not all(isinstance(value, str) for value in (content, config)):
        return None
    if not isinstance(extracts, Mapping) or not isinstance(results, Mapping):
        return None
    return cast(CacheEntry, {
        "content_sha256": content,
        "config_digest": config,
        "extracts": dict(extracts),
        "results": dict(results),
    })


def _clean_cache(vault: Path, raw: Any) -> LintCache:
    if not isinstance(raw, Mapping) or not isinstance(raw.get("config_digest"), str):
        return _empty_cache()
    source_entries = raw.get("entries")
    if not isinstance(source_entries, Mapping):
        return _empty_cache()

    entries: dict[str, CacheEntry] = {}
    for raw_path, raw_entry in source_entries.items():
        if not isinstance(raw_path, str):
            continue
        try:
            key = _relative_key(vault, raw_path)
        except (OSError, ValueError):
            continue
        if not (vault / key).is_file():
            continue
        entry = _valid_entry(raw_entry)
        if entry is not None:
            entries[key] = entry
    return {"config_digest": raw["config_digest"], "entries": entries}


def load_cache(vault: str | Path) -> LintCache:
    """Load a cache, returning an empty/pruned cache for absent or bad data."""
    root = Path(vault).expanduser().resolve()
    try:
        raw = json.loads(cache_path(root).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, TypeError):
        return _empty_cache()
    return _clean_cache(root, raw)


def prune_missing(cache: LintCache, vault: str | Path) -> LintCache:
    """Return *cache* without entries whose vault files no longer exist."""
    root = Path(vault).expanduser().resolve()
    return _clean_cache(root, cache)


def save_cache(vault: str | Path, cache: LintCache) -> None:
    """Persist a pruned cache with deterministic JSON and an atomic replacement."""
    root = Path(vault).expanduser().resolve()
    cleaned = prune_missing(cache, root)
    target = cache_path(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(cleaned, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    temporary_name: str | None = None
    try:
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{target.name}.", suffix=".tmp", dir=target.parent
        )
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, target)
        temporary_name = None
    finally:
        if temporary_name is not None:
            try:
                os.unlink(temporary_name)
            except FileNotFoundError:
                pass


def lookup_entry(
    cache: LintCache,
    vault: str | Path,
    path: str | Path,
    config_digest: str,
) -> CacheEntry | None:
    """Return a hit only when both file bytes and checker config still match."""
    root = Path(vault).expanduser().resolve()
    try:
        key = _relative_key(root, path)
        current_hash = sha256_file(root / key)
    except (OSError, ValueError):
        return None
    entry = cache.get("entries", {}).get(key)
    if entry is None or entry.get("content_sha256") != current_hash:
        return None
    if entry.get("config_digest") != config_digest:
        return None
    return entry


def update_entry(
    cache: LintCache,
    vault: str | Path,
    path: str | Path,
    config_digest: str,
    extracts: Mapping[str, Any],
    results: Mapping[str, Any],
) -> CacheEntry:
    """Hash and store one file's checker extracts and results in *cache*."""
    if not isinstance(extracts, Mapping) or not isinstance(results, Mapping):
        raise TypeError("cache extracts and results must be mappings")
    root = Path(vault).expanduser().resolve()
    key = _relative_key(root, path)
    entry: CacheEntry = {
        "content_sha256": sha256_file(root / key),
        "config_digest": config_digest,
        "extracts": dict(extracts),
        "results": dict(results),
    }
    cache.setdefault("entries", {})[key] = entry
    cache["config_digest"] = config_digest
    return entry


# Verbose names are the primary API; these aliases keep integration call sites terse.
get_cached = lookup_entry
put_cached = update_entry
cache_lookup = lookup_entry
cache_update = update_entry
