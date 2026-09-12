"""``dndsim parse`` — issue #40's CLI verb over the native statblock fence."""

from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from dndsim.cli import app

runner = CliRunner()

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def test_parse_json_emits_normalized_content() -> None:
    path = FIXTURES_DIR / "fixture-otar-the-foul.md"
    result = runner.invoke(app, ["parse", str(path), "--json"])
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    assert len(payload) == 1
    content = payload[0]["content"]
    assert content["name"] == "Otar the Foul"
    assert content["ac"] == 17
    assert content["hp"] == 241
    assert content["cr"] == 12


def test_parse_summary_mode_prints_readable_line() -> None:
    path = FIXTURES_DIR / "fixture-sawek.md"
    result = runner.invoke(app, ["parse", str(path)])
    assert result.exit_code == 0
    assert "Sawek" in result.stdout
    assert "AC 14" in result.stdout


def test_parse_empty_fence_reports_stub_not_error() -> None:
    path = FIXTURES_DIR / "fixture-blight.md"
    result = runner.invoke(app, ["parse", str(path), "--json"])
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    assert payload[0]["content"] is None


def test_parse_missing_required_field_fails_loudly_naming_field(tmp_path: Path) -> None:
    broken = tmp_path / "broken.md"
    broken.write_text("```statblock\nname: Broken\nhp: 10\nstats: [10,10,10,10,10,10]\n```")
    result = runner.invoke(app, ["parse", str(broken)])
    assert result.exit_code == 1
    assert result.stderr is not None
    assert 'missing required key "ac"' in result.stderr
