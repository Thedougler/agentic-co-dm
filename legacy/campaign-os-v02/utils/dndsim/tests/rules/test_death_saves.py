from __future__ import annotations

import numpy as np
import pytest

import dndsim.rules.dnd5e_2014.death_saves as death_saves_module
from dndsim.core.resources import ResourcePool
from dndsim.core.rng import BatchRNG
from dndsim.rules.dnd5e_2014.death_saves import (
    CRITICAL_FAILURE,
    CRITICAL_SUCCESS,
    FAILURE,
    SUCCESS,
    DeathSaveRollMechanic,
    DownedState,
    apply_damage_while_down,
    enter_down,
    roll_death_saves,
    scatter_bool,
)


def _fixed_roll(outcome_code: float) -> type[DeathSaveRollMechanic]:
    """A stand-in Mechanic whose ``resolve`` always returns ``outcome_code`` —
    for pinning a single death-save outcome deterministically in a test,
    since :class:`DeathSaveRollMechanic` itself draws a real d20."""

    class _Fixed(DeathSaveRollMechanic):
        def resolve(self, rng: BatchRNG, size: int) -> np.ndarray:
            return np.full(size, outcome_code, dtype=np.float64)

    return _Fixed


def test_death_save_roll_only_emits_the_four_outcome_codes() -> None:
    rng = BatchRNG(seed=1)
    outcome = DeathSaveRollMechanic().resolve(rng, size=20_000)
    expected = {CRITICAL_FAILURE, FAILURE, SUCCESS, CRITICAL_SUCCESS}
    assert set(np.unique(outcome).tolist()) == expected


def test_death_save_roll_face_frequencies_match_a_fair_d20() -> None:
    rng = BatchRNG(seed=1)
    outcome = DeathSaveRollMechanic().resolve(rng, size=200_000)
    crit_fail_rate = float((outcome == CRITICAL_FAILURE).mean())
    crit_success_rate = float((outcome == CRITICAL_SUCCESS).mean())
    success_rate = float((outcome == SUCCESS).mean())
    failure_rate = float((outcome == FAILURE).mean())
    assert abs(crit_fail_rate - 1 / 20) < 0.01
    assert abs(crit_success_rate - 1 / 20) < 0.01
    assert abs(success_rate - 10 / 20) < 0.01
    assert abs(failure_rate - 8 / 20) < 0.01


def test_scatter_bool_expands_back_to_full_batch_shape() -> None:
    base_mask = np.array([True, False, True, True, False])
    sub_bool = np.array([True, False, True])  # aligned to flatnonzero(base_mask)
    expanded = scatter_bool(base_mask, sub_bool)
    assert expanded.tolist() == [True, False, False, True, False]


def test_enter_down_resets_counters_and_sets_down() -> None:
    state = DownedState.empty(3)
    state.successes[:] = [2, 2, 2]
    state.failures[:] = [1, 1, 1]
    enter_down(state, np.array([True, False, True]))
    assert state.down.tolist() == [True, False, True]
    assert state.successes.tolist() == [0, 2, 0]
    assert state.failures.tolist() == [0, 1, 0]


def test_three_successes_stabilize_a_downed_combatant() -> None:
    size = 20_000
    state = DownedState.empty(size)
    hp = ResourcePool("hp", np.zeros(size, dtype=np.float64))
    enter_down(state, np.ones(size, dtype=bool))
    rng = BatchRNG(seed=42)

    for _ in range(60):  # plenty of rounds for every universe to resolve
        roll_death_saves(state, rng, np.ones(size, dtype=bool), hp)

    # Every universe reaches a terminal outcome: stabilized, dead, or a
    # natural-20 wake-up (``down`` cleared back to False).
    assert bool((state.stable | state.dead | ~state.down).all())
    # All three outcomes must occur given a fair d20 across 20,000 universes.
    assert bool(state.stable.any())
    assert bool(state.dead.any())
    assert bool((~state.down).any())


def test_three_failures_kill_a_downed_combatant_with_no_successes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    size = 1
    state = DownedState.empty(size)
    hp = ResourcePool("hp", np.zeros(size, dtype=np.float64))
    enter_down(state, np.array([True]))
    state.failures[:] = [2]  # one more failure is lethal

    monkeypatch.setattr(death_saves_module, "DeathSaveRollMechanic", _fixed_roll(FAILURE))
    roll_death_saves(state, BatchRNG(seed=1), np.array([True]), hp)

    assert state.dead.tolist() == [True]
    assert state.failures.tolist() == [3]


def test_natural_20_wakes_the_combatant_and_restores_one_hp(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    size = 1
    state = DownedState.empty(size)
    hp = ResourcePool("hp", np.array([10.0]))
    hp.current[:] = 0.0
    enter_down(state, np.array([True]))

    monkeypatch.setattr(death_saves_module, "DeathSaveRollMechanic", _fixed_roll(CRITICAL_SUCCESS))
    roll_death_saves(state, BatchRNG(seed=1), np.array([True]), hp)

    assert state.down.tolist() == [False]
    assert state.dead.tolist() == [False]
    assert hp.current.tolist() == [1.0]


def test_natural_1_counts_as_two_failures(monkeypatch: pytest.MonkeyPatch) -> None:
    size = 1
    state = DownedState.empty(size)
    hp = ResourcePool("hp", np.zeros(size, dtype=np.float64))
    enter_down(state, np.array([True]))

    monkeypatch.setattr(death_saves_module, "DeathSaveRollMechanic", _fixed_roll(CRITICAL_FAILURE))
    roll_death_saves(state, BatchRNG(seed=1), np.array([True]), hp)

    assert state.failures.tolist() == [2]
    assert state.dead.tolist() == [False]  # 2 failures is not yet lethal


def test_damage_while_down_inflicts_one_failure_and_clears_stable() -> None:
    state = DownedState.empty(2)
    enter_down(state, np.array([True, True]))
    state.stable[:] = [True, True]
    state.successes[:] = [3, 3]

    apply_damage_while_down(state, np.array([True, False]))

    assert state.stable.tolist() == [False, True]
    assert state.failures.tolist() == [1, 0]


def test_damage_while_down_can_kill_at_three_accumulated_failures() -> None:
    state = DownedState.empty(1)
    enter_down(state, np.array([True]))
    state.failures[:] = [2]

    apply_damage_while_down(state, np.array([True]))

    assert state.dead.tolist() == [True]
    assert state.failures.tolist() == [3]


def test_apply_damage_while_down_is_a_noop_for_a_combatant_not_down() -> None:
    state = DownedState.empty(1)  # never entered Down
    apply_damage_while_down(state, np.array([True]))
    assert state.failures.tolist() == [0]
    assert state.dead.tolist() == [False]


def test_roll_death_saves_ignores_universes_outside_the_mask() -> None:
    size = 2
    state = DownedState.empty(size)
    hp = ResourcePool("hp", np.zeros(size, dtype=np.float64))
    enter_down(state, np.array([True, True]))
    before_successes = state.successes.copy()
    before_failures = state.failures.copy()

    roll_death_saves(state, BatchRNG(seed=1), np.array([True, False]), hp)

    assert state.successes[1] == before_successes[1]
    assert state.failures[1] == before_failures[1]
