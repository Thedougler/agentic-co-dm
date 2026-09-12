"""TDD for W135 — frontmatter value validation via Pydantic models.

A page with a governed field set to an invalid value (wrong enum, wrong type)
surfaces a W135 finding. A page with valid frontmatter surfaces none.
Unknown or missing `type:` silently produces no findings (no false positives).

Tests build `Page` objects in memory — no fixture files needed, since the rule
depends only on the page's frontmatter dict (pure value-checking, no template
filesystem walk).
"""

from __future__ import annotations

from wiki_cli.contracts import Page
from wiki_cli.rules.frontmatter_values import FrontmatterValuesRule

RULE_ID = "W135"

_BASE_FM: dict[str, object] = {
    "type": "npc",
    "status": "draft",
    "publish": False,
    "aliases": [],
    "tags": [],
    "summary": "A test NPC.",
    "created": "2026-08-11",
    "updated": "2026-08-11",
    "uid": "0361b6c0-ff6f-4069-86b5-127881b00f8e",
    "subtype": "minor",
}


def _page(frontmatter: dict[str, object], page_type: str = "npc") -> Page:
    fm = dict(frontmatter)
    fm["type"] = page_type
    return Page(
        rel_path=f"vault/campaigns/shattered-sea/npcs/test-{page_type}.md",
        raw="",
        frontmatter=fm,
        body="# Test\n",
        body_start_line=len(fm) + 2,
    )


class _StubCorpus:
    repo_root = None  # type: ignore[assignment]


_CORPUS = _StubCorpus()


# --- unknown / missing type -----------------------------------------------


def test_unknown_type_yields_no_findings() -> None:
    fm = {"type": "totally-unknown-type", "status": "draft"}
    page = Page(
        rel_path="vault/test.md",
        raw="",
        frontmatter=fm,
        body="",
        body_start_line=3,
    )
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert findings == []


def test_missing_type_yields_no_findings() -> None:
    fm: dict[str, object] = {"status": "draft"}
    page = Page(
        rel_path="vault/test.md",
        raw="",
        frontmatter=fm,
        body="",
        body_start_line=3,
    )
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert findings == []


# --- status enum -----------------------------------------------------------


def test_invalid_status_yields_finding() -> None:
    fm = dict(_BASE_FM)
    fm["status"] = "not-a-valid-status"
    page = _page(fm)
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert len(findings) == 1
    assert findings[0].rule_id == RULE_ID
    assert "status" in findings[0].message


def test_valid_status_draft_yields_no_finding() -> None:
    fm = dict(_BASE_FM)
    fm["status"] = "draft"
    page = _page(fm)
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert findings == []


def test_valid_status_canon_yields_no_finding() -> None:
    fm = dict(_BASE_FM)
    fm["status"] = "canon"
    page = _page(fm)
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert findings == []


# --- publish bool ----------------------------------------------------------


def test_invalid_publish_string_yields_finding() -> None:
    fm = dict(_BASE_FM)
    fm["publish"] = "maybe"  # not a bool-coercible string
    page = _page(fm)
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert any(f.rule_id == RULE_ID and "publish" in f.message for f in findings)


def test_valid_publish_false_yields_no_finding() -> None:
    fm = dict(_BASE_FM)
    fm["publish"] = False
    page = _page(fm)
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert findings == []


# --- tier enum (standard types) -------------------------------------------


def test_invalid_tier_yields_finding() -> None:
    fm: dict[str, object] = {
        "type": "location",
        "status": "draft",
        "publish": False,
        "aliases": [],
        "tags": [],
        "summary": "A test location.",
        "created": "2026-08-11",
        "updated": "2026-08-11",
        "uid": "c69466f8-31d5-498a-a7a6-5ccc4bf0d538",
        "subtype": "building",
        "tier": "ultra-important",  # invalid
        "within": "[[somewhere]]",
        "north_of": "[[north]]",
        "east_of": "[[east]]",
        "south_of": "[[south]]",
        "west_of": "[[west]]",
        "geography": ["coastal"],
    }
    page = _page(fm, "location")
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert any(f.rule_id == RULE_ID and "tier" in f.message for f in findings)


def test_valid_tier_supporting_yields_no_finding() -> None:
    fm: dict[str, object] = {
        "type": "location",
        "status": "draft",
        "publish": False,
        "aliases": [],
        "tags": [],
        "summary": "A test location.",
        "created": "2026-08-11",
        "updated": "2026-08-11",
        "uid": "c69466f8-31d5-498a-a7a6-5ccc4bf0d538",
        "subtype": "building",
        "tier": "supporting",
        "within": "[[somewhere]]",
        "north_of": "[[north]]",
        "east_of": "[[east]]",
        "south_of": "[[south]]",
        "west_of": "[[west]]",
        "geography": ["coastal"],
    }
    page = _page(fm, "location")
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert findings == []


# --- type-specific subtype enum -------------------------------------------


def test_npc_invalid_subtype_yields_finding() -> None:
    fm = dict(_BASE_FM)
    fm["subtype"] = "legendary"  # invalid for npc; valid = major | minor | recurring
    page = _page(fm)
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert any(f.rule_id == RULE_ID and "subtype" in f.message for f in findings)


def test_npc_valid_subtype_major_yields_no_finding() -> None:
    fm = dict(_BASE_FM)
    fm["subtype"] = "major"
    page = _page(fm)
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert findings == []


def test_location_invalid_subtype_yields_finding() -> None:
    fm: dict[str, object] = {
        "type": "location",
        "status": "draft",
        "publish": False,
        "aliases": [],
        "tags": [],
        "summary": "A place.",
        "created": "2026-08-11",
        "updated": "2026-08-11",
        "uid": "c69466f8-31d5-498a-a7a6-5ccc4bf0d538",
        "subtype": "castle",  # invalid; valid = building | plane | dungeon | settlement | region | shop
        "tier": "supporting",
        "within": "[[somewhere]]",
        "north_of": "[[north]]",
        "east_of": "[[east]]",
        "south_of": "[[south]]",
        "west_of": "[[west]]",
        "geography": ["coastal"],
    }
    page = _page(fm, "location")
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert any(f.rule_id == RULE_ID and "subtype" in f.message for f in findings)


def test_spell_invalid_subtype_yields_finding() -> None:
    fm: dict[str, object] = {
        "type": "spell",
        "status": "srd",
        "publish": False,
        "aliases": [],
        "tags": [],
        "summary": "A spell.",
        "created": "2026-08-11",
        "updated": "2026-08-11",
        "uid": "abc12345-0000-0000-0000-000000000001",
        "subtype": "fire",  # invalid; valid = abjuration | conjuration | divination | ...
        "tier": "supporting",
    }
    page = _page(fm, "spell")
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert any(f.rule_id == RULE_ID and "subtype" in f.message for f in findings)


def test_spell_valid_subtype_yields_no_finding() -> None:
    fm: dict[str, object] = {
        "type": "spell",
        "status": "srd",
        "publish": False,
        "aliases": [],
        "tags": [],
        "summary": "A fireball.",
        "created": "2026-08-11",
        "updated": "2026-08-11",
        "uid": "abc12345-0000-0000-0000-000000000001",
        "subtype": "evocation",
        "tier": "supporting",
    }
    page = _page(fm, "spell")
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert findings == []


# --- conforming NPC page yields zero findings -----------------------------


def test_conforming_npc_yields_no_findings() -> None:
    page = _page(dict(_BASE_FM))
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert findings == []


# --- type with no subtype constraint (base-only validation) ---------------


def test_encounter_invalid_status_yields_finding() -> None:
    fm: dict[str, object] = {
        "type": "encounter",
        "status": "WRONG",
        "publish": False,
        "aliases": [],
        "tags": [],
        "summary": "A fight.",
        "created": "2026-08-11",
        "updated": "2026-08-11",
        "uid": "87e389ef-0000-4e43-9a2f-975ca9b8db0c",
    }
    page = _page(fm, "encounter")
    findings = list(FrontmatterValuesRule().check(page, _CORPUS))  # type: ignore[arg-type]
    assert any(f.rule_id == RULE_ID and "status" in f.message for f in findings)
