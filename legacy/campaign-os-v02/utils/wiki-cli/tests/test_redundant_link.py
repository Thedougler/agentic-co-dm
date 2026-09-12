"""Tests for the wiki/redundant-link advisory rule and the
`wiki links redundant` CLI report."""
from __future__ import annotations

import shutil
from pathlib import Path

import pytest
from typer.testing import CliRunner

from wiki_cli.cli import app
from wiki_cli.contracts import Severity
from wiki_cli.index import VaultIndex
from wiki_cli.rules.redundant_link import RedundantLinkRule

FIXTURES = Path(__file__).parent / "fixtures" / "index"
runner = CliRunner()


@pytest.fixture
def vault_cwd(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    shutil.copytree(FIXTURES, tmp_path / "vault", dirs_exist_ok=True)
    (tmp_path / "wiki.toml").write_text(
        '[vault]\nroot = "vault"\ntemplates = "vault/_templates"\n'
        '[cache]\npath = ".wiki-cli/cache.sqlite3"\n',
        encoding="utf-8",
    )
    (tmp_path / "vault" / "_templates").mkdir(exist_ok=True)
    monkeypatch.chdir(tmp_path)
    return tmp_path


def _build_index(vault_cwd: Path) -> VaultIndex:
    return VaultIndex.build(vault_cwd, vault_cwd / "vault", ())


# --- Rule tests ---

def test_redundant_link_finds_barnaby(vault_cwd: Path) -> None:
    index = _build_index(vault_cwd)
    rule = RedundantLinkRule()
    findings = list(rule.check(index))
    # barnaby-rook.md links [[the-rook]] 2x in section "Ties"
    assert len(findings) >= 1
    match = [f for f in findings if "barnaby-rook" in f.file and "the-rook" in f.message]
    assert match, f"Expected a finding on barnaby-rook for [[the-rook]], got {findings}"
    assert "Ties" in match[0].message


def test_redundant_link_ignores_different_section_targets(vault_cwd: Path) -> None:
    index = _build_index(vault_cwd)
    rule = RedundantLinkRule()
    findings = list(rule.check(index))
    match = [f for f in findings if "section-links" in f.file]
    assert match == [], f"Section-targeted links to same page should not be redundant: {match}"


def test_redundant_link_is_a_baselineable_warning() -> None:
    rule = RedundantLinkRule()
    assert rule.severity == Severity.WARNING
    assert rule.baselineable is True


def test_redundant_link_skips_non_vault_index() -> None:
    rule = RedundantLinkRule()

    # Pass a non-VaultIndex corpus — should return no findings
    class FakeCorpus:
        pass

    findings = list(rule.check(FakeCorpus()))  # type: ignore[arg-type]
    assert findings == []


# --- CLI tests ---

def test_cli_redundant_report(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["links", "redundant"])
    assert result.exit_code == 0
    assert "barnaby-rook" in result.output
    assert "the-rook" in result.output


def test_cli_redundant_json(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["links", "redundant", "--format", "json"])
    assert result.exit_code == 0
    import json

    data = json.loads(result.output)
    assert isinstance(data, list)
    assert any("barnaby-rook" in item.get("path", "") for item in data)
