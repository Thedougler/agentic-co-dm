"""W105, W107, W108, W109 — guardrails-docs cluster, ported from the legacy
JS lint engine's `utils/scripts/lint-rules/w105-w109-guardrails.test.mjs`
family. See each rule module's docstring for the ported spec.

Real (non-fixture-scaled) thresholds apply — `load_config()` inside each
rule reads the real `utils/wiki-cli/wiki.toml` (120 lines / 1100 words /
60 rule-words), so `LONG.md`/`MIGRATION-LOG.md` are padded to genuinely
cross those caps rather than a tiny fixture-local override."""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.contracts import registry
from wiki_cli.index import VaultIndex
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "guardrails_docs"


def _corpus() -> VaultIndex:
    return VaultIndex.build(FIXTURES, FIXTURES, ())


def check(rule_id: str, fixture: str):
    rule = registry()[rule_id]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, _corpus()))


def check_vault(rule_id: str):
    rule = registry()[rule_id]
    return list(rule.check(_corpus()))


# ---- W105 — guardrail-doc-budget ----


def test_w105_flags_doc_over_line_cap():
    findings = check("W105", "docs/guardrails/LONG.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W105", 1)]
    assert "126 lines" in findings[0].message


def test_w105_clean_under_both_caps():
    assert check("W105", "docs/guardrails/CLEAN.md") == []


def test_w105_migration_log_exempt_though_over_cap():
    assert check("W105", "docs/guardrails/MIGRATION-LOG.md") == []


# ---- W107 — routing-trigger-verbatim ----


def test_w107_flags_drifted_opener():
    findings = check("W107", "docs/guardrails/DRIFT.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W107", 2)]
    assert "drifted from CLAUDE.md's routing row for DRIFT.md" in findings[0].message


def test_w107_flags_one_word_drift():
    findings = check("W107", "docs/guardrails/SHIFT.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W107", 2)]
    assert 'row word' in findings[0].message


def test_w107_clean_on_verbatim_opener():
    assert check("W107", "docs/guardrails/CLEAN.md") == []


def test_w107_silent_with_no_routing_row():
    assert check("W107", "docs/guardrails/LONG.md") == []


# ---- W108 — guardrail-id-resolves ----


def test_w108_direction_a_unresolved_reference_fires():
    findings = check_vault("W108")
    drift_hits = [f for f in findings if f.file == "docs/guardrails/DRIFT.md"]
    assert len(drift_hits) == 1
    assert drift_hits[0].line == 6
    assert "reference to CLEAN.md X9 does not resolve" in drift_hits[0].message
    assert "defined: X1, X2" in drift_hits[0].message


def test_w108_direction_a_resolving_reference_stays_silent():
    findings = check_vault("W108")
    assert [f for f in findings if f.file == "docs/guardrails/CLEAN.md"] == []
    assert [f for f in findings if f.file == "CLAUDE.md"] == []


def test_w108_migration_log_exempt_as_reference_source():
    findings = check_vault("W108")
    assert [f for f in findings if f.file == "docs/guardrails/MIGRATION-LOG.md"] == []


def test_w108_direction_b_duplicate_definition_fires():
    findings = check_vault("W108")
    long_hits = [f for f in findings if f.file == "docs/guardrails/LONG.md"]
    assert len(long_hits) == 1
    assert long_hits[0].line == 4
    assert long_hits[0].message.startswith("X1 is defined twice (CLEAN.md:4)")


# ---- W109 — guardrail-rule-line-length ----


def test_w109_flags_long_rule_line():
    findings = check("W109", "docs/guardrails/DRIFT.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W109", 5)]
    assert "66-word rule" in findings[0].message


def test_w109_clean_short_rule_lines():
    assert check("W109", "docs/guardrails/CLEAN.md") == []


def test_w109_migration_log_exempt_though_over_cap():
    assert check("W109", "docs/guardrails/MIGRATION-LOG.md") == []
