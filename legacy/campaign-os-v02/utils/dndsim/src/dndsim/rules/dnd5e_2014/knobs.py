"""Mechanical mutation vocabulary shared by
:mod:`dndsim.rules.dnd5e_2014.sensitivity` (single-knob probing) and
:mod:`dndsim.rules.dnd5e_2014.evolve` (the GA) — one knob table so the two
can never drift apart.

This module's knob set is the subset of fields
:class:`~dndsim.rules.dnd5e_2014.compile.CompiledStatblock` and
:class:`~dndsim.rules.dnd5e_2014.fixture.CombatantSpec` actually carry today
(``ac``, ``hp``, ``to_hit``, ``flat_damage``, ``dice_step``, ``multiattack``,
``speed_ft``). Deferred knobs, each because the underlying field this
engine models differently or not yet — NOT approximated, named explicitly
rather than silently dropped:

- ``saveDc`` / ``riderSaveDc`` — no compiled ``SavePrimitive``/rider dc is
  reachable through a single "primary attack" seam the way ``to_hit`` is;
  the JS knob mutates every save-kind action, this port's primary-ability
  seam only ever touches one.
- ``rechargeWiden`` / ``legendaryActions`` / ``legendaryResistances`` —
  ``CombatantSpec.legendary`` is a bare bool here (issue #59), not a count;
  there is no legendary-action/resistance count to mutate.
- ``regenAmount`` / ``auraDamage`` — no ``periodic_effect``-kind Modifier
  is compiled into ``ability_primitives`` yet.
- ``startBand`` — ``CompiledStatblock.position`` is carried through
  read-only by this port; nothing deploys a mutated band into a live
  encounter yet.
- ``damageReductionPct`` — no ``damage_reduction_pct`` reaction compiles.

Every one of these is a real gap against ``evolve.mjs``, not a design
choice; a future issue that compiles the missing Primitive/field can add
its knob here without touching a caller.
"""

from __future__ import annotations

import dataclasses
from collections.abc import Sequence

from dndsim.rules.dnd5e_2014.compile import CompiledAbility, CompiledStatblock
from dndsim.rules.dnd5e_2014.dice import DiceTerm, parse_dice_expr
from dndsim.rules.dnd5e_2014.fixture import CombatantSpec
from dndsim.rules.dnd5e_2014.primitives import AttackPrimitive, RoutineStepPrimitive
from dndsim.rules.dnd5e_2014.sweep import combatant_spec_from_statblock

MUTATION_KNOBS: tuple[str, ...] = (
    "ac",
    "hp",
    "to_hit",
    "flat_damage",
    "dice_step",
    "multiattack",
    "speed_ft",
)

# Absolute caps per knob — the GA/probe cannot wander into absurdity.
# hp is a fraction of the original max, applied in clamp_delta below.
MUTATION_BOUNDS: dict[str, float] = {
    "ac": 3,
    "to_hit": 3,
    "flat_damage": 6,
    "dice_step": 3,
    "multiattack": 2,
    "speed_ft": 30,
}
HP_FRACTION_BOUND = 0.5


def hp_step(hp_max: int) -> int:
    """hp steps by 10% of max, never less than 5 — matches evolve.mjs's hpStep."""
    return max(5, round(hp_max * 0.1))


def knob_delta(statblock: CompiledStatblock, knob: str, direction: int) -> float:
    """Signed step size for one knob on one statblock. hp steps by
    :func:`hp_step`; speed_ft steps by 5 ft; every other knob steps by 1."""
    if knob == "hp":
        return direction * hp_step(statblock.hp)
    if knob == "speed_ft":
        return direction * 5
    return float(direction)


def clamp_delta(delta: dict[str, float], statblock: CompiledStatblock) -> dict[str, float]:
    """Clamp a delta into MUTATION_BOUNDS and drop zero entries."""
    out: dict[str, float] = {}
    for k, v in delta.items():
        if k == "hp":
            cap = round(statblock.hp * HP_FRACTION_BOUND)
            clamped = max(-cap, min(cap, v))
        else:
            bound = MUTATION_BOUNDS[k]
            clamped = max(-bound, min(bound, v))
        if clamped != 0:
            out[k] = clamped
    return out


def mutate_dice_expr(expr: str, dice_step: int = 0, flat_delta: int = 0) -> str:
    """Canonical rebuild of a dice expression with a die-count step on the
    leading NdM term and a flat-damage adjustment folded into the modifier —
    matches evolve.mjs's mutateDiceExpr."""
    parsed = parse_dice_expr(expr)
    dice: list[DiceTerm] = list(parsed.dice)
    if dice and dice_step:
        first = dice[0]
        dice[0] = DiceTerm(
            count=max(1, first.count + dice_step), sides=first.sides, sign=first.sign
        )
    flat = parsed.flat + flat_delta
    parts = []
    for i, d in enumerate(dice):
        sign = "-" if d.sign < 0 else ("+" if i > 0 else "")
        parts.append(f"{sign}{d.count}d{d.sides}")
    out = "".join(parts)
    if out == "":
        return str(flat)
    if flat > 0:
        out += f"+{flat}"
    elif flat < 0:
        out += str(flat)
    return out


def primary_attack_ability(statblock: CompiledStatblock) -> CompiledAbility | None:
    """The ability a knob probe/GA mutates: the first attack-kind step of
    the compiled routine, or (no routine resolved) the first attack-kind
    compiled action — the same priority ``sweep.py``'s own
    ``primary_attack`` uses to pick a sweep cell's representative attack."""
    by_id = {a.id: a for a in statblock.compiled_actions}
    for step in statblock.routine:
        ability = by_id.get(step.ref)
        if ability is not None and isinstance(ability.step, AttackPrimitive):
            return ability
    for ability in statblock.compiled_actions:
        if isinstance(ability.step, AttackPrimitive):
            return ability
    return None


def describe_delta(statblock: CompiledStatblock, delta: dict[str, float]) -> str:
    """Human delta summary: "AC 15->16, HP 90->75, damage dice +1 die"."""
    parts = []
    if "ac" in delta:
        parts.append(f"AC {statblock.ac}->{int(statblock.ac + delta['ac'])}")
    if "hp" in delta:
        parts.append(f"HP {statblock.hp}->{max(1, int(statblock.hp + delta['hp']))}")
    if "to_hit" in delta:
        parts.append(f"to-hit {delta['to_hit']:+.0f}")
    if "flat_damage" in delta:
        parts.append(f"flat damage {delta['flat_damage']:+.0f}")
    if "dice_step" in delta:
        parts.append(f"damage dice {delta['dice_step']:+.0f} die")
    if "multiattack" in delta:
        ability = primary_attack_ability(statblock)
        step = (
            next((s for s in statblock.routine if s.ref == ability.id), None) if ability else None
        )
        if step is not None:
            new_count = max(1, int(step.count + delta["multiattack"]))
            name = ability.name if ability else step.ref
            parts.append(
                f"multiattack {delta['multiattack']:+.0f} ({name} {step.count}->{new_count})"
            )
        else:
            parts.append(f"multiattack {delta['multiattack']:+.0f}")
    if "speed_ft" in delta:
        parts.append(f"speed {delta['speed_ft']:+.0f} ft")
    return ", ".join(parts) if parts else "original (no changes)"


def apply_delta(spec: CombatantSpec, delta: dict[str, float]) -> CombatantSpec:
    """Apply a delta to a combatant's compiled statblock (+ speed_ft, which
    lives on the spec rather than the statblock) -> a new CombatantSpec.
    ``spec.compiled`` must be set — every knob targets the compiled kit."""
    statblock = spec.compiled
    if statblock is None:
        raise ValueError("knobs.apply_delta: spec.compiled is required")

    new_ac = int(statblock.ac + delta.get("ac", 0))
    new_hp = max(1, int(statblock.hp + delta.get("hp", 0)))

    primary = primary_attack_ability(statblock)
    new_actions: Sequence[CompiledAbility] = statblock.compiled_actions
    if primary is not None and isinstance(primary.step, AttackPrimitive):
        step = primary.step
        new_to_hit = int(step.to_hit + delta.get("to_hit", 0))
        new_damage = list(step.damage)
        dice_step = int(delta.get("dice_step", 0))
        flat_delta = int(delta.get("flat_damage", 0))
        if (dice_step or flat_delta) and new_damage:
            new_damage[0] = new_damage[0].model_copy(
                update={"dice": mutate_dice_expr(new_damage[0].dice, dice_step, flat_delta)}
            )
        new_step = step.model_copy(update={"to_hit": new_to_hit, "damage": new_damage})
        new_actions = tuple(
            dataclasses.replace(a, step=new_step) if a.id == primary.id else a
            for a in statblock.compiled_actions
        )

    new_routine: Sequence[RoutineStepPrimitive] = statblock.routine
    multiattack_delta = delta.get("multiattack")
    if primary is not None and multiattack_delta:
        new_routine = tuple(
            rs.model_copy(update={"count": max(1, int(rs.count + multiattack_delta))})
            if rs.ref == primary.id
            else rs
            for rs in statblock.routine
        )

    mutated_statblock = dataclasses.replace(
        statblock,
        ac=new_ac,
        hp=new_hp,
        compiled_actions=tuple(new_actions),
        routine=tuple(new_routine),
    )
    new_spec = combatant_spec_from_statblock(mutated_statblock, suffix=_suffix(spec.entity.id))
    speed_ft = max(0, int(spec.speed_ft + delta.get("speed_ft", 0)))
    return dataclasses.replace(new_spec, speed_ft=speed_ft)


def _suffix(entity_id: str) -> str:
    """The trailing ``/...`` segment ``combatant_spec_from_statblock``
    appended when building ``entity_id`` originally — reused so a mutated
    combatant keeps the same id shape (never colliding with the original
    inside the same encounter)."""
    idx = entity_id.rfind("/")
    return entity_id[idx:] if idx != -1 else ""
