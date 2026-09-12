"""``parity_harness.simulate_time_excluded_matchups`` is the mechanism
DIVERGENCES.md's own "How the parity harness identifies a Divergence-
touching matchup" section specifies: parse every ```divergence fence,
union ``measured.matchups[].id`` across ``category: simulate-time``
entries. Tested twice — once against a small synthetic fixture (so the
union/category-filter logic itself is pinned independent of DIVERGENCES.md's
real, growing content) and once against the live file (so a real category
or id typo in that file is caught)."""

from __future__ import annotations

from pathlib import Path

from parity_matchups import DIVERGENCES_PATH, simulate_time_excluded_matchups

_FIXTURE = """\
# Fixture

## A simulate-time entry with two matchups

```divergence
id: fixture-simulate-time
category: simulate-time
mechanism: fixture mechanism
old_behavior: old
new_behavior: new
measured:
  seed: 1
  universes: 100
  round_cap: 5
  matchups:
    - id: ns:combatant/a-vs-ns:combatant/b
      a_win_rate_delta: 0.01
      b_win_rate_delta: -0.01
      a_tpk_rate_delta: -0.01
      draw_rate_delta: 0.0
    - id: ns:combatant/c-vs-ns:combatant/d
      a_win_rate_delta: 0.02
      b_win_rate_delta: -0.02
      a_tpk_rate_delta: -0.02
      draw_rate_delta: 0.0
```

## A validate-time entry — never contributes a live-matchup exclusion

```divergence
id: fixture-validate-time
category: validate-time
mechanism: fixture mechanism
old_behavior: old
new_behavior: new
measured:
  seed: null
  universes: null
  round_cap: null
  matchups:
    - id: ns:combatant/should-never-appear
      a_win_rate_delta: 0.0
      b_win_rate_delta: 0.0
      a_tpk_rate_delta: 0.0
      draw_rate_delta: 0.0
```
"""


def test_unions_matchups_across_simulate_time_entries_only(tmp_path: Path) -> None:
    fixture = tmp_path / "DIVERGENCES.md"
    fixture.write_text(_FIXTURE)
    excluded = simulate_time_excluded_matchups(fixture)
    assert excluded == {
        "ns:combatant/a-vs-ns:combatant/b",
        "ns:combatant/c-vs-ns:combatant/d",
    }
    assert "ns:combatant/should-never-appear" not in excluded


def test_empty_matchups_list_contributes_nothing(tmp_path: Path) -> None:
    fixture = tmp_path / "DIVERGENCES.md"
    fixture.write_text(
        "```divergence\n"
        "id: fixture-empty\n"
        "category: simulate-time\n"
        "mechanism: m\n"
        "old_behavior: o\n"
        "new_behavior: n\n"
        "measured:\n"
        "  seed: null\n"
        "  universes: null\n"
        "  round_cap: null\n"
        "  matchups: []\n"
        "```\n"
    )
    assert simulate_time_excluded_matchups(fixture) == set()


def test_live_divergences_file_excludes_the_lair_default_activation_matchup() -> None:
    excluded = simulate_time_excluded_matchups(DIVERGENCES_PATH)
    assert "dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/otar-the-foul" in excluded


def test_live_divergences_file_death_saves_matchups_are_excluded() -> None:
    excluded = simulate_time_excluded_matchups(DIVERGENCES_PATH)
    assert "dnd5e_2014:combatant/perrin-vs-dnd5e_2014:combatant/grung-skirmisher" in excluded
    assert "dnd5e_2014:combatant/duelist-vs-dnd5e_2014:combatant/bruiser" in excluded
