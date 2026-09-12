"""ElevenLabs speech-to-text engine (raw HTTP, diarized)."""

from __future__ import annotations

import os
from pathlib import Path

from ..transcribe import Segment

API_URL = "https://api.elevenlabs.io/v1/speech-to-text"

# A new segment starts when the speaker changes, when the gap since the
# previous word ended is at least this long, or when the previous word ends
# a sentence.
GAP_THRESHOLD = 0.8
SENTENCE_ENDERS = (".", "!", "?")


def _api_key() -> str:
    """Resolve the ElevenLabs API key from the environment or repo .env.local."""
    from ..env_local import load_env_local

    load_env_local()
    key = os.environ.get("ELEVENLABS_API_KEY")
    if key:
        return key
    raise RuntimeError(
        "ElevenLabs API key not found. Set the ELEVENLABS_API_KEY environment "
        "variable, or add ELEVENLABS_API_KEY=... to <repo-root>/.env.local"
    )


def _group_words(words: list[dict]) -> list[Segment]:
    """Group word/spacing tokens into Segments, splitting on speaker/gap/sentence."""
    segments: list[Segment] = []
    current_text: list[str] = []
    current_start: float | None = None
    current_end: float | None = None
    current_speaker: str | None = None
    prev_word_end: float | None = None
    prev_word_text = ""

    def flush() -> None:
        text = "".join(current_text).strip()
        if text:
            segments.append(
                Segment(
                    start=current_start,
                    end=current_end,
                    text=text,
                    engine_speaker_id=current_speaker,
                )
            )

    for tok in words:
        tok_type = tok.get("type")
        if tok_type == "audio_event":
            continue
        if tok_type == "spacing":
            if current_text:
                current_text.append(tok.get("text", ""))
            continue

        # tok_type == "word"
        speaker = tok.get("speaker_id")
        start = tok.get("start")
        end = tok.get("end")
        text = tok.get("text", "")

        new_segment = False
        if not current_text:
            new_segment = True
        elif speaker != current_speaker:
            new_segment = True
        elif prev_word_end is not None and start is not None and (start - prev_word_end) >= GAP_THRESHOLD:
            new_segment = True
        elif prev_word_text and prev_word_text[-1] in SENTENCE_ENDERS:
            new_segment = True

        if new_segment and current_text:
            flush()
            current_text = []

        if not current_text:
            current_start = start
            current_speaker = speaker

        current_text.append(text)
        current_end = end
        prev_word_end = end
        prev_word_text = text

    flush()
    return segments


def transcribe(
    audio_path: Path,
    *,
    model: str = "scribe_v2",
    num_speakers: int | None = None,
    language_code: str | None = None,
    **_,
) -> list[Segment]:
    """Transcribe an audio file using the ElevenLabs speech-to-text API."""
    import httpx

    api_key = _api_key()

    data = {
        "model_id": model,
        "diarize": "true",
        "timestamps_granularity": "word",
    }
    if num_speakers is not None:
        data["num_speakers"] = str(num_speakers)
    if language_code is not None:
        data["language_code"] = language_code

    with open(audio_path, "rb") as f:
        files = {"file": (Path(audio_path).name, f)}
        response = httpx.post(
            API_URL,
            headers={"xi-api-key": api_key},
            data=data,
            files=files,
            timeout=600,
        )

    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise RuntimeError(
            f"ElevenLabs speech-to-text failed ({response.status_code}): {response.text}"
        ) from e

    payload = response.json()
    return _group_words(payload.get("words", []))
