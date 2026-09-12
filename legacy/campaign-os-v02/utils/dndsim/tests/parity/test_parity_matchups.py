"""Issue #52 acceptance criterion: "A committed fixed matchup set spans
single combatants, parties, and a legendary creature" — asserted directly
against the real, built matchup set rather than against any hand-kept
inventory of what it's supposed to contain."""

from __future__ import annotations

from parity_matchups import build_matchups, strip_compiled


def test_matchup_ids_are_unique() -> None:
    matchups = build_matchups()
    ids = [m.id for m in matchups]
    assert len(ids) == len(set(ids))


def test_every_matchup_has_at_least_one_combatant_per_side() -> None:
    for matchup in build_matchups():
        assert len(matchup.party) >= 1, matchup.id
        assert len(matchup.enemies) >= 1, matchup.id


def test_matchup_set_spans_single_combatants() -> None:
    matchups = build_matchups()
    assert any(len(m.party) == 1 and len(m.enemies) == 1 for m in matchups)


def test_matchup_set_spans_full_party_vs_single_enemy() -> None:
    matchups = build_matchups()
    assert any(len(m.party) > 1 and len(m.enemies) == 1 for m in matchups)


def test_matchup_set_spans_party_vs_multiple_enemies() -> None:
    matchups = build_matchups()
    assert any(len(m.party) > 1 and len(m.enemies) > 1 for m in matchups)


def test_matchup_set_includes_a_legendary_creature_with_reactions_and_lair() -> None:
    matchups = build_matchups()
    legendary_lair = [m for m in matchups if any(c.legendary and c.has_lair for c in m.enemies)]
    assert legendary_lair, "no matchup exercises a legendary + lair-bearing enemy"
    # Reactions (opportunity attacks) are exercised generically by any melee
    # combatant in `run_combat`, not by a per-statblock flag — so the
    # requirement is that this matchup's legendary side is melee.
    assert any(c.is_melee for m in legendary_lair for c in m.enemies if c.legendary)


def test_old_engine_args_resolve_to_real_files_or_the_party_keyword() -> None:
    # The side-spec grammar: a comma-list of
    # <slug-or-path>[:count] tokens, or the keyword "party".
    from pathlib import Path

    for matchup in build_matchups():
        assert matchup.old_x == "party" or Path(matchup.old_x.split(":")[0]).exists(), matchup.id
        for token in matchup.old_y.split(","):
            assert Path(token.split(":")[0]).exists(), matchup.id


def test_combatants_are_built_from_real_vault_content_not_placeholder_stats() -> None:
    # Every combatant's hp/ac must come from a real page, never a zero or
    # obviously-unset default — a real regression here would silently turn
    # this harness into a comparison of nonsense stat lines.
    for matchup in build_matchups():
        for combatant in (*matchup.party, *matchup.enemies):
            assert combatant.hp_max > 0, combatant.entity.name
            assert combatant.armor_class > 0, combatant.entity.name
            assert combatant.attack_bonus != 0, combatant.entity.name


def test_at_least_one_matchup_is_a_regression_guard() -> None:
    # Issue #64: the CR2 ceiling cases are kept, but only as regression
    # guards, never as parity evidence.
    matchups = build_matchups()
    assert any(m.regression_guard for m in matchups)


def test_at_least_three_matchups_are_asserted_and_discriminating() -> None:
    # Issue #64's core acceptance criterion: the set must contain matchups
    # whose win probability sits away from 0 and 1 on both engines, beyond
    # the single pre-existing 1v1. regression_guard=False is what marks a
    # matchup as making that claim.
    matchups = build_matchups()
    non_guards = [m for m in matchups if not m.regression_guard]
    assert len(non_guards) >= 3, [m.id for m in non_guards]


def test_strip_compiled_clears_the_compiled_kit_without_changing_stats() -> None:
    for matchup in build_matchups():
        if matchup.regression_guard:
            continue
        for side in (matchup.party, matchup.enemies):
            ablated = strip_compiled(side)
            assert len(ablated) == len(side)
            for original, stripped in zip(side, ablated, strict=True):
                assert stripped.compiled is None
                assert stripped.hp_max == original.hp_max
                assert stripped.armor_class == original.armor_class
                assert stripped.entity.id == original.entity.id
