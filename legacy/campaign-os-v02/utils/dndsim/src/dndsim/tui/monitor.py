"""The live run monitor's one public entry point (issue #56).

``run_with_monitor`` is the only seam a CLI command should call: it
decides whether a monitor can attach at all — ``enabled`` and a real
terminal on the given stream — and runs ``work`` either way, so the
caller's own code never branches on the TTY decision. When a monitor
can't attach (disabled, or stdout redirected/no TTY), ``work`` runs
directly against :class:`~dndsim.tui.progress.NullReporter` with no
Textual app constructed at all: this is what makes a command's markdown
report byte-identical whether or not ``--monitor`` was passed, and what
makes redirected/no-TTY output degrade cleanly rather than error.
"""

from __future__ import annotations

import sys
from collections.abc import Callable
from typing import IO

from dndsim.tui.app import MonitorApp
from dndsim.tui.progress import NullReporter, ProgressReporter


def is_live_terminal(stream: IO[str]) -> bool:
    """Whether ``stream`` is a real, attached terminal — never true for a
    pipe, a redirected file, or ``CliRunner``'s captured stdout."""
    isatty = getattr(stream, "isatty", None)
    return bool(isatty and isatty())


def run_with_monitor[T](
    work: Callable[[ProgressReporter], T],
    *,
    enabled: bool,
    label: str,
    stream: IO[str] | None = None,
) -> T:
    """Run ``work(reporter)``, attaching the live monitor only when
    ``enabled`` and ``stream`` (default ``sys.stdout``) is a live
    terminal. ``work`` runs exactly once either way; only what it reports
    progress to differs.
    """
    live_stream = stream if stream is not None else sys.stdout
    if not enabled or not is_live_terminal(live_stream):
        return work(NullReporter())

    app: MonitorApp[T] = MonitorApp(work, label)
    app.run()
    return app.result()
