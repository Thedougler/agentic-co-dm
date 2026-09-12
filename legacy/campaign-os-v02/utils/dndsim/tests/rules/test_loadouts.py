"""Loadouts, creature overrides, and scenarios (issue #49), tested both
against inline fixtures and the real vault loadout files under
``vault/campaigns/shattered-sea/pcs/combat-profile/loadouts/``."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from dndsim.rules.dnd5e_2014.compile import CompiledStatblock, compile_statblock
from dndsim.rules.dnd5e_2014.loadouts import (
    RESERVED_LOADOUT_NAMES,
    LairAction,
    LoadoutError,
    LoadoutFile,
    apply_creature_overrides,
    apply_loadout,
    apply_modifiers,
    find_scenario,
    load_loadout_file,
    merge_loadout_files,
    parse_loadout_file,
    resolve_loadout,
    validate_modifier,
)
from dndsim.rules.dnd5e_2014.sim_extension import (
    AdvantageModifier,
    SimExtensionError,
    parse_sim_block,
)
from dndsim.rules.dnd5e_2014.statblock import parse_statblock_page

# tests/rules/test_loadouts.py -> repo root is 4 parents up (rules, tests,
# utils/dndsim, utils) — same computation test_sim_extension.py/
# test_spells.py already use from this same directory.
REPO_ROOT: Path = Path(__file__).resolve().parents[4]
LOADOUTS_DIR = REPO_ROOT / "content" / "pcs" / "combat-profile" / "loadouts"

PERRIN_FIXTURE = """\
```statblock
name: Perrin Black-Jaw
ac: 18
hp: 49
stats: [6, 18, 15, 11, 11, 20]
sim:
  side: party
  resources:
    - { id: bard_slot_1, max: 4, recharge: long_rest }
    - { id: pact_slot_1, max: 2, recharge: short_rest }
actions:
  - name: "Longsword"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft. Hit: 8 (1d8 + 4) slashing damage."
```
"""


def _compile_perrin() -> CompiledStatblock:
    content = parse_statblock_page(PERRIN_FIXTURE, "perrin.md")
    assert content is not None
    fence = PERRIN_FIXTURE.split("```statblock", 1)[1].rsplit("```", 1)[0]
    block = yaml.safe_load(fence)
    from dndsim.rules.dnd5e_2014.attack_string import parse_action_category

    actions, _warnings = parse_action_category(block.get("actions"), "actions")
    return compile_statblock(content, actions=actions, sim_data=block.get("sim"))


# --- modifier validation reuses the shared vocabulary ----------------------


def test_validate_modifier_dispatches_to_the_shared_registry() -> None:
    mod = validate_modifier(
        {"kind": "advantage", "on": "attack", "source": "ally Faerie Fire"},
        "x.yaml",
        "modifiers[0]",
    )
    assert isinstance(mod, AdvantageModifier)


def test_validate_modifier_unknown_kind_raises_sim_extension_error() -> None:
    # Raises the SAME error type page-authored content raises — never a
    # parallel LoadoutError for modifier content (module contract).
    with pytest.raises(SimExtensionError, match="unknown modifier kind"):
        validate_modifier({"kind": "not-a-real-kind"}, "x.yaml", "modifiers[0]")


def test_validate_modifier_bad_dice_raises() -> None:
    with pytest.raises(SimExtensionError, match="dice"):
        validate_modifier({"kind": "extra_damage", "dice": "not-dice"}, "x.yaml", "modifiers[0]")


def test_scenario_only_kind_is_legal_in_a_loadout_modifier() -> None:
    # resource_budget is SCENARIO_ONLY — legal here (a loadout file), only
    # rejected on a combatant's own sim.abilities (next test).
    mod = validate_modifier({"kind": "resource_budget", "pools": {"x": 0}}, "x.yaml", "m[0]")
    assert mod.kind == "resource_budget"  # type: ignore[attr-defined]


def test_scenario_only_modifier_rejected_on_a_combatants_own_page() -> None:
    # The gate lives in sim_extension.parse_sim_block (SCENARIO_ONLY_KINDS)
    # and is reused unchanged here, never duplicated — the concrete "named
    # reason" rejection the PRD asks for.
    with pytest.raises(SimExtensionError, match="scenario assumption"):
        parse_sim_block({"abilities": [{"kind": "resource_budget", "pools": {"x": 0}}]}, "bad.md")


# --- loadout-file structure -------------------------------------------------


def test_schema_version_required() -> None:
    with pytest.raises(LoadoutError, match="schema_version"):
        parse_loadout_file({"loadouts": []}, "x.yaml")


def test_loadout_missing_name_raises() -> None:
    with pytest.raises(LoadoutError, match="name"):
        parse_loadout_file(
            {"schema_version": 1, "loadouts": [{"applies_to": "x", "modifiers": []}]}, "x.yaml"
        )


def test_roster_entry_requires_file() -> None:
    with pytest.raises(LoadoutError, match="file"):
        parse_loadout_file(
            {"schema_version": 1, "scenarios": [{"name": "s", "party": [{"count": 1}]}]}, "x.yaml"
        )


def test_merge_loadout_files_concatenates() -> None:
    a = parse_loadout_file(
        {
            "schema_version": 1,
            "loadouts": [{"name": "avg", "applies_to": "perrin", "modifiers": []}],
        },
        "a.yaml",
    )
    b = parse_loadout_file(
        {
            "schema_version": 1,
            "loadouts": [{"name": "max", "applies_to": "perrin", "modifiers": []}],
        },
        "b.yaml",
    )
    merged = merge_loadout_files([a, b])
    assert [loadout.name for loadout in merged.loadouts] == ["avg", "max"]


# --- reserved loadout names -------------------------------------------------


def test_reserved_names_are_exactly_optimal_min_avg_max() -> None:
    assert RESERVED_LOADOUT_NAMES == {"optimal", "min", "avg", "max"}


def test_optimal_runs_with_no_modifiers() -> None:
    empty = LoadoutFile(source="<none>")
    resolved = resolve_loadout(
        empty, combatant_id="perrin", combatant_name="Perrin Black-Jaw", name="optimal"
    )
    assert resolved.modifiers == ()
    assert resolved.authored is False


def test_min_zeroes_every_declared_resource_pool() -> None:
    empty = LoadoutFile(source="<none>")
    resolved = resolve_loadout(
        empty,
        combatant_id="perrin",
        combatant_name="Perrin Black-Jaw",
        name="min",
        resource_ids=("bard_slot_1", "pact_slot_1"),
    )
    assert len(resolved.modifiers) == 1
    pools = resolved.modifiers[0].pools  # type: ignore[attr-defined]
    assert pools == {"bard_slot_1": 0, "pact_slot_1": 0}


def test_min_with_no_declared_pools_is_a_true_no_op() -> None:
    empty = LoadoutFile(source="<none>")
    resolved = resolve_loadout(
        empty, combatant_id="perrin", combatant_name="Perrin Black-Jaw", name="min"
    )
    assert resolved.modifiers == ()


def test_avg_and_max_run_bare_with_a_note_when_unauthored() -> None:
    empty = LoadoutFile(source="<none>")
    for name in ("avg", "max"):
        resolved = resolve_loadout(
            empty, combatant_id="perrin", combatant_name="Perrin Black-Jaw", name=name
        )
        assert resolved.modifiers == ()
        assert resolved.note is not None and "no" in resolved.note


def test_authored_loadout_wins_over_reserved_fallback() -> None:
    f = parse_loadout_file(
        {
            "schema_version": 1,
            "loadouts": [
                {
                    "name": "max",
                    "applies_to": "perrin",
                    "modifiers": [{"kind": "advantage", "on": "attack"}],
                }
            ],
        },
        "x.yaml",
    )
    resolved = resolve_loadout(
        f, combatant_id="perrin", combatant_name="Perrin Black-Jaw", name="max"
    )
    assert resolved.authored is True
    assert len(resolved.modifiers) == 1


def test_unknown_loadout_name_raises() -> None:
    empty = LoadoutFile(source="<none>")
    with pytest.raises(LoadoutError, match="no loadout named"):
        resolve_loadout(empty, combatant_id="perrin", combatant_name="Perrin", name="nova-blade")


def test_loadout_matches_by_id_or_display_name_case_insensitively() -> None:
    f = parse_loadout_file(
        {
            "schema_version": 1,
            "loadouts": [
                {
                    "name": "max",
                    "applies_to": "Vashu, the Weeping Veil",
                    "modifiers": [{"kind": "advantage", "on": "attack"}],
                }
            ],
        },
        "x.yaml",
    )
    resolved = resolve_loadout(
        f, combatant_id="vashu-slug", combatant_name="vashu, the weeping veil", name="max"
    )
    assert resolved.authored is True


# --- applying modifiers to a compiled statblock -----------------------------


def test_apply_modifiers_min_floor_caps_resource_pools_and_does_not_mutate() -> None:
    # resource_budget has no Primitive counterpart by design (it caps a
    # pool, it is not a combatant capability) — applying it overrides each
    # named resource's declared `max` instead of appending a Primitive.
    compiled = _compile_perrin()
    before_max = {r.id: r.max for r in compiled.resources}
    resolved = resolve_loadout(
        LoadoutFile(source="<none>"),
        combatant_id="perrin-black-jaw",
        combatant_name="Perrin Black-Jaw",
        name="min",
        resource_ids=tuple(r.id for r in compiled.resources),
    )
    applied = apply_modifiers(compiled, resolved.modifiers, tag="loadout-min")
    assert {r.id: r.max for r in applied.resources} == {"bard_slot_1": 0, "pact_slot_1": 0}
    assert {r.id: r.max for r in compiled.resources} == before_max  # original untouched
    assert applied.ability_primitives == compiled.ability_primitives


def test_apply_modifiers_reports_unmodeled_scenario_only_kinds_loudly() -> None:
    compiled = _compile_perrin()
    mod = validate_modifier({"kind": "setup_round"}, "x.yaml", "m[0]")
    applied = apply_modifiers(compiled, [mod], tag="loadout-max")
    assert any("setup_round" in w and "unapplied" in w for w in applied.warnings)


def test_apply_loadout_combines_resolve_and_apply() -> None:
    compiled = _compile_perrin()
    f = parse_loadout_file(
        {
            "schema_version": 1,
            "loadouts": [
                {
                    "name": "nova",
                    "applies_to": "perrin-black-jaw",
                    "modifiers": [
                        {"kind": "extra_damage", "id": "hex", "dice": "1d6", "type": "necrotic"}
                    ],
                }
            ],
        },
        "x.yaml",
    )
    applied, resolved = apply_loadout(
        compiled, f, combatant_id="perrin-black-jaw", combatant_name="Perrin Black-Jaw", name="nova"
    )
    assert resolved.authored is True
    assert len(applied.ability_primitives) == len(compiled.ability_primitives) + 1


def test_creature_override_applies_unconditionally_regardless_of_loadout_name() -> None:
    compiled = _compile_perrin()
    f = parse_loadout_file(
        {
            "schema_version": 1,
            "creature_overrides": [
                {
                    "applies_to": "Perrin Black-Jaw",
                    "modifiers": [
                        {
                            "kind": "damage_reduction_reaction",
                            "dice": "2d10+4",
                            "trigger": "self_or_ally_hit_by_ranged",
                        }
                    ],
                }
            ],
        },
        "x.yaml",
    )
    out = apply_creature_overrides(
        compiled, f, combatant_id="perrin-black-jaw", combatant_name="Perrin Black-Jaw"
    )
    assert len(out.ability_primitives) == len(compiled.ability_primitives) + 1


# --- lair actions ------------------------------------------------------------


def test_lair_action_parses_a_valid_entry() -> None:
    lair = LairAction.model_validate(
        {
            "id": "flood-surge",
            "dc": 15,
            "save": "dex",
            "on_fail": {"damage": [{"dice": "2d6", "type": "cold"}]},
            "half_on_save": True,
        }
    )
    assert lair.id == "flood-surge"
    assert lair.on_fail.damage[0].dice == "2d6"


def test_lair_action_rejects_bad_dice_expression() -> None:
    with pytest.raises(Exception, match="dice"):
        LairAction.model_validate(
            {"id": "x", "dc": 15, "save": "dex", "on_fail": {"damage": [{"dice": "not-dice"}]}}
        )


def test_lair_action_rejects_unknown_effect_tag() -> None:
    with pytest.raises(Exception, match="condition tag"):
        LairAction.model_validate(
            {"id": "x", "dc": 15, "save": "dex", "on_fail": {"effects": [{"effect": "not-a-tag"}]}}
        )


def test_lair_action_defaults_targets_to_area_radius_15() -> None:
    lair = LairAction.model_validate({"id": "x", "dc": 15, "save": "dex"})
    assert lair.targets == {"area": True, "radius": 15}


# --- scenarios: assemble a roster + lair from a name ------------------------


_PERRIN_SHEET = (
    REPO_ROOT / "vault/campaigns/shattered-sea/pcs" / "character-sheets/perrin-black-jaw-sheet.md"
).as_posix()
_OTAR_SURGE = (
    REPO_ROOT
    / "vault/campaigns/shattered-sea/pcs"
    / "combat-profile/sim-variants/otar-rattle-surge-s07.md"
).as_posix()

SCENARIO_YAML = f"""\
schema_version: 1
scenarios:
  - name: lair-repro-test
    party:
      - {{file: {_PERRIN_SHEET}, loadout: avg}}
    enemies:
      - {{file: {_OTAR_SURGE}}}
    lair:
      - id: flood-surge
        dc: 15
        save: dex
        on_fail: {{damage: [{{dice: 2d6, type: cold}}]}}
        half_on_save: true
    assumptions:
      targeting: {{party: focus_fire, enemies: focus_lowest_hp}}
      start_engaged: false
"""


def test_scenario_parses_lair_and_targeting_assumptions() -> None:
    data = yaml.safe_load(SCENARIO_YAML)
    f = parse_loadout_file(data, "scenario.yaml")
    scenario = find_scenario(f, "lair-repro-test")
    assert len(scenario.lair) == 1
    assert scenario.lair[0].id == "flood-surge"
    assert scenario.assumptions.targeting["party"] == "focus_fire"
    # start_engaged: false with no explicit formation -> skirmish alias.
    assert scenario.assumptions.formation == "skirmish"


def test_scenario_unknown_targeting_policy_rejected() -> None:
    with pytest.raises(LoadoutError, match="unknown policy"):
        parse_loadout_file(
            {
                "schema_version": 1,
                "scenarios": [
                    {
                        "name": "s",
                        "assumptions": {"targeting": {"party": "not-a-real-policy"}},
                    }
                ],
            },
            "x.yaml",
        )


def test_find_scenario_missing_raises() -> None:
    empty = LoadoutFile(source="<none>")
    with pytest.raises(LoadoutError, match="no scenario named"):
        find_scenario(empty, "does-not-exist")


# --- real vault loadout files: parse the corpus, never invent a dialect ----


def _real_loadout_files() -> list[Path]:
    return sorted(LOADOUTS_DIR.glob("*.loadouts.yaml"))


@pytest.mark.parametrize("path", _real_loadout_files(), ids=lambda p: p.name)
def test_every_real_loadout_file_parses(path: Path) -> None:
    """No live loadout file may fail validation — dndsim is a port: content
    the reference engine (loadout.mjs) accepts is content this validator
    must accept, including the open, needs-table-free `resource_budget`
    shape real content actually uses."""
    loaded = load_loadout_file(path)
    assert loaded.source == str(path)
