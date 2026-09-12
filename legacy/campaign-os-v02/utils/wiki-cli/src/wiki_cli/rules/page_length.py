"""Ported from npm's W12 (`utils/scripts/lint-rules/w12-page-length.mjs`,
neighbour-relative limit machinery in `lib/pageLengthNeighbors.mjs`).

A page's body has grown well past what pages of its `type:` normally run —
not a flat vault-wide cap, a per-type neighbour-relative one (some content
types are naturally longer than others). Below `PAGE_LENGTH_MIN_SAMPLE`
same-type siblings the median is too thin to trust; the limit falls back to
`PAGE_LENGTH_FALLBACK_MAX`. `PAGE_PROSE_FLOOR` sets an absolute minimum
ceiling regardless of how short a type's siblings run. Table rows count at
a discount (`TABLE_LINE_WEIGHT`) rather than zero — a page that is mostly a
price/stat table is dense, not verbose. A body that is >=80% wikilink-
catalog lines is a link index, not prose, and is exempt outright. SRD pages
and `vault/refs/table-*` transcribe upstream table shapes and are exempt
from the table-line count entirely.

Sibling measure is intentionally the *whole file's* raw text run through
`count_prose_lines` (frontmatter included) — matching
`pageLengthNeighbors.mjs`'s `buildIndex`, which reads `raw.split("\\n")`
with no frontmatter stripping, unlike this rule's own body-only measure of
the page under lint. That asymmetry is inherited verbatim from the legacy
source (bug-compatible port); in practice `PAGE_PROSE_FLOOR` dominates
almost every real verdict, so the few extra frontmatter lines rarely move
the outcome.
"""

from __future__ import annotations

import math
import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.corpus_stats import count_prose_lines, outlier_limit

_TEMPLATES_PREFIX = "vault/_templates/"
"""Markdownlint's own ignore-glob excludes `vault/_templates/**` from every
custom rule upstream (`.obsidian-linter.jsonc` / `lint-findings.mjs`'s
`MARKDOWNLINT_IGNORES`) — replicated here the same way `empty_tags.py`
replicates it, since wiki-cli's own file walk carries no such glob."""

_EXEMPT_PREFIXES = (
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
)
_EXEMPT_EXACT = "vault/campaigns/shattered-sea/dm-voice-script.md"
_TABLE_EXEMPT_PREFIX = "vault/refs/table-"

_LINK_ENTRY_RE = re.compile(r"^\s*(?:[-|*]\s*)?\[\[")

# Single-slot cache scoped to the most recently seen corpus, same pattern
# `unlinked_mention.py`'s `_scan_index_cache` uses: every page in a same-`type:`
# group recomputes every OTHER sibling's prose-line count on its own `check()`
# call, so an N-page type group paid N*(N-1) calls to `count_prose_lines`
# instead of N — the dominant cost of a full-vault sweep for large type
# groups. `sibling.raw` is fixed for the run, so counting once per page and
# reusing it is exactly `count_prose_lines(sibling.raw.splitlines())`, just
# computed once instead of once per group member.
_prose_line_cache: tuple[Corpus, dict[str, float]] | None = None


def _prose_line_counts(corpus: Corpus) -> dict[str, float]:
    global _prose_line_cache
    if _prose_line_cache is not None and _prose_line_cache[0] is corpus:
        return _prose_line_cache[1]
    counts = {p.rel_path: float(count_prose_lines(p.raw.splitlines())) for p in corpus.pages()}
    _prose_line_cache = (corpus, counts)
    return counts


def _js_round(value: float) -> int:
    """`Math.round` semantics (round-half-up), not Python's round-half-to-
    even — matters at the exact `.5` boundary of `tableLines * tableWeight`."""
    return math.floor(value + 0.5)


@register
class PageLengthRule(FileRule):
    """Ported from npm's W12 (`utils/scripts/lint-rules/w12-page-length.mjs`)."""

    id = "W12"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Split by H2 into linked subpages, or transclude a repeated block to its owning page."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if not page.rel_path.startswith("vault/"):
            return
        if page.rel_path.startswith(_TEMPLATES_PREFIX):
            return
        if page.rel_path.startswith(_EXEMPT_PREFIXES) or page.rel_path == _EXEMPT_EXACT:
            return

        page_type = page.type
        if page_type is None:
            return  # W84's own job

        config = load_config()
        headroom_pct = float(config.threshold("PAGE_LENGTH_HEADROOM_PCT"))
        min_sample = int(config.threshold("PAGE_LENGTH_MIN_SAMPLE"))
        fallback_max = float(config.threshold("PAGE_LENGTH_FALLBACK_MAX"))
        prose_floor = float(config.threshold("PAGE_PROSE_FLOOR"))
        table_weight = float(config.threshold("TABLE_LINE_WEIGHT"))

        body_lines = [text for _, text in page.body_lines()]
        is_table_exempt = page.frontmatter.get("status") == "srd" or page.rel_path.startswith(
            _TABLE_EXEMPT_PREFIX
        )
        table_lines = (
            0 if is_table_exempt else sum(1 for line in body_lines if line.strip().startswith("|"))
        )
        prose_lines = count_prose_lines(body_lines)
        line_count = prose_lines + _js_round(table_lines * table_weight)

        siblings = [
            sibling for sibling in corpus.by_type(page_type) if sibling.rel_path != page.rel_path
        ]
        prose_counts = _prose_line_counts(corpus)
        sibling_values = [prose_counts[sibling.rel_path] for sibling in siblings]

        resolved = outlier_limit(
            sibling_values,
            headroom_pct=headroom_pct,
            min_sample=min_sample,
            fallback_max=fallback_max,
            floor=prose_floor,
        )
        assert resolved is not None  # W12 always carries a fallback_max
        limit = math.ceil(resolved.limit)

        if line_count <= limit:
            return

        link_entry_lines = sum(1 for line in body_lines if _LINK_ENTRY_RE.match(line))
        if line_count > 0 and link_entry_lines / line_count >= 0.8:
            return

        basis_note = (
            f"{resolved.sample_size} same-type pages, median {resolved.sibling_median:g}"
            if resolved.basis == "neighbours"
            else f"fallback — only {resolved.sample_size} same-type pages"
        )
        yield self.finding(
            file=page.rel_path,
            line=page.body_start_line,
            message=(
                f"Page body is {line_count} effective lines ({prose_lines} prose + "
                f"{table_lines} table rows at {table_weight:g}x, fences excluded; limit "
                f"{limit}, {basis_note}) — trim redundancy, transclude/wikilink a repeated "
                "block to its owning page, or split by H2 into linked subpages; never trim "
                "at the cost of losing information or wikilinks"
            ),
        )
