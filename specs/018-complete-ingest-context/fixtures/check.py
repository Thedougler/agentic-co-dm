#!/usr/bin/env python3
"""Observable complete-ingest-context checks. Not a skill-text snapshot."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "vault"
ENT = VAULT / "entities"
REPORT = (ROOT / "report.md").read_text()
CRACKED = (ENT / "cracked-bell.md").read_text()
VERDIGRIS = (ENT / "verdigris-harbor.md").read_text()
LIGHTHOUSE = (ENT / "lighthouse.md").read_text()
MISS = (ENT / "miss-note.md").read_text()
SOLO = (ENT / "solo.md").read_text()


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def section(name: str) -> str:
    parts = REPORT.split("## ")
    for part in parts:
        if part.startswith(name):
            return part
    fail(f"report missing section {name}")
    return ""


def main() -> int:
    s1 = section("01-primary.md")
    if "complete" not in s1:
        fail("01 primary not complete")
    if "_raw/01-related.md" not in s1 or "origin: staging" not in s1:
        fail("01 missing staging related read")
    if "cracked" not in CRACKED.lower():
        fail("01 compiled page missing related cracked-bell fact")
    if (ENT / "01-related.md").exists() or (ENT / "01-primary.md").exists():
        fail("01 source filed as wiki page")

    s2 = section("02-primary.md")
    if "_raw/02-sibling.md" not in s2 or "legacy/02-old-variant.md" not in s2:
        fail("02 missing staging or legacy read")
    if s2.find("origin: staging") == -1 or s2.find("origin: legacy") == -1:
        fail("02 missing both origins")
    if "verdigris" not in VERDIGRIS.lower():
        fail("02 compiled page missing uncontradicted legacy color")
    if (ENT / "02-old-variant.md").exists():
        fail("02 legacy variant filed as wiki page")

    s3 = section("03-primary.md")
    if "The lighthouse is black." not in LIGHTHOUSE:
        fail("03 newest decision lost")
    if "The lighthouse is white." in LIGHTHOUSE.split("Canon proposal")[0]:
        fail("03 older wording silently preferred")
    if "Canon proposal" not in LIGHTHOUSE or "^[ambiguous]" not in LIGHTHOUSE:
        fail("03 conflict not surfaced")
    if "gulls nest" not in LIGHTHOUSE.lower():
        fail("03 uncontradicted older detail missing")
    if "recency-conflict" not in s3 or "white" not in s3:
        fail("03 recency conflict missing from record")

    s4 = section("04-primary.md")
    if "complete" not in s4:
        fail("04 miss stalled the primary")
    if "missing-ally.md" not in s4 or "misses:" not in s4:
        fail("04 miss not recorded")
    if "party waits" not in MISS.lower():
        fail("04 primary evidence was not compiled")

    s5 = section("05-primary.md")
    if "complete" not in s5:
        fail("05 no-related did not complete")
    if "related-search: nothing" not in s5:
        fail("05 omitted empty related search")
    if "tide pool" not in SOLO.lower():
        fail("05 primary was not compiled")

    sa = section("06-a.md")
    sb = section("06-b.md")
    if "complete" not in sa or "complete" not in sb:
        fail("06 named files not both complete")
    if "06-b.md" not in sa or "origin: staging" not in sa:
        fail("06-a missing related read of 06-b")
    if "no destinations attributed to 06-b" not in sa:
        fail("06-b treated as ingest unit while 06-a open")
    if "after: 06-a.md" not in sb:
        fail("06-b did not wait for 06-a")
    if "entities/second.md" not in sb:
        fail("06-b destinations missing after its turn")

    print("PASS: related reads, recency, misses, sequential non-overlap, ingest record")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
