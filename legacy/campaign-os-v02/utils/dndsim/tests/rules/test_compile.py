"""Compile-to-Primitives (issue #43): authored content's only executable form."""

from __future__ import annotations

from typing import Literal

import yaml

from dndsim.core.registry import Registry
from dndsim.rules.dnd5e_2014.attack_string import (
    Action,
    parse_action,
    parse_action_category,
    parse_name_usage,
)
from dndsim.rules.dnd5e_2014.compile import (
    ACTION_KIND_COMPILERS,
    ActionCompiler,
    CompiledStatblock,
    build_routine,
    compile_action,
    compile_statblock,
)
from dndsim.rules.dnd5e_2014.primitives import PrimitiveBase
from dndsim.rules.dnd5e_2014.sim_extension import ActionSim
from dndsim.rules.dnd5e_2014.statblock import extract_statblock_fence, parse_statblock_page

OTAR_FIXTURE = """\
```statblock
name: "Otar the Foul"
ac: 16
hp: 112
stats: [20, 12, 22, 5, 8, 6]
cr: 9
sim:
  abilities:
    - kind: periodic_effect
      trigger: start_of_turn_self
      effect: regen
      amount: 12
      suppressed_if_damaged_by: [fire, acid]
actions:
  - name: Multiattack
    desc: "Otar makes three attacks: one Bite attack and two Claw attacks."
  - name: Bite
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft. Hit: 14 (2d8 + 5) piercing damage."
  - name: Claw
    desc: "Melee Weapon Attack: +8 to hit, reach 10 ft. Hit: 12 (2d6 + 5) slashing damage."
  - name: "Chaos Pulse (Recharge 6)"
    desc: "Each creature within 20 feet makes a DC 16 Dexterity saving throw, taking
      22 (4d10) force damage and prone on a failure, half damage on a success."
```
"""

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
actions:
  - name: "Cure Wounds"
    desc: "Perrin touches a creature, restoring 9 (1d8 + 5) hit points."
    sim: { id: cure_wounds, heal: { dice: 1d8+5 }, cost: { resource: bard_slot_1, spend: 1 } }
reactions:
  - name: "Cutting Words"
    desc: "Perrin expends a Bardic Inspiration die to subtract it from an
      attack roll he can see."
    sim: { id: cutting_words, kind: damage_reduction, die: 1d6,
      trigger: self_or_ally_hit }
```
"""


def _compile_fixture(markdown: str, source: str) -> CompiledStatblock:
    content = parse_statblock_page(markdown, source)
    assert content is not None
    fence = extract_statblock_fence(markdown)
    assert fence is not None
    block = yaml.safe_load(fence)

    all_actions: list[Action] = []
    action_sim_data: dict[str, dict[str, object] | None] = {}
    for category in ("actions", "bonus_actions", "reactions", "legendary_actions"):
        parsed, _warnings = parse_action_category(block.get(category), category)
        all_actions.extend(parsed)
        for raw in block.get(category) or []:
            if isinstance(raw, dict) and raw.get("sim") is not None:
                name, _usage = parse_name_usage(raw.get("name") or "")
                action_sim_data[name] = raw["sim"]

    return compile_statblock(
        content,
        actions=all_actions,
        action_sim_data=action_sim_data,
        sim_data=block.get("sim"),
        routine=build_routine(block),
    )


def test_otar_real_shape_compiles_attacks_saves_periodic_effect_and_routine() -> None:
    compiled = _compile_fixture(OTAR_FIXTURE, "fixture-otar.md")

    assert compiled.ac == 16
    assert compiled.hp == 112
    assert compiled.side == "enemy"

    kinds = sorted(c.step.kind for c in compiled.compiled_actions)  # type: ignore[attr-defined]
    assert kinds == ["attack", "attack", "save"]

    ability_kinds = [p.kind for p in compiled.ability_primitives]  # type: ignore[attr-defined]
    assert ability_kinds == ["periodic_effect"]

    assert len(compiled.routine) == 2  # "one Bite attack and two Claw attacks"
    routine_by_ref = {step.ref: step.count for step in compiled.routine}
    assert routine_by_ref["dnd5e_2014:ability/otar-the-foul/bite"] == 1
    assert routine_by_ref["dnd5e_2014:ability/otar-the-foul/claw"] == 2


def test_perrin_real_shape_compiles_heal_and_reaction_overrides() -> None:
    compiled = _compile_fixture(PERRIN_FIXTURE, "fixture-perrin.md")

    assert compiled.side == "party"
    steps_by_id = {c.id: c.step for c in compiled.compiled_actions}
    assert steps_by_id["cure_wounds"].kind == "heal"  # type: ignore[attr-defined]
    assert steps_by_id["cure_wounds"].dice == "1d8+5"  # type: ignore[attr-defined]
    assert steps_by_id["cutting_words"].kind == "reaction"  # type: ignore[attr-defined]
    assert steps_by_id["cutting_words"].reaction_kind == "damage_reduction"  # type: ignore[attr-defined]


def test_every_compiled_primitive_carries_a_namespaced_id() -> None:
    compiled = _compile_fixture(OTAR_FIXTURE, "fixture-otar.md")
    for prim in compiled.ability_primitives:
        assert prim.id.startswith("dnd5e_2014:primitive/")
    for ability in compiled.compiled_actions:
        assert ability.step.id.startswith("dnd5e_2014:primitive/")


TRAIT_FIXTURE = """\
```statblock
name: "Test Wolf Pack Leader"
ac: 13
hp: 30
stats: [12, 15, 12, 3, 12, 6]
traits:
  - name: Pack Tactics
    desc: "The wolf has advantage on an attack roll against a creature if at
      least one of the wolf's allies is within 5 feet of the creature."
  - name: Magic Resistance
    desc: "The wolf has advantage on saving throws against spells and other
      magical effects."
  - name: Legendary Resistance (1/Day)
    desc: "If the wolf fails a saving throw, it can choose to succeed instead."
actions:
  - name: Bite
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7
      (2d4 + 2) piercing damage."
```
"""


def test_traits_compile_magic_resistance_and_legendary_resistance_ability_primitives() -> None:
    # Issue #66: Magic Resistance compiles to the same no-cost
    # `{kind: advantage, on: save}` Modifier a page-authored sim.abilities
    # entry would produce — no page needs a hand-authored sim: block.
    compiled = _compile_fixture(TRAIT_FIXTURE, "fixture-trait-wolf.md")
    ability_kinds = sorted(p.kind for p in compiled.ability_primitives)  # type: ignore[attr-defined]
    assert ability_kinds == ["advantage", "legendary_resistance_like"]
    advantage_primitive = next(
        p
        for p in compiled.ability_primitives
        if p.kind == "advantage"  # type: ignore[attr-defined]
    )
    assert advantage_primitive.on == "save"  # type: ignore[attr-defined]
    # Legendary Resistance has no consumer yet (combat.py's activation pass
    # doesn't execute legendary_resistance_like) — named unwired, never
    # silently dropped.
    assert any("legendary resistance (1/day)" in w for w in compiled.warnings)


def test_pack_tactics_trait_sets_advantage_if_on_compiled_attacks() -> None:
    compiled = _compile_fixture(TRAIT_FIXTURE, "fixture-trait-wolf.md")
    bite = next(c for c in compiled.compiled_actions if c.name == "Bite")
    assert bite.step.advantage_if == "ally_adjacent_to_target"  # type: ignore[attr-defined]


LEGENDARY_FIXTURE = """\
```statblock
name: "Test Legendary Stub"
ac: 15
hp: 100
stats: [16, 12, 14, 10, 10, 10]
legendary_actions:
  - name: ""
    desc: "The stub can take 1 legendary action, choosing from the options
      below, only at the end of another creature's turn. The stub regains
      its spent legendary action at the start of its turn."
  - name: Lash
    desc: "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit:
      10 (2d6 + 3) bludgeoning damage."
```
"""

MASTERY_FIXTURE = """\
```statblock
name: Delmar Fisk
ac: 16
hp: 30
stats: [10, 18, 12, 12, 12, 14]
sim:
  side: party
actions:
  - name: "The Baroness (rapier)"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target.
      Hit: 8 (1d8 + 4) piercing damage."
    sim: { id: baroness-rapier, mastery: vex }
  - name: "The Duchess (musket)"
    desc: "Ranged Weapon Attack: +7 to hit, range 40/120 ft., one target.
      Hit: 11 (1d12 + 4) piercing damage."
    sim: { id: duchess-musket, mastery: slow }
```
"""


def test_compile_statblock_carries_legendary_actions_per_round() -> None:
    content = parse_statblock_page(LEGENDARY_FIXTURE, "fixture-legendary-stub.md")
    assert content is not None
    fence = extract_statblock_fence(LEGENDARY_FIXTURE)
    assert fence is not None
    block = yaml.safe_load(fence)
    actions, _warnings = parse_action_category(block.get("legendary_actions"), "legendary_actions")
    action_categories = {action.name: "legendary_actions" for action in actions}
    compiled = compile_statblock(
        content,
        actions=actions,
        action_categories=action_categories,
        legendary_actions_per_round=1,
    )
    assert compiled.legendary_actions_per_round == 1


def test_compile_statblock_defaults_legendary_actions_per_round_to_zero() -> None:
    content = parse_statblock_page(OTAR_FIXTURE, "fixture-otar.md")
    assert content is not None
    compiled = compile_statblock(content, actions=[])
    assert compiled.legendary_actions_per_round == 0


def test_compile_statblock_carries_raw_ability_scores() -> None:
    """A rolled-initiative Dex tiebreak (or any other RAW-ability-score
    consumer) needs the bare score, not ``save_bonuses`` — that dict is
    overwritten by a proficient ``saves:`` entry and no longer reflects the
    plain ability score PHB p.189's tiebreak rule calls for."""
    content = parse_statblock_page(LEGENDARY_FIXTURE, "fixture-legendary-stub.md")
    assert content is not None
    compiled = compile_statblock(content, actions=[])
    assert compiled.abilities == {"str": 16, "dex": 12, "con": 14, "int": 10, "wis": 10, "cha": 10}


def test_otar_fixture_compiles_with_three_legendary_actions_per_round() -> None:
    # tests/fixtures/fixture-otar-the-foul.md's own legendary_actions preamble
    # declares "can take 3 legendary actions" (not the brief's illustrative
    # 1 — the fixture's own prose wins; asserted number matches it, not
    # the fixture edited to match a guess).
    from pathlib import Path

    from dndsim.profile import load_compiled_statblock

    # Fix-broken-tools-immediately (found this session): a bare
    # cwd-relative path only resolved when pytest happened to be invoked
    # from utils/dndsim itself — `npm run test:dndsim` (this project's own
    # documented command, CLAUDE.md) runs from the repo root instead and
    # raised FileNotFoundError. Every other fixture-loading test in this
    # tree anchors off `Path(__file__)` (see tests/cli/test_parse.py and
    # siblings) — matching that convention here too.
    fixture_path = Path(__file__).parent.parent / "fixtures" / "fixture-otar-the-foul.md"
    text = fixture_path.read_text()
    compiled, _block = load_compiled_statblock(text, str(fixture_path))
    assert compiled.legendary_actions_per_round == 3


def test_compile_action_carries_legendary_cost_from_parsed_usage() -> None:
    # Real Otar prose (fixture-otar-the-foul.md) — Bile Spray's own name
    # carries "(Costs 2 Actions)", parsed by attack_string.parse_name_usage
    # into ActionUsage.legendary_cost long before this task; compile_action
    # never read it onto CompiledAbility until now.
    action = parse_action(
        "Bile Spray (Costs 2 Actions)",
        "Otar vomits a 15-foot cone of caustic bile. Each creature in the "
        "cone must succeed on a DC 17 Constitution saving throw or take "
        "21 (6d6) acid damage.",
    )
    compiled = compile_action("dnd5e_2014", "otar", 0, action, ActionSim())
    assert compiled is not None
    assert compiled.legendary_cost == 2


def test_compile_action_defaults_legendary_cost_to_one() -> None:
    # "Lash" ("Otar makes one Tongue Lash attack.") compiles to None today
    # — unmodeled prose with no attack-grammar sentence of its own, a
    # pre-existing gap unrelated to this task (see combat.py's
    # _make_legendary_handler docstring). Thrash is Otar's own named
    # legendary action that DOES compile (a real save primitive) and
    # carries no "Costs N Actions" usage rider at all.
    action = parse_action(
        "Thrash",
        "Otar thrashes violently. Each creature within 5 feet must succeed "
        "on a DC 17 Strength saving throw or be pushed 10 feet and knocked "
        "prone.",
    )
    compiled = compile_action("dnd5e_2014", "otar", 0, action, ActionSim())
    assert compiled is not None
    assert compiled.legendary_cost == 1


def test_per_action_mastery_compiles_onto_the_attack_primitive() -> None:
    # issue #71: 2024 PHB Weapon Mastery — a per-action `sim:` override
    # (mirrors delmar-fisk-sheet.md's real Baroness/Duchess weapon names).
    compiled = _compile_fixture(MASTERY_FIXTURE, "fixture-mastery.md")
    rapier = next(c for c in compiled.compiled_actions if c.name == "The Baroness (rapier)")
    musket = next(c for c in compiled.compiled_actions if c.name == "The Duchess (musket)")
    assert rapier.step.mastery == "vex"  # type: ignore[attr-defined]
    assert musket.step.mastery == "slow"  # type: ignore[attr-defined]


def test_action_with_no_mastery_override_compiles_to_none() -> None:
    compiled = _compile_fixture(OTAR_FIXTURE, "fixture-otar.md")
    bite = next(c for c in compiled.compiled_actions if c.name == "Bite")
    assert bite.step.mastery is None  # type: ignore[attr-defined]


def test_unmodeled_action_with_no_sim_override_compiles_to_nothing() -> None:
    flavor_desc = "Does something unmodeled with no dice at all."
    content = parse_statblock_page(
        "```statblock\nname: Stub\nac: 10\nhp: 10\nstats: [10,10,10,10,10,10]\n"
        f'actions:\n  - name: "Flavor Only"\n    desc: "{flavor_desc}"\n```\n',
        "stub.md",
    )
    assert content is not None
    actions, _warnings = parse_action_category(
        [{"name": "Flavor Only", "desc": flavor_desc}], "actions"
    )
    compiled = compile_statblock(content, actions=actions)
    assert compiled.compiled_actions == ()


# --- registration replaces dispatch (no switch; extensible without an edit)


def test_new_action_kind_needs_no_compiler_edit() -> None:
    """A registry-registered compiler for a brand-new dummy action kind must
    drive through compile_action unchanged — proves ACTION_KIND_COMPILERS
    dispatch, not a hand-written branch."""

    class DummyPrimitive(PrimitiveBase):
        kind: Literal["dummy_test_action_kind"] = "dummy_test_action_kind"

    calls: list[str] = []

    def _compile_dummy(action: object, action_sim: ActionSim, primitive_id: str) -> PrimitiveBase:
        calls.append(primitive_id)
        return DummyPrimitive(id=primitive_id)

    dummy_compilers: Registry[ActionCompiler] = ACTION_KIND_COMPILERS
    dummy_compilers.register_value("dummy_test_action_kind", _compile_dummy)

    class DummyAction:
        kind = "dummy_test_action_kind"
        name = "Dummy"

    result = compile_action("test", "stub", 0, DummyAction(), ActionSim())  # type: ignore[arg-type]
    assert result is not None
    assert result.step.id == calls[0]
