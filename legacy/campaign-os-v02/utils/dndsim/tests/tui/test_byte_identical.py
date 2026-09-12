"""End-to-end proof for issue #56's core design decision: attaching the
live monitor never changes what a command writes to ``--out``, and
``--monitor`` degrades cleanly (no crash, no monitor) whenever stdout
isn't a live terminal — the two acceptance criteria that can't be proven
by a unit test against ``dndsim.tui`` in isolation, since they're about
the CLI's actual output under a real (or absent) terminal.
"""

from __future__ import annotations

import os
import pty
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]


def _run_under_pty(cmd: list[str]) -> int:
    """Run ``cmd`` with stdin/stdout/stderr attached to a real pty, so
    ``sys.stdout.isatty()`` is true inside the child — the only way to
    exercise the monitor-attached code path from a test."""
    master_fd, slave_fd = pty.openpty()
    proc = subprocess.Popen(cmd, stdin=slave_fd, stdout=slave_fd, stderr=slave_fd, cwd=REPO_ROOT)
    os.close(slave_fd)
    try:
        while True:
            try:
                chunk = os.read(master_fd, 4096)
            except OSError:
                break
            if not chunk:
                break
    finally:
        os.close(master_fd)
    return proc.wait(timeout=60)


@pytest.mark.skipif(sys.platform == "win32", reason="pty is POSIX-only")
def test_report_is_byte_identical_with_and_without_monitor_attached(
    tmp_path: Path,
) -> None:
    out_monitored = tmp_path / "monitored.md"
    out_plain = tmp_path / "plain.md"

    base_args = [
        "uv",
        "run",
        "dndsim",
        "sim-combat",
        "--seed",
        "13",
        "--universes",
        "500",
        "--adaptive",
        "--adaptive-cap",
        "1000",
        "--adaptive-chunk",
        "250",
        "--no-audit-log",
    ]

    monitored_rc = _run_under_pty([*base_args, "--monitor", "--out", str(out_monitored)])
    assert monitored_rc == 0

    plain = subprocess.run(
        [*base_args, "--out", str(out_plain)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert plain.returncode == 0, plain.stderr

    monitored_text = out_monitored.read_text()
    plain_text = out_plain.read_text()
    assert monitored_text == plain_text
    assert "# Combat simulation report" in plain_text


def test_monitor_flag_degrades_cleanly_with_redirected_output(
    tmp_path: Path,
) -> None:
    """``--monitor`` with stdout piped/redirected (never a TTY under a
    plain subprocess) must not crash and must not attach a Textual app —
    it degrades to the same output a run with no ``--monitor`` produces."""
    out_path = tmp_path / "redirected.md"
    result = subprocess.run(
        [
            "uv",
            "run",
            "dndsim",
            "sim-combat",
            "--seed",
            "21",
            "--universes",
            "300",
            "--no-audit-log",
            "--monitor",
            "--out",
            str(out_path),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode == 0, result.stderr
    assert out_path.read_text().startswith("# Combat simulation report")
    # No Textual screen/ANSI escape junk leaked to stdout — the degraded
    # path never constructs an App at all.
    assert "\x1b[" not in result.stdout
