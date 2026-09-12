"""Tests for the per-mic → per-part-CSV session transcription logic."""

from __future__ import annotations

import csv
import json
import shutil
import subprocess

import pytest

from shattered_audio.session_transcribe import (
    Utterance,
    apply_speaker_map,
    assign_scene,
    concat_track_parts,
    discover_tracks,
    fmt_timestamp,
    load_scene_markers,
    merge_part_utterances,
    resolve_speaker,
    scene_display,
    write_part_csv,
)


def _make_session(tmp_path, manifest, layout):
    """layout: {mic_id: [part_filenames]} — create empty m4a placeholders.

    Builds the new packet layout: capture artifacts live under ``<sdir>/audio/``
    (``audio/manifest.json`` + ``audio/raw/<mic_id>/``).
    """
    sdir = tmp_path / "session-07"
    audio = sdir / "audio"
    (audio / "raw").mkdir(parents=True)
    (audio / "manifest.json").write_text(json.dumps(manifest))
    for mic_id, parts in layout.items():
        d = audio / "raw" / mic_id
        d.mkdir(parents=True)
        for p in parts:
            (d / p).write_bytes(b"\x00")
    return sdir


def test_fmt_timestamp_is_srt_style():
    assert fmt_timestamp(0) == "00:00:00,000"
    assert fmt_timestamp(5.25) == "00:00:05,250"
    assert fmt_timestamp(65.519) == "00:01:05,519"
    assert fmt_timestamp(900) == "00:15:00,000"
    assert fmt_timestamp(3 * 3600 + 62 + 0.001) == "03:01:02,001"


def test_discover_tracks_reads_manifest_and_orders_parts(tmp_path):
    manifest = {
        "session": 7,
        "segment_seconds": 900,
        "mics": [
            {"mic_id": "mic00", "index": 0, "name": "Built-in", "speaker": "DM"},
            {"mic_id": "mic01", "index": 1, "name": "USB", "speaker": "Nick"},
        ],
    }
    sdir = _make_session(
        tmp_path,
        manifest,
        {"dm-mic": ["part-001.m4a", "part-000.m4a"], "player-mic": ["part-000.m4a"]},
    )
    tracks = discover_tracks(sdir)
    # mic_id stays in positional manifest form; on-disk dirs are role-named
    assert [t.mic_id for t in tracks] == ["mic00", "mic01"]
    assert tracks[0].speaker == "DM"
    # parts sorted by name regardless of creation order
    assert [p.name for p in tracks[0].parts] == ["part-000.m4a", "part-001.m4a"]


def test_discover_tracks_without_manifest_treats_loose_parts_as_one_mic(tmp_path):
    sdir = tmp_path / "session-09"
    parts_dir = sdir / "audio" / "parts"
    parts_dir.mkdir(parents=True)
    (parts_dir / "session-09-part-00.m4a").write_bytes(b"\x00")
    tracks = discover_tracks(sdir)
    assert len(tracks) == 1
    assert tracks[0].speaker is None
    assert [p.name for p in tracks[0].parts] == ["session-09-part-00.m4a"]


def test_discover_tracks_ignores_stale_clean_enhanced_dirs(tmp_path):
    """Legacy sessions with leftover audio/clean|enhanced/ dirs transcribe from raw."""
    manifest = {
        "session": 7,
        "segment_seconds": 900,
        "mics": [{"mic_id": "mic00", "index": 0, "name": "Built-in", "speaker": "DM"}],
    }
    sdir = _make_session(tmp_path, manifest, {"dm-mic": ["part-000.flac"]})
    for stale_tier in ("clean", "enhanced"):
        d = sdir / "audio" / stale_tier / "dm-mic"
        d.mkdir(parents=True)
        (d / "part-000.flac").write_bytes(b"\x00")
    tracks = discover_tracks(sdir)
    assert len(tracks) == 1
    assert all("/raw/" in str(p) for p in tracks[0].parts)


def test_discover_tracks_finds_flac_raw_parts(tmp_path):
    """FLAC capture (current recorder) must be visible in the raw tier."""
    manifest = {
        "session": 7,
        "segment_seconds": 900,
        "mics": [{"mic_id": "mic00", "index": 0, "name": "Built-in", "speaker": "DM"}],
    }
    sdir = _make_session(
        tmp_path, manifest, {"dm-mic": ["part-001.flac", "part-000.flac"]}
    )
    tracks = discover_tracks(sdir)
    assert [p.name for p in tracks[0].parts] == ["part-000.flac", "part-001.flac"]


# --- scene markers -------------------------------------------------------------


def _scene(n, slug, label, t):
    return {"scene_slug": slug, "scene_number": n, "label": label, "t_offset_s": t}


def test_load_scene_markers_prefers_finalized_json(tmp_path):
    audio = tmp_path / "audio"
    audio.mkdir()
    (audio / "markers.json").write_text(
        json.dumps(
            {
                "session": 7,
                "started_at_epoch": 1690000000.0,
                "markers": [
                    {"event": "recording-started", "t_offset_s": 0.0},
                    _scene(2, "scene-02-docks", "The Docks", 900.5),
                    _scene(1, "scene-01-kyzil", "Kyzil", 312.4),
                    {"event": "recording-ended", "reason": "manual", "t_offset_s": 5000.0},
                ],
            }
        )
    )
    scenes = load_scene_markers(tmp_path)
    # sentinels dropped, scenes sorted by offset
    assert [s["scene_number"] for s in scenes] == [1, 2]


def test_load_scene_markers_falls_back_to_jsonl_and_empty(tmp_path):
    assert load_scene_markers(tmp_path) == []  # no files → legacy no-op
    audio = tmp_path / "audio"
    audio.mkdir()
    lines = [
        json.dumps({"event": "recording-started", "t_offset_s": 0.0}),
        json.dumps(_scene(1, "scene-01-kyzil", "Kyzil", 312.4)),
        "{broken",
    ]
    (audio / "markers.jsonl").write_text("\n".join(lines) + "\n")
    scenes = load_scene_markers(tmp_path)
    assert [s["scene_slug"] for s in scenes] == ["scene-01-kyzil"]


def test_assign_scene_boundaries_and_pre_session():
    scenes = [
        _scene(1, "scene-01-kyzil", "Kyzil", 312.4),
        _scene(2, "scene-02-docks", "The Docks", 900.5),
    ]
    assert assign_scene(0.0, scenes) == "Pre-session"
    assert assign_scene(312.4, scenes) == "Scene 01 — Kyzil"  # inclusive start
    assert assign_scene(899.0, scenes) == "Scene 01 — Kyzil"
    assert assign_scene(4000.0, scenes) == "Scene 02 — The Docks"


def test_scene_display_degrades_without_label_or_number():
    assert scene_display(_scene(3, "scene-03-x", "", 5.0)) == "Scene 03 — scene-03-x"
    assert scene_display({"t_offset_s": 5.0}) == "Scene"


def test_merge_with_markers_adds_scene_and_csv_gains_column(tmp_path):
    utts = [
        Utterance(start=10.0, end=11.0, speaker="DM", text="pre-game chatter"),
        Utterance(start=400.0, end=401.0, speaker="DM", text="the scene begins"),
    ]
    scenes = [_scene(1, "scene-01-kyzil", "Kyzil", 312.4)]
    rows = merge_part_utterances(utts, markers=scenes)
    assert rows[0]["Scene"] == "Pre-session"
    assert rows[1]["Scene"] == "Scene 01 — Kyzil"
    out = tmp_path / "with-scenes.csv"
    write_part_csv(rows, out)
    header, first = out.read_text().splitlines()[:2]
    assert header == "ID,Start,End,Speaker,Text,Scene"
    assert first.endswith(',"Pre-session"')


def test_merge_without_markers_keeps_five_column_shape(tmp_path):
    """Regression guard: legacy sessions must not grow a Scene column."""
    utts = [Utterance(start=0.0, end=1.0, speaker="DM", text="hello")]
    rows = merge_part_utterances(utts)
    assert "Scene" not in rows[0]
    out = tmp_path / "plain.csv"
    write_part_csv(rows, out)
    assert out.read_text().splitlines()[0] == "ID,Start,End,Speaker,Text"


def test_concat_track_parts_single_part_passes_through(tmp_path):
    part = tmp_path / "part-000.m4a"
    part.write_bytes(b"\x00")
    out = tmp_path / "joined.m4a"
    assert concat_track_parts([part], out) == part
    assert not out.exists()


def test_resolve_speaker_prefers_match_then_prior_then_label():
    # identified persona/actor wins
    assert resolve_speaker("Thunk", prior="DM", mic_id="mic00") == "Thunk"
    # no match → mic's speaker prior from the manifest
    assert resolve_speaker(None, prior="Nick", mic_id="mic01") == "Nick"
    # no match, no prior → a stable mic-based label (so it's resolvable later)
    assert resolve_speaker(None, prior=None, mic_id="mic01") == "Speaker mic01"


def test_merge_part_utterances_sorts_and_numbers():
    utts = [
        Utterance(start=3.0, end=4.0, speaker="Nick", text="second"),
        Utterance(start=0.0, end=1.0, speaker="DM", text="first"),
        Utterance(start=3.0, end=3.5, speaker="DM", text="tie-break by speaker"),
    ]
    rows = merge_part_utterances(utts)
    assert [r["ID"] for r in rows] == [1, 2, 3]
    assert [r["Text"] for r in rows] == ["first", "tie-break by speaker", "second"]
    assert rows[0] == {
        "ID": 1,
        "Start": "00:00:00,000",
        "End": "00:00:01,000",
        "Speaker": "DM",
        "Text": "first",
    }


def test_merge_drops_empty_text():
    utts = [
        Utterance(start=0.0, end=1.0, speaker="DM", text="  "),
        Utterance(start=1.0, end=2.0, speaker="DM", text="real"),
    ]
    rows = merge_part_utterances(utts)
    assert [r["Text"] for r in rows] == ["real"]


def test_apply_speaker_map_replaces_labels_and_text_mentions():
    mapping = {"Nick": "DM", "Courtney": "Crissdalynn Khinriss"}
    rows = [
        {"ID": 1, "Start": "00:00:00,000", "End": "00:00:01,000", "Speaker": "Nick",
         "Text": "Courtney, roll for me. I nick the coin off the table."},
        {"ID": 2, "Start": "00:00:01,000", "End": "00:00:02,000", "Speaker": "Courtney",
         "Text": "Nice one, Nick."},
        {"ID": 3, "Start": "00:00:02,000", "End": "00:00:03,000", "Speaker": "Speaker 5",
         "Text": "Unmapped speaker stays."},
    ]
    got = apply_speaker_map(rows, mapping)
    assert got[0]["Speaker"] == "DM"
    # capitalized mention replaced; lowercase verb "nick" untouched
    assert got[0]["Text"] == "Crissdalynn Khinriss, roll for me. I nick the coin off the table."
    assert got[1]["Speaker"] == "Crissdalynn Khinriss"
    assert got[1]["Text"] == "Nice one, DM."
    assert got[2]["Speaker"] == "Speaker 5"


def test_apply_speaker_map_empty_mapping_is_noop():
    rows = [{"ID": 1, "Start": "00:00:00,000", "End": "00:00:01,000", "Speaker": "Nick", "Text": "hi"}]
    assert apply_speaker_map(rows, {}) == rows


def test_write_part_csv_matches_session_ingest_schema(tmp_path):
    rows = [
        {"ID": 1, "Start": "00:00:00,000", "End": "00:00:01,519", "Speaker": "DM", "Text": 'He said "hi"'},
    ]
    out = tmp_path / "session-07-part-00.csv"
    write_part_csv(rows, out)
    with open(out, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ["ID", "Start", "End", "Speaker", "Text"]
        got = list(reader)
    # the millisecond comma must survive a stock CSV round-trip (quoted field)
    assert got[0]["End"] == "00:00:01,519"
    assert got[0]["Text"] == 'He said "hi"'
    assert got[0]["Speaker"] == "DM"


def test_write_part_csv_quotes_timestamps_and_text(tmp_path):
    rows = [
        {"ID": 1, "Start": "00:00:00,000", "End": "00:00:01,519", "Speaker": "DM", "Text": "Hello there."},
    ]
    out = tmp_path / "part.csv"
    write_part_csv(rows, out)
    lines = out.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "ID,Start,End,Speaker,Text"
    assert lines[1] == '1,"00:00:00,000","00:00:01,519",DM,"Hello there."'


# --- real whisper end-to-end (skips without mlx_whisper + macOS `say`) --------


def _can_e2e() -> bool:
    if shutil.which("say") is None or shutil.which("ffmpeg") is None:
        return False
    try:
        import mlx_whisper  # noqa: F401

        return True
    except Exception:
        return False


@pytest.mark.skipif(not _can_e2e(), reason="needs macOS `say` + ffmpeg + mlx_whisper")
def test_transcribe_session_real_whisper(tmp_path):
    """Synthesize speech, record it as a session part, transcribe to CSV."""
    from shattered_audio.session_transcribe import transcribe_session

    sdir = tmp_path / "session-42"
    mic_dir = sdir / "audio" / "raw" / "dm-mic"
    mic_dir.mkdir(parents=True)
    (sdir / "audio" / "manifest.json").write_text(
        json.dumps(
            {
                "session": 42,
                "segment_seconds": 900,
                "mics": [{"mic_id": "mic00", "index": 0, "name": "test", "speaker": "DM"}],
            }
        )
    )
    aiff = tmp_path / "line.aiff"
    subprocess.run(
        ["say", "-o", str(aiff), "The dragon guards the bridge."], check=True
    )
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(aiff),
         "-ac", "1", "-ar", "16000", "-c:a", "aac", str(mic_dir / "part-000.m4a")],
        check=True,
    )

    transcribe_session(42, audio_dir=tmp_path, use_profiles=False)

    csv_path = sdir / "transcripts" / "raw" / "session-42.csv"
    assert csv_path.exists(), "expected a whole-session CSV"
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert rows, "transcript should not be empty"
    assert all(r["Speaker"] == "DM" for r in rows)  # mic prior applied
    joined = " ".join(r["Text"] for r in rows).lower()
    assert "dragon" in joined or "bridge" in joined
