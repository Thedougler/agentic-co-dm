"""Shared agent-shaped CLI conventions for wiki operations."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

EXIT_OK = 0
EXIT_ERROR = 1
EXIT_REJECTED = 2


def repo_root(start: str | Path | None = None) -> Path:
    """Find the nearest repository root, falling back to this package root."""
    current = Path(start or Path.cwd()).expanduser().resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    return Path(__file__).resolve().parents[2]


def _dotenv_value(path: Path, key: str) -> str | None:
    if not path.is_file():
        return None
    for line in path.read_text(encoding="utf-8").splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#") or "=" not in raw:
            continue
        name, value = raw.split("=", 1)
        if name.strip() != key:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        return value
    return None


def configured_vault(start: str | Path | None = None) -> str | None:
    """Resolve the configured vault without requiring infrastructure arguments."""
    if os.environ.get("OBSIDIAN_VAULT_PATH"):
        return os.environ["OBSIDIAN_VAULT_PATH"]
    root = repo_root(start)
    for candidate in (root, *root.parents):
        value = _dotenv_value(candidate / ".env", "OBSIDIAN_VAULT_PATH")
        if value:
            return value
    global_config = Path.home() / ".obsidian-wiki" / "config"
    return _dotenv_value(global_config, "OBSIDIAN_VAULT_PATH")


def resolve_vault(raw: str | Path | None = None, *, start: str | Path | None = None) -> Path:
    candidate = raw or configured_vault(start) or "wiki"
    vault = Path(candidate).expanduser()
    if not vault.is_absolute():
        vault = repo_root(start) / vault
    vault = vault.resolve()
    if not vault.exists():
        raise ValueError(f"vault does not exist: {vault}")
    if not vault.is_dir():
        raise ValueError(f"vault is not a directory: {vault}")
    return vault


def emit_json(value: Any) -> None:
    """Emit compact deterministic JSON for agent consumption."""
    print(json.dumps(value, sort_keys=True, separators=(",", ":")))


def emit_error(message: str, *, code: int = EXIT_ERROR) -> int:
    print(json.dumps({"status": "error", "error": message}, sort_keys=True, separators=(",", ":")))
    return code
