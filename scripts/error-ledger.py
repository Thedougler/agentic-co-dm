#!/usr/bin/env python3
"""Agent-owned error ledger and sitting log. Not wiki. Does not wrap qmd or git.

errors.md holds open entries only, one JSON object per line: {id, cause, source,
evidence: [{sitting, detail}]}. append attaches to the entry with the same source
and identical trimmed cause, else creates one; --attach e-N attaches a differently
worded cause of the same root (AGENTS.md "Error ledger"); detach undoes an attach;
drain removes the entry in the same commit as the verified fix.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.wiki_ops.cli import repo_root  # noqa: E402

REPO_ROOT = repo_root(Path(__file__).resolve().parent)
APPEND_EXAMPLE = 'python3 scripts/error-ledger.py error append --source .vale.ini --cause "…" --sitting "lint: …"'
EXAMPLES = f"""Examples:
  {APPEND_EXAMPLE}
  python3 scripts/error-ledger.py error append --source .vale.ini --cause "…" --sitting "lint: …" --attach e-212
  python3 scripts/error-ledger.py error detach --id e-212 --index 1
  python3 scripts/error-ledger.py error drain --id e-212
  python3 scripts/error-ledger.py error list
"""
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


def refuse(error: str, hint: str, example: str) -> int:
    """The FR-035 error object: JSON on stdout, the message on stderr, exit 2, nothing written."""
    print(json.dumps({"status": "error", "error": error, "hint": hint, "example": example}, sort_keys=True))
    print(f"error-ledger: {error}", file=sys.stderr)
    return 2


def fail(msg: str, code: int = 2) -> int:
    print(msg, file=sys.stderr)
    return code


def source_ok(source: str) -> bool:
    """A source is an existing repo-relative path or external:<name> (a deterministic check)."""
    if source.startswith("external:"):
        return len(source) > len("external:")
    return bool(source) and not Path(source).is_absolute() and (REPO_ROOT / source).exists()


def cmd_error_append(args: argparse.Namespace) -> int:
    if not source_ok(args.source):
        return refuse(f"source not found: {args.source}", "--source is a repo-relative path that exists, or external:<name>",
                      APPEND_EXAMPLE)
    entries = load_errors(args.root)
    occurrence = {"sitting": args.sitting, "detail": args.detail or args.cause.strip()}
    if args.attach:
        target = next((e for e in entries if e.get("id") == args.attach), None)
        if target is None or target.get("source") != args.source:
            have = target.get("source") if target else "none (unknown id)"
            return refuse(f"source mismatch: {args.attach} has source {have}, got {args.source}",
                          "attach only within one source; omit --attach to create an entry",
                          f'python3 scripts/error-ledger.py error append --source {have if target else "<X>"} '
                          f'--cause "…" --sitting "…" --attach {args.attach}')
    else:  # the only automatic match: same source, identical trimmed cause (FR-007)
        target = next((e for e in entries if e.get("source") == args.source
                       and str(e.get("cause", "")).strip() == args.cause.strip()), None)
    if target is not None:
        evidence = target["evidence"]
        if occurrence in evidence:
            result = {"status": "already_done", "id": target["id"], "occurrence_index": evidence.index(occurrence),
                      "occurrences": len(evidence)}
        else:
            result = {"status": "attached", "id": target["id"], "occurrence_index": len(evidence),
                      "occurrences": len(evidence) + 1}
            if not args.dry_run:
                evidence.append(occurrence)
    else:
        target = {"id": next_error_id(entries), "cause": args.cause, "source": args.source, "evidence": [occurrence]}
        result = {"status": "created", "id": target["id"], "occurrence_index": 0, "occurrences": 1}
        if not args.dry_run:
            entries.append(target)
    if args.dry_run:
        result = {"status": "planned", "planned": [result], "id": result["id"]}
    elif result["status"] != "already_done":
        write_errors(args.root, entries)
    emit(result, args.format)
    return 0


def cmd_error_drain(args: argparse.Namespace) -> int:
    entries = load_errors(args.root)
    if not any(e.get("id") == args.id for e in entries):
        emit({"status": "already_done", "id": args.id}, args.format)
        return 0
    result = {"status": "drained", "id": args.id}
    if args.dry_run:
        result = {"status": "planned", "planned": [result], "id": args.id}
    else:
        write_errors(args.root, [e for e in entries if e.get("id") != args.id])
    emit(result, args.format)
    return 0


def cmd_error_detach(args: argparse.Namespace) -> int:
    entries = load_errors(args.root)
    target = next((e for e in entries if e.get("id") == args.id), None)
    evidence = target["evidence"] if target else []
    if target is None or not 0 <= args.index < len(evidence):
        emit({"status": "already_done", "id": args.id, "occurrences": len(evidence)}, args.format)
        return 0
    if len(evidence) == 1:
        return refuse(f"{args.id} has only one occurrence", "use drain to remove the entry",
                      f"python3 scripts/error-ledger.py error drain --id {args.id}")
    result = {"status": "detached", "id": args.id, "occurrences": len(evidence) - 1}
    if args.dry_run:
        result = {"status": "planned", "planned": [result], "id": args.id}
    else:
        del evidence[args.index]
        write_errors(args.root, entries)
    emit(result, args.format)
    return 0


def cmd_error_list(args: argparse.Namespace) -> int:
    entries = load_errors(args.root)
    if args.ids_only:
        print("\n".join(str(e.get("id")) for e in entries))
        return 0
    by_sitting: dict[str, int] = {}
    for entry in entries:  # FR-009: every occurrence after the first is a recurrence
        for occ in entry.get("evidence", [])[1:]:
            by_sitting[occ["sitting"]] = by_sitting.get(occ["sitting"], 0) + 1
    missing = [e.get("id") for e in entries if not source_ok(str(e.get("source", "")))]
    emit({"entries": entries, "recurrence": {"total": sum(by_sitting.values()), "by_sitting": by_sitting},
          "missing_sources": missing}, args.format)
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


class _Parser(argparse.ArgumentParser):
    """Usage errors print the FR-035 error object (exit 2) plus the message on stderr."""

    def error(self, message: str) -> None:  # type: ignore[override]
        raise SystemExit(refuse(message, f"run {self.prog} --help", APPEND_EXAMPLE))


def build_parser() -> argparse.ArgumentParser:
    parser = _Parser(description=__doc__, epilog=EXAMPLES, formatter_class=argparse.RawDescriptionHelpFormatter)
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
    sub = parser.add_subparsers(dest="group", required=True, parser_class=_Parser)

    error = sub.add_parser("error", help="Fill or drain errors.md", epilog=EXAMPLES,
                           formatter_class=argparse.RawDescriptionHelpFormatter)
    error_sub = error.add_subparsers(dest="action", required=True, parser_class=_Parser)

    append = error_sub.add_parser("append", help="Record an occurrence: attach to the matching entry or create one",
                                  epilog=EXAMPLES, formatter_class=argparse.RawDescriptionHelpFormatter)
    append.add_argument("--source", required=True, help="repo-relative path the fix lands in, or external:<name>")
    append.add_argument("--cause", required=True, help="root cause; never rewritten once recorded")
    append.add_argument("--sitting", required=True, help="sitting label, as in sittings.jsonl")
    append.add_argument("--detail", help="this occurrence (default: the cause)")
    append.add_argument("--attach", metavar="e-N", help="same root cause as e-N (same source only)")
    append.add_argument("--dry-run", action="store_true")
    append.set_defaults(func=cmd_error_append)

    drain = error_sub.add_parser("drain", help="Remove an entry, in the same commit as its verified fix")
    drain.add_argument("--id", required=True)
    drain.add_argument("--dry-run", action="store_true")
    drain.set_defaults(func=cmd_error_drain)

    detach = error_sub.add_parser("detach", help="Undo an attach: remove occurrence k from e-N")
    detach.add_argument("--id", required=True)
    detach.add_argument("--index", type=int, required=True, help="occurrence_index that append reported")
    detach.add_argument("--dry-run", action="store_true")
    detach.set_defaults(func=cmd_error_detach)

    listed = error_sub.add_parser("list", help="Open entries, recurrence, and entries whose source is gone")
    listed.add_argument("--ids-only", action="store_true")
    listed.set_defaults(func=cmd_error_list)

    sitting = sub.add_parser("sitting", help="Record finished prep/wrapup sittings")
    sitting_sub = sitting.add_subparsers(dest="action", required=True, parser_class=_Parser)

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
    if any(arg == "--cause-fixed" or arg.startswith("--cause-fixed=") for arg in raw):
        return refuse("--cause-fixed was removed", "drain removes the entry; no flag needed",
                      "python3 scripts/error-ledger.py error drain --id e-212")
    args = build_parser().parse_args(_hoist_parent_flags(raw))
    args.root = args.root.resolve()
    args.root.mkdir(parents=True, exist_ok=True)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
