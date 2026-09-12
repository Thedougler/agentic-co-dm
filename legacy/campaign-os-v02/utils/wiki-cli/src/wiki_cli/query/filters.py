"""Shared `--where`/`--sort` parsing and evaluation for the read-layer CLI
commands (`wiki list`, `wiki search`, `wiki links`)."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass

COMPUTED_KEYS = frozenset({"path", "links-in", "links-out", "pagerank", "mtime"})

# Order matters: `!=`, `>=`, `<=` must be tried before the bare `=` operator,
# since `=` is a prefix of none of them but a greedy `=`-first alternation
# would still need this ordering to read correctly.
_WHERE_RE = re.compile(r"^([A-Za-z_-]+)(!=|>=|<=|~|=)(.*)$")


class FilterError(ValueError):
    """Bad `--where`/`--sort` input; message lists legal keys."""


@dataclass(frozen=True, slots=True)
class Where:
    key: str
    op: str
    value: str


@dataclass(frozen=True, slots=True)
class Row:
    """One result row: a page plus its computed values, ready to filter,
    sort, and render."""

    rel_path: str
    frontmatter: Mapping[str, object]
    computed: Mapping[str, object]


def _legal_keys_message(legal_keys: frozenset[str]) -> str:
    return f"legal keys: {', '.join(sorted(legal_keys))}"


def parse_where(raw: list[str], legal_keys: frozenset[str]) -> list[Where]:
    """Parse each `--where` clause (e.g. `type=npc`, `links-in>=3`) into a
    `Where`. Raises `FilterError` on a malformed clause or an unknown key."""
    wheres: list[Where] = []
    for clause in raw:
        match = _WHERE_RE.match(clause)
        if not match:
            raise FilterError(
                f"malformed --where clause: {clause!r} ({_legal_keys_message(legal_keys)})"
            )
        key, op, value = match.group(1), match.group(2), match.group(3)
        if key not in legal_keys:
            raise FilterError(f"unknown --where key: {key!r} ({_legal_keys_message(legal_keys)})")
        wheres.append(Where(key=key, op=op, value=value))
    return wheres


def parse_sort(raw: str | None, legal_keys: frozenset[str]) -> tuple[str, bool] | None:
    """Parse a `--sort` argument. A leading `-` means descending. Returns
    `None` when `raw` is `None`. Raises `FilterError` on an unknown key."""
    if raw is None:
        return None
    descending = raw.startswith("-")
    key = raw[1:] if descending else raw
    if key not in legal_keys:
        raise FilterError(f"unknown --sort key: {key!r} ({_legal_keys_message(legal_keys)})")
    return key, descending


def value_of(row: Row, key: str) -> object:
    """The value of `key` on `row` — computed values take precedence over
    frontmatter, since computed keys (e.g. `path`) can shadow a frontmatter
    key of the same name."""
    if key in row.computed:
        return row.computed[key]
    return row.frontmatter.get(key)


def _as_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return None
    return None


def _matches_one(row: Row, where: Where) -> bool:
    actual = value_of(row, where.key)

    if where.op == "~":
        needle = where.value.lower()
        if isinstance(actual, list):
            return any(needle in str(item).lower() for item in actual)
        return actual is not None and needle in str(actual).lower()

    if where.op in ("=", "!="):
        if isinstance(actual, list):
            is_member = any(str(item) == where.value for item in actual)
        else:
            is_member = actual is not None and str(actual) == where.value
        return is_member if where.op == "=" else not is_member

    # >= and <=
    if actual is None:
        return False
    actual_num = _as_float(actual)
    target_num = _as_float(where.value)
    if actual_num is not None and target_num is not None:
        if where.op == ">=":
            return actual_num >= target_num
        return actual_num <= target_num
    left_s, right_s = str(actual), where.value
    if where.op == ">=":
        return left_s >= right_s
    return left_s <= right_s


def matches(row: Row, wheres: list[Where]) -> bool:
    """True when `row` satisfies every clause in `wheres` (AND semantics)."""
    return all(_matches_one(row, where) for where in wheres)


def sort_rows(rows: list[Row], sort: tuple[str, bool] | None) -> list[Row]:
    """`rows` sorted by `sort`'s key, missing values always last regardless
    of direction. `sort` of `None` returns `rows` unchanged."""
    if sort is None:
        return rows
    key, descending = sort

    def sort_key(row: Row) -> tuple[bool, object]:
        value = value_of(row, key)
        if value is None:
            return (True, 0.0)
        num = _as_float(value)
        return (False, num if num is not None else str(value))

    missing = [row for row in rows if value_of(row, key) is None]
    present = [row for row in rows if value_of(row, key) is not None]
    present.sort(key=sort_key, reverse=descending)
    return present + missing
