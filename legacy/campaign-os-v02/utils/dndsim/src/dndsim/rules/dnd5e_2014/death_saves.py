"""Death saving throws (PHB p. 197) — a Divergence (issue #46; mechanism,
old/new behavior, and the measured win/TPK-rate effect are recorded in
``utils/dndsim/DIVERGENCES.md``).

dndsim implements the PHB mechanic: a combatant reduced to 0 HP falls Down
rather than losing outright, and — instead of acting on their turn — rolls an
unmodified d20 death saving throw (:class:`DeathSaveRollMechanic`): a
natural 1 counts as two failures, 2-9 is one failure, 10-19 is one
success, and a natural 20 is a critical success (they regain 1 HP and
stand back up, fully conscious). Three accumulated successes stabilizes
them (they stop rolling but remain Down, unconscious); three accumulated
failures kills them. Taking any damage while Down — stable or not —
inflicts one automatic failure and clears a stabilized combatant's
``stable`` flag, per the PHB rule that a stable creature which takes
damage resumes rolling.

Scope note: a critical hit landed on a Down combatant is not modeled as
inflicting two failures instead of one, and massive damage (damage at or
above HP maximum) does not trigger instant death. Both refinements need
the attack Mechanic itself to expose its own crit/miss decision, which
``mechanics.AttackDamageMechanic`` (a file outside this slice's scope)
does not currently do; each is a narrow, separately-scoped follow-up
rather than a silently dropped requirement.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

import numpy as np

from dndsim.core.mechanic import Mechanic, mechanics

if TYPE_CHECKING:
    from hypothesis.strategies import SearchStrategy

    from dndsim.core.resources import ResourcePool
    from dndsim.core.rng import BatchRNG

MECHANIC_ID = "dnd5e_2014:mechanic/death_save"

# DeathSaveRollMechanic's own outcome encoding — a per-roll result code,
# never combined with a raw d20 face value anywhere outside this module.
CRITICAL_FAILURE = -2.0  # natural 1: counts as two failures
FAILURE = -1.0  # 2-9
SUCCESS = 1.0  # 10-19
CRITICAL_SUCCESS = 3.0  # natural 20: regain 1 hp, stand up


@mechanics.register(MECHANIC_ID)
@dataclass(slots=True)
class DeathSaveRollMechanic(Mechanic):
    """One unmodified d20 death saving throw (PHB p. 197) — no ability
    modifier, no proficiency bonus, no advantage/disadvantage in the base
    rule (a condition granting either is a separate, later concern)."""

    id: ClassVar[str] = MECHANIC_ID

    def resolve(self, rng: BatchRNG, size: int) -> np.ndarray:
        d20 = rng.integers(1, 21, size=size)
        outcome = np.where(
            d20 == 1,
            CRITICAL_FAILURE,
            np.where(d20 == 20, CRITICAL_SUCCESS, np.where(d20 >= 10, SUCCESS, FAILURE)),
        )
        return outcome.astype(np.float64)

    def expected_value(self) -> float:
        return (CRITICAL_FAILURE * 1 + FAILURE * 8 + SUCCESS * 10 + CRITICAL_SUCCESS * 1) / 20.0

    @classmethod
    def hypothesis_strategy(cls) -> SearchStrategy[DeathSaveRollMechanic]:
        import hypothesis.strategies as st

        return st.builds(cls)


def scatter_bool(base_mask: np.ndarray, sub_bool: np.ndarray) -> np.ndarray:
    """Expand ``sub_bool`` (aligned to ``flatnonzero(base_mask)``, e.g. a
    Mechanic's per-active-universe outcome) back to ``base_mask``'s full
    batch shape."""
    out = np.zeros(base_mask.shape[0], dtype=bool)
    out[np.flatnonzero(base_mask)] = sub_bool
    return out


@dataclass(slots=True)
class DownedState:
    """Per-universe death-save bookkeeping for one combatant across a
    :class:`~dndsim.core.universe.UniverseBatch`. ``successes``/``failures``
    accumulate (not consecutive — PHB); ``stable`` and ``dead`` are
    terminal once set, except that taking damage while ``stable`` clears
    it again (:func:`apply_damage_while_down`)."""

    down: np.ndarray
    stable: np.ndarray
    dead: np.ndarray
    successes: np.ndarray
    failures: np.ndarray

    @classmethod
    def empty(cls, size: int) -> DownedState:
        return cls(
            down=np.zeros(size, dtype=bool),
            stable=np.zeros(size, dtype=bool),
            dead=np.zeros(size, dtype=bool),
            successes=np.zeros(size, dtype=np.int32),
            failures=np.zeros(size, dtype=np.int32),
        )


def enter_down(state: DownedState, mask: np.ndarray) -> None:
    """Newly reduced to 0 HP: fall Down with a clean set of death saves."""
    if not bool(mask.any()):
        return
    state.down[mask] = True
    state.stable[mask] = False
    state.successes[mask] = 0
    state.failures[mask] = 0


def apply_damage_while_down(state: DownedState, mask: np.ndarray) -> None:
    """A hit landed on an already-Down combatant: one automatic failure,
    and — if they were stable — they resume rolling (PHB p. 198)."""
    target = mask & state.down & ~state.dead
    if not bool(target.any()):
        return
    state.stable[target] = False
    state.failures[target] += 1
    state.dead |= state.down & (state.failures >= 3)


def roll_death_saves(state: DownedState, rng: BatchRNG, mask: np.ndarray, hp: ResourcePool) -> None:
    """Advance one death saving throw for every Down, not-stable, not-dead
    combatant selected by ``mask`` — their turn's action in place of an
    attack. A critical success restores 1 HP and clears Down entirely."""
    active = mask & state.down & ~state.stable & ~state.dead
    n = int(active.sum())
    if n == 0:
        return
    outcome = DeathSaveRollMechanic().resolve(rng, n)

    crit_fail = scatter_bool(active, outcome == CRITICAL_FAILURE)
    fail = scatter_bool(active, outcome == FAILURE)
    success = scatter_bool(active, outcome == SUCCESS)
    crit_success = scatter_bool(active, outcome == CRITICAL_SUCCESS)

    state.failures[crit_fail] += 2
    state.failures[fail] += 1
    state.successes[success] += 1

    if bool(crit_success.any()):
        state.down[crit_success] = False
        state.stable[crit_success] = False
        state.successes[crit_success] = 0
        state.failures[crit_success] = 0
        hp.restore(np.ones(int(crit_success.sum()), dtype=np.float64), crit_success)

    state.dead |= state.down & (state.failures >= 3)
    state.stable |= state.down & ~state.dead & (state.successes >= 3)
