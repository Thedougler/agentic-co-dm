"""Multi-format output for session transcripts.

``transcribe_session`` always writes the CSV (via :func:`write_part_csv`) and
optionally writes sibling files in other formats next to it — ``.json`` and
``.md`` today, matching the shapes transcribeX emits. All writers take the same
``rows`` shape produced by
:func:`shattered_audio.session_transcribe.merge_part_utterances` (dicts with
``ID``, ``Start``, ``End``, ``Speaker``, ``Text`` — ``Start``/``End`` already
formatted as SRT-style ``HH:MM:SS,mmm`` by
:func:`shattered_audio.session_transcribe.fmt_timestamp`).
"""

from __future__ import annotations

import json
from pathlib import Path

from .session_transcribe import write_part_csv


def _display_ts(ts: str) -> str:
    """transcribeX's json/md drop the hour field while it is zero: ``MM:SS,mmm``."""
    return ts[3:] if ts.startswith("00:") else ts


def write_csv(rows: list[dict], out_path: Path) -> None:
    """Write ``rows`` as the standard part CSV (delegates to write_part_csv)."""
    write_part_csv(rows, out_path)


def write_json(rows: list[dict], out_path: Path) -> None:
    """Write ``rows`` as one pretty-printed JSON array of utterance objects."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = []
    for row in rows:
        obj = {
            "id": row["ID"],
            "text": row["Text"],
            "start": _display_ts(row["Start"]),
            "end": _display_ts(row["End"]),
            "speaker": row["Speaker"],
        }
        # Scene tag is additive (present only when the session recorded
        # scene markers) — marker-less sessions keep the transcribeX shape.
        if "Scene" in row:
            obj["scene"] = row["Scene"]
        data.append(obj)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def write_md(rows: list[dict], out_path: Path) -> None:
    """Write ``rows`` as speaker blocks under a ``### <stem>`` heading.

    Each utterance renders as::

        **Speaker**
        <span style="color:gray">MM:SS,mmm - MM:SS,mmm</span>

        text
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    blocks = [f"### {out_path.stem}"]
    # Scene headings are emitted on scene change when rows carry a Scene tag
    # (sessions recorded with scene markers) — downstream slicing keys off
    # these `## <scene>` lines.
    current_scene: str | None = None
    for row in rows:
        scene = row.get("Scene")
        if scene and scene != current_scene:
            current_scene = scene
            blocks.append(f"## {scene}")
        blocks.append(
            f"**{row['Speaker']}**\n"
            f'<span style="color:gray">{_display_ts(row["Start"])} - {_display_ts(row["End"])}</span>\n'
            f"\n{row['Text']}"
        )
    out_path.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")


FORMATS = {
    "csv": ("csv", write_csv),
    "json": ("json", write_json),
    "md": ("md", write_md),
}


def write_all(
    rows: list[dict],
    out_dir: Path,
    stem: str,
    formats: tuple[str, ...] = ("csv",),
) -> dict[str, Path]:
    """Write ``rows`` to ``out_dir/<stem>.<ext>`` for each format in ``formats``.

    Returns a ``{format: path}`` map. Raises ``ValueError`` for an unknown
    format name.
    """
    written: dict[str, Path] = {}
    for fmt in formats:
        entry = FORMATS.get(fmt)
        if entry is None:
            raise ValueError(
                f"Unknown output format {fmt!r}; expected one of: {', '.join(sorted(FORMATS))}"
            )
        ext, writer = entry
        out_path = out_dir / f"{stem}.{ext}"
        writer(rows, out_path)
        written[fmt] = out_path
    return written
