"""Structural signals for a two-page continuity conflict.

pagerank: from page_metrics scope='all'; None when not yet computed.
corroboration: count of distinct vault pages (not page_a or page_b) that
wikilink to each conflicting page via the links table.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConflictSignal:
    page: str
    pagerank: float | None
    corroboration: int


def conflict_signals(
    conn: sqlite3.Connection,
    page_a: str,
    page_b: str,
) -> tuple[ConflictSignal, ConflictSignal]:
    """Return structural signals for each side of a continuity conflict.

    pagerank comes from page_metrics (scope='all'); call ensure_pagerank before
    this if fresh values are required.
    corroboration = distinct pages (not page_a or page_b) that wikilink to each page."""

    def _pagerank(page: str) -> float | None:
        row = conn.execute(
            "SELECT pagerank FROM page_metrics WHERE rel_path = ? AND scope = 'all'",
            (page,),
        ).fetchone()
        return row[0] if row else None

    def _corroboration(page: str, exclude: str) -> int:
        row = conn.execute(
            "SELECT COUNT(DISTINCT source) FROM links "
            "WHERE target = ? AND source != ? AND source != ?",
            (page, page, exclude),
        ).fetchone()
        return row[0] if row else 0

    return (
        ConflictSignal(
            page=page_a,
            pagerank=_pagerank(page_a),
            corroboration=_corroboration(page_a, page_b),
        ),
        ConflictSignal(
            page=page_b,
            pagerank=_pagerank(page_b),
            corroboration=_corroboration(page_b, page_a),
        ),
    )
