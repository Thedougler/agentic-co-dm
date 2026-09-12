"""Random Policy (issue #44).

Chooses uniformly among the available candidates, ignoring ``value`` and
``declared_order`` alike. Determinism rests on the same rule as the rest of
the engine's RNG story (``dndsim.core.rng``): one seeded generator, drawn
from in call order — identical seed plus identical call sequence produces
identical picks.
"""

from __future__ import annotations

from collections.abc import Sequence

from dndsim.core.policy import Candidate, Decision, Policy, policies
from dndsim.core.rng import BatchRNG

POLICY_ID = "dndsim:policy/random"


@policies.register(POLICY_ID)
class RandomPolicy(Policy):
    """Draws one candidate uniformly at random from whatever is offered."""

    id = POLICY_ID

    def __init__(self, seed: int) -> None:
        super().__init__(seed)
        self._rng = BatchRNG(seed)

    def choose(self, candidates: Sequence[Candidate]) -> Decision:
        if not candidates:
            return Decision(chosen=None)
        index = int(self._rng.integers(0, len(candidates), size=1)[0])
        return Decision(chosen=candidates[index])
