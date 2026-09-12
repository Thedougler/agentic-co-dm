"""``dndsim.tui.progress`` — issue #56."""

from __future__ import annotations

import time

from dndsim.core.stats import wilson_interval
from dndsim.tui.progress import CallbackReporter, NullReporter, RunProgress


def test_null_reporter_is_a_no_op() -> None:
    reporter = NullReporter()
    # Must not raise — a caller can never observe a difference between
    # reporting to this and reporting to nothing at all.
    reporter.report(RunProgress(label="x"))


def test_callback_reporter_forwards_every_report() -> None:
    seen: list[RunProgress] = []
    reporter = CallbackReporter(callback=seen.append)
    p1 = RunProgress(label="a", cells_done=1)
    p2 = RunProgress(label="a", cells_done=2)
    reporter.report(p1)
    reporter.report(p2)
    assert seen == [p1, p2]


def test_elapsed_is_zero_before_started_at_is_set() -> None:
    assert RunProgress().elapsed == 0.0


def test_elapsed_grows_from_started_at() -> None:
    started = time.perf_counter() - 5.0
    progress = RunProgress(started_at=started)
    assert progress.elapsed >= 5.0


def test_eta_is_none_with_no_progress_yet() -> None:
    started = time.perf_counter() - 1.0
    progress = RunProgress(started_at=started, cells_done=0, cells_total=10)
    assert progress.eta_seconds is None


def test_eta_is_none_before_a_start_time_exists() -> None:
    progress = RunProgress(cells_done=5, cells_total=10)
    assert progress.eta_seconds is None


def test_eta_extrapolates_from_cells_when_available() -> None:
    started = time.perf_counter() - 10.0
    # 5 of 10 cells done in ~10s -> ~2s/cell -> ~10s remaining for the
    # other 5.
    progress = RunProgress(started_at=started, cells_done=5, cells_total=10)
    eta = progress.eta_seconds
    assert eta is not None
    assert 7.0 < eta < 13.0


def test_eta_falls_back_to_iterations_when_cells_total_is_unset() -> None:
    started = time.perf_counter() - 10.0
    progress = RunProgress(started_at=started, iterations_done=500, iterations_target=1000)
    eta = progress.eta_seconds
    assert eta is not None
    assert 5.0 < eta < 15.0


def test_run_progress_carries_a_confidence_interval() -> None:
    ci = wilson_interval(450, 1000)
    progress = RunProgress(win_ci=ci)
    assert progress.win_ci is not None
    assert progress.win_ci.p == ci.p
