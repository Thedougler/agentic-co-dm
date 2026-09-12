from __future__ import annotations

from dndsim.ai.routine import RoutinePolicy
from dndsim.core.policy import Candidate


def test_routine_ignores_value_and_follows_declared_order() -> None:
    policy = RoutinePolicy(seed=1)
    candidates = [
        Candidate(payload="declared-first", declared_order=0, value=1.0),
        Candidate(payload="highest-value", declared_order=1, value=99.0),
    ]
    decision = policy.choose(candidates)
    assert decision.chosen is not None
    assert decision.chosen.payload == "declared-first"


def test_routine_follows_declared_order_regardless_of_list_position() -> None:
    policy = RoutinePolicy(seed=1)
    candidates = [
        Candidate(payload="listed-first-declared-second", declared_order=1, value=1.0),
        Candidate(payload="listed-second-declared-first", declared_order=0, value=1.0),
    ]
    decision = policy.choose(candidates)
    assert decision.chosen is not None
    assert decision.chosen.payload == "listed-second-declared-first"


def test_routine_empty_candidates_chooses_none() -> None:
    policy = RoutinePolicy(seed=1)
    decision = policy.choose([])
    assert decision.chosen is None
