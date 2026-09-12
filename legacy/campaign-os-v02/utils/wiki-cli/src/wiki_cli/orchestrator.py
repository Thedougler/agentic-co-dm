"""Central lint runner: wires rules and producers to the findings cache
(ADR-0041).

A rule's or producer's own metadata decides its runtime shape.

`pure` decides whether a per-file result is looked up in and written to the
findings cache (`db.py`, keyed on the file's own content hash plus the
rule/producer id and version and the config's fingerprint). A `VaultRule`
never caches, since its answer depends on the whole corpus, not one file's
bytes, and `VaultRule.pure` is `False` by construction (`contracts.py`). A
pure producer caches per target the same way a pure `FileRule` does, with
its own `config_fingerprint` covering the config it reads from disk
(`producers/__init__.py`) — that is what makes an expensive external tool
cheap on a second run over unchanged bytes, in place of any budget gate.

`when` decides whether it runs at all. A scoped run (`scoped=True`: the
caller named paths) runs only `When.EDIT` rules and producers; a full-vault
sweep runs every one. A SWEEP producer skipped on a scoped run is skipped
silently — its question (cross-file duplication) is not one an edited
file's own bytes can answer, so naming it in the report would only offer a
re-run nobody should make.

Every finding from every tier is reported, sorted by tier.
"""

from __future__ import annotations

import concurrent.futures
import hashlib
import os
import re
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli import autofix, db
from wiki_cli.config import Config, validate_paths
from wiki_cli.contracts import TIER_ORDER, FileRule, Finding, VaultRule, When, all_rules
from wiki_cli.index import VaultIndex
from wiki_cli.markdown import load_page
from wiki_cli.producers import ProducerRun, all_producer_meta

_VALE_TEMP_RE = re.compile(r"\.vale-(?:fm|chunk)-\d+-")
"""The prose tooling's ephemeral sibling copies (`<stem>.vale-fm-<pid>-<uuid>.md`
and the matching chunk dirs — `utils/scripts/lib/prose-scope.mjs`). They are
never lint targets, and under concurrent agents one run's target-discovery
routinely enumerates another run's copy microseconds before that run deletes
it, which reached `load_page` as a fatal `FileNotFoundError`. Filtered here so
every rule and producer sees the same target list, rather than per-rule (see
`rules/slug_kebab_case.py`, `rules/unlinked_mention.py`)."""

_CALLOUT_FRAGMENT_PATTERN = r"-c\d{2,}\.md$"
"""Canonical fragment-file pattern. Matches ``-c01.md``, ``-c02.md``, etc.
Declared in wiki.toml as CALLOUT_FRAGMENT_PATTERN; this constant is the
fallback for isolated test configs that omit thresholds."""


@dataclass(frozen=True)
class RunStats:
    files: int
    rules_run: int
    cache_hits: int
    seconds: float
    per_producer_seconds: dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class LintResult:
    findings: list[Finding]
    """Every finding this run produced, display-ready, sorted by tier."""
    stats: RunStats
    fixed: dict[str, int] = field(default_factory=dict)
    """`{rel_path: fixes applied}` for each file the autofix pass rewrote
    before evaluation (`autofix.py`). A defect the pass removed appears
    nowhere in `findings`; the report turns this into its `FIXED` lines."""


def _git_root(config: Config) -> Path:
    """The real repo root — the ancestor directory that actually contains
    `config.vault_root`.

    In production `wiki.toml` lives two levels below that root
    (`utils/wiki-cli`, the same relation `parity.py`'s `_REPO_ROOT` uses),
    so `config.repo_root` itself is usually NOT the vault's ancestor and
    the fallback below walks up to their common ancestor instead. Tests
    that point `repo_root` and `vault_root` at the same tree (matching
    `wiki_cli.index`'s own test fixtures) take the fast path.
    """
    repo_root = config.repo_root.resolve()
    vault_root = config.vault_root.resolve()
    try:
        vault_root.relative_to(repo_root)
        return repo_root
    except ValueError:
        return Path(os.path.commonpath([repo_root, vault_root]))


def _run_producer_timed(
    run_fn: ProducerRun,
    config: Config,
    targets: list[Path],
    corpus: VaultIndex,
) -> tuple[list[Finding], float]:
    """Run one producer's `run(config, targets, corpus)` and time it from
    inside the worker thread — the thread pool overlaps every producer, so
    the wall clock around `executor.submit` would measure queueing plus
    every other producer's runtime, not this one's own."""
    start = time.monotonic()
    findings = list(run_fn(config, targets, corpus))
    return findings, time.monotonic() - start


def _producer_cache_id(family_id: str) -> str:
    """A producer's key in the findings cache. Prefixed so it can never
    collide with a registered rule's own id, which shares the table."""
    return f"producer:{family_id}"


def rel_path(target: Path, git_root: Path) -> str:
    """A target path, relative to `git_root` when it lies underneath it —
    a raw absolute path is kept as-is rather than raising, since a target
    outside the repo is a caller error `load_page` will surface on read."""
    resolved = target.resolve()
    try:
        return str(resolved.relative_to(git_root))
    except ValueError:
        return str(resolved)


def run_lint(
    config: Config,
    targets: list[Path],
    *,
    producers: list[str] | None = None,
    include_dndsim: bool = False,
    scoped: bool = False,
    no_fix: bool = False,
) -> LintResult:
    """Run every applicable rule and producer over `targets`, caching pure
    per-file results by content hash.

    Every registered external producer (`wiki_cli.producers`, e.g. `markdownlint`
    for W87) also runs, concurrently via a thread pool since each shells a
    subprocess — its findings merge into the same per-file map native rule
    findings do, and its own wall time lands in `stats.per_producer_seconds`
    under its family id (e.g. `"W87"`).

    `producers`, when given, restricts which rules run to those whose
    `producer` ClassVar is in the list — display-only filtering the same
    way the CLI's `--rule` flag is (ADR-0023); it never
    changes which findings exist, only which are collected here. The same
    list also gates which external producer modules run, matched against
    each module's own family id (`wiki_cli.producers.all_producers()`'s keys).
    `include_dndsim` gates the dndsim producer (ADR-0015).

    `scoped=True` says the caller named its own paths, so only `When.EDIT`
    rules and producers run; the default runs every one, which is what a
    full-vault sweep wants.

    Every target is repaired first (`autofix.py`) and the rules then judge
    the repaired bytes, so a mechanical defect never reaches a report.
    `no_fix=True` skips that pass — what `wiki lint --no-fix` and every
    `--json` invocation pass, since a machine-readable run must describe
    the corpus it was given, not one it changed.
    """
    validate_paths(config)

    if include_dndsim:
        os.environ["WIKI_CLI_DNDSIM"] = "1"
    elif "WIKI_CLI_DNDSIM" in os.environ:
        del os.environ["WIKI_CLI_DNDSIM"]

    start = time.monotonic()
    git_root = _git_root(config)

    conn = db.connect(config.cache_path)
    try:
        corpus = VaultIndex.build(git_root, config.vault_root.resolve(), config.scoped_roots)

        rel_paths = sorted(
            rp
            for rp in {rel_path(target, git_root) for target in targets}
            if "/_templates/" not in f"/{rp}"
            and not rp.startswith("_templates/")
            and not _VALE_TEMP_RE.search(rp)
        )
        allowed = set(producers) if producers is not None else None

        # Repair before judging (ADR-0064): a mechanical defect is fixed on
        # disk here, so no rule below ever sees it and no report ever names
        # it. The corpus was built from the pre-fix bytes, so a rewritten
        # file is re-read from disk instead of taken from it.
        fixed: dict[str, int] = {}
        if not no_fix:
            fixed = autofix.run_autofix(git_root, rel_paths, corpus, allowed)

        pages = []
        for target_rel_path in rel_paths:
            page = None if target_rel_path in fixed else corpus.get_page(target_rel_path)
            if page is None:
                try:
                    page = load_page(git_root, target_rel_path)
                except FileNotFoundError:
                    continue  # vanished between target discovery and load — a concurrent write, not a lint failure
            pages.append(page)

        file_rules = [rule for rule in all_rules() if isinstance(rule, FileRule)]
        vault_rules = [rule for rule in all_rules() if isinstance(rule, VaultRule)]
        if allowed is not None:
            file_rules = [rule for rule in file_rules if rule.producer in allowed]
            vault_rules = [rule for rule in vault_rules if rule.producer in allowed]
        if scoped:
            file_rules = [rule for rule in file_rules if rule.when is When.EDIT]
            vault_rules = [rule for rule in vault_rules if rule.when is When.EDIT]

        per_file_findings: dict[str, list[Finding]] = {page.rel_path: [] for page in pages}
        cache_hits = 0
        rules_run = 0
        per_producer_seconds: dict[str, float] = defaultdict(float)

        corpus_fp = corpus.corpus_fingerprint
        fragment_re = re.compile(
            config._thresholds.get("CALLOUT_FRAGMENT_PATTERN", _CALLOUT_FRAGMENT_PATTERN)
        )

        content_hashes: dict[str, str] = {}
        for page in pages:
            is_fragment = bool(fragment_re.search(page.rel_path))
            page_file_rules = (
                [r for r in file_rules if not r.page_level] if is_fragment else file_rules
            )
            # A rewritten file's corpus hash covers its pre-fix bytes, and
            # keying the cache on it would serve findings about text that
            # no longer exists — hash the repaired bytes instead.
            content_hash = (
                None if page.rel_path in fixed else corpus.content_hash(page.rel_path)
            )
            if content_hash is None:
                content_hash = hashlib.sha256(page.raw.encode("utf-8")).hexdigest()
            content_hashes[page.rel_path] = content_hash
            for rule in page_file_rules:
                rule_start = time.monotonic()
                rules_run += 1
                effective_fp = (
                    config.fingerprint if rule.pure else f"{config.fingerprint}:{corpus_fp}"
                )
                cached: list[Finding] | None = db.get_cached(
                    conn,
                    rel_path=page.rel_path,
                    content_hash=content_hash,
                    rule_id=rule.id,
                    rule_version=rule.version,
                    config_fingerprint=effective_fp,
                )
                if cached is not None:
                    cache_hits += 1
                    findings = cached
                else:
                    findings = list(rule.check(page, corpus))
                    db.set_cached(
                        conn,
                        rel_path=page.rel_path,
                        content_hash=content_hash,
                        rule_id=rule.id,
                        rule_version=rule.version,
                        config_fingerprint=effective_fp,
                        findings=findings,
                    )
                per_file_findings[page.rel_path].extend(findings)
                per_producer_seconds[rule.producer] += time.monotonic() - rule_start

        target_rel_paths = set(per_file_findings)
        for rule in vault_rules:
            rule_start = time.monotonic()
            rules_run += 1
            for finding in rule.check(corpus):
                if finding.file in target_rel_paths:
                    per_file_findings[finding.file].append(finding)
            per_producer_seconds[rule.producer] += time.monotonic() - rule_start

        producer_meta = all_producer_meta()
        producer_ids = set(producer_meta)
        if not include_dndsim:
            producer_ids.discard("dndsim")
        if allowed is not None:
            producer_ids &= allowed
        if scoped:
            producer_ids = {
                fid for fid in producer_ids if producer_meta[fid].when is When.EDIT
            }
        if not pages:
            # Every producer finding is dropped below unless its file is in
            # `target_rel_paths`, which is empty here (a caller whose targets
            # were all filtered out — a `_templates/` path, a vale temp
            # sibling). Running them would be pure cost for zero findings.
            producer_ids = set()

        # A pure producer answers per target from that target's own bytes, so
        # each target is looked up in the same findings cache a pure FileRule
        # uses and only the misses are handed to the tool. That is what makes
        # an expensive external binary cheap on a re-run over unchanged
        # bytes. An impure producer (git state, cross-file existence, the
        # calendar) gets every target, every run.
        producer_jobs: dict[str, list[Path]] = {}
        producer_misses: dict[str, list[str]] = {}
        producer_keys: dict[str, str] = {}
        for family_id in producer_ids:
            meta = producer_meta[family_id]
            if not meta.pure:
                producer_jobs[family_id] = [git_root / page.rel_path for page in pages]
                continue
            producer_keys[family_id] = (
                f"{config.fingerprint}:{meta.cache_fingerprint(git_root)}"
            )
            misses: list[str] = []
            for page in pages:
                cached_producer = db.get_cached(
                    conn,
                    rel_path=page.rel_path,
                    content_hash=content_hashes[page.rel_path],
                    rule_id=_producer_cache_id(family_id),
                    rule_version=meta.version,
                    config_fingerprint=producer_keys[family_id],
                )
                if cached_producer is None:
                    misses.append(page.rel_path)
                else:
                    cache_hits += 1
                    per_file_findings[page.rel_path].extend(cached_producer)
            if misses:
                producer_misses[family_id] = misses
                producer_jobs[family_id] = [git_root / rp for rp in misses]

        if producer_jobs:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(producer_jobs)) as executor:
                future_to_family = {
                    executor.submit(
                        _run_producer_timed,
                        producer_meta[family_id].run,
                        config,
                        job_targets,
                        corpus,
                    ): family_id
                    for family_id, job_targets in producer_jobs.items()
                }
                for future in concurrent.futures.as_completed(future_to_family):
                    family_id = future_to_family[future]
                    findings, elapsed = future.result()
                    per_producer_seconds[family_id] += elapsed
                    misses = producer_misses.get(family_id, [])
                    if misses:
                        by_file: dict[str, list[Finding]] = {rp: [] for rp in misses}
                        for finding in findings:
                            if finding.file in by_file:
                                by_file[finding.file].append(finding)
                        for miss_rel_path, miss_findings in by_file.items():
                            db.set_cached(
                                conn,
                                rel_path=miss_rel_path,
                                content_hash=content_hashes[miss_rel_path],
                                rule_id=_producer_cache_id(family_id),
                                rule_version=producer_meta[family_id].version,
                                config_fingerprint=producer_keys[family_id],
                                findings=miss_findings,
                            )
                            per_file_findings[miss_rel_path].extend(miss_findings)
                        continue
                    for finding in findings:
                        if finding.file in target_rel_paths:
                            per_file_findings[finding.file].append(finding)

        if not scoped:
            # Every full sweep is the cache's maintenance point: without it
            # findings_cache grows unbounded (1M rows / 428MB observed),
            # since impure rules key on `corpus_fp` and every corpus edit
            # orphans their prior fingerprint's row for every file, forever.
            db.gc(conn)
    finally:
        conn.close()

    all_findings = [finding for findings in per_file_findings.values() for finding in findings]
    all_findings.sort(key=lambda f: (TIER_ORDER.index(f.tier), f.file, f.line, f.rule_id))

    stats = RunStats(
        files=len(pages),
        rules_run=rules_run,
        cache_hits=cache_hits,
        seconds=time.monotonic() - start,
        per_producer_seconds=dict(per_producer_seconds),
    )
    return LintResult(findings=all_findings, stats=stats, fixed=fixed)
