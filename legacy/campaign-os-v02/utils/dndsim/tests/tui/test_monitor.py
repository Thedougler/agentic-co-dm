"""``dndsim.tui.monitor.run_with_monitor`` — issue #56.

Covers the TTY decision itself: a monitor may only attach when both
``enabled`` is true and the target stream is a live terminal. Every other
case must run ``work`` directly, with no ``MonitorApp`` constructed at
all — asserted here by patching ``MonitorApp`` to raise if instantiated.
"""

from __future__ import annotations

import io

import pytest

import dndsim.tui.monitor as monitor_module
from dndsim.tui.monitor import is_live_terminal, run_with_monitor
from dndsim.tui.progress import NullReporter, ProgressReporter


class _FakeStream(io.StringIO):
    def __init__(self, live: bool) -> None:
        super().__init__()
        self._live = live

    def isatty(self) -> bool:
        return self._live


def test_is_live_terminal_true_for_a_tty_stream() -> None:
    assert is_live_terminal(_FakeStream(live=True)) is True


def test_is_live_terminal_false_for_a_redirected_stream() -> None:
    assert is_live_terminal(_FakeStream(live=False)) is False


def test_is_live_terminal_false_for_a_stream_with_no_isatty() -> None:
    class NoIsatty:
        pass

    assert is_live_terminal(NoIsatty()) is False  # type: ignore[arg-type]


def _forbid_monitor_app(monkeypatch: pytest.MonkeyPatch) -> None:
    def _boom(*args: object, **kwargs: object) -> object:
        raise AssertionError("MonitorApp must not be constructed on this path")

    monkeypatch.setattr(monitor_module, "MonitorApp", _boom)


def test_disabled_monitor_runs_work_with_null_reporter_directly(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _forbid_monitor_app(monkeypatch)
    seen: list[ProgressReporter] = []

    def work(reporter: ProgressReporter) -> str:
        seen.append(reporter)
        return "result"

    result = run_with_monitor(work, enabled=False, label="x", stream=_FakeStream(live=True))
    assert result == "result"
    assert isinstance(seen[0], NullReporter)


def test_enabled_but_no_tty_runs_work_with_null_reporter_directly(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _forbid_monitor_app(monkeypatch)
    seen: list[ProgressReporter] = []

    def work(reporter: ProgressReporter) -> str:
        seen.append(reporter)
        return "result"

    result = run_with_monitor(work, enabled=True, label="x", stream=_FakeStream(live=False))
    assert result == "result"
    assert isinstance(seen[0], NullReporter)


def test_defaults_to_sys_stdout_when_no_stream_given(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # CliRunner-captured / pytest-captured stdout is never a live terminal,
    # so the default path degrades the same way a redirected run does.
    _forbid_monitor_app(monkeypatch)

    def work(reporter: ProgressReporter) -> int:
        assert isinstance(reporter, NullReporter)
        return 42

    assert run_with_monitor(work, enabled=True, label="x") == 42


def test_work_exception_propagates_on_the_degraded_path(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _forbid_monitor_app(monkeypatch)

    def work(reporter: ProgressReporter) -> None:
        raise ValueError("boom")

    with pytest.raises(ValueError, match="boom"):
        run_with_monitor(work, enabled=False, label="x", stream=_FakeStream(live=True))
