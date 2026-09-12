"""TDD for the five term-list mechanics/prose rules ported from the npm
lint engine: W70 (dc-anatomy), W71 (plot-defense-phrasing), W115
(naming-substitute), W78 (unsourced-session-log), W61 (va-script-contract).

Each fixture lives under `tests/fixtures/mechanics_prose/` at the exact
`rel_path` its rule's scope gate needs (`vault/...`,
`vault/episodes/...`, `vault/campaigns/shattered-sea/pcs/va-scripts/...`)
so `load_page` + `registry()` exercises the real scope check, not a stub.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401 — triggers auto-discovery/registration of every rule module
from wiki_cli.contracts import registry
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "mechanics_prose"


def check(rule_id, fixture):
    rule = registry()[rule_id]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, corpus=None))


# --- W70: dc-anatomy-outside-check --------------------------------------


def test_w70_bare_dc_table_fires_once_per_row():
    findings = check("W70", "vault/dc-anatomy-bare.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W70", 14), ("W70", 15)]
    assert all("no ability/skill and no failure consequence" in f.message for f in findings)


def test_w70_attack_roll_labeled_dc_fires_both_forms():
    findings = check("W70", "vault/dc-anatomy-attack-as-dc.md")
    assert sorted((f.rule_id, f.line) for f in findings) == [("W70", 10), ("W70", 14)]
    assert all("Armor Class, never a DC" in f.message for f in findings)


def test_w70_clean_page_stays_silent():
    assert check("W70", "vault/dc-anatomy-clean.md") == []


# --- W71: plot-defense-phrasing ------------------------------------------


def test_w71_bans_with_no_fallback_fire_once_per_tell():
    findings = check("W71", "vault/plot-defense-violation.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W71", 9), ("W71", 13)]
    assert all("no stated fallback" in f.message for f in findings)


def test_w71_ban_with_nearby_fallback_stays_silent():
    assert check("W71", "vault/plot-defense-clean.md") == []


# --- W115: naming-substitute ----------------------------------------------


def test_w115_note_with_no_scripted_substitute_fires():
    findings = check("W115", "vault/episodes/naming-substitute-violation.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W115", 10)]
    assert "scripted substitute" in findings[0].message


def test_w115_note_with_quoted_substitute_stays_silent():
    assert check("W115", "vault/episodes/naming-substitute-clean.md") == []


def test_w115_outside_episodes_is_out_of_scope():
    # Same violating text, but not under vault/episodes/ — never scanned.
    assert check("W115", "vault/dc-anatomy-bare.md") == []


# --- W78: unsourced-session-log -------------------------------------------


def test_w78_session_log_with_zero_citations_fires():
    findings = check("W78", "vault/session-log-unsourced.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W78", 11)]
    assert "cites no real session" in findings[0].message


def test_w78_session_log_citing_a_sessions_path_stays_silent():
    assert check("W78", "vault/session-log-sourced.md") == []


def test_w78_session_log_citing_episodes_convention_stays_silent():
    assert check("W78", "vault/session-log-episodes-cited.md") == []


def test_w78_session_log_citing_prose_form_stays_silent():
    # Six real pages were nearly gutted before prose forms ("Session 02",
    # "s04:") were recognised as citations — see the module docstring.
    assert check("W78", "vault/session-log-prose-cited.md") == []


def test_w78_no_session_log_heading_stays_silent():
    assert check("W78", "vault/session-log-absent.md") == []


# --- W61: va-script-contract ----------------------------------------------


def test_w61_violating_script_fires_every_contract_breach():
    findings = check("W61", "vault/campaigns/shattered-sea/pcs/va-scripts/violation.md")
    lines = [f.line for f in findings]
    assert lines == [1, 5, 7, 9, 11, 13, 13, 18]
    messages = [f.message for f in findings]
    assert "carries frontmatter" in messages[0]
    assert "has a heading" in messages[1]
    assert "has a bullet list line" in messages[2]
    assert "is not italicized" in messages[3]
    assert 'carries a "direction:" label' in messages[4]
    assert "too long/explanatory" in messages[5]
    assert "no blank line before the text it precedes" in messages[6]
    assert "repeats verbatim from line 16" in messages[7]


def test_w61_clean_script_stays_silent():
    assert check("W61", "vault/campaigns/shattered-sea/pcs/va-scripts/clean.md") == []


def test_w61_outside_va_scripts_is_out_of_scope():
    findings = check(
        "W61", "vault/campaigns/shattered-sea/pcs/not-va-scripts/violation.md"
    )
    assert findings == []
