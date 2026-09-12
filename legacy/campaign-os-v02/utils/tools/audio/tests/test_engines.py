"""Tests for the pluggable transcription engines (shattered_audio.engines)."""

from __future__ import annotations

import sys
import types
from pathlib import Path

import pytest

from shattered_audio import engines
from shattered_audio.transcribe import Segment


def test_unknown_engine_raises_clear_value_error():
    with pytest.raises(ValueError, match="Unknown engine 'nope'"):
        engines.run("nope", Path("audio.m4a"))


def test_whisper_engine_reexports_transcribe_identity():
    from shattered_audio import transcribe as transcribe_mod
    from shattered_audio.engines import whisper_engine

    assert whisper_engine.transcribe is transcribe_mod.transcribe


def test_run_dispatches_to_whisper_engine(monkeypatch):
    calls = []

    def fake_transcribe(path, *, model=None, **kw):
        calls.append((path, model, kw))
        return [Segment(start=0.0, end=1.0, text="hi")]

    monkeypatch.setattr(
        "shattered_audio.engines.whisper_engine.transcribe", fake_transcribe
    )
    result = engines.run("whisper", Path("a.m4a"), model="my-model")
    assert calls == [(Path("a.m4a"), "my-model", {})]
    assert result[0].text == "hi"


# --- parakeet -----------------------------------------------------------


def _install_fake_parakeet_mlx(monkeypatch, sentences):
    class FakeModel:
        def transcribe(self, path, **kwargs):
            return types.SimpleNamespace(sentences=sentences)

    fake_module = types.ModuleType("parakeet_mlx")
    fake_module.from_pretrained = lambda model: FakeModel()
    monkeypatch.setitem(sys.modules, "parakeet_mlx", fake_module)

    from shattered_audio.engines import parakeet_engine

    monkeypatch.setattr(parakeet_engine, "_MODELS", {})


def test_parakeet_engine_maps_sentences_to_segments(monkeypatch):
    sentences = [
        types.SimpleNamespace(start=0.0, end=1.2, text=" hello there "),
        types.SimpleNamespace(start=1.2, end=2.5, text="general kenobi"),
    ]
    _install_fake_parakeet_mlx(monkeypatch, sentences)

    from shattered_audio.engines import parakeet_engine

    segments = parakeet_engine.transcribe(Path("audio.m4a"))
    assert [(s.start, s.end, s.text) for s in segments] == [
        (0.0, 1.2, "hello there"),
        (1.2, 2.5, "general kenobi"),
    ]


def test_parakeet_engine_missing_dependency_raises_runtime_error(monkeypatch):
    monkeypatch.setitem(sys.modules, "parakeet_mlx", None)  # forces ImportError

    from shattered_audio.engines import parakeet_engine

    monkeypatch.setattr(parakeet_engine, "_MODELS", {})

    with pytest.raises(RuntimeError, match="parakeet-mlx"):
        parakeet_engine.transcribe(Path("audio.m4a"))


def test_run_dispatches_to_parakeet_engine(monkeypatch):
    sentences = [types.SimpleNamespace(start=0.0, end=1.0, text="yo")]
    _install_fake_parakeet_mlx(monkeypatch, sentences)

    result = engines.run("parakeet-v3", Path("audio.m4a"))
    assert result[0].text == "yo"


# --- elevenlabs -----------------------------------------------------------


class _FakeResponse:
    def __init__(self, status_code=200, json_data=None, text=""):
        self.status_code = status_code
        self._json = json_data or {}
        self.text = text

    def raise_for_status(self):
        if self.status_code >= 400:
            import httpx

            raise httpx.HTTPStatusError("boom", request=None, response=self)

    def json(self):
        return self._json


def _install_fake_httpx(monkeypatch, response, captured=None):
    import httpx as real_httpx

    def fake_post(url, *, headers, data, files, timeout):
        if captured is not None:
            captured.update(url=url, headers=headers, data=data, timeout=timeout)
        return response

    monkeypatch.setattr(real_httpx, "post", fake_post)


def test_elevenlabs_engine_groups_words_and_sets_speaker_id(monkeypatch, tmp_path):
    words_payload = {
        "words": [
            {"type": "word", "text": "Hello", "start": 0.0, "end": 0.3, "speaker_id": "s1"},
            {"type": "spacing", "text": " "},
            {"type": "word", "text": "world.", "start": 0.3, "end": 0.8, "speaker_id": "s1"},
            {"type": "word", "text": "Bye.", "start": 1.6, "end": 2.0, "speaker_id": "s2"},
        ]
    }
    _install_fake_httpx(monkeypatch, _FakeResponse(200, words_payload))
    monkeypatch.setenv("ELEVENLABS_API_KEY", "test-key")

    audio_path = tmp_path / "clip.flac"
    audio_path.write_bytes(b"fake-audio")

    from shattered_audio.engines import elevenlabs_engine

    segments = elevenlabs_engine.transcribe(audio_path)
    assert len(segments) == 2
    assert segments[0].text == "Hello world."
    assert segments[0].engine_speaker_id == "s1"
    assert segments[1].text == "Bye."
    assert segments[1].engine_speaker_id == "s2"


def test_elevenlabs_engine_missing_key_raises_runtime_error(monkeypatch, tmp_path):
    monkeypatch.delenv("ELEVENLABS_API_KEY", raising=False)

    import shattered_audio.engines.elevenlabs_engine as eleven_mod
    import shattered_audio.env_local as env_local_mod

    # No .git ancestor findable from this fake __file__ location -> _api_key
    # falls through to the "not found" branch regardless of the real repo.
    fake_here = tmp_path / "nowhere" / "env_local.py"
    fake_here.parent.mkdir(parents=True)
    monkeypatch.setattr(env_local_mod, "__file__", str(fake_here))

    audio_path = tmp_path / "clip.flac"
    audio_path.write_bytes(b"fake-audio")

    with pytest.raises(RuntimeError, match="ElevenLabs API key not found"):
        eleven_mod.transcribe(audio_path)


def test_elevenlabs_engine_reads_key_from_env_local_fallback(monkeypatch, tmp_path):
    monkeypatch.delenv("ELEVENLABS_API_KEY", raising=False)

    repo_root = tmp_path / "repo"
    (repo_root / ".git").mkdir(parents=True)
    (repo_root / ".env.local").write_text('ELEVENLABS_API_KEY="from-env-local"\n')

    fake_here = repo_root / "src" / "shattered_audio" / "env_local.py"
    fake_here.parent.mkdir(parents=True)

    captured = {}
    _install_fake_httpx(monkeypatch, _FakeResponse(200, {"words": []}), captured)

    import shattered_audio.engines.elevenlabs_engine as eleven_mod
    import shattered_audio.env_local as env_local_mod

    monkeypatch.setattr(env_local_mod, "__file__", str(fake_here))

    audio_path = tmp_path / "clip.flac"
    audio_path.write_bytes(b"fake-audio")

    eleven_mod.transcribe(audio_path)
    assert captured["headers"]["xi-api-key"] == "from-env-local"


def test_elevenlabs_engine_non_200_raises_runtime_error(monkeypatch, tmp_path):
    monkeypatch.setenv("ELEVENLABS_API_KEY", "test-key")
    _install_fake_httpx(monkeypatch, _FakeResponse(500, {}, text="server exploded"))

    from shattered_audio.engines import elevenlabs_engine

    audio_path = tmp_path / "clip.flac"
    audio_path.write_bytes(b"fake-audio")

    with pytest.raises(RuntimeError, match="server exploded"):
        elevenlabs_engine.transcribe(audio_path)
