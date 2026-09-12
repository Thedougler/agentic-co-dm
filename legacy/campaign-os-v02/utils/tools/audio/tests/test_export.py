"""Tests for the session playback export (concat + stereo join)."""

from __future__ import annotations

from pathlib import Path

import pytest

from shattered_audio.export import (
    build_export_command,
    export_session,
    write_concat_list,
)


def test_write_concat_list_absolute_paths_and_quoting(tmp_path):
    parts = [tmp_path / "part-000.m4a", tmp_path / "it's.m4a"]
    lst = write_concat_list(parts, tmp_path / "concat.txt")
    text = lst.read_text()
    lines = text.strip().splitlines()
    assert len(lines) == 2
    assert lines[0] == f"file '{parts[0].resolve()}'"
    # single quote escaped per concat-demuxer rules
    assert "'\\''" in lines[1]


def test_build_export_command_stereo_join():
    lists = [Path("/tmp/a.txt"), Path("/tmp/b.txt")]
    cmd = build_export_command(lists, Path("/tmp/out.m4a"))
    assert cmd[0] == "ffmpeg"
    assert cmd.count("concat") == 2
    fc = cmd[cmd.index("-filter_complex") + 1]
    # dm-mic (input 0) left, player-mic (input 1) right
    assert fc == "[0:a][1:a]join=inputs=2:channel_layout=stereo:map=0.0-FL|1.0-FR[a]"
    assert cmd[cmd.index("-map") + 1] == "[a]"
    assert cmd[cmd.index("-b:a") + 1] == "192k"
    assert cmd[-1] == "/tmp/out.m4a"


def test_build_export_command_single_mic_is_passthrough():
    cmd = build_export_command([Path("/tmp/a.txt")], Path("/tmp/out.m4a"))
    assert "-filter_complex" not in cmd
    assert cmd.count("concat") == 1


def test_build_export_command_segmented():
    lists = [Path("/tmp/a.txt"), Path("/tmp/b.txt")]
    cmd = build_export_command(
        lists, Path("/tmp/playback/part-%03d.m4a"), segment_seconds=900
    )
    assert cmd[cmd.index("-segment_time") + 1] == "900"
    assert cmd[cmd.index("-reset_timestamps") + 1] == "1"
    assert "segment" in cmd
    assert cmd[-1] == "/tmp/playback/part-%03d.m4a"
    # segment flags come after the encoder, before the output pattern
    assert cmd.index("-b:a") < cmd.index("-segment_time")


def test_export_session_errors_without_audio(tmp_path):
    with pytest.raises(FileNotFoundError):
        export_session(tmp_path)
