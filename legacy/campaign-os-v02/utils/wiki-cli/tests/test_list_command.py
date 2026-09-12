"""CLI tests for `wiki list`."""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from wiki_cli.cli import app

runner = CliRunner()


def _write(path: Path, frontmatter: str, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{frontmatter}\n---\n{body}", encoding="utf-8")


@pytest.fixture
def vault_cwd(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    (tmp_path / "wiki.toml").write_text(
        '[vault]\nroot = "vault"\ntemplates = "vault/_templates"\n'
        '[cache]\npath = ".wiki-cli/cache.sqlite3"\n',
        encoding="utf-8",
    )
    _write(tmp_path / "vault" / "_templates" / "_npc.md", "type: npc")
    _write(tmp_path / "vault" / "npcs" / "the-rook.md", "type: npc", "# The Rook\n")
    _write(
        tmp_path / "vault" / "npcs" / "barnaby-rook.md",
        "type: npc",
        "# Barnaby Rook\n\nAllied with [[the-rook]].\n",
    )
    _write(
        tmp_path / "vault" / "npcs" / "other.md",
        "type: npc",
        "# Other\n\nAlso allied with [[the-rook]].\n",
    )
    _write(tmp_path / "vault" / "factions" / "ravens.md", "type: faction", "# Ravens\n")
    (tmp_path / ".wiki-cli").mkdir(exist_ok=True)
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_list_filters_by_type(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["list", "--where", "type=npc", "--format", "paths"])
    assert result.exit_code == 0
    paths = set(result.output.strip().split("\n"))
    assert paths == {
        "vault/npcs/the-rook.md",
        "vault/npcs/barnaby-rook.md",
        "vault/npcs/other.md",
    }


def test_list_sort_by_links_in_desc(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["list", "--sort", "-links-in", "--format", "paths"])
    assert result.exit_code == 0
    lines = result.output.strip().split("\n")
    # the-rook has the most inbound links (2)
    assert lines[0] == "vault/npcs/the-rook.md"


def test_list_unknown_key_exits_2(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["list", "--where", "bogus=1"])
    assert result.exit_code == 2
    assert "type" in result.output  # legal-keys listing


def test_list_limit(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["list", "--format", "paths", "--limit", "2"])
    assert result.exit_code == 0
    assert len(result.output.strip().split("\n")) == 2


def test_list_excludes_templates_by_default(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["list", "--format", "paths"])
    assert result.exit_code == 0
    assert "vault/_templates/_npc.md" not in result.output.strip().split("\n")


def test_list_include_templates(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["list", "--include-templates", "--format", "paths"])
    assert result.exit_code == 0
    assert "vault/_templates/_npc.md" in result.output.strip().split("\n")
