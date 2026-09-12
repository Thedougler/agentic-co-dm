"""Shared rendering for the read-layer CLI commands (`tsv`, `paths`, `json`)."""

from __future__ import annotations

import json

from wiki_cli.query.filters import Row, value_of

DEFAULT_COLUMNS = ["path", "type"]


def _cell(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ",".join(str(item) for item in value)
    return str(value)


def _render_tsv(rows: list[Row], columns: list[str] | None) -> str:
    cols = columns if columns is not None else DEFAULT_COLUMNS
    lines = ["\t".join(cols)]
    for row in rows:
        lines.append("\t".join(_cell(value_of(row, col)) for col in cols))
    return "\n".join(lines) + "\n"


def _render_paths(rows: list[Row]) -> str:
    return "".join(f"{row.rel_path}\n" for row in rows)


def _render_json(rows: list[Row]) -> str:
    payload = [{"path": row.rel_path, **row.frontmatter, **row.computed} for row in rows]
    return json.dumps(payload, indent=2)


def render(rows: list[Row], fmt: str, columns: list[str] | None) -> str:
    """Render `rows` in `fmt` (`tsv`, `paths`, or `json`). `columns` is only
    used by `tsv`; defaults to `DEFAULT_COLUMNS` when `None`."""
    if fmt == "tsv":
        return _render_tsv(rows, columns)
    if fmt == "paths":
        return _render_paths(rows)
    if fmt == "json":
        return _render_json(rows)
    raise ValueError(f"unknown output format: {fmt!r}")
