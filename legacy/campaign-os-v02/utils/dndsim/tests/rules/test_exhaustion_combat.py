"""Issue #55's acceptance criterion made checkable end to end: the SAME
CombatantSpec, unchanged, scores differently under the 2014 and 2024 Rules
packs, and the difference is attributable to Exhaustion — the one
mechanic this pass gives a real, pack-scoped resolution. Every wiring
point (`_init_state`, `_resolve_attack_primitive`'s to-hit,
`_save_advantage_mode`/`_save_bonus`, `_take_turn`'s speed read) is
exercised here against the real `run_combat`/`_init_state` call path, not
re-derived — `tests/rules/test_exhaustion.py` covers the data contract in
isolation.
"""

from __future__ import annotations

import numpy as np

from dndsim import plugins
from dndsim.core.universe import UniverseBatch
from dndsim.rules.dnd5e_2014.attack_string import DamageGroup
from dndsim.rules.dnd5e_2014.combat import (
    DEFAULT_EXHAUSTION_RULES_ID,
    _init_state,
    _save_advantage_mode,
    _save_bonus,
    run_combat,
)
from dndsim.rules.dnd5e_2014.compile import CompiledAbility, CompiledStatblock
from dndsim.rules.dnd5e_2014.exhaustion import RULES_ID as RULES_ID_2014
from dndsim.rules.dnd5e_2014.fixture import CombatantSpec, make_combatant
from dndsim.rules.dnd5e_2014.primitives import AttackPrimitive, RoutineStepPrimitive
from dndsim.rules.dnd5e_2024.exhaustion import RULES_ID as RULES_ID_2024

plugins.load_rules_packs()
plugins.load_policies()


def test_run_combat_defaults_to_the_2024_pack() -> None:
    assert DEFAULT_EXHAUSTION_RULES_ID == RULES_ID_2024


def _attacker(exhaustion_level: int) -> CombatantSpec:
    attack_id = "dnd5e_2014:primitive/attack/fixture-exhaustion-dagger"
    ability = CompiledAbility(
        id=attack_id,
        name="Dagger",
        step=AttackPrimitive(
            id=attack_id, to_hit=5, damage=[DamageGroup(dice="1d4+3", type="piercing")]
        ),
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-exhausted-attacker",
        name="Exhausted Attacker",
        ac=12,
        hp=30,
        side="party",
        compiled_actions=(ability,),
        routine=(RoutineStepPrimitive(ref=attack_id, count=1, alternatives=[]),),
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-exhausted-attacker",
        name="Exhausted Attacker",
        hp_max=30,
        armor_class=12,
        attack_bonus=5,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=4,
        compiled=statblock,
        exhaustion_level=exhaustion_level,
    )


def _dummy_target() -> CombatantSpec:
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-exhaustion-dummy",
        name="Dummy",
        ac=12,
        hp=200,
        side="enemy",
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-exhaustion-dummy",
        name="Dummy",
        hp_max=200,
        armor_class=12,
        attack_bonus=0,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
        compiled=statblock,
    )


def test_the_same_statblock_scores_differently_under_each_edition_attack_roll() -> None:
    """AC: "the same statblock scores under both editions and the
    difference is attributable" — same CombatantSpec (exhaustion_level=3),
    same seed, only `exhaustion_rules_id` differs. 2024's flat -6 to-hit
    (2 x level 3) lands fewer hits than 2014's unmodified to-hit (2014's
    tiered table only imposes disadvantage on SAVES at level 3+, never a
    numeric attack-roll penalty — see `dnd5e_2014/exhaustion.py`), so 2024
    deals strictly less mean damage at the same seed."""
    attacker = _attacker(exhaustion_level=3)
    dummy = _dummy_target()
    result_2014 = run_combat(
        [attacker],
        [dummy],
        UniverseBatch(size=4000, seed=55),
        round_cap=10,
        exhaustion_rules_id=RULES_ID_2014,
    )
    result_2024 = run_combat(
        [attacker],
        [dummy],
        UniverseBatch(size=4000, seed=55),
        round_cap=10,
        exhaustion_rules_id=RULES_ID_2024,
    )
    dmg_2014 = next(
        c.mean_damage_dealt for c in result_2014.combatant_outputs if "exhausted-attacker" in c.id
    )
    dmg_2024 = next(
        c.mean_damage_dealt for c in result_2024.combatant_outputs if "exhausted-attacker" in c.id
    )
    assert dmg_2024 < dmg_2014


def test_an_unexhausted_statblock_scores_identically_under_either_edition() -> None:
    """The flip side of the same criterion: a combatant nobody authored
    Exhaustion onto (`exhaustion_level=0`, every real statblock today)
    must be unaffected by which edition is active — proving the
    divergence is exhaustion-attributable, not an incidental side effect
    of picking a Rules pack."""
    attacker = _attacker(exhaustion_level=0)
    dummy = _dummy_target()
    result_2014 = run_combat(
        [attacker], [dummy], UniverseBatch(size=2000, seed=7), exhaustion_rules_id=RULES_ID_2014
    )
    result_2024 = run_combat(
        [attacker], [dummy], UniverseBatch(size=2000, seed=7), exhaustion_rules_id=RULES_ID_2024
    )
    assert result_2014 == result_2024


def test_init_state_resolves_speed_through_the_selected_edition() -> None:
    spec = _attacker(exhaustion_level=4)
    state_2014 = _init_state(spec, "party", 5, RULES_ID_2014)
    state_2024 = _init_state(spec, "party", 5, RULES_ID_2024)
    # level 4: 2014 halves (>=2, <5-zero) -> 15; 2024 flat -5ft/level -> 10.
    assert state_2014.exhaustion_speed_ft == 15
    assert state_2024.exhaustion_speed_ft == 10


def test_save_advantage_mode_imposes_2014_disadvantage_from_level_3_never_2024() -> None:
    spec_3 = _attacker(exhaustion_level=3)
    state_2014 = _init_state(spec_3, "party", 5, RULES_ID_2014)
    state_2024 = _init_state(spec_3, "party", 5, RULES_ID_2024)
    mask = np.ones(5, dtype=np.bool_)
    assert _save_advantage_mode(state_2014, mask) == "disadvantage"
    assert _save_advantage_mode(state_2024, mask) == "normal"


def test_save_bonus_carries_2024s_flat_penalty_never_2014s() -> None:
    spec_3 = _attacker(exhaustion_level=3)
    state_2014 = _init_state(spec_3, "party", 5, RULES_ID_2014)
    state_2024 = _init_state(spec_3, "party", 5, RULES_ID_2024)
    assert _save_bonus(state_2014, "dex") == 0  # no save_bonuses authored; 2014 applies no number
    assert _save_bonus(state_2024, "dex") == -6  # 2 x level 3
