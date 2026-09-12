"""Whisper engine — re-exports :func:`shattered_audio.transcribe.transcribe`."""

from __future__ import annotations

from ..transcribe import transcribe

__all__ = ["transcribe"]
