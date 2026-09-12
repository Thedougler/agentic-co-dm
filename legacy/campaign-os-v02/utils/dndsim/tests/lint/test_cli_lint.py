"""``dndsim lint --json`` — the payload-shape half of ADR-0010's contract:
identical to ``markdownlint-obsidian --output-formatter json``'s own shape,
so ``utils/scripts/lib/lint-findings.mjs`` can concatenate the two producers'
arrays without any format translation.
"""

from __future__ import annotations

from pathlib import Path

from dndsim.lint.findings import build_payload
from dndsim.lint.rules import lint_file
from dndsim.lint.run import lint_paths

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def test_payload_shape_matches_markdownlint_obsidian_json() -> None:
    payload = lint_paths([FIXTURES_DIR / "statblock-clean.md"])
    assert len(payload) == 1
    entry = payload[0]
    assert set(entry.keys()) == {"filePath", "errors"}
    file_path = entry["filePath"]
    assert isinstance(file_path, str)
    assert Path(file_path).is_absolute()
    assert entry["errors"] == []


def test_payload_carries_full_error_shape_when_dirty() -> None:
    # lint_paths resolves scope from the fixture's real on-disk path (not
    # under vault/srd/monsters/ or vault/campaigns/shattered-sea/monsters/),
    # so it's silent by design —
    # build the payload directly from lint_file with an in-scope rel
    # instead, the same way run.py's own _rel() would once this file
    # actually lived in the vault.
    path = FIXTURES_DIR / "statblock-broken.md"
    payload = build_payload([(path, lint_file(path, "vault/srd/monsters/statblock-broken.md"))])
    assert len(payload) == 1
    errors = payload[0]["errors"]
    assert len(errors) == 1
    err = errors[0]
    assert set(err.keys()) == {
        "ruleCode",
        "ruleName",
        "severity",
        "line",
        "column",
        "message",
        "fixable",
    }
    assert err["ruleCode"] == "statblock-simulatable"
    assert err["ruleName"] == "W-statblock-simulatable"
    assert err["severity"] == "error"
    assert err["fixable"] is False


def test_build_payload_always_includes_a_clean_file_entry() -> None:
    # markdownlint-obsidian lists every requested file, errors: [] for a
    # clean one — build_payload must reproduce that, never omit clean files.
    payload = build_payload([(FIXTURES_DIR / "statblock-clean.md", [])])
    assert payload == [
        {"filePath": str((FIXTURES_DIR / "statblock-clean.md").resolve()), "errors": []}
    ]
