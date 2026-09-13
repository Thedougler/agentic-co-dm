#!/usr/bin/env python3
"""Agent-owned error ledger and sitting log. Not wiki. Does not wrap qmd or git."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
KINDS = ("prep", "wrapup")
TOKEN_COST_NOTE = (
    "Derived from paths/skills/output for same-kind compare — not a tokenizer"
)


def ledger_path(root: Path) -> Path:
    return root / "errors.md"


def sittings_path(root: Path) -> Path:
    return root / "sittings.jsonl"


def load_errors(root: Path) -> list[dict[str, Any]]:
    path = ledger_path(root)
    if not path.exists():
        return []
    entries: list[dict[str, Any]] = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        entries.append(json.loads(line))
    return entries


def write_errors(root: Path, entries: list[dict[str, Any]]) -> None:
    path = ledger_path(root)
    body = "# Error ledger\n"
    if entries:
        body += "\n" + "\n".join(json.dumps(e, sort_keys=True) for e in entries) + "\n"
    path.write_text(body)


def next_error_id(entries: list[dict[str, Any]]) -> str:
    n = 0
    for entry in entries:
        raw = str(entry.get("id", ""))
        if raw.startswith("e-") and raw[2:].isdigit():
            n = max(n, int(raw[2:]))
    return f"e-{n + 1}"


def emit(data: Any, fmt: str) -> None:
    if fmt == "md":
        if isinstance(data, list):
            if not data:
                print("_none_")
                return
            for item in data:
                print(f"- `{json.dumps(item, sort_keys=True)}`")
            return
        print(f"```json\n{json.dumps(data, indent=2, sort_keys=True)}\n```")
        return
    print(json.dumps(data, indent=2, sort_keys=True))


def fail(msg: str, code: int = 2) -> int:
    print(msg, file=sys.stderr)
    return code


def cmd_error_append(args: argparse.Namespace) -> int:
    entries = load_errors(args.root)
    error_id = args.id or next_error_id(entries)
    if any(e.get("id") == error_id for e in entries):
        return fail(f"duplicate id: {error_id}")
    entry = {
        "id": error_id,
        "cause": args.cause,
        "sitting": args.sitting,
        "status": "open",
        "cause_fixed": False,
    }
    entries.append(entry)
    write_errors(args.root, entries)
    emit(entry, args.format)
    return 0


def cmd_error_drain(args: argparse.Namespace) -> int:
    if args.cause_fixed != "true":
        return fail("Drain-without-fix is invalid")
    if not args.id:
        return fail("Bulk-clear is invalid")
    entries = load_errors(args.root)
    match = [e for e in entries if e.get("id") == args.id]
    if not match:
        return fail(f"unknown id: {args.id}")
    remaining = [e for e in entries if e.get("id") != args.id]
    write_errors(args.root, remaining)
    drained = dict(match[0])
    drained["status"] = "drained"
    drained["cause_fixed"] = True
    emit(drained, args.format)
    return 0


def cmd_error_list(args: argparse.Namespace) -> int:
    emit(load_errors(args.root), args.format)
    return 0


def cmd_sitting_record(args: argparse.Namespace) -> int:
    if args.kind not in KINDS:
        return fail(f"kind must be prep or wrapup, got {args.kind!r}")
    jobs = args.job or []
    paths = args.path_read or []
    skills = args.skill or []
    helpers = args.helper or []
    waste = args.waste or []
    errors = args.error or []
    record = {
        "kind": args.kind,
        "jobs": jobs,
        "paths_read": paths,
        "skills_loaded": skills,
        "helpers_used": helpers,
        "waste_named": waste,
        "errors_filled": errors,
        "token_cost": {
            "paths_read": len(paths),
            "skills_loaded": len(skills),
            "jobs": len(jobs),
            "helpers_used": len(helpers),
            "note": TOKEN_COST_NOTE,
        },
        "status": "recorded",
    }
    path = sittings_path(args.root)
    with path.open("a") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")
    emit(record, args.format)
    return 0


def cmd_sitting_list(args: argparse.Namespace) -> int:
    path = sittings_path(args.root)
    if not path.exists():
        emit([], args.format)
        return 0
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    emit(rows, args.format)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=REPO_ROOT,
        help="Directory that holds errors.md and sittings.jsonl",
    )
    parser.add_argument(
        "--format",
        choices=("json", "md"),
        default="json",
        help="JSON or Markdown out",
    )
    sub = parser.add_subparsers(dest="group", required=True)

    error = sub.add_parser("error", help="Fill or drain errors.md")
    error_sub = error.add_subparsers(dest="action", required=True)

    append = error_sub.add_parser("append", help="Append an open error entry")
    append.add_argument("--id", help="Stable id (generated if omitted)")
    append.add_argument("--cause", required=True)
    append.add_argument("--sitting", required=True)
    append.set_defaults(func=cmd_error_append)

    drain = error_sub.add_parser("drain", help="Remove one entry whose cause is fixed")
    drain.add_argument("--id", required=True)
    drain.add_argument(
        "--cause-fixed",
        choices=("true", "false"),
        default="false",
        help="Drain requires true",
    )
    drain.set_defaults(func=cmd_error_drain)

    listed = error_sub.add_parser("list", help="List open error entries")
    listed.set_defaults(func=cmd_error_list)

    sitting = sub.add_parser("sitting", help="Record finished prep/wrapup sittings")
    sitting_sub = sitting.add_subparsers(dest="action", required=True)

    record = sitting_sub.add_parser("record", help="Append a recorded sitting")
    record.add_argument("--kind", required=True, choices=KINDS)
    record.add_argument("--job", action="append", dest="job")
    record.add_argument("--path-read", action="append", dest="path_read")
    record.add_argument("--skill", action="append", dest="skill")
    record.add_argument("--helper", action="append", dest="helper")
    record.add_argument("--waste", action="append", dest="waste")
    record.add_argument("--error", action="append", dest="error")
    record.set_defaults(func=cmd_sitting_record)

    sitting_list = sitting_sub.add_parser("list", help="List recorded sittings")
    sitting_list.set_defaults(func=cmd_sitting_list)

    return parser


def _hoist_parent_flags(argv: list[str]) -> list[str]:
    """Move --root/--format ahead of subcommands so either order works."""
    parent = {"--format", "--root"}
    hoisted: list[str] = []
    rest: list[str] = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg in parent and i + 1 < len(argv):
            hoisted.extend([arg, argv[i + 1]])
            i += 2
            continue
        if arg.startswith("--format=") or arg.startswith("--root="):
            hoisted.append(arg)
            i += 1
            continue
        rest.append(arg)
        i += 1
    return hoisted + rest


def main(argv: list[str] | None = None) -> int:
    raw = list(sys.argv[1:] if argv is None else argv)
    args = build_parser().parse_args(_hoist_parent_flags(raw))
    args.root = args.root.resolve()
    args.root.mkdir(parents=True, exist_ok=True)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
