"""``dndsim profile`` — issue #51's CLI verb, plus issue #67's audit-log gap."""

from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from dndsim.cli import app

runner = CliRunner()

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"

# Every test but the audit-log ones passes --no-audit-log: profile's audit
# line is ON by default (issue #67), but a test run must never write into
# the repo's real utils/dndsim/dndsim-audit.jsonl.
NO_AUDIT = ["--no-audit-log"]


def test_profile_prints_markdown_report() -> None:
    path = FIXTURES_DIR / "fixture-otar-the-foul.md"
    result = runner.invoke(
        app,
        [
            "profile",
            str(path),
            "--seed",
            "1",
            "--iterations",
            "200",
            "--ac-min",
            "10",
            "--ac-max",
            "12",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert "# Combat profile — Otar the Foul" in result.stdout
    assert "dndsim v" in result.stdout


def test_profile_out_option_writes_file(tmp_path: Path) -> None:
    path = FIXTURES_DIR / "fixture-otar-the-foul.md"
    out_path = tmp_path / "profile.md"
    result = runner.invoke(
        app,
        [
            "profile",
            str(path),
            "--seed",
            "1",
            "--iterations",
            "100",
            "--ac-min",
            "10",
            "--ac-max",
            "10",
            "--out",
            str(out_path),
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0
    assert out_path.exists()
    assert "# Combat profile" in out_path.read_text()


def test_profile_no_seed_generates_and_reports_one() -> None:
    path = FIXTURES_DIR / "fixture-otar-the-foul.md"
    result = runner.invoke(
        app,
        [
            "profile",
            str(path),
            "--iterations",
            "100",
            "--ac-min",
            "10",
            "--ac-max",
            "10",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0
    assert "**Seed generated**:" in result.stdout


def test_profile_same_seed_is_identical() -> None:
    path = FIXTURES_DIR / "fixture-otar-the-foul.md"
    args = [
        "profile",
        str(path),
        "--seed",
        "42",
        "--iterations",
        "300",
        "--ac-min",
        "10",
        "--ac-max",
        "14",
        *NO_AUDIT,
    ]
    first = runner.invoke(app, args)
    second = runner.invoke(app, args)
    assert first.stdout == second.stdout


def test_profile_no_fence_exits_nonzero_with_message() -> None:
    path = FIXTURES_DIR / "fixture-blight.md"
    result = runner.invoke(app, ["profile", str(path), *NO_AUDIT])
    assert result.exit_code == 1
    assert result.stderr is not None
    assert "dndsim profile:" in result.stderr


def test_profile_rejects_ac_max_below_ac_min() -> None:
    path = FIXTURES_DIR / "fixture-otar-the-foul.md"
    result = runner.invoke(
        app, ["profile", str(path), "--ac-min", "20", "--ac-max", "10", *NO_AUDIT]
    )
    assert result.exit_code == 1


def test_profile_writes_one_audit_line_by_default(tmp_path: Path) -> None:
    path = FIXTURES_DIR / "fixture-otar-the-foul.md"
    log_path = tmp_path / "audit.jsonl"
    result = runner.invoke(
        app,
        [
            "profile",
            str(path),
            "--seed",
            "1",
            "--iterations",
            "100",
            "--ac-min",
            "10",
            "--ac-max",
            "10",
            "--audit-log",
            str(log_path),
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert log_path.exists()
    lines = log_path.read_text().splitlines()
    assert len(lines) == 1
    payload = json.loads(lines[0])
    assert payload["seed"] == 1
    assert payload["engineVersion"]
    assert payload["resultDigest"]
    assert payload["subject"]["name"] == "Otar the Foul"


def test_profile_no_audit_log_suppresses_the_line(tmp_path: Path) -> None:
    path = FIXTURES_DIR / "fixture-otar-the-foul.md"
    log_path = tmp_path / "audit.jsonl"
    result = runner.invoke(
        app,
        [
            "profile",
            str(path),
            "--seed",
            "1",
            "--iterations",
            "100",
            "--ac-min",
            "10",
            "--ac-max",
            "10",
            "--audit-log",
            str(log_path),
            "--no-audit-log",
        ],
    )
    assert result.exit_code == 0
    assert not log_path.exists()
