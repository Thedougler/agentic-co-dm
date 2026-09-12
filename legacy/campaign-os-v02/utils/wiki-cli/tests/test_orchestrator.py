"""TDD for the orchestrator: findings cache wiring + all-tier reporting.

`FrontmatterSchemaRule` (W84, `pure=False`) supplies the real structural
finding — it resolves templates via a fresh `load_config()` call of its
own (see `rules/frontmatter_schema.py`), so it reads the REAL
`vault/_templates/` regardless of the isolated `Config` these tests build,
exactly like `test_frontmatter_schema.py` already relies on. Because W84
is impure, it can never exercise the cache — so a minimal test-only
`pure=True` `FileRule` is registered here (as the port-task shared-shape
explicitly sanctions) to prove caching and tier suppression together: it
fires whenever a page's body contains a marker string, at `Tier.
CONTENT_SHAPE`, so `violating.md` (missing `north_of` AND carrying the
marker) trips both tiers on one file. A second test-only rule fires at
`Tier.STRUCTURAL`, standing in for the
pending-link family (W125), which reports like every other finding
the same file's lower tiers.

Every `run_lint` call here scopes `producers` to `"wiki"` (the native rule
producer) plus `"test-tiers"` (the two test-only rules above): this suite's
`vault` fixture is an isolated `tmp_path` tree with no real `node_modules`
or `.obsidian-linter.jsonc` under it, so an external producer (e.g.
`markdownlint`, W87) would fail outright. A case that needs the test rules
alone, with no real rule's findings landing on the same file, scopes to
`"test-tiers"` by itself.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from wiki_cli.config import Config
from wiki_cli.contracts import (
    TIER_ORDER,
    Corpus,
    FileRule,
    Finding,
    Page,
    Severity,
    Tier,
    register,
)
from wiki_cli.orchestrator import run_lint

FIXTURES = Path(__file__).parent / "fixtures" / "orchestrator"

_MARKER = "ORCHESTRATOR_TEST_MARKER"


@register
class _MarkerContentShapeRule(FileRule):
    """Test-only rule: fires once at CONTENT_SHAPE whenever `_MARKER`
    appears in the page body. `pure=True` so it is the cache's only real
    exerciser here — W84 (the real structural rule these tests also rely
    on) is `pure=False` and never touches the cache."""

    id = "TEST-CONTENT-SHAPE-MARKER"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Remove the marker string from the fixture body (test-only rule)."
    producer = "test-tiers"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> list[Finding]:
        del corpus
        if _MARKER in page.body:
            return [self.finding(file=page.rel_path, line=page.body_start_line, message=_MARKER)]
        return []


_PENDING_MARKER = "ORCHESTRATOR_TEST_PENDING_LINK"


@register
class _MarkerPendingLinkRule(FileRule):
    """Test-only stand-in for the pending-target family (W125):
    a STRUCTURAL rule reported alongside the same file's CONTENT_SHAPE findings."""

    id = "TEST-PENDING-LINK-MARKER"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "Remove the pending-link marker from the fixture body (test-only rule)."
    producer = "test-tiers"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> list[Finding]:
        del corpus
        if _PENDING_MARKER in page.body:
            return [
                self.finding(
                    file=page.rel_path,
                    line=page.body_start_line,
                    message=_PENDING_MARKER,
                )
            ]
        return []


def _config(root: Path) -> Config:
    return Config(
        repo_root=root,
        vault_root=root / "vault",
        templates_root=root / "vault" / "_templates",
        cache_path=root / "cache.sqlite3",
        scoped_roots=("vault",),
        report_cap=50,
        fingerprint="test-fingerprint",
        _thresholds={},
    )


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    dest = tmp_path / "vault" / "orchestrator"
    dest.mkdir(parents=True)
    shutil.copytree(FIXTURES, dest, dirs_exist_ok=True)
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    return tmp_path


def test_every_tier_reports_in_one_run(vault: Path) -> None:
    """A file tripping both a STRUCTURAL and a CONTENT_SHAPE rule reports
    both in the same run — nothing is held back for a second pass."""
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "violating.md"

    result = run_lint(config, [target], producers=["wiki", "test-tiers"])

    assert {"W84", "TEST-CONTENT-SHAPE-MARKER"} <= {f.rule_id for f in result.findings}


def test_findings_are_sorted_worst_tier_first(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "violating.md"

    result = run_lint(config, [target], producers=["wiki", "test-tiers"])
    tiers = [TIER_ORDER.index(f.tier) for f in result.findings]

    assert tiers == sorted(tiers)


def test_ungated_finding_reports_alongside_lower_tiers_and_withholds_nothing(
    vault: Path,
) -> None:
    """A page whose only STRUCTURAL finding is a pending link still gets its
    CONTENT_SHAPE findings reported — both are listed, nothing is withheld."""
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"
    target.write_text(
        target.read_text(encoding="utf-8") + f"\n{_PENDING_MARKER}\n{_MARKER}\n",
        encoding="utf-8",
    )

    # Only the two test rules run: the real `wiki` rules would add STRUCTURAL
    # findings of their own to this fixture and gate the CONTENT_SHAPE one
    # for a reason that has nothing to do with the behaviour under test.
    result = run_lint(config, [target], producers=["test-tiers"])

    assert {"TEST-PENDING-LINK-MARKER", "TEST-CONTENT-SHAPE-MARKER"} <= {
        f.rule_id for f in result.findings
    }


def test_ungated_finding_reports_beside_a_real_structural_finding(vault: Path) -> None:
    """A genuine gating STRUCTURAL finding on the same file changes
    nothing about what else that file reports."""
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "violating.md"
    target.write_text(
        target.read_text(encoding="utf-8") + f"\n{_PENDING_MARKER}\n",
        encoding="utf-8",
    )

    result = run_lint(config, [target], producers=["wiki", "test-tiers"])
    reported = {f.rule_id for f in result.findings}

    assert {"W84", "TEST-PENDING-LINK-MARKER", "TEST-CONTENT-SHAPE-MARKER"} <= reported


def test_clean_page_yields_no_findings(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"

    result = run_lint(config, [target], producers=["wiki", "test-tiers"])

    known_ids = {"W84", "TEST-CONTENT-SHAPE-MARKER"}
    relevant = [f for f in result.findings if f.rule_id in known_ids]
    assert relevant == []


def test_cache_hits_on_second_run(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"

    first = run_lint(config, [target], producers=["wiki", "test-tiers"])
    second = run_lint(config, [target], producers=["wiki", "test-tiers"])

    assert first.stats.cache_hits == 0
    assert second.stats.cache_hits > 0
    assert second.findings == first.findings


def test_cache_busts_on_file_edit(tmp_path: Path) -> None:
    vault_dir = tmp_path / "vault" / "orchestrator"
    vault_dir.mkdir(parents=True)
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    target = vault_dir / "clean.md"
    shutil.copy(FIXTURES / "clean.md", target)
    config = _config(tmp_path)

    first = run_lint(config, [target], producers=["wiki", "test-tiers"])
    first_marker = [f for f in first.findings if f.rule_id == "TEST-CONTENT-SHAPE-MARKER"]
    assert first_marker == []

    original = target.read_text(encoding="utf-8")
    target.write_text(original + f"\n{_MARKER}\n", encoding="utf-8")

    second = run_lint(config, [target], producers=["wiki", "test-tiers"])

    assert second.stats.cache_hits == 0
    assert "TEST-CONTENT-SHAPE-MARKER" in {f.rule_id for f in second.findings}
