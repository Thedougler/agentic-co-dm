"""TDD for W144: depiction camera — no player state on non-session narration."""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401
from wiki_cli.contracts import FileRule, registry
from wiki_cli.index import VaultIndex


def _check(corpus: VaultIndex) -> list:
    rule = registry()["W144"]
    assert isinstance(rule, FileRule)
    findings = []
    for page in corpus.pages():
        findings.extend(rule.check(page, corpus))
    return [f for f in findings if f.rule_id == "W144"]


def test_depiction_you_yields_finding(tmp_path: Path) -> None:
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    page = tmp_path / "vault" / "nona-narration-appearance.md"
    page.write_text(
        "---\ntype: narration\nmode: establish\nparent: '[[nona]]'\n---\n\n"
        "*You see salt in her fur.*\n",
        encoding="utf-8",
    )
    findings = _check(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",)))
    assert len(findings) == 1, f"expected 1 finding; got {findings}"
    assert "you" in findings[0].message.lower()


def test_moment_narration_you_allowed(tmp_path: Path) -> None:
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    page = tmp_path / "vault" / "moment-01-open-narration-open.md"
    page.write_text(
        "---\ntype: narration\nmode: establish\nparent: '[[moment-01-open]]'\n---\n\n"
        "*The wreck lists. What do you do?*\n",
        encoding="utf-8",
    )
    findings = _check(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",)))
    assert findings == [], f"expected 0 findings on moment narration; got {findings}"


def test_recap_you_allowed(tmp_path: Path) -> None:
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    page = tmp_path / "vault" / "e09-run-guide-narration-last-time.md"
    page.write_text(
        "---\ntype: narration\nmode: recap\nparent: '[[e09-run-guide]]'\n---\n\n"
        "*You limped the Uncertainty into the basin.*\n",
        encoding="utf-8",
    )
    findings = _check(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",)))
    assert findings == [], f"expected 0 findings on recap; got {findings}"
