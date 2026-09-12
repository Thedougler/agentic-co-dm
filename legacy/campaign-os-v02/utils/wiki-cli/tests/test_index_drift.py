"""TDD for `wiki/index-drift` (wiki-lint migration plan Task 29) — a new
VaultRule with no npm parity. Fixtures live under
`tests/fixtures/index_drift/vault/`, built through a real `VaultIndex` so
the check exercises real page mtimes on disk; the sync-marker file is a
throwaway under `tmp_path`, pointed to via `WIKI_CLI_QMD_SYNC_MARKER` so
each test controls "when search:sync last ran" precisely with `os.utime`.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.contracts import Finding, registry
from wiki_cli.index import VaultIndex
from wiki_cli.rules.index_drift import _MARKER_ENV

FIXTURES = Path(__file__).parent / "fixtures" / "index_drift"
VAULT = FIXTURES / "vault"
RULE_ID = "wiki/index-drift"

_PAGE_ONE = VAULT / "page-one.md"
_PAGE_TWO = VAULT / "page-two.md"

# Arbitrary fixed instants, far enough apart that filesystem mtime
# resolution never collapses "before" and "after" into the same tick.
_MARKER_TIME = 1_700_000_000.0
_BEFORE_MARKER = _MARKER_TIME - 1000.0
_AFTER_MARKER = _MARKER_TIME + 1000.0


def _set_mtime(path: Path, when: float) -> None:
    os.utime(path, (when, when))


def _corpus() -> VaultIndex:
    return VaultIndex.build(FIXTURES, VAULT, ("vault",))


def _findings() -> list[Finding]:
    rule = registry()[RULE_ID]
    return list(rule.check(_corpus()))


@pytest.fixture(autouse=True)
def _reset_page_mtimes() -> None:
    """Every page starts older than the marker; individual tests promote
    the ones they want to count as stale."""
    _set_mtime(_PAGE_ONE, _BEFORE_MARKER)
    _set_mtime(_PAGE_TWO, _BEFORE_MARKER)


@pytest.fixture
def marker(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    marker_path = tmp_path / "index.yml"
    marker_path.write_text("collections: {}\n", encoding="utf-8")
    _set_mtime(marker_path, _MARKER_TIME)
    monkeypatch.setenv(_MARKER_ENV, str(marker_path))
    return marker_path


def test_page_newer_than_marker_fires_with_stale_count(marker: Path) -> None:
    _set_mtime(_PAGE_ONE, _AFTER_MARKER)

    findings = _findings()

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == RULE_ID
    assert finding.file == "vault/page-one.md"
    assert "1 vault page(s)" in finding.message


def test_all_pages_older_than_marker_stays_silent(marker: Path) -> None:
    assert _findings() == []


def test_message_includes_fix_line(marker: Path) -> None:
    _set_mtime(_PAGE_ONE, _AFTER_MARKER)
    _set_mtime(_PAGE_TWO, _AFTER_MARKER)

    findings = _findings()

    assert len(findings) == 1
    assert "2 vault page(s)" in findings[0].message
    assert "FIX: run npm run search:sync" in findings[0].message


def test_missing_marker_treats_every_page_as_stale(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    never_written = tmp_path / "never-synced" / "index.yml"
    monkeypatch.setenv(_MARKER_ENV, str(never_written))

    findings = _findings()

    assert len(findings) == 1
    assert "2 vault page(s)" in findings[0].message


def test_rule_is_registered_warning_structural(marker: Path) -> None:
    del marker
    rule = registry()[RULE_ID]
    assert rule.severity == "warning"
    assert rule.tier == "structural"
    assert rule.pure is False
    assert rule.fix.startswith("Run `npm run search:sync`")
