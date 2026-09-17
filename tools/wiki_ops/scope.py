"""Typed scope parsing and vault file resolution."""
from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

SKIP_DIRS = frozenset({".obsidian", "_archive", "_archives", "_raw", "_readouts", "_staging", "_meta", "templates", "attachments"})


def _safe_relative(vault: Path, raw: str) -> Path:
    path = (vault / raw).resolve()
    try:
        path.relative_to(vault.resolve())
    except ValueError as exc:
        raise ValueError(f"scope path escapes vault: {raw}") from exc
    return path


def _files(vault: Path) -> list[Path]:
    return sorted(p for p in vault.rglob("*.md") if p.is_file() and not SKIP_DIRS.intersection(p.relative_to(vault).parts))


def _frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line and not line[:1].isspace():
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("\"'")
    return result


@dataclass
class Scope:
    kind: str
    value: Any
    resolved_files: list[str] = field(default_factory=list)

    def resolve(self, vault: str | Path) -> "Scope":
        root = Path(vault).expanduser().resolve()
        if not root.is_dir():
            raise ValueError(f"vault does not exist: {root}")
        candidates = _files(root)
        if self.kind == "files":
            raw = self.value if isinstance(self.value, list) else str(self.value).split(",")
            selected = [_safe_relative(root, item) for item in raw if str(item).strip()]
            missing = [str(item) for item in selected if not item.is_file()]
            if missing:
                raise ValueError(f"scope file not found: {', '.join(missing)}")
        elif self.kind == "directory":
            directory = _safe_relative(root, str(self.value))
            if not directory.is_dir():
                raise ValueError(f"scope directory does not exist: {self.value}")
            selected = [p for p in candidates if p.is_relative_to(directory)]
        elif self.kind == "entity_type":
            selected = [p for p in candidates if _frontmatter(p.read_text(encoding="utf-8")).get("type") == str(self.value)]
        elif self.kind == "identity_set":
            values = self.value if isinstance(self.value, list) else []
            selected = [_safe_relative(root, item.get("path", item) if isinstance(item, dict) else str(item)) for item in values]
            selected = [p for p in selected if p.is_file()]
        elif self.kind == "changed":
            proc = subprocess.run(["git", "diff", "--name-only", str(self.value)], cwd=root, capture_output=True, text=True, check=False)
            selected = [_safe_relative(root, line.strip()) for line in proc.stdout.splitlines() if line.strip().endswith(".md")]
            selected = [p for p in selected if p.is_file()]
        elif self.kind == "bundle":
            selected = candidates
        else:
            raise ValueError(f"unknown scope kind: {self.kind}")
        self.resolved_files = [p.relative_to(root).as_posix() for p in sorted(set(selected))]
        return self

    def to_dict(self) -> dict[str, Any]:
        return {"kind": self.kind, "value": self.value, "resolved_files": list(self.resolved_files)}


def parse_scope(raw: str | None) -> Scope | None:
    if not raw:
        return None
    if ":" not in raw:
        raise ValueError("scope must use kind:value syntax")
    kind, value = raw.split(":", 1)
    if kind == "files":
        value = [part for part in value.split(",") if part]
    allowed = {"files", "dir", "directory", "type", "entity_type", "identity_set", "changed", "bundle"}
    if kind not in allowed:
        raise ValueError(f"unknown scope kind: {kind}")
    return Scope({"dir": "directory", "type": "entity_type"}.get(kind, kind), value)
