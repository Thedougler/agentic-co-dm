from __future__ import annotations

from dndsim.core.timeline import Phase, Timeline, Window


def test_phase_iterates_windows_in_order() -> None:
    phase = Phase(id="p1", windows=(Window("w1"), Window("w2")))
    assert [w.id for w in phase] == ["w1", "w2"]


def test_timeline_iterates_phases_in_order() -> None:
    timeline = Timeline(phases=(Phase(id="p1"), Phase(id="p2")))
    assert [p.id for p in timeline] == ["p1", "p2"]


def test_empty_timeline_iterates_to_nothing() -> None:
    assert list(Timeline()) == []
