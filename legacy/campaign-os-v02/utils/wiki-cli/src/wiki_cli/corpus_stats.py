"""Shared corpus-wide statistics ported from npm's `lib/corpusStats.mjs`
and `lib/pageLengthNeighbors.mjs` — ONLY the pieces W12 (page-length) and
W120 (section-count-outlier) need. W64/W65/W66 (sentence/paragraph length,
cliché density) are cut per `rules-audit.md`; `computeGroupStats`'s generic
arbitrary-grouping machinery those three relied on is not ported — W12 and
W120 both group by bare `type:`, which `wiki_cli.index.VaultIndex` already
indexes once per run via `Corpus.by_type`, so the JS engine's own
file-walk-and-cache layer (`walkFiles`/`computeGroupStats`) has no
counterpart here: a rule module calls `corpus.by_type(page.type)` directly
instead.

`outlier_limit` below generalizes `pageLengthNeighbors.mjs`'s
`resolvePageLengthLimit` (W12) and w120's own inline copy of the identical
shape (median * headroom, sibling p90, absolute floor; below a minimum
sample the measure is too thin to trust) so both rule modules share the
one implementation instead of each re-deriving it.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

_FENCE_LINE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")
_COMMENT_ONLY_RE = re.compile(r"^<!--.*-->$")
_H2_RE = re.compile(r"^## ")


def fenced_line_flags(lines: Sequence[str]) -> list[bool]:
    """Same CommonMark-correct fence tracker as `lib/fences.mjs`'s
    `fencedLineFlags` (also duplicated per-rule in `unsummarized_page.py`
    and `dead_weight.py`, each kept deliberately self-contained — this
    cluster's shared math lives here instead per the migration plan's
    Task 16 spec). A fence opened with N backtick/tilde characters closes
    only on a line using the same character, a run of at least N, and
    nothing else."""
    flags = [False] * len(lines)
    open_fence: tuple[str, int] | None = None
    for index, line in enumerate(lines):
        if open_fence is None:
            match = _FENCE_LINE_RE.match(line)
            if match:
                marker = match.group(1)
                open_fence = (marker[0], len(marker))
                flags[index] = True
            continue
        flags[index] = True
        closing = _CLOSING_ONLY_RE.match(line)
        if (
            closing
            and closing.group(1)[0] == open_fence[0]
            and len(closing.group(1)) >= open_fence[1]
        ):
            open_fence = None
    return flags


def count_prose_lines(lines: Sequence[str]) -> int:
    """Same measure as `corpusStats.mjs`'s `countProseLines`: blank lines,
    fenced code, table rows (`|`-led), and HTML-comment-only lines are data,
    not verbosity, and don't count."""
    fenced = fenced_line_flags(lines)
    count = 0
    for index, raw in enumerate(lines):
        if fenced[index]:
            continue
        trimmed = raw.strip()
        if trimmed == "" or trimmed.startswith("|") or _COMMENT_ONLY_RE.match(trimmed):
            continue
        count += 1
    return count


def count_h2_sections(lines: Sequence[str]) -> int:
    """Same measure as w120's own `countH2Sections`: lines starting with
    `"## "`, fenced code excluded — a statblock/shell example containing a
    literal `## ` line inside a fence is not a real section boundary."""
    fenced = fenced_line_flags(lines)
    return sum(1 for index, line in enumerate(lines) if not fenced[index] and _H2_RE.match(line))


def median(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 != 0:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def quantile(values: Sequence[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    base = int(pos)
    rest = pos - base
    if base + 1 < len(ordered):
        return ordered[base] + rest * (ordered[base + 1] - ordered[base])
    return ordered[base]


class OutlierLimit:
    """Result of `outlier_limit` — a neighbour-relative ceiling for one
    page's measure, plus the basis it was computed on."""

    __slots__ = ("basis", "limit", "sample_size", "sibling_median")

    def __init__(
        self, limit: float, basis: str, sibling_median: float | None, sample_size: int
    ) -> None:
        self.limit = limit
        self.basis = basis
        self.sibling_median = sibling_median
        self.sample_size = sample_size


def outlier_limit(
    sibling_values: Sequence[float],
    *,
    headroom_pct: float,
    min_sample: int,
    fallback_max: float | None = None,
    floor: float = 0.0,
) -> OutlierLimit | None:
    """Same neighbour-relative outlier math as `pageLengthNeighbors.mjs`'s
    `resolvePageLengthLimit` (W12) and w120's own inline copy of the same
    shape: below `min_sample` siblings the measure is too thin to trust.
    W12 falls back to a flat ceiling (`fallback_max`); W120 has none and
    stays silent instead — pass `fallback_max=None` for that shape, and a
    caller with too few siblings gets `None` back, meaning "don't judge
    this page at all" rather than a guessed ceiling.
    """
    sample_size = len(sibling_values)
    if sample_size < min_sample:
        if fallback_max is None:
            return None
        return OutlierLimit(float(fallback_max), "fallback", None, sample_size)
    sibling_median = median(sibling_values)
    limit = max(sibling_median * (1 + headroom_pct / 100), quantile(sibling_values, 0.9), floor)
    return OutlierLimit(limit, "neighbours", sibling_median, sample_size)
