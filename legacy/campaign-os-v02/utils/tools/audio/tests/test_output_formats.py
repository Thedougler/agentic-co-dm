"""Tests for shattered_audio.output_formats."""

from __future__ import annotations

import csv
import json

import pytest

from shattered_audio.output_formats import FORMATS, write_all, write_csv, write_json, write_md
from shattered_audio.session_transcribe import write_part_csv

ROWS = [
    {"ID": 1, "Start": "00:00:00,000", "End": "00:00:03,120", "Speaker": "DM", "Text": "The dragon guards the bridge."},
    {"ID": 2, "Start": "00:00:03,500", "End": "01:00:05,000", "Speaker": "Nick", "Text": "Not for long."},
]


def test_write_csv_matches_write_part_csv(tmp_path):
    a = tmp_path / "a.csv"
    b = tmp_path / "b.csv"
    write_csv(ROWS, a)
    write_part_csv(ROWS, b)
    assert a.read_bytes() == b.read_bytes()


def test_write_json_is_pretty_array_with_display_timestamps(tmp_path):
    out = tmp_path / "part.json"
    write_json(ROWS, out)
    raw = out.read_text(encoding="utf-8")
    assert raw.startswith("[\n  {")  # pretty-printed array, not JSONL
    got = json.loads(raw)
    assert got == [
        {
            "id": 1,
            "text": "The dragon guards the bridge.",
            "start": "00:00,000",  # zero hour dropped
            "end": "00:03,120",
            "speaker": "DM",
        },
        {
            "id": 2,
            "text": "Not for long.",
            "start": "00:03,500",
            "end": "01:00:05,000",  # non-zero hour kept
            "speaker": "Nick",
        },
    ]


def test_write_md_speaker_blocks(tmp_path):
    out = tmp_path / "session-01-part-00.md"
    write_md(ROWS, out)
    assert out.read_text(encoding="utf-8") == (
        "### session-01-part-00\n"
        "\n"
        "**DM**\n"
        '<span style="color:gray">00:00,000 - 00:03,120</span>\n'
        "\n"
        "The dragon guards the bridge.\n"
        "\n"
        "**Nick**\n"
        '<span style="color:gray">00:03,500 - 01:00:05,000</span>\n'
        "\n"
        "Not for long.\n"
    )


def test_write_all_writes_every_requested_format(tmp_path):
    written = write_all(ROWS, tmp_path, "session-01-part-00", ("csv", "json", "md"))
    assert set(written) == {"csv", "json", "md"}
    for fmt, path in written.items():
        assert path.exists()
        assert path.name == f"session-01-part-00.{FORMATS[fmt][0]}"


def test_write_all_unknown_format_raises_value_error(tmp_path):
    with pytest.raises(ValueError, match="Unknown output format 'xml'"):
        write_all(ROWS, tmp_path, "stem", ("xml",))


def test_write_all_default_is_csv_only(tmp_path):
    written = write_all(ROWS, tmp_path, "stem")
    assert set(written) == {"csv"}


SCENE_ROWS = [
    {**ROWS[0], "Scene": "Pre-session"},
    {**ROWS[1], "Scene": "Scene 01 — Kyzil"},
]


def test_write_json_carries_scene_when_present(tmp_path):
    out = tmp_path / "scenes.json"
    write_json(SCENE_ROWS, out)
    got = json.loads(out.read_text(encoding="utf-8"))
    assert [o["scene"] for o in got] == ["Pre-session", "Scene 01 — Kyzil"]
    # marker-less rows keep the transcribeX shape (no scene key)
    plain = tmp_path / "plain.json"
    write_json(ROWS, plain)
    assert "scene" not in json.loads(plain.read_text(encoding="utf-8"))[0]


def test_write_md_emits_scene_headings_on_change(tmp_path):
    out = tmp_path / "scenes.md"
    rows = [
        {**ROWS[0], "Scene": "Scene 01 — Kyzil"},
        {**ROWS[1], "Scene": "Scene 01 — Kyzil"},  # same scene → no repeat heading
    ]
    write_md(rows, out)
    text = out.read_text(encoding="utf-8")
    assert text.count("## Scene 01 — Kyzil") == 1
    assert text.index("## Scene 01 — Kyzil") < text.index("**DM**")


# --- transcribe_session return-contract regression -------------------------


def test_transcribe_session_return_stays_csv_paths_only(tmp_path, monkeypatch):
    """formats=("csv", "json") must still write both, but return only CSV paths."""
    import shattered_audio.session_transcribe as st

    sdir = tmp_path / "session-07"

    class FakeTrack:
        def __init__(self, mic_id, speaker, parts):
            self.mic_id = mic_id
            self.speaker = speaker
            self.parts = parts

    part_path = tmp_path / "part-000.m4a"
    part_path.write_bytes(b"fake")
    tracks = [FakeTrack("mic00", "DM", [part_path])]

    monkeypatch.setattr(st, "discover_tracks", lambda *a, **kw: tracks)
    monkeypatch.setattr("shattered_audio.record.session_dir", lambda *a, **kw: sdir)

    def fake_transcribe_part(path, model, *, engine="whisper", engine_kwargs=None):
        return [st.Utterance(start=0.0, end=1.0, speaker="", text="hello there")]

    monkeypatch.setattr(st, "_transcribe_part", fake_transcribe_part)

    written = st.transcribe_session(
        7,
        audio_dir=tmp_path,
        use_profiles=False,
        formats=("csv", "json"),
        log=lambda m: None,
    )

    assert len(written) == 1
    assert written[0].suffix == ".csv"
    assert written[0].exists()
    sibling_json = written[0].with_suffix(".json")
    assert sibling_json.exists()

    with open(written[0], newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert rows[0]["Text"] == "hello there"
