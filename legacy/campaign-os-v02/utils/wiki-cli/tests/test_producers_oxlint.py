"""TDD for the oxlint producer (W82).

Runs against the REAL repo root, not an isolated tmp fixture — same
constraint `test_producers_markdownlint.py` documents: the subprocess needs
the real `oxlint` binary (from the PyPI package installed in this venv)
and the real `.oxlintrc.json` to prove parity with the legacy engine, so
the fixtures live under this repo's own tree
(`tests/fixtures/producers/oxlint/`) rather than a copied tmp vault.
"""

from __future__ import annotations

from pathlib import Path

from wiki_cli.config import Config
from wiki_cli.contracts import Page
from wiki_cli.orchestrator import run_lint
from wiki_cli.producers import all_producers
from wiki_cli.producers.oxlint import FAMILY_ID, run

_REPO_ROOT = Path(__file__).resolve().parents[3]
"""tests/test_producers_oxlint.py -> utils/wiki-cli/tests -> utils/wiki-cli
-> repo root, 3 parents up."""

FIXTURES = _REPO_ROOT / "utils" / "wiki-cli" / "tests" / "fixtures" / "producers" / "oxlint"


class _StubCorpus:
    """Satisfies the `Corpus` protocol structurally — this producer only
    ever reads `repo_root` off it (see its `del config` / never touching
    `corpus` beyond that), so every other method is an intentionally
    unreachable stub, kept only so real callers (and pyright) see a real
    `Corpus`."""

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


def _config(repo_root: Path) -> Config:
    """The producer never reads `config` (see its `del config`) — a
    minimal real `Config` proves that without depending on `wiki.toml`."""
    return Config(
        repo_root=repo_root,
        vault_root=repo_root / "vault",
        templates_root=repo_root / "vault" / "_templates",
        cache_path=repo_root / ".wiki-cli-test-cache.sqlite3",
        scoped_roots=("vault",),
        report_cap=50,
        fingerprint="test-fingerprint",
        _thresholds={},
    )


def test_family_id_is_w82() -> None:
    assert FAMILY_ID == "W82"


def test_registers_in_producers_registry() -> None:
    assert all_producers()["W82"] is run


def test_broken_fixture_yields_one_w82_finding_with_rule_slug_in_message() -> None:
    target = FIXTURES / "broken.mjs"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(_REPO_ROOT))

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W82"
    assert finding.producer == "oxlint"
    assert finding.tier.value == "structural"
    assert finding.severity.value == "error"
    assert "no-unreachable" in finding.message
    assert finding.file == str(target.relative_to(_REPO_ROOT))


def test_clean_fixture_yields_no_findings() -> None:
    target = FIXTURES / "clean.mjs"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(_REPO_ROOT))

    assert findings == []


def test_empty_targets_is_a_noop() -> None:
    assert run(_config(_REPO_ROOT), [], _StubCorpus(_REPO_ROOT)) == []


def test_orchestrator_merges_producer_findings_into_lint_result() -> None:
    config = Config(
        repo_root=_REPO_ROOT,
        vault_root=_REPO_ROOT / "vault",
        templates_root=_REPO_ROOT / "vault" / "_templates",
        cache_path=_REPO_ROOT / "utils" / "wiki-cli" / ".wiki-cli-test-cache.sqlite3",
        scoped_roots=("vault", "utils/wiki-cli/tests"),
        report_cap=50,
        fingerprint="test-fingerprint-producers-oxlint",
        _thresholds={},
    )

    result = run_lint(config, [FIXTURES / "broken.mjs"])

    w82 = [f for f in result.findings if f.rule_id == "W82"]
    assert len(w82) == 1
    assert w82[0].producer == "oxlint"
    assert "W82" in result.stats.per_producer_seconds
    config.cache_path.unlink(missing_ok=True)
