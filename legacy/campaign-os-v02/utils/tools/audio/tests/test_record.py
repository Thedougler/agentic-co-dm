"""Tests for the multi-mic ffmpeg recorder (pure logic)."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from shattered_audio import record
from shattered_audio.record import (
    RecordMic,
    build_aggregate_ffmpeg_command,
    build_ffmpeg_command,
    build_manifest,
    parse_avfoundation_devices,
    raw_mic_dir,
    select_aggregate_mics,
    select_mics,
    session_dir,
)

# Real `ffmpeg -f avfoundation -list_devices true -i ""` stderr on macOS.
SAMPLE_LISTING = """\
[AVFoundation indev @ 0x850c24140] AVFoundation video devices:
[AVFoundation indev @ 0x850c24140] [0] FaceTime HD Camera
[AVFoundation indev @ 0x850c24140] AVFoundation audio devices:
[AVFoundation indev @ 0x850c24140] [0] MacBook Air Microphone
[AVFoundation indev @ 0x850c24140] [1] EMEET OfficeCore M0 Plus
[in#0 @ 0x850c24000] Error opening input: Input/output error
"""


def test_parse_avfoundation_devices_returns_only_audio():
    devs = parse_avfoundation_devices(SAMPLE_LISTING)
    assert devs == [
        {"index": 0, "name": "MacBook Air Microphone"},
        {"index": 1, "name": "EMEET OfficeCore M0 Plus"},
    ]


def test_parse_avfoundation_devices_empty_when_no_audio_section():
    assert parse_avfoundation_devices("no devices here") == []


def test_select_mics_defaults_to_all():
    devs = parse_avfoundation_devices(SAMPLE_LISTING)
    mics = select_mics(devs)
    assert [m.index for m in mics] == [0, 1]
    assert [m.mic_id for m in mics] == ["mic00", "mic01"]
    assert mics[0].name == "MacBook Air Microphone"


def test_select_mics_by_index_spec_preserves_request_order():
    devs = parse_avfoundation_devices(SAMPLE_LISTING)
    mics = select_mics(devs, indices=[1, 0])
    assert [m.index for m in mics] == [1, 0]
    # mic_id is positional in the selection, not the device index
    assert [m.mic_id for m in mics] == ["mic00", "mic01"]


def test_select_mics_by_name_substring():
    devs = parse_avfoundation_devices(SAMPLE_LISTING)
    mics = select_mics(devs, names=["EMEET"])
    assert [m.index for m in mics] == [1]
    assert mics[0].name == "EMEET OfficeCore M0 Plus"


def test_select_mics_unknown_index_is_skipped():
    devs = parse_avfoundation_devices(SAMPLE_LISTING)
    mics = select_mics(devs, indices=[0, 9])
    assert [m.index for m in mics] == [0]


def test_build_ffmpeg_command_shape():
    out = Path("/tmp/s07/audio/raw/dm-mic/part-%03d.flac")
    cmd = build_ffmpeg_command(device_index=1, out_pattern=out, segment_seconds=900)
    assert cmd[0] == "ffmpeg"
    # avfoundation audio-only input is ":<index>"
    assert "-f" in cmd and "avfoundation" in cmd
    i = cmd.index("-i")
    assert cmd[i + 1] == ":1"
    # mono, lossless FLAC at the 48 kHz capture rate, segmented
    assert "-ac" in cmd and cmd[cmd.index("-ac") + 1] == "1"
    assert "-ar" in cmd and cmd[cmd.index("-ar") + 1] == "48000"
    assert cmd[cmd.index("-c:a") + 1] == "flac"
    assert "-b:a" not in cmd
    assert "segment" in cmd
    assert cmd[cmd.index("-segment_time") + 1] == "900"
    assert cmd[-1] == str(out)
    # gap-filling: a glitchy device must not produce a time-compressed stream;
    # the highpass strips sub-speech rumble only (no capture-time denoise)
    assert cmd[cmd.index("-af") + 1] == "aresample=async=1:first_pts=0,highpass=f=80"


def test_build_ffmpeg_command_default_channels_is_mono():
    out = Path("/tmp/s07/audio/raw/dm-mic/part-%03d.m4a")
    cmd = build_ffmpeg_command(device_index=1, out_pattern=out, segment_seconds=900)
    assert cmd[cmd.index("-ac") + 1] == "1"


def test_build_ffmpeg_command_stereo_channels_opt_in():
    out = Path("/tmp/s07/audio/raw/player-mic/part-%03d.m4a")
    cmd = build_ffmpeg_command(
        device_index=1, out_pattern=out, segment_seconds=900, channels=2
    )
    assert cmd[cmd.index("-ac") + 1] == "2"


def test_session_and_raw_dirs_are_zero_padded():
    base = Path("/vault/.raw/sessions")
    assert session_dir(base, 7) == base / "session-07"
    assert session_dir(base, 12) == base / "session-12"
    # the first two mics are named by table role, not index
    mic = RecordMic(index=1, name="EMEET", mic_id="mic00")
    assert raw_mic_dir(base, 7, mic) == base / "session-07" / "audio" / "raw" / "dm-mic"
    mic1 = RecordMic(index=3, name="USB", mic_id="mic01")
    assert raw_mic_dir(base, 7, mic1) == base / "session-07" / "audio" / "raw" / "player-mic"
    # a third mic falls back to index form
    mic2 = RecordMic(index=5, name="Extra", mic_id="mic02")
    assert raw_mic_dir(base, 7, mic2) == base / "session-07" / "audio" / "raw" / "mic-02"


def test_build_manifest_records_mic_mapping():
    mics = [
        RecordMic(index=0, name="MacBook Air Microphone", mic_id="mic00", speaker="DM"),
        RecordMic(index=1, name="EMEET OfficeCore M0 Plus", mic_id="mic01"),
    ]
    m = build_manifest(session=7, mics=mics, segment_seconds=900)
    assert m["session"] == 7
    assert m["segment_seconds"] == 900
    assert m["capture"] == "per-mic"
    assert m["mics"] == [
        {
            "mic_id": "mic00",
            "index": 0,
            "name": "MacBook Air Microphone",
            "speaker": "DM",
            "channels": 1,
            "channel": None,
        },
        {
            "mic_id": "mic01",
            "index": 1,
            "name": "EMEET OfficeCore M0 Plus",
            "speaker": None,
            "channels": 1,
            "channel": None,
        },
    ]


def test_build_manifest_round_trips_stereo_channels():
    mics = [
        RecordMic(index=0, name="MacBook Air Microphone", mic_id="mic00", channels=2),
        RecordMic(index=1, name="EMEET OfficeCore M0 Plus", mic_id="mic01"),
    ]
    m = build_manifest(session=7, mics=mics, segment_seconds=900)
    assert m["mics"][0]["channels"] == 2
    assert m["mics"][1]["channels"] == 1


def test_record_mic_defaults_to_mono():
    mic = RecordMic(index=0, name="MacBook Air Microphone", mic_id="mic00")
    assert mic.channels == 1


# --- aggregate capture (preferred mode) ---------------------------------------

AGGREGATE_LISTING = """\
[AVFoundation indev @ 0x850c24140] AVFoundation audio devices:
[AVFoundation indev @ 0x850c24140] [0] Aggregate Device
[AVFoundation indev @ 0x850c24140] [1] MacBook Air Microphone
[AVFoundation indev @ 0x850c24140] [2] EMEET OfficeCore M0 Plus
"""

AGGREGATE_CFG = {
    "name": "Aggregate Device",
    "mics": [
        {"channel": 2, "name": "MacBook Air Microphone"},
        {"channel": 0, "name": "EMEET OfficeCore M0 Plus"},
    ],
}


def test_select_aggregate_mics_resolves_device_and_channels():
    devs = parse_avfoundation_devices(AGGREGATE_LISTING)
    agg = select_aggregate_mics(devs, AGGREGATE_CFG)
    assert agg is not None
    index, mics = agg
    assert index == 0
    assert [m.mic_id for m in mics] == ["mic00", "mic01"]
    assert [m.channel for m in mics] == [2, 0]
    assert mics[0].name == "MacBook Air Microphone"
    # all mics point at the aggregate's avfoundation index
    assert all(m.index == 0 for m in mics)


def test_select_aggregate_mics_none_without_config_or_device():
    devs = parse_avfoundation_devices(AGGREGATE_LISTING)
    assert select_aggregate_mics(devs, None) is None
    assert select_aggregate_mics(devs, {"name": "Aggregate Device", "mics": []}) is None
    no_agg = parse_avfoundation_devices(SAMPLE_LISTING)
    assert select_aggregate_mics(no_agg, AGGREGATE_CFG) is None


def test_build_aggregate_ffmpeg_command_shape():
    devs = parse_avfoundation_devices(AGGREGATE_LISTING)
    _, mics = select_aggregate_mics(devs, AGGREGATE_CFG)
    outs = [
        Path("/tmp/s07/audio/raw/dm-mic/part-%03d.flac"),
        Path("/tmp/s07/audio/raw/player-mic/part-%03d.flac"),
    ]
    cmd = build_aggregate_ffmpeg_command(0, mics, outs, segment_seconds=900)
    assert cmd[0] == "ffmpeg"
    assert cmd[cmd.index("-i") + 1] == ":0"
    # one pan per mic, each with gap-fill + rumble highpass, labeled m0/m1
    fc = cmd[cmd.index("-filter_complex") + 1]
    assert fc == (
        "[0:a]pan=mono|c0=c2,aresample=async=1:first_pts=0,highpass=f=80[m0];"
        "[0:a]pan=mono|c0=c0,aresample=async=1:first_pts=0,highpass=f=80[m1]"
    )
    # each output mapped, 48 kHz FLAC segments
    assert cmd.count("-map") == 2
    assert cmd.count("flac") == 2
    assert "-b:a" not in cmd
    assert cmd[cmd.index("-map") + 1] == "[m0]"
    assert cmd.count("segment") == 2
    assert str(outs[0]) in cmd and str(outs[1]) in cmd


def test_build_manifest_aggregate_capture_mode():
    devs = parse_avfoundation_devices(AGGREGATE_LISTING)
    _, mics = select_aggregate_mics(devs, AGGREGATE_CFG)
    m = build_manifest(session=7, mics=mics, segment_seconds=900, capture="aggregate")
    assert m["capture"] == "aggregate"
    assert [e["channel"] for e in m["mics"]] == [2, 0]


# --- device presence + scene markers ------------------------------------------


def test_verify_devices_present_reports_missing_names():
    devs = parse_avfoundation_devices(SAMPLE_LISTING)
    assert record.verify_devices_present(devs, ["MacBook Air Microphone"]) == []
    # case-insensitive substring match
    assert record.verify_devices_present(devs, ["emeet"]) == []
    assert record.verify_devices_present(devs, ["Blue Yeti", "EMEET"]) == ["Blue Yeti"]


def test_build_manifest_carries_capture_metadata():
    mics = [RecordMic(index=0, name="MacBook Air Microphone", mic_id="mic00")]
    m = build_manifest(
        session=7, mics=mics, segment_seconds=900,
        started_at_epoch=1690000000.0, strict=True,
    )
    assert m["started_at_epoch"] == 1690000000.0
    assert m["capture_sample_rate"] == 48000
    assert m["sample_rate"] == 16000  # transcription rate, unchanged
    assert m["strict"] is True


def test_markers_append_and_finalize(tmp_path):
    audio = tmp_path / "audio"
    audio.mkdir()
    record.append_marker(audio, {"event": "recording-started", "t_offset_s": 0.0})
    record.append_marker(
        audio, {"scene_slug": "scene-02-docks", "scene_number": 2, "t_offset_s": 900.5}
    )
    record.append_marker(
        audio, {"scene_slug": "scene-01-kyzil", "scene_number": 1, "t_offset_s": 312.4}
    )
    # a malformed line (crash mid-write, hand edit) must not sink the rest
    with open(audio / "markers.jsonl", "a") as f:
        f.write("{not json\n")
    record.finalize_markers(audio, session=7, started_at_epoch=1690000000.0)
    import json

    data = json.loads((audio / "markers.json").read_text())
    assert data["session"] == 7
    assert data["started_at_epoch"] == 1690000000.0
    assert [m.get("t_offset_s") for m in data["markers"]] == [0.0, 312.4, 900.5]


# --- real-capture integration (skips without ffmpeg + a working mic) ---------


def _has_mics() -> bool:
    if shutil.which("ffmpeg") is None:
        return False
    try:
        return len(record.list_avfoundation_devices()) > 0
    except Exception:
        return False


@pytest.mark.skipif(not _has_mics(), reason="no ffmpeg/avfoundation mic available")
def test_record_session_real_capture(tmp_path):
    """A few seconds of real capture should produce finalized, segmented FLAC."""
    mics = select_mics(record.list_avfoundation_devices())
    sdir = record.record_session(
        session=99, mics=mics, audio_dir=tmp_path, segment_seconds=2, max_seconds=5.0
    )
    assert (sdir / "audio" / "manifest.json").exists()
    parts = list(sdir.rglob("*.flac"))
    assert parts, "expected at least one recorded segment"
    # every selected mic produced its own track directory (dash-form, under audio/)
    for mic in mics:
        assert raw_mic_dir(tmp_path, 99, mic).is_dir()
    # segments are non-trivially sized (not empty/truncated)
    assert all(p.stat().st_size > 256 for p in parts)


def _aggregate_index() -> int | None:
    if shutil.which("ffmpeg") is None:
        return None
    try:
        devs = record.list_avfoundation_devices()
    except Exception:
        return None
    dev = next((d for d in devs if "aggregate device" in d["name"].lower()), None)
    return dev["index"] if dev else None


@pytest.mark.skipif(_aggregate_index() is None, reason="no Aggregate Device present")
def test_record_session_aggregate_real_capture(tmp_path):
    """Aggregate capture: one ffmpeg, per-mic mono part series from channels."""
    devs = record.list_avfoundation_devices()
    agg = select_aggregate_mics(
        devs,
        {
            "name": "Aggregate Device",
            "mics": [
                {"channel": 2, "name": "MacBook Air Microphone"},
                {"channel": 0, "name": "EMEET OfficeCore M0 Plus"},
            ],
        },
    )
    assert agg is not None
    index, mics = agg
    sdir = record.record_session(
        session=98,
        mics=mics,
        audio_dir=tmp_path,
        segment_seconds=2,
        max_seconds=5.0,
        calibrate=True,  # must be auto-skipped, not attempted
        aggregate_index=index,
    )
    import json

    manifest = json.loads((sdir / "audio" / "manifest.json").read_text())
    assert manifest["capture"] == "aggregate"
    assert "chirp_calibration" not in manifest
    for mic in mics:
        mic_parts = list(raw_mic_dir(tmp_path, 98, mic).glob("*.flac"))
        assert mic_parts, f"expected segments for {mic.mic_id}"
        assert all(p.stat().st_size > 256 for p in mic_parts)
