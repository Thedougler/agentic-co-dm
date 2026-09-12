"""CLI tests for `wiki search`."""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from wiki_cli.cli import app
from wiki_cli.query.qmd import QmdHit, QmdNotFoundError

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
    _write(tmp_path / "vault" / "_templates" / "_guide.md", "type: guide")
    _write(tmp_path / "vault" / "npcs" / "the-rook.md", "type: npc", "# The Rook\n")
    _write(tmp_path / "vault" / "guides" / "guide.md", "type: guide", "# Guide\n")
    (tmp_path / ".wiki-cli").mkdir(exist_ok=True)
    (tmp_path / "utils").mkdir(exist_ok=True)
    (tmp_path / "utils" / "qmd-collections.yml").write_text(
        'collections:\n  content:\n    path: "{{REPO}}/vault"\n    pattern: "**/*.md"\n',
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_search_joins_and_filters(vault_cwd: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    hits = [
        QmdHit("vault/npcs/the-rook.md", "content", 0.9, 1, "The Rook", ""),
        QmdHit("vault/guides/guide.md", "content", 0.8, 1, "Guide", ""),
    ]
    monkeypatch.setattr("wiki_cli.query.qmd.run_qmd", lambda *a, **k: hits)
    result = runner.invoke(app, ["search", "rook", "--where", "type=npc", "--format", "paths"])
    assert result.exit_code == 0, result.output
    lines = [line for line in result.output.strip().split("\n") if line]
    assert lines == ["vault/npcs/the-rook.md"]


def test_search_missing_binary_exit_2(vault_cwd: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    def boom(*a: object, **k: object) -> list[QmdHit]:
        raise QmdNotFoundError("wiki search needs the qmd CLI on PATH")

    monkeypatch.setattr("wiki_cli.query.qmd.run_qmd", boom)
    result = runner.invoke(app, ["search", "rook"])
    assert result.exit_code == 2
    assert "qmd" in result.output


def test_qmd_hit_parsing() -> None:
    sample = [
        {
            "docid": "#1cec55",
            "score": 0.93,
            "file": "qmd://content/campaigns/shattered-sea/vehicles/dead-lady.md",
            "line": 6,
            "title": "The *Dead Lady*",
            "snippet": "...",
        }
    ]
    item = sample[0]
    file_uri = item["file"]
    rest = file_uri[len("qmd://") :]
    coll, _, rel = rest.partition("/")
    assert coll == "content"
    assert rel == "campaigns/shattered-sea/vehicles/dead-lady.md"
    hit = QmdHit(
        rel_path=f"vault/{rel}",
        collection=coll,
        score=float(item["score"]),
        line=int(item["line"]),
        title=str(item["title"]),
        snippet=str(item["snippet"]),
    )
    assert hit.rel_path == "vault/campaigns/shattered-sea/vehicles/dead-lady.md"
    assert hit.score == 0.93


def test_search_xml_rejects_where(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["search", "--xml", "--where", "type=npc", "query", "test"])
    assert result.exit_code == 2


def test_search_no_query_exits_2(vault_cwd: Path) -> None:
    result = runner.invoke(app, ["search"])
    assert result.exit_code == 2
