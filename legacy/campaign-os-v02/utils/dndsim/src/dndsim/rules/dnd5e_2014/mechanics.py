"""This pack's core d20 Mechanics: the attack-roll-plus-damage roll, a
concentration save, and a recharge roll.

The attack roll: a d20 against a target's armour class, on hit dealing
damage dice plus a flat bonus; a natural 20 always hits and doubles the
damage dice (not the flat bonus); a natural 1 always misses; advantage and
disadvantage (already collapsed to one mode — see
:mod:`dndsim.rules.dnd5e_2014.advantage`) roll two dice and keep the
highest or lowest. This is 5e knowledge, so it lives here, never in
``dndsim.core`` (ADR-0007).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, ClassVar

import numpy as np

from dndsim.core.mechanic import Mechanic, mechanics
from dndsim.rules.dnd5e_2014.advantage import AdvantageMode, d20_face_probabilities, roll_d20
from dndsim.rules.dnd5e_2014.attack_string import DamageGroup
from dndsim.rules.dnd5e_2014.dice import parse_dice_expr
from dndsim.rules.dnd5e_2014.statblock import Defenses

if TYPE_CHECKING:
    from hypothesis.strategies import SearchStrategy

    from dndsim.core.rng import BatchRNG

MECHANIC_ID = "dnd5e_2014:mechanic/attack_damage"
MULTI_GROUP_ATTACK_MECHANIC_ID = "dnd5e_2014:mechanic/multi_group_attack_damage"
CONCENTRATION_MECHANIC_ID = "dnd5e_2014:mechanic/concentration_save"
RECHARGE_MECHANIC_ID = "dnd5e_2014:mechanic/recharge"

_ADVANTAGE_MODES: tuple[AdvantageMode, ...] = ("normal", "advantage", "disadvantage")


def mitigation_factor(defenses: Defenses, damage_type: str | None) -> float:
    """The x0/x0.5/x2 scalar one damage group's type resolves to against a
    target's declared :class:`~dndsim.rules.dnd5e_2014.statblock.Defenses`
    (issue #61), precedence immune beats resist beats vulnerable, with a
    plain literal-tag membership check: a ``nonmagical_<type>`` resist tag
    is carried through unchanged and matched only against a damage type
    spelled that way (nothing here expands or strips the prefix)."""
    t = damage_type if damage_type is not None else "untyped"
    if t in defenses.immune:
        return 0.0
    if t in defenses.resist:
        return 0.5
    if t in defenses.vulnerable:
        return 2.0
    return 1.0


@mechanics.register(MECHANIC_ID)
@dataclass(slots=True)
class AttackDamageMechanic(Mechanic):
    """One attacker-vs-target attack roll and its damage, fully parameterized."""

    id: ClassVar[str] = MECHANIC_ID

    attack_bonus: int
    target_ac: int
    damage_dice_count: int
    damage_dice_sides: int
    damage_bonus: int = 0
    advantage_mode: AdvantageMode = "normal"

    def resolve(self, rng: BatchRNG, size: int) -> np.ndarray:
        d20 = roll_d20(rng, size, self.advantage_mode)
        crit = d20 == 20
        fumble = d20 == 1
        hit = (~fumble) & (crit | (d20 + self.attack_bonus >= self.target_ac))

        dice = rng.integers(1, self.damage_dice_sides + 1, size=(self.damage_dice_count, size))
        base_damage = dice.sum(axis=0) + self.damage_bonus

        crit_dice = rng.integers(1, self.damage_dice_sides + 1, size=(self.damage_dice_count, size))
        crit_extra = np.where(crit, crit_dice.sum(axis=0), 0)

        damage = base_damage + crit_extra
        return np.where(hit, damage, 0).astype(np.float64)

    def expected_value(self) -> float:
        dice_avg = self.damage_dice_count * (self.damage_dice_sides + 1) / 2.0
        hit_damage = dice_avg + self.damage_bonus
        crit_damage = dice_avg * 2 + self.damage_bonus

        probs = d20_face_probabilities(self.advantage_mode)
        total = 0.0
        for roll, prob in zip(range(1, 21), probs, strict=True):
            if roll == 1:
                continue  # natural 1 always misses: contributes 0
            if roll == 20:
                total += crit_damage * prob  # natural 20 always hits
            elif roll + self.attack_bonus >= self.target_ac:
                total += hit_damage * prob
        return total

    @classmethod
    def hypothesis_strategy(cls) -> SearchStrategy[AttackDamageMechanic]:
        import hypothesis.strategies as st

        return st.builds(
            cls,
            attack_bonus=st.integers(min_value=-5, max_value=15),
            target_ac=st.integers(min_value=5, max_value=30),
            damage_dice_count=st.integers(min_value=1, max_value=4),
            damage_dice_sides=st.sampled_from([4, 6, 8, 10, 12]),
            damage_bonus=st.integers(min_value=0, max_value=10),
            advantage_mode=st.sampled_from(_ADVANTAGE_MODES),
        )


@mechanics.register(MULTI_GROUP_ATTACK_MECHANIC_ID)
@dataclass(slots=True)
class MultiGroupAttackMechanic(Mechanic):
    """One attacker-vs-target attack roll and its damage, across every
    declared :class:`~dndsim.rules.dnd5e_2014.attack_string.DamageGroup`
    (issue #60) — :class:`AttackDamageMechanic` generalized from a single
    dice-count/dice-sides/flat-bonus triple to a compiled
    :class:`~dndsim.rules.dnd5e_2014.primitives.AttackPrimitive`'s real
    ``damage`` list (e.g. a weapon die plus a separate poison-damage group),
    replacing the lossy single-group reduction
    ``sweep.py``'s ``_reduce_damage`` used to perform. A single-group
    ``damage`` list behaves identically to :class:`AttackDamageMechanic`."""

    id: ClassVar[str] = MULTI_GROUP_ATTACK_MECHANIC_ID

    attack_bonus: int
    target_ac: int
    damage: tuple[DamageGroup, ...]
    advantage_mode: AdvantageMode = "normal"
    # Issue #61: the target's declared resist/immune/vulnerable tags.
    # Defaults to no defenses at all — every existing call site (and every
    # combatant with no compiled statblock) keeps its prior full-value
    # behavior unchanged.
    target_defenses: Defenses = field(default_factory=Defenses)

    def _group_damage_totals(self) -> tuple[float, float]:
        """``(hit_damage, crit_damage)`` summed across every damage group,
        each group's own dice/flat mean mitigated by its own type's
        :func:`mitigation_factor` before the crit-doubling split — mirrors
        ``engine.mjs``'s ``applyDamage`` applying mitigation per typed part,
        after crit doubling, never before."""
        hit_damage = 0.0
        crit_damage = 0.0
        for group in self.damage:
            parsed = parse_dice_expr(group.dice)
            dice_mean = sum(term.sign * term.count * (term.sides + 1) / 2.0 for term in parsed.dice)
            factor = mitigation_factor(self.target_defenses, group.type)
            hit_damage += factor * (dice_mean + parsed.flat)
            crit_damage += factor * (dice_mean * 2 + parsed.flat)
        return hit_damage, crit_damage

    def resolve(self, rng: BatchRNG, size: int) -> np.ndarray:
        d20 = roll_d20(rng, size, self.advantage_mode)
        crit = d20 == 20
        fumble = d20 == 1
        hit = (~fumble) & (crit | (d20 + self.attack_bonus >= self.target_ac))

        total = np.zeros(size, dtype=np.float64)
        for group in self.damage:
            parsed = parse_dice_expr(group.dice)
            factor = mitigation_factor(self.target_defenses, group.type)
            group_total = np.full(size, float(parsed.flat), dtype=np.float64)
            for term in parsed.dice:
                rolls = rng.integers(1, term.sides + 1, size=(term.count, size)).sum(axis=0)
                group_total += term.sign * rolls
                crit_rolls = rng.integers(1, term.sides + 1, size=(term.count, size)).sum(axis=0)
                group_total += np.where(crit, term.sign * crit_rolls, 0.0)
            total += group_total * factor
        return np.where(hit, total, 0.0).astype(np.float64)

    def expected_value(self) -> float:
        hit_damage, crit_damage = self._group_damage_totals()

        probs = d20_face_probabilities(self.advantage_mode)
        total = 0.0
        for roll, prob in zip(range(1, 21), probs, strict=True):
            if roll == 1:
                continue  # natural 1 always misses: contributes 0
            if roll == 20:
                total += crit_damage * prob  # natural 20 always hits
            elif roll + self.attack_bonus >= self.target_ac:
                total += hit_damage * prob
        return total

    @classmethod
    def hypothesis_strategy(cls) -> SearchStrategy[MultiGroupAttackMechanic]:
        import hypothesis.strategies as st

        damage_types = ("slashing", "piercing", "fire", "poison")

        def _dice_group() -> SearchStrategy[DamageGroup]:
            def _build(count: int, sides: int, flat: int, dtype: str) -> DamageGroup:
                expr = f"{count}d{sides}"
                if flat != 0:
                    expr += f"+{flat}" if flat > 0 else str(flat)
                return DamageGroup(dice=expr, type=dtype)

            return st.builds(
                _build,
                count=st.integers(min_value=1, max_value=4),
                sides=st.sampled_from([4, 6, 8, 10, 12]),
                flat=st.integers(min_value=-5, max_value=10),
                dtype=st.sampled_from(damage_types),
            )

        def _defenses() -> SearchStrategy[Defenses]:
            tags = st.lists(st.sampled_from(damage_types), max_size=3, unique=True)
            return st.builds(Defenses, resist=tags, immune=tags, vulnerable=tags)

        return st.builds(
            cls,
            attack_bonus=st.integers(min_value=-5, max_value=15),
            target_ac=st.integers(min_value=5, max_value=30),
            damage=st.lists(_dice_group(), min_size=1, max_size=3).map(tuple),
            advantage_mode=st.sampled_from(_ADVANTAGE_MODES),
            target_defenses=_defenses(),
        )


@mechanics.register(CONCENTRATION_MECHANIC_ID)
@dataclass(slots=True)
class ConcentrationSaveMechanic(Mechanic):
    """A concentration check (PHB p.203): d20 + `con_bonus` against `dc`,
    resolving to ``1.0`` (concentration held) or ``0.0`` (broken). `dc` is
    the caller's own ``max(10, damage // 2)`` — this class only knows the
    roll, exactly as :class:`AttackDamageMechanic`'s `target_ac` is a
    caller-supplied scalar rather than a value it derives itself."""

    id: ClassVar[str] = CONCENTRATION_MECHANIC_ID

    con_bonus: int
    dc: int
    advantage_mode: AdvantageMode = "normal"

    def resolve(self, rng: BatchRNG, size: int) -> np.ndarray:
        d20 = roll_d20(rng, size, self.advantage_mode)
        return (d20 + self.con_bonus >= self.dc).astype(np.float64)

    def expected_value(self) -> float:
        probs = d20_face_probabilities(self.advantage_mode)
        return sum(
            prob
            for roll, prob in zip(range(1, 21), probs, strict=True)
            if roll + self.con_bonus >= self.dc
        )

    @classmethod
    def hypothesis_strategy(cls) -> SearchStrategy[ConcentrationSaveMechanic]:
        import hypothesis.strategies as st

        return st.builds(
            cls,
            con_bonus=st.integers(min_value=-2, max_value=15),
            dc=st.integers(min_value=5, max_value=30),
            advantage_mode=st.sampled_from(_ADVANTAGE_MODES),
        )


@mechanics.register(RECHARGE_MECHANIC_ID)
@dataclass(slots=True)
class RechargeMechanic(Mechanic):
    """A recharge roll (a statblock action's "(Recharge 5-6)" usage rider,
    parsed by :class:`~dndsim.rules.dnd5e_2014.attack_string.ActionUsage`):
    one d6, resolving to ``1.0`` (recharges) if it meets or beats
    `threshold`, else ``0.0``."""

    id: ClassVar[str] = RECHARGE_MECHANIC_ID

    threshold: int  # 1..6 — e.g. 5 for "Recharge 5-6"

    def resolve(self, rng: BatchRNG, size: int) -> np.ndarray:
        d6 = rng.integers(1, 7, size=size)
        return (d6 >= self.threshold).astype(np.float64)

    def expected_value(self) -> float:
        return max(0, 7 - self.threshold) / 6.0

    @classmethod
    def hypothesis_strategy(cls) -> SearchStrategy[RechargeMechanic]:
        import hypothesis.strategies as st

        return st.builds(cls, threshold=st.integers(min_value=1, max_value=6))
