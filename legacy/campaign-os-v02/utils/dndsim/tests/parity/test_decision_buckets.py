"""Covers `scripts/measure_decision_buckets.py`'s monkeypatch-based
telemetry — ADR-0011's decision-bucket ceiling re-measured against a real
legendary statblock (issue #52's other acceptance criterion) rather than
issue #59's synthetic "Grung Chief" fixture. The regression this guards:
the monkeypatch must count every `bucket_by_choice` call during
`run_combat` and then restore the real function — a leaked patch would
silently corrupt every other test importing `dndsim.rules.dnd5e_2014.combat`
in the same process."""

from __future__ import annotations

from measure_decision_buckets import measure

from dndsim import plugins
from dndsim.rules.dnd5e_2014 import combat as combat_module

plugins.load_policies()


def test_measure_restores_the_real_bucket_by_choice_after_running() -> None:
    real = getattr(combat_module, "bucket_by_choice")  # noqa: B009
    measure("dnd5e_2014:combatant/perrin-black-jaw-vs-dnd5e_2014:combatant/grung-elite-warrior")
    assert getattr(combat_module, "bucket_by_choice") is real  # noqa: B009


def test_measure_reports_at_least_one_decision_point_for_a_real_fight() -> None:
    decision_points, mean_buckets, max_buckets = measure(
        "dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/grung-elite-warrior-x2"
    )
    assert decision_points > 0
    assert mean_buckets >= 1.0
    assert max_buckets >= 1


def test_bucket_count_against_real_legendary_statblock_stays_bounded_by_side_size() -> None:
    # ADR-0011's own claim: bucket count is bounded by a combatant's own
    # option count, not by universe count. Two independent `bucket_by_choice`
    # call sites both apply here: target-choice branching (bounded by
    # Otar's opposing side, the full 5-PC party) and, since this session's
    # turn-order Divergence fix, rolled-initiative occupant branching in
    # the round loop (bounded by TOTAL combatants in the fight — party + Otar,
    # 6 here — since any of the 6 can occupy any turn-slot across the
    # batch). The real ceiling is the larger of the two, not the older
    # target-only bound.
    _decision_points, _mean, max_buckets = measure(
        "dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/otar-the-foul"
    )
    assert max_buckets <= 6
