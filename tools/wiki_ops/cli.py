"""Shared agent-shaped CLI conventions for wiki operations."""
from __future__ import annotations

import argparse
import json
import sys
import os
from pathlib import Path
from typing import Any

EXIT_OK = 0
EXIT_ERROR = 1
EXIT_REJECTED = 2


PACKAGE_ROOT = Path(__file__).resolve().parents[2]
SCOPE_KINDS = "files|directory(dir)|entity_type(type)|identity_set|changed|bundle"


def repo_root(start: str | Path | None = None) -> Path:
    """The repository root: the nearest .git above `start`, which defaults to this package (never the cwd)."""
    current = Path(start or PACKAGE_ROOT).expanduser().resolve()
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
    """Vault order after --vault: OBSIDIAN_VAULT_PATH > repo .env > <repo>/wiki > ~/.obsidian-wiki/config."""
    if os.environ.get("OBSIDIAN_VAULT_PATH"):
        return os.environ["OBSIDIAN_VAULT_PATH"]
    root = repo_root(start)
    value = _dotenv_value(root / ".env", "OBSIDIAN_VAULT_PATH")
    if value:
        return value
    if (root / "wiki").is_dir():
        return str(root / "wiki")
    return _dotenv_value(Path.home() / ".obsidian-wiki" / "config", "OBSIDIAN_VAULT_PATH")


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


def usage_error(error: str, *, hint: str, example: str, list_valid: str) -> int:
    """The FR-035 error object: JSON on stdout, the same message on stderr, exit 2."""
    emit_json({"status": "error", "error": error, "hint": hint, "example": example, "list_valid": list_valid})
    print(f"error: {error}", flush=True, file=sys.stderr)
    return EXIT_REJECTED


class UsageError(ValueError):
    """Invalid input: reported as the FR-035 error object (exit 2)."""

    def __init__(self, error: str, *, hint: str, example: str, list_valid: str | None = None):
        super().__init__(error)
        self.hint, self.example, self.list_valid = hint, example, list_valid


def examples_epilog(*lines: str) -> str:
    return "Examples:\n" + "\n".join(f"  {line}" for line in lines)


class AgentParser(argparse.ArgumentParser):
    """Usage errors become UsageError. Set exit_on_usage=False to let the caller format (wiki --pretty)."""

    def __init__(self, *args, example: str | None = None, exit_on_usage: bool = True, **kwargs):
        kwargs.setdefault("formatter_class", argparse.RawDescriptionHelpFormatter)
        super().__init__(*args, **kwargs)
        self.example = example
        self.exit_on_usage = exit_on_usage

    def error(self, message: str) -> None:  # type: ignore[override]
        exc = UsageError(
            message,
            hint=f"run {self.prog} --help",
            example=self.example or f"{self.prog} --help",
            list_valid=f"{self.prog} --help",
        )
        if self.exit_on_usage:
            raise SystemExit(usage_error(str(exc), hint=exc.hint, example=exc.example, list_valid=exc.list_valid or f"{self.prog} --help"))
        raise exc
