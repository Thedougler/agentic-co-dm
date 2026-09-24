#!/usr/bin/env python3
"""Grading aid for any eval whose output carries player-facing `[!narration]` prose
(scene openings, beat pages, portraits, recaps). For the grader only, never the subject.

usage: python3 scripts/check-narration.py <file-or-dir> ... [--source <page.md> ...]

paths     subject outputs: files or directories; every `[!narration]` callout
          in every .md is checked (a file with none is checked whole)
--source  each page or old block the facts came from; copied five-word phrases
          are reported against all of them (quoted speech exempt)

Prints each block, then one lead per line (long sentences, punctuation, paint-chip
colors, grid distances, compass legends, labels, copied phrases), then sentence
and word counts. Leads are for the grader to judge, not pass/fail gates: the
skill sets no hard counts. Exit 1 when any lead remains, 0 when clean.
"""
import argparse
import re
import sys
from pathlib import Path

COLORS = (r"(?:gr[ae]y|black|white|green|brown|orange|red|blue|gold|golden|amber|silver|"
          r"pink|yellow|purple|violet|tawny|russet|crimson|scarlet|copper|bronze|teal|turquoise)")
NUMBER = (r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|"
          r"twenty|twenty-five|thirty|forty|fifty|sixty|hundred)")
COMPASS = r"(?:north|south|east|west|northeast|northwest|southeast|southwest)"
PC_PERCEIVE = r"\byou (?:see|notice|spot|realize|realise|feel|sense|recognize|understand)\b"
LABELS = r"\b(?:hub|slack|magnet|live edge|windup|focus image|cold portrait)\b"


def narration_blocks(raw: str) -> list:
    """Every `> [!narration] Title` callout as (title, text); the whole text when there is none."""
    rows, blocks = raw.splitlines(), []
    for i, ln in enumerate(rows):
        m = re.match(r"\s*>\s*\[!narration\][-+]?\s*(.*)", ln)
        if not m:
            continue
        end = next((k for k in range(i + 1, len(rows)) if not rows[k].lstrip().startswith(">")), len(rows))
        body = "\n".join(re.sub(r"^\s*>\s?", "", r) for r in rows[i + 1:end]).strip()
        blocks.append((m.group(1).strip() or "narration", body))
    return blocks or [("text", raw.strip())]


def narration_text(raw: str) -> str:
    return narration_blocks(raw)[0][1]


def grams(text: str, n: int = 5) -> set:
    text = re.sub(r'["“][^"”]*["”]', " ", text)  # quoted speech stays verbatim
    words = re.findall(r"[a-z']+", text.lower())
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def check(body: str, sources: list) -> list:
    findings = []
    flat = " ".join(body.split())
    sentences = [s for s in re.split(r"(?<=[.!?”\"])\s+(?=[A-Z“\"])", flat) if s.strip()]
    paragraphs = [p for p in re.split(r"\n\s*\n", body) if p.strip()]

    for s in sentences:
        if len(s.split()) > 30:
            findings.append(f"long sentence ({len(s.split())} words), split it: {s[:70]}...")
    for p in paragraphs:
        if len(re.split(r"(?<=[.!?])\s+", p.strip())) == 1 and len(paragraphs) > 1:
            findings.append(f"one-sentence paragraph, merge it: {p.strip()[:70]}")
    if len(paragraphs) > 2:
        findings.append(f"{len(paragraphs)} paragraphs; a scene opening is one, two when loaded")
    for ch, name in ((";", "semicolon"), (":", "colon"), ("—", "em dash")):
        if ch in flat:
            findings.append(f"{name} in spoken prose")
    for m in re.findall(rf"\b[a-z]+-{COLORS}\b", flat, re.I):
        findings.append(f"paint-chip color '{m}', use one plain word or a comparison")
    for m in re.findall(rf"\b{NUMBER}[- ](?:foot|feet)\b", flat, re.I):
        findings.append(f"grid distance '{m}', say it in body-scale words unless a player must act on the number now")
    legend = re.findall(rf"(?:^|[.,;]\s+|\band\s+){COMPASS}\s*,", flat, re.I)
    if len(legend) >= 2:
        findings.append(f"directions read as a map legend ({len(legend)} compass-led clauses); hang routes on landmarks")
    for m in re.findall(PC_PERCEIVE, flat, re.I):
        findings.append(f"'{m}' tells the players what their characters perceive; show the thing instead")
    for m in re.findall(LABELS, flat, re.I):
        findings.append(f"'{m}' reads as a page or craft label; give its plain meaning unless it is ordinary speech here")
    if re.search(r"what do you do\??\s*$", flat, re.I):
        findings.append("ends on 'What do you do?'; the DM asks it, the block stops before it")
    mine = grams(flat)
    for src in sources:
        copied = sorted(mine & grams(Path(src).read_text()))
        for g in copied:
            findings.append(f"copied phrase from {Path(src).name}: '{g}'")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", type=Path, help="files or directories (every .md inside)")
    ap.add_argument("--source", action="append", default=[], help="page or old block to check copying against")
    a = ap.parse_args()
    files = [f for p in a.paths for f in (sorted(p.rglob("*.md")) if p.is_dir() else [p])
             if f.name != "process.md"]
    total = 0
    for f in files:
        for title, body in narration_blocks(f.read_text()):
            findings = check(body, a.source)
            total += len(findings)
            flat = " ".join(body.split())
            sentences = [s for s in re.split(r"(?<=[.!?])\s+", flat) if s]
            print(f"=== {f.name} :: {title} (sentences={len(sentences)} words={len(flat.split())})")
            print(body)
            for finding in findings:
                print(f"  ! {finding}")
            print()
    print("clean" if not total else f"{total} leads")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
