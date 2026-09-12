"""W146 — goal: required on narration, dialogue, handout."""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401
from wiki_cli.contracts import FileRule, registry
from wiki_cli.index import VaultIndex


def _check(corpus: VaultIndex) -> list:
    rule = registry()["W146"]
    assert isinstance(rule, FileRule)
    findings = []
    for page in corpus.pages():
        findings.extend(rule.check(page, corpus))
    return [f for f in findings if f.rule_id == "W146"]


def test_missing_goal_fails(tmp_path: Path) -> None:
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    page = tmp_path / "vault" / "dock-narration-open.md"
    page.write_text(
        "---\ntype: narration\nmode: establish\nparent: '[[dock]]'\n---\n\n"
        "*The basin smells of hide.*\n",
        encoding="utf-8",
    )
    findings = _check(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",)))
    assert len(findings) == 1, f"expected 1; got {findings}"


def test_empty_goal_fails(tmp_path: Path) -> None:
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    page = tmp_path / "vault" / "dock-narration-open.md"
    page.write_text(
        "---\ntype: narration\ngoal: ''\nmode: establish\nparent: '[[dock]]'\n---\n\n"
        "*The basin smells of hide.*\n",
        encoding="utf-8",
    )
    findings = _check(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",)))
    assert len(findings) == 1, f"expected 1; got {findings}"


def test_goal_present_is_silent(tmp_path: Path) -> None:
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    page = tmp_path / "vault" / "dock-narration-open.md"
    page.write_text(
        "---\ntype: narration\ngoal: Tribute is unpaid; the ship can sail.\n"
        "mode: establish\nparent: '[[dock]]'\n---\n\n"
        "*The basin smells of hide.*\n",
        encoding="utf-8",
    )
    assert _check(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))) == []
