"""TDD for the callout-fragment glob exclusion (ADR-0053, issue #02).

Files matching ``-c\\d{2,}\\.md$`` are callout fragment files — pure content
blocks with no frontmatter. All ``page_level`` FileRules are skipped for
these files by the orchestrator, without each rule needing its own
fragment-pattern check.

Two fixtures are created in tmp_path:
- ``vault/foo-c01.md`` (fragment, named per the convention) — with a marker
  string in its body that would normally trigger the test-only rule and W95.
- ``vault/foo.md`` (regular page) — same marker and same ``type: npc``
  in the wrong folder, so W95 fires.

``TEST-PAGE-LEVEL-MARKER`` is a test-only FileRule with ``page_level = True``
that fires on any page carrying the marker, regardless of type:. It stands
in for a hypothetical "missing type:" rule that would fire even without
frontmatter — proving that the orchestrator-level exclusion, not the rule's
own guard, is what protects the fragment.
"""

from __future__ import annotations

from pathlib import Path

import pytest

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.config import Config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.orchestrator import run_lint

_MARKER = "FRAGMENT_EXCLUSION_TEST_MARKER"

_FRAGMENT_THRESHOLDS = {"CALLOUT_FRAGMENT_PATTERN": r"-c\d{2,}\.md$"}


@register
class _PageLevelMarkerRule(FileRule):
    """Test-only page-level rule: fires on any vault/*.md carrying _MARKER.

    `page_level = True` (the default) so the orchestrator skips it for
    fragment files. No type: check — this is the rule that would otherwise
    fire on a fragment file if the orchestrator weren't doing the exclusion.
    """

    id = "TEST-PAGE-LEVEL-MARKER"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = "Remove the marker from the fixture body (test-only rule)."
    producer = "test-fragment"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> list[Finding]:
        del corpus
        if not page.rel_path.startswith("vault/"):
            return []
        if _MARKER in page.body:
            return [self.finding(file=page.rel_path, line=1, message=_MARKER)]
        return []


def _config(root: Path) -> Config:
    return Config(
        repo_root=root,
        vault_root=root / "vault",
        templates_root=root / "vault" / "_templates",
        cache_path=root / "cache.sqlite3",
        scoped_roots=("vault",),
        report_cap=50,
        fingerprint="test-fragment-fingerprint",
        _thresholds=_FRAGMENT_THRESHOLDS,
    )


@pytest.fixture()
def vault(tmp_path: Path) -> Path:
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir(parents=True)
    return tmp_path


def _fragment_file(vault_root: Path) -> Path:
    """vault/foo-c01.md — a callout fragment (matches ``-c\\d{2,}\\.md$``)."""
    path = vault_root / "vault" / "foo-c01.md"
    path.write_text(f"> [!read-aloud]\n> {_MARKER}\n", encoding="utf-8")
    return path


def _regular_file(vault_root: Path, *, with_type: str | None = None) -> Path:
    """vault/foo.md — a regular vault page (does not match fragment pattern)."""
    path = vault_root / "vault" / "foo.md"
    if with_type:
        path.write_text(
            f"---\ntype: {with_type}\n---\n\n{_MARKER}\n",
            encoding="utf-8",
        )
    else:
        path.write_text(f"{_MARKER}\n", encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Core test: orchestrator skips page_level rules for fragment files
# ---------------------------------------------------------------------------


def test_fragment_file_produces_no_page_level_findings(vault: Path) -> None:
    """A fragment file (matching ``-c\\d{2,}\\.md$``) gets 0 findings from
    page_level rules, even from a rule that fires on any vault page
    regardless of type:."""
    target = _fragment_file(vault)
    config = _config(vault)

    result = run_lint(config, [target], producers=["test-fragment"])
    fragment_findings = [f for f in result.findings if f.rule_id == "TEST-PAGE-LEVEL-MARKER"]
    assert fragment_findings == [], (
        f"fragment file should have 0 page-level findings; got {fragment_findings}"
    )


def test_regular_file_fires_page_level_rule(vault: Path) -> None:
    """A regular vault page (not matching the fragment pattern) fires the
    page-level test rule as normal — the fragment exclusion is file-specific."""
    target = _regular_file(vault)
    config = _config(vault)

    result = run_lint(config, [target], producers=["test-fragment"])
    marker_findings = [f for f in result.findings if f.rule_id == "TEST-PAGE-LEVEL-MARKER"]
    assert len(marker_findings) == 1, (
        f"regular file should fire TEST-PAGE-LEVEL-MARKER once; got {marker_findings}"
    )


# ---------------------------------------------------------------------------
# W95 (type-folder-placement): fragment with type: npc skips placement check
# ---------------------------------------------------------------------------


def test_w95_skips_fragment_even_with_type_frontmatter(vault: Path) -> None:
    """W95 fires when type: npc is in the wrong folder — but not for a
    fragment file, because W95 has page_level = True (the default)."""
    frag = vault / "vault" / "stray-npc-c01.md"
    frag.write_text("---\ntype: npc\n---\n\n> [!read-aloud]\n> text\n", encoding="utf-8")
    # Ensure the mapped home folder exists so W95 would fire on a regular page.
    (vault / "vault" / "campaigns" / "shattered-sea" / "npcs").mkdir(parents=True)

    config = _config(vault)
    result = run_lint(config, [frag], producers=["wiki"])
    w95_findings = [f for f in result.findings if f.rule_id == "W95"]
    assert w95_findings == [], (
        f"W95 should be skipped for fragment file; got {w95_findings}"
    )


def test_w95_fires_on_regular_file_with_wrong_folder(vault: Path) -> None:
    """W95 fires normally on a non-fragment page with type: npc in the
    wrong folder — confirming the fragment exclusion is not a blanket skip."""
    regular = vault / "vault" / "stray-npc.md"
    regular.write_text("---\ntype: npc\n---\n\n# Stray NPC\n\n## Overview\n\ntext\n", encoding="utf-8")
    (vault / "vault" / "campaigns" / "shattered-sea" / "npcs").mkdir(parents=True)

    config = _config(vault)
    result = run_lint(config, [regular], producers=["wiki"])
    w95_findings = [f for f in result.findings if f.rule_id == "W95"]
    assert len(w95_findings) == 1, (
        f"W95 should fire on stray-npc.md; got {w95_findings}"
    )
