from __future__ import annotations

import numpy as np
import pytest

from dndsim.core.mechanic import mechanics
from dndsim.core.rng import BatchRNG
from dndsim.core.tags import BatchTags
from dndsim.rules.dnd5e_2014.effects import EffectTracker, check_concentration_and_break
from dndsim.rules.dnd5e_2014.mechanics import (
    CONCENTRATION_MECHANIC_ID,
    RECHARGE_MECHANIC_ID,
    ConcentrationSaveMechanic,
    RechargeMechanic,
)


def test_concentration_mechanic_registered_under_stable_id() -> None:
    assert CONCENTRATION_MECHANIC_ID in mechanics
    assert mechanics.get(CONCENTRATION_MECHANIC_ID) is ConcentrationSaveMechanic


def test_recharge_mechanic_registered_under_stable_id() -> None:
    assert RECHARGE_MECHANIC_ID in mechanics
    assert mechanics.get(RECHARGE_MECHANIC_ID) is RechargeMechanic


def test_concentration_check_dc10_and_dc11_pass_rates_match_reference_engine() -> None:
    # Pinned pass rates: bonus
    # +3, DC 10 needs a 7+ (0.70 pass rate), DC 11 needs an 8+ (0.65).
    n = 20_000
    dc10 = ConcentrationSaveMechanic(con_bonus=3, dc=10)
    dc11 = ConcentrationSaveMechanic(con_bonus=3, dc=11)
    pass10 = dc10.resolve(BatchRNG(seed=1), size=n).mean()
    pass11 = dc11.resolve(BatchRNG(seed=2), size=n).mean()
    assert pass10 == pytest.approx(0.70, abs=0.02)
    assert pass11 == pytest.approx(0.65, abs=0.02)
    assert dc10.expected_value() == pytest.approx(0.70, abs=1e-9)
    assert dc11.expected_value() == pytest.approx(0.65, abs=1e-9)


def test_recharge_mechanic_probability_matches_threshold() -> None:
    # "Recharge 5-6" -> threshold=5 -> 2/6 chance.
    mechanic = RechargeMechanic(threshold=5)
    assert mechanic.expected_value() == pytest.approx(2 / 6)
    outcomes = mechanic.resolve(BatchRNG(seed=11), size=20_000)
    assert outcomes.mean() == pytest.approx(2 / 6, abs=0.02)


def test_recharge_mechanic_threshold_one_always_recharges() -> None:
    mechanic = RechargeMechanic(threshold=1)
    assert mechanic.expected_value() == 1.0
    outcomes = mechanic.resolve(BatchRNG(seed=12), size=1000)
    assert outcomes.min() == 1.0


def test_check_concentration_and_break_removes_exactly_its_own_effects() -> None:
    size = 4
    tags = BatchTags(size)
    tracker = EffectTracker(tags=tags, size=size)
    all_mask = np.ones(size, dtype=np.bool_)

    # caster's concentration spell (bless) applied to every universe
    tracker.apply(source="conc:caster", tag="blessed", mask=all_mask, duration_rounds=None)
    # an unrelated, non-concentration effect (a paralyzing trap) stays put
    tracker.apply(source="trap:1", tag="paralyzed", mask=all_mask, duration_rounds=3)

    assert tags.has("blessed").all()
    assert tags.has("paralyzed").all()

    # very low CON bonus, huge damage -> guaranteed to fail every check
    damage = np.full(size, 40.0)
    broke = check_concentration_and_break(
        tracker=tracker,
        owner_id="caster",
        damage=damage,
        concentrating_mask=all_mask,
        con_bonus=-5,
        advantage_mode="normal",
        rng=BatchRNG(seed=3),
    )
    assert broke.all()
    # concentration-sourced effect is gone everywhere...
    assert not tags.has("blessed").any()
    # ...but the unrelated effect survives untouched.
    assert tags.has("paralyzed").all()


def test_check_concentration_and_break_only_breaks_failing_universes() -> None:
    size = 5000
    tags = BatchTags(size)
    tracker = EffectTracker(tags=tags, size=size)
    all_mask = np.ones(size, dtype=np.bool_)
    tracker.apply(source="conc:caster", tag="blessed", mask=all_mask, duration_rounds=None)

    # DC 10, +3 bonus: ~0.70 pass rate (reference-matched above) -> some
    # universes keep concentration, some break it.
    damage = np.full(size, 8.0)  # dc = max(10, 8//2) = 10
    broke = check_concentration_and_break(
        tracker=tracker,
        owner_id="caster",
        damage=damage,
        concentrating_mask=all_mask,
        con_bonus=3,
        advantage_mode="normal",
        rng=BatchRNG(seed=4),
    )
    assert 0.0 < broke.mean() < 1.0
    # exactly the broken universes lost the tag; the rest kept it.
    assert np.array_equal(tags.has("blessed"), ~broke)
