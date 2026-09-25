#!/usr/bin/env python3
"""Thin CLI for objective tiktoken counts (issues #86 / #88).

Method of record: docs/agents/token-measurement.md

Examples:
  python3 scripts/token-count.py README.md docs/
  printf 'text' | python3 scripts/token-count.py --stdin
  python3 scripts/token-count.py --sum wiki
  python3 scripts/token-count.py --footprint --vault wiki

Stdout is JSON (default). No file bodies in stdout.

Dual-report transition (method §5): payloads include
`tokens_approx_bytes_div_4` (= total_bytes // 4) as a **temporary deprecated**
field alongside real tiktoken `total_tokens`. Do not use the approx field for
thresholds or anything labeled tokens. It will be removed after remeasure.

`--footprint` sums active vault pages (same skip rules as `--sum`), emits
encoding / totals / file count / warn vs WIKI_TOKEN_WARN_THRESHOLD (tiktoken
only; threshold 0 disables).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.token_count import (  # noqa: E402
    DEFAULT_ENCODING,
    count_file,
    count_text,
    resolve_encoding,
)

# Active vault markdown: skip these directory name segments (method / lint parity).
SKIP_DIR_NAMES = frozenset(
    {".obsidian", "_archive", "_archives", "_raw", "_readouts", "_meta", "templates"}
)


def _rel_to_root(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        try:
            return str(path.resolve().relative_to(Path.cwd().resolve()))
        except ValueError:
            return str(path)


def iter_markdown_pages(root: Path) -> list[Path]:
    """Walk .md under root; skip archive/raw/templates-style dirs and .manifest.json."""
    if not root.is_dir():
        return []
    out: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        if path.name == ".manifest.json":
            continue
        try:
            rel = path.relative_to(root)
        except ValueError:
            continue
        if set(rel.parts) & SKIP_DIR_NAMES:
            continue
        out.append(path)
    return out


def collect_from_path(target: Path, encoding: str) -> list[dict[str, Any]]:
    """Count a file, or expand a directory like --sum."""
    if target.is_file():
        row = count_file(target, encoding=encoding)
        row["path"] = _rel_to_root(target)
        return [row]
    if target.is_dir():
        rows: list[dict[str, Any]] = []
        for page in iter_markdown_pages(target):
            row = count_file(page, encoding=encoding)
            row["path"] = _rel_to_root(page)
            rows.append(row)
        return rows
    return []


def build_payload(
    files: list[dict[str, Any]],
    encoding: str,
    *,
    footprint: bool = False,
) -> dict[str, Any]:
    total_tokens = sum(int(f.get("tokens") or 0) for f in files)
    total_bytes = sum(int(f.get("bytes") or 0) for f in files)
    # Temporary deprecated dual-report (method §5) — NOT tokens.
    approx = total_bytes // 4
    payload: dict[str, Any] = {
        "encoding": encoding,
        "files": files,
        "total_tokens": total_tokens,
        "total_bytes": total_bytes,
        "tokens_approx_bytes_div_4": approx,  # deprecated; tiktoken is authoritative
    }
    if footprint:
        raw_thresh = os.environ.get("WIKI_TOKEN_WARN_THRESHOLD", "100000")
        try:
            threshold = int(raw_thresh)
        except ValueError:
            threshold = 100000
        warn = False if threshold == 0 else total_tokens > threshold
        payload["file_count"] = len(files)
        payload["warn_threshold"] = threshold
        payload["warn"] = warn
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Objective tiktoken counts (JSON). See docs/agents/token-measurement.md",
        epilog="Examples: scripts/token-count.py README.md docs/ | scripts/token-count.py --sum wiki | printf 'text' | scripts/token-count.py --stdin",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="file(s) or directories (dirs expand like --sum)",
    )
    parser.add_argument(
        "--encoding",
        default=None,
        help=f"tiktoken encoding (default: env WIKI_TOKEN_ENCODING or {DEFAULT_ENCODING})",
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help='count text from stdin as a single entry path="-"',
    )
    parser.add_argument(
        "--sum",
        metavar="PATH",
        help="rollup .md files under PATH (file or directory)",
    )
    parser.add_argument(
        "--footprint",
        action="store_true",
        help="vault footprint + WIKI_TOKEN_WARN_THRESHOLD (tiktoken only)",
    )
    parser.add_argument(
        "--vault",
        default="wiki",
        help="vault root for --footprint (default: wiki)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        default=True,
        help="emit JSON (default)",
    )
    args = parser.parse_args(argv)

    encoding = resolve_encoding(args.encoding)
    files: list[dict[str, Any]] = []

    if args.stdin:
        text = sys.stdin.read()
        data = text.encode("utf-8")
        files.append(
            {
                "path": "-",
                "tokens": count_text(text, encoding=encoding),
                "bytes": len(data),
            }
        )
    elif args.footprint:
        vault = Path(args.vault)
        if not vault.is_absolute():
            vault = (Path.cwd() / vault).resolve()
        if not vault.exists():
            sys.stderr.write(f"missing path: {args.vault}\n")
            return 1
        if vault.is_file():
            files = collect_from_path(vault, encoding)
        else:
            files = collect_from_path(vault, encoding)
        payload = build_payload(files, encoding, footprint=True)
        json.dump(payload, sys.stdout, indent=2, sort_keys=False)
        sys.stdout.write("\n")
        return 0
    elif args.sum is not None:
        target = Path(args.sum)
        if not target.is_absolute():
            target = (Path.cwd() / target).resolve()
        if not target.exists():
            sys.stderr.write(f"missing path: {args.sum}\n")
            return 1
        files = collect_from_path(target, encoding)
    else:
        if not args.paths:
            parser.error("provide path(s), --stdin, --sum PATH, or --footprint")
        for raw in args.paths:
            target = Path(raw)
            if not target.is_absolute():
                target = (Path.cwd() / target).resolve()
            if not target.exists():
                sys.stderr.write(f"missing path: {raw}\n")
                return 1
            files.extend(collect_from_path(target, encoding))

    payload = build_payload(files, encoding, footprint=False)
    json.dump(payload, sys.stdout, indent=2, sort_keys=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
