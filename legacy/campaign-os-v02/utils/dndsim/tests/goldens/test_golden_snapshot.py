"""Pins the party-vs-enemies fixture's result at a fixed seed and universe
count.

Any byte difference from ``sim_combat_seed1.md`` is a behavior change and
requires a deliberate, documented regeneration — never a silent update to
make a red test pass. To regenerate after an intentional engine change:

    uv run --project utils/dndsim dndsim sim-combat --seed 1 --universes 50000 \\
        --round-cap 30 --out utils/dndsim/tests/goldens/sim_combat_seed1.md

then bump ``dndsim.__version__`` and note the change in a commit message
explaining what moved and why (see docs/adr/0007..0012 for what counts as
a deliberate divergence vs. a regression). ``--round-cap 30`` (the CLI's own
default is 20): issue #59's default fixture is a real 3-vs-3 encounter with
movement, positioning, and a legendary/lair boss — genuinely slower to
resolve than the two-combatant walking skeleton the 20-round default was
tuned against, and the default round-cap stays 20 for that simpler case.
"""

from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from dndsim.cli import app

GOLDEN_PATH = Path(__file__).parent / "sim_combat_seed1.md"
runner = CliRunner()


def test_fixture_output_matches_golden_snapshot() -> None:
    # --no-audit-log: this test must never write into the repo's real
    # utils/dndsim/dndsim-audit.jsonl (issue #50's audit log defaults on).
    result = runner.invoke(
        app,
        [
            "sim-combat",
            "--seed",
            "1",
            "--universes",
            "50000",
            "--round-cap",
            "30",
            "--no-audit-log",
        ],
    )
    assert result.exit_code == 0
    expected = GOLDEN_PATH.read_text()
    assert result.stdout == expected + "\n"  # CliRunner/typer.echo appends a trailing newline
