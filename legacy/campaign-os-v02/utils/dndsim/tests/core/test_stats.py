from __future__ import annotations

import pytest

from dndsim.core.stats import wilson_interval


def test_zero_trials_returns_all_none() -> None:
    ci = wilson_interval(0, 0)
    assert ci.p is None
    assert ci.lo is None
    assert ci.hi is None
    assert ci.half_width is None


def test_point_estimate_matches_successes_over_trials() -> None:
    ci = wilson_interval(50, 100)
    assert ci.p == pytest.approx(0.5)


def test_interval_narrows_as_trials_grow() -> None:
    small = wilson_interval(500, 1000)
    large = wilson_interval(5000, 10000)
    assert small.half_width is not None
    assert large.half_width is not None
    assert large.half_width < small.half_width


def test_interval_bounds_stay_within_unit_range() -> None:
    ci = wilson_interval(1000, 1000)
    assert ci.lo is not None and ci.hi is not None
    assert 0.0 <= ci.lo <= ci.hi <= 1.0


def test_zero_successes_stays_within_unit_range() -> None:
    ci = wilson_interval(0, 1000)
    assert ci.lo is not None and ci.hi is not None
    assert 0.0 <= ci.lo <= ci.hi <= 1.0


def test_successes_out_of_range_raises() -> None:
    with pytest.raises(ValueError):
        wilson_interval(-1, 10)
    with pytest.raises(ValueError):
        wilson_interval(11, 10)
