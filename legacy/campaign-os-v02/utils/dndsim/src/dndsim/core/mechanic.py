"""The Mechanic contract (ADR-0008): resolution and expected value, together.

A Mechanic instance is one fully-parameterized primitive for one decision —
this attacker's weapon against this target's specific defenses and remaining
resources, not a generic "attack" abstraction. Constructing a fresh instance
per decision is what lets :meth:`expected_value` be a plain no-argument method while still
depending on live state: the state is baked into the instance's fields.

``resolve`` draws ``size`` independent Monte-Carlo outcomes (one per
universe, or one per masked slice of a lockstep batch — ADR-0011) and
``expected_value`` states the same primitive's closed-form mean. A registry-
wide Hypothesis property test (tests/property/) asserts the two agree for
every Mechanic in :data:`mechanics`, for every Mechanic that ever exists —
this file itself stays permanently free of any specific mechanic.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

import numpy as np

from dndsim.core.registry import Registry

if TYPE_CHECKING:
    from hypothesis.strategies import SearchStrategy

    from dndsim.core.rng import BatchRNG


class Mechanic(ABC):
    """One primitive's resolution and expected value, bound in one class."""

    id: ClassVar[str]

    @abstractmethod
    def resolve(self, rng: BatchRNG, size: int) -> np.ndarray:
        """Draw ``size`` independent outcomes. Returns a float array of shape ``(size,)``."""

    @abstractmethod
    def expected_value(self) -> float:
        """The closed-form mean of a single :meth:`resolve` draw."""

    @classmethod
    @abstractmethod
    def hypothesis_strategy(cls) -> SearchStrategy[Mechanic]:
        """A Hypothesis strategy producing valid, arbitrarily-parameterized instances.

        Consumed only by the registry-wide property test — never by
        simulation code.
        """


mechanics: Registry[type[Mechanic]] = Registry("dndsim.mechanics")
