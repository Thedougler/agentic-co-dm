"""TDD for the first four `Corpus`/`VaultIndex` consumers ported from the
npm engine (ADR-0042): W18 (redirect-resolution), W57 (duplicate-basename),
W76 (outside-wiki-family-reference), W116 (embed-heading-resolves).

All four are exercised against one mini-vault (`tests/fixtures/link_graph/`)
so a single `VaultIndex.build()` proves the `Corpus` interface for every
rule shape this cluster introduces: FileRule (corpus) for W18/W116,
VaultRule for W57, and a plain FileRule (fs-dependent, no corpus lookup for
detection itself) for W76.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.contracts import Finding, registry
from wiki_cli.index import VaultIndex
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "link_graph"


def _corpus() -> VaultIndex:
    return VaultIndex.build(FIXTURES, FIXTURES / "vault", ("vault",))


def check_file(rule_id: str, fixture: str, corpus: VaultIndex | None = None) -> list[Finding]:
    rule = registry()[rule_id]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, corpus or _corpus()))


def check_vault(rule_id: str, corpus: VaultIndex | None = None) -> list[Finding]:
    rule = registry()[rule_id]
    return list(rule.check(corpus or _corpus()))


# --- W18: redirect-resolution -------------------------------------------


def test_w18_dangling_redirect_fires() -> None:
    findings = check_file("W18", "vault/redirects/dangling-redirect.md")

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W18"
    assert finding.file == "vault/redirects/dangling-redirect.md"
    assert "dangling redirect" in finding.message


def test_w18_chained_redirect_fires() -> None:
    findings = check_file("W18", "vault/redirects/chain-start.md")

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W18"
    assert "redirect chain" in finding.message
    assert "chain-middle" in finding.message


def test_w18_resolving_clean_redirect_stays_silent() -> None:
    assert check_file("W18", "vault/redirects/clean-redirect.md") == []


def test_w18_chain_link_that_itself_resolves_cleanly_stays_silent() -> None:
    # chain-middle.md is itself a stub (fires as chain-start.md's target
    # above), but checked on its own it points at real-target.md, which is
    # not a stub — clean.
    assert check_file("W18", "vault/redirects/chain-middle.md") == []


def test_w18_out_of_scope_path_stays_silent() -> None:
    assert check_file("W18", "vault/real-target.md") == []


# --- W57: duplicate-basename ---------------------------------------------


def test_w57_colliding_pair_both_fire() -> None:
    findings = [f for f in check_vault("W57") if "duplicate-slug" in f.file]

    assert len(findings) == 2
    files = {f.file for f in findings}
    assert files == {"vault/w57/dup-a/duplicate-slug.md", "vault/w57/dup-b/duplicate-slug.md"}
    for finding in findings:
        assert finding.rule_id == "W57"
        other = "vault/w57/dup-b/duplicate-slug.md" if "dup-a" in finding.file else "vault/w57/dup-a/duplicate-slug.md"
        assert other in finding.message


def test_w57_unique_basename_stays_silent() -> None:
    findings = check_vault("W57")
    assert not any(f.file == "vault/w57/unique-page.md" for f in findings)


# --- W76: outside-wiki-family-reference -----------------------------------


def test_w76_link_into_docs_with_no_match_fires() -> None:
    findings = check_file("W76", "vault/w76/outside-link.md")

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W76"
    assert "outside the wiki family" in finding.message
    assert "no same-named page exists" in finding.message


def test_w76_link_outside_family_with_same_named_match_fires_and_names_it() -> None:
    findings = check_file("W76", "vault/w76/outside-with-match.md")

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W76"
    assert "a same-named page exists at `vault/w76/orphan-notes.md`" in finding.message


def test_w76_in_family_link_stays_clean() -> None:
    assert check_file("W76", "vault/w76/in-family-clean.md") == []


# --- W116: embed-heading-resolves -----------------------------------------


def test_w116_embed_referencing_missing_heading_fires() -> None:
    findings = check_file("W116", "vault/w116/missing-heading.md")

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W116"
    assert "#Old Name" in finding.message
    assert "vault/w116/target-page.md" in finding.message


def test_w116_embed_matching_real_heading_stays_silent() -> None:
    assert check_file("W116", "vault/w116/resolving-clean.md") == []
