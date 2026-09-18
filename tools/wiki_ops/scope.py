"""Typed scope parsing and vault file resolution."""
from __future__ import annotations

import subprocess
from dataclasses import asdict, dataclass, field, is_dataclass
from pathlib import Path
from typing import Any, Literal

SKIP_DIRS = frozenset(
    {".obsidian", "_archive", "_archives", "_raw", "_readouts", "_staging", "_meta", "templates", "attachments"}
)
ScopeKind = Literal["files", "directory", "entity_type", "identity_set", "changed", "bundle"]
_ALIASES = {"dir": "directory", "type": "entity_type"}
_KINDS = frozenset(ScopeKind.__args__)


def _safe_relative(vault: Path, raw: str | Path) -> Path:
    """Resolve a vault-relative path, rejecting traversal and absolute paths."""
    text = str(raw).strip()
    if not text:
        raise ValueError("scope path must not be empty")
    candidate_input = Path(text)
    if candidate_input.is_absolute():
        raise ValueError(f"scope path must be vault-relative: {text!r}")
    vault_root = vault.resolve()
    candidate = (vault_root / candidate_input).resolve()
    try:
        candidate.relative_to(vault_root)
    except ValueError as exc:
        raise ValueError(f"scope path escapes vault: {text!r}") from exc
    return candidate


def _is_skipped(path: Path, vault: Path) -> bool:
    return bool(SKIP_DIRS.intersection(path.relative_to(vault).parts))


def _files(vault: Path) -> list[Path]:
    root = vault.resolve()
    result: list[Path] = []
    for path in vault.rglob("*"):
        if not path.is_file() or path.suffix.casefold() != ".md" or _is_skipped(path, vault):
            continue
        try:
            path.resolve().relative_to(root)
        except ValueError:
            continue
        result.append(path)
    return sorted(result)


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


def _markdown_file(vault: Path, raw: str | Path, *, label: str = "scope file") -> Path:
    path = _safe_relative(vault, raw)
    if not path.is_file():
        raise ValueError(f"{label} not found in vault: {str(raw).strip()!r}")
    if path.suffix.casefold() != ".md":
        raise ValueError(f"{label} must be a Markdown file: {str(raw).strip()!r}")
    if _is_skipped(path, vault):
        raise ValueError(f"{label} is in a skipped directory: {str(raw).strip()!r}")
    return path


def _bundle_registry(vault: Path) -> tuple[Any, Path]:
    """Load the repository-owned bundle registry nearest to the vault."""
    candidates = [
        vault.parent / "rules" / "bundles.yml",
        vault.parent.parent / "rules" / "bundles.yml",
        Path(__file__).resolve().parents[2] / "rules" / "bundles.yml",
    ]
    for config in dict.fromkeys(path.resolve() for path in candidates):
        if config.is_file():
            from tools.creative_lint.bundles import BundleRegistry

            try:
                return BundleRegistry.load(config), config
            except (OSError, ValueError) as exc:
                raise ValueError(f"invalid bundle registry {config}: {exc}") from exc
    raise ValueError("bundle registry not found; expected rules/bundles.yml near the vault")


def _identity_path(identity: Any) -> str:
    if isinstance(identity, dict):
        path = identity.get("path")
    else:
        path = getattr(identity, "path", None)
    if path is None and isinstance(identity, (str, Path)):
        path = identity
    if not isinstance(path, (str, Path)) or not str(path).strip():
        raise ValueError("identity_set entries must contain a non-empty path")
    return str(path)


@dataclass
class Scope:
    kind: ScopeKind | str
    value: Any
    resolved_files: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        kind = _ALIASES.get(str(self.kind).strip(), str(self.kind).strip())
        if kind not in _KINDS:
            allowed = ", ".join(sorted(_KINDS))
            raise ValueError(f"unknown scope kind {self.kind!r}; expected one of: {allowed}")
        self.kind = kind  # type: ignore[assignment]

    def resolve(self, vault: str | Path) -> "Scope":
        root = Path(vault).expanduser().resolve()
        if not root.is_dir():
            raise ValueError(f"vault does not exist or is not a directory: {root}")
        candidates = _files(root)

        if self.kind == "files":
            raw = self.value if isinstance(self.value, (list, tuple)) else str(self.value).split(",")
            if not raw:
                raise ValueError("files scope requires at least one path")
            selected = [_markdown_file(root, item) for item in raw if str(item).strip()]
            if len(selected) != len(raw):
                raise ValueError("files scope contains an empty path")
        elif self.kind == "directory":
            value = str(self.value).strip()
            if not value:
                raise ValueError("directory scope requires a directory path")
            directory = _safe_relative(root, value)
            if not directory.is_dir():
                raise ValueError(f"scope directory does not exist in vault: {value!r}")
            selected = [path for path in candidates if path.is_relative_to(directory)]
        elif self.kind == "entity_type":
            value = str(self.value).strip()
            if not value:
                raise ValueError("entity_type scope requires a frontmatter type")
            wanted = value.casefold()
            selected = [
                path
                for path in candidates
                if _frontmatter(path.read_text(encoding="utf-8")).get("type", "").strip().casefold() == wanted
            ]
        elif self.kind == "identity_set":
            if not isinstance(self.value, (list, tuple, set, frozenset)) or not self.value:
                raise ValueError("identity_set scope requires a non-empty list of identities")
            selected = [
                _markdown_file(root, _identity_path(identity), label="identity_set path")
                for identity in self.value
            ]
        elif self.kind == "changed":
            ref = str(self.value).strip()
            if not ref:
                raise ValueError("changed scope requires a git diff target (for example, HEAD~1)")
            if ref.startswith("-"):
                raise ValueError(f"invalid git diff target: {ref!r}")
            try:
                proc = subprocess.run(
                    ["git", "diff", "--name-only", "--relative", "--no-renames", ref, "--"],
                    cwd=root,
                    capture_output=True,
                    text=True,
                    check=False,
                )
            except OSError as exc:
                raise ValueError(f"unable to run git diff for changed scope: {exc}") from exc
            if proc.returncode:
                detail = proc.stderr.strip() or f"git exited with status {proc.returncode}"
                raise ValueError(f"unable to resolve changed scope {ref!r}: {detail}")
            selected = []
            for line in proc.stdout.splitlines():
                raw = line.strip()
                if not raw or not raw.casefold().endswith(".md"):
                    continue
                path = _safe_relative(root, raw)
                if path.is_file() and not _is_skipped(path, root):
                    selected.append(path)
        elif self.kind == "bundle":
            bundle_name = str(self.value).strip()
            if not bundle_name:
                raise ValueError("bundle scope requires a bundle name")
            registry, config = _bundle_registry(root)
            try:
                registry.get(bundle_name)
            except KeyError as exc:
                available = ", ".join(registry.available())
                raise ValueError(
                    f"unknown bundle {bundle_name!r} in {config}; available bundles: {available}"
                ) from exc
            # Bundles select lint rules; their file surface is the complete vault.
            selected = candidates
        else:  # guarded by __post_init__; retained for type-checkers
            raise ValueError(f"unknown scope kind: {self.kind!r}")

        self.resolved_files = sorted({path.relative_to(root).as_posix() for path in selected})
        return self

    def to_dict(self) -> dict[str, Any]:
        def serialise(value: Any) -> Any:
            if is_dataclass(value):
                return serialise(asdict(value))
            if isinstance(value, dict):
                return {str(key): serialise(item) for key, item in value.items()}
            if isinstance(value, (list, tuple, set, frozenset)):
                return [serialise(item) for item in value]
            if isinstance(value, Path):
                return value.as_posix()
            return value

        return {"kind": self.kind, "value": serialise(self.value), "resolved_files": list(self.resolved_files)}


def parse_scope(raw: str | None) -> Scope | None:
    if raw is None or not raw.strip():
        return None
    if ":" not in raw:
        # ponytail: bare .md path → files:path shorthand (e-45)
        if raw.strip().endswith(".md"):
            return Scope("files", [raw.strip()])
        raise ValueError("scope must use kind:value syntax (for example, dir:entities, or a bare .md path)")
    kind, value = (part.strip() for part in raw.split(":", 1))
    if not kind:
        raise ValueError("scope kind must not be empty")
    canonical = _ALIASES.get(kind, kind)
    if canonical not in _KINDS:
        allowed = ", ".join(sorted(_KINDS | set(_ALIASES)))
        raise ValueError(f"unknown scope kind {kind!r}; expected one of: {allowed}")
    if not value:
        raise ValueError(f"{kind} scope requires a value")
    if canonical == "files":
        values = [part.strip() for part in value.split(",")]
        if not all(values):
            raise ValueError("files scope contains an empty path")
        value = values
    return Scope(canonical, value)
