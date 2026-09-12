"""Difficulty drivers (issue #54): "why is this encounter Deadly" — probe
each of :mod:`dndsim.rules.dnd5e_2014.knobs`'s ``MUTATION_KNOBS`` one at a
time, in the direction that weakens the enemy, and rank by how much each
single knob moves party win probability. Reuses knobs.py's exact
delta/step machinery — no separate mutation model to keep in sync with the
GA.

Every knob weakens the enemy in the same signed direction (dir=-1): lower
AC/HP/to-hit/damage, fewer attacks, less speed. A single probe per knob is
enough to see whether weakening it helps.
"""

from __future__ import annotations

from dataclasses import dataclass

from dndsim.core.rng import cell_seed
from dndsim.core.universe import UniverseBatch
from dndsim.rules.dnd5e_2014.combat import CombatResult, run_combat
from dndsim.rules.dnd5e_2014.fixture import CombatantSpec
from dndsim.rules.dnd5e_2014.knobs import (
    MUTATION_KNOBS,
    apply_delta,
    clamp_delta,
    describe_delta,
    knob_delta,
)

DEFAULT_DRIVER_PROBE_UNIVERSES = 1500

# A knob only counts as a real "driver" if weakening it alone swings win
# probability by at least this many percentage points (rejects probe-noise
# swings), OR by at least MATERIAL_WIN_RELATIVE_LIFT of the baseline
# itself, whichever is larger — a flat pp bar alone under-flags low-
# baseline fights. Matches sensitivity.mjs's isMaterialWinDelta exactly.
MATERIAL_WIN_DELTA = 0.05
MATERIAL_WIN_RELATIVE_LIFT = 0.30
MATERIAL_WIN_NOISE_FLOOR = 0.02


def is_material_win_delta(delta_win: float, baseline_win_probability: float) -> bool:
    """Whether a single knob's win-probability swing clears the
    materiality bar against a given baseline."""
    return delta_win >= MATERIAL_WIN_NOISE_FLOOR and (
        delta_win >= MATERIAL_WIN_DELTA
        or delta_win >= baseline_win_probability * MATERIAL_WIN_RELATIVE_LIFT
    )


@dataclass(frozen=True, slots=True)
class DriverProbe:
    knob: str
    delta_text: str
    delta_win: float
    delta_tpk: float
    delta_any_down: float
    delta_rounds: float


@dataclass(frozen=True, slots=True)
class DriverBaseline:
    win_probability: float
    tpk_probability: float
    any_down_probability: float
    rounds_mean: float


@dataclass(frozen=True, slots=True)
class DriverRanking:
    baseline: DriverBaseline
    drivers: tuple[DriverProbe, ...]
    primary_driver: DriverProbe | None
    note: str | None


_NO_DRIVER_NOTE = (
    "no standard knob (AC/HP/to-hit/damage/multiattack/speed) materially "
    "moves the outcome on its own — inspect this creature's custom traits "
    "by hand (a save-based rider, an aura, a summon); see the knobs.py "
    "module docstring for the knobs this port does not yet mutate."
)


def rank_drivers(
    party: list[CombatantSpec],
    enemies: list[CombatantSpec],
    target_index: int,
    *,
    seed: int,
    round_cap: int = 20,
    policy_id: str = "dndsim:policy/greedy",
    probe_universes: int = DEFAULT_DRIVER_PROBE_UNIVERSES,
) -> DriverRanking:
    """Rank each mutation knob by how much weakening it alone would improve
    the party's win probability against ``enemies[target_index]``."""
    target_statblock = enemies[target_index].compiled
    if target_statblock is None:
        raise ValueError("sensitivity.rank_drivers: target combatant has no compiled statblock")

    def simulate(cell_key: str, enemy_list: list[CombatantSpec]) -> CombatResult:
        batch = UniverseBatch(size=probe_universes, seed=cell_seed(seed, cell_key))
        return run_combat(party, enemy_list, batch, round_cap=round_cap, policy_id=policy_id)

    baseline_result = simulate("drivers:baseline", enemies)

    drivers: list[DriverProbe] = []
    for knob in MUTATION_KNOBS:
        delta = clamp_delta({knob: knob_delta(target_statblock, knob, -1)}, target_statblock)
        if not delta:
            continue  # already at its bound
        mutated = apply_delta(enemies[target_index], delta)
        probe_enemies = [mutated if i == target_index else e for i, e in enumerate(enemies)]
        result = simulate(f"drivers:{knob}", probe_enemies)
        drivers.append(
            DriverProbe(
                knob=knob,
                delta_text=describe_delta(target_statblock, delta),
                delta_win=result.party_win_rate - baseline_result.party_win_rate,
                delta_tpk=result.tpk_probability - baseline_result.tpk_probability,
                delta_any_down=result.any_down_probability - baseline_result.any_down_probability,
                delta_rounds=result.mean_rounds - baseline_result.mean_rounds,
            )
        )
    drivers.sort(key=lambda d: d.delta_win, reverse=True)

    top = drivers[0] if drivers else None
    primary = (
        top
        if top is not None and is_material_win_delta(top.delta_win, baseline_result.party_win_rate)
        else None
    )

    return DriverRanking(
        baseline=DriverBaseline(
            win_probability=baseline_result.party_win_rate,
            tpk_probability=baseline_result.tpk_probability,
            any_down_probability=baseline_result.any_down_probability,
            rounds_mean=baseline_result.mean_rounds,
        ),
        drivers=tuple(drivers),
        primary_driver=primary,
        note=None if primary is not None else _NO_DRIVER_NOTE,
    )
