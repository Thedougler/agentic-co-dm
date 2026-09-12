from __future__ import annotations

from collections.abc import Sequence

import pytest

from dndsim.core.policy import Candidate, Decision, Policy


def test_policy_cannot_be_instantiated_directly() -> None:
    with pytest.raises(TypeError):
        Policy(seed=1)  # type: ignore[abstract]


def test_a_complete_subclass_can_be_instantiated_and_used() -> None:
    class AlwaysFirst(Policy):
        id = "test:policy/always-first"

        def choose(self, candidates: Sequence[Candidate]) -> Decision:
            items = list(candidates)
            return Decision(chosen=items[0] if items else None)

    instance = AlwaysFirst(seed=1)
    assert instance.seed == 1
    candidate = Candidate(payload="only", declared_order=0, value=1.0)
    decision = instance.choose([candidate])
    assert decision.chosen is candidate
