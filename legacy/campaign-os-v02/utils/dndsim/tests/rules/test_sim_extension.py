"""The `sim:` extension namespace (issue #43) — tagged unions, registry
dispatch, and strictness that tracks `sim-extension.mjs` clause by clause."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

import pytest
import yaml

from dndsim.rules.dnd5e_2014.sim_extension import (
    MODIFIER_KINDS,
    ActionSim,
    AdvantageModifier,
    ModifierBase,
    PeriodicEffectModifier,
    SimExtensionError,
    TradeDiceForRiderModifier,
    TradeoffModifier,
    describe_modifier,
    parse_action_sim,
    parse_sim_block,
)
from dndsim.rules.dnd5e_2014.statblock import extract_statblock_fence

# tests/rules/test_sim_extension.py -> repo root is 4 parents up (rules,
# tests, utils/dndsim, utils) — the same computation lint/run.py and
# differential_harness.py do from their own locations.
REPO_ROOT: Path = Path(__file__).resolve().parents[4]
ACTION_CATEGORIES: tuple[str, ...] = ("actions", "bonus_actions", "reactions", "legendary_actions")


def test_sim_block_defaults_to_enemy_side_when_absent() -> None:
    sb = parse_sim_block(None, "legacy-monster.md")
    assert sb.side == "enemy"
    assert sb.abilities == []


def test_unknown_top_level_key_is_rejected_naming_the_field() -> None:
    with pytest.raises(SimExtensionError, match="bogus_key"):
        parse_sim_block({"bogus_key": 1}, "bad.md")


def test_malformed_side_value_is_rejected_naming_field_and_expectation() -> None:
    with pytest.raises(SimExtensionError, match="side"):
        parse_sim_block({"side": "nope"}, "bad.md")


def test_unknown_ability_kind_is_rejected() -> None:
    with pytest.raises(SimExtensionError, match="not_a_real_kind"):
        parse_sim_block({"abilities": [{"kind": "not_a_real_kind"}]}, "bad.md")


def test_ability_missing_required_field_is_rejected() -> None:
    # tradeoff requires damage_bonus
    with pytest.raises(SimExtensionError, match="damage_bonus"):
        parse_sim_block({"abilities": [{"kind": "tradeoff", "to_hit": -5}]}, "bad.md")


def test_ability_kind_dispatches_to_the_right_discriminated_member() -> None:
    sb = parse_sim_block(
        {
            "abilities": [
                {"kind": "advantage", "source": "ally Faerie Fire"},
                {"kind": "tradeoff", "to_hit": -5, "damage_bonus": 10},
            ]
        },
        "x.md",
    )
    assert isinstance(sb.abilities[0], AdvantageModifier)
    assert isinstance(sb.abilities[1], TradeoffModifier)


@pytest.mark.parametrize(
    "scenario_kind",
    ["resource_budget", "setup_round", "assume_rider_triggers", "save_action_priority"],
)
def test_scenario_only_kinds_rejected_on_a_statblocks_own_abilities(scenario_kind: str) -> None:
    data: dict[str, object]
    if scenario_kind == "resource_budget":
        data = {"pools": {"pact_slot_1": 0}}
    elif scenario_kind == "assume_rider_triggers":
        data = {"value": 0.5}
    else:
        data = {}
    with pytest.raises(SimExtensionError, match="scenario assumption"):
        parse_sim_block({"abilities": [{"kind": scenario_kind, **data}]}, "bad.md")


def test_extra_damage_requires_a_parseable_dice_expression() -> None:
    with pytest.raises(SimExtensionError, match="dice"):
        parse_sim_block({"abilities": [{"kind": "extra_damage", "dice": "not-dice"}]}, "bad.md")


def test_post_hit_rider_needs_an_on_fail_or_on_success_branch() -> None:
    with pytest.raises(SimExtensionError, match="on_fail"):
        parse_sim_block(
            {
                "abilities": [
                    {"kind": "post_hit_rider", "id": "stun", "save": {"ability": "con", "dc": 16}}
                ]
            },
            "bad.md",
        )


def test_real_otar_periodic_effect_abilities_validate() -> None:
    sb = parse_sim_block(
        {
            "abilities": [
                {
                    "kind": "periodic_effect",
                    "trigger": "start_of_turn_self",
                    "effect": "regen",
                    "amount": 12,
                    "suppressed_if_damaged_by": ["fire", "acid"],
                },
                {
                    "kind": "periodic_effect",
                    "trigger": "start_of_turn_others",
                    "effect": "damage",
                    "dice": "1d6",
                    "damage_type": "poison",
                },
            ]
        },
        "otar-the-foul-statblock.md",
    )
    assert len(sb.abilities) == 2
    assert all(isinstance(a, PeriodicEffectModifier) for a in sb.abilities)


def test_real_perrin_spellcasting_pool_with_extra_keys_validates() -> None:
    # Real vault content (perrin-black-jaw-sheet.md) carries `source` and
    # `ability_mod` keys the README table doesn't document — the reference
    # JS validator never closes this sub-object either.
    sb = parse_sim_block(
        {
            "side": "party",
            "spellcasting": [
                {
                    "ability": "cha",
                    "dc": 16,
                    "attack_bonus": 8,
                    "level": 5,
                    "ability_mod": 5,
                    "source": "bard",
                    "slots": {1: "bard_slot_1", 2: "bard_slot_2"},
                    "known": ["Hideous Laughter"],
                }
            ],
        },
        "perrin-black-jaw-sheet.md",
    )
    assert sb.spellcasting is not None
    assert sb.spellcasting[0].known == ["Hideous Laughter"]


def test_real_perrin_action_sim_heal_and_cost_validates() -> None:
    a = parse_action_sim(
        {
            "id": "cure_wounds",
            "heal": {"dice": "1d8+5"},
            "cost": {"resource": "bard_slot_1", "spend": 1},
        },
        "perrin-black-jaw-sheet.md",
        "actions[2].sim",
    )
    assert a.heal is not None
    assert a.heal.dice == "1d8+5"
    assert a.cost is not None
    assert a.cost.resource == "bard_slot_1"


def test_action_sim_unknown_key_is_rejected() -> None:
    with pytest.raises(SimExtensionError, match="typo_key"):
        parse_action_sim({"typo_key": True}, "bad.md", "actions[0].sim")


def test_action_sim_defaults_when_absent() -> None:
    a = parse_action_sim(None, "x.md", "actions[0].sim")
    assert a == ActionSim()


# --- strictness parity with sim-extension.mjs ------------------------------
#
# The reference validator calls `checkUnknownKeys` on exactly three maps —
# the top-level `sim:`, a per-action `sim:`, and `sim.position`. Everywhere
# else it walks a sub-object without a key check, and real vault content
# carries keys there. Each test below names the real page that proved it.


def test_ability_modifier_carries_extra_keys_the_reference_passes_through() -> None:
    # crissdalynn-khinriss-sheet.md / delmar-fisk-sheet.md — `validateModifier`
    # checks `kind` and the per-kind `needs` table, never the key set.
    sb = parse_sim_block(
        {
            "abilities": [
                {
                    "kind": "bonus_attack",
                    "id": "flurry-of-blows",
                    "attack": "unarmed",
                    "cost": {"resource": "ki", "spend": 1},
                },
                {"kind": "movement_boost", "id": "cunning-action", "grants": "both"},
            ]
        },
        "crissdalynn-khinriss-sheet.md",
    )
    assert len(sb.abilities) == 2


def test_rider_effects_carry_duration_and_save_ends() -> None:
    # crissdalynn's Stunning Strike (`duration`) and delmar's Cunning Poison
    # (`save_ends`) — the reference never closes an effect rider.
    sb = parse_sim_block(
        {
            "abilities": [
                {
                    "kind": "post_hit_rider",
                    "id": "stunning-strike",
                    "save": {"ability": "con", "dc": 14},
                    "on_fail": {
                        "effects": [
                            {
                                "effect": "stunned",
                                "duration": {"until": "start_of_source_next_turn"},
                            }
                        ]
                    },
                },
                {
                    "kind": "trade_dice_for_rider",
                    "id": "cunning-poison",
                    "from": "sneak-attack",
                    "dice_cost": "1d6",
                    "save": {"ability": "con", "dc": 15},
                    "on_fail": {
                        "effects": [
                            {
                                "effect": "poisoned",
                                "save_ends": {"save": "con", "dc": 15, "timing": "end_of_turn"},
                            }
                        ]
                    },
                },
            ]
        },
        "delmar-fisk-sheet.md",
    )
    assert len(sb.abilities) == 2


def test_trade_dice_for_rider_dice_cost_accepts_a_dice_expression() -> None:
    # The reference requires `dice_cost`'s presence and nothing more; delmar
    # spends `1d6` of Sneak Attack, which a bare `int` field rejected.
    sb = parse_sim_block(
        {
            "abilities": [
                {
                    "kind": "trade_dice_for_rider",
                    "id": "cunning-trip",
                    "from": "sneak-attack",
                    "dice_cost": "1d6",
                    "save": {"ability": "dex", "dc": 15},
                    "on_fail": {"effects": [{"effect": "prone"}]},
                }
            ]
        },
        "delmar-fisk-sheet.md",
    )
    trade = sb.abilities[0]
    assert isinstance(trade, TradeDiceForRiderModifier)
    assert trade.dice_cost == "1d6"


def test_action_sim_kind_accepts_damage_reduction_pct() -> None:
    # delmar's Uncanny Dodge / catarina's Absorb Elements — the reference's
    # REACTION_KINDS has always carried it.
    a = parse_action_sim(
        {"id": "uncanny-dodge", "kind": "damage_reduction_pct", "fraction": 0.5},
        "delmar-fisk-sheet.md",
        "reactions[0].sim",
    )
    assert a.kind == "damage_reduction_pct"


def test_action_sim_redirect_may_be_a_map() -> None:
    # crissdalynn's Deflect Attacks — `redirect` is a known ACTION_KEYS key
    # the reference type-checks not at all.
    a = parse_action_sim(
        {
            "id": "deflect-attacks",
            "kind": "damage_reduction",
            "die": "1d10+9",
            "redirect": {
                "cost": {"resource": "ki", "spend": 1},
                "damage": [{"dice": "2d8+4", "type": "same_as_triggering"}],
                "save": {"ability": "dex", "dc": 14},
                "range_ft": {"melee": 5, "ranged": 60},
            },
        },
        "crissdalynn-khinriss-sheet.md",
        "reactions[0].sim",
    )
    assert a.redirect["range_ft"]["ranged"] == 60


def test_die_is_parsed_only_for_a_damage_reduction_reaction() -> None:
    # `sim-extension.mjs:197-199` gates the dice parse on the reaction kind.
    with pytest.raises(SimExtensionError, match="die"):
        parse_action_sim({"kind": "damage_reduction", "die": "not-dice"}, "bad.md", "r[0].sim")
    assert parse_action_sim({"kind": "unmodeled", "die": "not-dice"}, "x.md", "r[0].sim").die


def test_on_fail_effect_tag_is_still_checked_on_a_per_action_sim() -> None:
    # The reference DOES check the tag vocabulary here (`:177-182`) even
    # though it never checks it on a modifier's own on_fail.
    with pytest.raises(SimExtensionError, match="unknown condition tag"):
        parse_action_sim(
            {"on_fail": {"effects": [{"effect": "bamboozled"}]}}, "bad.md", "actions[0].sim"
        )


def test_unknown_routine_slot_is_passed_through() -> None:
    # `sim-extension.mjs:135-138` iterates the four KNOWN slots only.
    sb = parse_sim_block({"routine": {"action": ["a"], "mythic": "whatever"}}, "x.md")
    assert sb.routine is not None
    with pytest.raises(SimExtensionError, match="routine.action"):
        parse_sim_block({"routine": {"action": "not-a-list"}}, "bad.md")


def test_unquoted_yaml_edition_int_is_accepted() -> None:
    # The reference compares `String(sim.edition)`.
    assert parse_sim_block({"edition": 2014}, "x.md").edition == 2014
    with pytest.raises(SimExtensionError, match="edition"):
        parse_sim_block({"edition": 2011}, "bad.md")


# --- the real corpus: every vault page carrying a `sim:` block -------------


def _sim_carrying_pages() -> list[Path]:
    """Every live vault page dndsim's own corpus scopes to — the same
    discovery `lint/run.py` and `differential_harness.py` do. Deliberately
    NOT a fixture copy: this test's job is to catch drift against the live
    content the way the differential harness does."""
    files = sorted((REPO_ROOT / "vault" / "srd" / "monsters").glob("*.md"))
    files += sorted((REPO_ROOT / "vault" / "campaigns" / "shattered-sea" / "monsters").glob("*.md"))
    dm_intel = REPO_ROOT / "vault" / "campaigns" / "shattered-sea" / "pcs" / "character-sheets"
    if dm_intel.exists():
        files += sorted(p for p in dm_intel.rglob("*.md") if p.is_file())
    return files


def _fence_data(path: Path) -> dict[str, Any] | None:
    inner = extract_statblock_fence(path.read_text(encoding="utf-8"))
    if inner is None:
        return None
    data = yaml.safe_load(inner)
    return data if isinstance(data, dict) else None


def _carries_sim(data: dict[str, Any]) -> bool:
    if "sim" in data:
        return True
    return any(
        isinstance(entry, dict) and "sim" in entry
        for category in ACTION_CATEGORIES
        for entry in (data.get(category) or [])
    )


def test_every_real_vault_sim_block_validates() -> None:
    """No live page carrying a `sim:` block — top-level or per-action — may
    fail validation. dndsim is a port: content the reference engine accepts
    is content this validator must accept."""
    checked = 0
    failures: list[str] = []
    for path in _sim_carrying_pages():
        data = _fence_data(path)
        if data is None or not _carries_sim(data):
            continue
        checked += 1
        rel = path.relative_to(REPO_ROOT).as_posix()
        if "sim" in data:
            try:
                parse_sim_block(data["sim"], rel)
            except SimExtensionError as err:
                failures.append(f"{rel} [sim]: {err}")
        for category in ACTION_CATEGORIES:
            for i, entry in enumerate(data.get(category) or []):
                if not isinstance(entry, dict) or "sim" not in entry:
                    continue
                try:
                    parse_action_sim(entry["sim"], rel, f"{category}[{i}].sim")
                except SimExtensionError as err:
                    failures.append(f"{rel} [{category}[{i}] {entry.get('name')}]: {err}")
    # A discovery break must fail loudly, not pass by checking nothing.
    assert checked >= 5, f"corpus discovery found only {checked} pages carrying a sim: block"
    assert not failures, "real vault content rejected by parse_sim_block/parse_action_sim:\n" + (
        "\n".join(failures)
    )


# --- registration replaces dispatch (no switch; extensible without an edit)


def test_describe_modifier_resolves_through_the_registry() -> None:
    m = describe_modifier("advantage", "x.md", "sim.abilities[0]", source="ally Faerie Fire")
    assert isinstance(m, AdvantageModifier)
    assert m.source == "ally Faerie Fire"


def test_describe_modifier_unknown_kind_names_it() -> None:
    with pytest.raises(SimExtensionError, match="bogus"):
        describe_modifier("bogus", "x.md", "sim.abilities[0]")


def test_new_modifier_kind_needs_no_registry_edit() -> None:
    """Registering a brand-new kind at test scope must be enough to drive it
    through the shared dispatcher — no edit to sim_extension.py itself."""

    class DummyModifier(ModifierBase):
        kind: Literal["dummy_test_kind"] = "dummy_test_kind"
        value: int

    MODIFIER_KINDS.register_value("dnd5e_2014:modifier/dummy_test_kind", DummyModifier)

    m = describe_modifier("dummy_test_kind", "x.md", "sim.abilities[0]", value=7)
    assert isinstance(m, DummyModifier)
    assert m.value == 7


# --- weapon mastery (issue #71): a per-action `sim:` override, since no
# statblock's prose ever names a mastery property (it is unlocked by a
# player-facing class feature, not stated in monster/attack text) ------------


@pytest.mark.parametrize("mastery", ["vex", "slow"])
def test_action_sim_accepts_a_supported_mastery_kind(mastery: str) -> None:
    a = parse_action_sim({"mastery": mastery}, "delmar-fisk-sheet.md", "actions[0].sim")
    assert a.mastery == mastery


def test_action_sim_rejects_an_unsupported_mastery_kind() -> None:
    # Sap/Push/Topple/Cleave/Graze/Nick are real SRD-2024 mastery properties
    # (vault/srd/rules/weapons.md) but only
    # vex/slow are modeled (issue #71's scope note) — an unmodeled kind is
    # rejected loudly, never silently ignored.
    with pytest.raises(SimExtensionError, match="mastery"):
        parse_action_sim({"mastery": "sap"}, "bad.md", "actions[0].sim")


def test_action_sim_mastery_defaults_to_none() -> None:
    assert parse_action_sim({}, "x.md", "actions[0].sim").mastery is None
