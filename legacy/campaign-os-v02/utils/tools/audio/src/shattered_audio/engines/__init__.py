"""Pluggable transcription engines.

Each engine module exposes a ``transcribe(audio_path, *, model=..., **kwargs)
-> list[Segment]`` function. :func:`run` dispatches to one by name, importing
it lazily so an engine's third-party dependency is only required when that
engine is actually used.
"""

from __future__ import annotations

import importlib
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..transcribe import Segment

ENGINES = {
    "whisper": "shattered_audio.engines.whisper_engine",
    "parakeet-v3": "shattered_audio.engines.parakeet_engine",
    "elevenlabs": "shattered_audio.engines.elevenlabs_engine",
}


def run(engine: str, audio_path: Path, *, model: str | None = None, **kwargs) -> list["Segment"]:
    """Transcribe ``audio_path`` with the named engine.

    Raises ``ValueError`` for an unknown engine name.
    """
    module_name = ENGINES.get(engine)
    if module_name is None:
        raise ValueError(
            f"Unknown engine {engine!r}; expected one of: {', '.join(sorted(ENGINES))}"
        )
    module = importlib.import_module(module_name)
    if model is not None:
        kwargs["model"] = model
    return module.transcribe(audio_path, **kwargs)
