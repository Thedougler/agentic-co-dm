"""Tests for Config — specifically the stereo_mics field used by the record
CLI to opt individual mics into 2-channel capture (record.py's RecordMic.channels)."""

from __future__ import annotations

from pathlib import Path

from shattered_audio.config import Config


def test_stereo_mics_defaults_to_empty_list():
    cfg = Config()
    assert cfg.stereo_mics == []


def test_stereo_mics_loads_from_yaml(tmp_path):
    config_path = tmp_path / "config.yaml"
    config_path.write_text("stereo_mics:\n  - mic01\n")
    cfg = Config.load(config_path)
    assert cfg.stereo_mics == ["mic01"]


def test_stereo_mics_missing_from_yaml_stays_empty(tmp_path):
    config_path = tmp_path / "config.yaml"
    config_path.write_text("vault_path: .\n")
    cfg = Config.load(config_path)
    assert cfg.stereo_mics == []


def test_chirp_bands_defaults_to_none():
    cfg = Config()
    assert cfg.chirp_bands is None


def test_chirp_bands_round_trips_from_yaml(tmp_path):
    config_path = tmp_path / "config.yaml"
    config_path.write_text(
        "chirp_bands:\n"
        "  mic00:\n"
        "    - 15000\n"
        "    - 17500\n"
    )
    cfg = Config.load(config_path)
    assert cfg.chirp_bands == {"mic00": [15000, 17500]}
