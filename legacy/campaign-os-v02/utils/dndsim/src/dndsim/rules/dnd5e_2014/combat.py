"""Lockstep batched party-vs-party combat (issue #59, generalizing #39's
two-combatant walking skeleton into the real encounter loop every other
mechanism slice built for).

Turn order is per-universe rolled initiative (5e RAW, PHB p.189: one 1d20 +
Dex-modifier roll per combatant at encounter start, order fixed for the
whole encounter after) — see :func:`_roll_initiative_order`. A lockstep
batch still resolves one decision per dispatch across every universe at
once (ADR-0011); a distinct turn order per universe does *not* require a
distinct :class:`~dndsim.core.timeline.Timeline` per universe, because each
turn-slot's window firing is masked to the subset of universes occupying
that slot that round (:func:`_turn_mask_from_event`) rather than the
`Timeline` itself branching. This replaced an earlier fixed
party-then-enemy order, a documented Divergence now resolved (see
``DIVERGENCES.md``'s "Fixed turn order" entry).

The round itself is driven by
:func:`~dndsim.rules.dnd5e_2014.encounter_timeline.build_round_timeline` /
:func:`~dndsim.rules.dnd5e_2014.encounter_timeline.run_round` — every
combatant's ``start_of_turn``/``action``/``end_of_turn`` window, every other
legendary combatant's ``legendary_action`` window after each turn, and one
``lair_action`` window at the top of the round, all ordinary
:class:`~dndsim.core.events.EventBus` subscriptions registered once before
the round loop and read live off the encounter's own mutable state (never a
stale snapshot baked in at registration time) rather than re-registered
every round.

Each acting combatant's target is chosen by the selected
:class:`~dndsim.core.policy.Policy`: every living opposing combatant is
enumerated as a :class:`~dndsim.core.policy.Candidate` valued by
:class:`~dndsim.rules.dnd5e_2014.mechanics.AttackDamageMechanic`'s own
``expected_value()`` (ADR-0008), and repeated :meth:`Policy.choose` calls
(removing the winner each time) build one full preference ranking — the
same ranking for the whole batch, since a Mechanic's expected value is a
scalar. Which target in that ranking is actually legal (alive, in range)
diverges per universe once positioning and death enter the picture, so each
universe's actual pick is the first ranked target that is legal *there* —
the per-universe ``codes`` array
:func:`~dndsim.core.universe.bucket_by_choice` buckets, ADR-0011's
vectorized-choose-then-bucket shape realized against a real statblock
rather than the Phase 0 spike's toy fixture.
"""

from __future__ import annotations

import math
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Any

import numpy as np

from dndsim.core.events import Event, EventBus
from dndsim.core.policy import Candidate, Policy, policies
from dndsim.core.resources import ResourcePool
from dndsim.core.rng import BatchRNG
from dndsim.core.tags import BatchTags
from dndsim.core.universe import UniverseBatch, bucket_by_choice
from dndsim.rules.dnd5e_2014.advantage import (
    AdvantageMode,
    batch_attack_advantage_modes,
    batch_prevented_from_acting,
    collapse_advantage,
    d20_face_probabilities,
)
from dndsim.rules.dnd5e_2014.compile import CompiledAbility, CompiledStatblock
from dndsim.rules.dnd5e_2014.conditions import conditions
from dndsim.rules.dnd5e_2014.death_saves import (
    DownedState,
    apply_damage_while_down,
    enter_down,
    roll_death_saves,
    scatter_bool,
)
from dndsim.rules.dnd5e_2014.dice import DiceTerm, parse_dice_expr
from dndsim.rules.dnd5e_2014.effects import (
    EffectTracker,
    check_concentration_and_break,
    concentration_source,
)
from dndsim.rules.dnd5e_2014.encounter_timeline import (
    ACTION,
    END_OF_ROUND,
    END_OF_TURN,
    LAIR_ACTION,
    START_OF_TURN,
)
from dndsim.rules.dnd5e_2014.fixture import CombatantSpec
from dndsim.rules.dnd5e_2014.loadouts import LairAction
from dndsim.rules.dnd5e_2014.mechanics import (
    AttackDamageMechanic,
    ConcentrationSaveMechanic,
    MultiGroupAttackMechanic,
    mitigation_factor,
)
from dndsim.rules.dnd5e_2014.position import (
    PositionState,
    Side,
    aoe_capacity,
    aoe_targets,
    apply_move,
    hostile_adjacent_mask,
    kite_destination,
    leave_band_event,
    nearest_living_band,
    range_check,
)
from dndsim.rules.dnd5e_2014.primitives import (
    AttackPrimitive,
    AutodamagePrimitive,
    HealPrimitive,
    ReactionPrimitive,
    SavePrimitive,
)
from dndsim.rules.dnd5e_2014.reactions import make_reaction_pool, register_reaction
from dndsim.rules.dnd5e_2014.sim_extension import DamageDie, EffectRider, OnFailBlock
from dndsim.rules.dnd5e_2014.statblock import Defenses
from dndsim.rules.exhaustion import exhaustion_rules

#: Issue #55: the Rules pack whose Exhaustion resolution `run_combat` looks
#: up when its own caller passes no `exhaustion_rules_id` — 2024, matching
#: `dndsim`'s own edition default (`cli.py`'s `--edition`). A combatant with
#: `exhaustion_level` 0 (every statblock this engine currently compiles)
#: resolves identically regardless of which edition is active.
DEFAULT_EXHAUSTION_RULES_ID = "dnd5e_2024:rules/exhaustion"

_ADV_MODE_BY_CODE = {1: "advantage", -1: "disadvantage", 0: "normal"}

#: Published from :func:`_resolve_attack_primitive` (issue #60) whenever a
#: compiled attack lands, so a compiled defender-side reaction (an
#: ``extra_attack``-kind :class:`~dndsim.rules.dnd5e_2014.primitives.
#: ReactionPrimitive`, e.g. Pack Tactics Strike) can trigger off it.
#: ``_resolve_hits`` — the legacy flat-``CombatantSpec`` attack, unchanged by
#: this issue — never publishes this, so a legacy attacker's hit does not
#: yet trigger a compiled-side reaction (a narrow, documented gap: NOT_DONE).
ATTACK_HIT_EVENT = "attack_hit"

#: Weapon Mastery (issue #71). Slow is a bearer-side tag, boolean by RAW
#: design ("the Speed reduction doesn't exceed 10 feet" even from multiple
#: mastery hits — never an amount to accumulate). Vex is scoped per attacker
#: **and** target (:func:`_mastery_vex_tag`) — "advantage on their next
#: attack roll against THAT creature", never against anyone the attacker
#: next chooses to attack.
MASTERY_SLOW_TAG = "speed_reduced_10"


def _mastery_vex_tag(target_id: str) -> str:
    return f"mastery_vex_vs:{target_id}"


def _mastery_vex_source(attacker_id: str, target_id: str) -> str:
    return f"mastery_vex:{attacker_id}:{target_id}"


@dataclass(frozen=True, slots=True)
class PcOutcome:
    """One party member's own result — the report's "Per-PC" section."""

    id: str
    name: str
    hp_remaining_pct_p5: float
    hp_remaining_pct_p50: float
    hp_remaining_pct_p95: float
    down_probability: float


@dataclass(frozen=True, slots=True)
class CombatantOutput:
    """One combatant's own output — the report's "Per-combatant output" and
    "Positional figures" sections."""

    id: str
    name: str
    side: str
    mean_damage_dealt: float
    mean_reactions_spent: float
    mean_concentration_breaks: float
    mean_turns_no_target: float
    mean_opportunity_attacks: float


@dataclass(slots=True)
class CombatResult:
    """Batch-level outcome of :func:`run_combat`."""

    universes: int
    seed: int
    rounds_cap: int
    party_name: str
    enemy_name: str
    party_win_rate: float
    enemy_win_rate: float
    draw_rate: float
    mean_rounds: float
    median_rounds: float
    p95_rounds: float
    any_down_probability: float
    at_least_k_down: tuple[float, ...]
    tpk_probability: float
    mean_party_hp_loss: float
    pc_outcomes: tuple[PcOutcome, ...]
    combatant_outputs: tuple[CombatantOutput, ...]


@dataclass(slots=True)
class _CombatantState:
    """One combatant's mutable state across the batch — every mechanism
    slice's own container, bundled so a turn/reaction/legendary handler
    reaches all of them by combatant id alone."""

    spec: CombatantSpec
    side: str
    hp: ResourcePool
    down: DownedState
    pos: PositionState
    tags: BatchTags
    effects: EffectTracker
    reaction_pool: ResourcePool
    damage_dealt: np.ndarray
    ever_down: np.ndarray
    reactions_spent: np.ndarray
    concentrating: np.ndarray
    concentration_breaks: np.ndarray
    #: Temporary HP (issue #63 cause B: `temp_hp` ability primitives — Armor
    #: of Agathys) — drained before real HP by
    #: :func:`_apply_damage_with_temp_hp`, zero (a no-op) for a combatant
    #: with no such grant.
    temp_hp: np.ndarray
    #: Whether this combatant rolls every saving throw at advantage (issue
    #: #65: an `advantage`-kind ability primitive with `on: save` — Magic
    #: Resistance). Every `SavePrimitive`/attached-save this engine executes
    #: models a magical effect (this Rules pack's authored-content compiler
    #: has no other source for one — see `compile.py`), so this treats
    #: `{vs: 'magic'}` as matching every ability unconditionally, rather
    #: than tracking a
    #: per-save "is this magical" flag this engine has no other use for. A
    #: no-cost grant (Magic Resistance carries none) is set
    #: uniformly True/False across the whole batch before the fight starts,
    #: never mixed within one call's `mask`.
    save_advantage: np.ndarray
    #: One :class:`~dndsim.core.resources.ResourcePool` per
    #: ``spec.compiled.resources`` entry (issue #60) — empty for a
    #: combatant with no compiled statblock. Gates a compiled ability's own
    #: ``cost`` (a heal's bard slot, a reaction's named charge) the same way
    #: ``reaction_pool`` already gates an opportunity attack.
    resources: dict[str, ResourcePool]
    #: Issue #55: this combatant's own Exhaustion (`spec.exhaustion_level`)
    #: resolved once, at state-init time, through whichever Rules pack's
    #: `exhaustion_rules` entry is active for this run — never re-derived
    #: per roll. `exhaustion_d20_penalty` subtracts from an attack roll's
    #: to-hit and a saving throw's bonus alike (2024's flat "D20 Test"
    #: rule; 0 under 2014, which uses disadvantage instead — see
    #: `exhaustion_save_disadvantage`). `exhaustion_speed_ft` is this
    #: combatant's `speed_ft` after whichever edition's speed penalty
    #: applies, consumed in place of `spec.speed_ft` at the one place a
    #: turn reads it.
    exhaustion_d20_penalty: int
    exhaustion_save_disadvantage: bool
    exhaustion_speed_ft: int


def _init_state(
    spec: CombatantSpec,
    side: str,
    size: int,
    exhaustion_rules_id: str = DEFAULT_EXHAUSTION_RULES_ID,
) -> _CombatantState:
    tags = BatchTags(size)
    rules = exhaustion_rules.get(exhaustion_rules_id)
    level = spec.exhaustion_level
    resources = (
        {
            r.id: ResourcePool(r.id, np.full(size, float(r.max), dtype=np.float64))
            for r in spec.compiled.resources
        }
        if spec.compiled is not None
        else {}
    )
    return _CombatantState(
        spec=spec,
        side=side,
        hp=ResourcePool("hp", np.full(size, spec.hp_max, dtype=np.float64)),
        down=DownedState.empty(size),
        pos=PositionState.deploy(
            side,  # type: ignore[arg-type]
            "engaged",
            size,
            start_band=(
                spec.compiled.position.start_band
                if spec.compiled is not None and spec.compiled.position is not None
                else None
            ),
        ),
        tags=tags,
        effects=EffectTracker(tags=tags, size=size),
        reaction_pool=make_reaction_pool(size),
        damage_dealt=np.zeros(size, dtype=np.float64),
        ever_down=np.zeros(size, dtype=np.bool_),
        reactions_spent=np.zeros(size, dtype=np.float64),
        concentrating=np.full(size, spec.starts_concentrating, dtype=np.bool_),
        concentration_breaks=np.zeros(size, dtype=np.float64),
        resources=resources,
        temp_hp=np.zeros(size, dtype=np.float64),
        save_advantage=np.zeros(size, dtype=np.bool_),
        exhaustion_d20_penalty=rules.d20_penalty(level),
        exhaustion_save_disadvantage=rules.imposes_save_disadvantage(level),
        exhaustion_speed_ft=rules.effective_speed_ft(level, spec.speed_ft),
    )


def _side_dead_all(combatants: dict[str, _CombatantState], ids: Sequence[str]) -> np.ndarray:
    result: np.ndarray = np.logical_and.reduce([combatants[i].down.dead for i in ids])
    return result


def _roll_initiative_order(
    rng: BatchRNG, combatants: dict[str, _CombatantState], all_ids: Sequence[str], size: int
) -> np.ndarray:
    """Per-universe rolled initiative order (5e RAW, PHB p.189: one 1d20 +
    Dex-modifier roll each, at the start of the encounter, order fixed for
    every round after) — the turn-order Divergence this session's Otar
    Phase 1 diagnosis found and quantified (`DIVERGENCES.md`): the prior
    fixed party-then-enemy group order let the party alpha-strike low-HP
    enemies dead before they ever acted, which no single mechanic fix (the
    legendary-action economy, movement_boost, reroll_take_best) touches.

    Returns a ``(len(all_ids), size)`` int array: ``order[slot, universe]``
    is the row-index into `all_ids` of whoever acts in turn-slot `slot` for
    that universe. Vectorized across the whole batch in one
    ``np.argsort`` — no per-universe Python loop — by encoding roll, Dex
    tiebreak, and a final declared-order tiebreak as one combined integer
    sort key at three well-separated magnitude bands (rolls span 1-20,
    scaled by 10000; Dex modifiers realistically span roughly -5..+10,
    scaled by 100, safely under half of 10000; declared order spans
    0..len(all_ids)-1, safely under 100) so no legitimate combination of
    the three collides across bands. PHB p.189's own tiebreak rule:
    "a good rule is to use each combatant's Dexterity score, with higher
    Dexterity going first" — not proficiency-adjusted (``save_bonuses``
    would be the wrong source; see ``CompiledStatblock.abilities``'s own
    docstring). A combatant with no compiled statblock (the bundled
    synthetic fixture) has no ability scores to read; its Dex modifier
    defaults to 0 (a 10 Dex, the SRD baseline), never a crash.
    """

    def _dex_mod(cid: str) -> int:
        compiled = combatants[cid].spec.compiled
        if compiled is None:
            return 0
        return (compiled.abilities.get("dex", 10) - 10) // 2

    n = len(all_ids)
    rolls = rng.integers(1, 21, (n, size))
    dex_mods = np.array([_dex_mod(cid) for cid in all_ids]).reshape(n, 1)
    declared_order = np.arange(n).reshape(n, 1)
    combined = rolls * 10000 + dex_mods * 100 - declared_order
    order: np.ndarray = np.argsort(-combined, axis=0)
    return order


def _fight_ongoing(
    combatants: dict[str, _CombatantState], party_ids: Sequence[str], enemy_ids: Sequence[str]
) -> np.ndarray:
    party_dead = _side_dead_all(combatants, party_ids)
    enemy_dead = _side_dead_all(combatants, enemy_ids)
    result: np.ndarray = ~party_dead & ~enemy_dead
    return result


def _turn_mask_from_event(event: Event, size: int) -> np.ndarray:
    """The rolled-initiative turn-order mask an event's own `payload`
    carries under `"mask"` — the whole batch (every universe) when absent,
    matching this event's behavior before per-universe rolled initiative
    existed (a bare ``Event(name=...)`` with no payload at all, or a payload
    dict that never set `"mask"`, both read as "this fires for everyone")."""
    payload = event.payload
    if not payload:
        return np.ones(size, dtype=np.bool_)
    mask = payload.get("mask")
    return mask if mask is not None else np.ones(size, dtype=np.bool_)


def _combined_advantage(
    condition_mode: np.ndarray,
    position_disadvantage: np.ndarray,
    extra_advantage: np.ndarray | None = None,
) -> np.ndarray:
    """Collapse condition-sourced advantage/disadvantage
    (:func:`~dndsim.rules.dnd5e_2014.advantage.batch_attack_advantage_modes`)
    with position-sourced disadvantage (:func:`~dndsim.rules.dnd5e_2014.
    position.range_check`'s stacking count) via the same any-advantage-
    cancels-any-disadvantage rule as
    :func:`~dndsim.rules.dnd5e_2014.advantage.collapse_advantage`, vectorized.
    ``extra_advantage`` (issue #66: Pack Tactics' per-universe "an ally is
    adjacent to the target" mask) is one more advantage source, folded in
    by the same cancel-with-any-disadvantage rule as every other source —
    never bypassing it."""
    has_adv = condition_mode == 1
    if extra_advantage is not None:
        has_adv = has_adv | extra_advantage
    has_dis = (condition_mode == -1) | (position_disadvantage > 0)
    out = np.zeros(condition_mode.shape[0], dtype=np.int8)
    out[has_adv & ~has_dis] = 1
    out[has_dis & ~has_adv] = -1
    return out


def _apply_damage_with_temp_hp(
    target: _CombatantState, damage: np.ndarray, mask: np.ndarray
) -> np.ndarray:
    """Drain `target`'s temp-HP pool before real HP (issue #63 cause B:
    Armor of Agathys and any other `temp_hp` ability primitive), returning
    the residual `damage` (masked-size, matching `damage`'s own shape) that
    actually reaches real HP. A no-op — returns `damage` unchanged — for a
    combatant with no temp HP outstanding, so every existing fixture/test
    that never grants any keeps its exact prior numbers."""
    current = target.temp_hp[mask]
    if not bool((current > 0).any()):
        return damage
    absorbed = np.minimum(damage, current)
    target.temp_hp[mask] = current - absorbed
    result: np.ndarray = damage - absorbed
    return result


def _resolve_hits(
    rng: BatchRNG,
    attacker: _CombatantState,
    target_id: str,
    target: _CombatantState,
    mask: np.ndarray,
    advantage_mode: str,
) -> None:
    """Roll and apply one attacker-vs-``target`` attack for every universe
    in ``mask``, at one collapsed ``advantage_mode`` — the masked-slice
    primitive every attack in this module (an ordinary turn, an opportunity
    attack, a legendary bonus attack) resolves through, matching the
    two-combatant skeleton's own ``_attack`` shape generalized to any
    attacker/target pair. Damage is credited to ``attacker.damage_dealt`` —
    the "how much this combatant dealt" figure the report's Per-combatant
    section wants — never to ``target``, which only tracks what it received
    through ``hp``/``down``."""
    n = int(mask.sum())
    if n == 0:
        return
    spec = attacker.spec
    mechanic = AttackDamageMechanic(
        attack_bonus=spec.attack_bonus,
        target_ac=target.spec.armor_class,
        damage_dice_count=spec.damage_dice_count,
        damage_dice_sides=spec.damage_dice_sides,
        damage_bonus=spec.damage_bonus,
        advantage_mode=advantage_mode,  # type: ignore[arg-type]
    )
    damage = mechanic.resolve(rng, n)
    hit = scatter_bool(mask, damage > 0)
    damage_full = np.zeros(mask.shape[0], dtype=np.float64)
    damage_full[mask] = damage
    was_down = target.down.down.copy()

    residual = _apply_damage_with_temp_hp(target, damage, mask)
    target.hp.spend(residual, mask)
    apply_damage_while_down(target.down, hit & was_down)
    newly_down = hit & ~was_down & target.hp.depleted()
    enter_down(target.down, newly_down)
    target.ever_down |= newly_down
    attacker.damage_dealt += damage_full

    if bool(target.concentrating.any()):
        conc_mask = hit & target.concentrating
        if bool(conc_mask.any()):
            broke = check_concentration_and_break(
                tracker=target.effects,
                owner_id=target_id,
                damage=damage_full[conc_mask],
                concentrating_mask=conc_mask,
                con_bonus=target.spec.con_bonus,
                advantage_mode="normal",
                rng=rng,
            )
            target.concentration_breaks += broke.astype(np.float64)
            target.concentrating &= ~broke


# --- compiled-statblock action execution (issue #60) ------------------------
#
# Everything below reads a combatant's real kit — ``spec.compiled.
# compiled_actions``/``routine``/``ability_primitives`` — instead of the flat
# single-attack shape ``_resolve_hits`` above still serves. ``_resolve_hits``
# itself is left untouched (byte-identical RNG/output sequence) so every
# existing fixture/test/golden snapshot that never attaches a compiled
# statblock keeps its exact prior behavior; this section is purely additive.


def _expr_mean(expr: str) -> float:
    """The closed-form mean of one dice expression — no crit doubling, the
    plain expected value a save/autodamage/heal roll (never a to-hit roll)
    needs."""
    parsed = parse_dice_expr(expr)
    total = float(parsed.flat)
    for term in parsed.dice:
        total += term.sign * term.count * (term.sides + 1) / 2.0
    return total


def _target_defenses(target: _CombatantState) -> Defenses:
    """``target``'s declared resist/immune/vulnerable tags (issue #61) — an
    uncompiled combatant (no real kit, the legacy flat-``CombatantSpec``
    path) carries none, matching its prior full-value-damage behavior."""
    return target.spec.compiled.defenses if target.spec.compiled is not None else Defenses()


def _dice_group_mean(damage: Sequence[Any], defenses: Defenses) -> float:
    """Mean damage across a list of dice-bearing entries — any object
    exposing ``.dice``/``.type`` (:class:`~dndsim.rules.dnd5e_2014.attack_string.
    DamageGroup` or :class:`~dndsim.rules.dnd5e_2014.sim_extension.DamageDie`
    are the two real shapes this is called with), each entry's mean
    mitigated by its own type against ``defenses`` (ADR-0008: this is the
    scalar the planner values a save/autodamage ability by, so it must
    agree with :func:`_roll_damage_groups`'s own per-entry mitigation)."""
    return sum(
        mitigation_factor(defenses, getattr(entry, "type", None)) * _expr_mean(entry.dice)
        for entry in damage
    )


def _roll_damage_groups(
    rng: BatchRNG, damage: Sequence[Any], size: int, defenses: Defenses
) -> np.ndarray:
    """Sum every dice-bearing entry's roll for ``size`` universes — no
    attack roll, no crit: the plain damage draw a save's ``on_fail`` block
    or an :class:`~dndsim.rules.dnd5e_2014.primitives.AutodamagePrimitive`'s
    own ``damage`` list resolves through. Each entry's own type is
    mitigated against ``defenses`` (issue #61) before it is added to the
    total, matching ``engine.mjs``'s ``applyDamage``."""
    total = np.zeros(size, dtype=np.float64)
    for entry in damage:
        parsed = parse_dice_expr(entry.dice)
        factor = mitigation_factor(defenses, getattr(entry, "type", None))
        group_total = np.full(size, float(parsed.flat), dtype=np.float64)
        for term in parsed.dice:
            rolls = rng.integers(1, term.sides + 1, size=(term.count, size)).sum(axis=0)
            group_total += term.sign * rolls
        total += group_total * factor
    return total


def _roll_expr(rng: BatchRNG, expr: str, size: int) -> np.ndarray:
    """:func:`_roll_damage_groups` for a single bare dice expression (a
    :class:`~dndsim.rules.dnd5e_2014.primitives.HealPrimitive`'s own
    ``dice`` field, which carries no wrapping damage-group object)."""
    parsed = parse_dice_expr(expr)
    total = np.full(size, float(parsed.flat), dtype=np.float64)
    for term in parsed.dice:
        rolls = rng.integers(1, term.sides + 1, size=(term.count, size)).sum(axis=0)
        total += term.sign * rolls
    return total


def _save_pass_probability(
    save_bonus: int, dc: int, advantage_mode: AdvantageMode = "normal"
) -> float:
    """Closed-form P(save succeeds) for a d20 + ``save_bonus`` against
    ``dc`` at ``advantage_mode`` (issue #65: a Magic-Resistant target's
    ``save_advantage`` — see :func:`_save_advantage_mode`) — the scalar
    valuation half of a save-driven ability; actual resolution rolls via
    :class:`~dndsim.rules.dnd5e_2014.mechanics.ConcentrationSaveMechanic`,
    reused generically (it is already parameterized on a plain bonus and a
    dc, nothing concentration-specific) rather than duplicated under a new
    name."""
    probs = d20_face_probabilities(advantage_mode)
    return sum(p for roll, p in zip(range(1, 21), probs, strict=True) if roll + save_bonus >= dc)


def _target_save_advantage_mode(target: _CombatantState) -> AdvantageMode:
    """Scalar (whole-batch) counterpart of :func:`_save_advantage_mode` for
    the EV valuation path — ``target.save_advantage`` is uniform across the
    batch (see the field's own docstring), so ``.any()`` over the whole
    array reads the same as the masked check."""
    return "advantage" if bool(target.save_advantage.any()) else "normal"


def _apply_damage_to_target(
    attacker: _CombatantState, target: _CombatantState, damage: np.ndarray, mask: np.ndarray
) -> None:
    """Shared HP/down/ever_down bookkeeping for a damage instance landing
    outside the ordinary to-hit attack roll (a save's on_fail damage, an
    autodamage Primitive) — the same tail ``_resolve_hits`` applies for an
    ordinary attack, factored out here for issue #60's new damage sources
    rather than duplicated a third time. ``_resolve_hits`` itself keeps its
    own inline copy unchanged (see this section's own docstring)."""
    damage_full = np.zeros(mask.shape[0], dtype=np.float64)
    damage_full[mask] = damage
    hit = scatter_bool(mask, damage > 0)
    was_down = target.down.down.copy()
    residual = _apply_damage_with_temp_hp(target, damage, mask)
    target.hp.spend(residual, mask)
    apply_damage_while_down(target.down, hit & was_down)
    newly_down = hit & ~was_down & target.hp.depleted()
    enter_down(target.down, newly_down)
    target.ever_down |= newly_down
    attacker.damage_dealt += damage_full


def _apply_damage_reduction_reaction(
    rng: BatchRNG,
    combatants: dict[str, _CombatantState],
    target_id: str,
    target: _CombatantState,
    damage: np.ndarray,
    mask: np.ndarray,
    incoming_types: frozenset[str] = frozenset(),
) -> np.ndarray:
    """Pre-commit interception of one attack's rolled damage by a
    ``damage_reduction`` reaction declared by ``target`` or an ally on its
    own side (Cutting Words) — issue #63 cause C. Mirrors ``simulator.mjs``'s
    ``executeAttack``: the reduction is rolled and subtracted from `damage`
    (masked-size, matching `damage`'s own shape) BEFORE
    :func:`_apply_damage_to_target` ever touches HP, never as a post-hoc
    event. The first eligible reactor in side-declared order (`target`
    itself first, then its allies) wins each hit — a simplification of the
    reference's EV-optimal choice among competing reactions, safe while real
    content declares exactly one ``damage_reduction`` reactor (Perrin's
    Cutting Words).

    ``damage_reduction_pct`` (Uncanny Dodge, Absorb Elements) resolves here
    too: its authored ``fraction`` scales the surviving damage and RAW rounds
    the result down (PHB-2024 p.131, "halve the attack's damage against
    him (round down)"), against the same eligibility gates — one reaction per
    round from the reactor's own pool, plus any named ``cost``.

    ``incoming_types`` is the triggering attack's own declared damage types.
    A reaction that authored a ``damage_types`` filter (Absorb Elements'
    acid/cold/fire/lightning/thunder) only fires when the hit carries one of
    them — the reference's ``reactionAccepts`` gate (``simulator.mjs:465``).
    The default empty set matches no filtered reaction, so a caller that
    cannot name the incoming types never fires one by accident."""
    # `damage`/`residual` are masked-size (shape mask.sum()); every other
    # array here (reactor.down.dead, reaction pools, ...) is full-size — the
    # same masked/full split every other resolver in this module keeps.
    hit_idx = np.flatnonzero(mask)  # damage[i] corresponds to universe hit_idx[i]
    hit_remaining = np.zeros(mask.shape[0], dtype=np.bool_)
    hit_remaining[hit_idx] = damage > 0
    if not bool(hit_remaining.any()):
        return damage
    residual = damage.copy()
    side_ids = [target_id] + [
        cid for cid, state in combatants.items() if state.side == target.side and cid != target_id
    ]
    for reactor_id in side_ids:
        if not bool(hit_remaining.any()):
            break
        reactor = combatants[reactor_id]
        if reactor.spec.compiled is None:
            continue
        for ability in reactor.spec.compiled.compiled_actions:
            step = ability.step
            if not isinstance(step, ReactionPrimitive) or step.reaction_kind not in (
                "damage_reduction",
                "damage_reduction_pct",
            ):
                continue
            if step.reaction_kind == "damage_reduction_pct" and (
                step.fraction is None
                # "a percentage reduction guards its owner only"
                # (`simulator.mjs:468`).
                or reactor_id != target_id
            ):
                continue
            if step.damage_types is not None and incoming_types.isdisjoint(step.damage_types):
                continue
            if step.trigger not in (None, "self_hit", "self_or_ally_hit"):
                continue
            if reactor_id != target_id and step.trigger != "self_or_ally_hit":
                continue
            size = mask.shape[0]
            incapacitated = batch_prevented_from_acting(reactor.tags, size) | reactor.down.down
            eligible = (
                hit_remaining
                & ~reactor.down.dead
                & ~incapacitated
                & ~reactor.reaction_pool.depleted()
            )
            if step.cost is not None:
                pool = reactor.resources.get(step.cost.resource)
                if pool is not None:
                    eligible = eligible & (pool.current >= step.cost.spend)
            if not bool(eligible.any()):
                continue
            n_elig = int(eligible.sum())
            elig_local = eligible[hit_idx]  # damage/residual's masked-size indexing
            if step.fraction is not None:  # a damage_reduction_pct step
                reduced = np.floor(residual[elig_local] * (1.0 - step.fraction))
            else:
                reduced = np.maximum(
                    0.0, residual[elig_local] - _roll_expr(rng, step.die or "1d6", n_elig)
                )
            reactor.reaction_pool.spend(np.ones(n_elig), eligible)
            if step.cost is not None:
                pool = reactor.resources.get(step.cost.resource)
                if pool is not None:
                    pool.spend(np.full(n_elig, float(step.cost.spend)), eligible)
            reactor.reactions_spent += eligible.astype(np.float64)
            residual[elig_local] = reduced
            hit_remaining = hit_remaining & ~eligible
    return residual


# --- reroll_take_best (issue #70: Lucky feat) --------------------------------


def _reroll_take_best_step(attacker: _CombatantState) -> Any | None:
    """`attacker`'s own compiled ``reroll_take_best`` ability primitive, if
    any (at most one is ever authored; the first wins). Duck-typed
    (``getattr``) like every other mechanically-generated ability Primitive
    this module reads — :func:`~dndsim.rules.dnd5e_2014.primitives.
    _primitive_for` builds no static class combat.py can import."""
    compiled = attacker.spec.compiled
    if compiled is None:
        return None
    for step in compiled.ability_primitives:
        if getattr(step, "kind", None) == "reroll_take_best":
            return step
    return None


def _apply_reroll_take_best(
    rng: BatchRNG,
    attacker: _CombatantState,
    mechanic: MultiGroupAttackMechanic,
    damage: np.ndarray,
    mask: np.ndarray,
) -> np.ndarray:
    """Issue #70: `attacker`'s ``reroll_take_best`` ability (Lucky feat)
    spends one point from its own named ``pool`` to reroll a missed attack
    and take the better of the two — never fires on an already-successful
    attack (a fresh roll cannot beat a hit already in hand, so spending here
    would only waste the charge) and only when this attack's own closed-form
    :meth:`~dndsim.rules.dnd5e_2014.mechanics.MultiGroupAttackMechanic.
    expected_value` is positive — the same scalar EV-gate
    :func:`_apply_trades` already uses for `trade_dice_for_rider` (issue #67
    follow-up), so a point is never spent chasing a target this attack
    cannot damage at all (e.g. full immunity to every declared damage
    type). ``damage`` is masked-size (shape ``mask.sum()``); every other
    array here (`pool.current`, ...) is full-size — the same masked/full
    split :func:`_apply_damage_reduction_reaction` already keeps."""
    step = _reroll_take_best_step(attacker)
    if step is None:
        return damage
    pool_name = getattr(step, "pool", None)
    if not isinstance(pool_name, str):
        return damage
    pool = attacker.resources.get(pool_name)
    if pool is None:
        return damage
    if mechanic.expected_value() <= 0.0:
        return damage
    hit_idx = np.flatnonzero(mask)
    missed = np.zeros(mask.shape[0], dtype=np.bool_)
    missed[hit_idx] = damage <= 0.0
    eligible = missed & (pool.current >= 1.0)
    if not bool(eligible.any()):
        return damage
    n_elig = int(eligible.sum())
    pool.spend(np.full(n_elig, 1.0, dtype=np.float64), eligible)
    reroll_damage = mechanic.resolve(rng, n_elig)
    elig_local = eligible[hit_idx]
    damage = damage.copy()
    damage[elig_local] = np.maximum(damage[elig_local], reroll_damage)
    return damage


def _resolve_attack_primitive(
    rng: BatchRNG,
    bus: EventBus,
    attacker_id: str,
    attacker: _CombatantState,
    target_id: str,
    target: _CombatantState,
    mask: np.ndarray,
    advantage_mode: str,
    step: AttackPrimitive,
    combatants: dict[str, _CombatantState],
) -> None:
    """The compiled-kit analogue of ``_resolve_hits``: rolls the attacker's
    real :class:`~dndsim.rules.dnd5e_2014.primitives.AttackPrimitive` (every
    declared damage group, via :class:`~dndsim.rules.dnd5e_2014.mechanics.
    MultiGroupAttackMechanic`) rather than the flat single-die
    ``CombatantSpec`` shape. Publishes :data:`ATTACK_HIT_EVENT` on a hit so a
    compiled defender-side reaction can trigger off it. A compiled
    ``reroll_take_best`` on `attacker` (issue #70: Lucky feat) gets first
    look at a miss, via :func:`_apply_reroll_take_best`, before hit/event
    publication — every one of this function's three call sites (a
    freeform action, a Multiattack routine step, an extra-attack reaction)
    picks it up uniformly."""
    n = int(mask.sum())
    if n == 0:
        return
    mechanic = MultiGroupAttackMechanic(
        attack_bonus=step.to_hit - attacker.exhaustion_d20_penalty,
        target_ac=target.spec.armor_class,
        damage=tuple(step.damage),
        advantage_mode=advantage_mode,  # type: ignore[arg-type]
        target_defenses=_target_defenses(target),
    )
    damage = mechanic.resolve(rng, n)
    damage = _apply_reroll_take_best(rng, attacker, mechanic, damage, mask)
    hit = scatter_bool(mask, damage > 0)
    damage = _apply_damage_reduction_reaction(
        rng,
        combatants,
        target_id,
        target,
        damage,
        mask,
        frozenset(group.type.lower() for group in step.damage if group.type),
    )
    _apply_damage_to_target(attacker, target, damage, mask)

    if bool(target.concentrating.any()):
        conc_mask = hit & target.concentrating
        if bool(conc_mask.any()):
            damage_full = np.zeros(mask.shape[0], dtype=np.float64)
            damage_full[mask] = damage
            broke = check_concentration_and_break(
                tracker=target.effects,
                owner_id=target_id,
                damage=damage_full[conc_mask],
                concentrating_mask=conc_mask,
                con_bonus=target.spec.con_bonus,
                advantage_mode="normal",
                rng=rng,
            )
            target.concentration_breaks += broke.astype(np.float64)
            target.concentrating &= ~broke

    if bool(hit.any()):
        # issue #71: Weapon Mastery — both properties gate on "hits ... and
        # deals damage to it" (SRD-2024), exactly `hit`'s own condition
        # (damage > 0 after the mechanic's own mitigation), never the bare
        # attack-roll outcome.
        if step.mastery == "vex":
            attacker.effects.apply(
                source=_mastery_vex_source(attacker_id, target_id),
                tag=_mastery_vex_tag(target_id),
                mask=hit,
                duration_rounds=1,
            )
        elif step.mastery == "slow":
            target.effects.apply(
                source=f"mastery_slow:{attacker_id}:{target_id}",
                tag=MASTERY_SLOW_TAG,
                mask=hit,
                duration_rounds=0,
            )
        bus.publish(
            Event(
                name=ATTACK_HIT_EVENT,
                payload={"attacker_id": attacker_id, "target_id": target_id, "mask": hit},
            )
        )


def _save_advantage_mode(target: _CombatantState, mask: np.ndarray) -> AdvantageMode:
    """(issue #65) The roll mode for a save `target` is about to make:
    Magic Resistance's ``target.save_advantage`` (set uniformly, never
    mixed within one call's `mask` — see the field's own docstring)
    combined with this edition's own Exhaustion disadvantage (issue #55;
    2014's tiered table imposes it from level 3 — see
    `_CombatantState.exhaustion_save_disadvantage` — 2024 never does,
    using a flat `exhaustion_d20_penalty` on the bonus instead, applied at
    each `_save_bonus` call site)."""
    modes: list[AdvantageMode] = []
    if bool(target.save_advantage[mask].any()):
        modes.append("advantage")
    if target.exhaustion_save_disadvantage:
        modes.append("disadvantage")
    return collapse_advantage(modes)


def _save_bonus(target: _CombatantState, ability: str) -> int:
    """A target's save bonus for `ability`, after their own Exhaustion's
    flat D20 Test penalty (issue #55; 0 under an edition that uses
    disadvantage instead — see `_save_advantage_mode`)."""
    base = target.spec.compiled.save_bonuses.get(ability, 0) if target.spec.compiled else 0
    return base - target.exhaustion_d20_penalty


def _resolve_save_primitive(
    rng: BatchRNG,
    actor: _CombatantState,
    target_id: str,
    target: _CombatantState,
    mask: np.ndarray,
    step: SavePrimitive,
) -> None:
    n = int(mask.sum())
    if n == 0:
        return
    saved = ConcentrationSaveMechanic(
        con_bonus=_save_bonus(target, step.save),
        dc=int(step.dc),
        advantage_mode=_save_advantage_mode(target, mask),
    ).resolve(rng, n)
    failed = saved <= 0.0
    dmg = _roll_damage_groups(rng, step.on_fail.damage, n, _target_defenses(target))
    applied = np.where(failed, dmg, dmg * 0.5 if step.half_on_save else 0.0)
    _apply_damage_to_target(actor, target, applied, mask)
    for rider in step.on_fail.effects:
        effect_mask = scatter_bool(mask, failed)
        target.effects.apply(
            source=f"save:{target_id}",
            tag=rider.effect.lower(),
            mask=effect_mask,
            save_ends=_rider_save_ends(rider),
        )


def _resolve_save_primitive_area(
    rng: BatchRNG,
    actor: _CombatantState,
    opposing_ids: Sequence[str],
    combatants: dict[str, _CombatantState],
    mask: np.ndarray,
    step: SavePrimitive,
) -> None:
    """Resolve a `SavePrimitive` whose `step.targets.area` is true (issue:
    AoE save actions never fire) against every opponent the shape actually
    catches, per universe — using the already-vectorized
    `position.aoe_targets`/`aoe_capacity` (built for issue #47 but never
    wired to a SavePrimitive before this). Each caught id gets its own
    `_resolve_save_primitive` call with a sub-mask of `mask`, so a universe
    where a given opponent was NOT caught this cast (out of band, already
    dead, or capacity-excluded) never rolls a save for it."""
    size = mask.shape[0]
    if not bool(mask.any()) or not opposing_ids:
        return
    capacity = aoe_capacity(radius_ft=step.targets.radius, cone_ft=step.targets.cone)
    positions = {oid: combatants[oid].pos.pos for oid in opposing_ids}
    alive = {oid: ~combatants[oid].down.dead for oid in opposing_ids}
    caught = aoe_targets(
        positions=positions,
        alive=alive,
        capacity=capacity,
        size=size,
        radius_ft=step.targets.radius or 0,
    )
    for oid, caught_mask in caught.items():
        sub_mask = mask & caught_mask
        if not bool(sub_mask.any()):
            continue
        _resolve_save_primitive(rng, actor, oid, combatants[oid], sub_mask, step)


def _resolve_autodamage_primitive(
    rng: BatchRNG,
    actor: _CombatantState,
    target_id: str,
    target: _CombatantState,
    mask: np.ndarray,
    step: AutodamagePrimitive,
) -> None:
    n = int(mask.sum())
    if n == 0:
        return
    dmg = _roll_damage_groups(rng, step.damage, n, _target_defenses(target))
    if step.attached_save is not None:
        saved = ConcentrationSaveMechanic(
            con_bonus=_save_bonus(target, step.attached_save.ability),
            dc=int(step.attached_save.dc),
            advantage_mode=_save_advantage_mode(target, mask),
        ).resolve(rng, n)
        dmg = np.where(saved > 0.0, 0.0, dmg)
    _apply_damage_to_target(actor, target, dmg, mask)


def _resolve_heal_primitive(
    rng: BatchRNG,
    mask: np.ndarray,
    step: HealPrimitive,
    allies: Sequence[str],
    combatants: dict[str, _CombatantState],
) -> None:
    """Heals the side's own lowest-HP-fraction living ally, chosen
    per-universe (a dead ally's fraction is pinned to +inf so it is never
    picked)."""
    n = int(mask.sum())
    if n == 0 or not allies:
        return
    heal_amount = _roll_expr(rng, step.dice, n)
    frac_stack = np.stack(
        [
            np.where(
                ~combatants[aid].down.dead,
                combatants[aid].hp.current / combatants[aid].hp.max_value,
                np.inf,
            )
            for aid in allies
        ]
    )
    target_idx = np.argmin(frac_stack, axis=0)
    for i, aid in enumerate(allies):
        ally = combatants[aid]
        ally_mask = mask & (target_idx == i) & ~ally.down.dead
        if not bool(ally_mask.any()):
            continue
        local = ally_mask[mask]
        ally.hp.restore(heal_amount[local], ally_mask)


def _ability_cost(step: object) -> Any | None:
    return getattr(step, "cost", None)


def _step_affordable(actor: _CombatantState, step: object, size: int) -> np.ndarray:
    """Per-universe affordability of `step`'s own resource cost — takes the
    bare Primitive rather than a wrapping :class:`CompiledAbility` so it
    also serves an `ability_primitives` entry (issue #63 cause B), which
    carries no such wrapper."""
    cost = _ability_cost(step)
    if cost is None:
        return np.ones(size, dtype=np.bool_)
    pool = actor.resources.get(cost.resource)
    if pool is None:
        return np.ones(size, dtype=np.bool_)
    result: np.ndarray = pool.current >= cost.spend
    return result


def _spend_step_cost(actor: _CombatantState, step: object, mask: np.ndarray) -> None:
    cost = _ability_cost(step)
    if cost is None:
        return
    pool = actor.resources.get(cost.resource)
    if pool is None:
        return
    n = int(mask.sum())
    if n == 0:
        return
    pool.spend(np.full(n, float(cost.spend), dtype=np.float64), mask)


def _ability_affordable(actor: _CombatantState, ability: CompiledAbility, size: int) -> np.ndarray:
    return _step_affordable(actor, ability.step, size)


def _spend_ability_cost(actor: _CombatantState, ability: CompiledAbility, mask: np.ndarray) -> None:
    _spend_step_cost(actor, ability.step, mask)


def _movement_boost_grant(
    actor: _CombatantState, size: int, wanted: str, eligible: np.ndarray
) -> np.ndarray:
    """Per-universe grant of a Cunning-Action-style ``movement_boost``
    covering ``wanted`` (``"dash"``/``"disengage"``), restricted to
    ``eligible`` universes and spending each used step's own cost (if any)
    only there — the vectorized form of the reference's ``useMovementBoost``
    (``simulator.mjs:1193-1204``): the first authored ``movement_boost``
    step whose ``grants`` covers ``wanted`` and that the actor can afford is
    used, tried in authored order, so one universe is never charged for more
    than one step even when several qualify."""
    granted = np.zeros(size, dtype=np.bool_)
    if actor.spec.compiled is None:
        return granted
    remaining = eligible.copy()
    for step in actor.spec.compiled.ability_primitives:
        if not bool(remaining.any()):
            break
        if getattr(step, "kind", None) != "movement_boost":
            continue
        grants = getattr(step, "grants", None)
        if grants != wanted and grants != "both":
            continue
        affordable = _step_affordable(actor, step, size) & remaining
        if not bool(affordable.any()):
            continue
        _spend_step_cost(actor, step, affordable)
        granted = granted | affordable
        remaining = remaining & ~affordable
    return granted


#: Fraction of a round's output a condition rider denies (issue #63
#: interlock: ``_ability_ev`` must value a save-or-suck by more than its raw
#: damage) — port of ``policy.mjs``'s ``CONDITION_DENIAL``: full denial for
#: the incapacitating set, ``restrained`` trades about half a round (attacks
#: at disadvantage, attacks against it at advantage). Anything else (a
#: rider tag with no condition-registry entry at all, or one that does not
#: `prevents_acting`) falls through to the same 0.25 partial-tax default the
#: reference uses for frightened/poisoned/riders.
_RESTRAINED_DENIAL = 0.5
_DEFAULT_RIDER_DENIAL = 0.25


def _condition_denial(tag: str) -> float:
    tag = tag.lower()
    if tag == "restrained":
        return _RESTRAINED_DENIAL
    definition = conditions.get(tag) if tag in conditions else None
    if definition is not None and definition.prevents_acting:
        return 1.0
    return _DEFAULT_RIDER_DENIAL


def _threat_score(combatant: _CombatantState) -> float:
    """Per-round expected damage `combatant`'s own kit deals against a
    reference AC 15 — port of ``policy.mjs``'s ``threatScore``, the scalar
    :func:`_rider_value` weights condition denial by (how much output landing
    a save-or-suck on this combatant actually denies)."""
    compiled = combatant.spec.compiled
    if compiled is not None and compiled.routine:
        action_by_id = {a.id: a for a in compiled.compiled_actions}
        total = 0.0
        for step in compiled.routine:
            attack_candidates: list[AttackPrimitive] = [
                action_by_id[rid].step  # type: ignore[misc]
                for rid in (step.ref, *step.alternatives)
                if rid in action_by_id and isinstance(action_by_id[rid].step, AttackPrimitive)
            ]
            if not attack_candidates:
                continue
            best_ev = max(
                MultiGroupAttackMechanic(
                    attack_bonus=c.to_hit, target_ac=15, damage=tuple(c.damage)
                ).expected_value()
                for c in attack_candidates
            )
            total += step.count * best_ev
        return total
    return AttackDamageMechanic(
        attack_bonus=combatant.spec.attack_bonus,
        target_ac=15,
        damage_dice_count=combatant.spec.damage_dice_count,
        damage_dice_sides=combatant.spec.damage_dice_sides,
        damage_bonus=combatant.spec.damage_bonus,
    ).expected_value()


def _rider_save_ends(rider: EffectRider) -> tuple[str, int] | None:
    """(ability, dc) for a rider's own re-save clause, or ``None`` for one
    that never re-saves (issue #63's save_ends interlock). ``save_ends``
    rides through as a pydantic ``extra=\"allow\"`` key
    (:class:`~dndsim.rules.dnd5e_2014.sim_extension.EffectRider`), never a
    declared field."""
    raw = getattr(rider, "save_ends", None)
    if not isinstance(raw, dict):
        return None
    ability = raw.get("save") or raw.get("ability")
    dc = raw.get("dc")
    if ability is None or dc is None:
        return None
    try:
        return (str(ability).lower()[:3], int(dc))
    except TypeError, ValueError:
        return None


def _rider_value(
    effects: Sequence[EffectRider],
    target: _CombatantState,
    p_fail: float,
    *,
    is_on_success_branch: bool = False,
) -> float:
    """Damage-equivalent value of a save-or-suck's condition riders landing
    on `target` (issue #63 interlock 1) — port of ``policy.mjs``'s
    ``riderValue``. Multiplied by `p_fail` at the call site (the rider only
    lands when the save is failed), exactly like the damage term it sits
    beside in :func:`_ability_ev`.

    `is_on_success_branch` (issue #68 decision): True for the branch scored
    after the landing save already succeeded — :func:`_apply_trades`'s own
    ``on_success`` rider. A rider's `save_ends` clause never compounds
    duration there; `rounds` stays 1.0, identical to a rider with no
    `save_ends` at all. Succeeding the landing save is definitionally the
    weaker branch — scoring its own save_ends rider at the same 3-round cap
    a FAILED save earns would value succeeding the save the same as the
    worst on_fail outcome. Real content's own on_success riders (Stunning
    Strike's speed_halved/grants_advantage_next_attack,
    `crissdalynn-khinriss-sheet.md`) use a fixed single-round duration, never
    a save_ends clause — this guards a shape the schema allows generically
    but no authored content exercises yet."""
    threat = _threat_score(target)
    total = 0.0
    for rider in effects:
        denial = _condition_denial(rider.effect)
        rounds = 1.0
        if not is_on_success_branch and _rider_save_ends(rider) is not None:
            # Geometric expectation of rounds until the target SUCCEEDS on
            # its re-save and the condition ends — `1 / P(succeed)`, capped,
            # exactly as `policy.mjs`'s `expectedDisabledRounds` computes it.
            # `p_fail` is P(fail), so the denominator is its complement: a
            # save-or-suck that lands rarely does not thereby last longer.
            rounds = min(3.0, 1.0 / max(1e-9, 1.0 - p_fail))
        total += denial * threat * rounds
    return total


# --- trade_dice_for_rider (issue #67 follow-up: Cunning Strike) -------------
#
# A conditional choice made at the moment its linked `extra_damage` source
# (matched by `from_`) actually lands a hit — not a standing grant like
# temp_hp/extra_damage/retaliate/advantage(on=save) above — so it has no
# branch of its own in :func:`_activate_ability_primitives`; it is wired
# alongside its matched `extra_damage` step's own reaction, below.


def _dice_cost_stats(dice_cost: int | str, source_dice_expr: str) -> tuple[int, float]:
    """(byCount, avg) surrendered by one trade — port of ``dice.mjs``'s
    ``parseDice(tr.dice_cost).dice[0]?.count`` / ``diceMoments(tr.dice_cost).avg``,
    both derived from the SAME parsed ``dice_cost`` expression when it is a
    dice-expression string (real content: `delmar-fisk-sheet.md`'s ``"1d6"``).
    A bare-int ``dice_cost`` (:class:`~dndsim.rules.dnd5e_2014.sim_extension.
    TradeDiceForRiderModifier`'s declared alternative, ``dice_cost: int | str``)
    carries no die size of its own, so it reads as that many dice of
    `source_dice_expr`'s own leading size — the only size available, and the
    only reading under which "N dice surrendered" has a coherent average."""
    if isinstance(dice_cost, str):
        parsed = parse_dice_expr(dice_cost)
        by_count = parsed.dice[0].count if parsed.dice else 0
        return by_count, _expr_mean(dice_cost)
    by_count = int(dice_cost)
    source_parsed = parse_dice_expr(source_dice_expr)
    sides = source_parsed.dice[0].sides if source_parsed.dice else 0
    return by_count, by_count * (sides + 1) / 2.0


def _leading_dice_count(expr: str) -> int:
    """Dice left in `expr`'s own leading NdM term, or 0 once none remain —
    issue #68's over-spend guard: how much of a shared `from_` pool a later
    `trade_dice_for_rider` entry actually has left to spend, after an
    earlier trade in the same call has already shrunk it."""
    parsed = parse_dice_expr(expr)
    return parsed.dice[0].count if parsed.dice else 0


def _shrink_leading_dice(expr: str, by_count: int) -> str:
    """Port of ``dice.mjs``'s ``shrinkLeadingDice``: rebuilds `expr` with its
    leading NdM term's count reduced by `by_count` (the term drops entirely
    at zero or fewer dice; flat modifiers are untouched, later terms keep
    their own sign). ``"3d6" -> "2d6"``; ``"1d6+2" -> "2"``.

    A KEPT leading term keeps its own sign too (issue #68) — `dice.py`'s
    grammar (`_TERM_RE`'s `([+-])?`) allows a leading ``"-1d4+3d6"``, so the
    rebuild must not assume index 0 is always positive."""
    parsed = parse_dice_expr(expr)
    if not parsed.dice or by_count <= 0:
        return expr
    first = parsed.dice[0]
    new_count = first.count - by_count
    kept: list[DiceTerm] = []
    if new_count > 0:
        kept.append(DiceTerm(count=new_count, sides=first.sides, sign=first.sign))
    kept.extend(parsed.dice[1:])
    terms = [f"{'-' if d.sign < 0 else ''}{d.count}d{d.sides}" for d in kept]
    out = "+".join(terms).replace("+-", "-")
    if out == "":
        return str(parsed.flat)
    if parsed.flat > 0:
        out += f"+{parsed.flat}"
    elif parsed.flat < 0:
        out += str(parsed.flat)
    return out


def _apply_trade_rider(
    rng: BatchRNG,
    *,
    trade_ref: str,
    target_id: str,
    target: _CombatantState,
    save: Any,
    on_fail: OnFailBlock | None,
    on_success: OnFailBlock | None,
    mask: np.ndarray,
) -> None:
    """Resolves one accepted trade's save + condition riders — mirrors
    ``simulator.mjs``'s ``resolveChosenRider`` for its ``pendingTradeRiders``
    branch specifically: effects only, never `on_fail`/`on_success` DAMAGE
    (the reference's own ``resolveChosenRider`` never rolls that list for a
    traded or post-hit rider either, only for a SavePrimitive action's own
    `on_fail`). Legendary-resistance override is NOT applied — matches
    :func:`_activate_ability_primitives`'s own NOT_DONE note that
    `legendary_resistance_like` compiles but nothing consumes it yet."""
    n = int(mask.sum())
    if n == 0:
        return
    saved = ConcentrationSaveMechanic(
        con_bonus=_save_bonus(target, save.ability),
        dc=int(save.dc),
        advantage_mode=_save_advantage_mode(target, mask),
    ).resolve(rng, n)
    failed_full = scatter_bool(mask, saved <= 0.0)
    alive = ~(target.down.down | target.down.dead)
    for rider in on_fail.effects if on_fail is not None else []:
        effect_mask = mask & failed_full & alive
        if not bool(effect_mask.any()):
            continue
        target.effects.apply(
            source=f"trade:{trade_ref}:{target_id}",
            tag=rider.effect.lower(),
            mask=effect_mask,
            save_ends=_rider_save_ends(rider),
        )
    for rider in on_success.effects if on_success is not None else []:
        effect_mask = mask & ~failed_full & alive
        if not bool(effect_mask.any()):
            continue
        target.effects.apply(
            source=f"trade:{trade_ref}:{target_id}",
            tag=rider.effect.lower(),
            mask=effect_mask,
            save_ends=_rider_save_ends(rider),
        )


def _apply_trades(
    rng: BatchRNG,
    target_id: str,
    target: _CombatantState,
    source_step: Any,
    trade_state: Sequence[tuple[Any, np.ndarray]],
    mask: np.ndarray,
) -> dict[str, np.ndarray]:
    """Sequentially decides and applies every `trade_dice_for_rider` entry
    drawing from `source_step`'s own dice pool — port of ``simulator.mjs``'s
    ``pendingTradeRiders`` loop. Each trade's own EV-vs-surrendered-dice
    comparison is scalar (fixed target, fixed save DC for the whole
    encounter — the same closed-form valuation :func:`_ability_ev` already
    uses for a SavePrimitive, never a lookahead search, per the game-theory
    "perfect knowledge, optimal closed-form choice" contract this ports),
    so the only per-universe variation is each trade's own once-per-turn
    gate (`trade_state`'s own array, reset at `START_OF_TURN`). Returns
    ``{dice_expr: universes_at_that_expr}`` for the caller to roll each
    group's damage separately — two trades sharing one source (Delmar
    Fisk's cunning-poison/cunning-trip, both drawing from sneak-attack)
    compound sequentially, mirroring the reference mutating the same
    `cand.dice` in place for each trade in turn.

    Over-spend guard (issue #68): a later trade whose own `dice_cost`
    exceeds what an earlier trade already left in THIS group's pool is
    rejected outright for that group's universes — never silently floored
    to 0 dice by :func:`_shrink_leading_dice` while its rider still applies
    as if paid in full. Checked per-group, not once globally, since two
    universes can be sitting on different remaining pools by the time a
    later trade runs (one already shrunk by an earlier trade, one not)."""
    groups: dict[str, np.ndarray] = {source_step.dice: mask}
    for trade, trade_used in trade_state:
        dice_cost = trade.dice_cost
        by_count, avg = _dice_cost_stats(dice_cost, source_step.dice)
        if by_count <= 0:
            continue
        save = trade.save
        save_bonus = (
            target.spec.compiled.save_bonuses.get(save.ability, 0) if target.spec.compiled else 0
        )
        p_fail = 1.0 - _save_pass_probability(
            save_bonus, int(save.dc), _target_save_advantage_mode(target)
        )
        on_fail: OnFailBlock | None = getattr(trade, "on_fail", None)
        on_success: OnFailBlock | None = getattr(trade, "on_success", None)
        value = p_fail * _rider_value(on_fail.effects if on_fail else [], target, p_fail) + (
            1.0 - p_fail
        ) * _rider_value(
            on_success.effects if on_success else [],
            target,
            0.0,
            is_on_success_branch=True,
        )
        if value <= avg:
            continue
        new_groups: dict[str, np.ndarray] = {}
        for expr, grp_mask in groups.items():
            trade_mask = grp_mask & ~trade_used
            keep_mask = grp_mask & trade_used
            if bool(trade_mask.any()):
                if by_count > _leading_dice_count(expr):
                    # Over-spend guard (issue #68): this group's pool can't
                    # cover the cost — leave it untouched instead of
                    # shrinking past 0 while still granting the rider.
                    new_groups[expr] = new_groups.get(expr, np.zeros_like(mask)) | trade_mask
                else:
                    shrunk = _shrink_leading_dice(expr, by_count)
                    new_groups[shrunk] = new_groups.get(shrunk, np.zeros_like(mask)) | trade_mask
                    _apply_trade_rider(
                        rng,
                        trade_ref=getattr(trade, "ref", None) or "trade",
                        target_id=target_id,
                        target=target,
                        save=save,
                        on_fail=on_fail,
                        on_success=on_success,
                        mask=trade_mask,
                    )
                    trade_used[trade_mask] = True
            if bool(keep_mask.any()):
                new_groups[expr] = new_groups.get(expr, np.zeros_like(mask)) | keep_mask
        groups = new_groups
    return groups


def _ability_ev(
    ability: CompiledAbility,
    target: _CombatantState | None,
    side_hp_frac_mean: float,
    *,
    enemy_count: int = 1,
) -> float | None:
    """Scalar expected-value valuation for one compiled ability — the
    Policy-facing figure Candidates are built from (ADR-0008). ``None`` for
    a :class:`~dndsim.rules.dnd5e_2014.primitives.ReactionPrimitive` and
    anything else this pass does not choose on the actor's own turn
    (excluded from candidates, matching a planner-opaque Candidate's
    contract in :mod:`dndsim.core.policy`).

    ``enemy_count`` (issue: AoE save actions never fire) is the caller's own
    opposing-roster size, used only to scale a :class:`SavePrimitive` whose
    ``step.targets.area`` is true (Chaos Pulse: "each creature within 20
    ft") — without it, an area save was valued as though it only ever hit
    one target, so a multi-attack routine's whole-turn EV always outscored
    it regardless of how many enemies it would actually catch. Every other
    branch ignores it; it defaults to 1 so a non-area caller (the legendary-
    action ranking, which already documents its own single-reference-target
    simplification) is unaffected."""
    step = ability.step
    if isinstance(step, AttackPrimitive):
        assert target is not None
        return MultiGroupAttackMechanic(
            attack_bonus=step.to_hit,
            target_ac=target.spec.armor_class,
            damage=tuple(step.damage),
            target_defenses=_target_defenses(target),
        ).expected_value()
    if isinstance(step, SavePrimitive):
        assert target is not None
        save_bonus = (
            target.spec.compiled.save_bonuses.get(step.save, 0) if target.spec.compiled else 0
        )
        p_fail = 1.0 - _save_pass_probability(
            save_bonus, int(step.dc), _target_save_advantage_mode(target)
        )
        dmg_mean = _dice_group_mean(step.on_fail.damage, _target_defenses(target))
        value = p_fail * dmg_mean
        if step.half_on_save:
            value += (1.0 - p_fail) * 0.5 * dmg_mean
        # issue #63 interlock: a save-or-suck's condition riders (Hideous
        # Laughter's incapacitated_prone) carry real value beyond their own
        # damage — without this the planner never picks it over plain
        # damage, no matter how much output it would deny.
        if step.on_fail.effects:
            value += p_fail * _rider_value(step.on_fail.effects, target, p_fail)
        if step.targets.area:
            # Area branch: a shaped area (radius/cone)
            # catches up to its capacity; a shapeless one catches half the
            # living side, rounded up. This is a scalar ranking approximation
            # against `enemy_count` (the caller's opposing-roster size) —
            # exact per-universe resolution happens in
            # `_resolve_save_primitive_area`, which uses the real
            # `aoe_targets` positions/alive state.
            capacity = aoe_capacity(radius_ft=step.targets.radius, cone_ft=step.targets.cone)
            catch = math.ceil(enemy_count / 2) if capacity is None else min(capacity, enemy_count)
            value *= max(catch, 1)
        return value
    if isinstance(step, AutodamagePrimitive):
        assert target is not None
        dmg_mean = _dice_group_mean(step.damage, _target_defenses(target))
        if step.attached_save is not None:
            save_bonus = (
                target.spec.compiled.save_bonuses.get(step.attached_save.ability, 0)
                if target.spec.compiled
                else 0
            )
            p_fail = 1.0 - _save_pass_probability(
                save_bonus, int(step.attached_save.dc), _target_save_advantage_mode(target)
            )
            return dmg_mean * p_fail
        return dmg_mean
    if isinstance(step, HealPrimitive):
        if side_hp_frac_mean >= 0.5:
            return 0.0
        return _expr_mean(step.dice)
    return None


def _consume_mastery_vex(
    actor: _CombatantState, actor_id: str, target_id: str, mask: np.ndarray
) -> np.ndarray:
    """Read, then immediately consume, issue #71's Vex advantage grant
    against `target_id` for the universes in `mask` about to roll an attack
    against it — SRD-2024: "advantage on their next attack roll against that
    creature", spent whether that roll hits or misses. Consuming before the
    roll (rather than after) matters only within a Multiattack routine that
    swings at the same target twice: it stops this same swing's own hit
    (which may re-grant the tag, if this weapon is ALSO Vex) from erasing
    itself — the read is captured in a plain array, unaffected by the
    :meth:`~dndsim.rules.dnd5e_2014.effects.EffectTracker.remove_from_source`
    call that follows it."""
    vex: np.ndarray = actor.tags.has(_mastery_vex_tag(target_id)) & mask
    if bool(vex.any()):
        actor.effects.remove_from_source(_mastery_vex_source(actor_id, target_id), vex)
    return vex


def _run_ability(
    rng: BatchRNG,
    bus: EventBus,
    actor_id: str,
    actor: _CombatantState,
    target_id: str | None,
    target: _CombatantState | None,
    mask: np.ndarray,
    condition_mode: np.ndarray,
    hostile_adjacent: np.ndarray,
    ally_adjacent_to_target: np.ndarray,
    allies: Sequence[str],
    combatants: dict[str, _CombatantState],
    ability: CompiledAbility,
    opposing_ids: Sequence[str] = (),
) -> None:
    step = ability.step
    if isinstance(step, AttackPrimitive):
        assert target_id is not None and target is not None
        # issue #63 cause D: position disadvantage from THIS attack's own
        # profile, not the actor's flat CombatantSpec.
        step_disadvantage = _attack_primitive_disadvantage(
            actor, step, target.pos.pos, hostile_adjacent
        )
        # issue #66: Pack Tactics ("advantage_if == ally_adjacent_to_target",
        # compiled onto this attack by compile.py from a parsed statblock
        # trait) — the one advantage_if trigger this engine models.
        extra_advantage = (
            ally_adjacent_to_target if step.advantage_if == "ally_adjacent_to_target" else None
        )
        # issue #71: Weapon Mastery's Vex — a standing grant against this
        # specific target, never gated on this attack's own mastery
        # property (the advantage came from a PRIOR hit, possibly with a
        # different weapon this same turn).
        vex_advantage = _consume_mastery_vex(actor, actor_id, target_id, mask)
        if extra_advantage is not None:
            extra_advantage = extra_advantage | vex_advantage
        else:
            extra_advantage = vex_advantage
        combined = _combined_advantage(condition_mode, step_disadvantage, extra_advantage)
        for adv_code in np.unique(combined[mask]):
            sub_mask = mask & (combined == adv_code)
            _resolve_attack_primitive(
                rng,
                bus,
                actor_id,
                actor,
                target_id,
                target,
                sub_mask,
                _ADV_MODE_BY_CODE[int(adv_code)],
                step,
                combatants,
            )
    elif isinstance(step, SavePrimitive):
        assert target_id is not None and target is not None
        if step.targets.area:
            _resolve_save_primitive_area(rng, actor, opposing_ids, combatants, mask, step)
        else:
            _resolve_save_primitive(rng, actor, target_id, target, mask, step)
    elif isinstance(step, AutodamagePrimitive):
        assert target_id is not None and target is not None
        _resolve_autodamage_primitive(rng, actor, target_id, target, mask, step)
    elif isinstance(step, HealPrimitive):
        _resolve_heal_primitive(rng, mask, step, allies, combatants)
    # ReactionPrimitive, and anything else _ability_ev declined to value
    # (returned None), never reaches here: it is filtered out of the
    # candidate list before ranking (see _choose_and_run_freeform).


def _choose_and_run_freeform(
    rng: BatchRNG,
    bus: EventBus,
    actor_id: str,
    actor: _CombatantState,
    target_id: str | None,
    target: _CombatantState | None,
    mask: np.ndarray,
    condition_mode: np.ndarray,
    hostile_adjacent: np.ndarray,
    ally_adjacent_to_target: np.ndarray,
    allies: Sequence[str],
    combatants: dict[str, _CombatantState],
    slot: str,
    opposing_ids: Sequence[str] = (),
) -> None:
    """Ranks every compiled ability declared for ``slot`` (``"action"`` or
    ``"bonus"``) by its scalar :func:`_ability_ev` against ``target`` (or,
    for a heal, ``mask``'s own side HP), then per-universe walks that
    ranking for the first ability whose resource cost the actor can still
    afford — the same declared-order-ranking-then-per-universe-legality-
    bucket shape ``_take_turn``'s own enemy-target selection already uses
    (ADR-0011), one level up: here the *decision* is which ability, not
    which target.

    ``opposing_ids`` (issue: AoE save actions never fire) is the actor's own
    full opposing roster — passed to :func:`_ability_ev` as ``enemy_count``
    so an area :class:`~dndsim.rules.dnd5e_2014.primitives.SavePrimitive`
    (Chaos Pulse) is valued for how many targets it would actually catch,
    not one, and passed to :func:`_run_ability` so it resolves against every
    caught target rather than only ``target``."""
    size = mask.shape[0]
    if not bool(mask.any()):
        return
    compiled = actor.spec.compiled
    assert compiled is not None
    allowed_costs = (None, "action") if slot == "action" else ("bonus",)
    candidates = [a for a in compiled.compiled_actions if a.action_cost in allowed_costs]
    if not candidates:
        return

    if allies:
        ally_hp_frac = np.mean(
            [combatants[aid].hp.current / combatants[aid].hp.max_value for aid in allies], axis=0
        )
        masked = ally_hp_frac[mask]
        side_hp_frac_mean = float(masked.mean()) if masked.size else 1.0
    else:
        side_hp_frac_mean = 1.0

    enemy_count = max(len(opposing_ids), 1)
    scored = [
        (a, _ability_ev(a, target, side_hp_frac_mean, enemy_count=enemy_count)) for a in candidates
    ]
    ranking = [a for a, v in sorted(scored, key=lambda pair: pair[1] or -1.0, reverse=True) if v]
    if not ranking:
        return

    codes = np.full(size, -1, dtype=np.int64)
    resolved = np.zeros(size, dtype=np.bool_)
    for idx, ability in enumerate(ranking):
        legal = mask & _ability_affordable(actor, ability, size) & ~resolved
        codes = np.where(legal, idx, codes)
        resolved = resolved | legal

    for code, sub_mask in bucket_by_choice(codes):
        ability = ranking[code]
        _spend_ability_cost(actor, ability, sub_mask)
        _run_ability(
            rng,
            bus,
            actor_id,
            actor,
            target_id,
            target,
            sub_mask,
            condition_mode,
            hostile_adjacent,
            ally_adjacent_to_target,
            allies,
            combatants,
            ability,
            opposing_ids,
        )


def _routine_expected_value(compiled: CompiledStatblock, target: _CombatantState) -> float:
    """Total EV of running `compiled`'s WHOLE routine against `target` this
    turn — issue #63 cause A: the scalar the routine competes on against
    every other declared action-slot ability, instead of unconditionally
    winning the turn. Ranks ``[ref, *alternatives]`` by scalar attack EV
    per step exactly like :func:`_run_routine` itself will, then sums
    ``step.count * best_ev`` across every declared step."""
    action_by_id = {a.id: a for a in compiled.compiled_actions}
    target_defenses = _target_defenses(target)
    total = 0.0
    for step in compiled.routine:
        attack_candidates: list[AttackPrimitive] = [
            action_by_id[rid].step  # type: ignore[misc]
            for rid in (step.ref, *step.alternatives)
            if rid in action_by_id and isinstance(action_by_id[rid].step, AttackPrimitive)
        ]
        if not attack_candidates:
            continue
        best_ev = max(
            MultiGroupAttackMechanic(
                attack_bonus=candidate.to_hit,
                target_ac=target.spec.armor_class,
                damage=tuple(candidate.damage),
                target_defenses=target_defenses,
            ).expected_value()
            for candidate in attack_candidates
        )
        total += step.count * best_ev
    return total


def _run_routine(
    rng: BatchRNG,
    bus: EventBus,
    actor_id: str,
    actor: _CombatantState,
    target_id: str,
    target: _CombatantState,
    mask: np.ndarray,
    condition_mode: np.ndarray,
    hostile_adjacent: np.ndarray,
    ally_adjacent_to_target: np.ndarray,
    combatants: dict[str, _CombatantState],
    target_ranking: Sequence[str],
    usable: dict[str, np.ndarray],
    hostile_adjacent_by_target: dict[str, np.ndarray],
    ally_adjacent_by_target: dict[str, np.ndarray],
) -> None:
    """Executes a compiled Multiattack routine (issue #60): for each
    declared step, ranks ``[ref, *alternatives]`` by scalar attack EV
    against ``target`` once (batch-wide — real content's alternatives, e.g.
    Grung Elite Warrior's dagger/shortbow, carry no resource cost, so every
    universe agrees on the same choice), then resolves that attack
    ``step.count`` times — each step's own position disadvantage recomputed
    from the attack actually chosen (issue #63 cause D), not the actor's
    flat profile.

    Multiattack target lock fix: ``target_id``/``target`` only seed the
    per-universe current target — between swings, any universe whose
    current target just went Down (not dead) is re-bucketed onto the best
    remaining live, usable target from ``target_ranking`` (the identical
    ranking :func:`_take_turn` chose ``target_id`` from) — a fresh
    candidate pool each swing. A universe with no
    eligible replacement keeps swinging at its current (Down) target,
    unchanged from before this fix."""
    compiled = actor.spec.compiled
    assert compiled is not None
    action_by_id = {a.id: a for a in compiled.compiled_actions}
    size = mask.shape[0]
    code_by_id = {oid: idx for idx, oid in enumerate(target_ranking)}
    for step in compiled.routine:
        attack_candidates: list[AttackPrimitive] = [
            action_by_id[rid].step  # type: ignore[misc]
            for rid in (step.ref, *step.alternatives)
            if rid in action_by_id and isinstance(action_by_id[rid].step, AttackPrimitive)
        ]
        if not attack_candidates:
            continue
        target_defenses = _target_defenses(target)
        best = max(
            attack_candidates,
            key=lambda candidate: MultiGroupAttackMechanic(
                attack_bonus=candidate.to_hit,
                target_ac=target.spec.armor_class,
                damage=tuple(candidate.damage),
                target_defenses=target_defenses,
            ).expected_value(),
        )

        # Per-universe current target for this step; every universe in
        # `mask` starts on the routine's own `target_id`.
        current_code = np.where(mask, code_by_id.get(target_id, -1), -1)

        for swing in range(step.count):
            for code in (int(c) for c in np.unique(current_code[current_code >= 0])):
                cur_id = target_ranking[code]
                cur_target = combatants[cur_id]
                sub_mask = current_code == code
                step_disadvantage = _attack_primitive_disadvantage(
                    actor,
                    best,
                    cur_target.pos.pos,
                    hostile_adjacent_by_target.get(cur_id, hostile_adjacent),
                )
                # issue #66: Pack Tactics — see _run_ability's identical fold.
                extra_advantage = (
                    ally_adjacent_by_target.get(cur_id, ally_adjacent_to_target)
                    if best.advantage_if == "ally_adjacent_to_target"
                    else None
                )
                # issue #71: Weapon Mastery's Vex — see _run_ability's
                # identical fold. Read+consumed per swing (not once for the
                # whole routine) so a routine that swings twice at the same
                # target only spends the grant on the first of those swings.
                vex_advantage = _consume_mastery_vex(actor, actor_id, cur_id, sub_mask)
                if extra_advantage is not None:
                    extra_advantage = extra_advantage | vex_advantage
                else:
                    extra_advantage = vex_advantage
                combined = _combined_advantage(condition_mode, step_disadvantage, extra_advantage)
                for adv_code in np.unique(combined[sub_mask]):
                    fire_mask = sub_mask & (combined == adv_code)
                    _resolve_attack_primitive(
                        rng,
                        bus,
                        actor_id,
                        actor,
                        cur_id,
                        cur_target,
                        fire_mask,
                        _ADV_MODE_BY_CODE[int(adv_code)],
                        best,
                        combatants,
                    )

            if swing == step.count - 1:
                break

            # Re-derive, per universe, whether the swing just now knocked
            # the current target Down (not dead) — if so, and a live usable
            # replacement exists in `target_ranking` for that universe,
            # retarget it for the remaining swings.
            down_mask = np.zeros(size, dtype=np.bool_)
            for code in (int(c) for c in np.unique(current_code[current_code >= 0])):
                cur = combatants[target_ranking[code]]
                down_mask |= (current_code == code) & cur.down.down & ~cur.down.dead
            if not bool(down_mask.any()):
                continue
            reassign_codes = np.full(size, -1, dtype=np.int64)
            resolved = np.zeros(size, dtype=np.bool_)
            for idx, oid in enumerate(target_ranking):
                cand = combatants[oid]
                legal = (
                    down_mask
                    & usable.get(oid, np.zeros(size, dtype=np.bool_))
                    & ~cand.down.dead
                    & ~cand.down.down
                    & ~resolved
                )
                reassign_codes = np.where(legal, idx, reassign_codes)
                resolved = resolved | legal
            current_code = np.where(reassign_codes >= 0, reassign_codes, current_code)


_ROUTINE_CANDIDATE_ID = "__routine__"


def _run_action_slot(
    rng: BatchRNG,
    bus: EventBus,
    actor_id: str,
    actor: _CombatantState,
    target_id: str,
    target: _CombatantState,
    mask: np.ndarray,
    condition_mode: np.ndarray,
    hostile_adjacent: np.ndarray,
    ally_adjacent_to_target: np.ndarray,
    allies: Sequence[str],
    combatants: dict[str, _CombatantState],
    target_ranking: Sequence[str],
    usable: dict[str, np.ndarray],
    hostile_adjacent_by_target: dict[str, np.ndarray],
    ally_adjacent_by_target: dict[str, np.ndarray],
) -> None:
    """The action slot's own decision (issue #63 cause A): a compiled
    Multiattack/authored routine SEEDS the candidate set rather than
    replacing it — its own whole-turn EV (:func:`_routine_expected_value`)
    competes against every other declared action-slot ability (Perrin's
    Eldritch Blast, Hideous Laughter — neither reachable before this)
    instead of unconditionally winning whenever one exists. A statblock
    with no routine falls straight through to the plain freeform ranking,
    unchanged."""
    compiled = actor.spec.compiled
    assert compiled is not None
    if not compiled.routine:
        _choose_and_run_freeform(
            rng,
            bus,
            actor_id,
            actor,
            target_id,
            target,
            mask,
            condition_mode,
            hostile_adjacent,
            ally_adjacent_to_target,
            allies,
            combatants,
            "action",
            target_ranking,
        )
        return

    size = mask.shape[0]
    if not bool(mask.any()):
        return
    # The routine's own referenced actions (Longsword, Dagger/Shortbow)
    # don't ALSO compete as standalone single-attack freeform candidates —
    # that would double-count the same attack once as part of the routine
    # and once alone.
    routine_ref_ids = {rid for step in compiled.routine for rid in (step.ref, *step.alternatives)}
    freeform_candidates = [
        a
        for a in compiled.compiled_actions
        if a.action_cost in (None, "action") and a.id not in routine_ref_ids
    ]

    if allies:
        ally_hp_frac = np.mean(
            [combatants[aid].hp.current / combatants[aid].hp.max_value for aid in allies], axis=0
        )
        masked = ally_hp_frac[mask]
        side_hp_frac_mean = float(masked.mean()) if masked.size else 1.0
    else:
        side_hp_frac_mean = 1.0

    enemy_count = max(len(target_ranking), 1)
    scored: list[tuple[str, float]] = [
        (_ROUTINE_CANDIDATE_ID, _routine_expected_value(compiled, target))
    ]
    for a in freeform_candidates:
        v = _ability_ev(a, target, side_hp_frac_mean, enemy_count=enemy_count)
        if v:
            scored.append((a.id, v))
    ranking = [aid for aid, v in sorted(scored, key=lambda pair: pair[1], reverse=True) if v > 0]
    if not ranking:
        return

    ability_by_id = {a.id: a for a in freeform_candidates}

    codes = np.full(size, -1, dtype=np.int64)
    resolved = np.zeros(size, dtype=np.bool_)
    for idx, aid in enumerate(ranking):
        affordable = (
            np.ones(size, dtype=np.bool_)
            if aid == _ROUTINE_CANDIDATE_ID
            else _ability_affordable(actor, ability_by_id[aid], size)
        )
        legal = mask & affordable & ~resolved
        codes = np.where(legal, idx, codes)
        resolved = resolved | legal

    for code, sub_mask in bucket_by_choice(codes):
        aid = ranking[code]
        if aid == _ROUTINE_CANDIDATE_ID:
            _run_routine(
                rng,
                bus,
                actor_id,
                actor,
                target_id,
                target,
                sub_mask,
                condition_mode,
                hostile_adjacent,
                ally_adjacent_to_target,
                combatants,
                target_ranking,
                usable,
                hostile_adjacent_by_target,
                ally_adjacent_by_target,
            )
            continue
        ability = ability_by_id[aid]
        _spend_ability_cost(actor, ability, sub_mask)
        _run_ability(
            rng,
            bus,
            actor_id,
            actor,
            target_id,
            target,
            sub_mask,
            condition_mode,
            hostile_adjacent,
            ally_adjacent_to_target,
            allies,
            combatants,
            ability,
            target_ranking,
        )


def _run_compiled_turn(
    rng: BatchRNG,
    bus: EventBus,
    actor_id: str,
    actor: _CombatantState,
    target_id: str,
    target: _CombatantState,
    mask: np.ndarray,
    condition_mode: np.ndarray,
    hostile_adjacent: np.ndarray,
    ally_adjacent_to_target: np.ndarray,
    allies: Sequence[str],
    combatants: dict[str, _CombatantState],
    target_ranking: Sequence[str],
    usable: dict[str, np.ndarray],
    hostile_adjacent_by_target: dict[str, np.ndarray],
    ally_adjacent_by_target: dict[str, np.ndarray],
) -> None:
    """One compiled combatant's action + bonus slots for this dispatch
    (issue #60's replacement for the single ``_resolve_hits`` call the
    flat-``CombatantSpec`` path still makes). The action slot is
    :func:`_run_action_slot` (issue #63 cause A: a routine seeds rather than
    replaces the candidate set); the bonus slot is always a plain freeform
    ranking — a statblock that declares no bonus-cost ability simply has no
    candidates there, so this never improvises an action the page's own
    author left empty."""
    _run_action_slot(
        rng,
        bus,
        actor_id,
        actor,
        target_id,
        target,
        mask,
        condition_mode,
        hostile_adjacent,
        ally_adjacent_to_target,
        allies,
        combatants,
        target_ranking,
        usable,
        hostile_adjacent_by_target,
        ally_adjacent_by_target,
    )
    _choose_and_run_freeform(
        rng,
        bus,
        actor_id,
        actor,
        target_id,
        target,
        mask,
        condition_mode,
        hostile_adjacent,
        ally_adjacent_to_target,
        allies,
        combatants,
        "bonus",
        target_ranking,
    )


def _register_extra_attack_reaction(
    bus: EventBus,
    rng: BatchRNG,
    *,
    reactor_id: str,
    ability: CompiledAbility,
    combatants: dict[str, _CombatantState],
    allies_of_reactor: Sequence[str],
) -> None:
    """Wires one ``extra_attack``-kind :class:`~dndsim.rules.dnd5e_2014.
    primitives.ReactionPrimitive` (real content: Pack Tactics Strike —
    "When an enemy hits an ally adjacent to Perrin, he makes one Longsword
    attack") as a genuine reaction: subscribed to :data:`ATTACK_HIT_EVENT`,
    eligible only when the hit landed on a living ally other than the
    reactor, gated by both the reactor's ordinary 1-per-turn reaction pool
    (:func:`~dndsim.rules.dnd5e_2014.reactions.register_reaction`'s own
    contract) and the ability's own named resource cost, spent manually here
    since that cost is a second pool ``register_reaction`` doesn't know
    about. ``damage_reduction`` (Cutting Words) is wired separately —
    :func:`_apply_damage_reduction_reaction`, issue #63 cause C — since it
    needs pre-commit interception of the triggering attack's own rolled
    damage, a materially different shape than this additive post-hit
    attack. ``ac_bonus``/``damage_reduction_pct``/``unmodeled`` are still
    NOT wired by either pass (NOT_DONE — no measured content exercises
    them)."""
    step = ability.step
    assert isinstance(step, ReactionPrimitive)
    reactor = combatants[reactor_id]
    reactor_compiled = reactor.spec.compiled
    if reactor_compiled is None or step.attack is None:
        return
    action_by_id = {a.id: a for a in reactor_compiled.compiled_actions}
    action_by_name = {a.name: a for a in reactor_compiled.compiled_actions}
    referenced = action_by_id.get(step.attack) or action_by_name.get(step.attack)
    if referenced is None or not isinstance(referenced.step, AttackPrimitive):
        return
    referenced_attack = referenced.step
    cost = step.cost
    allies = set(allies_of_reactor)

    def eligible(event: Event) -> np.ndarray:
        payload = event.payload
        mask: np.ndarray = payload["mask"]
        target_id: str = payload["target_id"]
        size = mask.shape[0]
        if target_id == reactor_id or target_id not in allies:
            return np.zeros(size, dtype=np.bool_)
        incapacitated = batch_prevented_from_acting(reactor.tags, size) | reactor.down.down
        legal = mask & ~reactor.down.dead & ~incapacitated
        if cost is not None:
            pool = reactor.resources.get(cost.resource)
            if pool is not None:
                legal = legal & (pool.current >= cost.spend)
        result: np.ndarray = legal
        return result

    def handler(event: Event, mask: np.ndarray) -> None:
        if cost is not None:
            _spend_ability_cost(reactor, ability, mask)
        reactor.reactions_spent += mask.astype(np.float64)
        attacker_id: str = event.payload["attacker_id"]
        attacker = combatants[attacker_id]
        _resolve_attack_primitive(
            rng,
            bus,
            reactor_id,
            reactor,
            attacker_id,
            attacker,
            mask,
            "normal",
            referenced_attack,
            combatants,
        )

    register_reaction(
        bus,
        trigger=ATTACK_HIT_EVENT,
        pool=reactor.reaction_pool,
        eligible=eligible,
        handler=handler,
    )


def _actor_target_range(
    actor: _CombatantState, target_pos: np.ndarray, hostile_adjacent: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """(usable, disadvantage) for one target from ``actor``'s current
    position and its flat physical profile (issue #62). A melee profile
    that also carries a ranged option (``range_ft`` set alongside
    ``is_melee`` — a thrown weapon like the Grung Elite Warrior's Dagger)
    is usable wherever either reach or range qualifies, never only reach;
    melee's own zero disadvantage wins when both do. Every other profile
    (pure melee, or ``is_melee=False``) is unchanged: a single
    :func:`~dndsim.rules.dnd5e_2014.position.range_check` call."""
    if not actor.spec.is_melee or actor.spec.range_ft is None:
        return range_check(
            pos_actor=actor.pos.pos,
            pos_target=target_pos,
            melee=actor.spec.is_melee,
            reach_ft=actor.spec.reach_ft,
            range_ft=actor.spec.range_ft,
            range_long_ft=actor.spec.range_long_ft,
            hostile_adjacent=hostile_adjacent,
        )
    melee_usable, _ = range_check(
        pos_actor=actor.pos.pos,
        pos_target=target_pos,
        melee=True,
        reach_ft=actor.spec.reach_ft,
        range_ft=None,
        range_long_ft=None,
        hostile_adjacent=hostile_adjacent,
    )
    ranged_usable, ranged_disadvantage = range_check(
        pos_actor=actor.pos.pos,
        pos_target=target_pos,
        melee=False,
        reach_ft=None,
        range_ft=actor.spec.range_ft,
        range_long_ft=actor.spec.range_long_ft,
        hostile_adjacent=hostile_adjacent,
    )
    usable = melee_usable | ranged_usable
    disadvantage = np.where(melee_usable, 0, ranged_disadvantage)
    return usable, disadvantage


def _attack_primitive_disadvantage(
    actor: _CombatantState,
    step: AttackPrimitive,
    target_pos: np.ndarray,
    hostile_adjacent: np.ndarray,
) -> np.ndarray:
    """Position-sourced disadvantage for firing `step` specifically (issue
    #63 cause D) — the primitive's OWN reach/range profile
    (:class:`AttackPrimitive`'s ``is_melee``/``reach_ft``/``range_ft``/
    ``range_long_ft``, issue #63), never the actor's flat ``CombatantSpec``.
    Mirrors :func:`_actor_target_range`'s own melee-wins-when-both-qualify
    shape, but keyed off the attack that was actually chosen (a routine that
    ends up firing the Grung's Shortbow over its Dagger is judged as a
    ranged shot, not by the Dagger's own dual melee/thrown profile the flat
    ``CombatantSpec`` happens to declare)."""
    if not step.is_melee:
        _, disadvantage = range_check(
            pos_actor=actor.pos.pos,
            pos_target=target_pos,
            melee=False,
            reach_ft=None,
            range_ft=step.range_ft,
            range_long_ft=step.range_long_ft,
            hostile_adjacent=hostile_adjacent,
        )
        return disadvantage
    if step.range_ft is not None:
        melee_usable, _ = range_check(
            pos_actor=actor.pos.pos,
            pos_target=target_pos,
            melee=True,
            reach_ft=step.reach_ft,
            range_ft=None,
            range_long_ft=None,
            hostile_adjacent=hostile_adjacent,
        )
        _, ranged_disadvantage = range_check(
            pos_actor=actor.pos.pos,
            pos_target=target_pos,
            melee=False,
            reach_ft=None,
            range_ft=step.range_ft,
            range_long_ft=step.range_long_ft,
            hostile_adjacent=hostile_adjacent,
        )
        result: np.ndarray = np.where(melee_usable, 0, ranged_disadvantage)
        return result
    _, disadvantage = range_check(
        pos_actor=actor.pos.pos,
        pos_target=target_pos,
        melee=True,
        reach_ft=step.reach_ft,
        range_ft=None,
        range_long_ft=None,
        hostile_adjacent=hostile_adjacent,
    )
    return disadvantage


def _take_turn(
    *,
    rng: BatchRNG,
    policy: Policy,
    round_num: int,
    bus: EventBus,
    combatants: dict[str, _CombatantState],
    actor_id: str,
    opposing_ids: Sequence[str],
    party_ids: Sequence[str],
    enemy_ids: Sequence[str],
    side: str,
    turn_mask: np.ndarray,
) -> None:
    """`turn_mask` restricts this turn to the universes where it is genuinely
    `actor_id`'s own turn right now (rolled-initiative turn order): with
    per-universe rolled initiative, ``ACTION:<actor_id>`` can fire more than
    once per round, once per turn-order bucket this actor occupies across
    the batch, so every per-universe effect below (the death-save roll,
    whether the actor can act at all) must stay confined to `turn_mask` —
    never the bare batch-wide `live` mask, which would otherwise let an
    actor take a second turn this round in universes already handled by an
    earlier bucket."""
    actor = combatants[actor_id]
    size = actor.hp.size
    live = _fight_ongoing(combatants, party_ids, enemy_ids) & turn_mask

    roll_death_saves(actor.down, rng, live, actor.hp)

    prevented = batch_prevented_from_acting(actor.tags, size)
    can_act = live & ~actor.down.dead & ~actor.down.down & ~prevented
    if not bool(can_act.any()):
        return

    opp_pos = [combatants[oid].pos.pos for oid in opposing_ids]
    opp_alive = [~combatants[oid].down.dead for oid in opposing_ids]

    actor.pos.start_turn(
        actor.exhaustion_speed_ft,
        grappled=actor.tags.has("grappled"),
        restrained=actor.tags.has("restrained"),
        prone=actor.tags.has("prone"),
        speed_halved=actor.tags.has("speed_halved"),
        speed_reduced_10=actor.tags.has(MASTERY_SLOW_TAG),
    )
    disengaged = np.zeros(size, dtype=np.bool_)
    if actor.spec.is_melee:
        nearest, has_any = nearest_living_band(actor.pos.pos, opp_pos, opp_alive)
        # Issue #62: closing is one option competing against every reachable
        # option from here, not an unconditional branch — a melee profile
        # that already reaches a living target (via reach, or via a
        # secondary thrown/ranged option on the same flat profile) does not
        # spend its turn walking toward one it can already hit.
        already_usable = np.zeros(size, dtype=np.bool_)
        for opp_p, opp_a in zip(opp_pos, opp_alive, strict=True):
            u, _ = _actor_target_range(actor, opp_p, np.zeros(size, dtype=np.bool_))
            already_usable |= u & opp_a
        closing = can_act & has_any & ~already_usable
        dest = np.where(closing, nearest, actor.pos.pos)
        # Issue #69: nothing was attackable from anywhere reachable this
        # turn — a `movement_boost` dash grant (Cunning Action) doubles the
        # closing budget so the fight still converges instead of stalling
        # (simulator.mjs:1205-1212).
        dashing = _movement_boost_grant(actor, size, "dash", closing & (actor.pos.budget > 0))
        if bool(dashing.any()):
            actor.pos.budget[:] = np.where(dashing, actor.pos.budget * 2, actor.pos.budget)
    else:
        hostile_adj = hostile_adjacent_mask(actor.pos.pos, opp_pos, opp_alive)
        side_literal: Side = "party" if side == "party" else "enemy"
        kited = kite_destination(side_literal, actor.pos.pos)
        kiting = can_act & hostile_adj
        dest = np.where(kiting, kited, actor.pos.pos)
        # Issue #69: a ranged attacker sharing a band with a living hostile
        # backs off one band — Disengaging first when a `movement_boost`
        # grant offers it, so the withdrawal draws no opportunity attack
        # (simulator.mjs:1218-1229).
        disengaged = _movement_boost_grant(actor, size, "disengage", kiting)

    apply_move(
        bus,
        mover_id=actor_id,
        pos=actor.pos.pos,
        dest=dest,
        budget=actor.pos.budget,
        round_num=round_num,
        disengaged=disengaged,
        alive=lambda: ~actor.down.dead,
    )

    # --- target ranking, driven by the selected Policy (ADR-0008) ----------
    candidates = [
        Candidate(
            payload=oid,
            declared_order=order,
            value=AttackDamageMechanic(
                attack_bonus=actor.spec.attack_bonus,
                target_ac=combatants[oid].spec.armor_class,
                damage_dice_count=actor.spec.damage_dice_count,
                damage_dice_sides=actor.spec.damage_dice_sides,
                damage_bonus=actor.spec.damage_bonus,
            ).expected_value(),
        )
        for order, oid in enumerate(opposing_ids)
    ]
    ranking: list[str] = []
    remaining = list(candidates)
    while remaining:
        decision = policy.choose(remaining)
        if decision.chosen is None:
            break
        chosen_payload = decision.chosen.payload
        ranking.append(chosen_payload)  # type: ignore[arg-type]
        remaining = [c for c in remaining if c.payload != chosen_payload]

    if not ranking:
        actor.pos.tally.record_turn_no_target(can_act)
        return

    # --- per-universe legality (alive + in range), then bucket by choice ---
    usable: dict[str, np.ndarray] = {}
    position_disadvantage: dict[str, np.ndarray] = {}
    hostile_adjacent_by_target: dict[str, np.ndarray] = {}
    # Issue #66: Pack Tactics's "an ally is adjacent to the target" trigger
    # — the mirror image of hostile_adjacent_mask's own hostile-adjacency
    # check, anchored on the target's band instead of the actor's, over the
    # actor's own side (excluding the actor itself; an attacker is never
    # its own Pack Tactics ally).
    own_side_ids = party_ids if side == "party" else enemy_ids
    ally_ids = [aid for aid in own_side_ids if aid != actor_id]
    ally_adjacent_by_target: dict[str, np.ndarray] = {}
    for oid in ranking:
        target = combatants[oid]
        others_pos = [combatants[o].pos.pos for o in opposing_ids if o != oid]
        others_alive = [~combatants[o].down.dead for o in opposing_ids if o != oid]
        hostile_adj_for_range = (
            hostile_adjacent_mask(actor.pos.pos, others_pos, others_alive)
            if not actor.spec.is_melee or actor.spec.range_ft is not None
            else np.zeros(size, dtype=np.bool_)
        )
        u, d = _actor_target_range(actor, target.pos.pos, hostile_adj_for_range)
        usable[oid] = u
        position_disadvantage[oid] = d
        hostile_adjacent_by_target[oid] = hostile_adj_for_range
        ally_adjacent_by_target[oid] = hostile_adjacent_mask(
            target.pos.pos,
            [combatants[aid].pos.pos for aid in ally_ids],
            [~combatants[aid].down.dead for aid in ally_ids],
        )

    codes = np.full(size, -1, dtype=np.int64)
    resolved = np.zeros(size, dtype=np.bool_)
    for idx, oid in enumerate(ranking):
        legal = can_act & usable[oid] & ~combatants[oid].down.dead & ~resolved
        codes = np.where(legal, idx, codes)
        resolved = resolved | legal

    actor.pos.tally.record_turn_no_target(can_act & (codes == -1))

    for code, mask in bucket_by_choice(codes):
        target_id = ranking[code]
        target = combatants[target_id]
        condition_mode = batch_attack_advantage_modes(
            attacker_tags=actor.tags,
            defender_tags=target.tags,
            is_melee=np.full(size, actor.spec.is_melee),
            size=size,
        )
        if actor.spec.compiled is not None and actor.spec.compiled.compiled_actions:
            allies = party_ids if side == "party" else enemy_ids
            # issue #63 cause D: pass condition_mode + hostile_adjacent down
            # rather than a single pre-baked combined advantage — the
            # compiled path recomputes position disadvantage from whichever
            # attack primitive it actually selects, not actor.spec's flat
            # profile.
            _run_compiled_turn(
                rng,
                bus,
                actor_id,
                actor,
                target_id,
                target,
                mask,
                condition_mode,
                hostile_adjacent_by_target[target_id],
                ally_adjacent_by_target[target_id],
                allies,
                combatants,
                ranking,
                usable,
                hostile_adjacent_by_target,
                ally_adjacent_by_target,
            )
        else:
            combined = _combined_advantage(condition_mode, position_disadvantage[target_id])
            for adv_code in np.unique(combined[mask]):
                sub_mask = mask & (combined == adv_code)
                _resolve_hits(
                    rng, actor, target_id, target, sub_mask, _ADV_MODE_BY_CODE[int(adv_code)]
                )


def _register_opportunity_attack(
    bus: EventBus,
    rng: BatchRNG,
    *,
    mover_id: str,
    reactor_id: str,
    combatants: dict[str, _CombatantState],
) -> None:
    """A melee-capable reactor's opportunity attack against ``mover_id``'s
    departures — an ordinary :func:`~dndsim.rules.dnd5e_2014.reactions.
    register_reaction`, like :func:`~dndsim.rules.dnd5e_2014.position.
    register_opportunity_attack`, but reading the reactor's alive/
    incapacitated state live off ``combatants`` at trigger time instead of a
    snapshot baked in at registration — state that changes every round in a
    real encounter, unlike that helper's single-shot test usage."""
    mover = combatants[mover_id]
    reactor = combatants[reactor_id]

    def eligible(event: Event) -> np.ndarray:
        payload = event.payload
        mask: np.ndarray = payload["mask"]
        from_pos: np.ndarray = payload["from_pos"]
        size = mask.shape[0]
        incapacitated = batch_prevented_from_acting(reactor.tags, size) | reactor.down.down
        same_band = reactor.pos.pos == from_pos
        result: np.ndarray = mask & ~reactor.down.dead & ~incapacitated & same_band
        return result

    def handler(event: Event, mask: np.ndarray) -> None:
        reactor.reactions_spent += mask.astype(np.float64)
        reactor.pos.tally.record_opportunity_attack(mask)
        _resolve_hits(rng, reactor, mover_id, mover, mask, "normal")

    register_reaction(
        bus,
        trigger=leave_band_event(mover_id),
        pool=reactor.reaction_pool,
        eligible=eligible,
        handler=handler,
    )


def _legendary_pool_max_value(state: _CombatantState) -> float:
    """This legendary combatant's own declared legendary-actions-per-round
    count (Otar's Phase 1 vs. Phase 2 statblocks differ: 1/round vs.
    3/round) — the SRD-default 3.0 fallback fires only for a legendary
    combatant with no compiled statblock at all (PARTY_VS_ENEMIES_FIXTURE's
    synthetic grung-chief), never as a silent override of a real creature's
    own declared count."""
    compiled = state.spec.compiled
    if compiled is not None and compiled.legendary_actions_per_round > 0:
        return float(compiled.legendary_actions_per_round)
    return 3.0


def _make_legendary_handler(
    rng: BatchRNG,
    bus: EventBus,
    *,
    legendary_id: str,
    opposing_ids: Sequence[str],
    combatants: dict[str, _CombatantState],
    legendary_pool: ResourcePool,
) -> Callable[[Event], None]:
    """Fires one of `legendary_id`'s own named legendary actions (issue
    (this task): Otar's Lash/Thrash/Bile Spray were previously all
    collapsed into one hardcoded ``_resolve_hits(..., "normal")`` — a
    single generic bonus attack with no relationship to what the
    creature's own compiled kit actually grants, and no accounting for a
    2-cost option like Bile Spray (every use spent a flat 1 regardless).

    Ranks every compiled ``action_cost == "legendary"`` ability once, at
    handler-build time, by the same :func:`_ability_ev` scalar
    :func:`_choose_and_run_freeform` already ranks action/bonus-slot
    candidates with — valued against the first opposing id as a fixed
    reference target for the whole encounter, mirroring
    :func:`_threat_score`'s own "a reference AC/target" simplification
    (see its docstring) rather than inventing a fresh per-target valuation
    scheme. Per universe, per call, walks that ranking for the first
    ability whose own ``legendary_cost`` the pool can still afford
    (``legendary_pool.current >= ability.legendary_cost`` — not
    ``.depleted()``, which only tests ``<= 0`` and would wrongly let a
    2-cost Bile Spray fire off a pool of 1), then executes it via
    :func:`_run_ability` against every still-live opposing target in
    ``opposing_ids`` order — the same per-universe multi-target "spread"
    this handler already did before this change (a genuine simplification
    versus true single-target Lash). Since the AoE-save fix (issue: AoE save
    actions never fire), a legendary action whose compiled step is an area
    :class:`~dndsim.rules.dnd5e_2014.primitives.SavePrimitive` (a Thrash/
    Bile-Spray-shaped ability) now resolves as a genuine AoE the first time
    its per-universe mask reaches ``_run_ability`` — `opposing_ids` is
    passed through so :func:`_resolve_save_primitive_area` sees the whole
    roster, and the outer loop's `remaining` narrowing means each universe
    only ever reaches one such call, so this is not a double-resolve.
    Spends ``ability.legendary_cost`` from the pool exactly once per use,
    never once per target hit.

    Falls back to the prior flat generic-attack behavior
    (``_resolve_hits(..., "normal")``, spending a flat 1) for a legendary
    combatant with no compiled ``action_cost == "legendary"`` abilities at
    all — e.g. ``PARTY_VS_ENEMIES_FIXTURE``'s synthetic grung-chief
    (``fixture.py``), which carries no ``compiled`` statblock at all —
    never regressing that path. A combatant that DOES carry named
    legendary actions but whose every one values at zero or less this
    encounter (no non-Heal action reachable when a Heal's own
    ``side_hp_frac_mean`` is pinned to 1.0 — see below) simply takes no
    legendary action that call, rather than falling back to the generic
    attack; that is a deliberate behavior difference from the empty-list
    case, not an oversight.
    """
    legendary = combatants[legendary_id]
    compiled = legendary.spec.compiled
    legendary_actions = (
        tuple(a for a in compiled.compiled_actions if a.action_cost == "legendary")
        if compiled is not None
        else ()
    )
    own_side_ids = tuple(
        cid
        for cid, state in combatants.items()
        if state.side == legendary.side and cid != legendary_id
    )
    # A heal never has a positive EV here (``side_hp_frac_mean=1.0`` always
    # — no per-round HP-fraction context exists at handler-build time), so
    # it never wins the ranking; no authored legendary action is a heal
    # today, so this is a documented simplification, not a live gap.
    reference_target = combatants[opposing_ids[0]]
    scored = [(a, _ability_ev(a, reference_target, 1.0)) for a in legendary_actions]
    ranking = [a for a, v in sorted(scored, key=lambda pair: pair[1] or -1.0, reverse=True) if v]

    size = legendary_pool.size
    no_condition = np.zeros(size, dtype=np.int8)
    no_position_adjacency = np.zeros(size, dtype=np.bool_)

    def handler(event: Event) -> None:
        # Rolled-initiative turn order: the round loop fires this window
        # once per turn-order bucket restricted to `event.payload["mask"]`
        # — never the whole batch — so a legendary action never fires
        # "after" its own owner's turn in a universe where a DIFFERENT
        # combatant actually just went (see `_turn_mask_from_event`).
        turn_mask = _turn_mask_from_event(event, legendary_pool.size)
        eligible = (
            ~legendary.down.dead & ~legendary.down.down & ~legendary_pool.depleted() & turn_mask
        )
        if not bool(eligible.any()):
            return

        if not legendary_actions:
            legendary_pool.spend(np.ones(int(eligible.sum())), eligible)
            remaining = eligible
            for oid in opposing_ids:
                if not bool(remaining.any()):
                    break
                target = combatants[oid]
                mask = remaining & ~target.down.dead
                _resolve_hits(rng, legendary, oid, target, mask, "normal")
                remaining = remaining & ~mask
            return

        if not ranking:
            return

        codes = np.full(size, -1, dtype=np.int64)
        resolved = np.zeros(size, dtype=np.bool_)
        for idx, ability in enumerate(ranking):
            affordable = legendary_pool.current >= ability.legendary_cost
            legal = eligible & affordable & ~resolved
            codes = np.where(legal, idx, codes)
            resolved = resolved | legal
        if not bool(resolved.any()):
            return

        for code, sub_mask in bucket_by_choice(codes):
            ability = ranking[code]
            legendary_pool.spend(
                np.full(int(sub_mask.sum()), float(ability.legendary_cost)), sub_mask
            )
            remaining = sub_mask
            for oid in opposing_ids:
                if not bool(remaining.any()):
                    break
                target = combatants[oid]
                mask = remaining & ~target.down.dead
                _run_ability(
                    rng,
                    bus,
                    legendary_id,
                    legendary,
                    oid,
                    target,
                    mask,
                    no_condition,
                    no_position_adjacency,
                    no_position_adjacency,
                    own_side_ids,
                    combatants,
                    ability,
                    opposing_ids,
                )
                remaining = remaining & ~mask

    return handler


def _register_retaliate_reaction(
    bus: EventBus,
    rng: BatchRNG,
    *,
    reactor_id: str,
    step: Any,
    combatants: dict[str, _CombatantState],
    active: np.ndarray,
) -> None:
    """Wires a ``retaliate`` ability primitive (issue #63 cause B: Armor of
    Agathys) as a standing, always-on reaction to being hit — RAW retaliate
    is not action-economy-gated (no reaction-pool spend), so this is a plain
    :meth:`~dndsim.core.events.EventBus.subscribe` on :data:`ATTACK_HIT_EVENT`
    where ``target_id == reactor_id``, not a :func:`~dndsim.rules.dnd5e_2014.
    reactions.register_reaction`. ``trigger: hit_by_melee`` is approximated
    by the attacker's flat ``CombatantSpec.is_melee`` — the same granularity
    the rest of this module already uses for melee/ranged distinctions.
    ``while: temp_hp_remaining`` gates on `reactor.temp_hp` being positive AT
    THE MOMENT the event fires (i.e. after this same hit's own temp-HP
    absorption) — a named simplification (NOT_DONE): a hit that exactly
    empties the temp-HP pool will not retaliate, where 5e RAW would still
    trigger it, since Armor of Agathys' HP was present at the instant of the
    hit."""
    reactor = combatants[reactor_id]

    def handler(event: Event) -> None:
        payload = event.payload
        target_id: str = payload["target_id"]
        if target_id != reactor_id:
            return
        attacker_id: str = payload["attacker_id"]
        attacker = combatants[attacker_id]
        mask: np.ndarray = payload["mask"] & active & ~reactor.down.dead
        trigger = getattr(step, "trigger", "hit_by_any")
        if trigger == "hit_by_melee":
            mask = mask & np.full(mask.shape[0], attacker.spec.is_melee, dtype=np.bool_)
        while_ = getattr(step, "while_", None)
        if while_ == "temp_hp_remaining":
            mask = mask & (reactor.temp_hp > 0)
        if not bool(mask.any()):
            return
        n = int(mask.sum())
        dmg = _roll_damage_groups(rng, [step.damage], n, _target_defenses(attacker))
        _apply_damage_to_target(reactor, attacker, dmg, mask)

    bus.subscribe(ATTACK_HIT_EVENT, handler)


def _register_extra_damage_reaction(
    bus: EventBus,
    rng: BatchRNG,
    *,
    actor_id: str,
    step: Any,
    combatants: dict[str, _CombatantState],
    active: np.ndarray,
    requires_concentration: bool,
    trades: Sequence[Any] = (),
) -> None:
    """Wires an ``extra_damage`` ability primitive (issue #63 cause B: Hex)
    onto every hit `actor_id` lands: subscribed to :data:`ATTACK_HIT_EVENT`
    where ``attacker_id == actor_id``, gated by `active` (this ability's own
    resource cost was affordable when activated),
    ``once_per_turn`` (reset at the actor's own `start_of_turn`, matching a
    real per-turn tracker rather than a global one), and — when the
    modifier's own ``requires: {concentration: true}`` (Hex) — the actor's
    `concentrating` flag, which the existing damage-triggered concentration
    check (:func:`check_concentration_and_break`) already clears on a
    failed save, so a caster who loses concentration genuinely stops
    dealing the bonus damage.

    `trades` (issue #67 follow-up) are every ``trade_dice_for_rider``
    primitive whose own ``from_`` names this `step`'s ``ref`` (Cunning
    Strike drawing from Sneak Attack) — when non-empty, :func:`_apply_trades`
    decides and applies each one against this landed hit's own dice pool
    BEFORE it is rolled, exactly like ``simulator.mjs``'s
    ``pendingTradeRiders`` collection runs before ``rollAttackDamage``."""
    actor = combatants[actor_id]
    once_per_turn = bool(getattr(step, "once_per_turn", False))
    used_this_turn = np.zeros(active.shape[0], dtype=np.bool_)
    trade_state: list[tuple[Any, np.ndarray]] = [
        (trade, np.zeros(active.shape[0], dtype=np.bool_)) for trade in trades
    ]

    if once_per_turn:

        def _reset(event: Event) -> None:
            # Rolled-initiative turn order: reset only the universes where
            # it's genuinely `actor_id`'s own turn starting right now — this
            # event can fire more than once per round (see
            # `_turn_mask_from_event`), and a blanket reset would clear an
            # already-used flag for a universe still mid-round in an
            # earlier bucket.
            used_this_turn[_turn_mask_from_event(event, active.shape[0])] = False

        bus.subscribe(f"{START_OF_TURN}:{actor_id}", _reset)

    if trade_state:
        # `state` default-binds `trade_state` at definition time (this
        # function's own single call, never a loop) so every trade's own
        # array is reset together — the closures-in-loop trap does not
        # apply since there is exactly one subscription per call.
        def _reset_trades(event: Event, state: list[tuple[Any, np.ndarray]] = trade_state) -> None:
            mask = _turn_mask_from_event(event, active.shape[0])
            for _, arr in state:
                arr[mask] = False

        bus.subscribe(f"{START_OF_TURN}:{actor_id}", _reset_trades)

    def handler(event: Event) -> None:
        payload = event.payload
        if payload["attacker_id"] != actor_id:
            return
        mask: np.ndarray = payload["mask"] & active & ~actor.down.dead
        if requires_concentration:
            mask = mask & actor.concentrating
        if once_per_turn:
            mask = mask & ~used_this_turn
        if not bool(mask.any()):
            return
        target_id: str = payload["target_id"]
        target = combatants[target_id]
        if trade_state:
            groups = _apply_trades(rng, target_id, target, step, trade_state, mask)
            for expr, grp_mask in groups.items():
                grp_n = int(grp_mask.sum())
                if grp_n == 0:
                    continue
                dmg = _roll_damage_groups(
                    rng,
                    [DamageDie(dice=expr, type=getattr(step, "type", None))],
                    grp_n,
                    _target_defenses(target),
                )
                _apply_damage_to_target(actor, target, dmg, grp_mask)
        else:
            n = int(mask.sum())
            dmg = _roll_damage_groups(rng, [step], n, _target_defenses(target))
            _apply_damage_to_target(actor, target, dmg, mask)
        if once_per_turn:
            used_this_turn[mask] = True

    bus.subscribe(ATTACK_HIT_EVENT, handler)


def _activate_ability_primitives(
    bus: EventBus,
    rng: BatchRNG,
    *,
    actor_id: str,
    combatants: dict[str, _CombatantState],
    size: int,
) -> None:
    """Spends each compiled ``ability_primitives`` entry's own resource cost
    once, up front, for the universes that can afford it, and wires its
    standing combat-loop effect (issue #63 cause B: these compile correctly
    but the combat loop never reads them at all).

    Modeled as always-cast-before-the-fight-starts —
    ``CompiledStatblock.ability_primitives``'s own docstring: "standing,
    always-available capabilities" — never as a mid-fight action choice.
    That is coarser than the reference's own cast-on-your-turn timing, but
    the measured gap this closes (Hex -0.109, Armor of Agathys -0.035, issue
    #63) comes from the ability being applied AT ALL, not from its cast
    timing.

    Six of the 27 non-scenario ability-primitive kinds are wired —
    ``temp_hp``, ``extra_damage``, ``retaliate`` (issue #63),
    ``advantage`` with ``on: save`` (issue #65: Magic Resistance — the only
    named enemy capability issue #65 measured as actually reaching the
    engine on Party vs Archmage+Zealot; it closed 0.0251 of that matchup's
    0.1954 measured overshoot), ``trade_dice_for_rider``
    (issue #67 follow-up: Cunning Strike) — matched to its own `extra_damage`
    source by `from_` and wired alongside it, below, rather than getting an
    independent branch here, since it is a conditional choice made when that
    source lands, not a standing grant. ``movement_boost`` (issue #69:
    Cunning Action Dash/Disengage) is a sixth wired kind, but not by this
    pass: unlike the five above, it grants nothing standing — it is spent
    only in the specific universes/turns ``_take_turn`` actually uses it to
    double the closing budget or waive a kiting opportunity attack (see
    :func:`_movement_boost_grant`), so this pass explicitly skips it rather
    than spending its cost up front for the whole fight. ``reroll_take_best``
    (issue #70: Lucky feat) is a seventh wired kind, likewise skipped here:
    it is a per-attack-roll decision :func:`_apply_reroll_take_best` makes
    inside :func:`_resolve_attack_primitive` itself, never a standing grant
    this pass spends up front. ``advantage`` with any other ``on`` value
    (``attack``) and every other kind (``bonus_attack``, ``crit_range``,
    ``post_hit_rider``, ``legendary_resistance_like``, ...) still compile
    but are NOT executed by this pass (NOT_DONE — issue #65 found none of
    them authored on either enemy in that matchup, so none were measurable
    there; ``legendary_resistance_like`` in particular would matter for
    Otar, but Otar is excluded from the asserted matchup set and is a
    DM-tuned live encounter issue #65 left untouched)."""
    actor = combatants[actor_id]
    if actor.spec.compiled is None:
        return
    trades_by_source: dict[str, list[Any]] = {}
    for step in actor.spec.compiled.ability_primitives:
        if getattr(step, "kind", None) == "trade_dice_for_rider":
            source_id = getattr(step, "from_", None)
            if isinstance(source_id, str):
                trades_by_source.setdefault(source_id, []).append(step)
    for step in actor.spec.compiled.ability_primitives:
        kind = getattr(step, "kind", None)
        if kind == "movement_boost":
            # Issue #69: spent per-turn by `_take_turn` via
            # `_movement_boost_grant`, never up front — an up-front spend
            # here would burn a costed grant's resource for the whole fight
            # the first time any universe could afford it, long before any
            # universe actually dashes or disengages with it.
            continue
        affordable = _step_affordable(actor, step, size)
        if not bool(affordable.any()):
            continue
        _spend_step_cost(actor, step, affordable)
        if kind == "temp_hp":
            actor.temp_hp[affordable] += float(getattr(step, "amount", 0.0))
        elif kind == "extra_damage":
            requires: dict[str, Any] | None = getattr(step, "requires", None)
            requires_concentration = bool((requires or {}).get("concentration"))
            if requires_concentration:
                actor.concentrating[affordable] = True
            source_ref = getattr(step, "ref", None)
            _register_extra_damage_reaction(
                bus,
                rng,
                actor_id=actor_id,
                step=step,
                combatants=combatants,
                active=affordable,
                requires_concentration=requires_concentration,
                trades=trades_by_source.get(source_ref, ()) if isinstance(source_ref, str) else (),
            )
        elif kind == "retaliate":
            _register_retaliate_reaction(
                bus, rng, reactor_id=actor_id, step=step, combatants=combatants, active=affordable
            )
        elif kind == "advantage" and getattr(step, "on", None) == "save":
            actor.save_advantage[affordable] = True
        elif kind == "trade_dice_for_rider":
            continue  # wired via its `from_` source's own extra_damage branch, above
        elif kind == "reroll_take_best":
            continue  # wired per-attack inside _resolve_attack_primitive (issue #70)


def _print_debug_event(universe_index: int, event: Event) -> None:
    """One line to stderr for ``event``, restricted to ``universe_index``.

    A payload's ``"mask"`` (a per-universe boolean array — every window
    event `run_combat`'s round loop dispatches carries one) gates whether
    this universe was even live for that event; a payload with no
    ``"mask"`` key (``END_OF_ROUND``, the lair-action window) applies to
    every universe alike and always prints. Every other payload key prints
    as-is — this is a raw trace, not a formatted report."""
    payload = event.payload
    if isinstance(payload, dict) and "mask" in payload:
        mask = payload["mask"]
        if mask is not None and not bool(mask[universe_index]):
            return
        rest = {k: v for k, v in payload.items() if k != "mask"}
    else:
        rest = payload
    print(f"[debug u{universe_index}] {event.name} {rest}", file=sys.stderr)


def _debug_trace(universe_index: int) -> Callable[[Event], None]:
    """:func:`run_combat`'s ``debug_universe`` — an :class:`EventBus`
    ``trace`` sink bound to one universe index."""

    def _handler(event: Event) -> None:
        _print_debug_event(universe_index, event)

    return _handler


def run_combat(
    party: Sequence[CombatantSpec],
    enemies: Sequence[CombatantSpec],
    universes: UniverseBatch,
    round_cap: int = 20,
    policy_id: str = "dndsim:policy/greedy",
    lair_actions: Sequence[LairAction] = (),
    exhaustion_rules_id: str = DEFAULT_EXHAUSTION_RULES_ID,
    debug_universe: int | None = None,
) -> CombatResult:
    """Run ``party`` vs. ``enemies`` across every universe in ``universes``,
    in lockstep, driven by the registered Policy named ``policy_id``.

    ``exhaustion_rules_id`` (issue #55) selects which Rules pack's
    :data:`~dndsim.rules.exhaustion.exhaustion_rules` entry resolves every
    combatant's own :attr:`~dndsim.rules.dnd5e_2014.fixture.CombatantSpec.
    exhaustion_level` for this run — the edition-selectable half of
    ADR-0007's payoff. Defaults to 2024 (``dndsim``'s own edition
    default); a combatant with ``exhaustion_level`` 0 (every statblock this
    engine currently compiles) is unaffected either way.

    Generalizes the two-combatant walking skeleton's ``run_combat(a, b,
    ...)`` to any non-empty party and enemy list — a 1-vs-1 fight is simply
    the ``len(party) == len(enemies) == 1`` case, still exercised by
    ``tests/rules/test_combat.py``'s determinism/round-cap tests.

    A combatant whose :attr:`~dndsim.rules.dnd5e_2014.fixture.CombatantSpec.
    compiled` field is set (issue #60) fights with its real compiled kit —
    every declared action, its Multiattack/authored routine, and its
    ability Primitives, chosen by ``policy_id`` — instead of the flat
    single-attack shape a bare ``CombatantSpec`` otherwise resolves through
    unchanged. ``lair_actions`` (a scenario's own ``lair:`` list — see
    :class:`~dndsim.rules.dnd5e_2014.loadouts.LairAction`) drives the lair
    window with real dc/save/on_fail data, cycling one entry per round, when
    supplied; the lair owner's side still comes from
    :attr:`~dndsim.rules.dnd5e_2014.fixture.CombatantSpec.has_lair`.
    Omitted, the window keeps its prior hardcoded generic effect — existing
    callers (and the pinned golden snapshot) are unaffected.

    ``debug_universe`` (debug mode): an index into the batch. When set,
    every :class:`~dndsim.core.events.Event` the encounter's
    :class:`~dndsim.core.events.EventBus` dispatches is printed to stderr
    via :func:`_print_debug_event`, filtered to that one universe (a
    payload without a ``"mask"`` key — round-level bookkeeping like
    ``END_OF_ROUND`` — always prints, since it applies to every universe
    alike). ``None`` (the default) installs no trace and changes nothing.
    """
    if not party or not enemies:
        raise ValueError("run_combat requires at least one combatant on each side")
    size = universes.size
    rng = universes.rng
    policy = policies.get(policy_id)(seed=universes.seed)

    party_ids = [c.entity.id for c in party]
    enemy_ids = [c.entity.id for c in enemies]

    combatants: dict[str, _CombatantState] = {}
    for side, group in (("party", party), ("enemy", enemies)):
        for c in group:
            combatants[c.entity.id] = _init_state(c, side, size, exhaustion_rules_id)

    # A combatant marked starts_concentrating maintains a real, tracked
    # effect on their own side (a "blessed" tag; not wired into any roll —
    # this exercises EffectTracker.apply/remove_from_source and the
    # damage-triggered concentration check end to end, not any specific
    # concentration-source ability's mechanical benefit) so a concentration
    # break in _resolve_hits has something real to remove.
    for cid, state in combatants.items():
        if state.spec.starts_concentrating:
            allies = party_ids if state.side == "party" else enemy_ids
            full_mask = np.ones(size, dtype=np.bool_)
            for aid in allies:
                combatants[aid].effects.apply(
                    source=concentration_source(cid), tag="blessed", mask=full_mask
                )

    bus = EventBus(trace=_debug_trace(debug_universe) if debug_universe is not None else None)

    # Issue #63 cause B: each compiled combatant's standing ability
    # primitives (Hex, Armor of Agathys, ...) — dead code before this pass.
    for cid in (*party_ids, *enemy_ids):
        _activate_ability_primitives(bus, rng, actor_id=cid, combatants=combatants, size=size)

    for mover_id in (*party_ids, *enemy_ids):
        mover_side = combatants[mover_id].side
        reactor_ids = enemy_ids if mover_side == "party" else party_ids
        for reactor_id in reactor_ids:
            if combatants[reactor_id].spec.is_melee:
                _register_opportunity_attack(
                    bus, rng, mover_id=mover_id, reactor_id=reactor_id, combatants=combatants
                )

    # Issue (this task): sized per :func:`_legendary_pool_max_value` — each
    # legendary combatant's own declared count, never a flat constant.
    legendary_ids = frozenset(cid for cid, c in combatants.items() if c.spec.legendary)
    legendary_pools = {
        lid: ResourcePool("legendary", np.full(size, _legendary_pool_max_value(combatants[lid])))
        for lid in legendary_ids
    }
    for lid in legendary_ids:
        opposing = enemy_ids if combatants[lid].side == "party" else party_ids
        handler = _make_legendary_handler(
            rng,
            bus,
            legendary_id=lid,
            opposing_ids=opposing,
            combatants=combatants,
            legendary_pool=legendary_pools[lid],
        )
        bus.subscribe(f"legendary_action:{lid}", handler)

    # Issue #60: an extra_attack-kind ReactionPrimitive (Pack Tactics
    # Strike) on any compiled combatant, wired regardless of which side it
    # fights on.
    for cid, state in combatants.items():
        if state.spec.compiled is None:
            continue
        allies = party_ids if state.side == "party" else enemy_ids
        for ability in state.spec.compiled.compiled_actions:
            if (
                isinstance(ability.step, ReactionPrimitive)
                and ability.step.reaction_kind == "extra_attack"
            ):
                _register_extra_attack_reaction(
                    bus,
                    rng,
                    reactor_id=cid,
                    ability=ability,
                    combatants=combatants,
                    allies_of_reactor=[a for a in allies if a != cid],
                )

    lair_owner = next((c for c in (*party, *enemies) if c.has_lair), None)
    has_lair = lair_owner is not None
    if lair_owner is not None:
        lair_owner_side = combatants[lair_owner.entity.id].side
        lair_target_ids = enemy_ids if lair_owner_side == "party" else party_ids

        lair_cycle = {"round": 0}

        def _lair_handler_from_scenario(event: Event) -> None:
            action = lair_actions[lair_cycle["round"] % len(lair_actions)]
            lair_cycle["round"] += 1
            for tid in lair_target_ids:
                target = combatants[tid]
                tsize = target.hp.size
                alive = ~target.down.dead
                n = int(alive.sum())
                if n == 0:
                    continue
                saved = ConcentrationSaveMechanic(
                    con_bonus=_save_bonus(target, action.save),
                    dc=int(action.dc),
                    advantage_mode=_save_advantage_mode(target, alive),
                ).resolve(rng, n)
                failed_alive = saved <= 0.0
                failed_full = np.zeros(tsize, dtype=np.bool_)
                failed_full[alive] = failed_alive
                if action.on_fail.damage:
                    rolled = _roll_damage_groups(
                        rng, action.on_fail.damage, n, _target_defenses(target)
                    )
                    applied_alive = np.where(
                        failed_alive, rolled, rolled * 0.5 if action.half_on_save else 0.0
                    )
                    if bool((applied_alive > 0).any()):
                        was_down = target.down.down.copy()
                        target.hp.spend(applied_alive, alive)
                        hit_full = np.zeros(tsize, dtype=np.bool_)
                        hit_full[alive] = applied_alive > 0
                        apply_damage_while_down(target.down, hit_full & was_down)
                        newly_down = hit_full & ~was_down & target.hp.depleted()
                        enter_down(target.down, newly_down)
                        target.ever_down |= newly_down
                for rider in action.on_fail.effects:
                    target.effects.apply(
                        source="lair", tag=rider.effect.lower(), mask=failed_full, duration_rounds=1
                    )

        def _lair_handler(event: Event) -> None:
            # "poisoned" (self-disadvantage only, per conditions.py) rather
            # than "restrained": a lair hazard reapplied every round via a
            # bare, unresisted duration_rounds=1 tag (no saving throw
            # modeled here) must stay survivable across a whole encounter.
            # "restrained" additionally zeros speed and grants attacker
            # advantage — reapplied every round with no way to shake it off,
            # that permanently locks its targets out of both movement and
            # any fair roll for the rest of the fight, which is a fixture
            # design defect, not a realistic lair action.
            for tid in lair_target_ids:
                target = combatants[tid]
                target.effects.apply(
                    source="lair", tag="poisoned", mask=~target.down.dead, duration_rounds=1
                )

        bus.subscribe(LAIR_ACTION, _lair_handler_from_scenario if lair_actions else _lair_handler)

    for cid in (*party_ids, *enemy_ids):

        def _start_of_turn_handler(event: Event, cid: str = cid) -> None:
            # Rolled-initiative turn order (issue: turn-order Divergence):
            # `mask` restricts this to the universes where it's genuinely
            # `cid`'s own turn right now — with per-universe rolled
            # initiative this event can fire more than once per round, once
            # per turn-order bucket `cid` occupies across the batch. Absent
            # a mask (an older caller not carrying rolled-order state — none
            # remain in this module, but the payload contract stays opaque
            # per `Event`'s own docstring), the whole batch is the default,
            # matching this handler's pre-rolled-initiative behavior.
            state = combatants[cid]
            mask: np.ndarray = _turn_mask_from_event(event, size)
            n = int(mask.sum())
            if n == 0:
                return
            state.reaction_pool.restore(np.ones(n), mask)
            legendary_pool = legendary_pools.get(cid)
            if legendary_pool is not None:
                legendary_pool.restore(legendary_pool.max_value[mask], mask)

        def _action_handler(event: Event, cid: str = cid) -> None:
            state = combatants[cid]
            opposing = enemy_ids if state.side == "party" else party_ids
            mask: np.ndarray = _turn_mask_from_event(event, size)
            _take_turn(
                rng=rng,
                policy=policy,
                round_num=event.payload["round"],
                bus=bus,
                combatants=combatants,
                actor_id=cid,
                opposing_ids=opposing,
                party_ids=party_ids,
                enemy_ids=enemy_ids,
                side=state.side,
                turn_mask=mask,
            )

        def _end_of_turn_handler(event: Event, cid: str = cid) -> None:
            # Issue #63 interlock: save_ends conditions (Hideous Laughter's
            # incapacitated_prone) re-save at the bearer's own end-of-turn
            # instead of persisting for the rest of the fight. `mask`:
            # see `_start_of_turn_handler`'s own note above.
            state = combatants[cid]
            mask: np.ndarray = _turn_mask_from_event(event, size)

            def _tick_save_bonus(ability: str) -> int:
                compiled = state.spec.compiled
                base = compiled.save_bonuses.get(ability, 0) if compiled else 0
                return base - state.exhaustion_d20_penalty

            state.effects.tick_saves(rng, save_bonus=_tick_save_bonus, mask=mask)

        bus.subscribe(f"{START_OF_TURN}:{cid}", _start_of_turn_handler)
        bus.subscribe(f"{ACTION}:{cid}", _action_handler)
        bus.subscribe(f"{END_OF_TURN}:{cid}", _end_of_turn_handler)

    max_party_down = np.zeros(size, dtype=np.int64)

    def _end_of_round_handler(event: Event) -> None:
        for state in combatants.values():
            state.effects.tick_end_of_round()
        count = np.zeros(size, dtype=np.int64)
        for pid in party_ids:
            p = combatants[pid]
            count += (p.down.down | p.down.dead).astype(np.int64)
        max_party_down[:] = np.maximum(max_party_down, count)

    bus.subscribe(END_OF_ROUND, _end_of_round_handler)

    # Turn-order Divergence fix: per-universe rolled initiative (see
    # `_roll_initiative_order`) replaces the fixed party-then-enemy group
    # order `build_round_timeline`/`run_round` walk identically for every
    # universe. Rolled once at encounter start (5e RAW: order is fixed for
    # the whole encounter, not re-rolled per round) — `all_ids[order[slot,
    # u]]` is who acts in turn-slot `slot` for universe `u`.
    all_ids = [*party_ids, *enemy_ids]
    turn_order = _roll_initiative_order(rng, combatants, all_ids, size)

    rounds_played = np.zeros(size, dtype=np.int32)
    for round_num in range(1, round_cap + 1):
        live = _fight_ongoing(combatants, party_ids, enemy_ids)
        if not bool(live.any()):
            break
        rounds_played = np.where(live, round_num, rounds_played)
        if has_lair:
            bus.publish(Event(name=LAIR_ACTION, payload={"round": round_num}))
        for slot in range(len(all_ids)):
            for idx, mask in bucket_by_choice(turn_order[slot]):
                cid = all_ids[idx]
                payload = {"round": round_num, "mask": mask}
                bus.publish(Event(name=f"{START_OF_TURN}:{cid}", payload=payload))
                bus.publish(Event(name=f"{ACTION}:{cid}", payload=payload))
                bus.publish(Event(name=f"{END_OF_TURN}:{cid}", payload=payload))
                for lid in legendary_ids:
                    if lid != cid:
                        bus.publish(Event(name=f"legendary_action:{lid}", payload=payload))
        bus.publish(Event(name=END_OF_ROUND, payload={"round": round_num}))

    party_dead_all = _side_dead_all(combatants, party_ids)
    enemy_dead_all = _side_dead_all(combatants, enemy_ids)
    party_win = enemy_dead_all & ~party_dead_all
    enemy_win = party_dead_all & ~enemy_dead_all
    draw = ~(party_win | enemy_win)

    party_hp_pct = {
        pid: combatants[pid].hp.current / combatants[pid].hp.max_value for pid in party_ids
    }
    pc_outcomes = tuple(
        PcOutcome(
            id=pid,
            name=combatants[pid].spec.entity.name,
            hp_remaining_pct_p5=float(np.percentile(party_hp_pct[pid], 5)),
            hp_remaining_pct_p50=float(np.percentile(party_hp_pct[pid], 50)),
            hp_remaining_pct_p95=float(np.percentile(party_hp_pct[pid], 95)),
            down_probability=float(combatants[pid].ever_down.mean()),
        )
        for pid in party_ids
    )
    combatant_outputs = tuple(
        CombatantOutput(
            id=cid,
            name=state.spec.entity.name,
            side=state.side,
            mean_damage_dealt=float(state.damage_dealt.mean()),
            mean_reactions_spent=float(state.reactions_spent.mean()),
            mean_concentration_breaks=float(state.concentration_breaks.mean()),
            mean_turns_no_target=state.pos.tally.mean_turns_no_target(),
            mean_opportunity_attacks=state.pos.tally.mean_opportunity_attacks(),
        )
        for cid, state in combatants.items()
    )
    at_least_k_down = tuple(
        float((max_party_down >= k).mean()) for k in range(1, len(party_ids) + 1)
    )
    mean_party_hp_loss = float(
        (1.0 - np.mean([party_hp_pct[pid] for pid in party_ids], axis=0)).mean()
    )

    return CombatResult(
        universes=size,
        seed=universes.seed,
        rounds_cap=round_cap,
        party_name=", ".join(c.entity.name for c in party),
        enemy_name=", ".join(c.entity.name for c in enemies),
        party_win_rate=float(party_win.sum()) / size,
        enemy_win_rate=float(enemy_win.sum()) / size,
        draw_rate=float(draw.sum()) / size,
        mean_rounds=float(rounds_played.mean()),
        median_rounds=float(np.percentile(rounds_played, 50)),
        p95_rounds=float(np.percentile(rounds_played, 95)),
        any_down_probability=at_least_k_down[0] if at_least_k_down else 0.0,
        at_least_k_down=at_least_k_down,
        tpk_probability=float(enemy_win.sum()) / size,
        mean_party_hp_loss=mean_party_hp_loss,
        pc_outcomes=pc_outcomes,
        combatant_outputs=combatant_outputs,
    )
