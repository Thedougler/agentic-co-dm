#!/usr/bin/env python3
"""Low-context access to a vault .manifest.json. Does not load doctrine.

Vault arg is the wiki root (the directory that contains .manifest.json).

Examples:
  python3 scripts/manifest.py stats wiki
  python3 scripts/manifest.py has wiki source-id
  python3 scripts/manifest.py get wiki source-id
  python3 scripts/manifest.py lookup wiki --page entities/npc/example.md
  python3 scripts/manifest.py list wiki --project campaign --limit 20
  python3 scripts/manifest.py --format tsv list wiki --limit 20
  python3 scripts/manifest.py delta wiki --paths-file -
  python3 scripts/manifest.py record wiki source-id --pages entities/npc/example.md
  python3 scripts/manifest.py upsert wiki source-id --json '{"status":"complete"}'
  python3 scripts/manifest.py normalize wiki --dry-run
  python3 scripts/manifest.py tool-pages wiki --tool codex --limit 20
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


def emit_fmt(fmt: str, rows: list[dict[str, Any]]) -> None:
    if fmt == "tsv":
        print("path\tlast_ingested\tpages\tsource_type")
        for row in rows:
            print(f"{row['path']}\t{row['last_ingested']}\t{row['pages']}\t{row.get('source_type') or ''}")
        return
    emit(rows)


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


def page_count(entry: dict[str, Any]) -> int:
    pages: set[str] = set()
    for field in PAGE_FIELDS:
        pages.update(str(item) for item in (entry.get(field) or []))
    return len(pages)


def cmd_list(args: argparse.Namespace) -> int:
    seen: set[str] = set()
    rows: list[dict[str, Any]] = []
    for key, entry, _where in iter_entries(load(args.vault)):
        if key in seen:
            continue
        seen.add(key)
        if args.project and entry.get("project") != args.project:
            continue
        stamp = ingested_stamp(entry)
        if args.since and stamp < args.since:
            continue
        rows.append({"path": key, "last_ingested": stamp, "pages": page_count(entry), "source_type": str(entry.get("source_type") or "")})
    rows.sort(key=lambda row: row["path"])
    if args.limit is not None:
        rows = rows[: args.limit]
    emit_fmt(args.format, rows)
    return 0


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


def source_path(vault: Path, raw: str) -> Path:
    expanded = Path(os.path.expandvars(os.path.expanduser(raw)))
    if expanded.is_absolute():
        return expanded.resolve()
    cwd_path = expanded.resolve()
    vault_path = (vault / expanded).resolve()
    if cwd_path.is_file() or not vault_path.is_file():
        return cwd_path
    return vault_path


def record_source_matches(vault: Path, key: str, source: Path) -> bool:
    candidates = [resolve_path(key)]
    key_path = Path(os.path.expandvars(os.path.expanduser(key)))
    if not key_path.is_absolute():
        candidates.append((vault / key_path).resolve())
    return source in candidates


def normalize_page(vault: Path, raw: str) -> str:
    try:
        return str(resolve_path(raw).relative_to(vault)).replace("\\", "/")
    except ValueError:
        normalized = raw.replace("\\", "/").lstrip("./")
        prefix = f"{vault.name}/"
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix):]
        return normalized


def cmd_record(args: argparse.Namespace) -> int:
    vault = args.vault.resolve()
    source = source_path(vault, args.source)
    if not source.is_file():
        return fail(f"source file not found: {source}")

    try:
        current_hash = file_hash(source)
    except OSError as exc:
        return fail(f"cannot hash source {source}: {exc}")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = load(vault)
    rows = [
        row
        for row in iter_entries(data)
        if record_source_matches(vault, row[0], source)
    ]

    entry: dict[str, Any] = {}
    existing_pages: set[str] = set()
    for _key, old, _where in rows:
        entry = merge_entries(entry, old)
        for field in PAGE_FIELDS:
            existing_pages.update(str(item) for item in (old.get(field) or []))

    pages = {normalize_page(vault, page) for page in args.pages}
    entry["content_hash"] = current_hash
    entry["last_ingested"] = now
    entry["pages_produced"] = sorted(existing_pages | pages)
    if args.source_type is not None:
        entry["source_type"] = args.source_type
    if args.project is not None:
        entry["project"] = args.project

    sources = data.get("sources")
    if not isinstance(sources, dict):
        sources = {}
        data["sources"] = sources
    for key, _old, where in rows:
        if where == "sources":
            sources.pop(key, None)
        else:
            data.pop(key, None)
    canonical = str(source)
    sources[canonical] = entry
    recount_stats(data)
    data["last_updated"] = now
    write(vault, data)
    emit({"key": canonical, "entry": entry, "rows_merged": len(rows)})
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
def cmd_transition(args: argparse.Namespace) -> int:
    repo_root = str(Path(__file__).resolve().parent.parent)
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
    from tools.wiki_ops.manifest_ops import ManifestTransition, apply_transition
    data = load(args.vault)
    transition = ManifestTransition(args.page, args.transition, args.target, args.reason)
    try:
        out = apply_transition(data, transition)
    except ValueError as exc:
        return fail(str(exc), 2)
    write(args.vault, out)
    emit({"status": "applied", "page": args.page, "transition": transition.to_dict()})
    return 0




TOOL_TYPE_MAP = {
    "claude_conversation": "claude",
    "claude_memory": "claude",
    "claude_audit_log": "claude",
    "claude_desktop_session": "claude",
    "codex_rollout": "codex",
    "codex_index": "codex",
    "codex_history": "codex",
    "hermes_memory": "hermes",
    "hermes_session": "hermes",
    "openclaw_memory": "openclaw",
    "openclaw_daily_note": "openclaw",
    "openclaw_session": "openclaw",
    "openclaw_dreams": "openclaw",
    "copilot_session": "copilot",
    "copilot_checkpoint": "copilot",
    "copilot_transcript": "copilot",
    "copilot_memory_artifact": "copilot",
    "pi_session": "pi",
    "document": "ingest",
}


def source_tool(source_type: str) -> str:
    return TOOL_TYPE_MAP.get(source_type, "manual")


def cmd_tool_pages(args: argparse.Namespace) -> int:
    """Compact tool\tpage rows for memory-bridge. CLI loads the ledger; agent sees only this TSV/JSON."""
    rows_out: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for _key, entry, _where in iter_entries(load(args.vault)):
        tool = source_tool(str(entry.get("source_type") or ""))
        if args.tool and tool != args.tool:
            continue
        pages: set[str] = set()
        for field in PAGE_FIELDS:
            pages.update(str(item) for item in (entry.get(field) or []))
        for page in sorted(pages):
            pair = (tool, page)
            if pair in seen:
                continue
            seen.add(pair)
            rows_out.append(pair)
    rows_out.sort(key=lambda row: (row[0], row[1]))
    if args.limit is not None:
        rows_out = rows_out[: args.limit]
    if args.format == "tsv":
        print("tool\tpage")
        for tool, page in rows_out:
            print(f"{tool}\t{page}")
    else:
        emit([{"tool": tool, "page": page} for tool, page in rows_out])
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("json", "tsv"), default="json")
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

    listing = sub.add_parser("list", help="paths, last_ingested, page counts")
    vault_arg(listing)
    listing.add_argument("--project")
    listing.add_argument("--since")
    listing.add_argument("--limit", type=int)
    listing.set_defaults(func=cmd_list)

    delta = sub.add_parser("delta", help="which listed paths need ingest")
    vault_arg(delta)
    delta.add_argument("--paths-file", required=True)
    delta.set_defaults(func=cmd_delta)

    upsert = sub.add_parser("upsert", help="merge one entry")
    vault_arg(upsert)
    upsert.add_argument("source")
    upsert.add_argument("--json", required=True)
    upsert.set_defaults(func=cmd_upsert)

    record = sub.add_parser("record", help="hash and record one completed source atomically")
    vault_arg(record)
    record.add_argument("source")
    record.add_argument("--pages", nargs="+", required=True)
    record.add_argument("--source-type")
    record.add_argument("--project")
    record.set_defaults(func=cmd_record)

    transition = sub.add_parser("transition", help="record a page identity transition")
    vault_arg(transition)
    transition.add_argument("--page", required=True)
    transition.add_argument("--transition", required=True, choices=("merged_into", "renamed_to", "archived"))
    transition.add_argument("--target")
    transition.add_argument("--reason")
    transition.set_defaults(func=cmd_transition)
    normalize = sub.add_parser("normalize", help="merge ~ vs absolute collisions")
    vault_arg(normalize)
    normalize.add_argument("--dry-run", action="store_true")
    normalize.set_defaults(func=cmd_normalize)

    tool_pages = sub.add_parser("tool-pages", help="compact tool\tpage rows for memory-bridge")
    tool_pages.add_argument("vault", type=Path)
    tool_pages.add_argument("--tool", default=None, help="filter to one tool (claude, codex, ...)")
    tool_pages.add_argument("--limit", type=int, default=None)
    tool_pages.set_defaults(func=cmd_tool_pages)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    args.vault = args.vault.expanduser().resolve()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
