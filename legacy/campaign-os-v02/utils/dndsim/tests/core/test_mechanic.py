from __future__ import annotations

import numpy as np
import pytest

from dndsim.core.mechanic import Mechanic


def test_mechanic_cannot_be_instantiated_directly() -> None:
    with pytest.raises(TypeError):
        Mechanic()  # type: ignore[abstract]


def test_a_complete_subclass_can_be_instantiated_and_used() -> None:
    class Coin(Mechanic):
        id = "test:mechanic/coin"

        def resolve(self, rng, size):  # type: ignore[no-untyped-def]
            return rng.integers(0, 2, size=size).astype(np.float64)

        def expected_value(self) -> float:
            return 0.5

        @classmethod
        def hypothesis_strategy(cls):  # type: ignore[no-untyped-def]
            raise NotImplementedError

    instance = Coin()
    assert instance.expected_value() == 0.5
