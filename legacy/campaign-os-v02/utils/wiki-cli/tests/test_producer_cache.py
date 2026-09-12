"""TDD for producer caching and `when:` scoping (ADR-0042).

A pure producer joins the same content-hash findings cache a pure
`FileRule` uses, so a second run over unchanged bytes never shells the tool
again. A SWEEP producer runs on a full sweep only. Neither behaviour is
allowed to depend on a timing budget: a slow producer is cached, never
skipped, and no report line ever proposes a re-run.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from unittest.mock import patch

import pytest

from wiki_cli import db
from wiki_cli.config import Config
from wiki_cli.contracts import Corpus, Finding, Severity, Tier, When
from wiki_cli.orchestrator import run_lint
from wiki_cli.producers import ProducerMeta, all_producer_meta
from wiki_cli.producers import vale as vale_producer

FIXTURES = Path(__file__).parent / "fixtures" / "orchestrator"


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


class _CountingProducer:
    """A stand-in for an external tool that records every target it was
    handed, so a cache hit is observable as a target that never arrived."""

    def __init__(self, *, finding_message: str | None = None) -> None:
        self.calls: list[list[Path]] = []
        self.finding_message = finding_message

    def __call__(self, config: Config, targets: list[Path], corpus: Corpus) -> list[Finding]:
        del config
        self.calls.append(list(targets))
        if self.finding_message is None:
            return []
        return [
            Finding(
                rule_id="TEST-PRODUCER",
                file=str(target.resolve().relative_to(corpus.repo_root)),
                line=1,
                message=self.finding_message,
                severity=Severity.WARNING,
                tier=Tier.PROSE,
                producer="test-producer",
            )
            for target in targets
        ]

    @property
    def targets_seen(self) -> list[str]:
        return [target.name for call in self.calls for target in call]


def _meta(
    run: _CountingProducer,
    *,
    when: When = When.EDIT,
    pure: bool = True,
    version: str = "1",
    fingerprint: str = "fp",
) -> dict[str, ProducerMeta]:
    return {
        "TESTP": ProducerMeta(
            family_id="TESTP",
            run=run,
            when=when,
            pure=pure,
            version=version,
            config_fingerprint=lambda _repo_root: fingerprint,
        )
    }


def test_pure_producer_is_skipped_on_a_second_run_over_unchanged_bytes(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"
    producer = _CountingProducer(finding_message="prose nit")

    with patch("wiki_cli.orchestrator.all_producer_meta", return_value=_meta(producer)):
        first = run_lint(config, [target], producers=["TESTP"])
        second = run_lint(config, [target], producers=["TESTP"])

    assert producer.targets_seen == ["clean.md"]
    assert [f.message for f in second.findings] == [f.message for f in first.findings]
    assert second.stats.cache_hits > first.stats.cache_hits


def test_pure_producer_reruns_after_the_file_changes(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"
    producer = _CountingProducer()

    with patch("wiki_cli.orchestrator.all_producer_meta", return_value=_meta(producer)):
        run_lint(config, [target], producers=["TESTP"])
        target.write_text(target.read_text(encoding="utf-8") + "\nAnother line.\n", encoding="utf-8")
        run_lint(config, [target], producers=["TESTP"])

    assert producer.targets_seen == ["clean.md", "clean.md"]


def test_config_fingerprint_change_busts_the_producer_cache(vault: Path) -> None:
    """A Vale styles edit changes no target's bytes, so only the producer's
    own `config_fingerprint` can make the cached verdict miss."""
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"
    producer = _CountingProducer()

    with patch(
        "wiki_cli.orchestrator.all_producer_meta",
        return_value=_meta(producer, fingerprint="styles-v1"),
    ):
        run_lint(config, [target], producers=["TESTP"])
    with patch(
        "wiki_cli.orchestrator.all_producer_meta",
        return_value=_meta(producer, fingerprint="styles-v2"),
    ):
        run_lint(config, [target], producers=["TESTP"])

    assert producer.targets_seen == ["clean.md", "clean.md"]


def test_version_bump_busts_the_producer_cache(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"
    producer = _CountingProducer()

    with patch("wiki_cli.orchestrator.all_producer_meta", return_value=_meta(producer)):
        run_lint(config, [target], producers=["TESTP"])
    with patch(
        "wiki_cli.orchestrator.all_producer_meta", return_value=_meta(producer, version="2")
    ):
        run_lint(config, [target], producers=["TESTP"])

    assert producer.targets_seen == ["clean.md", "clean.md"]


def test_impure_producer_never_caches(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"
    producer = _CountingProducer()

    with patch(
        "wiki_cli.orchestrator.all_producer_meta", return_value=_meta(producer, pure=False)
    ):
        run_lint(config, [target], producers=["TESTP"])
        run_lint(config, [target], producers=["TESTP"])

    assert producer.targets_seen == ["clean.md", "clean.md"]


def test_only_the_uncached_targets_reach_a_pure_producer(vault: Path) -> None:
    config = _config(vault)
    first_target = vault / "vault" / "orchestrator" / "clean.md"
    second_target = vault / "vault" / "orchestrator" / "violating.md"
    producer = _CountingProducer()

    with patch("wiki_cli.orchestrator.all_producer_meta", return_value=_meta(producer)):
        run_lint(config, [first_target], producers=["TESTP"])
        run_lint(config, [first_target, second_target], producers=["TESTP"])

    assert producer.targets_seen == ["clean.md", "violating.md"]


def test_sweep_producer_is_skipped_on_a_scoped_run(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"
    producer = _CountingProducer(finding_message="cross-file duplication")

    with patch(
        "wiki_cli.orchestrator.all_producer_meta",
        return_value=_meta(producer, when=When.SWEEP, pure=False),
    ):
        result = run_lint(config, [target], producers=["TESTP"], scoped=True)

    assert producer.calls == []
    assert result.findings == []


def test_sweep_producer_runs_on_a_full_sweep(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"
    producer = _CountingProducer()

    with patch(
        "wiki_cli.orchestrator.all_producer_meta",
        return_value=_meta(producer, when=When.SWEEP, pure=False),
    ):
        run_lint(config, [target], producers=["TESTP"], scoped=False)

    assert producer.targets_seen == ["clean.md"]


def test_no_producer_runs_when_every_target_was_filtered_out(vault: Path) -> None:
    """A caller whose targets are all filtered before the rule loop (a
    `_templates/` path) leaves no page for a producer finding to attach
    to, so no producer is invoked."""
    config = _config(vault)
    (vault / "vault" / "_templates" / "_note.md").write_text(
        "---\nsummary: t\n---\nBody.\n", encoding="utf-8"
    )
    producer = _CountingProducer()

    with patch("wiki_cli.orchestrator.all_producer_meta", return_value=_meta(producer)):
        result = run_lint(
            config, [vault / "vault" / "_templates" / "_note.md"], producers=["TESTP"]
        )

    assert producer.calls == []
    assert result.findings == []


# --- registered producers' own metadata ---


def test_vale_fingerprint_changes_when_a_style_file_changes(tmp_path: Path) -> None:
    styles = tmp_path / "docs" / "vale-styles" / "CampaignOS"
    styles.mkdir(parents=True)
    rule_file = styles / "BannedCliches.yml"
    rule_file.write_text("extends: existence\nmessage: nope\n", encoding="utf-8")
    (tmp_path / ".vale.ini").write_text("StylesPath = docs/vale-styles\n", encoding="utf-8")

    before = vale_producer.config_fingerprint(tmp_path)
    rule_file.write_text("extends: existence\nmessage: also nope\n", encoding="utf-8")
    after = vale_producer.config_fingerprint(tmp_path)

    assert before != after


def test_vale_fingerprint_changes_when_vale_ini_changes(tmp_path: Path) -> None:
    config_file = tmp_path / ".vale.ini"
    config_file.write_text("MinAlertLevel = warning\n", encoding="utf-8")

    before = vale_producer.config_fingerprint(tmp_path)
    config_file.write_text("MinAlertLevel = error\n", encoding="utf-8")
    after = vale_producer.config_fingerprint(tmp_path)

    assert before != after


def test_slow_shelling_producers_are_pure_and_fingerprinted() -> None:
    """W86/W87/W82 are the runs worth caching; each must declare a config
    fingerprint, or a config edit serves a stale verdict."""
    meta = all_producer_meta()
    for family_id in ("W86", "W87", "W82"):
        assert meta[family_id].pure, family_id
        assert meta[family_id].config_fingerprint is not None, family_id


def test_duplication_is_the_only_sweep_producer() -> None:
    """Cross-file duplication cannot be keyed per file, so it stays SWEEP.
    Every other producer answers from an edited file and runs on a scoped
    lint."""
    sweep = {fid for fid, meta in all_producer_meta().items() if meta.when is When.SWEEP}
    assert sweep == {"W83"}


# --- cache retention ---


def test_gc_keeps_the_newest_generations_per_file_and_rule(tmp_path: Path) -> None:
    conn = db.connect(tmp_path / "test.sqlite3")
    try:
        for generation in range(6):
            db.set_cached(
                conn,
                rel_path="vault/a.md",
                content_hash=f"hash-{generation}",
                rule_id="W1",
                rule_version="1",
                config_fingerprint="fp",
                findings=[],
            )
        db.set_cached(
            conn,
            rel_path="vault/b.md",
            content_hash="hash-b",
            rule_id="W1",
            rule_version="1",
            config_fingerprint="fp",
            findings=[],
        )

        deleted = db.gc(conn, keep=3)

        rows = conn.execute(
            "SELECT rel_path, COUNT(*) FROM findings_cache GROUP BY rel_path"
        ).fetchall()
        assert deleted == 3
        assert dict(rows) == {"vault/a.md": 3, "vault/b.md": 1}
        assert (
            db.get_cached(
                conn,
                rel_path="vault/a.md",
                content_hash="hash-5",
                rule_id="W1",
                rule_version="1",
                config_fingerprint="fp",
            )
            is not None
        )
    finally:
        conn.close()


def test_full_sweep_collects_the_cache_and_a_scoped_run_does_not(vault: Path) -> None:
    config = _config(vault)
    target = vault / "vault" / "orchestrator" / "clean.md"

    with patch("wiki_cli.orchestrator.db.gc") as collected:
        run_lint(config, [target], producers=["wiki"], scoped=True)
        assert collected.call_count == 0

        run_lint(config, [target], producers=["wiki"], scoped=False)
        assert collected.call_count == 1
