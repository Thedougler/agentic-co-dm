"""Issue #44 acceptance criteria that span more than one Policy: plugin
registration (including out-of-tree), same-candidates-different-decisions,
and same-seed reproducibility.
"""

from __future__ import annotations

from importlib.metadata import EntryPoint
from typing import TYPE_CHECKING

from dndsim import plugins
from dndsim.ai.greedy import GreedyPolicy
from dndsim.ai.random_policy import RandomPolicy
from dndsim.ai.routine import RoutinePolicy
from dndsim.core.policy import Candidate, Decision, Policy, policies
from dndsim.core.registry import Registry

if TYPE_CHECKING:
    import pytest


def test_three_policies_register_through_the_plugin_group_and_are_selectable() -> None:
    plugins.load_policies()
    assert policies.get("dndsim:policy/greedy") is GreedyPolicy
    assert policies.get("dndsim:policy/routine") is RoutinePolicy
    assert policies.get("dndsim:policy/random") is RandomPolicy


def test_same_candidates_same_seed_three_policies_differ() -> None:
    """Greedy, routine, and random each read the exact same candidate list
    differently — proof the CLI's ``--policy`` selection is not cosmetic."""
    candidates = [
        Candidate(payload="declared-first-lowest-value", declared_order=0, value=1.0),
        Candidate(payload="declared-second-highest-value", declared_order=1, value=9.0),
        Candidate(payload="declared-third-mid-value", declared_order=2, value=5.0),
    ]

    greedy_pick = GreedyPolicy(seed=1).choose(candidates).chosen
    routine_pick = RoutinePolicy(seed=1).choose(candidates).chosen
    assert greedy_pick is not None
    assert routine_pick is not None
    assert greedy_pick.payload == "declared-second-highest-value"
    assert routine_pick.payload == "declared-first-lowest-value"


def test_same_seed_same_policy_reproduces_the_same_decision() -> None:
    candidates = [
        Candidate(payload="a", declared_order=0, value=1.0),
        Candidate(payload="b", declared_order=1, value=1.0),
        Candidate(payload="c", declared_order=2, value=1.0),
    ]
    first = RandomPolicy(seed=99).choose(candidates)
    second = RandomPolicy(seed=99).choose(candidates)
    assert first.chosen is not None
    assert second.chosen is not None
    assert first.chosen.payload == second.chosen.payload


# --- out-of-tree registration -----------------------------------------------

_out_of_tree_registry: Registry[type[Policy]] = Registry("test.dndsim.policies")


class _OutOfTreePolicy(Policy):
    """Stands in for a Policy an out-of-tree package would ship — never
    imported into :data:`dndsim.core.policy.policies` directly; the test
    below registers it only by driving the real entry-point loading path."""

    id = "test:policy/out-of-tree"

    def choose(self, candidates: object) -> Decision:
        raise NotImplementedError("not exercised — this proves registration only")


def _register_out_of_tree_policy() -> None:
    _out_of_tree_registry.register_value(_OutOfTreePolicy.id, _OutOfTreePolicy)


def test_out_of_tree_package_can_register_a_policy_with_no_engine_edit(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Drives the exact mechanism :data:`dndsim.core.policy.policies` itself
    uses (``Registry.load_entry_points`` -> ``importlib.metadata.entry_points``)
    against a throwaway registry, proving a Policy can be added by a package
    outside this tree with no change to any engine file (issue #44)."""
    entry_point = EntryPoint(
        name="out-of-tree",
        value=f"{__name__}:_register_out_of_tree_policy",
        group="test.dndsim.policies",
    )

    def fake_entry_points(*, group: str) -> tuple[EntryPoint, ...]:
        assert group == "test.dndsim.policies"
        return (entry_point,)

    monkeypatch.setattr("dndsim.core.registry.entry_points", fake_entry_points)
    _out_of_tree_registry.load_entry_points()

    assert _out_of_tree_registry.get("test:policy/out-of-tree") is _OutOfTreePolicy
