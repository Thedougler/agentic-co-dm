"""The live run monitor's Textual App (issue #56).

``MonitorApp`` runs a caller-supplied ``work`` callable on a background
thread and renders whatever :class:`~dndsim.tui.progress.RunProgress`
snapshots it reports — cells completed, win rate with its confidence
interval, iterations done, and an estimated time remaining. It is a
MONITOR ONLY: it never calls into the work being observed except to start
it once and read its return value, and it never touches run state itself.
Use :func:`dndsim.tui.monitor.run_with_monitor` rather than this class
directly — it is the seam that decides whether a monitor can attach at
all (a real terminal on stdout).
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

from textual import work
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Footer, Header, Label, ProgressBar

from dndsim.tui.progress import CallbackReporter, ProgressReporter, RunProgress

T = TypeVar("T")


def format_eta(seconds: float | None) -> str:
    """Render an ETA estimate as ``1h02m03s`` and friends, or a neutral
    placeholder before enough progress exists to extrapolate from."""
    if seconds is None:
        return "estimating..."
    total = max(0, int(seconds))
    minutes, secs = divmod(total, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h{minutes:02d}m{secs:02d}s"
    if minutes:
        return f"{minutes}m{secs:02d}s"
    return f"{secs}s"


class MonitorApp(App[T]):
    """Runs ``work(reporter)`` on a background thread and exits — returning
    its result via ``run()``/``run_async()`` — the moment ``work`` returns
    or raises. An exception raised by ``work`` is re-raised from
    :meth:`result` after the app exits, never swallowed.
    """

    CSS = """
    #status {
        padding: 1 2;
    }
    """

    def __init__(self, work: Callable[[ProgressReporter], T], label: str) -> None:
        super().__init__()
        self._work = work
        self._label = label
        self._error: BaseException | None = None
        self._result: T | None = None

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id="status"):
            yield Label(self._label, id="run-label")
            yield Label("cells: -", id="cells-line")
            yield Label("win rate: -", id="win-line")
            yield Label("iterations: -", id="iter-line")
            yield Label("elapsed: 0s  |  eta: estimating...", id="time-line")
            yield ProgressBar(id="bar", show_eta=False)
        yield Footer()

    def on_mount(self) -> None:
        self._run_work()

    @work(thread=True)
    def _run_work(self) -> None:
        reporter = CallbackReporter(callback=self._on_progress)
        try:
            result = self._work(reporter)
        except BaseException as err:  # noqa: BLE001 - re-raised by result() on the caller's thread
            self._error = err
            self.call_from_thread(self.exit)
            return
        self._result = result
        self.call_from_thread(self.exit)

    def result(self) -> T:
        """The ``work`` callable's return value. Call only after ``run()``
        (or ``run_async``) has returned. Re-raises whatever exception
        ``work`` raised, so a caller sees the same failure it would have
        seen calling ``work`` directly."""
        if self._error is not None:
            raise self._error
        return self._result  # type: ignore[return-value]

    def _on_progress(self, progress: RunProgress) -> None:
        try:
            self.call_from_thread(self._apply_progress, progress)
        except RuntimeError:
            # The app already exited (work finished between this report
            # and the call landing) — nothing left to render.
            pass

    def _apply_progress(self, progress: RunProgress) -> None:
        cells_line = self.query_one("#cells-line", Label)
        win_line = self.query_one("#win-line", Label)
        iter_line = self.query_one("#iter-line", Label)
        time_line = self.query_one("#time-line", Label)
        bar = self.query_one("#bar", ProgressBar)

        if progress.cells_total:
            cells_line.update(f"cells: {progress.cells_done}/{progress.cells_total}")
            bar.update(total=progress.cells_total, progress=progress.cells_done)
        elif progress.iterations_target:
            cells_line.update("cells: n/a (single run)")
            bar.update(total=progress.iterations_target, progress=progress.iterations_done)
        else:
            cells_line.update("cells: n/a (single run)")
            bar.update(total=None)

        if progress.win_ci is not None and progress.win_ci.p is not None:
            ci = progress.win_ci
            assert ci.lo is not None and ci.hi is not None
            win_line.update(f"win rate: {ci.p:.1%}  (95% CI [{ci.lo:.1%}, {ci.hi:.1%}])")

        if progress.generations_done is not None:
            gen = f"{progress.generations_done}"
            if progress.generations_total is not None:
                gen += f"/{progress.generations_total}"
            iter_line.update(f"iterations: {progress.iterations_done:,}  |  generation {gen}")
        else:
            target = f"/{progress.iterations_target:,}" if progress.iterations_target else ""
            iter_line.update(f"iterations: {progress.iterations_done:,}{target}")

        eta = format_eta(progress.eta_seconds)
        time_line.update(f"elapsed: {int(progress.elapsed)}s  |  eta: {eta}")
