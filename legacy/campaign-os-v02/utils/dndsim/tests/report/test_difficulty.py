"""``dndsim.difficulty`` — the Effective Difficulty Rating (issue #51)."""

from __future__ import annotations

from dndsim.difficulty import DifficultyInputs, rate_difficulty


def test_low_win_probability_is_deadly() -> None:
    rating = rate_difficulty(DifficultyInputs(win_probability=0.5))
    assert rating.band == "Deadly"
    assert "P(win) < 0.75" in rating.rule


def test_high_tpk_is_deadly_even_with_high_win_probability() -> None:
    rating = rate_difficulty(
        DifficultyInputs(win_probability=0.9, tpk_probability=0.1, any_down_probability=0.05)
    )
    assert rating.band == "Deadly"


def test_high_any_down_is_deadly() -> None:
    rating = rate_difficulty(DifficultyInputs(win_probability=0.9, any_down_probability=0.6))
    assert rating.band == "Deadly"


def test_trivial_needs_hp_loss_data() -> None:
    rating = rate_difficulty(
        DifficultyInputs(win_probability=0.999, mean_party_hp_loss=0.01, tpk_probability=0.0)
    )
    assert rating.band == "Trivial"


def test_easy_band() -> None:
    rating = rate_difficulty(
        DifficultyInputs(win_probability=0.96, any_down_probability=0.05, tpk_probability=0.0)
    )
    assert rating.band == "Easy"


def test_medium_band() -> None:
    rating = rate_difficulty(
        DifficultyInputs(win_probability=0.87, any_down_probability=0.2, tpk_probability=0.0)
    )
    assert rating.band == "Medium"


def test_hard_is_the_catch_all() -> None:
    rating = rate_difficulty(
        DifficultyInputs(win_probability=0.80, any_down_probability=0.4, tpk_probability=0.0)
    )
    assert rating.band == "Hard"
    assert rating.rule == "everything else that is not Deadly"


def test_missing_any_down_and_hp_loss_falls_through_to_hard() -> None:
    """A run that only ever computed win_probability/tpk_probability can
    never confidently classify Trivial/Easy/Medium (all three need a field
    it doesn't have) — it falls through to Hard rather than guessing."""
    rating = rate_difficulty(DifficultyInputs(win_probability=0.98, tpk_probability=0.0))
    assert rating.band == "Hard"
