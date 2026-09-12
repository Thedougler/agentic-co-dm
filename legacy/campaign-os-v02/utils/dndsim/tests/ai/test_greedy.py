from __future__ import annotations

from dndsim.ai.greedy import GreedyPolicy
from dndsim.core.policy import Candidate


def test_greedy_chooses_highest_value() -> None:
    policy = GreedyPolicy(seed=1)
    candidates = [
        Candidate(payload="low", declared_order=0, value=1.0),
        Candidate(payload="high", declared_order=1, value=5.0),
        Candidate(payload="mid", declared_order=2, value=3.0),
    ]
    decision = policy.choose(candidates)
    assert decision.chosen is not None
    assert decision.chosen.payload == "high"
    assert decision.opaque == ()


def test_greedy_ties_break_by_declared_order() -> None:
    policy = GreedyPolicy(seed=1)
    candidates = [
        Candidate(payload="second", declared_order=1, value=5.0),
        Candidate(payload="first", declared_order=0, value=5.0),
    ]
    decision = policy.choose(candidates)
    assert decision.chosen is not None
    assert decision.chosen.payload == "first"


def test_greedy_excludes_opaque_candidates_explicitly() -> None:
    """Planner-opaque (ADR-0008) never means 'valued at zero': it is
    reported separately, and never chosen over a valued alternative."""
    policy = GreedyPolicy(seed=1)
    opaque_candidate = Candidate(payload="mystery", declared_order=0, value=None)
    valued_candidate = Candidate(payload="known", declared_order=1, value=-100.0)
    decision = policy.choose([opaque_candidate, valued_candidate])
    assert decision.chosen is not None
    assert decision.chosen.payload == "known"
    assert decision.opaque == (opaque_candidate,)


def test_greedy_all_opaque_chooses_none_not_zero() -> None:
    policy = GreedyPolicy(seed=1)
    opaque_candidate = Candidate(payload="mystery", declared_order=0, value=None)
    decision = policy.choose([opaque_candidate])
    assert decision.chosen is None
    assert decision.opaque == (opaque_candidate,)


def test_greedy_empty_candidates_chooses_none() -> None:
    policy = GreedyPolicy(seed=1)
    decision = policy.choose([])
    assert decision.chosen is None
    assert decision.opaque == ()


def test_greedy_values_a_candidate_it_was_never_taught_about() -> None:
    """The planner has no branch keyed on what a candidate's payload is —
    it only compares the ``value`` each candidate already carries
    (ADR-0008), so an entirely novel payload type is valued exactly like
    any other."""
    policy = GreedyPolicy(seed=1)
    candidates = [
        Candidate(payload=object(), declared_order=0, value=9.0),
        Candidate(payload=object(), declared_order=1, value=1.0),
    ]
    decision = policy.choose(candidates)
    assert decision.chosen is candidates[0]
