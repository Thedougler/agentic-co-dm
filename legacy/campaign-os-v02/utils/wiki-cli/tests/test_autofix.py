"""The autofix pass (ADR-0064): repair first, then judge.

Every case here is written from what an agent sees. A mechanical defect
must be gone from the file AND absent from the report; a rewritten file
must announce itself so a stale in-context copy is re-read; a
`docs/guardrails/**` file must come back byte-identical; and both escape
hatches (`--no-fix`, `--json`) must leave the corpus untouched.

`producers=["wiki"]` on every `run_lint` call scopes the run to the native
rules, the same reason `test_orchestrator.py` does it: this suite's vault
is an isolated `tmp_path` tree, so an external tool producer has no real
config to read under it.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from wiki_cli import autofix
from wiki_cli.autofix import REWRITTEN_LINE, FixContext, is_exempt, repair_text
from wiki_cli.cli import app
from wiki_cli.config import Config
from wiki_cli.contracts import BaseRule, all_rules
from wiki_cli.orchestrator import LintResult, RunStats, run_lint
from wiki_cli.report import render

CALLOUT_PAGE = """---
type: ref
title: Example
status: draft
---

# Example

> [!DM]
> A note for the DM.
"""

ITEM_PAGE = """---
type: item
title: Reef Knife
attunement: false
---

# Reef Knife

> [!DM]
> A note for the DM.
"""


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
def repo(tmp_path: Path) -> Path:
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / "vault" / "autofix").mkdir(parents=True)
    (tmp_path / "docs" / "guardrails").mkdir(parents=True)
    return tmp_path


def _write(repo: Path, rel_path: str, text: str) -> Path:
    path = repo / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def test_the_file_is_repaired_before_any_rule_reads_it(repo: Path) -> None:
    target = _write(repo, "vault/autofix/example.md", CALLOUT_PAGE)

    result = run_lint(_config(repo), [target], producers=["wiki"])

    assert "> [!dm]" in target.read_text(encoding="utf-8")
    assert "W22" not in {finding.rule_id for finding in result.findings}


def test_a_rewritten_file_is_named_once_with_its_fix_count(repo: Path) -> None:
    target = _write(repo, "vault/autofix/example.md", CALLOUT_PAGE)

    result = run_lint(_config(repo), [target], producers=["wiki"])

    assert result.fixed == {"vault/autofix/example.md": 1}


def test_one_pass_lands_a_frontmatter_and_a_syntax_repair_together(repo: Path) -> None:
    target = _write(repo, "vault/autofix/knife.md", ITEM_PAGE)

    result = run_lint(_config(repo), [target], producers=["wiki"])
    text = target.read_text(encoding="utf-8")

    assert result.fixed == {"vault/autofix/knife.md": 2}
    assert "unique: false" in text
    assert "> [!dm]" in text
    assert not {"W22", "W138"} & {finding.rule_id for finding in result.findings}


def test_the_report_tells_the_agent_to_read_the_file_again(repo: Path) -> None:
    target = _write(repo, "vault/autofix/example.md", CALLOUT_PAGE)

    rendered = render(run_lint(_config(repo), [target], producers=["wiki"]))

    assert "FIXED vault/autofix/example.md: 1 mechanical fixes" in rendered
    assert REWRITTEN_LINE in rendered


def test_the_rewrite_notice_survives_a_clean_and_a_quiet_report() -> None:
    result = LintResult(
        findings=[],
        stats=RunStats(files=1, rules_run=1, cache_hits=0, seconds=0.1),
        fixed={"vault/autofix/example.md": 3},
    )

    for rendered in (render(result), render(result, quiet=True)):
        assert "FIXED vault/autofix/example.md: 3 mechanical fixes" in rendered
        assert REWRITTEN_LINE in rendered


def test_a_guardrail_doc_is_never_rewritten(repo: Path) -> None:
    """F15 version-bump pairs desynchronise if anything but the editing
    agent writes the file, so the defect reports instead."""
    target = _write(repo, "docs/guardrails/EXAMPLE.md", CALLOUT_PAGE)

    result = run_lint(_config(repo), [target], producers=["wiki"])

    assert target.read_text(encoding="utf-8") == CALLOUT_PAGE
    assert result.fixed == {}
    assert "W22" in {finding.rule_id for finding in result.findings}


def test_no_fix_reports_the_defect_and_leaves_the_bytes_alone(repo: Path) -> None:
    target = _write(repo, "vault/autofix/example.md", CALLOUT_PAGE)

    result = run_lint(_config(repo), [target], producers=["wiki"], no_fix=True)

    assert target.read_text(encoding="utf-8") == CALLOUT_PAGE
    assert result.fixed == {}
    assert "W22" in {finding.rule_id for finding in result.findings}


def test_json_output_never_fixes(monkeypatch: pytest.MonkeyPatch) -> None:
    """The NDJSON surface describes the corpus it was handed. Asserted at
    the wiring, since the flag's whole effect is the argument it passes."""
    seen: dict[str, object] = {}

    def _record(config: object, targets: object, **kwargs: object) -> LintResult:
        seen.update(kwargs)
        return LintResult(
            findings=[], stats=RunStats(files=0, rules_run=0, cache_hits=0, seconds=0.0)
        )

    monkeypatch.setattr("wiki_cli.cli.run_lint", _record)
    monkeypatch.setattr("wiki_cli.cli._collect_targets", lambda *args, **kwargs: [])

    CliRunner().invoke(app, ["lint", "--json", "vault/index.md"])

    assert seen["no_fix"] is True


def test_a_repair_is_stable_and_never_needs_a_second_run(repo: Path) -> None:
    once, count = repair_text("vault/autofix/example.md", CALLOUT_PAGE)
    twice, again = repair_text("vault/autofix/example.md", once)

    assert count == 1
    assert twice == once
    assert again == 0


def test_only_guardrail_docs_are_exempt() -> None:
    assert is_exempt("docs/guardrails/CODE.md")
    assert not is_exempt("docs/adr/0064-lint-output-is-an-instruction-list.md")
    assert not is_exempt("vault/autofix/example.md")


def test_a_repair_needing_the_corpus_changes_nothing_without_one() -> None:
    """`Autofix.apply` is `str -> str`, so a fix whose correct target lives
    on another page returns its input rather than guessing."""
    with autofix.fixing(FixContext(rel_path="vault/autofix/example.md", corpus=None)):
        text = "| Region | [[midchain]] |\n"
        rule = next(r for r in _autofix_rules() if r.id == "W119")
        assert rule.autofix is not None
        assert rule.autofix.apply(text) == text


def _autofix_rules() -> list[BaseRule]:
    return [rule for rule in all_rules() if rule.autofix is not None]
