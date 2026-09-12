from __future__ import annotations

import numpy as np
import pytest

from dndsim.core.universe import UniverseBatch, bucket_by_choice


def test_universe_batch_size_and_seed() -> None:
    batch = UniverseBatch(size=100, seed=5)
    assert batch.size == 100
    assert batch.seed == 5
    assert batch.active.all()


def test_universe_batch_rejects_nonpositive_size() -> None:
    with pytest.raises(ValueError, match="size"):
        UniverseBatch(size=0, seed=1)


def test_bucket_by_choice_groups_by_code() -> None:
    codes = np.array([0, 1, 0, -1, 1, 0])
    buckets = dict(bucket_by_choice(codes))
    assert set(buckets) == {0, 1}
    assert list(buckets[0]) == [True, False, True, False, False, True]
    assert list(buckets[1]) == [False, True, False, False, True, False]


def test_bucket_by_choice_excludes_no_choice() -> None:
    codes = np.array([-1, -1, -1])
    assert bucket_by_choice(codes) == []
