from __future__ import annotations

import numpy as np
import pytest

from dndsim.core.resources import ResourcePool


def test_spend_subtracts_on_masked_universes() -> None:
    pool = ResourcePool("x", np.array([10.0, 10.0, 10.0]))
    mask = np.array([True, False, True])
    pool.spend(np.array([3.0, 4.0]), mask)
    assert list(pool.current) == [7.0, 10.0, 6.0]


def test_spend_clamps_at_zero() -> None:
    pool = ResourcePool("x", np.array([5.0]))
    pool.spend(np.array([100.0]), np.array([True]))
    assert pool.current[0] == 0.0


def test_restore_clamps_at_max() -> None:
    pool = ResourcePool("x", np.array([10.0]))
    pool.spend(np.array([8.0]), np.array([True]))
    pool.restore(np.array([100.0]), np.array([True]))
    assert pool.current[0] == 10.0


def test_depleted_true_only_at_zero() -> None:
    pool = ResourcePool("x", np.array([10.0, 0.0]))
    assert list(pool.depleted()) == [False, True]


def test_spend_shape_mismatch_raises() -> None:
    pool = ResourcePool("x", np.array([10.0, 10.0]))
    with pytest.raises(ValueError, match="entries"):
        pool.spend(np.array([1.0, 2.0, 3.0]), np.array([True, True]))


def test_size_property() -> None:
    pool = ResourcePool("x", np.array([1.0, 2.0, 3.0]))
    assert pool.size == 3
