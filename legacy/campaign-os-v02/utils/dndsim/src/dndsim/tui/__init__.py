"""The live run monitor (issue #56) — a terminal view of a run in progress.

Monitor only. Nothing in this package drives a run, retries a step, or
mutates run state; it observes progress a caller reports and renders it.
Opt-in and off by default (``--monitor`` on the CLI); attaching or not
attaching it never changes what a command writes to stdout/``--out`` —
see :mod:`dndsim.tui.monitor` for the entry point that enforces that.
"""

from __future__ import annotations
