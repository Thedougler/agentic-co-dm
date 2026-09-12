"""Whisper-based audio transcription via MLX on Apple Silicon."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Segment:
    start: float
    end: float
    text: str
    speaker: str | None = None
    engine_speaker_id: str | None = None


def transcribe(
    audio_path: Path,
    *,
    model: str = "mlx-community/whisper-large-v3-mlx",
) -> list[Segment]:
    """Transcribe an audio file using mlx-whisper.

    Returns a list of timed segments with text.
    """
    import mlx_whisper

    result = mlx_whisper.transcribe(
        str(audio_path),
        path_or_hf_repo=model,
        verbose=False,
        # Independent 30s windows: conditioning on prior text sends whisper
        # into repetition loops ("Okay." × 15) on the near-silent stretches a
        # cross-talk-cleaned track has wherever only the other mic was live.
        condition_on_previous_text=False,
        # With word timestamps available, skip over silent gaps ≥ 2s instead
        # of hallucinating into them.
        word_timestamps=True,
        hallucination_silence_threshold=2.0,
    )

    segments = []
    for seg in result.get("segments", []):
        segments.append(
            Segment(
                start=seg["start"],
                end=seg["end"],
                text=seg["text"].strip(),
            )
        )

    return segments
