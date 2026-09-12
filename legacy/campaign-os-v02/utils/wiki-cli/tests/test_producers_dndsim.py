"""TDD for the dndsim in-process merge producer (Task 23 of the wiki-lint
migration plan; ADR-0010, ADR-0015, ADR-0041).

Fixtures live under this repo's own tree
(`tests/fixtures/producers/dndsim/`) rather than reusing dndsim's own
(`utils/dndsim/tests/lint/fixtures/`) — this producer's rel-path mapping is
`corpus.repo_root`-relative, distinct from dndsim's module-level
`REPO_ROOT`, and needs proving independently of dndsim's own test suite.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from wiki_cli.config import Config
from wiki_cli.contracts import Page, Severity, Tier
from wiki_cli.producers import all_producers
from wiki_cli.producers.dndsim import _ENV_FLAG, FAMILY_ID, run

_REPO_ROOT = Path(__file__).resolve().parents[3]
"""tests/test_producers_dndsim.py -> utils/wiki-cli/tests -> utils/wiki-cli
-> repo root, 3 parents up."""

FIXTURES = _REPO_ROOT / "utils" / "wiki-cli" / "tests" / "fixtures" / "producers" / "dndsim"
BROKEN_STATBLOCK = FIXTURES / "vault" / "srd" / "monsters" / "statblock-broken.md"
CLEAN_STATBLOCK = FIXTURES / "vault" / "srd" / "monsters" / "statblock-clean.md"


class _StubCorpus:
    """See test_producers_markdownlint.py's identical stub — this producer
    also only ever reads `repo_root` off the corpus."""

    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root

    def pages(self) -> list[Page]:
        raise NotImplementedError

    def resolve(self, name: str) -> Page | None:
        raise NotImplementedError

    def by_type(self, page_type: str) -> list[Page]:
        raise NotImplementedError

    def links_from(self, rel_path: str) -> list[str]:
        raise NotImplementedError

    def links_to(self, rel_path: str) -> list[str]:
        raise NotImplementedError


def _config() -> Config:
    """The producer never reads `config` (see its `del config`) — a
    minimal real `Config` proves that without depending on `wiki.toml`."""
    return Config(
        repo_root=_REPO_ROOT,
        vault_root=_REPO_ROOT / "vault",
        templates_root=_REPO_ROOT / "vault" / "_templates",
        cache_path=_REPO_ROOT / ".wiki-cli-test-cache.sqlite3",
        scoped_roots=("vault",),
        report_cap=50,
        fingerprint="test-fingerprint",
        _thresholds={},
    )


@pytest.fixture
def dndsim_enabled(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(_ENV_FLAG, "1")


def test_family_id_is_dndsim() -> None:
    assert FAMILY_ID == "dndsim"


def test_registers_in_producers_registry() -> None:
    assert all_producers()["dndsim"] is run


def test_disabled_by_default_even_on_a_broken_fixture(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(_ENV_FLAG, raising=False)

    assert run(_config(), [BROKEN_STATBLOCK], _StubCorpus(FIXTURES)) == []


def test_falsy_env_value_still_disables(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(_ENV_FLAG, "0")

    assert run(_config(), [BROKEN_STATBLOCK], _StubCorpus(FIXTURES)) == []


def test_empty_targets_is_a_noop(dndsim_enabled: None) -> None:
    assert run(_config(), [], _StubCorpus(FIXTURES)) == []


def test_broken_statblock_fixture_yields_one_structural_finding(dndsim_enabled: None) -> None:
    findings = run(_config(), [BROKEN_STATBLOCK], _StubCorpus(FIXTURES))

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "dndsim"
    assert finding.producer == "dndsim"
    assert finding.tier == Tier.STRUCTURAL
    assert finding.severity == Severity.ERROR
    assert "W-statblock-simulatable" in finding.message
    assert 'missing required key "ac"' in finding.message
    assert finding.file == str(BROKEN_STATBLOCK.relative_to(FIXTURES))


def test_clean_statblock_fixture_yields_no_findings(dndsim_enabled: None) -> None:
    assert run(_config(), [CLEAN_STATBLOCK], _StubCorpus(FIXTURES)) == []


def test_target_outside_scoped_content_roots_is_silent(dndsim_enabled: None) -> None:
    # Same broken fixture, but its repo_root-relative path becomes
    # "dndsim/vault/srd/monsters/statblock-broken.md" — never starts
    # with "vault/srd/monsters/", so dndsim's own STATBLOCK_ROOTS check
    # never fires. Proves this producer computes `rel` from `corpus.
    # repo_root`, not a hardcoded prefix.
    findings = run(_config(), [BROKEN_STATBLOCK], _StubCorpus(FIXTURES.parent))
    assert findings == []


def test_target_outside_corpus_repo_root_is_skipped(tmp_path: Path, dndsim_enabled: None) -> None:
    outsider = tmp_path / "content" / "monsters" / "srd" / "ghost.md"
    findings = run(_config(), [outsider], _StubCorpus(FIXTURES))
    assert findings == []


def test_real_vault_layout_never_matches_dndsim_scoped_roots(dndsim_enabled: None) -> None:
    # Against the REAL repo root, this fixture's rel path lives under
    # utils/wiki-cli/tests/fixtures/..., not content/monsters/srd/ — and
    # even a real vault page (vault/srd/monsters/...) would not match
    # either. This is why a normal `wiki lint` sweep already excludes
    # dndsim findings today: the legacy engine's own default sweep does
    # too (`utils/scripts/lib/lint-findings.mjs`'s `collectFindings` only
    # calls `runDndsimLint` when `includeDndsim` is explicitly passed).
    findings = run(_config(), [BROKEN_STATBLOCK], _StubCorpus(_REPO_ROOT))
    assert findings == []
