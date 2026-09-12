"""Load repo-root .env.local keys (API tokens) into the process environment."""

from __future__ import annotations

import os
from pathlib import Path


def find_env_local() -> Path | None:
    """Locate <repo-root>/.env.local by walking up to the enclosing git repo."""
    for parent in Path(__file__).resolve().parents:
        if (parent / ".git").is_dir():
            env_local = parent / ".env.local"
            return env_local if env_local.exists() else None
    return None


def load_env_local() -> None:
    """Read every KEY=value line from .env.local into os.environ.

    Real environment variables always win: values are applied with
    setdefault, never overwritten. Lets huggingface_hub (HF_TOKEN) and the
    ElevenLabs engine (ELEVENLABS_API_KEY) pick up repo-local credentials
    without exporting them in the shell.
    """
    env_local = find_env_local()
    if env_local is None:
        return
    for line in env_local.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        if key:
            os.environ.setdefault(key, value)
