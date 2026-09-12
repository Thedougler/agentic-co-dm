"""Unit tests for wiki_cli.query.schema — extracted W84 template parsing."""

from __future__ import annotations

from pathlib import Path

from wiki_cli.query.schema import all_templates, legal_filter_keys, resolve_template, template_keys


def test_template_keys_optional_marker() -> None:
    fm = "type: npc\ntitle:  # OPTIONAL\ntags: []"
    required, allowed = template_keys(fm)
    assert required == frozenset({"type", "tags"})
    assert allowed == frozenset({"type", "title", "tags"})


def test_resolve_template_subtype_beats_bare(tmp_path: Path) -> None:
    (tmp_path / "_shop.md").write_text("---\ntype: shop\n---\n", encoding="utf-8")
    (tmp_path / "_shop_smith.md").write_text("---\ntype: shop\n---\n", encoding="utf-8")
    assert resolve_template(tmp_path, "shop", "smith") == tmp_path / "_shop_smith.md"
    assert resolve_template(tmp_path, "shop", None) == tmp_path / "_shop.md"


def test_legal_filter_keys_unions_templates(tmp_path: Path) -> None:
    (tmp_path / "_npc.md").write_text("---\ntype: npc\nfaction:\n---\n", encoding="utf-8")
    (tmp_path / "_shop.md").write_text("---\ntype: shop\nwares:\n---\n", encoding="utf-8")
    assert {"type", "faction", "wares"} <= legal_filter_keys(tmp_path)


def test_all_templates_missing_dir_is_empty(tmp_path: Path) -> None:
    assert all_templates(tmp_path / "nope") == []
