from __future__ import annotations

import numpy as np
import pytest

from dndsim import plugins
from dndsim.core.events import Event, EventBus
from dndsim.core.policy import policies
from dndsim.core.universe import UniverseBatch
from dndsim.rules.dnd5e_2014.attack_string import DamageGroup, TargetClause
from dndsim.rules.dnd5e_2014.combat import (
    ATTACK_HIT_EVENT,
    MASTERY_SLOW_TAG,
    _activate_ability_primitives,
    _apply_damage_reduction_reaction,
    _combined_advantage,
    _dice_cost_stats,
    _init_state,
    _mastery_vex_source,
    _mastery_vex_tag,
    _register_opportunity_attack,
    _resolve_attack_primitive,
    _rider_value,
    _run_ability,
    _run_routine,
    _shrink_leading_dice,
    _take_turn,
    run_combat,
)
from dndsim.rules.dnd5e_2014.compile import CompiledAbility, CompiledStatblock
from dndsim.rules.dnd5e_2014.encounter_timeline import START_OF_TURN
from dndsim.rules.dnd5e_2014.fixture import (
    PARTY_VS_ENEMIES_FIXTURE,
    TWO_COMBATANT_FIXTURE,
    CombatantSpec,
    make_combatant,
)
from dndsim.rules.dnd5e_2014.loadouts import LairAction
from dndsim.rules.dnd5e_2014.primitives import (
    AttackPrimitive,
    ReactionPrimitive,
    RoutineStepPrimitive,
    SavePrimitive,
    modifier_to_primitive,
)
from dndsim.rules.dnd5e_2014.sim_extension import (
    DamageDie,
    EffectRider,
    OnFailBlock,
    Position,
    ResourcePoolSpec,
    describe_modifier,
)
from dndsim.rules.dnd5e_2014.statblock import Defenses

plugins.load_rules_packs()
plugins.load_policies()


def _attack(id_: str, to_hit: int, damage: list[DamageGroup]) -> AttackPrimitive:
    return AttackPrimitive(id=id_, to_hit=to_hit, damage=damage)


def _target() -> CombatantSpec:
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/dummy", name="Dummy", ac=12, hp=200, side="enemy"
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/dummy",
        name="Dummy",
        hp_max=200,
        armor_class=12,
        attack_bonus=0,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
        compiled=statblock,
    )


def test_combined_advantage_extra_advantage_source_cancels_with_disadvantage() -> None:
    # Issue #66: Pack Tactics' ally-adjacent-to-target mask is folded in as
    # one more advantage source, subject to the same any-advantage-cancels-
    # any-disadvantage rule as every other source (PHB p.173) — it never
    # bypasses position disadvantage.
    condition_mode = np.array([0, 0, 0], dtype=np.int8)
    position_disadvantage = np.array([0, 1, 0], dtype=np.int64)
    extra_advantage = np.array([True, True, False])
    combined = _combined_advantage(condition_mode, position_disadvantage, extra_advantage)
    assert combined.tolist() == [1, 0, 0]  # advantage; cancelled by disadvantage; normal


def test_run_combat_is_deterministic_for_a_given_seed() -> None:
    a, b = TWO_COMBATANT_FIXTURE
    result_1 = run_combat([a], [b], UniverseBatch(size=5000, seed=123))
    result_2 = run_combat([a], [b], UniverseBatch(size=5000, seed=123))
    assert result_1 == result_2


def test_run_combat_different_seeds_differ() -> None:
    a, b = TWO_COMBATANT_FIXTURE
    result_1 = run_combat([a], [b], UniverseBatch(size=5000, seed=1))
    result_2 = run_combat([a], [b], UniverseBatch(size=5000, seed=2))
    assert result_1.party_win_rate != result_2.party_win_rate


def test_run_combat_rates_sum_to_one() -> None:
    a, b = TWO_COMBATANT_FIXTURE
    result = run_combat([a], [b], UniverseBatch(size=5000, seed=7))
    total = result.party_win_rate + result.enemy_win_rate + result.draw_rate
    # Three independent Monte Carlo means summed in floating point — exact
    # equality is not guaranteed (and isn't the property under test; each
    # rate is `count / size` and every universe falls in exactly one
    # bucket), only agreement to float precision.
    assert total == pytest.approx(1.0)


def test_run_combat_respects_round_cap() -> None:
    a, b = TWO_COMBATANT_FIXTURE
    result = run_combat([a], [b], UniverseBatch(size=2000, seed=7), round_cap=3)
    assert result.rounds_cap == 3
    assert result.mean_rounds <= 3.0


def test_run_combat_rejects_an_empty_side() -> None:
    a, b = TWO_COMBATANT_FIXTURE
    try:
        run_combat([], [b], UniverseBatch(size=10, seed=1))
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for an empty party")


def test_run_combat_party_vs_enemies_is_deterministic() -> None:
    party, enemies = PARTY_VS_ENEMIES_FIXTURE
    result_1 = run_combat(party, enemies, UniverseBatch(size=2000, seed=42))
    result_2 = run_combat(party, enemies, UniverseBatch(size=2000, seed=42))
    assert result_1 == result_2


def test_run_combat_party_vs_enemies_carries_per_pc_and_per_combatant_detail() -> None:
    party, enemies = PARTY_VS_ENEMIES_FIXTURE
    result = run_combat(party, enemies, UniverseBatch(size=2000, seed=42))
    assert len(result.pc_outcomes) == len(party)
    assert {pc.id for pc in result.pc_outcomes} == {c.entity.id for c in party}
    assert len(result.combatant_outputs) == len(party) + len(enemies)
    assert len(result.at_least_k_down) == len(party)
    # Rowan (ranged) should show some opportunity-attack/positional activity
    # across 2000 universes of a real 3-vs-3 fight with a melee threat.
    rowan = next(c for c in result.combatant_outputs if c.id == "dnd5e_2014:combatant/rowan")
    assert rowan.mean_damage_dealt > 0


def test_run_combat_party_vs_enemies_respects_selected_policy() -> None:
    party, enemies = PARTY_VS_ENEMIES_FIXTURE
    greedy = run_combat(
        party, enemies, UniverseBatch(size=2000, seed=42), policy_id="dndsim:policy/greedy"
    )
    routine = run_combat(
        party, enemies, UniverseBatch(size=2000, seed=42), policy_id="dndsim:policy/routine"
    )
    # Greedy targets by highest expected value; routine always targets
    # whichever option was declared first — different targeting rules must
    # produce a different per-combatant damage distribution even on the
    # rare seed/sample where the aggregate win rate happens to tie.
    greedy_damage = tuple(c.mean_damage_dealt for c in greedy.combatant_outputs)
    routine_damage = tuple(c.mean_damage_dealt for c in routine.combatant_outputs)
    assert greedy_damage != routine_damage


# --- compiled-statblock execution (issue #60) --------------------------------


def _multiattacker(*, routine_count: int) -> CombatantSpec:
    attack_id = "dnd5e_2014:primitive/attack/fixture-dagger"
    ability = CompiledAbility(
        id=attack_id,
        name="Dagger",
        step=_attack(attack_id, 5, [DamageGroup(dice="1d4+3", type="piercing")]),
    )
    routine = (
        (RoutineStepPrimitive(ref=attack_id, count=routine_count, alternatives=[]),)
        if routine_count > 0
        else ()
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-multiattacker",
        name="Fixture Multiattacker",
        ac=12,
        hp=30,
        side="party",
        compiled_actions=(ability,),
        routine=routine,
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-multiattacker",
        name="Fixture Multiattacker",
        hp_max=30,
        armor_class=12,
        attack_bonus=5,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=4,
        compiled=statblock,
    )


def test_run_combat_executes_a_multiattack_routine_not_a_single_attack() -> None:
    """A compiled Multiattack (count=2) deals meaningfully more damage over
    the same encounter than the identical statblock's own count=1 routine —
    not the single flat swing the old ``combatant_spec_from_compiled``/
    ``_reduce_damage`` bridge modeled regardless of a real Multiattack."""
    dummy = _target()
    single = run_combat(
        [_multiattacker(routine_count=1)], [dummy], UniverseBatch(size=3000, seed=11), round_cap=10
    )
    double = run_combat(
        [_multiattacker(routine_count=2)], [dummy], UniverseBatch(size=3000, seed=11), round_cap=10
    )
    single_out = next(c for c in single.combatant_outputs if "multiattacker" in c.id)
    double_out = next(c for c in double.combatant_outputs if "multiattacker" in c.id)
    single_dmg = single_out.mean_damage_dealt
    double_dmg = double_out.mean_damage_dealt
    assert double_dmg > single_dmg * 1.3


# --- Multiattack target-lock fix: re-target when the current swing target
# goes Down (not dead) mid-routine, instead of dumping every remaining swing
# into an already-unconscious combatant — a fresh candidate pool each
# swing. ------------------------------


def _low_hp_enemy(suffix: str, hp: int) -> CombatantSpec:
    statblock = CompiledStatblock(
        id=f"dnd5e_2014:statblock/dummy-{suffix}",
        name=f"Dummy {suffix}",
        ac=12,
        hp=hp,
        side="enemy",
    )
    return make_combatant(
        entity_id=f"dnd5e_2014:combatant/dummy-{suffix}",
        name=f"Dummy {suffix}",
        hp_max=hp,
        armor_class=12,
        attack_bonus=0,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
        compiled=statblock,
    )


def _no_op_routine_context(
    target_ranking: list[str], size: int
) -> tuple[np.ndarray, dict[str, np.ndarray], dict[str, np.ndarray], dict[str, np.ndarray]]:
    """A `_run_routine` call's own targeting context, flattened to "nothing
    ever blocks a shot": every declared target is always usable and never
    stands next to a hostile/ally — isolates the retarget logic itself from
    position/range concerns this fix does not touch."""
    condition_mode = np.zeros(size, dtype=np.int8)
    always_usable = {oid: np.ones(size, dtype=np.bool_) for oid in target_ranking}
    never_hostile_adjacent = {oid: np.zeros(size, dtype=np.bool_) for oid in target_ranking}
    never_ally_adjacent = {oid: np.zeros(size, dtype=np.bool_) for oid in target_ranking}
    return condition_mode, always_usable, never_hostile_adjacent, never_ally_adjacent


def test_run_routine_retargets_a_universe_whose_target_goes_down_mid_routine() -> None:
    """A 5-swing Multiattack against the weaker of two enemies: in whichever
    universes the weak one (8 hp) drops to 0 hp partway through the 5
    swings, the remaining swings must land on the other, still-up enemy
    instead of continuing to pile onto the Down one — while universes where
    the weak one never goes Down leave the other enemy completely
    untouched, proving the retarget only fires where it is actually
    warranted."""
    size = 6000
    actor = _multiattacker(routine_count=5)
    weak = _low_hp_enemy("weak", hp=8)
    strong = _low_hp_enemy("strong", hp=200)
    batch = UniverseBatch(size=size, seed=11)
    combatants = {
        actor.entity.id: _init_state(actor, "party", size),
        weak.entity.id: _init_state(weak, "enemy", size),
        strong.entity.id: _init_state(strong, "enemy", size),
    }
    target_ranking = [weak.entity.id, strong.entity.id]
    condition_mode, usable, hostile_adjacent_by_target, ally_adjacent_by_target = (
        _no_op_routine_context(target_ranking, size)
    )
    mask = np.ones(size, dtype=np.bool_)
    bus = EventBus()
    _run_routine(
        batch.rng,
        bus,
        actor.entity.id,
        combatants[actor.entity.id],
        weak.entity.id,
        combatants[weak.entity.id],
        mask,
        condition_mode,
        hostile_adjacent_by_target[weak.entity.id],
        ally_adjacent_by_target[weak.entity.id],
        combatants,
        target_ranking,
        usable,
        hostile_adjacent_by_target,
        ally_adjacent_by_target,
    )
    weak_state = combatants[weak.entity.id]
    strong_state = combatants[strong.entity.id]
    weak_went_down = weak_state.down.down & ~weak_state.down.dead
    strong_damage_taken = strong_state.hp.max_value - strong_state.hp.current

    # Sanity: this scenario actually produces both outcomes across the batch.
    assert bool(weak_went_down.any())
    assert bool((~weak_state.down.down).any())

    # The fix: some universes redirected onto the other enemy...
    assert bool((strong_damage_taken > 0).any())
    # ...and only universes where the weak enemy never went Down at all keep
    # the strong enemy completely untouched (a universe where it goes Down
    # only on the very last swing has nothing left to redirect either, so it
    # is excluded from this stricter check).
    never_down_mask = ~weak_state.down.down
    assert bool((strong_damage_taken[never_down_mask] == 0).all())


def test_run_routine_keeps_swinging_at_the_down_target_when_no_replacement_exists() -> None:
    """Regression: a 1v1 fight has no alternative in `target_ranking` to
    retarget onto, so every swing keeps landing on the same (possibly Down)
    target exactly as before this fix — the total damage dealt is
    bit-for-bit unchanged."""
    size = 3000
    actor = _multiattacker(routine_count=4)
    lone = _target()
    batch = UniverseBatch(size=size, seed=11)
    combatants = {
        actor.entity.id: _init_state(actor, "party", size),
        lone.entity.id: _init_state(lone, "enemy", size),
    }
    target_ranking = [lone.entity.id]
    condition_mode, usable, hostile_adjacent_by_target, ally_adjacent_by_target = (
        _no_op_routine_context(target_ranking, size)
    )
    mask = np.ones(size, dtype=np.bool_)
    bus = EventBus()
    _run_routine(
        batch.rng,
        bus,
        actor.entity.id,
        combatants[actor.entity.id],
        lone.entity.id,
        combatants[lone.entity.id],
        mask,
        condition_mode,
        hostile_adjacent_by_target[lone.entity.id],
        ally_adjacent_by_target[lone.entity.id],
        combatants,
        target_ranking,
        usable,
        hostile_adjacent_by_target,
        ally_adjacent_by_target,
    )
    mean_dealt = float(combatants[actor.entity.id].damage_dealt.mean())
    # Golden value captured from this exact scenario against the pre-fix
    # `_run_routine` (single fixed target, no retargeting code at all) —
    # confirms the fix is a genuine no-op with only one legal target.
    assert mean_dealt == pytest.approx(15.766666666666667)


def _dual_wielder(*, with_bonus: bool) -> CombatantSpec:
    action_id = "dnd5e_2014:primitive/attack/fixture-longsword"
    bonus_id = "dnd5e_2014:primitive/attack/fixture-offhand"
    action_ability = CompiledAbility(
        id=action_id,
        name="Longsword",
        step=_attack(action_id, 6, [DamageGroup(dice="1d8+3", type="slashing")]),
        action_cost="action",
    )
    compiled_actions: tuple[CompiledAbility, ...] = (action_ability,)
    if with_bonus:
        bonus_ability = CompiledAbility(
            id=bonus_id,
            name="Offhand Dagger",
            step=_attack(bonus_id, 6, [DamageGroup(dice="1d4+3", type="piercing")]),
            action_cost="bonus",
        )
        compiled_actions = (action_ability, bonus_ability)
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-dual-wielder",
        name="Fixture Dual-Wielder",
        ac=14,
        hp=30,
        side="party",
        compiled_actions=compiled_actions,
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-dual-wielder",
        name="Fixture Dual-Wielder",
        hp_max=30,
        armor_class=14,
        attack_bonus=6,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=8,
        compiled=statblock,
    )


def test_run_combat_freeform_turn_uses_both_action_and_bonus_slot() -> None:
    """No routine declared -> the action slot AND the bonus slot each pick
    their own compiled ability: a combatant with a bonus-cost attack
    available deals meaningfully more damage over the encounter than the
    identical statblock with only its action-slot attack."""
    dummy = _target()
    action_only = run_combat(
        [_dual_wielder(with_bonus=False)], [dummy], UniverseBatch(size=3000, seed=13), round_cap=10
    )
    with_bonus = run_combat(
        [_dual_wielder(with_bonus=True)], [dummy], UniverseBatch(size=3000, seed=13), round_cap=10
    )
    action_only_dmg = next(
        c for c in action_only.combatant_outputs if "dual-wielder" in c.id
    ).mean_damage_dealt
    with_bonus_dmg = next(
        c for c in with_bonus.combatant_outputs if "dual-wielder" in c.id
    ).mean_damage_dealt
    assert with_bonus_dmg > action_only_dmg * 1.2


def test_run_combat_lair_actions_from_scenario_data_apply_damage() -> None:
    """A ``lair_actions`` list (a scenario's own ``lair:`` entries) drives
    the lair window with real dc/save/on_fail damage instead of the
    hardcoded generic poison effect."""
    from dataclasses import replace

    a, b = TWO_COMBATANT_FIXTURE
    lair_owner = replace(b, has_lair=True)
    lair_action = LairAction(
        id="dnd5e_2014:lair/fixture-collapse",
        dc=1,  # near-certain failure at bonus 0, so damage reliably lands
        save="dex",
        on_fail=OnFailBlock(damage=[DamageDie(dice="2d6", type="bludgeoning")]),
    )
    batch = UniverseBatch(size=1000, seed=17)
    result = run_combat([a], [lair_owner], batch, round_cap=1, lair_actions=(lair_action,))
    # The lair action fires once before round 1's own turns and damages the
    # opposing (party) side — Perrin's hp loss must exceed what one round
    # of the Grung Skirmisher's own attack alone would cause.
    assert result.mean_party_hp_loss > 0.0


# --- legendary pool sizing (this task) --------------------------------------


def _legendary_combatant(*, legendary_actions_per_round: int) -> CombatantSpec:
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-legendary",
        name="Fixture Legendary",
        ac=15,
        hp=100,
        side="enemy",
        legendary_actions_per_round=legendary_actions_per_round,
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-legendary",
        name="Fixture Legendary",
        hp_max=100,
        armor_class=15,
        attack_bonus=6,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=6,
        legendary=True,
        compiled=statblock,
    )


def test_legendary_pool_sized_from_compiled_statblocks_own_declared_count(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """combat.py's legendary ``ResourcePool`` must size itself from each
    legendary combatant's own compiled ``legendary_actions_per_round`` (Otar's
    Phase 1 vs. Phase 2 statblocks), never the flat hardcoded 3.0 every
    legendary creature used to get regardless of its own declared count.
    Asserting on the pool's own ``max_value`` (never on stochastic
    round-by-round behavior) via a recording subclass swapped in for
    ``ResourcePool`` — ``run_combat`` returns no other seam that exposes its
    internal per-combatant resource pools."""
    from dndsim.core.resources import ResourcePool
    from dndsim.rules.dnd5e_2014 import combat as combat_module

    recorded: list[np.ndarray] = []

    class _RecordingResourcePool(ResourcePool):
        def __init__(self, name: str, max_value: np.ndarray) -> None:
            super().__init__(name, max_value)
            if name == "legendary":
                recorded.append(max_value.copy())

    monkeypatch.setattr(combat_module, "ResourcePool", _RecordingResourcePool)

    attacker = _target()
    run_combat(
        [attacker],
        [_legendary_combatant(legendary_actions_per_round=1)],
        UniverseBatch(size=50, seed=1),
        round_cap=1,
    )
    assert recorded[-1].min() == 1.0
    assert recorded[-1].max() == 1.0

    run_combat(
        [attacker],
        [_legendary_combatant(legendary_actions_per_round=3)],
        UniverseBatch(size=50, seed=1),
        round_cap=1,
    )
    assert recorded[-1].min() == 3.0
    assert recorded[-1].max() == 3.0


# --- legendary handler executes named legendary actions (this task) --------


def test_legendary_handler_selects_the_highest_ev_affordable_named_action() -> None:
    """A legendary combatant compiled with two legendary_actions: a weak
    single-target attack (near-certain miss against AC 30) and a strong
    AoE save (near-certain fail at DC 30 against a target with no save
    bonus) — both costing 1 out of a 1/round pool. The old hardcoded
    ``_resolve_hits(rng, legendary, oid, target, mask, "normal")`` ignored
    both and always ran a flat generic attack instead; the handler must
    now rank by ``_ability_ev`` and actually run the AoE save's own
    Primitive, whose damage dwarfs what the near-miss attack could ever
    contribute even across the whole batch."""
    weak_attack = CompiledAbility(
        id="dnd5e_2014:ability/fixture-legendary/weak-attack",
        name="Weak Attack",
        step=AttackPrimitive(
            id="dnd5e_2014:primitive/attack/fixture-legendary-weak-attack",
            to_hit=0,
            damage=[DamageGroup(dice="1d4", type="bludgeoning")],
        ),
        action_cost="legendary",
        legendary_cost=1,
    )
    strong_save = CompiledAbility(
        id="dnd5e_2014:ability/fixture-legendary/strong-save",
        name="Strong Save",
        step=SavePrimitive(
            id="dnd5e_2014:primitive/save/fixture-legendary-strong-save",
            dc=30,
            save="con",
            targets=TargetClause(area=True, radius=15),
            on_fail=OnFailBlock(damage=[DamageDie(dice="4d6", type="acid")]),
        ),
        action_cost="legendary",
        legendary_cost=1,
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-legendary",
        name="Fixture Legendary",
        ac=15,
        hp=100,
        side="enemy",
        legendary_actions_per_round=1,
        compiled_actions=(weak_attack, strong_save),
    )
    legendary = make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-legendary",
        name="Fixture Legendary",
        hp_max=100,
        armor_class=15,
        attack_bonus=6,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=6,
        legendary=True,
        compiled=statblock,
    )
    party_target = make_combatant(
        entity_id="dnd5e_2014:combatant/party-target",
        name="Party Target",
        hp_max=500,
        armor_class=30,
        attack_bonus=0,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
    )
    result = run_combat([party_target], [legendary], UniverseBatch(size=3000, seed=1), round_cap=1)
    legendary_output = next(
        o for o in result.combatant_outputs if o.id == "dnd5e_2014:combatant/fixture-legendary"
    )
    # Weak Attack's own ceiling (it hit on every single universe, which a
    # ~5% to-hit chance against AC 30 never approaches) is 2.5 (1d4 mean).
    # Strong Save's mean is ~0.8 * 14.0 (~11.2) at DC 30 vs. a 0-bonus
    # save. Only the save's own value clears this bar.
    assert legendary_output.mean_damage_dealt > 5.0


def test_legendary_handler_respects_bile_sprays_two_action_cost() -> None:
    """A legendary combatant with legendary_actions_per_round=3 and a
    single named legendary action costing 2 (Bile Spray-shaped). The
    legendary window fires once after each of 2 party members' turns in
    round 1 (5e RAW: "at the end of another creature's turn") — the first
    firing affords the 2-cost spend (pool 3 -> 1), the second cannot
    (pool 1 < 2), so across the batch the ability's own damage lands
    close to ONE use's expected value, never two, proving
    ``legendary_cost`` is spent per-use rather than the old flat 1
    regardless of which "action" was notionally taken (which would have
    let this fire on both triggers, netting close to twice the damage)."""
    bile_spray = CompiledAbility(
        id="dnd5e_2014:ability/fixture-legendary/bile-spray",
        name="Bile Spray",
        step=SavePrimitive(
            id="dnd5e_2014:primitive/save/fixture-legendary-bile-spray",
            dc=30,
            save="con",
            targets=TargetClause(area=True, cone=15),
            on_fail=OnFailBlock(damage=[DamageDie(dice="4d6", type="acid")]),
        ),
        action_cost="legendary",
        legendary_cost=2,
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-legendary",
        name="Fixture Legendary",
        ac=15,
        hp=100,
        side="enemy",
        legendary_actions_per_round=3,
        compiled_actions=(bile_spray,),
    )
    legendary = make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-legendary",
        name="Fixture Legendary",
        hp_max=100,
        armor_class=15,
        attack_bonus=6,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=6,
        legendary=True,
        compiled=statblock,
    )
    party_a = make_combatant(
        entity_id="dnd5e_2014:combatant/party-a",
        name="Party A",
        hp_max=500,
        armor_class=30,
        attack_bonus=0,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
    )
    party_b = make_combatant(
        entity_id="dnd5e_2014:combatant/party-b",
        name="Party B",
        hp_max=500,
        armor_class=30,
        attack_bonus=0,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
    )
    result = run_combat(
        [party_a, party_b], [legendary], UniverseBatch(size=3000, seed=1), round_cap=1
    )
    legendary_output = next(
        o for o in result.combatant_outputs if o.id == "dnd5e_2014:combatant/fixture-legendary"
    )
    # Rolled-initiative turn order (this session's turn-order Divergence
    # fix): a legendary creature's pool regains at the START of ITS OWN
    # turn (5e RAW), which can fall mid-round rather than always last —
    # when it does, the pool refills in time to afford a second Bile Spray
    # after the round's remaining opponent's turn too. Averaged over all 3
    # possible turn positions (this fixture's 3 combatants, no Dex-mod
    # asymmetry) this converges empirically to about 1.3 uses at a
    # single-target-equivalent ~14 (4d6 acid, DC 30 con always fails).
    #
    # AoE-save fix (issue: AoE save actions never fire — Chaos Pulse):
    # Bile Spray's own `targets: {area: true, cone: 15}` now actually
    # catches both party members deployed in the same band (a 15-ft cone's
    # aoe_capacity is 4, so both fit), instead of being resolved as a
    # single-target save — this fixture's own bug before this fix, not a
    # deliberate scope choice (the docstring calling it "true AoE...not
    # fixed here" predates the general infrastructure fix). ~1.3 uses at
    # ~28/use (both targets hit) converges to ~37.2, stable across seeds —
    # roughly double the pre-fix single-target band (15-22), as expected
    # for a 2-target cone.
    assert 33.0 < legendary_output.mean_damage_dealt < 41.0


# --- legendary pool restores at start of owner's own turn (this task) ------


def test_legendary_pool_restores_at_the_start_of_its_owners_own_turn(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """5e RAW: a legendary creature "regains its spent legendary action(s)
    at the start of its turn" — every round, not once for the whole
    encounter. Pre-fix (Task 2's documented NOT_DONE gap), no
    ``legendary_pool.restore(...)`` call existed anywhere in the engine, so
    a ``legendary_actions_per_round=1`` pool spent its only point in round
    1 and stayed at 0 for the rest of the fight — the legendary window
    still fires every round (once per OTHER participant's turn per
    ``encounter_timeline.py``), it would just never find an affordable
    action again. Recording via a ``ResourcePool`` subclass swapped in for
    ``combat_module.ResourcePool`` — the same seam
    ``test_legendary_pool_sized_from_compiled_statblocks_own_declared_count``
    above already uses, since ``run_combat`` exposes no other way to
    inspect the internal per-combatant pool."""
    from dndsim.core.resources import ResourcePool
    from dndsim.rules.dnd5e_2014 import combat as combat_module

    legendary_restore_masks: list[np.ndarray] = []

    class _RecordingResourcePool(ResourcePool):
        def restore(self, amount: np.ndarray, mask: np.ndarray) -> None:
            super().restore(amount, mask)
            if self.name == "legendary":
                legendary_restore_masks.append(mask.copy())

    monkeypatch.setattr(combat_module, "ResourcePool", _RecordingResourcePool)

    weak_attack = CompiledAbility(
        id="dnd5e_2014:ability/fixture-legendary/weak-attack",
        name="Weak Attack",
        step=AttackPrimitive(
            id="dnd5e_2014:primitive/attack/fixture-legendary-weak-attack",
            to_hit=0,
            damage=[DamageGroup(dice="1d4", type="bludgeoning")],
        ),
        action_cost="legendary",
        legendary_cost=1,
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-legendary",
        name="Fixture Legendary",
        ac=15,
        hp=100,
        side="enemy",
        legendary_actions_per_round=1,
        compiled_actions=(weak_attack,),
    )
    legendary = make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-legendary",
        name="Fixture Legendary",
        hp_max=100,
        armor_class=15,
        attack_bonus=6,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=6,
        legendary=True,
        compiled=statblock,
    )
    party_target = make_combatant(
        entity_id="dnd5e_2014:combatant/party-target",
        name="Party Target",
        hp_max=500,
        armor_class=30,
        attack_bonus=0,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
    )
    size = 50
    round_cap = 3
    run_combat([party_target], [legendary], UniverseBatch(size=size, seed=1), round_cap=round_cap)

    # Pre-fix: legendary_restore_masks stays empty (no restore(...) call
    # ever targets the "legendary" pool), so the total below is 0, not
    # round_cap * size. Post-fix: with rolled initiative order and only 2
    # combatants, the legendary's own start_of_turn fires from whichever of
    # the round's 2 turn-order buckets it occupies — at most 2 separate
    # restore() calls per round, each restricted to its own disjoint
    # universe submask — so a raw call *count* is no longer a stable
    # assertion (the old fixed-order model always fired it exactly once
    # per round, globally). What must still hold: every universe gets
    # restored to full exactly once per round, covered across however many
    # calls that takes — the real "every round, not once for the whole
    # encounter" guarantee 5e RAW requires.
    total_restored_universes = sum(int(mask.sum()) for mask in legendary_restore_masks)
    assert total_restored_universes == round_cap * size
    # No universe is ever restored twice in the same round (the buckets
    # are disjoint) — every recorded mask this round, unioned, covers the
    # batch exactly once; summed cleanly to round_cap * size above already
    # proves this (an overlap would double-count and exceed it, a gap
    # would fall short).


# --- Weapon Mastery (issue #71: Vex/Slow) ------------------------------------


def _mastery_attacker(
    *, mastery: str | None, to_hit: int
) -> tuple[CombatantSpec, AttackPrimitive, CompiledAbility]:
    attack_id = "dnd5e_2014:primitive/attack/fixture-mastery-weapon"
    step = AttackPrimitive(
        id=attack_id,
        to_hit=to_hit,
        damage=[DamageGroup(dice="1d4", type="piercing")],
        mastery=mastery,  # type: ignore[arg-type]
    )
    ability = CompiledAbility(id=attack_id, name="Mastery Weapon", step=step)
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-mastery-attacker",
        name="Fixture Mastery Attacker",
        ac=12,
        hp=30,
        side="party",
        compiled_actions=(ability,),
    )
    spec = make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-mastery-attacker",
        name="Fixture Mastery Attacker",
        hp_max=30,
        armor_class=12,
        attack_bonus=to_hit,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
        compiled=statblock,
    )
    return spec, step, ability


def test_vex_hit_grants_a_target_scoped_advantage_tag_on_the_attacker() -> None:
    size = 2000
    actor_spec, step, _ability = _mastery_attacker(mastery="vex", to_hit=15)
    target_spec = _low_hp_enemy("vex-grant", hp=1000)
    batch = UniverseBatch(size=size, seed=3)
    actor = _init_state(actor_spec, "party", size)
    target = _init_state(target_spec, "enemy", size)
    combatants = {actor_spec.entity.id: actor, target_spec.entity.id: target}
    mask = np.ones(size, dtype=np.bool_)
    _resolve_attack_primitive(
        batch.rng,
        EventBus(),
        actor_spec.entity.id,
        actor,
        target_spec.entity.id,
        target,
        mask,
        "normal",
        step,
        combatants,
    )
    took_damage = target.hp.current < target.hp.max_value
    vex_tag = actor.tags.has(_mastery_vex_tag(target_spec.entity.id))
    assert bool(took_damage.any())  # sanity: this scenario actually produces hits
    assert (vex_tag == took_damage).all()


def test_slow_hit_sets_the_shared_speed_reduced_tag_on_the_target() -> None:
    size = 2000
    actor_spec, step, _ability = _mastery_attacker(mastery="slow", to_hit=15)
    target_spec = _low_hp_enemy("slow-grant", hp=1000)
    batch = UniverseBatch(size=size, seed=3)
    actor = _init_state(actor_spec, "party", size)
    target = _init_state(target_spec, "enemy", size)
    combatants = {actor_spec.entity.id: actor, target_spec.entity.id: target}
    mask = np.ones(size, dtype=np.bool_)
    _resolve_attack_primitive(
        batch.rng,
        EventBus(),
        actor_spec.entity.id,
        actor,
        target_spec.entity.id,
        target,
        mask,
        "normal",
        step,
        combatants,
    )
    took_damage = target.hp.current < target.hp.max_value
    slow_tag = target.tags.has(MASTERY_SLOW_TAG)
    assert bool(took_damage.any())
    assert (slow_tag == took_damage).all()


def test_vex_advantage_is_consumed_by_the_next_attack_regardless_of_hit_or_miss() -> None:
    size = 2000
    # No mastery on this weapon at all — isolates consumption of a
    # standing, pre-existing grant from this attack's own hit re-granting it.
    actor_spec, _step, ability = _mastery_attacker(mastery=None, to_hit=-30)
    target_spec = _low_hp_enemy("vex-consume", hp=1000)
    batch = UniverseBatch(size=size, seed=5)
    actor = _init_state(actor_spec, "party", size)
    target = _init_state(target_spec, "enemy", size)
    combatants = {actor_spec.entity.id: actor, target_spec.entity.id: target}
    all_true = np.ones(size, dtype=np.bool_)
    actor.effects.apply(
        source=_mastery_vex_source(actor_spec.entity.id, target_spec.entity.id),
        tag=_mastery_vex_tag(target_spec.entity.id),
        mask=all_true,
        duration_rounds=1,
    )
    condition_mode = np.zeros(size, dtype=np.int8)
    no_bool = np.zeros(size, dtype=np.bool_)
    _run_ability(
        batch.rng,
        EventBus(),
        actor_spec.entity.id,
        actor,
        target_spec.entity.id,
        target,
        all_true,
        condition_mode,
        no_bool,
        no_bool,
        [],
        combatants,
        ability,
    )
    # to_hit=-30 guarantees a mix of misses (~95%) and crits (~5%, always
    # hit) — the tag must be gone in BOTH subsets, proving consumption is
    # unconditional on this roll's own outcome.
    assert not actor.tags.has(_mastery_vex_tag(target_spec.entity.id)).any()


def test_vex_advantage_meaningfully_increases_the_next_attacks_hit_rate() -> None:
    size = 6000
    # +1 to-hit vs AC 12 (_low_hp_enemy's fixed AC): needs an 11+ to hit
    # normally (~50%); advantage raises that to ~1-0.5**2 = 75%.
    actor_spec, _step, ability = _mastery_attacker(mastery=None, to_hit=1)
    target_spec = _low_hp_enemy("vex-hit-rate", hp=100_000)
    all_true = np.ones(size, dtype=np.bool_)
    condition_mode = np.zeros(size, dtype=np.int8)
    no_bool = np.zeros(size, dtype=np.bool_)

    def _hit_rate(seed: int, *, pre_vex: bool) -> float:
        batch = UniverseBatch(size=size, seed=seed)
        actor = _init_state(actor_spec, "party", size)
        target = _init_state(target_spec, "enemy", size)
        combatants = {actor_spec.entity.id: actor, target_spec.entity.id: target}
        if pre_vex:
            actor.effects.apply(
                source=_mastery_vex_source(actor_spec.entity.id, target_spec.entity.id),
                tag=_mastery_vex_tag(target_spec.entity.id),
                mask=all_true,
                duration_rounds=1,
            )
        _run_ability(
            batch.rng,
            EventBus(),
            actor_spec.entity.id,
            actor,
            target_spec.entity.id,
            target,
            all_true,
            condition_mode,
            no_bool,
            no_bool,
            [],
            combatants,
            ability,
        )
        return float((target.hp.current < target.hp.max_value).mean())

    without_vex = _hit_rate(seed=9, pre_vex=False)
    with_vex = _hit_rate(seed=9, pre_vex=True)
    assert with_vex > without_vex + 0.15


def test_vex_advantage_does_not_leak_to_a_different_target() -> None:
    size = 500
    actor_spec, _step, ability = _mastery_attacker(mastery=None, to_hit=1)
    target_a = _low_hp_enemy("vex-scope-a", hp=1000)
    target_b = _low_hp_enemy("vex-scope-b", hp=1000)
    batch = UniverseBatch(size=size, seed=21)
    actor = _init_state(actor_spec, "party", size)
    b_state = _init_state(target_b, "enemy", size)
    combatants = {actor_spec.entity.id: actor, target_b.entity.id: b_state}
    all_true = np.ones(size, dtype=np.bool_)
    # Standing grant is against A; this attack targets B.
    actor.effects.apply(
        source=_mastery_vex_source(actor_spec.entity.id, target_a.entity.id),
        tag=_mastery_vex_tag(target_a.entity.id),
        mask=all_true,
        duration_rounds=1,
    )
    condition_mode = np.zeros(size, dtype=np.int8)
    no_bool = np.zeros(size, dtype=np.bool_)
    _run_ability(
        batch.rng,
        EventBus(),
        actor_spec.entity.id,
        actor,
        target_b.entity.id,
        b_state,
        all_true,
        condition_mode,
        no_bool,
        no_bool,
        [],
        combatants,
        ability,
    )
    # Untouched: an attack on B never consumes the standing grant against A.
    assert actor.tags.has(_mastery_vex_tag(target_a.entity.id)).all()


# --- trade_dice_for_rider (issue #67 follow-up: Cunning Strike) -------------


def test_shrink_leading_dice_reduces_leading_term_count() -> None:
    assert _shrink_leading_dice("3d6", 1) == "2d6"


def test_shrink_leading_dice_drops_the_term_entirely_leaving_the_flat_modifier() -> None:
    assert _shrink_leading_dice("1d6+2", 1) == "2"


def test_shrink_leading_dice_is_a_no_op_for_zero_or_negative_count() -> None:
    assert _shrink_leading_dice("3d6", 0) == "3d6"


def test_dice_cost_stats_string_expression_uses_its_own_count_and_average() -> None:
    by_count, avg = _dice_cost_stats("1d6", "3d6")
    assert by_count == 1
    assert avg == 3.5


def test_dice_cost_stats_int_reads_the_source_pools_own_die_size() -> None:
    by_count, avg = _dice_cost_stats(2, "3d8")
    assert by_count == 2
    assert avg == 2 * 4.5


def _trader(*, dc: float, once_per_turn_extra: bool = True) -> CombatantSpec:
    """A sneak-attack (3d6, once-per-turn) with one Cunning-Strike-shaped
    ``trade_dice_for_rider`` (``cunning-poison``) drawing 1d6 from it —
    real content's own shape (`delmar-fisk-sheet.md`), built through the
    same ``describe_modifier`` -> ``modifier_to_primitive`` compile path
    `compile.py` itself uses (never a hand-built Primitive instance).
    `dc` controls whether the EV comparison favors the trade."""
    extra_mod = describe_modifier(
        "extra_damage",
        "test.md",
        "sim.abilities[0]",
        dice="3d6",
        type="piercing",
        id="sneak-attack",
        once_per_turn=once_per_turn_extra,
    )
    trade_mod = describe_modifier(
        "trade_dice_for_rider",
        "test.md",
        "sim.abilities[1]",
        id="cunning-poison",
        from_="sneak-attack",
        dice_cost="1d6",
        save={"ability": "con", "dc": dc},
        on_fail={"effects": [{"effect": "poisoned"}]},
    )
    extra_prim = modifier_to_primitive(extra_mod, "dnd5e_2014:primitive/extra_damage/fixture-sneak")
    trade_prim = modifier_to_primitive(
        trade_mod, "dnd5e_2014:primitive/trade_dice_for_rider/fixture-poison"
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-trader",
        name="Fixture Trader",
        ac=14,
        hp=40,
        side="party",
        ability_primitives=(extra_prim, trade_prim),
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-trader",
        name="Fixture Trader",
        hp_max=40,
        armor_class=14,
        attack_bonus=8,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=8,
        compiled=statblock,
    )


def _victim() -> CombatantSpec:
    """A high-offense target (own attack profile) so denying its turn via
    the poisoned rider is worth more than the surrendered 1d6 — the same
    ``_threat_score`` a real save-or-suck ability is valued against."""
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-victim",
        name="Fixture Victim",
        ac=10,
        hp=200,
        side="enemy",
        save_bonuses={"con": 0},
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-victim",
        name="Fixture Victim",
        hp_max=200,
        armor_class=10,
        attack_bonus=8,
        damage_bonus=5,
        damage_dice_count=6,
        damage_dice_sides=10,
        compiled=statblock,
    )


def test_trade_dice_for_rider_shrinks_the_pool_and_poisons_when_ev_favors_it() -> None:
    """dc=30 vs a 0 con-save bonus auto-fails every universe (roll+0 never
    reaches 30) — the EV comparison must favor the trade against a
    high-threat victim, shrinking sneak-attack's 3d6 (avg 10.5) to 2d6
    (avg 7) and poisoning the target."""
    size = 500
    attacker = _trader(dc=30)
    target = _victim()
    batch = UniverseBatch(size=size, seed=1)
    combatants = {
        attacker.entity.id: _init_state(attacker, "party", size),
        target.entity.id: _init_state(target, "enemy", size),
    }
    bus = EventBus()
    _activate_ability_primitives(
        bus, batch.rng, actor_id=attacker.entity.id, combatants=combatants, size=size
    )
    mask = np.ones(size, dtype=np.bool_)
    bus.publish(
        Event(
            name=ATTACK_HIT_EVENT,
            payload={
                "attacker_id": attacker.entity.id,
                "target_id": target.entity.id,
                "mask": mask,
            },
        )
    )
    assert bool(combatants[target.entity.id].tags.has("poisoned").all())
    mean_dealt = float(combatants[attacker.entity.id].damage_dealt.mean())
    assert 5.0 < mean_dealt < 9.0  # 2d6 avg 7, nowhere near un-shrunk 3d6's avg 10.5


def test_trade_dice_for_rider_does_not_fire_when_the_save_auto_succeeds() -> None:
    """dc=-100 auto-succeeds every universe (any roll+0 clears it) — plain
    damage beats the trade (`value <= avg` for a p_fail of exactly 0), so
    the pool stays the full 3d6 and no condition lands."""
    size = 500
    attacker = _trader(dc=-100)
    target = _victim()
    batch = UniverseBatch(size=size, seed=1)
    combatants = {
        attacker.entity.id: _init_state(attacker, "party", size),
        target.entity.id: _init_state(target, "enemy", size),
    }
    bus = EventBus()
    _activate_ability_primitives(
        bus, batch.rng, actor_id=attacker.entity.id, combatants=combatants, size=size
    )
    mask = np.ones(size, dtype=np.bool_)
    bus.publish(
        Event(
            name=ATTACK_HIT_EVENT,
            payload={
                "attacker_id": attacker.entity.id,
                "target_id": target.entity.id,
                "mask": mask,
            },
        )
    )
    assert not bool(combatants[target.entity.id].tags.has("poisoned").any())
    mean_dealt = float(combatants[attacker.entity.id].damage_dealt.mean())
    assert mean_dealt > 9.0  # full un-shrunk 3d6 average (10.5)


def test_trade_dice_for_rider_is_gated_once_per_turn_independent_of_its_source() -> None:
    """Sneak-attack's own ``once_per_turn`` is False here so the SAME hit
    source fires twice within one turn — the trade's own once-per-turn key
    (`trade:cunning-poison`, separate from sneak-attack's own gate) must
    still cap it to a single shrink per turn, resetting only at the actor's
    next `START_OF_TURN`."""
    size = 500
    attacker = _trader(dc=30, once_per_turn_extra=False)
    target = _victim()
    batch = UniverseBatch(size=size, seed=1)
    combatants = {
        attacker.entity.id: _init_state(attacker, "party", size),
        target.entity.id: _init_state(target, "enemy", size),
    }
    bus = EventBus()
    _activate_ability_primitives(
        bus, batch.rng, actor_id=attacker.entity.id, combatants=combatants, size=size
    )
    mask = np.ones(size, dtype=np.bool_)
    attacker_state = combatants[attacker.entity.id]

    def _fire() -> None:
        bus.publish(
            Event(
                name=ATTACK_HIT_EVENT,
                payload={
                    "attacker_id": attacker.entity.id,
                    "target_id": target.entity.id,
                    "mask": mask,
                },
            )
        )

    _fire()
    first = float(attacker_state.damage_dealt.mean())
    assert 5.0 < first < 9.0  # first hit this turn: trade fires, 2d6

    _fire()
    second = float(attacker_state.damage_dealt.mean()) - first
    assert second > 9.0  # second hit, SAME turn: trade already used, full 3d6

    bus.publish(Event(name=f"{START_OF_TURN}:{attacker.entity.id}"))
    _fire()
    third = float(attacker_state.damage_dealt.mean()) - first - second
    assert 5.0 < third < 9.0  # new turn: trade's own gate reset, fires again


# --- movement_boost: Cunning-Action-style Dash/Disengage (issue #69) --------


def _movement_booster(
    *,
    grants: str,
    start_band: int | None = None,
    is_melee: bool = True,
    range_ft: float | None = None,
) -> CombatantSpec:
    """A combatant carrying one `movement_boost` ability primitive (Cunning
    Action), optionally deployed ``start_band`` bands from contact."""
    boost_mod = describe_modifier(
        "movement_boost", "test.md", "sim.abilities[0]", id="cunning-action", grants=grants
    )
    boost_prim = modifier_to_primitive(
        boost_mod, "dnd5e_2014:primitive/movement_boost/fixture-booster"
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-booster",
        name="Fixture Booster",
        ac=14,
        hp=40,
        side="party",
        ability_primitives=(boost_prim,),
        position=Position(start_band=start_band) if start_band is not None else None,
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-booster",
        name="Fixture Booster",
        hp_max=40,
        armor_class=14,
        attack_bonus=5,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=6,
        is_melee=is_melee,
        range_ft=range_ft,
        compiled=statblock,
    )


# --- reroll_take_best (issue #70: Lucky feat) --------------------------------


def _lucky_attacker(*, pool_max: float, to_hit: int = 3) -> CombatantSpec:
    """A flat ``+to_hit`` attacker with one compiled ``reroll_take_best``
    (Lucky feat) drawing from a ``luck_points`` pool of ``pool_max`` — real
    content's own shape (an authored ``{ kind: reroll_take_best, pool:
    luck_points }``), built through the same ``describe_modifier`` ->
    ``modifier_to_primitive`` compile path `compile.py` itself uses (never a
    hand-built Primitive instance)."""
    reroll_mod = describe_modifier(
        "reroll_take_best", "test.md", "sim.abilities[0]", pool="luck_points"
    )
    reroll_prim = modifier_to_primitive(
        reroll_mod, "dnd5e_2014:primitive/reroll_take_best/fixture-lucky"
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-lucky",
        name="Fixture Lucky",
        ac=14,
        hp=40,
        side="party",
        resources=(ResourcePoolSpec(id="luck_points", max=pool_max),),
        ability_primitives=(reroll_prim,),
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-lucky",
        name="Fixture Lucky",
        hp_max=40,
        armor_class=14,
        attack_bonus=to_hit,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=6,
        compiled=statblock,
    )


def test_take_turn_movement_boost_dash_doubles_the_closing_budget() -> None:
    """Issue #69: nothing is reachable from 2 bands out at 30-ft speed (one
    band per turn) — a bare melee actor closes only to 1 band away, but a
    `movement_boost` dash grant (Cunning Action) doubles this turn's budget
    to 2 bands, closing all the way to contact in the same turn —
    ``simulator.mjs:1205-1212``'s "doubles the closing budget" behavior, so
    the fight still converges instead of stalling."""
    size = 200
    actor = _movement_booster(grants="dash", start_band=2)
    target = _target()
    batch = UniverseBatch(size=size, seed=1)
    combatants = {
        actor.entity.id: _init_state(actor, "party", size),
        target.entity.id: _init_state(target, "enemy", size),
    }
    bus = EventBus()
    policy = policies.get("dndsim:policy/greedy")(seed=1)
    _take_turn(
        rng=batch.rng,
        policy=policy,
        round_num=1,
        bus=bus,
        combatants=combatants,
        actor_id=actor.entity.id,
        opposing_ids=[target.entity.id],
        party_ids=[actor.entity.id],
        enemy_ids=[target.entity.id],
        side="party",
        turn_mask=np.ones(size, dtype=np.bool_),
    )
    assert combatants[actor.entity.id].pos.pos.tolist() == [0] * size


def test_take_turn_movement_boost_disengage_avoids_the_kiting_opportunity_attack() -> None:
    """Issue #69: a ranged attacker sharing a band with a living melee
    threat kites one band back (existing behavior) — ``simulator.mjs:
    1218-1229`` Disengages first when a `movement_boost` grant covers it, so
    the withdrawal draws no opportunity attack."""
    size = 200
    actor = _movement_booster(grants="disengage", is_melee=False, range_ft=60.0)
    threat_statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-threat", name="Fixture Threat", ac=12, hp=200, side="enemy"
    )
    threat = make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-threat",
        name="Fixture Threat",
        hp_max=200,
        armor_class=12,
        attack_bonus=5,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=8,
        is_melee=True,
        compiled=threat_statblock,
    )
    batch = UniverseBatch(size=size, seed=1)
    combatants = {
        actor.entity.id: _init_state(actor, "party", size),
        threat.entity.id: _init_state(threat, "enemy", size),
    }
    bus = EventBus()
    _register_opportunity_attack(
        bus,
        batch.rng,
        mover_id=actor.entity.id,
        reactor_id=threat.entity.id,
        combatants=combatants,
    )
    policy = policies.get("dndsim:policy/greedy")(seed=1)
    _take_turn(
        rng=batch.rng,
        policy=policy,
        round_num=1,
        bus=bus,
        combatants=combatants,
        actor_id=actor.entity.id,
        opposing_ids=[threat.entity.id],
        party_ids=[actor.entity.id],
        enemy_ids=[threat.entity.id],
        side="party",
        turn_mask=np.ones(size, dtype=np.bool_),
    )
    assert combatants[actor.entity.id].pos.pos.tolist() == [-1] * size  # kited one band back
    assert float(combatants[threat.entity.id].reactions_spent.sum()) == 0.0


# --- issue #68: trade_dice_for_rider edge-case hardening --------------------


def test_shrink_leading_dice_keeps_a_negative_leading_terms_sign() -> None:
    """`dice.py`'s grammar allows a leading sign (`_TERM_RE`'s `([+-])?`), so
    a `from_` expression could in principle read ``"-1d4+3d6"`` — shrinking
    a KEPT (not fully dropped) leading term must not silently drop its own
    minus sign just because it sits at index 0."""
    assert _shrink_leading_dice("-3d6+1d4", 1) == "-2d6+1d4"


def test_rider_value_scores_an_on_success_save_ends_rider_as_a_single_round() -> None:
    """issue #68 decision: the on_success branch is scored after the target
    already succeeded the landing save — the definitionally weaker branch.
    Its own `save_ends` clause must never compound duration to the same
    3-round cap a FAILED save's rider earns (that would rate succeeding the
    save identically to the worst on_fail outcome); `_apply_trades` passes
    `on_success=True` so a save_ends rider there always scores exactly like
    a rider with no save_ends at all."""
    target = _init_state(_victim(), "enemy", 1)
    with_save_ends = _rider_value(
        [EffectRider(effect="poisoned", save_ends={"save": "con", "dc": 15})],
        target,
        0.0,
        is_on_success_branch=True,
    )
    without_save_ends = _rider_value(
        [EffectRider(effect="poisoned")], target, 0.0, is_on_success_branch=True
    )
    assert with_save_ends == without_save_ends


def _trader_with_on_success(*, dc: float) -> CombatantSpec:
    """Like :func:`_trader`, but the trade's rider has both an `on_fail`
    branch (``prone``) and an `on_success` branch (``speed_halved``) so a
    real per-universe DC can split the save outcome within one batch
    instead of the existing tests' auto-fail (dc=30) / auto-succeed
    (dc=-100) uniform masks."""
    extra_mod = describe_modifier(
        "extra_damage",
        "test.md",
        "sim.abilities[0]",
        dice="3d6",
        type="piercing",
        id="sneak-attack",
        once_per_turn=True,
    )
    trade_mod = describe_modifier(
        "trade_dice_for_rider",
        "test.md",
        "sim.abilities[1]",
        id="cunning-poison",
        from_="sneak-attack",
        dice_cost="1d6",
        save={"ability": "con", "dc": dc},
        on_fail={"effects": [{"effect": "prone"}]},
        on_success={"effects": [{"effect": "speed_halved"}]},
    )
    extra_prim = modifier_to_primitive(extra_mod, "dnd5e_2014:primitive/extra_damage/fixture-sneak")
    trade_prim = modifier_to_primitive(
        trade_mod, "dnd5e_2014:primitive/trade_dice_for_rider/fixture-poison"
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-trader",
        name="Fixture Trader",
        ac=14,
        hp=40,
        side="party",
        ability_primitives=(extra_prim, trade_prim),
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-trader",
        name="Fixture Trader",
        hp_max=40,
        armor_class=14,
        attack_bonus=8,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=8,
        compiled=statblock,
    )


def _reroll_target(*, ac: int, immune: tuple[str, ...] = ()) -> CombatantSpec:
    """A durable target at a stated `ac`, optionally immune to `immune`
    damage types (to force :meth:`MultiGroupAttackMechanic.expected_value`
    to exactly 0 for the EV-gate test)."""
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-reroll-victim",
        name="Fixture Reroll Victim",
        ac=ac,
        hp=1_000_000,
        side="enemy",
        defenses=Defenses(immune=list(immune)),
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-reroll-victim",
        name="Fixture Reroll Victim",
        hp_max=1_000_000,
        armor_class=ac,
        attack_bonus=0,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
        compiled=statblock,
    )


def test_trade_dice_for_rider_splits_a_genuinely_mixed_save_outcome() -> None:
    """dc=11 vs a 0 con-save bonus is a real coin-flip (roll >= 11 succeeds)
    — unlike every existing trade test's dc=30/-100 uniform mask, this must
    produce BOTH outcomes inside one batch: some universes land `prone`
    (on_fail) and others land `speed_halved` (on_success), never all-True
    or all-False for either tag, and never both tags on the same universe."""
    size = 500
    attacker = _trader_with_on_success(dc=11)
    target = _victim()
    batch = UniverseBatch(size=size, seed=1)
    combatants = {
        attacker.entity.id: _init_state(attacker, "party", size),
        target.entity.id: _init_state(target, "enemy", size),
    }
    bus = EventBus()
    _activate_ability_primitives(
        bus, batch.rng, actor_id=attacker.entity.id, combatants=combatants, size=size
    )
    mask = np.ones(size, dtype=np.bool_)
    bus.publish(
        Event(
            name=ATTACK_HIT_EVENT,
            payload={
                "attacker_id": attacker.entity.id,
                "target_id": target.entity.id,
                "mask": mask,
            },
        )
    )
    prone = combatants[target.entity.id].tags.has("prone")
    slowed = combatants[target.entity.id].tags.has("speed_halved")
    assert bool(prone.any()) and not bool(prone.all())
    assert bool(slowed.any()) and not bool(slowed.all())
    assert not bool((prone & slowed).any())


def test_apply_trades_rejects_a_second_trade_that_overspends_its_shared_pool() -> None:
    """Two `trade_dice_for_rider` entries (``cunning-a``, ``cunning-b``)
    both draw from the SAME `1d6` sneak-attack pool, each costing 1 die —
    the exact `_apply_trades` docstring scenario ("two trades sharing one
    source ... compound sequentially"). The first trade spends the pool's
    only die; the second must be REJECTED (issue #68's over-spend guard),
    never silently floored to 0 dice while its rider still lands as if
    paid in full."""
    size = 500
    extra_mod = describe_modifier(
        "extra_damage",
        "test.md",
        "sim.abilities[0]",
        dice="1d6",
        type="piercing",
        id="sneak-attack",
        once_per_turn=True,
    )
    trade_a = describe_modifier(
        "trade_dice_for_rider",
        "test.md",
        "sim.abilities[1]",
        id="cunning-a",
        from_="sneak-attack",
        dice_cost=1,
        save={"ability": "con", "dc": 30},
        on_fail={"effects": [{"effect": "prone"}]},
    )
    trade_b = describe_modifier(
        "trade_dice_for_rider",
        "test.md",
        "sim.abilities[2]",
        id="cunning-b",
        from_="sneak-attack",
        dice_cost=1,
        save={"ability": "con", "dc": 30},
        on_fail={"effects": [{"effect": "poisoned"}]},
    )
    extra_prim = modifier_to_primitive(extra_mod, "dnd5e_2014:primitive/extra_damage/fixture-sneak")
    trade_a_prim = modifier_to_primitive(
        trade_a, "dnd5e_2014:primitive/trade_dice_for_rider/fixture-a"
    )
    trade_b_prim = modifier_to_primitive(
        trade_b, "dnd5e_2014:primitive/trade_dice_for_rider/fixture-b"
    )
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-trader",
        name="Fixture Trader",
        ac=14,
        hp=40,
        side="party",
        ability_primitives=(extra_prim, trade_a_prim, trade_b_prim),
    )
    attacker = make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-trader",
        name="Fixture Trader",
        hp_max=40,
        armor_class=14,
        attack_bonus=8,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=8,
        compiled=statblock,
    )
    target = _victim()
    batch = UniverseBatch(size=size, seed=1)
    combatants = {
        attacker.entity.id: _init_state(attacker, "party", size),
        target.entity.id: _init_state(target, "enemy", size),
    }
    bus = EventBus()
    _activate_ability_primitives(
        bus, batch.rng, actor_id=attacker.entity.id, combatants=combatants, size=size
    )
    mask = np.ones(size, dtype=np.bool_)
    bus.publish(
        Event(
            name=ATTACK_HIT_EVENT,
            payload={
                "attacker_id": attacker.entity.id,
                "target_id": target.entity.id,
                "mask": mask,
            },
        )
    )
    assert bool(combatants[target.entity.id].tags.has("prone").all())
    assert not bool(combatants[target.entity.id].tags.has("poisoned").any())


def test_reroll_take_best_spends_a_point_and_upgrades_a_missed_attack() -> None:
    """Issue #70: a +3-to-hit attack against AC 15 hits on a natural 12+
    (45%, excluding the always-hits nat 20 and always-misses nat 1 already
    folded into that count). Lucky's reroll on the 55% that miss should push
    the final hit rate up toward ``1 - 0.55**2 = 0.6975``, spending exactly
    one luck point per universe that actually used it (~55% of the batch)."""
    size = 20_000
    attacker_spec = _lucky_attacker(pool_max=3)
    target_spec = _reroll_target(ac=15)
    combatants = {
        attacker_spec.entity.id: _init_state(attacker_spec, "party", size),
        target_spec.entity.id: _init_state(target_spec, "enemy", size),
    }
    attacker = combatants[attacker_spec.entity.id]
    target = combatants[target_spec.entity.id]
    bus = EventBus()
    batch = UniverseBatch(size=size, seed=3)
    step = _attack("fixture-attack", 3, [DamageGroup(dice="1d6", type="piercing")])
    mask = np.ones(size, dtype=np.bool_)
    _resolve_attack_primitive(
        batch.rng,
        bus,
        attacker_spec.entity.id,
        attacker,
        target_spec.entity.id,
        target,
        mask,
        "normal",
        step,
        combatants,
    )
    hit_rate = float((attacker.damage_dealt > 0).mean())
    assert 0.64 < hit_rate < 0.75  # single-roll ~0.45; Lucky pushes it toward ~0.6975
    pool = attacker.resources["luck_points"]
    spent = float((3.0 - pool.current).mean())
    assert 0.50 < spent < 0.60  # ~55% of universes missed the first roll and paid for one


def test_reroll_take_best_does_not_fire_when_the_pool_is_empty() -> None:
    """Issue #70: a pool already drained to 0 (every luck point already
    spent earlier this encounter) means every universe starts unaffordable
    — the hit rate must stay at the un-rerolled single-roll figure (~45%)
    and the pool must never go negative. ``ResourcePoolSpec.max`` itself
    must be a positive number (sim_extension.py's own validator), so the
    fixture starts at 1 and is drained by hand rather than authored at 0."""
    size = 20_000
    attacker_spec = _lucky_attacker(pool_max=1)
    target_spec = _reroll_target(ac=15)
    combatants = {
        attacker_spec.entity.id: _init_state(attacker_spec, "party", size),
        target_spec.entity.id: _init_state(target_spec, "enemy", size),
    }
    attacker = combatants[attacker_spec.entity.id]
    target = combatants[target_spec.entity.id]
    attacker.resources["luck_points"].spend(
        np.ones(size, dtype=np.float64), np.ones(size, dtype=np.bool_)
    )
    bus = EventBus()
    batch = UniverseBatch(size=size, seed=5)
    step = _attack("fixture-attack", 3, [DamageGroup(dice="1d6", type="piercing")])
    mask = np.ones(size, dtype=np.bool_)
    _resolve_attack_primitive(
        batch.rng,
        bus,
        attacker_spec.entity.id,
        attacker,
        target_spec.entity.id,
        target,
        mask,
        "normal",
        step,
        combatants,
    )
    hit_rate = float((attacker.damage_dealt > 0).mean())
    assert 0.40 < hit_rate < 0.50  # no reroll available: stays near the single-roll ~0.45
    pool = attacker.resources["luck_points"]
    assert bool((pool.current == 0.0).all())  # never goes negative


def test_reroll_take_best_never_spends_when_expected_value_is_zero() -> None:
    """Issue #70: a target fully immune to the attack's only damage type
    means no fresh roll can ever deal real damage —
    ``MultiGroupAttackMechanic.expected_value()`` is exactly 0 there, so the
    EV gate (matching ``_apply_trades``'s own ``value <= avg`` skip) must
    never spend a luck point chasing an attack that cannot possibly help."""
    size = 2_000
    attacker_spec = _lucky_attacker(pool_max=3)
    target_spec = _reroll_target(ac=15, immune=("piercing",))
    combatants = {
        attacker_spec.entity.id: _init_state(attacker_spec, "party", size),
        target_spec.entity.id: _init_state(target_spec, "enemy", size),
    }
    attacker = combatants[attacker_spec.entity.id]
    target = combatants[target_spec.entity.id]
    bus = EventBus()
    batch = UniverseBatch(size=size, seed=7)
    step = _attack("fixture-attack", 3, [DamageGroup(dice="1d6", type="piercing")])
    mask = np.ones(size, dtype=np.bool_)
    _resolve_attack_primitive(
        batch.rng,
        bus,
        attacker_spec.entity.id,
        attacker,
        target_spec.entity.id,
        target,
        mask,
        "normal",
        step,
        combatants,
    )
    pool = attacker.resources["luck_points"]
    assert bool((pool.current == 3.0).all())


def _pct_reducer(*, fraction: float, damage_types: tuple[str, ...] | None) -> CombatantSpec:
    """A defender whose only compiled ability is an Uncanny-Dodge-shaped
    ``damage_reduction_pct`` reaction — `delmar-fisk-sheet.md`'s own shape."""
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/fixture-dodger",
        name="Fixture Dodger",
        ac=10,
        hp=200,
        side="party",
        compiled_actions=(
            CompiledAbility(
                id="uncanny-dodge",
                name="Uncanny Dodge",
                step=ReactionPrimitive(
                    id="dnd5e_2014:primitive/reaction/fixture-dodger-0",
                    reaction_kind="damage_reduction_pct",
                    fraction=fraction,
                    damage_types=damage_types,
                    trigger="self_hit",
                ),
            ),
        ),
    )
    return make_combatant(
        entity_id="dnd5e_2014:combatant/fixture-dodger",
        name="Fixture Dodger",
        hp_max=200,
        armor_class=10,
        attack_bonus=0,
        damage_bonus=0,
        damage_dice_count=1,
        damage_dice_sides=4,
        compiled=statblock,
    )


@pytest.mark.parametrize(
    ("damage_types", "incoming", "expected"),
    [
        # No authored filter: fires on anything (Uncanny Dodge).
        (None, frozenset({"force"}), [13.0, 6.0]),
        # Authored filter matching the hit (Absorb Elements vs. fire).
        (("acid", "fire"), frozenset({"fire"}), [13.0, 6.0]),
        # Authored filter the hit does not match: never fires, damage stands.
        (("acid", "fire"), frozenset({"force"}), [27.0, 13.0]),
    ],
)
def test_damage_reduction_pct_halves_a_hit_and_honours_its_damage_type_filter(
    damage_types: tuple[str, ...] | None,
    incoming: frozenset[str],
    expected: list[float],
) -> None:
    """`damage_reduction_pct` (Uncanny Dodge, Absorb Elements) compiled but
    never executed before this: the reaction is real content on two PC
    sheets, so a hit against its owner must lose `fraction` of its damage,
    rounded down (PHB-2024 p.131), and only when the hit's own damage type
    passes the reaction's authored `damage_types` filter — the reference's
    `reactionAccepts` gate (`simulator.mjs:465`)."""
    size = 2
    dodger = _pct_reducer(fraction=0.5, damage_types=damage_types)
    state = _init_state(dodger, "party", size)
    combatants = {"dnd5e_2014:combatant/fixture-dodger": state}
    batch = UniverseBatch(size=size, seed=1)
    mask = np.ones(size, dtype=np.bool_)
    residual = _apply_damage_reduction_reaction(
        batch.rng,
        combatants,
        "dnd5e_2014:combatant/fixture-dodger",
        state,
        np.array([27.0, 13.0]),
        mask,
        incoming,
    )
    assert list(residual) == expected


def test_damage_reduction_pct_guards_only_its_own_owner() -> None:
    """ "A percentage reduction guards its owner only" (`simulator.mjs:468`)
    — an ally's Uncanny Dodge never intercepts a hit aimed at someone else,
    however the ally's own `trigger` reads."""
    size = 1
    victim = _victim()
    ally = _pct_reducer(fraction=0.5, damage_types=None)
    combatants = {
        "dnd5e_2014:combatant/fixture-victim": _init_state(victim, "party", size),
        "dnd5e_2014:combatant/fixture-dodger": _init_state(ally, "party", size),
    }
    batch = UniverseBatch(size=size, seed=1)
    residual = _apply_damage_reduction_reaction(
        batch.rng,
        combatants,
        "dnd5e_2014:combatant/fixture-victim",
        combatants["dnd5e_2014:combatant/fixture-victim"],
        np.array([27.0]),
        np.ones(size, dtype=np.bool_),
        frozenset({"force"}),
    )
    assert list(residual) == [27.0]


def test_rider_value_save_ends_duration_shortens_as_the_effect_lands_less_often() -> None:
    """A save-ends rider lasts until the target SUCCEEDS on its re-save, so
    its expected duration is `1 / P(succeed)` — `policy.mjs`'s
    `expectedDisabledRounds`. A rider that lands rarely (low `p_fail`) is
    therefore SHORTER-lived, never longer: scoring it as `1 / p_fail`
    inverted the relationship and made a save-or-suck against a strong-saving
    target the single most attractive play on the board."""
    target = _init_state(_victim(), "enemy", 1)
    rider = [EffectRider(effect="stunned", save_ends={"save": "wis", "dc": 16})]
    sticks_often = _rider_value(rider, target, 0.9)
    lands_rarely = _rider_value(rider, target, 0.2)
    no_save_ends = _rider_value([EffectRider(effect="stunned")], target, 0.2)

    assert sticks_often > lands_rarely
    assert lands_rarely == pytest.approx(no_save_ends * (1.0 / 0.8))
