#!/usr/bin/env python3
"""Low-context access to a vault .manifest.json. Does not load doctrine.

Vault arg is the wiki root (the directory that contains .manifest.json).

Usage:
  python3 scripts/manifest.py stats <vault>
  python3 scripts/manifest.py has <vault> <source>
  python3 scripts/manifest.py get <vault> <source>
  python3 scripts/manifest.py lookup <vault> --page <vault-rel-page>
  python3 scripts/manifest.py delta <vault> --paths-file <file|->
  python3 scripts/manifest.py upsert <vault> <source> --json '{...}'
  python3 scripts/manifest.py normalize <vault> [--dry-run]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

META = {"version", "stats", "last_updated", "projects"}
PAGE_FIELDS = ("pages_produced", "pages_created", "pages_updated")


def fail(msg: str, code: int = 1) -> int:
    print(msg, file=sys.stderr)
    return code


def expand(raw: str) -> str:
    return str(Path(os.path.expandvars(os.path.expanduser(raw))).expanduser())


def resolve_path(raw: str) -> Path:
    return Path(expand(raw)).resolve()


def vault_rel(vault: Path, raw: str) -> str | None:
    try:
        return resolve_path(raw).relative_to(vault.resolve()).as_posix()
    except ValueError:
        return None


def load(vault: Path) -> dict[str, Any]:
    path = vault / ".manifest.json"
    if not path.is_file():
        return {"version": 1, "stats": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("manifest is not an object")
    return data


def write(vault: Path, data: dict[str, Any]) -> None:
    path = vault / ".manifest.json"
    tmp = path.with_name(".manifest.json.tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def top_entries(data: dict[str, Any]) -> dict[str, dict]:
    return {
        key: value
        for key, value in data.items()
        if key not in META and key != "sources" and isinstance(value, dict)
    }


def nested_entries(data: dict[str, Any]) -> dict[str, dict]:
    src = data.get("sources")
    if not isinstance(src, dict):
        return {}
    return {key: value for key, value in src.items() if isinstance(value, dict)}


def iter_entries(data: dict[str, Any]) -> list[tuple[str, dict, str]]:
    rows: list[tuple[str, dict, str]] = []
    for key, value in top_entries(data).items():
        rows.append((key, value, "top"))
    for key, value in nested_entries(data).items():
        rows.append((key, value, "sources"))
    return rows


def same_source(left: str, right: str) -> bool:
    if left == right:
        return True
    try:
        return resolve_path(left) == resolve_path(right)
    except OSError:
        return expand(left) == expand(right)


def find_rows(data: dict[str, Any], source: str) -> list[tuple[str, dict, str]]:
    return [row for row in iter_entries(data) if same_source(row[0], source)]


def file_hash(path: Path) -> str:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"sha256:{digest}"


def ingested_stamp(entry: dict[str, Any]) -> str:
    return str(entry.get("last_ingested") or entry.get("ingested_at") or "")


def merge_entries(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    newer, older = (right, left) if ingested_stamp(right) >= ingested_stamp(left) else (left, right)
    out = dict(older)
    out.update(newer)
    for field in PAGE_FIELDS:
        values = []
        seen: set[str] = set()
        for item in list(older.get(field) or []) + list(newer.get(field) or []):
            if item in seen:
                continue
            seen.add(item)
            values.append(item)
        if values:
            out[field] = values
    return out


def recount_stats(data: dict[str, Any]) -> None:
    keys = {row[0] for row in iter_entries(data)}
    pages: set[str] = set()
    for _, entry, _ in iter_entries(data):
        for field in PAGE_FIELDS:
            pages.update(entry.get(field) or [])
    stats = dict(data.get("stats") or {})
    stats["total_sources_ingested"] = len(keys)
    stats["total_pages"] = len(pages)
    data["stats"] = stats
    data.setdefault("version", 1)


def emit(data: Any) -> None:
    print(json.dumps(data, indent=2, sort_keys=True))


def cmd_stats(args: argparse.Namespace) -> int:
    data = load(args.vault)
    rows = iter_entries(data)
    pages: set[str] = set()
    for _, entry, _ in rows:
        for field in PAGE_FIELDS:
            pages.update(entry.get(field) or [])
    emit(
        {
            "sources": len({row[0] for row in rows}),
            "pages": len(pages),
            "stats": data.get("stats") or {},
        }
    )
    return 0


def cmd_has(args: argparse.Namespace) -> int:
    rows = find_rows(load(args.vault), args.source)
    hit = rows[0][0] if rows else None
    emit({"has": bool(rows), "key": hit})
    return 0 if rows else 1


def cmd_get(args: argparse.Namespace) -> int:
    rows = find_rows(load(args.vault), args.source)
    if not rows:
        return fail(f"missing: {args.source}")
    emit({"key": rows[0][0], "entry": rows[0][1]})
    return 0


def page_matches(entry: dict[str, Any], page: str) -> bool:
    want = page.replace("\\", "/").lstrip("./")
    for field in PAGE_FIELDS:
        for item in entry.get(field) or []:
            have = str(item).replace("\\", "/").lstrip("./")
            if have == want or Path(have).name == Path(want).name:
                return True
    return False


def cmd_lookup(args: argparse.Namespace) -> int:
    hits = []
    for key, entry, _where in iter_entries(load(args.vault)):
        if page_matches(entry, args.page):
            hits.append(key)
    emit({"page": args.page, "sources": hits})
    return 0 if hits else 1


def cmd_delta(args: argparse.Namespace) -> int:
    data = load(args.vault)
    raw = sys.stdin.read() if args.paths_file == "-" else Path(args.paths_file).read_text(encoding="utf-8")
    paths = [line.strip() for line in raw.splitlines() if line.strip() and not line.startswith("#")]
    need = []
    current = 0
    for item in paths:
        path = resolve_path(item)
        rows = find_rows(data, item)
        if not rows:
            need.append({"path": item, "reason": "missing"})
            continue
        if not path.is_file():
            need.append({"path": item, "reason": "missing_file"})
            continue
        stored = str(rows[0][1].get("content_hash") or "")
        if stored and stored != file_hash(path):
            need.append({"path": item, "reason": "hash_mismatch"})
            continue
        current += 1
    emit({"need": need, "current": current})
    return 1 if need else 0


def cmd_upsert(args: argparse.Namespace) -> int:
    try:
        patch = json.loads(args.json)
    except json.JSONDecodeError as exc:
        return fail(f"invalid --json: {exc}")
    if not isinstance(patch, dict):
        return fail("--json must be an object")
    vault = args.vault.resolve()
    data = load(vault)
    rows = find_rows(data, args.source)
    if rows:
        key, old, where = rows[0]
        entry = merge_entries(old, patch)
        if where == "sources":
            data.setdefault("sources", {})[key] = entry
        else:
            data[key] = entry
        for extra_key, _entry, extra_where in rows[1:]:
            if extra_where == "sources":
                data["sources"][extra_key] = entry
            else:
                data[extra_key] = entry
        stored = key
    else:
        rel = vault_rel(vault, args.source)
        stored = rel if rel is not None else str(resolve_path(args.source))
        bucket = data.setdefault("sources", {})
        if not isinstance(bucket, dict):
            data["sources"] = {}
            bucket = data["sources"]
        bucket[stored] = patch
    recount_stats(data)
    data["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write(vault, data)
    emit({"key": stored, "entry": find_rows(data, stored)[0][1]})
    return 0


def cmd_normalize(args: argparse.Namespace) -> int:
    data = load(args.vault)
    groups: dict[str, list[tuple[str, dict, str]]] = {}
    for row in iter_entries(data):
        try:
            canon = str(resolve_path(row[0]))
        except OSError:
            canon = expand(row[0])
        groups.setdefault(canon, []).append(row)
    collisions = {key: rows for key, rows in groups.items() if len(rows) > 1}
    plan = [
        {"canonical": key, "keys": [row[0] for row in rows]}
        for key, rows in sorted(collisions.items())
    ]
    if args.dry_run:
        emit({"collisions": plan, "would_merge": len(plan)})
        return 0
    for canon, rows in collisions.items():
        merged = rows[0][1]
        for _key, entry, _where in rows[1:]:
            merged = merge_entries(merged, entry)
        keep_key, _keep_entry, keep_where = rows[0]
        # drop extras, write merged onto the first key
        for key, _entry, where in rows[1:]:
            if where == "sources":
                data.get("sources", {}).pop(key, None)
            else:
                data.pop(key, None)
        if keep_where == "sources":
            data.setdefault("sources", {})[keep_key] = merged
        else:
            data[keep_key] = merged
    recount_stats(data)
    write(args.vault, data)
    emit({"merged": len(plan), "collisions": plan})
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    def vault_arg(p: argparse.ArgumentParser) -> None:
        p.add_argument("vault", type=Path)

    stats = sub.add_parser("stats", help="counts only")
    vault_arg(stats)
    stats.set_defaults(func=cmd_stats)

    has = sub.add_parser("has", help="exit 0 if source is tracked")
    vault_arg(has)
    has.add_argument("source")
    has.set_defaults(func=cmd_has)

    get = sub.add_parser("get", help="one entry")
    vault_arg(get)
    get.add_argument("source")
    get.set_defaults(func=cmd_get)

    lookup = sub.add_parser("lookup", help="sources that list a page")
    vault_arg(lookup)
    lookup.add_argument("--page", required=True)
    lookup.set_defaults(func=cmd_lookup)

    delta = sub.add_parser("delta", help="which listed paths need ingest")
    vault_arg(delta)
    delta.add_argument("--paths-file", required=True)
    delta.set_defaults(func=cmd_delta)

    upsert = sub.add_parser("upsert", help="merge one entry")
    vault_arg(upsert)
    upsert.add_argument("source")
    upsert.add_argument("--json", required=True)
    upsert.set_defaults(func=cmd_upsert)

    normalize = sub.add_parser("normalize", help="merge ~ vs absolute collisions")
    vault_arg(normalize)
    normalize.add_argument("--dry-run", action="store_true")
    normalize.set_defaults(func=cmd_normalize)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    args.vault = args.vault.expanduser().resolve()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
