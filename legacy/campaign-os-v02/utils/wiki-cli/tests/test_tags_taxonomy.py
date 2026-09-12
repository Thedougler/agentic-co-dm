"""TDD for the tags-taxonomy cluster (W111, W112, W113), ported from npm's
w111/w112/w113-*.mjs — see each rule module's docstring for the legacy
source. Fixtures: tests/fixtures/tags_taxonomy/.

All three rules read `docs/tags.md` from disk rather than from the page
under check, so every test instantiates the rule directly with a
`taxonomy_path` override pointed at the fixture doc instead of going
through `registry()` (whose singleton resolves the real repo's
`docs/tags.md` via `config.repo_root` in production).
"""

from __future__ import annotations

from pathlib import Path

from wiki_cli.contracts import Page, Tier, registry
from wiki_cli.markdown import load_page
from wiki_cli.rules.narrative_domain_tag import NarrativeDomainTagRule
from wiki_cli.rules.tag_alias_direct_use import TagAliasDirectUseRule
from wiki_cli.rules.tag_taxonomy_doc import TagTaxonomyDocRule

FIXTURES = Path(__file__).parent / "fixtures" / "tags_taxonomy"


class _StubCorpus:
    """Minimal `Corpus`-shaped stand-in — none of these rules call it."""

    repo_root = None  # type: ignore[assignment]


def _check(rule: object, page: Page) -> list:
    return list(rule.check(page, _StubCorpus()))  # type: ignore[union-attr,arg-type]


def test_all_three_rules_are_registered_under_their_w_ids() -> None:
    reg = registry()
    assert reg["W112"].tier == Tier.STRUCTURAL
    assert reg["W111"].tier == Tier.STRUCTURAL
    assert reg["W113"].tier == Tier.STRUCTURAL


# --- W112: docs/tags.md itself --------------------------------------------

_W112_MALFORMED_DIR = FIXTURES / "w112-malformed"
_W112_CLEAN_DIR = FIXTURES / "w112-clean"


def test_w112_malformed_doc_fires_once_per_planted_defect() -> None:
    tags_path = _W112_MALFORMED_DIR / "docs" / "tags.md"
    page = load_page(_W112_MALFORMED_DIR, "docs/tags.md")
    rule = TagTaxonomyDocRule(taxonomy_path=tags_path)

    findings = _check(rule, page)

    assert len(findings) == 5
    by_line = {f.line: f for f in findings}
    assert all(f.rule_id == "W112" for f in findings)
    assert "does not parse as a tag entry" in by_line[9].message
    assert "is defined twice (line 13)" in by_line[14].message
    assert "parses as a fourth tag group" in by_line[16].message
    assert "is not a canonical tag" in by_line[23].message
    assert "outside the tag sections" in by_line[27].message


def test_w112_only_the_duplicate_finding_is_fixable() -> None:
    tags_path = _W112_MALFORMED_DIR / "docs" / "tags.md"
    page = load_page(_W112_MALFORMED_DIR, "docs/tags.md")
    rule = TagTaxonomyDocRule(taxonomy_path=tags_path)

    findings = _check(rule, page)

    fixable_lines = {f.line for f in findings if f.fixable}
    assert fixable_lines == {14}


def test_w112_fires_only_on_docs_tags_md() -> None:
    tags_path = _W112_MALFORMED_DIR / "docs" / "tags.md"
    page = load_page(_W112_MALFORMED_DIR, "vault/other.md")
    rule = TagTaxonomyDocRule(taxonomy_path=tags_path)

    assert _check(rule, page) == []


def test_w112_well_formed_doc_stays_silent() -> None:
    tags_path = _W112_CLEAN_DIR / "docs" / "tags.md"
    page = load_page(_W112_CLEAN_DIR, "docs/tags.md")
    rule = TagTaxonomyDocRule(taxonomy_path=tags_path)

    assert _check(rule, page) == []


# --- W111 / W113: narrative pages carrying tags ----------------------------

_NARRATIVE_DIR = FIXTURES / "w111-w113"
_NARRATIVE_TAGS = _NARRATIVE_DIR / "docs" / "tags.md"


def _narrative_page(rel_path: str) -> Page:
    return load_page(_NARRATIVE_DIR, rel_path)


def test_w111_narrative_page_without_domain_tag_fires_listing_domain_members() -> None:
    rule = NarrativeDomainTagRule(taxonomy_path=_NARRATIVE_TAGS)
    page = _narrative_page("vault/npcs/no-domain.md")

    findings = _check(rule, page)

    assert len(findings) == 1
    assert findings[0].rule_id == "W111"
    assert "no Domain tag" in findings[0].message
    assert "intrigue" in findings[0].message


def test_w111_page_already_carrying_a_domain_tag_is_clean() -> None:
    rule = NarrativeDomainTagRule(taxonomy_path=_NARRATIVE_TAGS)
    assert _check(rule, _narrative_page("vault/npcs/has-domain.md")) == []


def test_w111_alias_resolving_to_a_domain_member_satisfies_the_check() -> None:
    rule = NarrativeDomainTagRule(taxonomy_path=_NARRATIVE_TAGS)
    assert _check(rule, _narrative_page("vault/npcs/alias-domain-draft.md")) == []
    assert _check(rule, _narrative_page("vault/npcs/block-list-alias.md")) == []
    assert _check(rule, _narrative_page("vault/npcs/alias-canon.md")) == []


def test_w111_exempt_cases_stay_silent() -> None:
    rule = NarrativeDomainTagRule(taxonomy_path=_NARRATIVE_TAGS)
    exempt_pages = (
        "vault/npcs/empty-tags.md",  # W27's job
        "vault/npcs/no-type.md",  # W84's job
        "vault/npcs/ingest-review.md",  # pipeline scaffolding
        "vault/npcs/only-visibility.md",  # empty remainder after stripping visibility tags
        "vault/guides/non-narrative-type.md",  # non-narrative content type
    )
    for rel_path in exempt_pages:
        assert _check(rule, _narrative_page(rel_path)) == []


def test_w113_alias_tag_on_a_draft_page_fires_and_is_fixable() -> None:
    rule = TagAliasDirectUseRule(taxonomy_path=_NARRATIVE_TAGS)
    page = _narrative_page("vault/npcs/alias-domain-draft.md")

    findings = _check(rule, page)

    assert len(findings) == 1
    assert findings[0].rule_id == "W113"
    assert findings[0].line == 3
    assert 'tag "boss-fight" is an alias' in findings[0].message
    assert 'replace with "combat"' in findings[0].message
    assert findings[0].fixable is True


def test_w113_same_alias_on_a_canon_page_fires_with_no_fixable_flag() -> None:
    rule = TagAliasDirectUseRule(taxonomy_path=_NARRATIVE_TAGS)
    page = _narrative_page("vault/npcs/alias-canon.md")

    findings = _check(rule, page)

    assert len(findings) == 1
    assert 'tag "boss-fight" is an alias' in findings[0].message
    assert findings[0].fixable is False


def test_w113_alias_in_block_list_shape_fires_and_is_fixable() -> None:
    rule = TagAliasDirectUseRule(taxonomy_path=_NARRATIVE_TAGS)
    page = _narrative_page("vault/npcs/block-list-alias.md")

    findings = _check(rule, page)

    assert len(findings) == 1
    assert findings[0].line == 4
    assert findings[0].fixable is True


def test_w113_page_with_no_alias_tags_stays_silent() -> None:
    rule = TagAliasDirectUseRule(taxonomy_path=_NARRATIVE_TAGS)
    assert _check(rule, _narrative_page("vault/npcs/has-domain.md")) == []
