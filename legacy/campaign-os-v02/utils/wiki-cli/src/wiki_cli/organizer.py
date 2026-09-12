"""Cluster analysis for the vault organizer (ADR-0049)."""

from __future__ import annotations

import sqlite3
from collections import defaultdict
from dataclasses import dataclass

from wiki_cli.config import OrganizerConfig
from wiki_cli.query.pagerank import ensure_pagerank

_DEFAULT_BODY_WEIGHT = 1.0

_EXCLUDED_PREFIXES = (
    "vault/refs/",
    "vault/_templates/",
    "vault/_assets/",
)


@dataclass(frozen=True, slots=True)
class Cluster:
    anchor: str
    members: list[str]
    density: float


@dataclass(frozen=True, slots=True)
class ClusterResult:
    clusters: list[Cluster]
    unassigned: list[str]
    ambiguous: list[tuple[str, list[str]]]


_INCLUDED_PREFIXES = (
    "vault/campaigns/",
    "vault/episodes/",
)


def _in_scope(
    rel_path: str,
    srd_included: bool,
    page_type: str | None = None,
    unique: int | None = None,
    float_types: frozenset[str] = frozenset(),
) -> bool:
    if any(rel_path.startswith(prefix) for prefix in _EXCLUDED_PREFIXES):
        return False
    if rel_path.startswith("vault/srd/"):
        return srd_included
    if not any(rel_path.startswith(prefix) for prefix in _INCLUDED_PREFIXES):
        return False
    if rel_path.startswith("vault/episodes/") and page_type is None:
        return False
    if page_type in float_types:
        return False
    return not (page_type == "item" and unique != 1)


def _load_page_meta(
    conn: sqlite3.Connection,
) -> dict[str, tuple[str | None, int | None]]:
    """Return {rel_path: (type, unique)} for all rows in the pages table.

    Falls back to an empty dict when the pages table does not exist (pre-migration
    DBs, in-memory test fixtures). A missing row for a real path is treated as
    (type=None, unique=None) by callers, which skips float filtering — the safe
    conservative direction (unknown pages are included, not excluded).
    """
    try:
        return {
            row[0]: (row[1], row[2])
            for row in conn.execute(
                'SELECT rel_path, type, "unique" FROM pages'
            ).fetchall()
        }
    except sqlite3.OperationalError:
        return {}


def _build_graph(
    conn: sqlite3.Connection,
    weights: dict[str, float],
    srd_included: bool,
    float_types: frozenset[str] = frozenset(),
) -> tuple[set[str], dict[tuple[str, str], float]]:
    """Build weighted undirected edge set from the links table."""
    nodes: set[str] = set()
    edges: dict[tuple[str, str], float] = defaultdict(float)

    page_meta = _load_page_meta(conn)

    rows = conn.execute(
        "SELECT source, target, link_type FROM links WHERE target IS NOT NULL"
    ).fetchall()

    for source, target, link_type in rows:
        if source == target:
            continue
        src_type, src_unique = page_meta.get(source, (None, None))
        tgt_type, tgt_unique = page_meta.get(target, (None, None))
        if not _in_scope(source, srd_included, src_type, src_unique, float_types):
            continue
        if not _in_scope(target, srd_included, tgt_type, tgt_unique, float_types):
            continue
        nodes.add(source)
        nodes.add(target)
        w = weights.get(link_type, _DEFAULT_BODY_WEIGHT) if link_type else _DEFAULT_BODY_WEIGHT
        edge_key = (min(source, target), max(source, target))
        edges[edge_key] += w

    return nodes, dict(edges)


def _louvain(
    nodes: set[str],
    edges: dict[tuple[str, str], float],
    resolution: float = 1.0,
) -> dict[str, int]:
    """Single-pass Louvain community detection. Returns node-to-community mapping."""
    if not nodes:
        return {}

    node_list = sorted(nodes)
    community: dict[str, int] = {n: i for i, n in enumerate(node_list)}

    adj: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for (a, b), w in edges.items():
        adj[a].append((b, w))
        adj[b].append((a, w))

    total_weight = sum(edges.values())
    if total_weight == 0:
        return community

    def _community_weights(node: str) -> dict[int, float]:
        result: dict[int, float] = defaultdict(float)
        for neighbor, w in adj[node]:
            result[community[neighbor]] += w
        return dict(result)

    def _node_degree(node: str) -> float:
        return sum(w for _, w in adj[node])

    improved = True
    while improved:
        improved = False
        for node in node_list:
            current_comm = community[node]
            ki = _node_degree(node)
            comm_weights = _community_weights(node)

            best_comm = current_comm
            best_delta = 0.0

            comm_totals: dict[int, float] = defaultdict(float)
            for n in node_list:
                comm_totals[community[n]] += _node_degree(n)

            ki_in_current = comm_weights.get(current_comm, 0.0)
            sigma_current = comm_totals[current_comm] - ki

            for candidate_comm, ki_in_candidate in comm_weights.items():
                if candidate_comm == current_comm:
                    continue
                sigma_candidate = comm_totals[candidate_comm]

                delta = resolution * (
                    (ki_in_candidate - ki_in_current)
                    - ki * (sigma_candidate - sigma_current) / (2.0 * total_weight)
                )

                if delta > best_delta:
                    best_delta = delta
                    best_comm = candidate_comm

            if best_comm != current_comm:
                community[node] = best_comm
                improved = True

    cids = sorted(set(community.values()))
    remap = {old: new for new, old in enumerate(cids)}
    return {n: remap[c] for n, c in community.items()}


def _cluster_density(
    members: list[str],
    edges: dict[tuple[str, str], float],
) -> float:
    """Ratio of actual edges to possible edges among ``members``."""
    n = len(members)
    if n < 2:
        return 0.0
    member_set = set(members)
    actual = sum(
        1 for (a, b) in edges if a in member_set and b in member_set
    )
    possible = n * (n - 1) / 2
    return actual / possible


_ANCHOR_TYPE_PRIORITY: dict[str, int] = {
    # 0 — explicit containers: ship/vehicle names the crew cluster, pc page names character files
    "ship": 0,
    "vehicle": 0,
    "pc": 0,
    # 1 — named places and organisations
    "location": 1,
    "faction": 1,
    # 2 — named entities (also the default for unknown types)
    "npc": 2,
    "quest": 2,
    "event": 2,
    "encounter": 2,
    # 3 — character sub-pages
    "pc-abilities": 3,
    "pc-stats": 3,
    "pc-inventory": 3,
    "pc-spells": 3,
    "pc-gallery": 3,
    # 4 — taxonomic / reference material: worst anchors
    "monster": 4,
    "species": 4,
    "culture": 4,
    "lore": 4,
    "item": 4,
    "deity": 4,
    "secret": 4,
    "reference": 4,
}
_DEFAULT_ANCHOR_PRIORITY = 2

# Container types that may be adopted into a cluster they're strongly connected to
# when Louvain leaves them unassigned (e.g. a ship page that links to its crew cluster).
_CONTAINER_TYPES: frozenset[str] = frozenset({"ship", "vehicle", "pc", "location", "faction"})


def _load_page_ranks(conn: sqlite3.Connection) -> dict[str, float]:
    """Return {rel_path: pagerank} from the page_metrics table.

    Falls back to an empty dict when the table does not exist. A missing row
    for a real path scores 0.0 at the call site, producing an alphabetical
    tiebreak — the safe conservative direction.
    """
    try:
        return {
            row[0]: row[1]
            for row in conn.execute(
                "SELECT rel_path, pagerank FROM page_metrics "
                "WHERE scope = 'all' AND pagerank IS NOT NULL"
            ).fetchall()
        }
    except sqlite3.OperationalError:
        return {}


def _resolve_anchor(
    members: list[str],
    page_ranks: dict[str, float],
    page_meta: dict[str, tuple[str | None, int | None]] | None = None,
) -> str:
    """Pick the cluster anchor.

    Lowest `_ANCHOR_TYPE_PRIORITY` tier wins first. Within the best tier,
    highest global PageRank wins. Ties break alphabetically.
    """
    if page_meta is None:
        page_meta = {}

    def _tier(path: str) -> int:
        page_type = page_meta.get(path, (None, None))[0]
        return _ANCHOR_TYPE_PRIORITY.get(page_type or "", _DEFAULT_ANCHOR_PRIORITY)

    best_tier = min(_tier(m) for m in members)
    tier_members = [m for m in members if _tier(m) == best_tier]
    best_pr = max(page_ranks.get(m, 0.0) for m in tier_members)
    return min(m for m in tier_members if page_ranks.get(m, 0.0) == best_pr)


def _slug_from_path(rel_path: str) -> str:
    return rel_path.rsplit("/", 1)[-1].removesuffix(".md")


def analyze(
    conn: sqlite3.Connection,
    cfg: OrganizerConfig,
    weights: dict[str, float],
) -> ClusterResult:
    """Run the full cluster analysis pipeline."""
    ensure_pagerank(conn, weights=weights)
    page_ranks = _load_page_ranks(conn)
    page_meta = _load_page_meta(conn)

    nodes, edges = _build_graph(conn, weights, srd_included=cfg.srd_included, float_types=cfg.float_types)

    if not nodes:
        return ClusterResult(clusters=[], unassigned=[], ambiguous=[])

    community = _louvain(nodes, edges, resolution=cfg.resolution)

    groups: dict[int, list[str]] = defaultdict(list)
    for node, cid in community.items():
        groups[cid].append(node)

    clusters: list[Cluster] = []
    unassigned: list[str] = []
    ambiguous: list[tuple[str, list[str]]] = []

    for _, members in sorted(groups.items()):
        members.sort()
        density = _cluster_density(members, edges)

        if len(members) < cfg.min_cluster_size or density < cfg.min_cluster_density:
            unassigned.extend(members)
            continue

        anchor = _resolve_anchor(members, page_ranks, page_meta)
        clusters.append(Cluster(
            anchor=_slug_from_path(anchor),
            members=members,
            density=density,
        ))

    # Container adoption: unassigned hub pages (ship, vehicle, pc, location, faction)
    # that have ≥2 edges into a single cluster and a better type tier than that
    # cluster's best current member get pulled in as the anchor.
    if unassigned and clusters:
        member_to_cid: dict[str, int] = {
            m: cid for cid, cl in enumerate(clusters) for m in cl.members
        }
        adopted: list[str] = []
        for path in unassigned:
            path_type = page_meta.get(path, (None, None))[0]
            if path_type not in _CONTAINER_TYPES:
                continue
            path_priority = _ANCHOR_TYPE_PRIORITY.get(path_type, _DEFAULT_ANCHOR_PRIORITY)

            edge_counts: dict[int, int] = {}
            for a, b in edges:
                neighbor = b if a == path else (a if b == path else None)
                if neighbor is None:
                    continue
                neighbor_cid = member_to_cid.get(neighbor)
                if neighbor_cid is not None:
                    edge_counts[neighbor_cid] = edge_counts.get(neighbor_cid, 0) + 1

            if not edge_counts:
                continue
            best_cid = max(edge_counts, key=lambda i: edge_counts[i])
            if edge_counts[best_cid] < 2:
                continue

            best_cluster = clusters[best_cid]
            best_member_priority = min(
                _ANCHOR_TYPE_PRIORITY.get(
                    page_meta.get(m, (None, None))[0] or "", _DEFAULT_ANCHOR_PRIORITY
                )
                for m in best_cluster.members
            )
            if path_priority >= best_member_priority:
                continue

            new_members = sorted(best_cluster.members + [path])
            new_anchor = _resolve_anchor(new_members, page_ranks, page_meta)
            clusters[best_cid] = Cluster(
                anchor=_slug_from_path(new_anchor),
                members=new_members,
                density=_cluster_density(new_members, edges),
            )
            member_to_cid[path] = best_cid
            adopted.append(path)

        for path in adopted:
            unassigned.remove(path)

    clusters.sort(key=lambda c: (-len(c.members), c.anchor))
    unassigned.sort()

    return ClusterResult(clusters=clusters, unassigned=unassigned, ambiguous=ambiguous)
