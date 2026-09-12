from __future__ import annotations

import numpy as np

from dndsim.core.tags import BatchTags
from dndsim.rules.dnd5e_2014.effects import EffectTracker, concentration_source


def test_apply_adds_tag_only_in_masked_universes() -> None:
    size = 4
    tags = BatchTags(size)
    tracker = EffectTracker(tags=tags, size=size)
    mask = np.array([True, False, True, False])

    tracker.apply(source="spell:hold-person", tag="paralyzed", mask=mask, duration_rounds=2)

    assert tags.has("paralyzed").tolist() == [True, False, True, False]


def test_tick_end_of_round_expires_on_schedule() -> None:
    size = 2
    tags = BatchTags(size)
    tracker = EffectTracker(tags=tags, size=size)
    mask = np.ones(size, dtype=np.bool_)

    tracker.apply(source="spell:hold-person", tag="paralyzed", mask=mask, duration_rounds=2)
    assert tags.has("paralyzed").all()

    tracker.tick_end_of_round()  # duration 2 -> 1
    assert tags.has("paralyzed").all()

    tracker.tick_end_of_round()  # duration 1 -> 0, still active this round
    assert tags.has("paralyzed").all()

    tracker.tick_end_of_round()  # duration 0 -> -1, expires
    assert not tags.has("paralyzed").any()


def test_indefinite_effect_never_ticks_away() -> None:
    size = 3
    tags = BatchTags(size)
    tracker = EffectTracker(tags=tags, size=size)
    mask = np.ones(size, dtype=np.bool_)

    tracker.apply(source="conc:caster", tag="blessed", mask=mask, duration_rounds=None)
    for _ in range(50):
        tracker.tick_end_of_round()
    assert tags.has("blessed").all()


def test_remove_from_source_only_touches_matching_source() -> None:
    size = 3
    tags = BatchTags(size)
    tracker = EffectTracker(tags=tags, size=size)
    mask = np.ones(size, dtype=np.bool_)

    tracker.apply(source=concentration_source("caster"), tag="blessed", mask=mask)
    tracker.apply(source="item:ring-of-protection", tag="invisible", mask=mask)

    tracker.remove_from_source(concentration_source("caster"), mask)

    assert not tags.has("blessed").any()
    assert tags.has("invisible").all()


def test_remove_from_source_respects_a_partial_mask() -> None:
    size = 4
    tags = BatchTags(size)
    tracker = EffectTracker(tags=tags, size=size)
    all_mask = np.ones(size, dtype=np.bool_)
    tracker.apply(source=concentration_source("caster"), tag="blessed", mask=all_mask)

    partial = np.array([True, True, False, False])
    tracker.remove_from_source(concentration_source("caster"), partial)

    assert tags.has("blessed").tolist() == [False, False, True, True]


def test_active_sources_reports_current_holders() -> None:
    size = 2
    tags = BatchTags(size)
    tracker = EffectTracker(tags=tags, size=size)
    mask = np.ones(size, dtype=np.bool_)
    tracker.apply(source="conc:a", tag="blessed", mask=mask)

    assert tracker.active_sources("blessed") == ["conc:a"]
    assert tracker.active_sources("stunned") == []
