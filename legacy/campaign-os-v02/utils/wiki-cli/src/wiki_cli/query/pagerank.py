"""Lazy dirty-flagged PageRank over the `links` table.

`compute_pagerank` is a pure power-iteration implementation; `ensure_pagerank`
is the DB-facing wrapper that only recomputes when `page_metrics.dirty = 1`
for the given scope, then writes scores back and clears the flag.
"""

from __future__ import annotations

import sqlite3

_CONVERGENCE_THRESHOLD = 1e-9


def compute_pagerank(
    edges: dict[str, list[tuple[str, str | None]]],
    nodes: set[str],
    damping: float = 0.85,
    iterations: int = 50,
    weights: dict[str, float] | None = None,
) -> dict[str, float]:
    """Power-iteration PageRank over `nodes` using `edges` as the outbound
    adjacency list. Each edge is a ``(target, link_type)`` pair.

    When `weights` is provided, each edge's contribution is scaled by
    ``weights.get(link_type, 1.0)`` (``None`` link_type maps to 1.0 via the
    default). A node absent from `edges` (or mapped to an empty list) is
    dangling: its mass is redistributed uniformly. Runs `iterations` rounds
    or until the max per-node delta drops below ``1e-9``. Returns a dict
    summing to ~1.0."""
    node_count = len(nodes)
    if node_count == 0:
        return {}

    ranks = {node: 1.0 / node_count for node in nodes}
    base = (1.0 - damping) / node_count

    for _ in range(iterations):
        inbound: dict[str, float] = dict.fromkeys(nodes, 0.0)
        dangling_mass = 0.0

        for source in nodes:
            raw_targets = [(t, lt) for t, lt in edges.get(source, []) if t in nodes]
            if not raw_targets:
                dangling_mass += ranks[source]
                continue

            if weights is not None:
                edge_weights = [weights.get(lt or "", 1.0) for _, lt in raw_targets]
                total_weight = sum(edge_weights) or 1.0
                for (target, _), w in zip(raw_targets, edge_weights):
                    inbound[target] += ranks[source] * w / total_weight
            else:
                share = ranks[source] / len(raw_targets)
                for target, _ in raw_targets:
                    inbound[target] += share

        dangling_share = dangling_mass / node_count
        new_ranks = {
            node: base + damping * (inbound[node] + dangling_share) for node in nodes
        }

        max_delta = max(abs(new_ranks[node] - ranks[node]) for node in nodes)
        ranks = new_ranks
        if max_delta < _CONVERGENCE_THRESHOLD:
            break

    return ranks


def ensure_pagerank(
    conn: sqlite3.Connection,
    scope: str = "all",
    weights: dict[str, float] | None = None,
) -> None:
    """No-op unless some `page_metrics` row in `scope` has `dirty = 1`.
    Otherwise recomputes PageRank over every resolved edge in `links`
    (``target IS NOT NULL``) and writes ``pagerank``/``dirty = 0`` for every
    `page_metrics` row in `scope`, in one transaction.

    `weights` maps each ``link_type`` to a multiplier; ``None`` link_type edges
    always use 1.0. When `weights` is ``None``, all edges are treated equally."""
    dirty_row = conn.execute(
        "SELECT 1 FROM page_metrics WHERE scope = ? AND dirty = 1 LIMIT 1",
        (scope,),
    ).fetchone()
    if dirty_row is None:
        return

    nodes = {
        row[0]
        for row in conn.execute(
            "SELECT rel_path FROM page_metrics WHERE scope = ?", (scope,)
        ).fetchall()
    }

    edges: dict[str, list[tuple[str, str | None]]] = {}
    for source, target, link_type in conn.execute(
        "SELECT source, target, link_type FROM links WHERE target IS NOT NULL"
    ).fetchall():
        nodes.add(source)
        nodes.add(target)
        edges.setdefault(source, []).append((target, link_type))

    ranks = compute_pagerank(edges, nodes, weights=weights)

    with conn:
        conn.executemany(
            "UPDATE page_metrics SET pagerank = ?, dirty = 0 "
            "WHERE rel_path = ? AND scope = ?",
            [(ranks.get(rel_path, 0.0), rel_path, scope) for rel_path in nodes],
        )
