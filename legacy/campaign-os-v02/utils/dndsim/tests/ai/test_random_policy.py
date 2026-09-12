from __future__ import annotations

from dndsim.ai.random_policy import RandomPolicy
from dndsim.core.policy import Candidate


def _candidates() -> list[Candidate]:
    return [Candidate(payload=i, declared_order=i, value=float(i)) for i in range(5)]


def test_random_same_seed_reproduces_same_decisions() -> None:
    first = RandomPolicy(seed=7)
    second = RandomPolicy(seed=7)
    picks_first = [first.choose(_candidates()).chosen for _ in range(10)]
    picks_second = [second.choose(_candidates()).chosen for _ in range(10)]
    payloads_first = [c.payload if c is not None else None for c in picks_first]
    payloads_second = [c.payload if c is not None else None for c in picks_second]
    assert payloads_first == payloads_second


def test_random_visits_more_than_one_candidate_across_draws() -> None:
    policy = RandomPolicy(seed=7)
    picks = set()
    for _ in range(50):
        decision = policy.choose(_candidates())
        assert decision.chosen is not None
        picks.add(decision.chosen.payload)
    assert len(picks) > 1


def test_random_empty_candidates_chooses_none() -> None:
    policy = RandomPolicy(seed=1)
    decision = policy.choose([])
    assert decision.chosen is None
