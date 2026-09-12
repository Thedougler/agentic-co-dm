"""Goals vocabulary (issue #54): score a :class:`~dndsim.rules.dnd5e_2014.
combat.CombatResult` against DM-stated numeric targets — "deadly but
winnable" encoded as numbers instead of eyeballed. This module's metric
vocabulary is the subset ``CombatResult`` actually carries
(``mean_rounds_out_of_range`` has no positioning aggregate on
``CombatResult`` yet — NOTED (not done), tracked alongside issue #1's
mechanic-vocabulary gaps rather than approximated here).

A goal is met when its value falls within ``[min, max]`` (either bound
optional). :func:`evaluate_goals` returns a weighted violation distance per
goal (0 = met) plus a total score — 0 iff every goal is met — that
:mod:`dndsim.rules.dnd5e_2014.evolve`'s GA minimizes as its fitness
function.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from dndsim.difficulty import (
    DEADLY_DOWN_MIN,
    DEADLY_TPK_MIN,
    DEADLY_WIN_MAX,
    EASY_DOWN_MAX,
    EASY_WIN_MIN,
    MEDIUM_DOWN_MAX,
    MEDIUM_WIN_MIN,
)
from dndsim.rules.dnd5e_2014.combat import CombatResult

GOALS_SCHEMA_VERSION = 1

GOAL_METRICS = frozenset(
    {
        "win_probability",
        "p_down_at_least",
        "tpk_probability",
        "stalemate_rate",
        "rounds_mean",
        "rounds_median",
        "mean_party_hp_loss",
    }
)

# Metrics already on a 0..1 scale — violation distance needs no
# normalization; every other metric normalizes by the bound span instead.
_PROBABILITY_METRICS = frozenset(
    {
        "win_probability",
        "p_down_at_least",
        "tpk_probability",
        "stalemate_rate",
        "mean_party_hp_loss",
    }
)


class GoalsError(ValueError):
    """A goals document failed validation, or an unknown metric was requested."""


@dataclass(frozen=True, slots=True)
class Goal:
    metric: str
    k: int | None = None
    min: float | None = None
    max: float | None = None
    weight: float = 1.0


@dataclass(frozen=True, slots=True)
class GoalOutcome:
    goal: Goal
    value: float
    met: bool
    distance: float


@dataclass(frozen=True, slots=True)
class GoalsEvaluation:
    per_goal: tuple[GoalOutcome, ...]
    score: float
    all_met: bool


def validate_goals(doc: Any, source: str = "(inline)") -> tuple[Goal, ...]:
    """Validate a parsed goals mapping into the normalized goal list."""
    if not isinstance(doc, dict):
        raise GoalsError(f"goals: {source} — (root): must be a map")
    if doc.get("schema_version") != GOALS_SCHEMA_VERSION:
        raise GoalsError(f"goals: {source} — schema_version: must be {GOALS_SCHEMA_VERSION}")
    raw_goals = doc.get("goals")
    if not isinstance(raw_goals, list) or len(raw_goals) == 0:
        raise GoalsError(f"goals: {source} — goals: requires a non-empty list")

    goals: list[Goal] = []
    for i, g in enumerate(raw_goals):
        path = f"goals[{i}]"
        if not isinstance(g, dict):
            raise GoalsError(f"goals: {source} — {path}: must be a map")
        metric = g.get("metric")
        if metric not in GOAL_METRICS:
            raise GoalsError(
                f"goals: {source} — {path}.metric: unknown metric {metric!r} — "
                f"vocabulary: {', '.join(sorted(GOAL_METRICS))}"
            )
        k = g.get("k")
        if metric == "p_down_at_least" and (not isinstance(k, int) or isinstance(k, bool) or k < 1):
            raise GoalsError(
                f"goals: {source} — {path}.k: p_down_at_least requires an integer k >= 1"
            )
        gmin, gmax = g.get("min"), g.get("max")
        if gmin is None and gmax is None:
            raise GoalsError(f"goals: {source} — {path}: requires min and/or max")
        for bound_name, bound in (("min", gmin), ("max", gmax)):
            if bound is not None and not isinstance(bound, int | float):
                raise GoalsError(f"goals: {source} — {path}.{bound_name}: must be a number")
        if gmin is not None and gmax is not None and gmin > gmax:
            raise GoalsError(f"goals: {source} — {path}: min {gmin} exceeds max {gmax}")
        weight = g.get("weight", 1.0)
        if not isinstance(weight, int | float) or weight <= 0:
            raise GoalsError(f"goals: {source} — {path}.weight: must be a positive number")
        goals.append(
            Goal(
                metric=metric,
                k=k if metric == "p_down_at_least" else None,
                min=float(gmin) if gmin is not None else None,
                max=float(gmax) if gmax is not None else None,
                weight=float(weight),
            )
        )
    return tuple(goals)


def load_goals_file(path: Path) -> tuple[Goal, ...]:
    """Load and validate one goals YAML file."""
    try:
        doc = yaml.safe_load(path.read_text())
    except (OSError, yaml.YAMLError) as err:
        raise GoalsError(f"goals: cannot read/parse {path}: {err}") from err
    return validate_goals(doc, str(path))


def extract_metric(result: CombatResult, goal: Goal) -> float:
    """Pull one goal's metric value out of a simulated ``CombatResult``."""
    if goal.metric == "win_probability":
        return result.party_win_rate
    if goal.metric == "p_down_at_least":
        assert goal.k is not None
        # k beyond party size cannot occur => probability 0, not an error.
        idx = goal.k - 1
        return result.at_least_k_down[idx] if 0 <= idx < len(result.at_least_k_down) else 0.0
    if goal.metric == "tpk_probability":
        return result.tpk_probability
    if goal.metric == "stalemate_rate":
        return result.draw_rate
    if goal.metric == "rounds_mean":
        return result.mean_rounds
    if goal.metric == "rounds_median":
        return result.median_rounds
    if goal.metric == "mean_party_hp_loss":
        return result.mean_party_hp_loss
    raise GoalsError(f"goals: (runtime) — metric: unknown metric {goal.metric!r}")


def _violation_distance(goal: Goal, value: float) -> float:
    under = max(0.0, goal.min - value) if goal.min is not None else 0.0
    over = max(0.0, value - goal.max) if goal.max is not None else 0.0
    raw = under + over
    if raw == 0.0:
        return 0.0
    span = 1.0
    if goal.metric not in _PROBABILITY_METRICS:
        if goal.min is not None and goal.max is not None and goal.max > goal.min:
            span = goal.max - goal.min
        else:
            bound = goal.min if goal.min is not None else goal.max
            assert bound is not None  # validate_goals requires min and/or max
            span = max(1.0, abs(bound))
    return (raw / span) * goal.weight


def evaluate_goals(goals: tuple[Goal, ...], result: CombatResult) -> GoalsEvaluation:
    """Score ``result`` against ``goals`` — 0 iff every goal is met.
    :mod:`dndsim.rules.dnd5e_2014.evolve`'s GA minimizes this score."""
    per_goal = []
    for g in goals:
        value = extract_metric(result, g)
        distance = _violation_distance(g, value)
        per_goal.append(GoalOutcome(goal=g, value=value, met=distance == 0.0, distance=distance))
    return GoalsEvaluation(
        per_goal=tuple(per_goal),
        score=sum(o.distance for o in per_goal),
        all_met=all(o.met for o in per_goal),
    )


# --- band-ladder presets (issue #51's DifficultyInputs thresholds) --------
# Every bound below is dndsim.difficulty's own named constant — the tune
# target and the classifier can never drift apart, matching goals.mjs's own
# defaultTuneGoals()/bandTuneGoals() contract.

# dndsim.difficulty has no "achievable Deadly"/"TPK-inducing" constants of
# its own (issue #51 never needed them — those bands only exist as GA
# *targets*, not classifier outputs) — named here, next to their one use,
# rather than added to difficulty.py's classifier vocabulary.
DEADLY_ACHIEVABLE_WIN_MIN = 0.40
TPK_TARGET_MIN = 0.20

BAND_NAMES: tuple[str, ...] = ("easy", "medium", "hard", "deadly", "tpk")


def default_tune_goals() -> tuple[Goal, ...]:
    """The default auto-tune target for a Deadly result: land in the Hard
    band — clear of Deadly, short of Medium — with TPK and any-PC-down risk
    both bounded."""
    return validate_goals(
        {
            "schema_version": GOALS_SCHEMA_VERSION,
            "goals": [
                {"metric": "win_probability", "min": DEADLY_WIN_MAX, "max": MEDIUM_WIN_MIN},
                {"metric": "tpk_probability", "max": DEADLY_TPK_MIN},
                {"metric": "p_down_at_least", "k": 1, "max": DEADLY_DOWN_MIN},
            ],
        },
        "(default tune goals: Hard band)",
    )


_BAND_GOAL_DOCS: dict[str, dict[str, Any]] = {
    "easy": {
        "schema_version": GOALS_SCHEMA_VERSION,
        "goals": [
            {"metric": "win_probability", "min": EASY_WIN_MIN},
            {"metric": "p_down_at_least", "k": 1, "max": EASY_DOWN_MAX},
        ],
    },
    "medium": {
        "schema_version": GOALS_SCHEMA_VERSION,
        "goals": [
            {"metric": "win_probability", "min": MEDIUM_WIN_MIN, "max": EASY_WIN_MIN},
            {"metric": "p_down_at_least", "k": 1, "max": MEDIUM_DOWN_MAX},
        ],
    },
    "deadly": {
        "schema_version": GOALS_SCHEMA_VERSION,
        "goals": [
            {
                "metric": "win_probability",
                "min": DEADLY_ACHIEVABLE_WIN_MIN,
                "max": DEADLY_WIN_MAX,
            },
            {"metric": "tpk_probability", "max": DEADLY_TPK_MIN * 3},
        ],
    },
    "tpk": {
        "schema_version": GOALS_SCHEMA_VERSION,
        "goals": [{"metric": "tpk_probability", "min": TPK_TARGET_MIN}],
    },
}


def band_tune_goals(band: str) -> tuple[Goal, ...]:
    """Band-ladder tune goals for one of :data:`BAND_NAMES`. ``'hard'``
    delegates to :func:`default_tune_goals` rather than duplicating it."""
    if band == "hard":
        return default_tune_goals()
    doc = _BAND_GOAL_DOCS.get(band)
    if doc is None:
        raise GoalsError(
            f"goals: band_tune_goals — unknown band {band!r}, vocabulary: {', '.join(BAND_NAMES)}"
        )
    return validate_goals(doc, f"(band tune goals: {band})")
