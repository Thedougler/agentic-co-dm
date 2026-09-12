"""Effective Difficulty Rating (issue #51): the DM-facing band plus the rule
that fired to select it. Every threshold is a named constant, evaluated
top-down, first match wins; this is explicitly not a DMG table lookup.

A threshold whose required input is unavailable this run (``None`` on
:class:`DifficultyInputs`) never matches — the first-match-wins order falls
through past it to the next rule, or to the terminal ``Hard`` default.
:func:`rate_difficulty` never guesses a band from data it doesn't have; the
caller is expected to report which inputs were unavailable alongside the
band (issue #51's "warnings appear in the report" acceptance criterion).
"""

from __future__ import annotations

from dataclasses import dataclass

DEADLY_WIN_MAX = 0.75
DEADLY_DOWN_MIN = 0.5
DEADLY_TPK_MIN = 0.05
MEDIUM_WIN_MIN = 0.85
EASY_WIN_MIN = 0.95
EASY_DOWN_MAX = 0.10
MEDIUM_DOWN_MAX = 0.30
TRIVIAL_WIN_MIN = 0.99
TRIVIAL_HP_LOSS_MAX = 0.10


@dataclass(frozen=True, slots=True)
class DifficultyInputs:
    """Everything :func:`rate_difficulty` can read. ``win_probability`` is
    the only field a run always has; the rest are ``None`` when this run's
    engine didn't compute them."""

    win_probability: float
    any_down_probability: float | None = None
    tpk_probability: float | None = None
    mean_party_hp_loss: float | None = None


@dataclass(frozen=True, slots=True)
class DifficultyRating:
    band: str
    rule: str


def rate_difficulty(inputs: DifficultyInputs) -> DifficultyRating:
    """Band + the rule that fired, evaluated in the reference engine's
    documented order: Deadly, Trivial, Easy, Medium, then Hard as the
    catch-all."""
    win = inputs.win_probability
    down = inputs.any_down_probability
    tpk = inputs.tpk_probability
    hp_loss = inputs.mean_party_hp_loss

    if (
        win < DEADLY_WIN_MAX
        or (down is not None and down > DEADLY_DOWN_MIN)
        or (tpk is not None and tpk >= DEADLY_TPK_MIN)
    ):
        return DifficultyRating(
            band="Deadly",
            rule=(
                f"P(win) < {DEADLY_WIN_MAX} or P(≥1 down) > {DEADLY_DOWN_MIN} "
                f"or P(TPK) ≥ {DEADLY_TPK_MIN}"
            ),
        )
    if win > TRIVIAL_WIN_MIN and hp_loss is not None and hp_loss < TRIVIAL_HP_LOSS_MAX:
        return DifficultyRating(
            band="Trivial",
            rule=f"P(win) > {TRIVIAL_WIN_MIN} and mean party HP loss < {TRIVIAL_HP_LOSS_MAX:.0%}",
        )
    if win >= EASY_WIN_MIN and down is not None and down < EASY_DOWN_MAX:
        return DifficultyRating(
            band="Easy", rule=f"P(win) ≥ {EASY_WIN_MIN} and P(≥1 down) < {EASY_DOWN_MAX}"
        )
    if win >= MEDIUM_WIN_MIN and down is not None and down < MEDIUM_DOWN_MAX:
        return DifficultyRating(
            band="Medium",
            rule=f"P(win) ≥ {MEDIUM_WIN_MIN} and P(≥1 down) < {MEDIUM_DOWN_MAX}",
        )
    return DifficultyRating(band="Hard", rule="everything else that is not Deadly")
