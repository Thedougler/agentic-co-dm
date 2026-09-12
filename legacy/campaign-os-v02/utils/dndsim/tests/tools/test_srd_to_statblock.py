"""dndsim.tools.srd_to_statblock (issue #55). Verifies the SRD bullet+table
page converts to a ```statblock fence that parses cleanly through dndsim's
own native-fence importer, with source wording preserved.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dndsim.rules.dnd5e_2014.statblock import parse_statblock_page
from dndsim.tools.srd_to_statblock import (
    SrdToStatblockError,
    parse_srd_monster_page,
    render_statblock_page,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"
SRD_PAGE = (FIXTURES_DIR / "srd-test-ooze.md").read_text(encoding="utf-8")


def test_parse_srd_monster_page_frontmatter_type_ac_hp_stat_table_resist_immune() -> None:
    parsed = parse_srd_monster_page(SRD_PAGE, "test-ooze.md")
    assert 'source: "raw/2026-07/12_MonstersA-Z.md"' in parsed.frontmatter
    assert parsed.name == "Test Ooze"
    assert parsed.size == "Large"
    assert parsed.creature_type == "ooze"
    assert parsed.alignment == "Unaligned"
    assert parsed.ac == 8
    assert parsed.hp == 52
    assert parsed.hit_dice == "7d10 + 14"
    assert parsed.stats == [15, 6, 14, 2, 6, 1]
    # CON save (+5) differs from CON mod (+2) -> proficient save recorded;
    # every other ability's save equals its mod -> omitted.
    assert parsed.saves == [{"con": 5}]
    assert parsed.damage_resistances == "Acid"
    assert parsed.damage_immunities == "Lightning, Slashing"
    assert parsed.condition_immunities == "Charmed, Prone"
    assert parsed.cr == "2"
    assert len(parsed.traits) == 1
    assert parsed.traits[0].name == "Amorphous"
    assert len(parsed.actions) == 2
    assert parsed.actions[1].name == "Pseudopod"
    assert "Melee Attack Roll:* +4" in parsed.actions[1].desc


def test_render_statblock_page_round_trips_through_the_real_sim_parser() -> None:
    parsed = parse_srd_monster_page(SRD_PAGE, "test-ooze.md")
    rendered = render_statblock_page(parsed)
    sb = parse_statblock_page(rendered, "test-ooze.md")
    assert sb is not None
    assert sb.name == "Test Ooze"
    assert sb.ac == 8
    assert sb.hp == 52
    assert sb.saves["con"] == 5
    assert "acid" in sb.defenses.resist
    assert "lightning" in sb.defenses.immune
    assert "charmed" in sb.defenses.condition_immune


def test_missing_required_bullet_fails_loudly_with_the_source_path() -> None:
    no_ac = SRD_PAGE.replace("- **Armor Class:** 8\n", "")
    with pytest.raises(SrdToStatblockError, match=r"test-ooze\.md.*Armor Class"):
        parse_srd_monster_page(no_ac, "test-ooze.md")


REPO_ROOT = Path(__file__).resolve().parents[4]


def test_real_srd_corpus_page_converts_and_parses() -> None:
    """A real SRD page — vault/srd/monsters/badger.md, still in the
    raw bullet+table shape — converts and the result parses through the real
    native-fence importer with no fact loss. Read-only: never writes back to
    the live page (CLAUDE.md — never modify vault/ to make code work)."""
    source = REPO_ROOT / "vault" / "srd" / "monsters" / "badger.md"
    markdown = source.read_text(encoding="utf-8")
    parsed = parse_srd_monster_page(markdown, str(source))
    rendered = render_statblock_page(parsed)
    sb = parse_statblock_page(rendered, str(source))
    assert sb is not None
    assert sb.name == "Badger"
    assert sb.ac == 11
    assert sb.hp == 5
    assert sb.cr == 0.0
    assert "poison" in sb.defenses.resist
    assert len(parsed.actions) == 1
    assert parsed.actions[0].name == "Bite"
