"""Shared tiktoken counters for wiki/context tooling (issues #86 / #88).

Method of record: docs/agents/token-measurement.md

Anything labeled tokens MUST use this helper (or scripts/token-count.py).
Never label bytes as tokens. Default encoding: cl100k_base.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

DEFAULT_ENCODING = "cl100k_base"

_ENV_ENCODING = "WIKI_TOKEN_ENCODING"


def resolve_encoding(cli: str | None = None) -> str:
    """CLI --encoding > env WIKI_TOKEN_ENCODING > DEFAULT_ENCODING."""
    if cli:
        return cli.strip()
    env = (os.environ.get(_ENV_ENCODING) or "").strip()
    if env:
        return env
    return DEFAULT_ENCODING


def get_encoding(name: str) -> Any:
    """Wrap tiktoken.get_encoding(name)."""
    import tiktoken

    return tiktoken.get_encoding(name)


def count_text(text: str, encoding: str | None = None) -> int:
    """Return tiktoken token count for a Unicode string."""
    enc_name = resolve_encoding(encoding)
    enc = get_encoding(enc_name)
    return len(enc.encode(text))


def count_bytes(data: bytes, encoding: str | None = None) -> int:
    """Decode UTF-8 (errors=replace) then count tokens. Bytes are never tokens."""
    text = data.decode("utf-8", errors="replace")
    return count_text(text, encoding=encoding)


def count_file(path: Path, encoding: str | None = None) -> dict[str, Any]:
    """Count tokens and byte size for a file.

    Returns dict with keys: path (str), tokens (int), bytes (int).
    Never labels bytes as tokens.
    """
    p = Path(path)
    data = p.read_bytes()
    return {
        "path": str(p),
        "tokens": count_bytes(data, encoding=encoding),
        "bytes": len(data),
    }
