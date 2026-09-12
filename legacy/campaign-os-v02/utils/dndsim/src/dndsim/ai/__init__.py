"""Concrete Policies (issue #44): greedy expected-value, routine, and random.

Every Policy defined under this package holds zero rules vocabulary — see
``dndsim.core.policy`` for the boundary that makes that possible: each one
compares or orders :class:`~dndsim.core.policy.Candidate` values it was
handed, never anything it inferred about what a candidate represents.
Registered through the ``dndsim.policies`` entry-point group declared in
``pyproject.toml`` — the same mechanism an out-of-tree package uses to add
its own Policy with no engine edit.
"""

from __future__ import annotations


def register() -> None:
    """Entry point target: importing these modules runs their decorators."""
    from dndsim.ai import greedy as _greedy  # noqa: F401
    from dndsim.ai import random_policy as _random_policy  # noqa: F401
    from dndsim.ai import routine as _routine  # noqa: F401
