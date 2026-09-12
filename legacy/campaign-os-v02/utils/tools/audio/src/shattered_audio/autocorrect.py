"""CSV autocorrect dictionary applied post-transcription.

Reads a ``wrong,right[,mode]`` CSV, builds case-insensitive word-boundary
regexes (longest entries first so multi-word phrases pre-empt shorter
overlapping words), and applies them to transcribed CSV rows. Every
application is recorded so the caller can write a jsonl audit log alongside
the part CSV.
"""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Correction:
    wrong: str
    right: str
    mode: str = "word"


def load_dictionary(path: Path, log=None) -> list[Correction]:
    """Load corrections from ``path``; missing file -> ``[]`` (no error).

    Header is ``wrong,right[,mode]``. ``#``-prefixed and blank lines are
    skipped. A row missing ``wrong`` or ``right`` is skipped. Result is
    sorted longest-first (word count desc, then character length desc) so
    multi-word phrases take priority over shorter overlapping entries.
    """
    if not path.exists():
        return []

    corrections: list[Correction] = []
    skipped = 0
    with open(path, newline="", encoding="utf-8") as f:
        lines = [line for line in f if line.strip() and not line.lstrip().startswith("#")]
    reader = csv.DictReader(lines)
    for row in reader:
        wrong = (row.get("wrong") or "").strip()
        right = (row.get("right") or "").strip()
        mode = (row.get("mode") or "").strip() or ("phrase" if " " in wrong else "word")
        if not wrong or not right:
            skipped += 1
            continue
        corrections.append(Correction(wrong=wrong, right=right, mode=mode))

    if skipped and log:
        log(f"autocorrect: skipped {skipped} malformed row(s) in {path}")

    corrections.sort(key=lambda c: (len(c.wrong.split()), len(c.wrong)), reverse=True)
    return corrections


def _apply_case(replacement: str, matched: str) -> str:
    if matched.islower():
        return replacement.lower()
    if matched.isupper():
        return replacement.upper()
    if matched.istitle():
        return " ".join(w.capitalize() for w in replacement.split())
    return replacement


def _compile(corrections: list[Correction]) -> list[tuple[Correction, re.Pattern]]:
    compiled = []
    for c in corrections:
        escaped = re.escape(c.wrong)
        escaped = re.sub(r"\\ ", r"\\s+", escaped)
        pattern = re.compile(rf"\b{escaped}\b", re.IGNORECASE)
        compiled.append((c, pattern))
    return compiled


def apply_corrections(
    rows: list[dict], corrections: list[Correction], log=None
) -> tuple[list[dict], list[dict]]:
    """Apply ``corrections`` to ``rows``' ``Text`` field.

    Never mutates the input rows or list. Returns ``(new_rows, applied)``
    where ``applied`` has one entry per (row, rule) application:
    ``{"row_id", "before", "after", "wrong", "right"}``.
    """
    compiled = _compile(corrections)
    new_rows: list[dict] = []
    applied: list[dict] = []

    for row in rows:
        text = row.get("Text", "")
        before = text
        for correction, pattern in compiled:
            def _sub(m: re.Match) -> str:
                return _apply_case(correction.right, m.group(0))

            new_text, n = pattern.subn(_sub, text)
            if n:
                applied.append(
                    {
                        "row_id": row.get("ID"),
                        "before": before,
                        "after": new_text,
                        "wrong": correction.wrong,
                        "right": correction.right,
                    }
                )
                text = new_text

        if text != row.get("Text", ""):
            new_row = dict(row)
            new_row["Text"] = text
            new_rows.append(new_row)
            if log:
                log(f"autocorrect: row {row.get('ID')}: {before!r} -> {text!r}")
        else:
            new_rows.append(dict(row))

    return new_rows, applied


def write_autocorrect_log(applied: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for entry in applied:
            f.write(json.dumps(entry) + "\n")
