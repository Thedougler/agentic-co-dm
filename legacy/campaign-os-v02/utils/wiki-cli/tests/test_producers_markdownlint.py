"""TDD for the markdownlint producer (W87) and the producer framework it
exercises (`wiki_cli.producers`).

Runs against the REAL repo root, not an isolated tmp fixture — same
constraint `test_orchestrator.py` documents for W84 (frontmatter-schema):
`Finding.file` is repo-root-relative, so proving that shape needs a real
`repo_root` to relativize against. Unlike the legacy JS engine, this
producer needs no external binary or config file (pymarkdown's Python API
carries its own rule defaults), so the fixtures live under this repo's own
tree (`tests/fixtures/producers/markdownlint/`) purely for that
repo-root-relative path proof, not for binary/config discovery.
"""

from __future__ import annotations

from pathlib import Path

from wiki_cli.config import Config
from wiki_cli.contracts import Page
from wiki_cli.orchestrator import run_lint
from wiki_cli.producers import all_producers
from wiki_cli.producers.markdownlint import FAMILY_ID, run

_REPO_ROOT = Path(__file__).resolve().parents[3]
"""tests/test_producers_markdownlint.py -> utils/wiki-cli/tests -> utils/wiki-cli
-> repo root, 3 parents up."""

FIXTURES = _REPO_ROOT / "utils" / "wiki-cli" / "tests" / "fixtures" / "producers" / "markdownlint"


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


def test_family_id_is_w87() -> None:
    assert FAMILY_ID == "W87"


def test_registers_in_producers_registry() -> None:
    assert all_producers()["W87"] is run


def test_broken_fixture_yields_one_w87_finding_with_md_id_in_message() -> None:
    target = FIXTURES / "broken.md"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(_REPO_ROOT))

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W87"
    assert finding.producer == "markdownlint"
    assert finding.tier.value == "content-shape"
    assert "MD040" in finding.message
    assert finding.file == str(target.relative_to(_REPO_ROOT))


def test_clean_fixture_yields_no_findings() -> None:
    target = FIXTURES / "clean.md"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(_REPO_ROOT))

    assert findings == []


def test_frontmatter_title_key_does_not_double_count_as_md025() -> None:
    """Every `vault/_templates/` page declares a `title:` frontmatter key
    (present even when empty). pymarkdown's front-matter extension treats
    a present `title` key as an implicit top-level heading by default, so
    it collided with the page's own `# <Name>` H1 and fired a false MD025
    on every single templated page in the vault — confirmed independently
    on two unrelated pages (aruhe.md, midchain-north.md) before the fix."""
    target = FIXTURES / "title-frontmatter.md"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(_REPO_ROOT))

    assert findings == []


def test_docs_guardrails_files_do_not_trigger_md041() -> None:
    """`docs/guardrails/_FORMAT.md` F11 mandates no H1 on a guardrail doc —
    MD041 (first line should be a top-level heading) must stay disabled
    for this directory, verified against a real corpus file rather than a
    fixture since the exemption is keyed off the target's repo-relative
    path."""
    target = _REPO_ROOT / "docs" / "guardrails" / "CODE.md"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(_REPO_ROOT))

    assert not any("MD041" in f.message for f in findings)


def test_claude_md_files_do_not_trigger_md041() -> None:
    """The kit's `CLAUDE.md` KIT CORE block opens with an HTML comment and
    a trigger-restatement line by design, same no-H1 shape as
    `docs/guardrails/**` — MD041 must stay disabled for every
    `CLAUDE.md`, not just the repo root's."""
    root_target = _REPO_ROOT / "CLAUDE.md"
    nested_target = _REPO_ROOT / "utils" / "wiki-cli" / "CLAUDE.md"

    root_findings = run(_config(_REPO_ROOT), [root_target], _StubCorpus(_REPO_ROOT))
    nested_findings = run(_config(_REPO_ROOT), [nested_target], _StubCorpus(_REPO_ROOT))

    assert not any("MD041" in f.message for f in root_findings)
    assert not any("MD041" in f.message for f in nested_findings)


def test_narration_sibling_does_not_trigger_md041() -> None:
    """type: narration files have no H1 by design (ADR-0056). The target is
    a fixture, not a live vault page: the name pattern is what the producer
    keys on, and a real page can be renamed or retired by any content
    session, which would fail this test for a reason it does not test."""
    target = FIXTURES / "e01-run-guide-narration-sample.md"
    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(_REPO_ROOT))
    assert not any("MD041" in f.message for f in findings)


def test_hot_log_keeps_compact_heading_entries() -> None:
    """`hot.md` is an append-only recency log, not narrative prose. Its
    contract is one heading per entry, so consecutive entry headings must
    not become MD022 churn."""
    target = _REPO_ROOT / "hot.md"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(_REPO_ROOT))

    assert not any("MD022" in f.message for f in findings)


def test_empty_targets_is_a_noop() -> None:
    assert run(_config(_REPO_ROOT), [], _StubCorpus(_REPO_ROOT)) == []


def test_batch_of_files_does_not_truncate() -> None:
    """The legacy subprocess implementation shelled ALL targets into one
    `markdownlint-obsidian` invocation and parsed its combined stdout as a
    single JSON blob — past ~64KB of combined output (359+ real files) the
    OS pipe buffer truncated that blob mid-stream and crashed the run.
    pymarkdown's API is called once per target in-process (no subprocess,
    no shared pipe), so a batch this size proves there is no such ceiling
    to hit."""
    batch_dir = FIXTURES / "batch"
    targets = sorted(batch_dir.glob("page-*.md"))
    assert len(targets) == 20, "fixture batch directory should hold 20 pages"

    findings = run(_config(_REPO_ROOT), targets, _StubCorpus(_REPO_ROOT))

    assert len(findings) == 20
    assert all(f.rule_id == "W87" and "MD040" in f.message for f in findings)
    assert {f.file for f in findings} == {
        str(target.relative_to(_REPO_ROOT)) for target in targets
    }


def test_custom_rule_findings_never_surface_as_w87() -> None:
    """`broken.md` and `clean.md` both carry no tags beyond a single generic
    one and a minimal body — real custom W-rules (W25 unlinked-mention, W27
    empty-tags, ...) may still fire on them, but none of that may leak into
    this producer's output: only a genuine MD###/OFM### built-in check may
    ever become a W87 finding here."""
    for name in ("broken.md", "clean.md"):
        findings = run(_config(_REPO_ROOT), [FIXTURES / name], _StubCorpus(_REPO_ROOT))
        for finding in findings:
            code = finding.message.split(":", 1)[0]
            assert code.startswith(("MD", "OFM")), f"{name}: leaked non-built-in finding {finding}"


def test_orchestrator_merges_producer_findings_into_lint_result() -> None:
    config = Config(
        repo_root=_REPO_ROOT,
        vault_root=_REPO_ROOT / "vault",
        templates_root=_REPO_ROOT / "vault" / "_templates",
        cache_path=_REPO_ROOT / "utils" / "wiki-cli" / ".wiki-cli-test-cache.sqlite3",
        scoped_roots=("vault", "utils/wiki-cli/tests"),
        report_cap=50,
        fingerprint="test-fingerprint-producers-markdownlint",
        _thresholds={},
    )

    result = run_lint(config, [FIXTURES / "broken.md"])

    w87 = [f for f in result.findings if f.rule_id == "W87"]
    assert len(w87) == 1
    assert w87[0].producer == "markdownlint"
    assert "W87" in result.stats.per_producer_seconds
    config.cache_path.unlink(missing_ok=True)
