"""Tests for the W128 (PATH_WIKILINK) lint rule and the ``wiki slug-scrub`` command."""
from __future__ import annotations

import shutil
from pathlib import Path

import pytest
from typer.testing import CliRunner

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.cli import app
from wiki_cli.contracts import Severity, Tier, registry
from wiki_cli.index import VaultIndex
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "path_wikilink"
runner = CliRunner()


def _corpus(fixtures: Path = FIXTURES) -> VaultIndex:
    return VaultIndex.build(fixtures, fixtures / "vault", ("vault",))


def _check_file(rel_path: str) -> list:
    rule = registry()["W128"]
    page = load_page(FIXTURES, rel_path)
    return list(rule.check(page, _corpus()))


# --- W128 rule: detection ---


def test_w128_flags_path_qualified_inline_link() -> None:
    findings = _check_file("vault/w128/path-based-links.md")
    path_links = [f for f in findings if "npcs/barnaby-rook" in f.message]
    assert path_links, f"Expected finding for [[npcs/barnaby-rook|...]], got: {findings}"


def test_w128_flags_path_qualified_bare_link() -> None:
    findings = _check_file("vault/w128/path-based-links.md")
    bare = [f for f in findings if "factions/chain-council" in f.message]
    assert bare, f"Expected finding for [[factions/chain-council]], got: {findings}"


def test_w128_flags_path_qualified_link_with_heading() -> None:
    findings = _check_file("vault/w128/path-based-links.md")
    headed = [f for f in findings if "locations/midchain/sparhold" in f.message]
    assert headed, f"Expected finding for [[locations/midchain/sparhold#...]], got: {findings}"


def test_w128_silent_on_slug_only_links() -> None:
    findings = _check_file("vault/w128/slug-only-links.md")
    assert findings == [], f"Expected no findings for slug-only links, got: {findings}"


def test_w128_is_structural_error() -> None:
    rule = registry()["W128"]
    assert rule.tier == Tier.STRUCTURAL
    assert rule.severity == Severity.ERROR


def test_w128_is_pure() -> None:
    rule = registry()["W128"]
    assert rule.pure is True


def test_w128_finding_names_bare_slug_in_message() -> None:
    findings = _check_file("vault/w128/path-based-links.md")
    rook = [f for f in findings if "barnaby-rook" in f.message]
    assert rook, "message should include the bare slug as the corrected form"


def test_w128_skips_non_vault_files(tmp_path: Path) -> None:
    """Rule must only fire for vault/ files."""
    rule = registry()["W128"]
    md = tmp_path / "docs" / "note.md"
    md.parent.mkdir()
    md.write_text("See [[some/path/file|Display]].\n")
    from wiki_cli.markdown import load_page as _load

    page = _load(tmp_path, "docs/note.md")
    findings = list(rule.check(page, _corpus()))
    assert findings == [], "W128 must not fire outside vault/"


# --- slug-scrub command ---


@pytest.fixture()
def scrub_vault(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A writable copy of the path_wikilink fixture vault, with wiki.toml."""
    shutil.copytree(FIXTURES / "vault" / "w128", tmp_path / "vault" / "w128", dirs_exist_ok=True)
    (tmp_path / "wiki.toml").write_text(
        '[vault]\nroot = "vault"\ntemplates = "vault/_templates"\n'
        '[cache]\npath = ".wiki-cli/cache.sqlite3"\n',
        encoding="utf-8",
    )
    (tmp_path / "vault" / "_templates").mkdir(exist_ok=True)
    monkeypatch.chdir(tmp_path)
    return tmp_path


@pytest.fixture()
def collision_vault(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Vault with duplicate basenames to trigger slug-scrub's uniqueness pre-check."""
    vault = tmp_path / "vault"
    shutil.copytree(FIXTURES / "vault" / "collision", vault / "collision", dirs_exist_ok=True)
    (tmp_path / "wiki.toml").write_text(
        '[vault]\nroot = "vault"\ntemplates = "vault/_templates"\n'
        '[cache]\npath = ".wiki-cli/cache.sqlite3"\n',
        encoding="utf-8",
    )
    (tmp_path / "vault" / "_templates").mkdir(exist_ok=True)
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_slug_scrub_rewrites_path_links(scrub_vault: Path) -> None:
    result = runner.invoke(app, ["slug-scrub"])
    assert result.exit_code == 0, result.output

    rewritten = (scrub_vault / "vault" / "w128" / "path-based-links.md").read_text()
    assert "[[barnaby-rook|Barnaby Rook]]" in rewritten
    assert "[[chain-council]]" in rewritten
    assert "npcs/" not in rewritten
    assert "factions/" not in rewritten


def test_slug_scrub_preserves_heading_and_display(scrub_vault: Path) -> None:
    result = runner.invoke(app, ["slug-scrub"])
    assert result.exit_code == 0

    rewritten = (scrub_vault / "vault" / "w128" / "path-based-links.md").read_text()
    assert "[[sparhold#The Docks|Sparhold Docks]]" in rewritten


def test_slug_scrub_dry_run_does_not_write(scrub_vault: Path) -> None:
    original = (scrub_vault / "vault" / "w128" / "path-based-links.md").read_text()
    result = runner.invoke(app, ["slug-scrub", "--dry-run"])
    assert result.exit_code == 0

    after = (scrub_vault / "vault" / "w128" / "path-based-links.md").read_text()
    assert after == original, "--dry-run must not modify files"
    assert "dry-run" in result.output.lower() or "dry_run" in result.output.lower()


def test_slug_scrub_leaves_slug_only_file_unchanged(scrub_vault: Path) -> None:
    # Copy the slug-only fixture into the scrub vault too
    shutil.copy(
        FIXTURES / "vault" / "w128" / "slug-only-links.md",
        scrub_vault / "vault" / "w128" / "slug-only-links.md",
    )
    original = (scrub_vault / "vault" / "w128" / "slug-only-links.md").read_text()
    result = runner.invoke(app, ["slug-scrub"])
    assert result.exit_code == 0

    after = (scrub_vault / "vault" / "w128" / "slug-only-links.md").read_text()
    assert after == original, "slug-only file must not be modified"


def test_slug_scrub_errors_on_slug_collision(collision_vault: Path) -> None:
    result = runner.invoke(app, ["slug-scrub"])
    assert result.exit_code != 0, "slug-scrub must fail when basename collisions exist"
    assert "collision" in result.output.lower() or "collision" in (result.stderr or "").lower()


def test_slug_scrub_after_scrub_lint_clean(scrub_vault: Path) -> None:
    """After slug-scrub, W128 must report zero findings on the vault."""
    result = runner.invoke(app, ["slug-scrub"])
    assert result.exit_code == 0

    lint_result = runner.invoke(app, ["lint", str(scrub_vault / "vault")])
    w128_findings = [
        line for line in lint_result.output.splitlines() if "W128" in line
    ]
    assert w128_findings == [], f"Expected zero W128 findings after scrub, got: {w128_findings}"
