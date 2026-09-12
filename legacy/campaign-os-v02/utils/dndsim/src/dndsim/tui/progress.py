"""Progress state and thread-safe reporting for the live run monitor.

A caller instruments its own work with a :class:`ProgressReporter` and
calls ``.report(...)`` as work advances. Passing :class:`NullReporter` (the
default when no monitor is attached) must be behaviorally identical to
passing no reporter at all — that is what keeps a command's report
byte-identical whether or not ``--monitor`` is on. Nothing here reaches
back into the run being observed: a reporter only receives snapshots, it
never returns a value or raises into the caller's control flow.
"""

from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Protocol

from dndsim.core.stats import ConfidenceInterval


@dataclass(frozen=True, slots=True)
class RunProgress:
    """One snapshot of a run's progress. Every field beyond ``label`` and
    ``started_at`` is optional — a caller reports whichever axes it has
    (cells, iterations, generations, a win-rate interval); the monitor
    renders whichever are set and leaves the rest at their placeholder.
    """

    label: str = ""
    cells_done: int = 0
    cells_total: int | None = None
    iterations_done: int = 0
    iterations_target: int | None = None
    generations_done: int | None = None
    generations_total: int | None = None
    win_ci: ConfidenceInterval | None = None
    started_at: float = 0.0

    @property
    def elapsed(self) -> float:
        """Seconds since ``started_at``, or 0.0 before a start time is known."""
        if self.started_at <= 0:
            return 0.0
        return time.perf_counter() - self.started_at

    @property
    def eta_seconds(self) -> float | None:
        """Estimated remaining seconds, extrapolated from whichever of
        cells/iterations has both a known target and nonzero progress so
        far. ``None`` when there is nothing yet to extrapolate from —
        rendered as "estimating..." rather than a misleading 0.
        """
        elapsed = self.elapsed
        if elapsed <= 0:
            return None
        for done, total in (
            (self.cells_done, self.cells_total),
            (self.iterations_done, self.iterations_target),
        ):
            if total is not None and total > 0 and done > 0:
                rate = done / elapsed
                if rate <= 0:
                    return None
                remaining = max(total - done, 0)
                return remaining / rate
        return None


class ProgressReporter(Protocol):
    """The seam instrumented work code reports through. Implementations
    must never block the caller meaningfully or raise — a monitor is
    allowed to be slow or wrong about rendering, never allowed to make the
    run it's watching slower or less correct.
    """

    def report(self, progress: RunProgress) -> None: ...


class NullReporter:
    """The off-monitor reporter: every call is a no-op. This is what makes
    instrumented code's report output identical whether or not a monitor
    is attached — the instrumentation itself never branches on that.
    """

    def report(self, progress: RunProgress) -> None:
        return None


@dataclass(slots=True)
class CallbackReporter:
    """Forwards each ``report`` call to a plain callback. The seam
    :mod:`dndsim.tui.app` uses to marshal a worker-thread progress update
    onto the Textual app's own thread via ``App.call_from_thread``.
    """

    callback: Callable[[RunProgress], None]

    def report(self, progress: RunProgress) -> None:
        self.callback(progress)
