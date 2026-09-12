"""TDD for the corpus-stats cluster ported from the npm engine (ADR-0042):
W12 (page-length) and W120 (section-count-outlier), plus the shared math
in `wiki_cli.corpus_stats`.

Both rules are corpus rules (`FileRule`, `pure = False`) — they judge one
page against its same-`type:` siblings, so every test builds a real
`VaultIndex` over `tests/fixtures/corpus_stats/vault/` rather than passing
a bare `Page` with `corpus=None`. W35 (verbose-section) is not ported here:
`utils/scripts/lint-rules/README.md`'s Retired list carries it
(docs/adr/0043 — Vale handles prose length), predating this task.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.contracts import registry
from wiki_cli.corpus_stats import (
    count_h2_sections,
    count_prose_lines,
    median,
    outlier_limit,
    quantile,
)
from wiki_cli.index import VaultIndex

FIXTURES = Path(__file__).parent / "fixtures" / "corpus_stats"

_CORPUS = None


def _corpus():
    global _CORPUS
    if _CORPUS is None:
        _CORPUS = VaultIndex.build(FIXTURES, FIXTURES / "vault", ("vault",))
    return _CORPUS


def check(rule_id: str, rel_path: str):
    rule = registry()[rule_id]
    corpus = _corpus()
    page = next(p for p in corpus.pages() if p.rel_path == rel_path)
    return list(rule.check(page, corpus))


# --- shared math ------------------------------------------------------


def test_median_odd_and_even():
    assert median([3, 1, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5


def test_quantile_p90():
    assert quantile([1, 2, 3, 4, 5], 0.9) == 4.6


def test_count_prose_lines_excludes_data():
    lines = ["", "prose", "| a | b |", "<!-- comment -->", "```", "## in fence", "```", "more"]
    assert count_prose_lines(lines) == 2  # "prose" and "more"


def test_count_h2_sections_excludes_fenced():
    lines = ["## Real", "text", "```", "## Fake", "```", "## Also Real"]
    assert count_h2_sections(lines) == 2


def test_outlier_limit_below_min_sample_with_fallback():
    result = outlier_limit([], headroom_pct=100, min_sample=1, fallback_max=400, floor=150)
    assert result is not None
    assert result.basis == "fallback"
    assert result.limit == 400


def test_outlier_limit_below_min_sample_no_fallback_is_none():
    assert outlier_limit([1, 2], headroom_pct=100, min_sample=5, fallback_max=None, floor=9) is None


# --- W12: page-length ---------------------------------------------------


def test_w12_page_too_long_fires():
    findings = check("W12", "vault/w12/page-too-long.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "W12"
    assert findings[0].file == "vault/w12/page-too-long.md"


def test_w12_short_page_stays_silent():
    assert check("W12", "vault/w12/page-ok.md") == []


def test_w12_link_catalog_exempt_even_though_long():
    assert check("W12", "vault/w12/link-catalog.md") == []


def test_w12_short_sibling_stays_silent():
    assert check("W12", "vault/w12/sibling-1.md") == []


# --- W120: section-count-outlier -----------------------------------------


def test_w120_11_sections_fires_and_excludes_fenced_heading():
    findings = check("W120", "vault/w120/atomicity-violation.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "W120"
    assert findings[0].severity.value == "warning"
    assert "11 H2 sections" in findings[0].message
    assert "ONE-FACT-ONE-PAGE" in findings[0].message


def test_w120_3_sections_against_low_siblings_stays_silent():
    assert check("W120", "vault/w120/atomicity-clean.md") == []


def test_w120_low_section_sibling_stays_silent():
    assert check("W120", "vault/w120/sibling-1.md") == []


def test_w120_derived_data_type_exempt_even_with_many_sections():
    assert check("W120", "vault/w120/derived-data-exempt.md") == []
