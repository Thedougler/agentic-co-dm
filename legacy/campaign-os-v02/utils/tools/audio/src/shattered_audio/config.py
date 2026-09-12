"""Configuration management for shattered-audio."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


PROFILES_DIR = Path.home() / ".config" / "shattered-audio" / "profiles"
AUTOCORRECT_PATH = Path(__file__).resolve().parent.parent.parent / "autocorrect.csv"


@dataclass
class Config:
    vault_path: Path = Path(".")
    whisper_model: str = "mlx-community/whisper-large-v3-mlx"
    whisper_model_fast: str = "mlx-community/whisper-medium-mlx"
    device: str = "mps"
    speaker_map: dict[str, str] = field(default_factory=dict)
    mic_names: list[str] = field(default_factory=list)
    stereo_mics: list[str] = field(default_factory=list)
    aggregate: dict | None = None
    # Capture-stage knobs (record.py owns the defaults). The aggregate.mics
    # list scales 1..N: a single entry is a one-mic rig, per-player mics are
    # just more entries — device checks, channel splits, and speaker priors
    # all follow the list.
    capture_sample_rate: int = 48000
    capture_highpass_hz: int = 80
    channel_priors: dict[str, str] = field(default_factory=dict)
    chirp_bands: dict[str, list[float]] | None = None
    channel_boost: float = 0.15
    speaker_threshold: float = 0.7
    profiles_dir: Path = PROFILES_DIR
    chunk_target_minutes: int = 15
    chunk_silence_gap: float = 2.0
    inbox_path: Path = Path("Inbox")

    # v2 persona identification
    actor_threshold: float = 0.7
    persona_threshold: float = 0.6
    persona_margin: float = 0.05
    prosody_weight: float = 0.3
    max_exemplars: int = 8

    # Transcription engine + output formats
    engine: str = "parakeet-v3"
    output_formats: list[str] = field(default_factory=lambda: ["csv", "json", "md"])
    autocorrect_path: Path | None = AUTOCORRECT_PATH

    @classmethod
    def load(cls, path: Path | None = None) -> Config:
        candidates = [
            path,
            Path("config.yaml"),
            Path.home() / ".config" / "shattered-audio" / "config.yaml",
        ]
        for candidate in candidates:
            if candidate and candidate.exists():
                with open(candidate) as f:
                    data = yaml.safe_load(f) or {}

                # actor_threshold falls back to speaker_threshold for compat
                speaker_thresh = data.get("speaker_threshold", cls.speaker_threshold)
                actor_thresh = data.get("actor_threshold", speaker_thresh)

                return cls(
                    vault_path=Path(data.get("vault_path", ".")),
                    whisper_model=data.get("whisper_model", cls.whisper_model),
                    whisper_model_fast=data.get("whisper_model_fast", cls.whisper_model_fast),
                    device=data.get("device", cls.device),
                    speaker_map=data.get("speaker_map", {}),
                    mic_names=data.get("mic_names", []),
                    stereo_mics=data.get("stereo_mics", []),
                    aggregate=data.get("aggregate", cls.aggregate),
                    capture_sample_rate=data.get("capture_sample_rate", cls.capture_sample_rate),
                    capture_highpass_hz=data.get("capture_highpass_hz", cls.capture_highpass_hz),
                    channel_priors=data.get("channel_priors", {}),
                    chirp_bands=data.get("chirp_bands", cls.chirp_bands),
                    channel_boost=data.get("channel_boost", cls.channel_boost),
                    speaker_threshold=speaker_thresh,
                    profiles_dir=Path(data.get("profiles_dir", cls.profiles_dir)),
                    chunk_target_minutes=data.get("chunk_target_minutes", cls.chunk_target_minutes),
                    chunk_silence_gap=data.get("chunk_silence_gap", cls.chunk_silence_gap),
                    inbox_path=Path(data.get("inbox_path", cls.inbox_path)),
                    actor_threshold=actor_thresh,
                    persona_threshold=data.get("persona_threshold", cls.persona_threshold),
                    persona_margin=data.get("persona_margin", cls.persona_margin),
                    prosody_weight=data.get("prosody_weight", cls.prosody_weight),
                    max_exemplars=data.get("max_exemplars", cls.max_exemplars),
                    engine=data.get("engine", cls.engine),
                    output_formats=data.get("output_formats", ["csv", "json", "md"]),
                    autocorrect_path=(
                        Path(autocorrect_val)
                        if (autocorrect_val := data.get("autocorrect_path", cls.autocorrect_path))
                        else None
                    ),
                )
        return cls()
