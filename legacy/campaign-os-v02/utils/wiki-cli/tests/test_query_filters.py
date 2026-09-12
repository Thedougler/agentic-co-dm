"""Tests for wiki_cli.query.filters — --where/--sort parsing and evaluation."""

from __future__ import annotations

import pytest

from wiki_cli.query.filters import (
    COMPUTED_KEYS,
    FilterError,
    Row,
    matches,
    parse_sort,
    parse_where,
    sort_rows,
    value_of,
)


def test_parse_where_equals() -> None:
    wheres = parse_where(["type=npc"], frozenset({"type"}))
    assert wheres[0].key == "type"
    assert wheres[0].op == "="
    assert wheres[0].value == "npc"


def test_parse_where_not_equals() -> None:
    wheres = parse_where(["type!=npc"], frozenset({"type"}))
    assert wheres[0].op == "!="
    assert wheres[0].value == "npc"


def test_parse_where_tilde() -> None:
    wheres = parse_where(["type~np"], frozenset({"type"}))
    assert wheres[0].op == "~"
    assert wheres[0].value == "np"


def test_parse_where_gte() -> None:
    wheres = parse_where(["links-in>=3"], frozenset({"links-in"}) | COMPUTED_KEYS)
    assert wheres[0].op == ">="
    assert wheres[0].value == "3"


def test_parse_where_lte() -> None:
    wheres = parse_where(["links-in<=3"], frozenset({"links-in"}) | COMPUTED_KEYS)
    assert wheres[0].op == "<="
    assert wheres[0].value == "3"


def test_unknown_key_lists_legal() -> None:
    with pytest.raises(FilterError, match="tags"):
        parse_where(["bogus=1"], frozenset({"tags", "type"}))


def test_tilde_substring_on_string() -> None:
    row = Row(rel_path="a.md", frontmatter={"type": "npc"}, computed={"path": "a.md"})
    assert matches(row, parse_where(["type~np"], frozenset({"type"})))
    assert not matches(row, parse_where(["type~xyz"], frozenset({"type"})))


def test_tilde_on_list_checks_any_element() -> None:
    row = Row(
        rel_path="a.md",
        frontmatter={"tags": ["faith-horror", "undead"]},
        computed={"path": "a.md"},
    )
    assert matches(row, parse_where(["tags~horror"], frozenset({"tags"})))
    assert not matches(row, parse_where(["tags~xyz"], frozenset({"tags"})))


def test_where_membership_on_tags() -> None:
    row = Row(rel_path="a.md", frontmatter={"tags": ["horror", "faith"]}, computed={"path": "a.md"})
    assert matches(row, parse_where(["tags=faith"], frozenset({"tags"})))
    assert not matches(row, parse_where(["tags!=faith"], frozenset({"tags"})))


def test_numeric_gte() -> None:
    row = Row(rel_path="a.md", frontmatter={}, computed={"path": "a.md", "links-in": 5})
    assert matches(row, parse_where(["links-in>=3"], frozenset({"links-in"}) | COMPUTED_KEYS))
    assert not matches(row, parse_where(["links-in>=10"], frozenset({"links-in"}) | COMPUTED_KEYS))


def test_string_gte_on_dates() -> None:
    row = Row(rel_path="a.md", frontmatter={"date": "2026-08-01"}, computed={"path": "a.md"})
    assert matches(row, parse_where(["date>=2026-01-01"], frozenset({"date"})))
    assert not matches(row, parse_where(["date>=2027-01-01"], frozenset({"date"})))


def test_value_of_prefers_computed() -> None:
    row = Row(
        rel_path="a.md",
        frontmatter={"path": "wrong"},
        computed={"path": "a.md"},
    )
    assert value_of(row, "path") == "a.md"


def test_parse_sort_ascending() -> None:
    sort = parse_sort("links-in", COMPUTED_KEYS)
    assert sort == ("links-in", False)


def test_sort_descending() -> None:
    sort = parse_sort("-links-in", COMPUTED_KEYS)
    assert sort == ("links-in", True)


def test_parse_sort_none() -> None:
    assert parse_sort(None, COMPUTED_KEYS) is None


def test_parse_sort_unknown_key_raises() -> None:
    with pytest.raises(FilterError, match="path"):
        parse_sort("bogus", frozenset({"path"}))


def test_sort_missing_values_last() -> None:
    rows = [
        Row("b.md", {}, {"path": "b.md", "links-in": None}),
        Row("a.md", {}, {"path": "a.md", "links-in": 5}),
        Row("c.md", {}, {"path": "c.md", "links-in": 2}),
    ]
    sorted_rows = sort_rows(rows, ("links-in", False))
    assert [r.rel_path for r in sorted_rows] == ["c.md", "a.md", "b.md"]


def test_sort_missing_values_last_descending() -> None:
    rows = [
        Row("b.md", {}, {"path": "b.md", "links-in": None}),
        Row("a.md", {}, {"path": "a.md", "links-in": 5}),
        Row("c.md", {}, {"path": "c.md", "links-in": 2}),
    ]
    sorted_rows = sort_rows(rows, ("links-in", True))
    assert [r.rel_path for r in sorted_rows] == ["a.md", "c.md", "b.md"]


def test_sort_none_returns_rows_unchanged() -> None:
    rows = [Row("b.md", {}, {"path": "b.md"}), Row("a.md", {}, {"path": "a.md"})]
    assert sort_rows(rows, None) == rows
