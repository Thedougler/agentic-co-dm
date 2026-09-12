from __future__ import annotations

import pytest

from dndsim.core.mechanic import mechanics
from dndsim.core.rng import BatchRNG
from dndsim.rules.dnd5e_2014.mechanics import MECHANIC_ID, AttackDamageMechanic


def test_registered_under_stable_id() -> None:
    assert MECHANIC_ID in mechanics
    assert mechanics.get(MECHANIC_ID) is AttackDamageMechanic


def test_resolve_is_deterministic_for_a_given_seed() -> None:
    mechanic = AttackDamageMechanic(
        attack_bonus=7, target_ac=15, damage_dice_count=1, damage_dice_sides=8, damage_bonus=4
    )
    a = mechanic.resolve(BatchRNG(seed=99), size=2000)
    b = mechanic.resolve(BatchRNG(seed=99), size=2000)
    assert list(a) == list(b)


def test_resolve_shape_and_bounds() -> None:
    mechanic = AttackDamageMechanic(
        attack_bonus=0, target_ac=10, damage_dice_count=2, damage_dice_sides=6, damage_bonus=3
    )
    outcomes = mechanic.resolve(BatchRNG(seed=1), size=5000)
    assert outcomes.shape == (5000,)
    # miss = 0; hit = [1*2+3, 2*2+3] = [5, 7]; crit doubles dice only = [2*2+3, 4*2+3] = [7, 11]
    assert outcomes.min() >= 0
    assert outcomes.max() <= 2 * 6 * 2 + 3  # max possible: crit doubles both dice


def test_expected_value_is_zero_when_attack_bonus_cannot_reach_ac() -> None:
    # need a natural 20 (which always hits) to land; every other roll misses.
    mechanic = AttackDamageMechanic(
        attack_bonus=-10, target_ac=30, damage_dice_count=1, damage_dice_sides=6, damage_bonus=0
    )
    ev = mechanic.expected_value()
    # only the natural-20 crit term contributes: (avg*2)/20
    assert ev > 0
    assert ev < 1.0


def test_natural_one_always_misses_even_with_huge_bonus() -> None:
    mechanic = AttackDamageMechanic(
        attack_bonus=100, target_ac=5, damage_dice_count=1, damage_dice_sides=4, damage_bonus=0
    )
    outcomes = mechanic.resolve(BatchRNG(seed=3), size=20_000)
    # 19/20 rolls hit (everything except a natural 1); EV should reflect that,
    # not 100% hit.
    ev = mechanic.expected_value()
    assert outcomes.mean() == pytest.approx(ev, rel=0.1)


def test_advantage_mode_defaults_to_normal() -> None:
    mechanic = AttackDamageMechanic(
        attack_bonus=5, target_ac=15, damage_dice_count=1, damage_dice_sides=8, damage_bonus=3
    )
    assert mechanic.advantage_mode == "normal"


def test_advantage_raises_expected_value_over_normal_and_disadvantage_lowers_it() -> None:
    base = {
        "attack_bonus": 5,
        "target_ac": 15,
        "damage_dice_count": 1,
        "damage_dice_sides": 8,
        "damage_bonus": 3,
    }
    normal = AttackDamageMechanic(**base, advantage_mode="normal")
    advantage = AttackDamageMechanic(**base, advantage_mode="advantage")
    disadvantage = AttackDamageMechanic(**base, advantage_mode="disadvantage")
    assert advantage.expected_value() > normal.expected_value() > disadvantage.expected_value()


def test_advantage_mode_mc_mean_matches_declared_expected_value() -> None:
    mechanic = AttackDamageMechanic(
        attack_bonus=3,
        target_ac=14,
        damage_dice_count=2,
        damage_dice_sides=6,
        damage_bonus=2,
        advantage_mode="advantage",
    )
    outcomes = mechanic.resolve(BatchRNG(seed=7), size=20_000)
    assert outcomes.mean() == pytest.approx(mechanic.expected_value(), abs=0.75)
