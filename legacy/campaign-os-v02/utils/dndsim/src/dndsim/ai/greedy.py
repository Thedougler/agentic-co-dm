"""Greedy expected-value Policy (issue #44).

Argmaxes over each candidate's own stated ``value`` — nothing else. This is
the whole proof that the plugin boundary holds: the policy below never
names what a candidate *is*, so it values an option nobody taught it about
exactly as readily as one shipped in this file.
"""

from __future__ import annotations

from collections.abc import Sequence

from dndsim.core.policy import Candidate, Decision, Policy, policies

POLICY_ID = "dndsim:policy/greedy"


def _by_value_then_declared_order(candidate: Candidate) -> tuple[float, int]:
    assert candidate.value is not None
    return (candidate.value, -candidate.declared_order)


@policies.register(POLICY_ID)
class GreedyPolicy(Policy):
    """Chooses the candidate with the highest declared ``value``.

    Targeting is part of this argmax, not a separate rule: a caller that
    enumerates (action, target) pairs as distinct candidates gets both
    chosen together, in one comparison. Ties break by ``declared_order``
    (lowest wins) so behavior stays deterministic for a fixed candidate
    list.

    A candidate with ``value is None`` is planner-opaque (ADR-0008) and is
    excluded from the comparison — but never silently: every excluded
    candidate is returned in :attr:`~dndsim.core.policy.Decision.opaque`.
    If every candidate is opaque, :attr:`~dndsim.core.policy.Decision.chosen`
    is ``None`` rather than an arbitrary or zero-valued pick.
    """

    id = POLICY_ID

    def choose(self, candidates: Sequence[Candidate]) -> Decision:
        valued = [c for c in candidates if c.value is not None]
        opaque = tuple(c for c in candidates if c.value is None)
        if not valued:
            return Decision(chosen=None, opaque=opaque)
        best = max(valued, key=_by_value_then_declared_order)
        return Decision(chosen=best, opaque=opaque)
