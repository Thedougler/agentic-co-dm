"""wiki_cli.query.pagerank — rank order on synthetic graphs, never exact floats."""
from __future__ import annotations

import sqlite3

from wiki_cli.query.pagerank import compute_pagerank, ensure_pagerank


def test_hub_outranks_leaves() -> None:
    nodes = {"hub", "a", "b", "c"}
    edges: dict[str, list[tuple[str, str | None]]] = {
        "a": [("hub", None)],
        "b": [("hub", None)],
        "c": [("hub", None)],
        "hub": [],
    }
    ranks = compute_pagerank(edges, nodes)
    assert ranks["hub"] > ranks["a"]
    assert abs(sum(ranks.values()) - 1.0) < 1e-6


def _mem_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE links "
        "(source TEXT, target TEXT, raw_target TEXT, section TEXT, count INTEGER, link_type TEXT)"
    )
    conn.execute(
        "CREATE TABLE page_metrics (rel_path TEXT, scope TEXT, links_in INTEGER, "
        "links_out INTEGER, pagerank REAL, dirty INTEGER, PRIMARY KEY (rel_path, scope))"
    )
    return conn


def test_ensure_pagerank_clears_dirty_and_is_lazy() -> None:
    conn = _mem_db()
    conn.execute("INSERT INTO links VALUES ('a.md', 'hub.md', 'hub', '', 1, NULL)")
    for rel in ("a.md", "hub.md"):
        conn.execute("INSERT INTO page_metrics VALUES (?, 'all', 0, 0, NULL, 1)", (rel,))
    ensure_pagerank(conn)
    rows = dict(conn.execute("SELECT rel_path, dirty FROM page_metrics").fetchall())
    assert rows == {"a.md": 0, "hub.md": 0}
    hub = conn.execute("SELECT pagerank FROM page_metrics WHERE rel_path='hub.md'").fetchone()[0]
    assert hub is not None
    conn.execute("UPDATE page_metrics SET pagerank = 99.0")  # sentinel: recompute would overwrite
    ensure_pagerank(conn)  # nothing dirty -> no-op
    assert conn.execute("SELECT pagerank FROM page_metrics WHERE rel_path='hub.md'").fetchone()[0] == 99.0


def test_weighted_typed_edges_boost_typed_inlink_target() -> None:
    """A page with typed-edge inlinks outranks one with only body wikilinks."""
    nodes = {"typed-target", "body-target", "src1", "src2", "src3"}
    weights = {"CONTAINS": 3.0, "MEMBER_OF": 3.0}
    edges: dict[str, list[tuple[str, str | None]]] = {
        "src1": [("typed-target", "CONTAINS")],
        "src2": [("typed-target", "MEMBER_OF")],
        "src3": [("body-target", None)],
        "typed-target": [],
        "body-target": [],
    }
    ranks = compute_pagerank(edges, nodes, weights=weights)
    assert ranks["typed-target"] > ranks["body-target"]
    assert abs(sum(ranks.values()) - 1.0) < 1e-6


def test_all_null_link_type_equals_unweighted() -> None:
    """When all link_type values are NULL, weighted rank equals unweighted rank."""
    nodes = {"hub", "a", "b"}
    edges: dict[str, list[tuple[str, str | None]]] = {
        "a": [("hub", None)],
        "b": [("hub", None)],
        "hub": [],
    }
    weights = {"CONTAINS": 3.0, "MEMBER_OF": 3.0}
    ranked_weighted = compute_pagerank(edges, nodes, weights=weights)
    ranked_unweighted = compute_pagerank(edges, nodes, weights=None)
    for node in nodes:
        assert abs(ranked_weighted[node] - ranked_unweighted[node]) < 1e-9
