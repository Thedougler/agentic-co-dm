"""TDD for the five frontmatter-hygiene rules ported from the npm engine:
W27 (empty-tags), W89 (unsummarized-page), W118 (source-resolves), W98
(slug-kebab-case), W38 (dead-weight).

Every fixture is a real file on disk under `fixtures/frontmatter_hygiene/`,
loaded through the real `load_page` parser — no in-memory `Page` stand-ins,
so each test proves the rule against real frontmatter/body text, not a
hand-built object. Fixture rel_paths are given relative to `FIXTURES`
itself and always start with `vault/`, matching every ported rule's own
`vault/`-prefix scope check.

W118 is the one impure rule here — it needs a real filesystem to resolve
`source:` against, so its cases pass an explicit stub `corpus` whose
`repo_root` points at `FIXTURES` (mirroring the fixture's own `raw/`
sibling directory), rather than the default `corpus=None` every pure rule
ignores.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.contracts import registry
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "frontmatter_hygiene"


class _StubCorpus:
    """Minimal `Corpus`-shaped stand-in carrying only `repo_root` — the one
    field W118 actually reads."""

    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root


def check(rule_id: str, fixture: str, *, corpus: object | None = None):
    rule = registry()[rule_id]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, corpus))


# --- W27: empty-tags -----------------------------------------------------


def test_w27_no_tags_key_fires() -> None:
    findings = check("W27", "vault/w27/no-tags.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "W27"
    assert findings[0].file == "vault/w27/no-tags.md"


def test_w27_tagged_page_stays_silent() -> None:
    assert check("W27", "vault/w27/tagged-clean.md") == []


# --- W89: unsummarized-page ------------------------------------------------


def test_w89_long_page_no_summary_fires() -> None:
    findings = check("W89", "vault/w89/long-no-summary.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "W89"
    assert "summary:" in findings[0].message


def test_w89_page_with_summary_stays_silent() -> None:
    assert check("W89", "vault/w89/long-with-summary.md") == []


def test_w89_short_page_no_summary_fires() -> None:
    findings = check("W89", "vault/w89/short-no-summary.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "W89"


def test_w89_derived_data_page_no_summary_fires() -> None:
    findings = check("W89", "vault/w89/derived-no-summary.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "W89"


# --- W118: source-resolves ---------------------------------------------


def test_w118_dangling_source_fires() -> None:
    corpus = _StubCorpus(FIXTURES)

    findings = check("W118", "vault/w118/missing.md", corpus=corpus)

    assert len(findings) == 1
    assert findings[0].rule_id == "W118"
    assert "does not resolve" in findings[0].message


def test_w118_resolving_source_stays_silent() -> None:
    corpus = _StubCorpus(FIXTURES)

    assert check("W118", "vault/w118/resolves.md", corpus=corpus) == []


# --- W98: slug-kebab-case -------------------------------------------------


def test_w98_bad_basename_fires() -> None:
    findings = check("W98", "vault/w98/Bad_Name.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "W98"
    assert "bad-name.md" in findings[0].message


def test_w98_clean_basename_stays_silent() -> None:
    assert check("W98", "vault/w98/clean-slug.md") == []


# --- W38: dead-weight ------------------------------------------------------


def test_w38_empty_section_fires() -> None:
    findings = check("W38", "vault/w38/empty-section.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "W38"
    assert "Background" in findings[0].message


def test_w38_leftover_agent_comment_fires() -> None:
    findings = check("W38", "vault/w38/agent-comment.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "W38"
    assert "AGENT" in findings[0].message


def test_w38_clean_page_stays_silent() -> None:
    assert check("W38", "vault/w38/clean.md") == []
