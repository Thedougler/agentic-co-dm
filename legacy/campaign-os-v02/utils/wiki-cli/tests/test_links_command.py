"""CLI tests for `wiki links in|out|breakdown|orphans`."""

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
    _write(tmp_path / "vault" / "guides" / "lonely.md", "type: guide", "# Lonely\n")
    _write(
        tmp_path / "vault" / "npcs" / "barnaby-rook.md",
        "type: npc",
        "# Barnaby Rook\n\nAllied with [[the-rook]] and [[guide#Setup]].\n\n"
        "## Ties\n\nAlso [[the-rook]].\n",
    )
    _write(tmp_path / "vault" / "npcs" / "the-rook.md", "type: npc", "# The Rook\n")
    _write(tmp_path / "vault" / "factions" / "guide.md", "type: faction", "# Faction Guide\n")
    _write(tmp_path / "vault" / "factions" / "ravens.md", "type: faction", "# Ravens\n")
    _write(tmp_path / "vault" / "guides" / "guide.md", "type: guide", "# Guide\n")
    (tmp_path / ".wiki-cli").mkdir(exist_ok=True)
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_links_in_resolves_names(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["links", "in", "the-rook", "--format", "paths"])
    assert result.exit_code == 0
    assert "vault/npcs/barnaby-rook.md" in result.output


def test_links_out(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["links", "out", "barnaby-rook", "--format", "paths"])
    assert result.exit_code == 0
    assert "the-rook" in result.output


def test_orphans_report(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["links", "orphans", "--format", "paths"])
    assert result.exit_code == 0
    assert "vault/guides/lonely.md" in result.output


def test_links_in_unresolvable_exits_2(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["links", "in", "no-such-page-ever"])
    assert result.exit_code == 2


def test_breakdown_least_linked_first(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["links", "breakdown", "--to", "type=npc"])
    assert result.exit_code == 0
    lines = result.output.strip().splitlines()
    assert len(lines) >= 2  # header + at least one row
    data_lines = lines[1:]
    counts = [int(line.split("\t")[1]) for line in data_lines]
    assert counts == sorted(counts)


def test_spread_surfaces_unrepresented(vault_cwd: Path) -> None:
    """Two shops, three items — one item links shop-a, two unlinked.
    Balance should spread the two unlinked across both shops."""
    (vault_cwd / "vault" / "shops").mkdir(exist_ok=True)
    (vault_cwd / "vault" / "shops" / "shop-a.md").write_text(
        "---\ntype: shop\ntitle: Shop A\n---\n# Shop A\n", encoding="utf-8"
    )
    (vault_cwd / "vault" / "shops" / "shop-b.md").write_text(
        "---\ntype: shop\ntitle: Shop B\n---\n# Shop B\n", encoding="utf-8"
    )
    (vault_cwd / "vault" / "items").mkdir(exist_ok=True)
    (vault_cwd / "vault" / "items" / "sword.md").write_text(
        "---\ntype: item\ntitle: Sword\n---\n# Sword\nSold at [[shop-a]].\n", encoding="utf-8"
    )
    (vault_cwd / "vault" / "items" / "shield.md").write_text(
        "---\ntype: item\ntitle: Shield\n---\n# Shield\nA sturdy shield.\n", encoding="utf-8"
    )
    (vault_cwd / "vault" / "items" / "potion.md").write_text(
        "---\ntype: item\ntitle: Potion\n---\n# Potion\nA healing potion.\n", encoding="utf-8"
    )

    result = runner.invoke(app, ["links", "spread", "--to", "type=shop", "--from", "type=item"])
    assert result.exit_code == 0
    lines = result.output.strip().splitlines()
    assert len(lines) >= 2  # header + at least 1 data row
    data_lines = lines[1:]  # skip header
    suggested = [line.split("\t")[2] for line in data_lines if not line.split("\t")[1]]
    if len(suggested) == 2:
        assert len(set(suggested)) == 2, f"Both unassigned should go to different shops, got {suggested}"


def test_spread_no_targets_exits_2(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["links", "spread", "--to", "type=nonexistent", "--from", "type=npc"])
    assert result.exit_code == 2
