#!/usr/bin/env python3
"""Detect structural context-waste signals (path + metric only).

Per docs/agents/context-waste-method.md §4. Detector only — no body dumps,
no prose scoring, soft gate (exit 0 on scan success).

Usage:
  python3 scripts/context-waste-scan.py
  python3 scripts/context-waste-scan.py --vault wiki --skills .agents/skills
  python3 scripts/context-waste-scan.py --text
  python3 scripts/context-waste-scan.py --include-templates
  python3 scripts/context-waste-scan.py --excerpt
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

VERSION = 1

# S3: oversized skill (~24KB)
SKILL_BYTES_SOFT = 24 * 1024

# S4: oversized page (lines)
ENTITY_LINES_SOFT = 250
ENTITY_LINES_SOFT_PLUS = 400
SESSION_PREP_LINES_SOFT = 220

# S7: Foundry dump-copy span
FOUNDRY_LINES_SOFT = 40
FOUNDRY_TYPES = frozenset({"pc", "npc"})

SKIP_DIR_NAMES = frozenset({"_archive", "_raw", "templates"})
SKIP_PAGE_NAMES = frozenset({"index.md", "log.md", "hot.md", ".manifest.json"})

ENTITY_TYPES = frozenset(
    {
        "pc",
        "npc",
        "faction",
        "location",
        "region",
        "vehicle",
        "item",
        "creature",
        "monster",
        "deity",
        "organization",
        "ship",
        "place",
    }
)

# Affirmative instruction to read/load the whole manifest file.
MANIFEST_INSTRUCT = re.compile(
    r"(?i)(?:\b(?:read|load|cat|open|preload|parse)\b[^\n]{0,120}\.manifest\.json"
    r"|\.manifest\.json[^\n]{0,80}\b(?:into\s+(?:context|chat)|in\s+full|wholesale|whole))"
)
# Nearby forbid: do not / never … whole/full … .manifest.json (and close variants).
MANIFEST_FORBID = re.compile(
    r"(?i)(?:"
    r"(?:do\s*\*?\*?not\*?\*?|don't|never|must\s+not).{0,140}"
    r"(?:whole|full|load|read).{0,80}\.manifest\.json"
    r"|(?:do\s*\*?\*?not\*?\*?|don't|never|must\s+not).{0,60}"
    r"(?:read|load).{0,60}(?:the\s+)?(?:whole\s+)?\.manifest\.json"
    r"|\.manifest\.json.{0,100}(?:token\s+waste|is\s+a\s+bug|wholesale)"
    r"|never\s+load(?:/edit)?\s+the\s+whole"
    r"|whole-file\s+read"
    r"|not\s+(?:load|read)\s+whole"
    r"|loading\s+the\s+full\s+ledger"
    r")"
)

H1_RE = re.compile(r"(?m)^# ")
FOUNDRY_H2_RE = re.compile(r"(?m)^## Foundry\b[^\n]*")
NEXT_H2_RE = re.compile(r"(?m)^## ")
FM_FIELD_RE = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")


def fail(msg: str, code: int = 1) -> int:
    print(msg, file=sys.stderr)
    return code


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (scalar FM fields, body after closing ---)."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}, text
    # Find closing fence after opening ---
    rest = text[3:]
    if rest.startswith("\r\n"):
        rest = rest[2:]
    elif rest.startswith("\n"):
        rest = rest[1:]
    else:
        return {}, text
    match = re.search(r"\n---\s*(?:\n|$)", rest)
    if not match:
        return {}, text
    block = rest[: match.start()]
    body = rest[match.end() :]
    fields: dict[str, str] = {}
    for line in block.splitlines():
        item = FM_FIELD_RE.match(line)
        if item and not line.startswith((" ", "\t", "-")):
            fields[item.group(1)] = item.group(2).strip().strip("\"'")
    return fields, body


def rel_posix(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def should_skip_page(path: Path, vault: Path, include_templates: bool) -> bool:
    try:
        rel_parts = path.resolve().relative_to(vault.resolve()).parts
    except ValueError:
        rel_parts = path.parts
    if path.name in SKIP_PAGE_NAMES:
        return True
    for part in rel_parts[:-1]:
        if part in SKIP_DIR_NAMES:
            if part == "templates" and include_templates:
                continue
            return True
        if part.startswith("_") and part in {"_archive", "_raw"}:
            return True
    return False


def page_line_threshold(fields: dict[str, str], path: Path) -> tuple[int | None, str]:
    """Return (threshold_lines, bucket) or (None, '') if not sized."""
    ptype = fields.get("type", "").lower()
    if ptype == "session-prep":
        return SESSION_PREP_LINES_SOFT, "session-prep"
    if ptype in ENTITY_TYPES:
        return ENTITY_LINES_SOFT, "entity"
    # Path heuristic when type missing/odd
    if "entities" in path.parts:
        return ENTITY_LINES_SOFT, "entity"
    return None, ""


def scan_skill_s1(path: Path, text: str, excerpt: bool) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    lines = text.splitlines()
    seen_patterns: set[str] = set()
    for i, line in enumerate(lines):
        if ".manifest.json" not in line:
            continue
        lo, hi = max(0, i - 2), min(len(lines), i + 3)
        window = "\n".join(lines[lo:hi])
        if not (MANIFEST_INSTRUCT.search(line) or MANIFEST_INSTRUCT.search(window)):
            continue
        if MANIFEST_FORBID.search(window):
            continue
        # Collapse whitespace for metric pattern key
        pattern = re.sub(r"\s+", " ", line.strip())[:160]
        if pattern in seen_patterns:
            continue
        seen_patterns.add(pattern)
        metric: dict[str, Any] = {"pattern": pattern, "line": i + 1}
        if excerpt:
            metric["excerpt"] = line.strip()[:120]
        hits.append(
            {
                "signal": "S1_skill_full_manifest_read",
                "severity": "hard",
                "path": path.as_posix(),
                "metric": metric,
            }
        )
    return hits


def scan_skill_s3(path: Path, nbytes: int) -> dict[str, Any] | None:
    if nbytes <= SKILL_BYTES_SOFT:
        return None
    return {
        "signal": "S3_oversized_skill",
        "severity": "soft",
        "path": path.as_posix(),
        "metric": {"bytes": nbytes, "threshold": SKILL_BYTES_SOFT},
    }


def scan_page(
    path: Path,
    text: str,
    fields: dict[str, str],
    body: str,
    include_templates: bool,
    excerpt: bool,
) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    lines = text.count("\n") + (0 if text.endswith("\n") or text == "" else 1)
    if text == "":
        lines = 0
    nbytes = len(text.encode("utf-8"))
    ptype = fields.get("type", "")

    # S4 oversized page
    threshold, bucket = page_line_threshold(fields, path)
    if threshold is not None and lines > threshold:
        metric: dict[str, Any] = {
            "lines": lines,
            "bytes": nbytes,
            "type": ptype or None,
            "threshold": threshold,
            "bucket": bucket,
        }
        if bucket == "entity" and lines > ENTITY_LINES_SOFT_PLUS:
            metric["soft_plus"] = True
            metric["soft_plus_threshold"] = ENTITY_LINES_SOFT_PLUS
        hits.append(
            {
                "signal": "S4_oversized_page",
                "severity": "soft",
                "path": path.as_posix(),
                "metric": metric,
            }
        )

    # S5 multi-H1 (body only, after FM)
    h1_count = len(H1_RE.findall(body))
    if h1_count > 1:
        metric_s5: dict[str, Any] = {"h1_count": h1_count}
        if excerpt:
            first = next((ln.strip()[:120] for ln in body.splitlines() if ln.startswith("# ")), "")
            if first:
                metric_s5["excerpt"] = first
        hits.append(
            {
                "signal": "S5_multi_h1",
                "severity": "soft",
                "path": path.as_posix(),
                "metric": metric_s5,
            }
        )

    # S7 Foundry dump span — PC/NPC (by type or path)
    is_pc_npc = ptype.lower() in FOUNDRY_TYPES or (
        "entities" in path.parts and ("pc" in path.parts or "npc" in path.parts)
    )
    if is_pc_npc:
        for m in FOUNDRY_H2_RE.finditer(body):
            rest = body[m.end() :]
            nxt = NEXT_H2_RE.search(rest)
            # span = heading line + body lines until next ##
            if nxt:
                span_text = rest[: nxt.start()]
            else:
                span_text = rest
            # +1 for the ## Foundry heading itself
            foundry_lines = span_text.count("\n") + 1
            if foundry_lines > FOUNDRY_LINES_SOFT:
                metric_s7: dict[str, Any] = {"foundry_lines": foundry_lines}
                if excerpt:
                    metric_s7["excerpt"] = m.group(0).strip()[:120]
                hits.append(
                    {
                        "signal": "S7_foundry_dump_span",
                        "severity": "soft",
                        "path": path.as_posix(),
                        "metric": metric_s7,
                    }
                )
    return hits


def iter_skill_files(skills_root: Path) -> list[Path]:
    if not skills_root.is_dir():
        return []
    return sorted(skills_root.glob("*/SKILL.md"))


def iter_vault_pages(vault: Path, include_templates: bool) -> list[Path]:
    if not vault.is_dir():
        return []
    out: list[Path] = []
    for path in sorted(vault.rglob("*.md")):
        if should_skip_page(path, vault, include_templates):
            continue
        # templates bucket only when explicitly included
        if not include_templates and "templates" in path.parts:
            continue
        out.append(path)
    return out


def emit_json(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=False))


def emit_text(hits: list[dict[str, Any]]) -> None:
    for hit in hits:
        metric = json.dumps(hit["metric"], sort_keys=True, separators=(",", ":"))
        print(f"{hit['signal']} {hit['path']} {metric}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Scan skills + vault for structural context-waste signals (path+metric JSON)."
    )
    p.add_argument(
        "root",
        nargs="?",
        default=".",
        type=Path,
        help="repo root (default: .)",
    )
    p.add_argument("--vault", default="wiki", help="vault path relative to root (default: wiki)")
    p.add_argument(
        "--skills",
        default=".agents/skills",
        help="skills root relative to root (default: .agents/skills)",
    )
    p.add_argument(
        "--json",
        dest="fmt",
        action="store_const",
        const="json",
        default="json",
        help="JSON stdout (default)",
    )
    p.add_argument(
        "--text",
        dest="fmt",
        action="store_const",
        const="text",
        help="one-line-per-hit: signal path metric",
    )
    p.add_argument(
        "--include-templates",
        action="store_true",
        help="include wiki/templates (and report multi-H1 scaffolds)",
    )
    p.add_argument(
        "--excerpt",
        action="store_true",
        help="optional ≤120-char excerpt of matching line only (never page body)",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        return fail(f"root is not a directory: {root}")

    vault = (root / args.vault).resolve() if not Path(args.vault).is_absolute() else Path(args.vault).resolve()
    skills = (
        (root / args.skills).resolve()
        if not Path(args.skills).is_absolute()
        else Path(args.skills).resolve()
    )

    hits: list[dict[str, Any]] = []
    skills_scanned = 0
    pages_scanned = 0

    try:
        for skill in iter_skill_files(skills):
            skills_scanned += 1
            rel = rel_posix(root, skill)
            try:
                raw = skill.read_bytes()
                text = raw.decode("utf-8", errors="replace")
            except OSError as exc:
                return fail(f"read failed: {rel}: {exc}")
            for hit in scan_skill_s1(Path(rel), text, args.excerpt):
                hits.append(hit)
            s3 = scan_skill_s3(Path(rel), len(raw))
            if s3:
                hits.append(s3)

        if not vault.is_dir():
            return fail(f"vault is not a directory: {vault}")

        for page in iter_vault_pages(vault, args.include_templates):
            pages_scanned += 1
            rel = rel_posix(root, page)
            try:
                text = page.read_text(encoding="utf-8", errors="replace")
            except OSError as exc:
                return fail(f"read failed: {rel}: {exc}")
            fields, body = split_frontmatter(text)
            for hit in scan_page(
                Path(rel), text, fields, body, args.include_templates, args.excerpt
            ):
                hits.append(hit)
    except OSError as exc:
        return fail(f"IO error: {exc}")

    # Stable order: signal then path
    hits.sort(key=lambda h: (h["signal"], h["path"]))

    payload = {
        "version": VERSION,
        "vault": rel_posix(root, vault) if vault.is_relative_to(root) else str(vault),
        "summary": {
            "skills_scanned": skills_scanned,
            "pages_scanned": pages_scanned,
            "hits": len(hits),
        },
        "hits": hits,
    }

    if args.fmt == "text":
        emit_text(hits)
    else:
        emit_json(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
