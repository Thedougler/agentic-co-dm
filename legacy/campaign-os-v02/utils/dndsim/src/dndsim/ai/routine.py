"""Fixed routine Policy (issue #44).

Executes a declared order rather than an expected value: whichever
candidate its caller enumerated first, every time. This is what "targeting
is part of the argmax under greedy, but declaration order governs under
routine" means concretely — the same ``declared_order`` field the greedy
Policy uses only to break ties is, here, the entire decision rule.
"""

from __future__ import annotations

from collections.abc import Sequence

from dndsim.core.policy import Candidate, Decision, Policy, policies

POLICY_ID = "dndsim:policy/routine"


@policies.register(POLICY_ID)
class RoutinePolicy(Policy):
    """Chooses the candidate with the lowest ``declared_order``, ignoring
    ``value`` entirely — a fixed order executes regardless of how good or
    bad any option looks."""

    id = POLICY_ID

    def choose(self, candidates: Sequence[Candidate]) -> Decision:
        if not candidates:
            return Decision(chosen=None)
        chosen = min(candidates, key=lambda c: c.declared_order)
        return Decision(chosen=chosen)
