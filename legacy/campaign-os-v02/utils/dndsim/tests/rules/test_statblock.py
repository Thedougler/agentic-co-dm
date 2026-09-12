"""Native-fence statblock parsing (issue #40), restricted to the
native fence keys this slice covers (name, ac, hp, stats, saves, damage
tags, cr, speed, senses). Fixtures are copied files under tests/fixtures/,
never live vault pages (they change under the engine).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dndsim.rules.dnd5e_2014.statblock import (
    StatblockParseError,
    extract_statblock_fence,
    parse_damage_tags,
    parse_statblock_page,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def fixture(name: str) -> str:
    return (FIXTURES_DIR / name).read_text()


def test_sawek_lowercase_save_keys_ac_class_fallback() -> None:
    s = parse_statblock_page(fixture("fixture-sawek.md"), "sawek.md")
    assert s is not None
    assert s.name == "Sawek"
    assert s.ac == 14
    assert s.ac_note == "natural armour"
    assert s.hp == 95
    assert s.abilities == {"str": 20, "dex": 16, "con": 18, "int": 6, "wis": 14, "cha": 4}
    # explicit saves
    assert s.saves["str"] == 8
    assert s.saves["con"] == 7
    # omitted saves default to ability mod
    assert s.saves["dex"] == 3
    assert s.saves["int"] == -2
    assert s.cr == 5
    assert s.speed == "5 ft., swim 40 ft."
    assert s.senses == (
        "blindsight 60 ft. (underwater only), darkvision 120 ft., passive Perception 15"
    )


def test_grung_elite_warrior_ac_note_and_immunity_tags() -> None:
    s = parse_statblock_page(fixture("fixture-grung-elite-warrior.md"), "grung-elite-warrior.md")
    assert s is not None
    assert s.ac == 13
    assert s.ac_note == "natural armor"
    assert "poison" in s.defenses.immune
    assert "poisoned" in s.defenses.condition_immune
    assert s.cr == 2  # quoted "2" still parses numeric


def test_vashu_capitalized_short_save_keys_and_quoted_ac_string() -> None:
    s = parse_statblock_page(fixture("fixture-vashu-the-weeping-veil.md"), "vashu.md")
    assert s is not None
    assert s.ac == 20
    assert s.ac_note == "unarmored, perfected Still-Water Discipline"
    assert s.saves["dex"] == 8
    assert s.saves["con"] == 7
    assert s.saves["wis"] == 8
    # omitted -> mod: STR 14 -> +2
    assert s.saves["str"] == 2


def test_otar_resistances_and_darkvision_senses() -> None:
    s = parse_statblock_page(fixture("fixture-otar-the-foul.md"), "otar.md")
    assert s is not None
    assert s.hp == 241
    assert "cold" in s.defenses.resist
    assert "lightning" in s.defenses.resist
    assert "thunder" in s.defenses.resist
    assert "charmed" in s.defenses.condition_immune
    assert s.senses == "darkvision 60 ft., passive Perception 13"
    assert s.cr == 12


def test_hierarch_nonmagical_bps_resistance_expansion_and_quoted_cr() -> None:
    s = parse_statblock_page(fixture("fixture-hierarch.md"), "hierarch.md")
    assert s is not None
    assert s.cr == 19
    assert "cold" in s.defenses.resist
    assert "necrotic" in s.defenses.resist
    assert "nonmagical_bludgeoning" in s.defenses.resist
    assert "nonmagical_piercing" in s.defenses.resist
    assert "nonmagical_slashing" in s.defenses.resist


def test_blight_empty_statblock_fence_returns_none() -> None:
    assert parse_statblock_page(fixture("fixture-blight.md"), "blight.md") is None


def test_page_without_any_fence_returns_none() -> None:
    assert parse_statblock_page("# Just prose\n\nNo stats here.") is None


def test_parse_damage_tags_splits_on_comma_semicolon_and_lowercases() -> None:
    tags = parse_damage_tags(
        "Cold, Necrotic, Poison; Bludgeoning, Piercing, and Slashing from Nonmagical Attacks"
    )
    assert tags == sorted(
        [
            "cold",
            "necrotic",
            "nonmagical_bludgeoning",
            "nonmagical_piercing",
            "nonmagical_slashing",
            "poison",
        ]
    )


def test_extract_statblock_fence_returns_inner_yaml_none_for_empty() -> None:
    assert extract_statblock_fence("```statblock\n```") is None
    assert extract_statblock_fence("```statblock\nname: X\n```") == "name: X"


def test_missing_required_key_fails_loudly_naming_field_and_source() -> None:
    with pytest.raises(StatblockParseError, match=r'broken\.md missing required key "ac"'):
        parse_statblock_page(
            "```statblock\nname: Broken\nhp: 10\nstats: [10,10,10,10,10,10]\n```", "broken.md"
        )


def test_non_numeric_ac_string_with_no_digits_fails_loudly() -> None:
    md = "```statblock\nname: Broken AC\nac: 'unknown'\nhp: 10\nstats: [10,10,10,10,10,10]\n```"
    with pytest.raises(StatblockParseError, match=r"broken-ac\.md — ac: no numeric AC"):
        parse_statblock_page(md, "broken-ac.md")


def test_stats_wrong_length_fails_loudly() -> None:
    md = "```statblock\nname: Broken Stats\nac: 10\nhp: 10\nstats: [10,10,10]\n```"
    with pytest.raises(StatblockParseError, match=r"broken-stats\.md stats must be"):
        parse_statblock_page(md, "broken-stats.md")


def test_dravosi_deckhand_real_creature_page_no_sim_block_parses_cleanly() -> None:
    name = "dravosi-deckhand-statblock.md"
    s = parse_statblock_page(fixture(name), name)
    assert s is not None
    assert s.name == "Dravosi Deckhand"


def test_adult_black_dragon_2024_srd_full_page_round_trips_cleanly() -> None:
    s = parse_statblock_page(fixture("adult-black-dragon.md"), "adult-black-dragon.md")
    assert s is not None
    assert s.name == "Adult Black Dragon"
    assert s.hp == 195


# --- traits (issue #66, port of statblock-parse.test.mjs's parseTraits cases) ---


def test_otar_legendary_resistance_and_magic_resistance_traits() -> None:
    s = parse_statblock_page(fixture("fixture-otar-the-foul.md"), "otar.md")
    assert s is not None
    assert s.legendary_resistance == 3
    assert any(a.vs == "magic" for a in s.save_advantage)
    # Otar's other three traits (Foul Miasma, Entropic Regeneration, Unstable
    # Form) match none of the recognised patterns — named unmodeled, never
    # silently dropped.
    assert set(s.unmodeled_traits) == {
        "Foul Miasma",
        "Entropic Regeneration",
        "Unstable Form",
    }
    assert any("unmodeled trait: Foul Miasma" in w for w in s.warnings)


def test_extended_lair_parenthetical_still_parses_base_legendary_resistance_count() -> None:
    # 2024 SRD often extends the parenthetical ("3/Day, or 4/Day in Lair") —
    # the base (non-lair) count is the conservative number to take (the
    # engine has no in-lair-vs-not state to gate the higher one), and the
    # whole trait must not also land in unmodeled_traits.
    md = (
        "```statblock\n"
        "name: Test Dragon\n"
        "ac: 19\n"
        "hp: 195\n"
        "stats: [23, 14, 21, 14, 13, 19]\n"
        "traits:\n"
        '  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"\n'
        '    desc: "If the dragon fails a saving throw, it can choose to succeed instead."\n'
        "```"
    )
    s = parse_statblock_page(md, "test-dragon.md")
    assert s is not None
    assert s.legendary_resistance == 3
    assert "Legendary Resistance (3/Day, or 4/Day in Lair)" not in s.unmodeled_traits


def test_pack_tactics_trait_sets_advantage_if() -> None:
    md = (
        "```statblock\n"
        "name: Test Wolf\n"
        "ac: 13\n"
        "hp: 11\n"
        "stats: [12, 15, 12, 3, 12, 6]\n"
        "traits:\n"
        "  - name: Pack Tactics\n"
        '    desc: "The wolf has advantage on an attack roll against a creature if at '
        "least one of the wolf's allies is within 5 feet of the creature.\"\n"
        "```"
    )
    s = parse_statblock_page(md, "test-wolf.md")
    assert s is not None
    assert s.advantage_if == ["ally_adjacent_to_target"]


def test_generic_advantage_on_saving_throws_prose_pattern() -> None:
    md = (
        "```statblock\n"
        "name: Test Golem\n"
        "ac: 17\n"
        "hp: 178\n"
        "stats: [22, 9, 20, 3, 11, 1]\n"
        "traits:\n"
        "  - name: Immutable Form\n"
        '    desc: "The golem has advantage on Constitution saving throws."\n'
        "```"
    )
    s = parse_statblock_page(md, "test-golem.md")
    assert s is not None
    assert any(a.vs == "con" for a in s.save_advantage)
    assert s.unmodeled_traits == []
