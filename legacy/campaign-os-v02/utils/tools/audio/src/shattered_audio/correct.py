"""Post-transcription corrector helpers: split, merge, audit.

The mechanical half of the corrector pass that runs between
``transcribe-session`` output and the ``transcript-label`` skill. The
transcript CSV is split into a few large parts; one subagent per part fixes
obvious transcription errors in place using that part's own context; the
merge step recombines the parts, refuses structural damage (added/dropped
rows), regenerates siblings, and audits every changed field to a
``.corrections.jsonl`` sidecar diffed script-side — agents just fix, the
script keeps the evidence trail.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

from .autocorrect import Correction, write_autocorrect_log
from .session_transcribe import write_part_csv

_TS = re.compile(r"^\d{2}:\d{2}:\d{2}$")
_MS = re.compile(r"^\d{1,3}$")

AUDITED_FIELDS = ("Speaker", "Text")


def read_transcript_csv(path: Path) -> list[dict]:
    """Read a part/merged transcript CSV back to rows.

    Handles both shapes: write_part_csv's (timestamps quoted) and the legacy
    transcribeX export (timestamps unquoted, so the millisecond comma splits
    Start/End into two fields each — rejoined here).
    """
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            return []
        rows: list[dict] = []
        for rec in reader:
            if not rec:
                continue
            if (
                len(rec) >= len(header) + 2
                and _TS.match(rec[1])
                and _MS.match(rec[2])
                and _TS.match(rec[3])
                and _MS.match(rec[4])
            ):
                rec = [rec[0], f"{rec[1]},{rec[2]}", f"{rec[3]},{rec[4]}", *rec[5:]]
            row = dict(zip(header, rec))
            if len(rec) > len(header):  # stray trailing fields: fold into Text
                row[header[-1]] = ",".join(rec[len(header) - 1 :])
            rows.append(row)
        return rows


def split_transcript_csv(csv_path: Path, parts: int = 4) -> list[Path]:
    """Split the transcript into ``parts`` contiguous CSVs for the fixers.

    Written to ``<csv-dir>/correction-work/<stem>.part-N.csv`` in
    write_part_csv's quoted shape (so a plain DictReader round-trips them).
    """
    rows = read_transcript_csv(csv_path)
    if not rows:
        return []
    parts = max(1, min(parts, len(rows)))
    out_dir = csv_path.parent / "correction-work"
    size = -(-len(rows) // parts)  # ceil
    paths: list[Path] = []
    for n in range(parts):
        chunk = rows[n * size : (n + 1) * size]
        if not chunk:
            break
        p = out_dir / f"{csv_path.stem}.part-{n + 1}.csv"
        write_part_csv(chunk, p)
        paths.append(p)
    return paths


def merge_corrected_parts(
    csv_path: Path, part_paths: list[Path]
) -> tuple[list[dict], list[dict]]:
    """Recombine corrected parts and diff them against the original.

    Returns ``(new_rows, applied)`` where ``applied`` audits every changed
    Speaker/Text field as ``{row_id, field, before, after}``. Raises
    ``ValueError`` if the parts' row IDs don't exactly match the original's
    in order — an agent that dropped, added, or reordered rows corrupted
    the evidence trail, and the merge refuses it.
    """
    original = read_transcript_csv(csv_path)
    corrected: list[dict] = []
    for p in sorted(part_paths):
        corrected.extend(read_transcript_csv(Path(p)))

    if [r["ID"] for r in corrected] != [r["ID"] for r in original]:
        raise ValueError(
            f"row IDs of {len(corrected)} corrected rows do not match the "
            f"original {len(original)} — a part dropped, added, or reordered "
            "rows; refusing to merge"
        )

    applied: list[dict] = []
    for old, new in zip(original, corrected):
        for field in AUDITED_FIELDS:
            if old.get(field, "") != new.get(field, ""):
                applied.append(
                    {
                        "row_id": old["ID"],
                        "field": field,
                        "before": old.get(field, ""),
                        "after": new.get(field, ""),
                    }
                )
    return corrected, applied


def write_correction_log(applied: list[dict], path: Path) -> None:
    """Jsonl audit sidecar — same writer as the autocorrect sidecar."""
    write_autocorrect_log(applied, path)


def suggest_autocorrect_promotions(
    log_paths: list[Path], min_occurrences: int = 2
) -> list[Correction]:
    """Recurring single-token Text fixes across correction sidecars, as
    dictionary entries. Speaker fixes never promote (attribution is
    contextual, not lexical). Proposal only — the caller appends to
    autocorrect.csv on a human yes.
    """
    import json

    counts: dict[tuple[str, str], int] = {}
    for path in log_paths:
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("field") != "Text":
                continue
            before, after = entry.get("before", ""), entry.get("after", "")
            # reduce the row diff to the one changed token pair, if clean
            pair = _changed_token_pair(before, after)
            if pair:
                counts[pair] = counts.get(pair, 0) + 1
    return [
        Correction(wrong=old, right=new)
        for (old, new), n in sorted(counts.items())
        if n >= min_occurrences
    ]


def _changed_token_pair(before: str, after: str) -> tuple[str, str] | None:
    """The single differing word pair between two texts, else None."""
    b, a = before.split(), after.split()
    if len(b) != len(a):
        return None
    diffs = [(x, y) for x, y in zip(b, a) if x != y]
    if len(diffs) != 1:
        return None
    old, new = diffs[0]
    return old.strip(".,!?\"'"), new.strip(".,!?\"'")
