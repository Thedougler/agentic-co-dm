"""Helpers for root instruction files that may point at another file."""

from __future__ import annotations

from pathlib import Path


def resolve_at_pointer_text(raw: str, repo_root: Path) -> str:
    pointer = raw.strip()
    if not pointer.startswith("@") or "\n" in pointer:
        return raw

    target = repo_root / pointer[1:]
    try:
        if target.is_file():
            return target.read_text(encoding="utf-8")
    except OSError:
        return raw
    return raw
