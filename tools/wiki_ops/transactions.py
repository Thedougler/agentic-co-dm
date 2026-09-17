"""All-or-nothing mutation transactions with deferred finalization."""
from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from .manifest_ops import ManifestTransition, apply_transition
from .mutations import MutationOp, atomic_write, resolve_mutation, validate_non_overlapping

@dataclass
class Validation:
    failures: list[str] = field(default_factory=list)
    results: list[dict[str, Any]] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return not self.failures


class Transaction:
    def __init__(self, vault: str | Path, *, qmd_runner: Callable[[], int] | None = None):
        self.vault = Path(vault).resolve()
        self.operations: list[MutationOp] = []
        self.qmd_runner = qmd_runner
        self._resolved: dict[Path, str] = {}
        self._originals: dict[Path, str] = {}
        self.status = "pending"

    def add(self, operation: MutationOp | dict[str, Any]) -> "Transaction":
        self.operations.append(operation if isinstance(operation, MutationOp) else MutationOp.from_dict(operation))
        return self

    def validate(self) -> Validation:
        validation = Validation(failures=validate_non_overlapping(self.operations))
        if validation.failures:
            return validation
        for op in self.operations:
            path = self.vault / op.target
            if not path.is_file():
                validation.failures.append(f"file_not_found: {op.target}")
                continue
            try:
                original = self._originals.setdefault(path, path.read_text(encoding="utf-8"))
                current = self._resolved.get(path, original)
                result, diff = resolve_mutation(self.vault, op, current)
                self._resolved[path] = result
                validation.results.append({"kind": op.kind, "target": op.target, "diff": diff})
            except (OSError, ValueError) as exc:
                validation.failures.append(f"{op.target}: {exc}")
        return validation

    def commit(self) -> dict[str, Any]:
        validation = self.validate()
        if not validation.valid:
            self.status = "failed"
            return {"status": "rejected", "mutations_valid": 0, "mutations_invalid": len(validation.failures), "failures": validation.failures}
        written: list[Path] = []
        try:
            for path, text in self._resolved.items():
                atomic_write(path, text)
                written.append(path)
        except BaseException as exc:
            for path in written:
                if path in self._originals:
                    atomic_write(path, self._originals[path])
            self.status = "failed"
            return {"status": "failed", "error": str(exc), "files_changed": [str(p.relative_to(self.vault)) for p in written]}
        self.status = "committed"
        return {"status": "committed", "mutations_applied": len(self.operations), "files_changed": [str(p.relative_to(self.vault)) for p in self._resolved]}

    def finalize(self) -> dict[str, Any]:
        if self.status != "committed":
            return {"status": self.status, "finalization": {}}
        finalization: dict[str, Any] = {"index_updated": False, "manifest_updated": False, "qmd_refreshed": False, "qmd_exit_code": None}
        try:
            for op in self.operations:
                if op.kind == "update_manifest_identity":
                    manifest = self.vault / ".manifest.json"
                    data = __import__("json").loads(manifest.read_text(encoding="utf-8"))
                    transition = ManifestTransition(str(op.payload.get("page_path", op.target)), str(op.payload.get("transition")), op.payload.get("target"), op.payload.get("reason"))
                    from .manifest_ops import update_manifest
                    update_manifest(manifest, transition)
                    finalization["manifest_updated"] = True
            runner = self.qmd_runner
            if runner is None:
                script = self.vault.parent / "scripts" / "qmd-maintain.sh"
                if script.is_file():
                    runner = lambda: subprocess.run([str(script)], cwd=self.vault.parent, check=False).returncode
            if runner is not None:
                code = int(runner())
                finalization["qmd_exit_code"] = code
                finalization["qmd_refreshed"] = code == 0
                if code != 0:
                    self.status = "committed"
                    return {"status": "committed", "finalization": finalization, "error": "finalization_failed"}
            self.status = "finalized"
            return {"status": "finalized", "finalization": finalization}
        except (OSError, ValueError, KeyError) as exc:
            self.status = "committed"
            return {"status": "committed", "finalization": finalization, "error": str(exc)}

    def preview(self) -> dict[str, Any]:
        validation = self.validate()
        return {"status": "preview" if validation.valid else "rejected", "mutations_valid": len(validation.results), "mutations_invalid": len(validation.failures), "diffs": validation.results, "failures": validation.failures}

    def __enter__(self) -> "Transaction":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is not None:
            self.status = "failed"
            return
        result = self.commit()
        if result.get("status") == "committed":
            self.finalize()
