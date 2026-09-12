#!/usr/bin/env python3
"""Observable ingest-polish checks against the fixture vault. Not a skill-text snapshot."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "vault"
SOURCES = ROOT / "sources"
HARBOR = (VAULT / "entities/red-harbor.md").read_text()
GLASS = (VAULT / "entities/tide-glass.md").read_text()
MANIFEST = json.loads((VAULT / ".manifest.json").read_text())
REPORT = (ROOT / "report.md").read_text()


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    entity_names = {p.name for p in (VAULT / "entities").glob("*.md")}
    source_names = {p.name for p in SOURCES.glob("*.md")}
    if entity_names & source_names:
        fail(f"source copied as wiki note: {entity_names & source_names}")

    if "Ila Voss" not in HARBOR:
        fail("existing page missing routed idea (Ila Voss)")
    if HARBOR.lower().count("the lighthouse is white") > 1:
        fail("repeated lighthouse fragment was duplicated")
    if re.search(r"lighthouse is black(?!.*\^\[ambiguous\])", HARBOR, re.I | re.S) and "The lighthouse is white." not in HARBOR:
        fail("conflict silently overwrote lighthouse color")
    if "The lighthouse is white." not in HARBOR:
        fail("settled lighthouse color was lost")
    if "^[ambiguous]" not in HARBOR or "Canon proposal" not in HARBOR:
        fail("conflict was not surfaced as proposal/ambiguity")

    required = ("title:", "category:", "tags:", "sources:", "created:", "updated:", "type:", "lifecycle:", "reveal:")
    if any(field not in GLASS for field in required):
        fail("new page missing required frontmatter")
    if "[[Red Harbor]]" not in GLASS:
        fail("new page missing link to related page")
    if "bell?" in GLASS or (VAULT / "entities/bell.md").exists():
        fail("insufficient fragment was padded into a page")
    staged = VAULT / "_raw/02b-fragment.md"
    if not staged.exists() or "Insufficient scope" not in staged.read_text():
        fail("insufficient fragment was not staged with a reason")

    narration = re.search(r"\[!narration\][^\n]*\n(?P<body>(?:>.*\n)+)", HARBOR)
    spoken = narration.group("body") if narration else ""
    if not spoken:
        fail("missing player-facing narration")
    if re.search(r"\bDC\b|tide ledger", spoken, re.I):
        fail("spoken narration leaked DC or DM secret")
    if "**Wisdom (Perception) — `DC 12`**" not in HARBOR:
        fail("mechanical test missing at-table grammar")
    if "Success →" not in HARBOR or "Failure →" not in HARBOR:
        fail("mechanical test missing consequences")
    if "tide ledger" not in HARBOR.lower() or "[!secret]" not in HARBOR:
        fail("DM-only fact not kept on a secret surface")

    sources = MANIFEST.get("sources", MANIFEST)
    empty_keys = [k for k in sources if "05b-empty" in k]
    if empty_keys:
        fail("empty source marked successfully ingested")
    if "05b-empty.md" not in REPORT or "failed" not in REPORT.lower():
        fail("empty source missing failed report")
    if "outer pier" not in HARBOR.lower():
        fail("readable source was not compiled into the destination")

    print("PASS: routing, preservation, quality, and tracking outcomes hold")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
