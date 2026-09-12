"""TDD for the duplication producer (W83).

Runs against the REAL repo root, not an isolated tmp fixture — same
constraint `test_producers_markdownlint.py` documents for W87: the
subprocess needs the real system-installed jscpd binary (resolved off
`PATH`) and the real `.jscpd.json` to prove parity with the legacy engine,
so the fixtures live under this repo's own tree
(`tests/fixtures/producers/duplication/`).

Fixture note: `.jscpd.json`'s defaults are `minLines: 3, minTokens: 50`, and
this jscpd build's markdown extractor only registers a file with detectable
content when it contains a fenced code block (pure prose alone yields zero
extracted tokens) — every fixture here carries a code fence long enough to
clear both floors.
"""

from __future__ import annotations

from pathlib import Path

from wiki_cli.config import Config
from wiki_cli.contracts import Page
from wiki_cli.orchestrator import run_lint
from wiki_cli.producers import all_producers
from wiki_cli.producers.duplication import FAMILY_ID, run

_REPO_ROOT = Path(__file__).resolve().parents[3]
"""tests/test_producers_duplication.py -> utils/wiki-cli/tests -> utils/wiki-cli
-> repo root, 3 parents up."""

FIXTURES = _REPO_ROOT / "utils" / "wiki-cli" / "tests" / "fixtures" / "producers" / "duplication"


class _StubCorpus:
    """Satisfies the `Corpus` protocol structurally — this producer only
    ever reads `repo_root` off it, so every other method is an
    intentionally unreachable stub, kept only so real callers (and
    pyright) see a real `Corpus`."""

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


def _config(repo_root: Path, thresholds: dict[str, str] | None = None) -> Config:
    return Config(
        repo_root=repo_root,
        vault_root=repo_root / "vault",
        templates_root=repo_root / "vault" / "_templates",
        cache_path=repo_root / ".wiki-cli-test-cache.sqlite3",
        scoped_roots=("vault",),
        report_cap=50,
        fingerprint="test-fingerprint",
        _thresholds=thresholds or {},
    )


def test_family_id_is_w83() -> None:
    assert FAMILY_ID == "W83"


def test_registers_in_producers_registry() -> None:
    assert all_producers()["W83"] is run


def test_real_clone_pair_yields_one_w83_finding() -> None:
    targets = [FIXTURES / "clone-a.md", FIXTURES / "clone-b.md"]

    findings = run(_config(_REPO_ROOT), targets, _StubCorpus(_REPO_ROOT))

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W83"
    assert finding.producer == "duplication"
    assert finding.tier.value == "content-shape"
    assert finding.severity.value == "warning"
    assert finding.fixable is False
    assert finding.file == str((FIXTURES / "clone-a.md").relative_to(_REPO_ROOT))
    assert "clone-b.md" in finding.message


def test_known_boilerplate_pair_is_exempted() -> None:
    """`exempt-a.md`/`exempt-b.md` carry the leaflet Map block's
    `zoomDelta: 0.125` signature — a real jscpd clone that must never
    surface as a finding."""
    targets = [FIXTURES / "exempt-a.md", FIXTURES / "exempt-b.md"]

    findings = run(_config(_REPO_ROOT), targets, _StubCorpus(_REPO_ROOT))

    assert findings == []


def test_empty_targets_is_a_noop() -> None:
    assert run(_config(_REPO_ROOT), [], _StubCorpus(_REPO_ROOT)) == []


def test_configured_known_boilerplate_overrides_default() -> None:
    """A `DUPLICATION_KNOWN_BOILERPLATE` threshold, once `wiki.toml` carries
    one, must take over from the hardcoded fallback list — proven here by
    configuring a signature that exempts the real (normally non-exempt)
    clone-a/clone-b pair."""
    config = _config(_REPO_ROOT, thresholds={"DUPLICATION_KNOWN_BOILERPLATE": "alpha: one"})
    targets = [FIXTURES / "clone-a.md", FIXTURES / "clone-b.md"]

    findings = run(config, targets, _StubCorpus(_REPO_ROOT))

    assert findings == []


def test_orchestrator_merges_producer_findings_into_lint_result() -> None:
    config = Config(
        repo_root=_REPO_ROOT,
        vault_root=_REPO_ROOT / "vault",
        templates_root=_REPO_ROOT / "vault" / "_templates",
        cache_path=_REPO_ROOT / "utils" / "wiki-cli" / ".wiki-cli-test-cache.sqlite3",
        scoped_roots=("vault", "utils/wiki-cli/tests"),
        report_cap=50,
        fingerprint="test-fingerprint-producers-duplication",
        _thresholds={},
    )

    result = run_lint(
        config, [FIXTURES / "clone-a.md", FIXTURES / "clone-b.md"]
    )

    w83 = [f for f in result.findings if f.rule_id == "W83"]
    assert len(w83) == 1
    assert w83[0].producer == "duplication"
    assert "W83" in result.stats.per_producer_seconds
    config.cache_path.unlink(missing_ok=True)
