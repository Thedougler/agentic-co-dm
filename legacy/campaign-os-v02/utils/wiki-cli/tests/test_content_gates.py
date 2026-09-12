"""TDD for the three content-gate rules ported from the npm engine
(ADR-0041): W47 (story-first-gate), W90 (template-boilerplate-leak), and
W123 (link-footer-section).

W47 needs a real filesystem root to list `vault/episodes/NNN/` against — a
`_StubCorpus` pointed at the fixtures tree stands in for the real vault so
the gate can be exercised both ways without touching the real episode
folders. W90 and W123 never touch `corpus` (W90 resolves templates via the
real `vault/_templates/`, same as `FrontmatterSchemaRule`; W123 is pure
text), so the stub is harmless for them too.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.contracts import Finding, registry
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "content_gates"


class _StubCorpus:
    """Minimal `Corpus`-shaped stand-in, rooted at the fixtures tree."""

    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root


def check(rule_id: str, fixture: str) -> list[Finding]:
    rule = registry()[rule_id]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, _StubCorpus(FIXTURES)))


# --- W47: story-first-gate ---------------------------------------------


def test_w47_run_guide_with_no_story_fires() -> None:
    findings = check("W47", "vault/episodes/009/run-guide.md")

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W47"
    assert "session-09-" in finding.message


def test_w47_run_guide_with_story_stays_silent() -> None:
    assert check("W47", "vault/episodes/008/run-guide.md") == []


def test_w47_non_run_guide_path_stays_silent() -> None:
    assert check("W47", "vault/episodes/008/session-08-mock-story.md") == []


def test_w47_beat_with_no_story_fires() -> None:
    findings = check("W47", "vault/episodes/009/beat-01-hook.md")

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W47"
    assert "session-09-" in finding.message


def test_w47_beat_with_story_stays_silent() -> None:
    assert check("W47", "vault/episodes/008/beat-01-hook.md") == []


# --- W90: template-boilerplate-leak -------------------------------------


def test_w90_leaked_template_sentence_fires() -> None:
    findings = check(
        "W90", "vault/campaigns/shattered-sea/locations/w90-leaked-sentence.md"
    )

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W90"
    assert "scaffolding prose" in finding.message


def test_w90_edited_body_stays_clean() -> None:
    assert check("W90", "vault/campaigns/shattered-sea/locations/w90-clean.md") == []


# --- W123: link-footer-section -------------------------------------------


def test_w123_link_dump_footer_fires() -> None:
    findings = check("W123", "vault/locations/w123-link-dump-footer.md")

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W123"
    assert "link-footer section" in finding.message


def test_w123_prose_with_no_footer_heading_stays_clean() -> None:
    assert check("W123", "vault/locations/w123-clean.md") == []
