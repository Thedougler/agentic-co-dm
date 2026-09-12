"""Tests for W138 — item page missing the `unique:` frontmatter key."""

from __future__ import annotations

from wiki_cli.contracts import Page
from wiki_cli.rules.item_unique_missing import ItemUniqueMissingRule

RULE_ID = "W138"

_BASE_ITEM: dict[str, object] = {
    "type": "item",
    "status": "draft",
    "publish": False,
    "aliases": [],
    "summary": "A test item.",
    "created": "2026-08-13",
    "updated": "2026-08-13",
    "tags": [],
    "tier": "supporting",
    "rarity": "common",
    "attunement": False,
    "unique": False,
    "form": "wondrous item",
    "found_at": [],
    "value": "50 gp",
    "campaigns": [],
    "reference_image": "",
    "uid": "aaaaaaaa-0000-0000-0000-000000000001",
}


def _page(rel_path: str, frontmatter: dict[str, object]) -> Page:
    return Page(
        rel_path=rel_path,
        raw="",
        frontmatter=frontmatter,
        body="# Test Item\n",
        body_start_line=len(frontmatter) + 2,
    )


class _StubCorpus:
    repo_root = None  # type: ignore[assignment]


def test_item_with_unique_false_yields_no_finding() -> None:
    page = _page(
        "vault/campaigns/shattered-sea/items/common/test-item.md",
        dict(_BASE_ITEM),
    )
    findings = list(ItemUniqueMissingRule().check(page, _StubCorpus()))  # type: ignore[arg-type]
    assert findings == []


def test_item_with_unique_true_yields_no_finding() -> None:
    frontmatter = dict(_BASE_ITEM)
    frontmatter["unique"] = True
    page = _page(
        "vault/campaigns/shattered-sea/items/rare/test-unique-item.md",
        frontmatter,
    )
    findings = list(ItemUniqueMissingRule().check(page, _StubCorpus()))  # type: ignore[arg-type]
    assert findings == []


def test_item_missing_unique_yields_one_finding() -> None:
    frontmatter = {k: v for k, v in _BASE_ITEM.items() if k != "unique"}
    page = _page(
        "vault/campaigns/shattered-sea/items/uncommon/fios-own-curtain.md",
        frontmatter,
    )
    findings = list(ItemUniqueMissingRule().check(page, _StubCorpus()))  # type: ignore[arg-type]
    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == RULE_ID
    assert "unique" in finding.message


def test_non_item_page_missing_unique_yields_no_finding() -> None:
    frontmatter: dict[str, object] = {
        "type": "npc",
        "status": "draft",
        "publish": False,
        "summary": "A test NPC.",
        "created": "2026-08-13",
        "updated": "2026-08-13",
        "tags": [],
        "uid": "aaaaaaaa-0000-0000-0000-000000000002",
    }
    page = _page(
        "vault/campaigns/shattered-sea/npcs/test-npc.md",
        frontmatter,
    )
    findings = list(ItemUniqueMissingRule().check(page, _StubCorpus()))  # type: ignore[arg-type]
    assert findings == []


def test_finding_is_fixable() -> None:
    frontmatter = {k: v for k, v in _BASE_ITEM.items() if k != "unique"}
    page = _page(
        "vault/campaigns/shattered-sea/items/uncommon/fios-own-curtain.md",
        frontmatter,
    )
    findings = list(ItemUniqueMissingRule().check(page, _StubCorpus()))  # type: ignore[arg-type]
    assert len(findings) == 1
    assert findings[0].fixable is True
