"""dndsim lint's two ported rules (issue #57; ADR-0010) — proves both
directions per utils/scripts/lint-rules/README.md's "Adding a rule" step 5:
a planted violation fires, and a clean near-miss stays silent. Fixtures
only, matching the reference statblock parser tests' own convention (never
live vault pages, which change under the engine).
"""

from __future__ import annotations

from pathlib import Path

from dndsim.lint.rules import lint_combatant_block, lint_file, lint_statblock_page

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def fixture_path(name: str) -> Path:
    return FIXTURES_DIR / name


# --- W-statblock-simulatable -------------------------------------------


def test_statblock_clean_fixture_is_silent() -> None:
    findings = lint_statblock_page(
        fixture_path("statblock-clean.md"), "vault/srd/monsters/statblock-clean.md"
    )
    assert findings == []


def test_statblock_missing_required_key_fires() -> None:
    findings = lint_statblock_page(
        fixture_path("statblock-broken.md"), "vault/srd/monsters/statblock-broken.md"
    )
    assert len(findings) == 1
    assert findings[0].rule_code == "statblock-simulatable"
    assert findings[0].rule_name == "W-statblock-simulatable"
    assert findings[0].severity == "error"
    assert "does not parse" in findings[0].message
    assert 'missing required key "ac"' in findings[0].message


def test_statblock_attack_grammar_drift_fires() -> None:
    findings = lint_statblock_page(
        fixture_path("statblock-attack-drift.md"), "vault/srd/monsters/statblock-attack-drift.md"
    )
    assert len(findings) == 1
    assert findings[0].rule_code == "statblock-simulatable"
    assert "Odd Strike" in findings[0].message
    assert "does not match the SRD attack grammar" in findings[0].message


def test_statblock_out_of_scope_path_is_silent() -> None:
    # Same broken fixture, but outside vault/srd/monsters/ or
    # vault/campaigns/shattered-sea/monsters/ — the rule never fires there
    # (matches the reference rule's SCOPED_ROOTS check).
    findings = lint_statblock_page(
        fixture_path("statblock-broken.md"), "vault/campaigns/shattered-sea/npcs/broken.md"
    )
    assert findings == []


# --- W-combatant-block ---------------------------------------------------


def test_combatant_retired_fence_fires_anywhere() -> None:
    # Unscoped by design, mirrors the reference rule — checked even outside
    # character-sheets/.
    findings = lint_combatant_block(
        fixture_path("combatant-retired-fence.md"),
        "vault/campaigns/shattered-sea/npcs/combatant-retired-fence.md",
    )
    assert len(findings) == 1
    assert findings[0].rule_code == "combatant-block"
    assert "retired ```combatant fence" in findings[0].message


def test_combatant_sheet_missing_heading_fires() -> None:
    findings = lint_combatant_block(
        fixture_path("combatant-sheet-missing-heading.md"),
        "vault/campaigns/shattered-sea/pcs/character-sheets/combatant-sheet-missing-heading.md",
    )
    assert len(findings) == 1
    assert "Combatant Block" in findings[0].message


def test_combatant_sheet_wrong_side_fires() -> None:
    findings = lint_combatant_block(
        fixture_path("combatant-sheet-wrong-side.md"),
        "vault/campaigns/shattered-sea/pcs/character-sheets/combatant-sheet-wrong-side.md",
    )
    assert len(findings) == 1
    assert "sim.side: party" in findings[0].message
    assert '"enemy"' in findings[0].message


def test_combatant_sheet_valid_is_silent() -> None:
    findings = lint_combatant_block(
        fixture_path("combatant-sheet-valid.md"),
        "vault/campaigns/shattered-sea/pcs/character-sheets/combatant-sheet-valid.md",
    )
    assert findings == []


def test_combatant_sheet_outside_dm_intel_is_silent() -> None:
    findings = lint_combatant_block(
        fixture_path("combatant-sheet-missing-heading.md"),
        "vault/campaigns/shattered-sea/npcs/not-character-sheet.md",
    )
    assert findings == []


def test_combatant_sheet_wrong_subtype_is_silent() -> None:
    # A character-sheets page that isn't a character-sheet subtype — reuses the
    # missing-heading fixture's body but pretends a different subtype via
    # the rel path check only; frontmatter subtype is read from the file
    # itself, so this proves the frontmatter gate independently by using a
    # combat-profile fixture instead.
    findings = lint_combatant_block(
        fixture_path("statblock-clean.md"),  # subtype: absent, type: creature
        "vault/campaigns/shattered-sea/pcs/character-sheets/statblock-clean.md",
    )
    assert findings == []


# --- lint_file dispatch ---------------------------------------------------


def test_lint_file_combines_both_rules() -> None:
    findings = lint_file(
        fixture_path("statblock-broken.md"), "vault/srd/monsters/statblock-broken.md"
    )
    assert len(findings) == 1
    assert findings[0].rule_code == "statblock-simulatable"
