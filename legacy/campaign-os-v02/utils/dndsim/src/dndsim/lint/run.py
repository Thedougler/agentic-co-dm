"""Discovers dndsim's scoped corpus and builds the merged JSON payload
(ADR-0010) the ``dndsim lint`` CLI command emits.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from dndsim.lint.findings import Finding, build_payload
from dndsim.lint.rules import lint_file

# utils/dndsim/src/dndsim/lint/run.py -> repo root is 5 parents up (lint,
# dndsim pkg, src, utils/dndsim project, utils) — same computation
# differential_harness.py uses from its own location.
REPO_ROOT: Path = Path(__file__).resolve().parents[5]


def _default_corpus() -> list[Path]:
    """Every file either rule scopes to, when no explicit files are given —
    mirrors markdownlint-obsidian's own full-corpus-sweep behavior."""
    files: list[Path] = []
    monster_dirs = (
        REPO_ROOT / "vault" / "srd" / "monsters",
        REPO_ROOT / "vault" / "campaigns" / "shattered-sea" / "monsters",
    )
    for d in monster_dirs:
        if d.exists():
            files += sorted(d.glob("*.md"))
    dm_intel = REPO_ROOT / "vault" / "campaigns" / "shattered-sea" / "pcs" / "character-sheets"
    if dm_intel.exists():
        # Recursive: the retired-```combatant-fence check and the
        # character-sheet checks both apply to any depth under
        # character-sheets/, not just its top level.
        files += sorted(p for p in dm_intel.rglob("*.md") if p.is_file())
    return files


def _rel(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def lint_paths(files: list[Path] | None) -> list[dict[str, Any]]:
    """Lint the given files, or dndsim's whole scoped corpus if none are
    given. Returns the markdownlint-obsidian-shaped JSON payload."""
    targets = list(files) if files else _default_corpus()
    results: list[tuple[Path, list[Finding]]] = []
    for path in targets:
        results.append((path, lint_file(path, _rel(path))))
    return build_payload(results)
