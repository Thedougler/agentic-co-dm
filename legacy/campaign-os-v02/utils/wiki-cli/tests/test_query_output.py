"""Tests for wiki_cli.query.output — tsv/paths/json rendering."""

from __future__ import annotations

import json

from wiki_cli.query.filters import Row
from wiki_cli.query.output import render


def test_tsv_header_and_columns() -> None:
    rows = [Row("a.md", {"type": "npc"}, {"path": "a.md"})]
    out = render(rows, "tsv", ["path", "type"])
    lines = out.strip().splitlines()
    assert lines[0] == "path\ttype"
    assert lines[1] == "a.md\tnpc"


def test_tsv_default_columns() -> None:
    rows = [Row("a.md", {"type": "npc"}, {"path": "a.md"})]
    out = render(rows, "tsv", None)
    lines = out.strip().splitlines()
    assert lines[0] == "path\ttype"
    assert lines[1] == "a.md\tnpc"


def test_paths_format() -> None:
    rows = [Row("a.md", {}, {"path": "a.md"}), Row("b.md", {}, {"path": "b.md"})]
    out = render(rows, "paths", None)
    assert out.strip().splitlines() == ["a.md", "b.md"]


def test_json_roundtrips() -> None:
    rows = [Row("a.md", {"type": "npc"}, {"path": "a.md", "links-in": 3})]
    data = json.loads(render(rows, "json", None))
    assert data[0]["path"] == "a.md"
    assert data[0]["type"] == "npc"
    assert data[0]["links-in"] == 3


def test_tsv_list_comma_joined() -> None:
    rows = [Row("a.md", {"tags": ["horror", "faith"]}, {"path": "a.md"})]
    out = render(rows, "tsv", ["path", "tags"])
    assert "horror,faith" in out


def test_tsv_missing_value_empty() -> None:
    rows = [Row("a.md", {}, {"path": "a.md"})]
    out = render(rows, "tsv", ["path", "type"])
    lines = out.splitlines()
    assert lines[1] == "a.md\t"
