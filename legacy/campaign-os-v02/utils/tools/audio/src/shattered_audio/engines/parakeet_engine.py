"""Parakeet-TDT engine via parakeet-mlx."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..transcribe import Segment

_MODELS: dict[str, Any] = {}


def _get_model(model: str) -> Any:
    """Load a parakeet model once per process; reloading per call leaks Metal buffers."""
    cached = _MODELS.get(model)
    if cached is not None:
        return cached
    try:
        from parakeet_mlx import from_pretrained
    except ImportError as e:
        raise RuntimeError(
            "parakeet-mlx is not installed. Install it with: "
            "pip install 'shattered-audio[parakeet]'"
        ) from e
    loaded = from_pretrained(model)
    _MODELS[model] = loaded
    return loaded


def transcribe(
    audio_path: Path,
    *,
    model: str = "mlx-community/parakeet-tdt-0.6b-v3",
    chunk_duration: float = 120.0,
    overlap_duration: float = 15.0,
    progress=None,
    **_,
) -> list[Segment]:
    """Transcribe an audio file using parakeet-mlx.

    Chunked decode: an unchunked pass runs attention over the whole file —
    a 15-minute track costs ~10 GB and runs several times slower.
    `progress` (optional) receives (current_position, total_position) per chunk.

    Returns a list of timed segments with text.
    """
    m = _get_model(model)
    result = m.transcribe(
        str(audio_path),
        chunk_duration=chunk_duration,
        overlap_duration=overlap_duration,
        chunk_callback=progress,
    )

    import mlx.core as mx

    mx.clear_cache()

    return [
        Segment(start=sentence.start, end=sentence.end, text=sentence.text.strip())
        for sentence in result.sentences
    ]
