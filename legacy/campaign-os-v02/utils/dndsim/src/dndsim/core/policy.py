"""The Policy contract: a pluggable decision-maker choosing among candidates.

Every Policy is one class exposing :meth:`Policy.choose`, which selects
among a list of :class:`Candidate` instances that its caller has already
assembled and, where tractable, already valued. This is deliberate: a
Policy never constructs its own worth for an option — a Candidate's
``value`` is supplied at the boundary by whatever assembled the option
list (in production, a Rules pack's turn-resolution code calling a
Mechanic's own ``expected_value()``, per ADR-0008; in isolation, a test
fixture). That boundary is what keeps every concrete Policy free of domain
vocabulary: an expected-value-maximizing Policy compares floats it was
handed, never anything it inferred about what an option represents.
``payload`` is likewise opaque here — a Policy returns it unexamined.

``value`` is ``None`` exactly when the candidate is planner-opaque
(ADR-0008): the Mechanic behind it declared no tractable closed form. A
``None`` must never be read as a worst-case numeric value — see
:class:`Decision`.

Registered through the ``dndsim.policies`` entry-point group (see
``pyproject.toml``), so an out-of-tree package can add a Policy with no
change to this module or to any other engine file (issue #44 acceptance
criterion).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass
from typing import ClassVar

from dndsim.core.registry import Registry


@dataclass(frozen=True, slots=True)
class Candidate:
    """One option a Policy may choose.

    ``declared_order`` is this candidate's position in the order its
    caller enumerated it — the sole deterministic tie-break key (never a
    set's or dict's iteration order, which carries no ordering contract).
    """

    payload: object
    declared_order: int
    value: float | None = None


@dataclass(frozen=True, slots=True)
class Decision:
    """The result of one :meth:`Policy.choose` call.

    ``chosen`` is ``None`` only when no candidate could be chosen at all —
    an empty candidate list, or (for an expected-value Policy) every
    candidate being planner-opaque. ``opaque`` carries every candidate the
    Policy declined to value, explicitly, rather than dropping them: a
    caller can route them to a different valuation strategy (rollout,
    ADR-0008) instead of reading their absence as "valued at zero".
    """

    chosen: Candidate | None
    opaque: tuple[Candidate, ...] = ()


class Policy(ABC):
    """Chooses one :class:`Candidate` from a list, each call.

    Every Policy is constructed with the run's seed, whether or not the
    concrete class is itself stochastic — so a caller can build any
    registered Policy uniformly (``policies.get(policy_id)(seed=seed)``)
    without introspecting which ones need one.
    """

    id: ClassVar[str]

    def __init__(self, seed: int) -> None:
        self.seed = seed

    @abstractmethod
    def choose(self, candidates: Sequence[Candidate]) -> Decision:
        """Select one candidate from ``candidates``, or none if it is empty."""


policies: Registry[type[Policy]] = Registry("dndsim.policies")
