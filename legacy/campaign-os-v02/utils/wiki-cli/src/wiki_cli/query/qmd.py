"""Wrapper around the external `qmd` CLI (hybrid semantic search) for the
`wiki search` command — runs `qmd query ... --format json`, parses hits,
and resolves each hit's `qmd://collection/relpath` into a repo-relative
path so it can be joined against a `Row` from `wiki_cli.query.runtime`.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from itertools import chain
from pathlib import Path

from ruamel.yaml import YAML


class QmdNotFoundError(RuntimeError):
    """The `qmd` binary is not on PATH."""


class QmdError(RuntimeError):
    """`qmd` ran but exited non-zero."""


@dataclass(frozen=True, slots=True)
class QmdHit:
    rel_path: str
    collection: str
    score: float
    line: int
    title: str
    snippet: str


def collection_roots(repo_root: Path) -> dict[str, str]:
    """Parse `utils/qmd-collections.yml` -> `{collection: repo-relative root dir}`."""
    path = repo_root / "utils" / "qmd-collections.yml"
    yaml = YAML(typ="safe")
    data = yaml.load(path.read_text(encoding="utf-8"))
    roots: dict[str, str] = {}
    for name, entry in data.get("collections", {}).items():
        raw_path = entry.get("path", "")
        cleaned = raw_path.replace("{{REPO}}/", "").replace("{{REPO}}", "")
        roots[name] = cleaned
    return roots


def run_qmd(collections: list[str], query: str, limit: int, repo_root: Path) -> list[QmdHit]:
    """Run `qmd query` across `collections` and return parsed hits.
    Raises `QmdNotFoundError` if the binary is missing, `QmdError` if it
    exits non-zero."""
    cmd = [
        "qmd",
        "query",
        query,
        "--format",
        "json",
        "-n",
        str(limit),
        *chain.from_iterable(("-c", c) for c in collections),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except FileNotFoundError as e:
        raise QmdNotFoundError(
            "wiki search needs the qmd CLI on PATH (npm i -g @tobilu/qmd)"
        ) from e
    if result.returncode != 0:
        raise QmdError(result.stderr.strip() or f"qmd exited {result.returncode}")

    hits: list[QmdHit] = []
    if not result.stdout.strip():
        return hits

    roots = collection_roots(repo_root)
    for item in json.loads(result.stdout):
        file_uri: str = item.get("file", "")
        if file_uri.startswith("qmd://"):
            rest = file_uri[len("qmd://") :]
            coll, _, rel = rest.partition("/")
        else:
            coll, rel = "", file_uri
        coll_root = roots.get(coll, "")
        full_rel = f"{coll_root}/{rel}" if coll_root else rel
        hits.append(
            QmdHit(
                rel_path=full_rel,
                collection=coll,
                score=float(item.get("score", 0.0)),
                line=int(item.get("line", 0)),
                title=str(item.get("title", "")),
                snippet=str(item.get("snippet", "")),
            )
        )
    return hits
