"""wiki_cli.query.conflict — conflict_signals with fixture canon pages."""

from __future__ import annotations

import sqlite3

from wiki_cli.query.conflict import ConflictSignal, conflict_signals


def _mem_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE links "
        "(source TEXT, target TEXT, raw_target TEXT, section TEXT, count INTEGER, link_type TEXT)"
    )
    conn.execute(
        "CREATE TABLE page_metrics "
        "(rel_path TEXT, scope TEXT, links_in INTEGER, links_out INTEGER, "
        "pagerank REAL, dirty INTEGER, PRIMARY KEY (rel_path, scope))"
    )
    return conn


def _seed(
    conn: sqlite3.Connection,
    *,
    page_a: str,
    page_b: str,
    rank_a: float,
    rank_b: float,
    corroborators_for_a: list[str],
    corroborators_for_b: list[str],
) -> None:
    for page, rank in ((page_a, rank_a), (page_b, rank_b)):
        conn.execute(
            "INSERT INTO page_metrics VALUES (?, 'all', 0, 0, ?, 0)",
            (page, rank),
        )
    for src in corroborators_for_a:
        conn.execute("INSERT INTO links VALUES (?, ?, '', '', 1, NULL)", (src, page_a))
    for src in corroborators_for_b:
        conn.execute("INSERT INTO links VALUES (?, ?, '', '', 1, NULL)", (src, page_b))


# ---------------------------------------------------------------------------
# Fixtures: two conflicting canon pages
# ---------------------------------------------------------------------------

_PAGE_A = "vault/npcs/rook.md"
_PAGE_B = "vault/npcs/sable.md"
_RANK_A = 0.042
_RANK_B = 0.017


def test_conflict_signals_returns_correct_rank_and_corroboration() -> None:
    """fixture vault with two conflicting canon pages → correct rank and corroboration."""
    conn = _mem_db()
    _seed(
        conn,
        page_a=_PAGE_A,
        page_b=_PAGE_B,
        rank_a=_RANK_A,
        rank_b=_RANK_B,
        corroborators_for_a=["vault/locations/a.md", "vault/factions/b.md", "vault/episodes/001/recap.md"],
        corroborators_for_b=["vault/npcs/other.md"],
    )
    sig_a, sig_b = conflict_signals(conn, _PAGE_A, _PAGE_B)

    assert sig_a == ConflictSignal(page=_PAGE_A, pagerank=_RANK_A, corroboration=3)
    assert sig_b == ConflictSignal(page=_PAGE_B, pagerank=_RANK_B, corroboration=1)


def test_conflict_signals_excludes_the_two_conflicting_pages() -> None:
    """Page A linking to page B (or B to A) must not count as corroboration."""
    conn = _mem_db()
    conn.execute(
        "INSERT INTO page_metrics VALUES (?, 'all', 0, 0, 0.05, 0)", (_PAGE_A,)
    )
    conn.execute(
        "INSERT INTO page_metrics VALUES (?, 'all', 0, 0, 0.03, 0)", (_PAGE_B,)
    )
    # Each page links to the other — these must be excluded from corroboration counts.
    conn.execute("INSERT INTO links VALUES (?, ?, '', '', 1, NULL)", (_PAGE_A, _PAGE_B))
    conn.execute("INSERT INTO links VALUES (?, ?, '', '', 1, NULL)", (_PAGE_B, _PAGE_A))

    sig_a, sig_b = conflict_signals(conn, _PAGE_A, _PAGE_B)

    assert sig_a.corroboration == 0
    assert sig_b.corroboration == 0


def test_conflict_signals_null_pagerank_when_not_computed() -> None:
    """pagerank is None when page_metrics row is absent."""
    conn = _mem_db()
    # No rows in page_metrics; corroboration still works via links table.
    sig_a, sig_b = conflict_signals(conn, _PAGE_A, _PAGE_B)

    assert sig_a.pagerank is None
    assert sig_b.pagerank is None
    assert sig_a.corroboration == 0
    assert sig_b.corroboration == 0


def test_conflict_signals_multiple_links_from_same_source_count_once() -> None:
    """A corroborator with multiple wikilinks to a page counts only once."""
    conn = _mem_db()
    _seed(
        conn,
        page_a=_PAGE_A,
        page_b=_PAGE_B,
        rank_a=0.01,
        rank_b=0.01,
        corroborators_for_a=[],
        corroborators_for_b=[],
    )
    # Two links from the same source to PAGE_A.
    conn.execute("INSERT INTO links VALUES ('vault/npcs/other.md', ?, '', 'intro', 1, NULL)", (_PAGE_A,))
    conn.execute("INSERT INTO links VALUES ('vault/npcs/other.md', ?, '', 'body', 1, NULL)", (_PAGE_A,))

    sig_a, _ = conflict_signals(conn, _PAGE_A, _PAGE_B)
    assert sig_a.corroboration == 1
