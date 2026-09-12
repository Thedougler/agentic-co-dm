"""TDD for the vale producer (W86) and its integration with the
producer/orchestrator framework `test_producers_markdownlint.py` already
exercises for W87.

Vale's own `.vale.ini` scopes which style packages apply per file via
directory-scoped glob sections (`[vault/**/*.md]`, `[docs/guardrails/**/
*.md]`, ...) — a file outside every named glob gets NO style applied at
all (confirmed empirically against vale 3.13.0: a relative target path
under, say, `utils/` matches no section and always returns zero alerts,
regardless of content). `tests/fixtures/producers/vale/broken.md` sits
outside every real `.vale.ini` glob for exactly that reason, so the
detection tests below give it its OWN minimal, self-contained `.vale.ini` +
a real copy of `docs/vale-styles/CampaignOS/BannedCliches.yml` (same
fixture-vault pattern the legacy JS engine's own Vale test already uses —
`utils/scripts/lint-rules/fixtures/vale-vault/.vale.ini`) and points the
producer at it via `corpus.repo_root` — the one input `run()` actually
reads the config path from (see the markdownlint producer's own
`repo_root = corpus.repo_root`; vale.py does the same).
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from wiki_cli.config import Config
from wiki_cli.contracts import Page
from wiki_cli.orchestrator import run_lint
from wiki_cli.producers import all_producers
from wiki_cli.producers import vale as vale_module
from wiki_cli.producers.vale import FAMILY_ID, run

_REPO_ROOT = Path(__file__).resolve().parents[3]
"""tests/test_producers_vale.py -> utils/wiki-cli/tests -> utils/wiki-cli
-> repo root, 3 parents up."""

FIXTURES = _REPO_ROOT / "utils" / "wiki-cli" / "tests" / "fixtures" / "producers" / "vale"
"""Doubles as its own isolated fixture-repo root: carries its own
`.vale.ini` + `vale-styles/CampaignOS/BannedCliches.yml` alongside
`broken.md`/`clean.md`, so `corpus.repo_root = FIXTURES` resolves a real,
working Vale config with no dependency on the real repo's `.vale.ini`
glob-routing."""


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


def test_family_id_is_w86() -> None:
    assert FAMILY_ID == "W86"


def test_registers_in_producers_registry() -> None:
    assert all_producers()["W86"] is run


def test_broken_fixture_yields_one_w86_finding_with_check_in_message() -> None:
    target = FIXTURES / "broken.md"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(FIXTURES))

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W86"
    assert finding.producer == "vale"
    assert finding.tier.value == "prose"
    assert finding.severity.value == "error"
    assert finding.file == "broken.md"
    assert finding.line == 6
    assert finding.column == 9
    assert finding.message.startswith("CampaignOS.BannedCliches: ")


def test_clean_fixture_yields_no_findings() -> None:
    target = FIXTURES / "clean.md"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(FIXTURES))

    assert findings == []


def test_frontmatter_owner_skill_value_is_not_linted_as_prose() -> None:
    """`frontmatter-leak.md`'s `owner_skill:` value contains a literal
    `SKILL.md` (ADR-0044's mandated shape for a skill-owned page) — real
    prose vocabulary CampaignOS.ProcessLeak (docs/vale-styles/CampaignOS/
    ProcessLeak.yml, copied into this fixture's own vale-styles/) correctly
    flags in the BODY but must never flag in this one frontmatter key. The
    body still carries the same BannedCliches "loom" trip broken.md uses,
    at its real line (7, one line later than broken.md's 6 — this fixture
    has one extra frontmatter line) — proving the frontmatter guard masks
    only the targeted value, not the whole file, and line numbers survive
    the ephemeral-copy round-trip untouched."""
    target = FIXTURES / "frontmatter-leak.md"

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(FIXTURES))

    checks = [f.message.split(":", 1)[0] for f in findings]
    assert "CampaignOS.ProcessLeak" not in checks
    assert len(findings) == 1
    assert findings[0].message.startswith("CampaignOS.BannedCliches: ")
    assert findings[0].line == 7


def test_frontmatter_guard_mirrors_outside_repo_and_directory_scoped_section_still_applies(
    monkeypatch,
) -> None:
    """Regression for the concurrent-lint race: a same-directory `.vale-fm-*`
    sibling was visible to every other invocation's own target discovery
    for as long as it existed (two agents hit `wiki lint: internal error`
    naming one as a discovered target; `test_producers_duplication.py`'s
    orchestrator test failed under load reading one mid-flight). The fix
    mirrors the transformed copy into a private `tempfile.mkdtemp()`
    directory OUTSIDE the fixture tree instead of beside the original.

    `scoped/owner-skill-scoped.md` sits under `[scoped/**/*.md]` (this
    fixture's own `.vale.ini`), the ONLY section that turns on
    `CampaignOS.ScopedOnly` (off everywhere else) — proving the mirror
    copy's relative path still resolves the SAME directory-scoped section
    as the original, not just that the frontmatter guard itself works. A
    fix that silently dropped section-glob matching (e.g. a naive
    `$TMPDIR/foo.md` mirror with no relative-path structure) would fail
    this assertion even though `ProcessLeak` still correctly disappeared.
    """
    target = FIXTURES / "scoped" / "owner-skill-scoped.md"
    real_mkdtemp = vale_module.tempfile.mkdtemp
    captured: list[Path] = []

    def spy_mkdtemp(
        suffix: str | None = None, prefix: str | None = None, dir: str | None = None
    ) -> str:
        made = real_mkdtemp(suffix=suffix, prefix=prefix, dir=dir)
        captured.append(Path(made))
        return made

    monkeypatch.setattr(vale_module.tempfile, "mkdtemp", spy_mkdtemp)

    findings = run(_config(_REPO_ROOT), [target], _StubCorpus(FIXTURES))

    checks = {f.message.split(":", 1)[0] for f in findings}
    # frontmatter guard: the owner_skill: value's literal "SKILL.md" never
    # reaches Vale as body prose.
    assert "CampaignOS.ProcessLeak" not in checks
    # directory-scoped section: the mirror's relative path still matched
    # [scoped/**/*.md], not just the bare [*.md] section.
    assert "CampaignOS.ScopedOnly" in checks

    assert len(captured) == 1, "expected exactly one mirror temp root for one fm-guarded target"
    temp_root = captured[0].resolve()
    fixtures_resolved = FIXTURES.resolve()
    assert not temp_root.is_relative_to(fixtures_resolved), (
        f"mirror root {temp_root} must live outside the scanned fixture tree {fixtures_resolved}"
    )
    assert temp_root.is_relative_to(Path(tempfile.gettempdir()).resolve())
    assert not temp_root.exists(), "mirror root must be torn down (finally: shutil.rmtree) after run()"
    assert not any(fixtures_resolved.rglob("*vale-fm*")), (
        "no ephemeral artifact may ever appear inside the scanned fixture tree"
    )


def test_sweep_stale_temp_roots_reclaims_dead_pid_but_spares_live_pid(tmp_path: Path) -> None:
    """`_sweep_stale_temp_roots` is the self-heal for a SIGKILLed run's
    leftover mirror tree (the `finally` block that normally removes it
    never runs on SIGKILL) — proves it removes an aged orphan whose
    embedded pid is dead, and spares one whose embedded pid is alive, using
    an isolated `tmp_path` root so this test never touches the real system
    temp directory."""
    import os
    import subprocess
    import time

    # A pid that is guaranteed dead: spawn a subprocess and wait for exit.
    proc = subprocess.Popen(["true"])
    dead_pid = proc.pid
    proc.wait()

    dead_dir = tmp_path / f"wiki-vale-fm-{dead_pid}-deadbeef"
    dead_dir.mkdir()
    self_dir = tmp_path / f"wiki-vale-fm-{os.getpid()}-livecafe"
    self_dir.mkdir()
    other_live_dir = tmp_path / "wiki-vale-fm-1-otherlive"  # pid 1 (init/launchd) — always alive
    other_live_dir.mkdir()

    old_time = time.time() - vale_module._STALE_TEMP_ROOT_AGE_S - 5
    os.utime(dead_dir, (old_time, old_time))
    os.utime(self_dir, (old_time, old_time))
    os.utime(other_live_dir, (old_time, old_time))

    vale_module._sweep_stale_temp_roots(tmp_path)

    assert not dead_dir.exists(), "aged orphan with a dead embedded pid must be reclaimed"
    assert self_dir.exists(), "a directory embedding this OWN live pid must never be swept"
    assert other_live_dir.exists(), "a directory embedding a DIFFERENT live pid must never be swept"


def test_empty_targets_is_a_noop() -> None:
    assert run(_config(_REPO_ROOT), [], _StubCorpus(FIXTURES)) == []


def test_repo_root_with_no_vale_ini_yields_no_findings() -> None:
    """Vale simply isn't configured at a root with no `.vale.ini` (a
    fixture repo without a prose arm) — not a failure, same contract as the
    legacy `runVale`'s own `existsSync` guard. `utils/wiki-cli/` itself
    carries no `.vale.ini` of its own (only the real repo root does)."""
    no_vale_root = _REPO_ROOT / "utils" / "wiki-cli"

    findings = run(_config(no_vale_root), [FIXTURES / "broken.md"], _StubCorpus(no_vale_root))

    assert findings == []


def test_orchestrator_merges_producer_findings_into_lint_result() -> None:
    """`FIXTURES` itself doubles as the isolated repo root here (see the
    module docstring) so `corpus.repo_root` resolves the fixture's own
    `.vale.ini` through the real `run_lint` orchestrator path, not just a
    direct `run()` call. `producers=["W86"]` restricts the sweep to just
    this producer — the fixture repo carries no `node_modules/` for
    markdownlint (W87) to shell out to, and no interest in running the
    native rule suite against a two-line fixture page."""
    config = Config(
        repo_root=FIXTURES,
        vault_root=FIXTURES,
        templates_root=FIXTURES / "_templates",
        cache_path=FIXTURES / ".wiki-cli-test-cache.sqlite3",
        scoped_roots=(".",),
        report_cap=50,
        fingerprint="test-fingerprint-producers-vale",
        _thresholds={},
    )
    try:
        result = run_lint(config, [FIXTURES / "broken.md"], producers=["W86"])

        w86 = [f for f in result.findings if f.rule_id == "W86"]
        assert len(w86) == 1
        assert w86[0].producer == "vale"
        assert "W86" in result.stats.per_producer_seconds
    finally:
        config.cache_path.unlink(missing_ok=True)
        (FIXTURES / ".wiki-cli" / "cache.sqlite3").unlink(missing_ok=True)
