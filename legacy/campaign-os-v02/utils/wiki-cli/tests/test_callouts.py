"""W22, W23, W56, W101, W102, W104, W46 — content-shape body-line scanners
ported from the legacy JS lint engine's `utils/scripts/lint-rules/w*.mjs`
modules. See each rule module's docstring for the ported spec."""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.contracts import registry
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "callouts"


def check(rule_id: str, fixture: str):
    rule = registry()[rule_id]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, corpus=None))


# ---- W22 — callout-lowercase ----


def test_w22_flags_uppercase_callout():
    findings = check("W22", "uppercase-callout.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W22", 7)]


def test_w22_clean_on_lowercase():
    assert check("W22", "clean-callouts.md") == []


# ---- W23 — callout-type-by-path ----


def test_w23_flags_generic_callout_on_play_page():
    findings = check("W23", "vault/w23-generic-callout.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W23", 7)]
    assert "Generic callout" in findings[0].message


def test_w23_flags_bare_dc_outside_callout():
    findings = check("W23", "vault/w23-bare-dc.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W23", 7)]
    assert "DC in bare prose" in findings[0].message


def test_w23_clean_on_srd_doc_page():
    assert check("W23", "vault/srd/monsters/w23-srd-clean.md") == []


# ---- W56 — table-wikilink-pipe ----


def test_w56_flags_unescaped_pipe_in_table_wikilink():
    findings = check("W56", "broken-row.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W56", 9)]


def test_w56_clean_on_escaped_pipe():
    assert check("W56", "escaped-row.md") == []


# ---- W101 — consecutive-callouts ----


def test_w101_flags_adjacent_same_type_callouts():
    findings = check("W101", "vault/w101-adjacent-fires.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W101", 11)]


def test_w101_clean_on_different_types():
    assert check("W101", "vault/w101-different-types-clean.md") == []


def test_w101_clean_on_three_blank_gap():
    assert check("W101", "vault/w101-three-blank-clean.md") == []


# ---- W102 — table-too-wide ----


def test_w102_flags_nine_column_table():
    findings = check("W102", "wide-table.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W102", 7)]
    assert "9-column table" in findings[0].message


def test_w102_clean_on_class_page():
    assert check("W102", "vault/srd/classes/w102-class-clean.md") == []


# ---- W104 — nested-callout ----


def test_w104_flags_indented_callout():
    findings = check("W104", "indented-callout.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W104", 8)]


def test_w104_clean_on_column_zero_callout():
    assert check("W104", "column-zero-callout.md") == []


# ---- W46 — zsh-unsafe-glob ----


def test_w46_flags_bare_glob_in_shell_fence():
    findings = check("W46", "docs/w46-bare-glob.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W46", 8)]


def test_w46_clean_on_quoted_glob():
    assert check("W46", "docs/w46-quoted-glob.md") == []
