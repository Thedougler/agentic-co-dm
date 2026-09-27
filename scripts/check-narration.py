#!/usr/bin/env python3
"""Grading aid for any eval whose output carries player-facing `[!narration]` prose
(scene openings, beat pages, portraits, recaps). The subject runs it on its draft (theatre-of-the-mind step 7); the grader runs it on the output.

Examples:
  python3 scripts/check-narration.py output.md
  python3 scripts/check-narration.py output/ --source wiki/entities/npc/example.md

paths     subject outputs: files or directories; every `[!narration]` callout
          in every .md is checked (a file with none is checked whole)
--source  each page or old block the facts came from; copied five-word phrases
          are reported against all of them (quoted speech exempt)

Prints each block, then one lead per line (long sentences, punctuation, paint-chip
colors, grid distances, compass legends, labels, copied phrases), then sentence
and word counts. Leads are for the grader to judge, not pass/fail gates: the
skill sets a word band (80-120, toward 150 for a first arrival, awe, horror, or a
climax), and a portrait, place packet, or recap may rightly run past it. Exit 1 when any lead remains, 0 when clean.
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
COMMON = set("""that this with from into over under your their them they then than when while where
there here have has had been were what which whose will would could should about above below
beyond behind before after around across along against between through toward towards onto
upon each every some more most much many other another only just still even also like
same very once again back away down each both
the and but for you its his her hers are was one two not all out off can may now new own
yet nor too any who how why did does get got see way its ago""".split())
LABELS = r"\b(?:hub|slack|magnet|live edge|reaction point|withheld layer|windup|focus image|cold portrait)\b"


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


def sentence_units(body: str) -> list:
    """Treat immediate-fact bullets as separate sentences for line checks."""
    bullets = [line.strip()[2:].strip() for line in body.splitlines()
               if re.match(r"\s*-\s+", line)]
    if len(bullets) > 1:
        return bullets
    flat = " ".join(body.split())
    return [s for s in re.split(r"(?<=[.!?”\"])\s+(?=[A-Z“\"])", flat) if s.strip()]


def grams(text: str, n: int = 5) -> set:
    text = re.sub(r'["“][^"”]*["”]', " ", text)  # quoted speech stays verbatim
    words = re.findall(r"[a-z']+", text.lower())
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def check(body: str, sources: list) -> list:
    findings = []
    flat = " ".join(body.split())
    sentences = sentence_units(body)
    paragraphs = [p for p in re.split(r"\n\s*\n", body) if p.strip()]

    for s in sentences:
        if len(s.split()) > 30:
            findings.append(f"long sentence ({len(s.split())} words), split it: {s[:70]}...")
    for p in paragraphs:
        if len(re.split(r"(?<=[.!?])\s+", p.strip())) == 1 and len(paragraphs) > 1:
            findings.append(f"one-sentence paragraph, merge it: {p.strip()[:70]}")
    if len(paragraphs) > 1:
        findings.append(f"{len(paragraphs)} paragraphs; a box is one paragraph (a place packet or recap may run longer)")
    words = len(flat.split())
    if words > 150:
        findings.append(f"{words} words; a box is 80-120, toward 150 for a first arrival, awe, horror, or a climax")
    # ponytail: a sentence with no joining word is a standalone fact; most of them = a fact list
    sents = [s for s in re.split(r"(?<=[.!?])\s+", flat.strip()) if s]
    alone = [s for s in sents if not re.search(r"\b(?:and|as|while|until|till|so|when|before|after|then|but|because|where|which|whose|until|though|if)\b", s, re.I)]
    if len(sents) >= 4 and len(alone) * 2 > len(sents):
        findings.append(f"{len(alone)} of {len(sents)} sentences stand alone; this reads as a fact list, so join them into one telling")
    # ponytail: crude stem (drop -s/-es/-ing/-ed); catches "man"/"man's" and "worry"/"worrying"
    stems = {}
    for w in re.findall(r"[a-z]{3,}", flat.lower()):
        if w in COMMON:
            continue
        stems.setdefault(re.sub(r"(?:'s|ing|ed|es|s)$", "", w), []).append(w)
    for group in stems.values():
        if len(group) > 1:
            findings.append(f"'{group[0]}' used {len(group)} times; where it names the same subject, vary the descriptor")
    for ch, name in ((";", "semicolon"), (":", "colon"), ("—", "em dash")):
        if ch in flat:
            findings.append(f"{name} in spoken prose")
    for m in re.findall(rf"\b[a-z]+-{COLORS}\b", flat, re.I):
        findings.append(f"paint-chip color '{m}', use one plain word or a comparison")
    for m in re.findall(rf"\b{NUMBER}[- ](?:foot|feet)\b", flat, re.I):
        findings.append(f"grid distance '{m}', say it in body-scale words unless a player must act on the number now")
    for m in re.findall(rf"\b{COMPASS}\w*", flat, re.I):  # the skill keeps every compass bearing out of speech
        findings.append(f"compass direction '{m}', use one a body knows (ahead, upriver, to your left) or a landmark")
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
            sentences = sentence_units(body)
            print(f"=== {f.name} :: {title} (sentences={len(sentences)} words={len(flat.split())})")
            print(body)
            for finding in findings:
                print(f"  ! {finding}")
            print()
    print("clean" if not total else f"{total} leads")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
