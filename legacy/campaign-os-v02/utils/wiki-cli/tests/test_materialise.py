"""Tests for the vault organiser materialisation phase."""

from __future__ import annotations

from pathlib import Path

from wiki_cli.materialise import MoveOp, _scrub_path_wikilinks, apply_moves, compute_moves
from wiki_cli.organizer import Cluster, ClusterResult


def _result(*clusters: Cluster) -> ClusterResult:
    return ClusterResult(clusters=list(clusters), unassigned=[], ambiguous=[])


def _cluster(anchor_path: str, *member_paths: str) -> Cluster:
    slug = anchor_path.rsplit("/", 1)[-1].removesuffix(".md")
    all_members = sorted({anchor_path, *member_paths})
    return Cluster(anchor=slug, members=all_members, density=1.0)


# -- compute_moves --


class TestComputeMoves:
    def test_anchor_does_not_move(self) -> None:
        anchor = "vault/campaigns/locations/sparhold.md"
        result = _result(_cluster(anchor))
        assert compute_moves(result) == []

    def test_member_moves_to_anchor_subfolder(self) -> None:
        anchor = "vault/campaigns/locations/sparhold.md"
        member = "vault/campaigns/npcs/foo.md"
        moves = compute_moves(_result(_cluster(anchor, member)))
        assert moves == [MoveOp(src=member, dst="vault/campaigns/locations/sparhold/foo.md")]

    def test_already_in_place_is_noop(self) -> None:
        anchor = "vault/campaigns/locations/sparhold.md"
        member = "vault/campaigns/locations/sparhold/foo.md"
        moves = compute_moves(_result(_cluster(anchor, member)))
        assert moves == []

    def test_multiple_members(self) -> None:
        anchor = "vault/campaigns/loc/town.md"
        members = [
            "vault/campaigns/npcs/npc-a.md",
            "vault/campaigns/npcs/npc-b.md",
        ]
        moves = compute_moves(_result(_cluster(anchor, *members)))
        dsts = {op.dst for op in moves}
        assert dsts == {
            "vault/campaigns/loc/town/npc-a.md",
            "vault/campaigns/loc/town/npc-b.md",
        }

    def test_scope_filters_out_of_scope_clusters(self) -> None:
        anchor_in = "vault/campaigns/shattered-sea/locations/town.md"
        anchor_out = "vault/campaigns/other/locations/city.md"
        member_in = "vault/campaigns/shattered-sea/npcs/npc.md"
        member_out = "vault/campaigns/other/npcs/other-npc.md"
        result = _result(
            _cluster(anchor_in, member_in),
            _cluster(anchor_out, member_out),
        )
        moves = compute_moves(result, scope="vault/campaigns/shattered-sea/")
        assert all(op.src == member_in for op in moves)
        assert len(moves) == 1

    def test_scope_includes_matching_cluster(self) -> None:
        anchor = "vault/campaigns/shattered-sea/locations/town.md"
        member = "vault/campaigns/shattered-sea/npcs/npc.md"
        moves = compute_moves(
            _result(_cluster(anchor, member)),
            scope="vault/campaigns/shattered-sea/",
        )
        assert len(moves) == 1

    def test_anchor_slug_missing_from_members_skips_cluster(self) -> None:
        # Cluster with anchor slug that doesn't match any member path — defensive.
        cluster = Cluster(anchor="ghost", members=["vault/campaigns/a.md"], density=1.0)
        moves = compute_moves(_result(cluster))
        assert moves == []


# -- compute_moves: subordination table --


class TestSubordinationTable:
    """type_map enforcement: eligible members move, ineligible members are skipped."""

    def test_location_under_npc_blocked(self) -> None:
        anchor = "vault/campaigns/npcs/fio.md"
        member = "vault/campaigns/locations/il-preludio.md"
        type_map = {anchor: "npc", member: "location"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert moves == []

    def test_npc_under_npc_allowed(self) -> None:
        anchor = "vault/campaigns/npcs/fio.md"
        member = "vault/campaigns/npcs/serena.md"
        type_map = {anchor: "npc", member: "npc"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert len(moves) == 1

    def test_faction_under_npc_blocked(self) -> None:
        anchor = "vault/campaigns/npcs/fio.md"
        member = "vault/campaigns/factions/guild.md"
        type_map = {anchor: "npc", member: "faction"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert moves == []

    def test_faction_under_location_allowed(self) -> None:
        anchor = "vault/campaigns/locations/sparhold.md"
        member = "vault/campaigns/factions/guild.md"
        type_map = {anchor: "location", member: "faction"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert len(moves) == 1

    def test_location_under_location_allowed(self) -> None:
        anchor = "vault/campaigns/locations/sparhold.md"
        member = "vault/campaigns/locations/market.md"
        type_map = {anchor: "location", member: "location"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert len(moves) == 1

    def test_location_under_faction_blocked(self) -> None:
        anchor = "vault/campaigns/factions/guild.md"
        member = "vault/campaigns/locations/market.md"
        type_map = {anchor: "faction", member: "location"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert moves == []

    def test_faction_under_faction_allowed(self) -> None:
        anchor = "vault/campaigns/factions/guild.md"
        member = "vault/campaigns/factions/cell.md"
        type_map = {anchor: "faction", member: "faction"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert len(moves) == 1

    def test_location_under_event_blocked(self) -> None:
        anchor = "vault/campaigns/events/festival.md"
        member = "vault/campaigns/locations/square.md"
        type_map = {anchor: "event", member: "location"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert moves == []

    def test_faction_under_event_blocked(self) -> None:
        anchor = "vault/campaigns/events/festival.md"
        member = "vault/campaigns/factions/guild.md"
        type_map = {anchor: "event", member: "faction"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert moves == []

    def test_item_under_npc_allowed(self) -> None:
        anchor = "vault/campaigns/npcs/fio.md"
        member = "vault/campaigns/items/ring.md"
        type_map = {anchor: "npc", member: "item"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert len(moves) == 1

    def test_monster_under_npc_allowed(self) -> None:
        anchor = "vault/campaigns/npcs/fio.md"
        member = "vault/campaigns/monsters/bear.md"
        type_map = {anchor: "npc", member: "monster"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert len(moves) == 1

    def test_encounter_under_location_allowed(self) -> None:
        anchor = "vault/campaigns/locations/sparhold.md"
        member = "vault/campaigns/encounters/ambush.md"
        type_map = {anchor: "location", member: "encounter"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert len(moves) == 1

    def test_quest_under_npc_allowed(self) -> None:
        anchor = "vault/campaigns/npcs/fio.md"
        member = "vault/campaigns/quests/delivery.md"
        type_map = {anchor: "npc", member: "quest"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert len(moves) == 1

    def test_unknown_type_freely_nestable(self) -> None:
        anchor = "vault/campaigns/npcs/fio.md"
        member = "vault/campaigns/lore/myth.md"
        type_map = {anchor: "npc", member: "lore"}
        moves = compute_moves(_result(_cluster(anchor, member)), type_map=type_map)
        assert len(moves) == 1

    def test_mixed_cluster_partial_materialisation(self) -> None:
        """Eligible members still move when some members are blocked."""
        anchor = "vault/campaigns/npcs/fio.md"
        eligible = "vault/campaigns/npcs/serena.md"
        blocked = "vault/campaigns/locations/shop.md"
        type_map = {anchor: "npc", eligible: "npc", blocked: "location"}
        moves = compute_moves(_result(_cluster(anchor, eligible, blocked)), type_map=type_map)
        srcs = {op.src for op in moves}
        assert srcs == {eligible}
        assert blocked not in srcs

    def test_no_type_map_no_filtering(self) -> None:
        """Without a type_map, location under npc is not blocked (backward compat)."""
        anchor = "vault/campaigns/npcs/fio.md"
        member = "vault/campaigns/locations/shop.md"
        moves = compute_moves(_result(_cluster(anchor, member)))
        assert len(moves) == 1


# -- apply_moves --


class TestApplyMoves:
    def test_file_moved_to_target(self, tmp_path: Path) -> None:
        src_rel = "vault/campaigns/npcs/foo.md"
        dst_rel = "vault/campaigns/locations/town/foo.md"
        src = tmp_path / src_rel
        src.parent.mkdir(parents=True)
        src.write_text("content", encoding="utf-8")

        apply_moves([MoveOp(src=src_rel, dst=dst_rel)], tmp_path)

        assert not src.exists()
        assert (tmp_path / dst_rel).read_text(encoding="utf-8") == "content"

    def test_missing_src_is_skipped(self, tmp_path: Path) -> None:
        apply_moves([MoveOp(src="vault/missing.md", dst="vault/other.md")], tmp_path)
        # No exception raised

    def test_parent_dirs_created(self, tmp_path: Path) -> None:
        src_rel = "vault/a.md"
        dst_rel = "vault/deep/nested/dir/a.md"
        src = tmp_path / src_rel
        src.parent.mkdir(parents=True)
        src.write_text("x", encoding="utf-8")

        apply_moves([MoveOp(src=src_rel, dst=dst_rel)], tmp_path)
        assert (tmp_path / dst_rel).exists()

    def test_path_wikilinks_scrubbed_after_move(self, tmp_path: Path) -> None:
        src_rel = "vault/campaigns/npcs/foo.md"
        dst_rel = "vault/campaigns/locations/town/foo.md"
        src = tmp_path / src_rel
        src.parent.mkdir(parents=True)
        src.write_text("See [[vault/campaigns/locations/town|Town]].", encoding="utf-8")

        apply_moves([MoveOp(src=src_rel, dst=dst_rel)], tmp_path)

        content = (tmp_path / dst_rel).read_text(encoding="utf-8")
        assert "[[town|Town]]" in content
        assert "vault/campaigns" not in content


# -- scrub helper --


class TestScrubPathWikilinks:
    def test_path_wikilink_rewritten(self, tmp_path: Path) -> None:
        f = tmp_path / "page.md"
        f.write_text("[[vault/campaigns/npcs/foo|Foo]]", encoding="utf-8")
        _scrub_path_wikilinks(f)
        assert f.read_text(encoding="utf-8") == "[[foo|Foo]]"

    def test_slug_only_untouched(self, tmp_path: Path) -> None:
        f = tmp_path / "page.md"
        original = "[[foo|Foo]] and [[bar]]"
        f.write_text(original, encoding="utf-8")
        _scrub_path_wikilinks(f)
        assert f.read_text(encoding="utf-8") == original

    def test_embed_wikilink_rewritten(self, tmp_path: Path) -> None:
        f = tmp_path / "page.md"
        f.write_text("![[vault/assets/maps/sparhold.png]]", encoding="utf-8")
        _scrub_path_wikilinks(f)
        assert f.read_text(encoding="utf-8") == "![[sparhold]]"


# -- idempotency integration --


class TestIdempotency:
    def test_second_run_is_noop(self, tmp_path: Path) -> None:
        """Materialise, then verify compute_moves returns empty on re-analysis."""
        anchor = "vault/campaigns/locations/town.md"
        member = "vault/campaigns/npcs/guard.md"
        (tmp_path / "vault/campaigns/locations").mkdir(parents=True)
        (tmp_path / "vault/campaigns/npcs").mkdir(parents=True)
        (tmp_path / anchor).write_text("---\ntitle: Town\n---\n", encoding="utf-8")
        (tmp_path / member).write_text("---\ntitle: Guard\n---\n", encoding="utf-8")

        # First run
        result = _result(_cluster(anchor, member))
        moves = compute_moves(result)
        assert len(moves) == 1
        apply_moves(moves, tmp_path)

        # After move, guard is at town/guard.md; rebuild result with new paths
        new_member = "vault/campaigns/locations/town/guard.md"
        assert (tmp_path / new_member).exists()

        result2 = _result(_cluster(anchor, new_member))
        moves2 = compute_moves(result2)
        assert moves2 == []
