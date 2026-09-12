"""Port tests for the skill-hygiene cluster (wiki-lint migration Task 17):
W72 (skill-length), W75 (doc-pointer-resolves), W79 (skill-description-
budget), W80 (skill-trigger-overlap), W81 (claude-md-kit-budget) — ported
from utils/scripts/lint-rules/w72-*.mjs, w75-*.mjs, w79-*.mjs, w80-*.mjs,
w81-*.mjs.

Fixtures live under `fixtures/skill_hygiene/.claude/skills/` (a mini skills
tree) and `fixtures/skill_hygiene/w81/<case>/CLAUDE.md` (one directory per
W81 case, since the rule only fires on a file at exactly `CLAUDE.md`).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import wiki_cli.rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.config import load_config
from wiki_cli.contracts import Finding, Page, registry
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "skill_hygiene"


@dataclass
class _StubCorpus:
    """Minimal `Corpus` stand-in — every rule in this cluster only ever
    reads `repo_root` off the corpus, never the page graph."""

    repo_root: Path

    def pages(self):
        return []

    def resolve(self, name: str):
        del name

    def by_type(self, page_type: str):
        del page_type
        return []

    def links_from(self, rel_path: str):
        del rel_path
        return []

    def links_to(self, rel_path: str):
        del rel_path
        return []


def _check(rule_id: str, rel_path: str, *, repo_root: Path = FIXTURES) -> list[Finding]:
    rule = registry()[rule_id]
    page = load_page(repo_root, rel_path)
    return list(rule.check(page, _StubCorpus(repo_root)))


# ---- W72: skill-length ------------------------------------------------


def test_w72_clean_under_line_cap():
    assert _check("W72", ".claude/skills/short-skill/SKILL.md") == []


def test_w72_flags_over_line_cap():
    findings = _check("W72", ".claude/skills/too-long-skill/SKILL.md")
    assert len(findings) == 1
    assert findings[0].rule_id == "W72"
    assert findings[0].line == 201
    assert "205 lines" in findings[0].message
    assert "cap 200" in findings[0].message


def test_w72_ignores_non_skill_path():
    page = Page(
        rel_path=".claude/skills/short-skill/references/notes.md",
        raw="x\n" * 500,
        frontmatter={},
        body="x\n" * 500,
        body_start_line=1,
    )
    rule = registry()["W72"]
    assert list(rule.check(page, _StubCorpus(FIXTURES))) == []


# ---- W75: doc-pointer-resolves -----------------------------------------


def test_w75_clean_when_pointer_resolves_in_own_dir():
    assert _check("W75", ".claude/skills/pointer-ok-skill/SKILL.md") == []


def test_w75_flags_pointer_resolving_nowhere():
    findings = _check("W75", ".claude/skills/pointer-broken-skill/SKILL.md")
    assert len(findings) == 1
    assert findings[0].rule_id == "W75"
    assert "references/missing.md" in findings[0].message


def test_w75_ignores_out_of_scope_path():
    page = Page(
        rel_path="vault/some-page.md",
        raw="see `references/missing.md`\n",
        frontmatter={},
        body="see `references/missing.md`\n",
        body_start_line=1,
    )
    rule = registry()["W75"]
    assert list(rule.check(page, _StubCorpus(FIXTURES))) == []


# ---- W79: skill-description-budget --------------------------------------


def test_w79_clean_under_both_budgets():
    assert _check("W79", ".claude/skills/desc-ok-skill/SKILL.md") == []


def test_w79_flags_over_word_budget():
    findings = _check("W79", ".claude/skills/desc-over-word-budget-skill/SKILL.md")
    assert len(findings) == 1
    assert findings[0].rule_id == "W79"
    assert "100 words" in findings[0].message
    assert "budget ~80" in findings[0].message


def test_w79_flags_over_char_cap_and_subsumes_word_finding():
    findings = _check("W79", ".claude/skills/desc-over-char-cap-skill/SKILL.md")
    assert len(findings) == 1
    assert findings[0].rule_id == "W79"
    assert "1679 characters" in findings[0].message
    assert "past 1536" in findings[0].message


# ---- W80: skill-trigger-overlap (VaultRule) -----------------------------


def _w80_findings() -> list[Finding]:
    rule = registry()["W80"]
    return list(rule.check(_StubCorpus(FIXTURES)))


def test_w80_flags_near_duplicate_pair_both_directions():
    flagged = {f.file for f in _w80_findings()}
    assert ".claude/skills/trigger-overlap-a/SKILL.md" in flagged
    assert ".claude/skills/trigger-overlap-b/SKILL.md" in flagged


def test_w80_distinct_skill_stays_clean():
    findings = _w80_findings()
    assert all(f.file != ".claude/skills/trigger-distinct/SKILL.md" for f in findings)


def test_w80_message_names_the_other_file():
    findings = _w80_findings()
    a_finding = next(
        f for f in findings if f.file == ".claude/skills/trigger-overlap-a/SKILL.md"
    )
    assert "trigger-overlap-b/SKILL.md" in a_finding.message


# ---- W81: claude-md-kit-budget -------------------------------------------


def _check_w81(case: str) -> list[Finding]:
    return _check("W81", "CLAUDE.md", repo_root=FIXTURES / "w81" / case)


def test_w81_clean_within_every_budget():
    assert _check_w81("clean") == []


def test_w81_flags_over_iron_rule_budget():
    findings = _check_w81("over-iron-rules")
    assert len(findings) == 1
    assert "16 iron rules" in findings[0].message
    assert "budget 15" in findings[0].message


def test_w81_flags_over_caps_budget():
    findings = _check_w81("over-caps")
    assert len(findings) == 1
    assert "6 NEVER/ALWAYS/MUST lines" in findings[0].message
    assert "budget 5" in findings[0].message


def test_w81_flags_over_zone_line_budget():
    findings = _check_w81("over-zone-lines")
    assert len(findings) == 1
    assert "69 lines" in findings[0].message
    assert "budget 60" in findings[0].message


def test_w81_flags_multiple_routing_tables():
    findings = _check_w81("multi-table")
    assert len(findings) == 1
    assert "2 routing tables" in findings[0].message


def test_w81_no_kit_markers_stays_silent():
    assert _check_w81("no-kit-markers") == []


def test_w81_subtree_claude_md_never_fires():
    page = Page(
        rel_path="vault/CLAUDE.md",
        raw="\n".join(["## Iron rules", *[f"- Rule {i}." for i in range(1, 20)]]),
        frontmatter={},
        body="",
        body_start_line=1,
    )
    rule = registry()["W81"]
    assert list(rule.check(page, _StubCorpus(FIXTURES))) == []


def test_w81_thresholds_read_from_wiki_toml():
    config = load_config()
    assert config.threshold("KIT_MAX_IRON_RULES") == "15"
    assert config.threshold("KIT_MAX_CAPS_LINES") == "5"
    assert config.threshold("KIT_MAX_ZONE_LINES") == "60"
