"""Tests for the vault organiser cluster analysis."""

from __future__ import annotations

import sqlite3

import pytest

from wiki_cli.config import DEFAULT_ORGANIZER_FLOAT_TYPES, OrganizerConfig
from wiki_cli.organizer import (
    ClusterResult,
    _build_graph,
    _cluster_density,
    _in_scope,
    _louvain,
    _resolve_anchor,
    _slug_from_path,
    analyze,
)


@pytest.fixture
def conn() -> sqlite3.Connection:
    c = sqlite3.connect(":memory:")
    c.execute(
        "CREATE TABLE links ("
        "  source TEXT, target TEXT, raw_target TEXT, section TEXT,"
        "  count INTEGER, link_type TEXT,"
        "  PRIMARY KEY (source, raw_target, section))"
    )
    c.execute(
        "CREATE TABLE pages ("
        '  rel_path TEXT PRIMARY KEY, type TEXT, "unique" INTEGER DEFAULT NULL)'
    )
    c.execute(
        "CREATE TABLE page_metrics ("
        "  rel_path TEXT NOT NULL, scope TEXT NOT NULL DEFAULT 'all',"
        "  links_in INTEGER NOT NULL DEFAULT 0, links_out INTEGER NOT NULL DEFAULT 0,"
        "  pagerank REAL, dirty INTEGER NOT NULL DEFAULT 1,"
        "  PRIMARY KEY (rel_path, scope))"
    )
    return c


def _insert_link(
    conn: sqlite3.Connection,
    source: str,
    target: str,
    link_type: str | None = None,
) -> None:
    conn.execute(
        "INSERT INTO links (source, target, raw_target, section, count, link_type) "
        "VALUES (?, ?, ?, '', 1, ?)",
        (source, target, target, link_type),
    )


def _insert_page_rank(
    conn: sqlite3.Connection,
    rel_path: str,
    pagerank: float,
    scope: str = "all",
) -> None:
    conn.execute(
        "INSERT INTO page_metrics (rel_path, scope, pagerank, dirty) VALUES (?, ?, ?, 0)",
        (rel_path, scope, pagerank),
    )
    conn.commit()


def _insert_page(
    conn: sqlite3.Connection,
    rel_path: str,
    page_type: str | None = None,
    unique: int | None = None,
) -> None:
    conn.execute(
        'INSERT INTO pages (rel_path, type, "unique") VALUES (?, ?, ?)',
        (rel_path, page_type, unique),
    )


# -- scope filtering --


class TestInScope:
    def test_campaigns_included(self) -> None:
        assert _in_scope("vault/campaigns/shattered-sea/npcs/foo.md", srd_included=False)

    def test_episodes_typed_unique_item_included(self) -> None:
        assert _in_scope(
            "vault/episodes/001/special-sword.md",
            srd_included=False,
            page_type="item",
            unique=1,
            float_types=DEFAULT_ORGANIZER_FLOAT_TYPES,
        )

    def test_refs_excluded(self) -> None:
        assert not _in_scope("vault/refs/craft/foo.md", srd_included=False)

    def test_templates_excluded(self) -> None:
        assert not _in_scope("vault/_templates/npc.md", srd_included=False)

    def test_assets_excluded(self) -> None:
        assert not _in_scope("vault/_assets/maps/foo.png", srd_included=False)

    def test_srd_excluded_by_default(self) -> None:
        assert not _in_scope("vault/srd/monsters/goblin.md", srd_included=False)

    def test_srd_included_when_flag_set(self) -> None:
        assert _in_scope("vault/srd/monsters/goblin.md", srd_included=True)

    def test_other_vault_dirs_excluded(self) -> None:
        assert not _in_scope("vault/ideas/foo.md", srd_included=False)

    def test_beat_excluded(self) -> None:
        assert not _in_scope(
            "vault/episodes/001/beat-01.md",
            srd_included=False,
            page_type="beat",
            float_types=DEFAULT_ORGANIZER_FLOAT_TYPES,
        )

    def test_item_without_unique_excluded(self) -> None:
        assert not _in_scope(
            "vault/campaigns/shattered-sea/items/rare/sword.md",
            srd_included=False,
            page_type="item",
            unique=None,
            float_types=DEFAULT_ORGANIZER_FLOAT_TYPES,
        )

    def test_item_with_unique_included(self) -> None:
        assert _in_scope(
            "vault/campaigns/shattered-sea/items/rare/sword.md",
            srd_included=False,
            page_type="item",
            unique=1,
            float_types=DEFAULT_ORGANIZER_FLOAT_TYPES,
        )

    def test_untyped_episode_page_excluded(self) -> None:
        assert not _in_scope(
            "vault/episodes/007/transcript.md",
            srd_included=False,
            page_type=None,
            float_types=DEFAULT_ORGANIZER_FLOAT_TYPES,
        )

    def test_untyped_campaigns_page_included(self) -> None:
        assert _in_scope(
            "vault/campaigns/shattered-sea/npcs/someone.md",
            srd_included=False,
            page_type=None,
            float_types=DEFAULT_ORGANIZER_FLOAT_TYPES,
        )


# -- graph building --


class TestBuildGraph:
    def test_basic_edges(self, conn: sqlite3.Connection) -> None:
        _insert_link(conn, "vault/campaigns/a.md", "vault/campaigns/b.md")
        _insert_link(conn, "vault/campaigns/b.md", "vault/campaigns/c.md")
        nodes, edges = _build_graph(conn, {}, srd_included=False)
        assert nodes == {"vault/campaigns/a.md", "vault/campaigns/b.md", "vault/campaigns/c.md"}
        assert len(edges) == 2

    def test_typed_edge_weight(self, conn: sqlite3.Connection) -> None:
        _insert_link(conn, "vault/campaigns/a.md", "vault/campaigns/b.md", "CONTAINS")
        _, edges = _build_graph(conn, {"CONTAINS": 3.0}, srd_included=False)
        key = ("vault/campaigns/a.md", "vault/campaigns/b.md")
        assert edges[key] == 3.0

    def test_excludes_refs(self, conn: sqlite3.Connection) -> None:
        _insert_link(conn, "vault/campaigns/a.md", "vault/refs/craft/foo.md")
        nodes, edges = _build_graph(conn, {}, srd_included=False)
        assert len(nodes) == 0
        assert len(edges) == 0

    def test_undirected_merge(self, conn: sqlite3.Connection) -> None:
        _insert_link(conn, "vault/campaigns/b.md", "vault/campaigns/a.md")
        _insert_link(conn, "vault/campaigns/a.md", "vault/campaigns/b.md")
        _, edges = _build_graph(conn, {}, srd_included=False)
        assert len(edges) == 1
        assert edges[("vault/campaigns/a.md", "vault/campaigns/b.md")] == 2.0


# -- Louvain --


class TestLouvain:
    def test_empty_graph(self) -> None:
        assert _louvain(set(), {}) == {}

    def test_single_node(self) -> None:
        result = _louvain({"a"}, {})
        assert result == {"a": 0}

    def test_two_disconnected_components(self) -> None:
        nodes = {"a", "b", "c", "d"}
        edges = {("a", "b"): 5.0, ("c", "d"): 5.0}
        result = _louvain(nodes, edges)
        assert result["a"] == result["b"]
        assert result["c"] == result["d"]
        assert result["a"] != result["c"]

    def test_dense_clique(self) -> None:
        nodes = {"a", "b", "c"}
        edges = {("a", "b"): 1.0, ("a", "c"): 1.0, ("b", "c"): 1.0}
        result = _louvain(nodes, edges)
        assert result["a"] == result["b"] == result["c"]


# -- cluster density --


class TestClusterDensity:
    def test_complete_graph(self) -> None:
        members = ["a", "b", "c"]
        edges = {("a", "b"): 1.0, ("a", "c"): 1.0, ("b", "c"): 1.0}
        assert _cluster_density(members, edges) == pytest.approx(1.0)

    def test_single_node(self) -> None:
        assert _cluster_density(["a"], {}) == 0.0

    def test_sparse_graph(self) -> None:
        members = ["a", "b", "c", "d"]
        edges = {("a", "b"): 1.0}
        assert _cluster_density(members, edges) == pytest.approx(1 / 6)


# -- anchor resolution --


class TestResolveAnchor:
    def test_highest_pagerank_wins(self) -> None:
        members = ["a", "b", "c"]
        page_ranks = {"a": 0.1, "b": 0.5, "c": 0.2}
        assert _resolve_anchor(members, page_ranks) == "b"

    def test_tie_breaks_alphabetically(self) -> None:
        members = ["c", "a", "b"]
        assert _resolve_anchor(members, {}) == "a"

    def test_missing_score_treated_as_zero(self) -> None:
        members = ["vault/campaigns/z.md", "vault/campaigns/a.md"]
        page_ranks = {"vault/campaigns/z.md": 0.0}
        assert _resolve_anchor(members, page_ranks) == "vault/campaigns/a.md"

    def test_type_priority_beats_pagerank(self) -> None:
        """location (tier 1) beats monster (tier 4) even when monster has higher PageRank."""
        loc = "vault/campaigns/shattered-sea/locations/midchain-west.md"
        mon = "vault/campaigns/shattered-sea/monsters/reef-shark.md"
        meta: dict[str, tuple[str | None, int | None]] = {
            loc: ("location", None), mon: ("monster", None)
        }
        assert _resolve_anchor([loc, mon], {mon: 0.9, loc: 0.1}, meta) == loc

    def test_pc_beats_pc_spells(self) -> None:
        """pc (tier 0) beats pc-spells (tier 3) regardless of PageRank."""
        sheet = "vault/campaigns/shattered-sea/pcs/character-sheets/perrin-sheet.md"
        spells = "vault/campaigns/shattered-sea/pcs/spells/perrin-spells.md"
        meta: dict[str, tuple[str | None, int | None]] = {
            sheet: ("pc", None), spells: ("pc-spells", None)
        }
        assert _resolve_anchor([sheet, spells], {spells: 0.9, sheet: 0.1}, meta) == sheet

    def test_npc_beats_species(self) -> None:
        """npc (tier 2) beats species (tier 4) regardless of PageRank."""
        npc = "vault/campaigns/shattered-sea/npcs/otar-the-foul.md"
        spc = "vault/campaigns/shattered-sea/species/human.md"
        meta: dict[str, tuple[str | None, int | None]] = {
            npc: ("npc", None), spc: ("species", None)
        }
        assert _resolve_anchor([npc, spc], {spc: 0.9, npc: 0.1}, meta) == npc


# -- slug extraction --


class TestSlugFromPath:
    def test_basic(self) -> None:
        assert _slug_from_path("vault/campaigns/npcs/foo.md") == "foo"

    def test_nested(self) -> None:
        assert _slug_from_path("vault/episodes/001/run-guide.md") == "run-guide"


# -- full pipeline --


class TestAnalyze:
    def _default_cfg(self, **overrides: object) -> OrganizerConfig:
        defaults: dict[str, object] = {
            "min_cluster_size": 3,
            "min_cluster_density": 0.3,
            "resolution": 1.0,
            "srd_included": False,
        }
        defaults.update(overrides)
        return OrganizerConfig(**defaults)  # type: ignore[arg-type]

    def test_empty_db(self, conn: sqlite3.Connection) -> None:
        result = analyze(conn, self._default_cfg(), {})
        assert result == ClusterResult(clusters=[], unassigned=[], ambiguous=[])

    def test_dense_cluster_detected(self, conn: sqlite3.Connection) -> None:
        # Star graph: hub links to 3 spokes, hub has highest centrality.
        hub = "vault/campaigns/hub.md"
        spokes = [f"vault/campaigns/s{i}.md" for i in range(3)]
        for s in spokes:
            _insert_link(conn, hub, s)

        result = analyze(conn, self._default_cfg(min_cluster_size=2, min_cluster_density=0.3), {})
        assert len(result.clusters) >= 1
        all_members = [m for c in result.clusters for m in c.members]
        assert hub in all_members

    def test_below_size_threshold_unassigned(self, conn: sqlite3.Connection) -> None:
        _insert_link(conn, "vault/campaigns/a.md", "vault/campaigns/b.md")
        result = analyze(conn, self._default_cfg(min_cluster_size=5), {})
        assert len(result.clusters) == 0
        assert len(result.unassigned) == 2

    def test_two_separate_clusters(self, conn: sqlite3.Connection) -> None:
        for prefix in ("x", "y"):
            hub = f"vault/campaigns/{prefix}-hub.md"
            spokes = [f"vault/campaigns/{prefix}{i}.md" for i in range(3)]
            for s in spokes:
                _insert_link(conn, hub, s)
            _insert_link(conn, spokes[0], spokes[1])

        result = analyze(conn, self._default_cfg(min_cluster_size=3, min_cluster_density=0.3), {})
        assert len(result.clusters) == 2
        cluster_sizes = sorted(len(c.members) for c in result.clusters)
        assert cluster_sizes == [4, 4]

    def test_scope_exclusion(self, conn: sqlite3.Connection) -> None:
        _insert_link(conn, "vault/refs/craft/a.md", "vault/refs/craft/b.md")
        _insert_link(conn, "vault/refs/craft/b.md", "vault/refs/craft/c.md")
        _insert_link(conn, "vault/refs/craft/c.md", "vault/refs/craft/a.md")
        result = analyze(conn, self._default_cfg(min_cluster_size=2), {})
        assert len(result.clusters) == 0
        assert len(result.unassigned) == 0

    def test_srd_included_flag(self, conn: sqlite3.Connection) -> None:
        hub = "vault/srd/monsters/hub.md"
        spokes = [f"vault/srd/monsters/m{i}.md" for i in range(3)]
        for s in spokes:
            _insert_link(conn, hub, s)

        result_excluded = analyze(
            conn, self._default_cfg(srd_included=False, min_cluster_size=2), {}
        )
        assert len(result_excluded.clusters) == 0
        assert len(result_excluded.unassigned) == 0

        result_included = analyze(
            conn, self._default_cfg(srd_included=True, min_cluster_size=2), {}
        )
        assert len(result_included.clusters) >= 1
        all_members = [m for c in result_included.clusters for m in c.members]
        assert hub in all_members

    def test_typed_edge_weights(self, conn: sqlite3.Connection) -> None:
        hub = "vault/campaigns/t-hub.md"
        spokes = [f"vault/campaigns/t{i}.md" for i in range(3)]
        for s in spokes:
            _insert_link(conn, hub, s, "CONTAINS")

        weights = {"CONTAINS": 3.0}
        result = analyze(
            conn, self._default_cfg(min_cluster_size=2, min_cluster_density=0.3), weights
        )
        assert len(result.clusters) >= 1
        all_members = [m for c in result.clusters for m in c.members]
        assert hub in all_members

    def test_float_pages_absent_from_clusters(self, conn: sqlite3.Connection) -> None:
        """Float pages do not appear in clusters even when densely linked to non-float pages."""
        hub = "vault/campaigns/shattered-sea/npcs/hub.md"
        spoke = "vault/campaigns/shattered-sea/npcs/spoke.md"
        beat = "vault/episodes/001/beat-01.md"
        item_non_unique = "vault/campaigns/shattered-sea/items/rare/sword.md"

        _insert_page(conn, hub, page_type="npc")
        _insert_page(conn, spoke, page_type="npc")
        _insert_page(conn, beat, page_type="beat")
        _insert_page(conn, item_non_unique, page_type="item", unique=None)

        _insert_link(conn, hub, beat)
        _insert_link(conn, hub, item_non_unique)
        _insert_link(conn, hub, spoke)
        _insert_link(conn, beat, spoke)
        _insert_link(conn, item_non_unique, spoke)

        cfg = self._default_cfg(
            min_cluster_size=2,
            min_cluster_density=0.1,
            float_types=DEFAULT_ORGANIZER_FLOAT_TYPES,
        )
        result = analyze(conn, cfg, {})

        all_members = [m for c in result.clusters for m in c.members]
        assert beat not in all_members
        assert item_non_unique not in all_members

    def test_unique_item_included_in_clusters(self, conn: sqlite3.Connection) -> None:
        """A type:item page with unique=1 participates in graph analysis normally."""
        hub = "vault/campaigns/shattered-sea/npcs/hub.md"
        unique_item = "vault/campaigns/shattered-sea/items/rare/crown.md"
        spokes = [f"vault/campaigns/shattered-sea/npcs/spoke{i}.md" for i in range(3)]

        _insert_page(conn, hub, page_type="npc")
        _insert_page(conn, unique_item, page_type="item", unique=1)
        for s in spokes:
            _insert_page(conn, s, page_type="npc")

        _insert_link(conn, hub, unique_item)
        for s in spokes:
            _insert_link(conn, hub, s)

        cfg = self._default_cfg(
            min_cluster_size=2,
            min_cluster_density=0.1,
            float_types=DEFAULT_ORGANIZER_FLOAT_TYPES,
        )
        result = analyze(conn, cfg, {})

        all_members = [m for c in result.clusters for m in c.members]
        assert unique_item in all_members

    def test_pagerank_elects_anchor(self, conn: sqlite3.Connection) -> None:
        """PageRank score, not intra-cluster centrality, decides the anchor."""
        hub = "vault/campaigns/shattered-sea/locations/loc.md"
        npc = "vault/campaigns/shattered-sea/npcs/recurring-npc.md"
        spokes = [f"vault/campaigns/shattered-sea/npcs/s{i}.md" for i in range(2)]

        # Hub is the structural star (most intra-cluster edges) but npc has highest PageRank.
        # Five edges keep all 4 nodes in one Louvain community (density 5/6 ≈ 0.83).
        for s in spokes:
            _insert_link(conn, hub, s)
        _insert_link(conn, hub, npc)
        _insert_link(conn, npc, spokes[0])
        _insert_link(conn, npc, spokes[1])  # extra edge: one cluster, not two

        _insert_page_rank(conn, npc, 0.9)
        _insert_page_rank(conn, hub, 0.1)

        cfg = self._default_cfg(min_cluster_size=2, min_cluster_density=0.1)
        result = analyze(conn, cfg, {})

        # One cluster: without PageRank, 'loc' wins alphabetically (locations/ < npcs/).
        # With PageRank, npc's score of 0.9 overrides the tiebreak → recurring-npc wins.
        assert len(result.clusters) == 1
        assert result.clusters[0].anchor == "recurring-npc"
