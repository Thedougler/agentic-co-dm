#!/usr/bin/env python3
"""Grading aid for theatre-of-the-mind eval output (grader only, never the subject).

usage: python3 scripts/check-narration.py --draft <output.md> [--source <page.md> ...]

--draft   a subject's output.md, or any file holding a narration block; the
          first `[!narration]` callout is checked when there is one
--source  each page or old block the facts came from; copied five-word phrases
          are reported against all of them (quoted speech exempt)

Prints the block, then one lead per line (long sentences, punctuation, paint-chip
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


def narration_text(raw: str) -> str:
    rows = raw.splitlines()
    start = next((i for i, ln in enumerate(rows) if "[!narration]" in ln), None)
    if start is not None:  # first narration callout only, not the notes after it
        end = next((i for i in range(start + 1, len(rows)) if not rows[i].startswith(">")), len(rows))
        rows = rows[start:end]
    lines = [re.sub(r"^>\s?", "", ln) for ln in rows]
    lines = [ln for ln in lines if not ln.strip().startswith("[!")]
    return "\n".join(lines).strip()


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", required=True)
    ap.add_argument("--source", action="append", default=[])
    a = ap.parse_args()
    body = narration_text(Path(a.draft).read_text())
    findings = check(body, a.source)
    print(body, end="\n\n")
    for f in findings:
        print(f"  ! {f}")
    flat = " ".join(body.split())
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", flat) if s]
    print(f"  {'clean' if not findings else f'{len(findings)} leads'}; sentences={len(sentences)} words={len(flat.split())}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
