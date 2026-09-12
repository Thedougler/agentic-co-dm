"""``dndsim.tui.app.MonitorApp`` — issue #56, headless-driven via Textual's
``run_test``/``Pilot`` (never asserted against rendered ANSI). No
pytest-asyncio dependency: each test is a plain sync function wrapping a
single ``asyncio.run`` call, since the repo has no other async tests and
stdlib already covers this one seam.
"""

from __future__ import annotations

import asyncio
import threading
import time

import pytest
from textual.widgets import Label, ProgressBar

from dndsim.core.stats import wilson_interval
from dndsim.tui.app import MonitorApp, format_eta
from dndsim.tui.progress import ProgressReporter, RunProgress


def test_format_eta_renders_seconds_minutes_hours() -> None:
    assert format_eta(None) == "estimating..."
    assert format_eta(9) == "9s"
    assert format_eta(65) == "1m05s"
    assert format_eta(3725) == "1h02m05s"


async def _drive_live_progress() -> MonitorApp[str]:
    """Two progress reports land, in order, while the same worker is still
    running — proof the display updates live rather than only rendering a
    final snapshot after the work function returns."""
    seen_first = threading.Event()
    proceed_to_second = threading.Event()
    seen_second = threading.Event()

    def work(reporter: ProgressReporter) -> str:
        reporter.report(
            RunProgress(
                label="corpus sweep",
                cells_done=1,
                cells_total=4,
                started_at=time.perf_counter(),
            )
        )
        seen_first.set()
        assert proceed_to_second.wait(timeout=5), "test never signalled to continue"
        reporter.report(
            RunProgress(
                label="corpus sweep",
                cells_done=3,
                cells_total=4,
                win_ci=wilson_interval(2, 3),
                started_at=time.perf_counter() - 2,
            )
        )
        seen_second.set()
        return "swept"

    app: MonitorApp[str] = MonitorApp(work, "corpus sweep")
    async with app.run_test() as pilot:
        for _ in range(200):
            if seen_first.is_set():
                break
            await pilot.pause()
        assert seen_first.is_set(), "worker never reported its first progress snapshot"

        first_cells = str(app.query_one("#cells-line", Label).content)
        first_bar_progress = app.query_one("#bar", ProgressBar).progress
        assert "1/4" in first_cells
        assert first_bar_progress == 1

        proceed_to_second.set()
        for _ in range(200):
            if seen_second.is_set():
                break
            await pilot.pause()
        assert seen_second.is_set(), "worker never reported its second progress snapshot"

        second_cells = str(app.query_one("#cells-line", Label).content)
        second_win = str(app.query_one("#win-line", Label).content)
        assert "3/4" in second_cells
        assert second_cells != first_cells
        assert "win rate" in second_win and "CI" in second_win

        for _ in range(200):
            if not app.is_running:
                break
            await pilot.pause()

    return app


def test_monitor_app_shows_live_progress_updating() -> None:
    app = asyncio.run(_drive_live_progress())
    assert app.result() == "swept"


async def _drive_exception() -> MonitorApp[str]:
    def work(reporter: ProgressReporter) -> str:
        raise ValueError("sweep blew up")

    app: MonitorApp[str] = MonitorApp(work, "boom")
    async with app.run_test() as pilot:
        for _ in range(200):
            if not app.is_running:
                break
            await pilot.pause()
    return app


def test_monitor_app_reraises_the_work_functions_exception() -> None:
    app = asyncio.run(_drive_exception())
    with pytest.raises(ValueError, match="sweep blew up"):
        app.result()
