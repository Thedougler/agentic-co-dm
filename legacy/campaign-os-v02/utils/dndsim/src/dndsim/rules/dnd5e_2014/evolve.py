"""Evolutionary statblock tuner + difficulty ladder (issue #54): a
generational GA over one enemy's mechanical knobs (:mod:`dndsim.rules.
dnd5e_2014.knobs`), fitness = :mod:`dndsim.rules.dnd5e_2014.goals`'s
violation score on a reduced-universe probe. GA randomness runs on its own
substream (:func:`~dndsim.core.rng.substream_seed`), so fitness sims stay
bit-identical per delta and the whole search is deterministic for a given
seed.

**No wall-clock budget**: a full 274-page corpus sweep runs in about a
second at 8 workers (ADR-0011's Phase 0 measurement), so a GA population of
fixed, generous size (population 12, generations 8, probe 2000 universes)
completes in well under a second too; there is nothing here for a
calibrated ms budget to protect against. See this module's own test for a
measured wall-clock figure.

**Corpus-integrity guard**: staging (:func:`stage_tuned_statblock`) never
writes over a page carrying ``source_url``/``source_archive`` frontmatter
(SRD/shared reference material) — refused with a reason, matching
``sys/runbooks/encounter-tuning.md``'s guard. Output always lands at a
fixed, gitignored scratch path by default; writing the real page requires
``apply=True``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from dndsim.core.rng import cell_seed, substream_seed
from dndsim.core.universe import UniverseBatch
from dndsim.rules.dnd5e_2014.combat import CombatResult, run_combat
from dndsim.rules.dnd5e_2014.compile import CompiledStatblock
from dndsim.rules.dnd5e_2014.dice import parse_dice_expr
from dndsim.rules.dnd5e_2014.fixture import CombatantSpec
from dndsim.rules.dnd5e_2014.goals import Goal, GoalsEvaluation, band_tune_goals, evaluate_goals
from dndsim.rules.dnd5e_2014.knobs import (
    MUTATION_KNOBS,
    apply_delta,
    clamp_delta,
    describe_delta,
    knob_delta,
    mutate_dice_expr,
)
from dndsim.rules.dnd5e_2014.sensitivity import DriverRanking, rank_drivers
from dndsim.rules.dnd5e_2014.statblock import (
    StatblockParseError,
    extract_statblock_fence,
    parse_statblock_page,
)

DEFAULT_POPULATION = 12
DEFAULT_GENERATIONS = 8
DEFAULT_ELITISM = 2
DEFAULT_TOURNAMENT_K = 3
DEFAULT_PROBE_UNIVERSES = 2000
DEFAULT_CONFIRM_UNIVERSES = 10_000
DEFAULT_TOP_N = 5
DEFAULT_GA_SUBSTREAM_KEY = 0x9A11

# Retry budget for finding a non-duplicate child in one population slot,
# scoped per slot so one hard-to-mutate-into-something-new delta space
# never starves every other slot's own budget.
_MAX_DEDUP_ATTEMPTS = 200

BAND_NAMES: tuple[str, ...] = ("easy", "medium", "hard", "deadly", "tpk")


def _canonical_key(delta: dict[str, float]) -> tuple[tuple[str, float], ...]:
    return tuple(sorted(delta.items()))


@dataclass(frozen=True, slots=True)
class EvolveVariant:
    delta: dict[str, float]
    delta_text: str
    score: float
    evaluation: GoalsEvaluation
    result: CombatResult
    confirmed: bool


@dataclass(frozen=True, slots=True)
class EvolveResult:
    ranked: tuple[EvolveVariant, ...]
    generations_run: int
    sims_run: int
    params: dict[str, Any]


def evolve_statblock(
    party: list[CombatantSpec],
    enemies: list[CombatantSpec],
    target_index: int,
    goals: tuple[Goal, ...],
    *,
    seed: int,
    round_cap: int = 20,
    policy_id: str = "dndsim:policy/greedy",
    population: int = DEFAULT_POPULATION,
    generations: int = DEFAULT_GENERATIONS,
    elitism: int = DEFAULT_ELITISM,
    tournament_k: int = DEFAULT_TOURNAMENT_K,
    probe_universes: int = DEFAULT_PROBE_UNIVERSES,
    confirm_universes: int = DEFAULT_CONFIRM_UNIVERSES,
    top_n: int = DEFAULT_TOP_N,
    substream_key: int = DEFAULT_GA_SUBSTREAM_KEY,
) -> EvolveResult:
    """Generational GA searching ``enemies[target_index]``'s knobs toward
    ``goals``. Returns the top ``top_n`` variants, best-first."""
    target_statblock = enemies[target_index].compiled
    if target_statblock is None:
        raise ValueError("evolve.evolve_statblock: target combatant has no compiled statblock")

    rng = np.random.default_rng(substream_seed(seed, substream_key))
    memo: dict[tuple[tuple[tuple[str, float], ...], int], EvolveVariant] = {}
    sims_run = 0

    def evaluate(delta: dict[str, float], universes: int = probe_universes) -> EvolveVariant:
        nonlocal sims_run
        key = (_canonical_key(delta), universes)
        cached = memo.get(key)
        if cached is not None:
            return cached
        mutated = apply_delta(enemies[target_index], delta) if delta else enemies[target_index]
        probe_enemies = [mutated if i == target_index else e for i, e in enumerate(enemies)]
        # Deterministic in (seed, substream_key, delta, universes) alone —
        # never in call order — matching cell_seed's own stable-identity
        # contract (never Python's hash(), which is per-process randomized).
        cell_key = f"evolve:{substream_key}:{_canonical_key(delta)}@{universes}"
        batch = UniverseBatch(size=universes, seed=cell_seed(seed, cell_key))
        result = run_combat(party, probe_enemies, batch, round_cap=round_cap, policy_id=policy_id)
        sims_run += 1
        evaluation = evaluate_goals(goals, result)
        variant = EvolveVariant(
            delta=delta,
            delta_text=describe_delta(target_statblock, delta),
            score=evaluation.score,
            evaluation=evaluation,
            result=result,
            confirmed=universes != probe_universes,
        )
        memo[key] = variant
        return variant

    def mutate(delta: dict[str, float]) -> dict[str, float]:
        knob = MUTATION_KNOBS[int(rng.integers(len(MUTATION_KNOBS)))]
        direction = -1 if rng.random() < 0.5 else 1
        next_delta = dict(delta)
        next_delta[knob] = next_delta.get(knob, 0) + knob_delta(target_statblock, knob, direction)
        if rng.random() < 0.3:
            knob2 = MUTATION_KNOBS[int(rng.integers(len(MUTATION_KNOBS)))]
            direction2 = -1 if rng.random() < 0.5 else 1
            next_delta[knob2] = next_delta.get(knob2, 0) + knob_delta(
                target_statblock, knob2, direction2
            )
        return clamp_delta(next_delta, target_statblock)

    # Gen 0: the original plus deterministic single-knob +-1 probes.
    seeds: list[dict[str, float]] = [{}]
    for knob in MUTATION_KNOBS:
        for direction in (1, -1):
            if len(seeds) >= population:
                break
            d = clamp_delta({knob: knob_delta(target_statblock, knob, direction)}, target_statblock)
            if d:
                seeds.append(d)
    pop = [evaluate(d) for d in seeds[:population]]

    generations_run = 0
    confirmed_best: EvolveVariant | None = None
    for g in range(generations):
        pop.sort(key=lambda v: v.score)
        if pop[0].score == 0:
            confirm = evaluate(pop[0].delta, confirm_universes)
            if confirm.score == 0:
                confirmed_best = confirm
                break
        generations_run = g + 1
        next_pop = list(pop[:elitism])
        seen = {_canonical_key(v.delta) for v in next_pop}
        while len(next_pop) < population:
            parent = pop[int(rng.integers(len(pop)))]
            for _ in range(1, tournament_k):
                rival = pop[int(rng.integers(len(pop)))]
                if rival.score < parent.score:
                    parent = rival
            child = mutate(parent.delta)
            key = _canonical_key(child)
            attempts = 0
            while key in seen and attempts < _MAX_DEDUP_ATTEMPTS:
                child = mutate(parent.delta)
                key = _canonical_key(child)
                attempts += 1
            seen.add(key)
            next_pop.append(evaluate(child))
        pop = next_pop

    pop.sort(key=lambda v: v.score)
    ranked = list(pop[:top_n])
    if confirmed_best is not None and ranked:
        ranked[0] = confirmed_best

    return EvolveResult(
        ranked=tuple(ranked),
        generations_run=generations_run,
        sims_run=sims_run,
        params={
            "population": population,
            "generations": generations,
            "elitism": elitism,
            "tournament_k": tournament_k,
            "probe_universes": probe_universes,
            "top_n": top_n,
        },
    )


@dataclass(frozen=True, slots=True)
class BandLadderResult:
    target_name: str
    drivers: DriverRanking
    ladder: dict[str, EvolveResult]


def run_band_ladder_tune(
    party: list[CombatantSpec],
    enemies: list[CombatantSpec],
    target_index: int,
    *,
    seed: int,
    round_cap: int = 20,
    policy_id: str = "dndsim:policy/greedy",
    ga_kwargs: dict[str, Any] | None = None,
) -> BandLadderResult:
    """Driver attribution (run once, shared) plus one GA per band in
    :data:`BAND_NAMES`, each targeting that band's ``band_tune_goals``
    preset — the DM-facing "what would an Easy/.../TPK-inducing version of
    this creature look like" answer, no hand-authored goals file needed."""
    target_statblock = enemies[target_index].compiled
    if target_statblock is None:
        raise ValueError("evolve.run_band_ladder_tune: target combatant has no compiled statblock")

    drivers = rank_drivers(
        party, enemies, target_index, seed=seed, round_cap=round_cap, policy_id=policy_id
    )

    ladder: dict[str, EvolveResult] = {}
    for i, band in enumerate(BAND_NAMES):
        kwargs = dict(ga_kwargs or {})
        # Each band gets its own GA substream so Easy/Medium/Hard/Deadly/TPK
        # explore distinct mutation sequences instead of converging on
        # whatever the shared stream finds first.
        kwargs.setdefault("substream_key", DEFAULT_GA_SUBSTREAM_KEY + i + 1)
        ladder[band] = evolve_statblock(
            party,
            enemies,
            target_index,
            band_tune_goals(band),
            seed=seed,
            round_cap=round_cap,
            policy_id=policy_id,
            **kwargs,
        )
    return BandLadderResult(target_name=target_statblock.name, drivers=drivers, ladder=ladder)


# --- staged output -----------------------------------------------------------

DEFAULT_SCRATCH_PATH = Path(__file__).resolve().parents[4] / ".scratch" / "evolve-statblock.md"


class TuneWriteRefused(ValueError):
    """Staging/applying a tuned statblock was refused (corpus-integrity guard)."""


def _frontmatter(markdown: str) -> dict[str, Any]:
    match = re.match(r"^---\r?\n(.*?)^---[ \t]*\r?\n", markdown, re.MULTILINE | re.DOTALL)
    if match is None:
        return {}
    try:
        doc = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return {}
    return doc if isinstance(doc, dict) else {}


def guard_shared_reference(markdown: str, path: Path) -> None:
    """Refuse a write target that is shared reference material: SRD/RAW
    content carries ``source_url``/``source_archive`` frontmatter (the
    corpus-integrity constraint in ``sys/runbooks/encounter-tuning.md`` —
    the bestiary doubles as every ``--sweep-corpus``/``--sweep-count``'s own
    corpus, so silently overwriting a shared page corrupts every future
    sweep that depends on it)."""
    fm = _frontmatter(markdown)
    if fm.get("source_url") or fm.get("source_archive"):
        raise TuneWriteRefused(
            f"{path}: carries source_url/source_archive frontmatter — this is shared reference "
            "material, not this encounter's own homebrew creature. Emit to a new page instead "
            "(vault/refs/vault/monster/references/reskin-templates.md's variant-naming "
            "convention)."
        )


def emit_statblock_markdown(
    original_markdown: str, statblock: CompiledStatblock, delta: dict[str, float]
) -> str:
    """Patch the winning variant's delta into the original page's
    ```statblock fence — ``ac``/``hp`` fields directly, action ``desc``
    prose for to-hit/damage/multiattack via the same regex patches
    ``evolve.mjs``'s ``emitStatblockMarkdown`` applies. Re-parses its own
    output before returning, so the emitted block is simulatable by
    construction."""
    fence = extract_statblock_fence(original_markdown)
    if fence is None:
        raise TuneWriteRefused("emit_statblock_markdown: target has no ```statblock fence")
    doc = yaml.safe_load(fence)
    if not isinstance(doc, dict):
        raise TuneWriteRefused(
            "emit_statblock_markdown: target's ```statblock fence is not a mapping"
        )

    if "ac" in delta:
        if isinstance(doc.get("ac"), int | float):
            doc["ac"] = int(doc["ac"] + delta["ac"])
        else:
            doc["ac"] = re.sub(
                r"\d+", lambda m: str(int(m.group()) + int(delta["ac"])), str(doc.get("ac", ""))
            )
    if "hp" in delta:
        doc["hp"] = max(1, int(doc.get("hp", 0) + delta["hp"]))
    if "speed_ft" in delta and isinstance(doc.get("speed"), str):
        doc["speed"] = re.sub(
            r"\d+",
            lambda m: str(max(0, int(m.group()) + int(delta["speed_ft"]))),
            doc["speed"],
            count=1,
        )

    action_names = [a.get("name", "") for a in (doc.get("actions") or []) if isinstance(a, dict)]
    doc["actions"] = _patch_action_list(doc.get("actions"), delta, action_names)
    if doc.get("bonus_actions"):
        doc["bonus_actions"] = _patch_action_list(doc.get("bonus_actions"), delta, action_names)

    new_fence = f"```statblock\n{yaml.safe_dump(doc, sort_keys=False)}```"
    emitted = re.sub(
        r"^```statblock[ \t]*\r?\n.*?^```[ \t]*$",
        lambda _m: new_fence,
        original_markdown,
        count=1,
        flags=re.MULTILINE | re.DOTALL,
    )

    reparsed = parse_statblock_page(emitted, "(evolved)")
    if reparsed is None:
        raise StatblockParseError("evolve: emitted statblock no longer parses")
    return emitted


_NUMBER_WORDS = {
    "a": 1,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
}


def _patch_multiattack_desc(desc: str, action_names: list[str], delta: int) -> str:
    best: re.Match[str] | None = None
    for name in action_names:
        if not name:
            continue
        pattern = re.compile(
            rf"\b({'|'.join(re.escape(w) for w in _NUMBER_WORDS)}|\d+)\s+{re.escape(name)}",
            re.IGNORECASE,
        )
        m = pattern.search(desc)
        if m is not None and (best is None or m.start() < best.start()):
            best = m
    if best is None:
        return desc
    token = best.group(1)
    count = _NUMBER_WORDS.get(token.lower(), int(token) if token.isdigit() else 1)
    new_token = str(max(1, count + delta))
    return desc[: best.start(1)] + new_token + desc[best.end(1) :]


def _dice_expr_avg(expr: str) -> int:
    parsed = parse_dice_expr(expr)
    total = float(parsed.flat)
    for d in parsed.dice:
        total += d.sign * d.count * (d.sides + 1) / 2
    return int(total)


def _patch_action_desc(desc: str, delta: dict[str, float]) -> str:
    out = desc
    if "to_hit" in delta:
        out = re.sub(
            r"([+-]\d+)\s+to hit",
            lambda m: f"{int(m.group(1)) + int(delta['to_hit']):+d} to hit",
            out,
            flags=re.IGNORECASE,
        )
    if delta.get("dice_step") or delta.get("flat_damage"):

        def _sub(m: re.Match[str]) -> str:
            expr = m.group(2)
            new_expr = mutate_dice_expr(
                expr, int(delta.get("dice_step", 0)), int(delta.get("flat_damage", 0))
            )
            return f"Hit: {_dice_expr_avg(new_expr)} ({new_expr})"

        out = re.sub(r"Hit:\s*(\d+)\s*\(([^)]+)\)", _sub, out, flags=re.IGNORECASE)
    return out


def _patch_action_list(actions: Any, delta: dict[str, float], action_names: list[str]) -> Any:
    if not isinstance(actions, list):
        return actions
    patched = []
    for a in actions:
        if not isinstance(a, dict):
            patched.append(a)
            continue
        a = dict(a)
        name = a.get("name", "")
        desc = a.get("desc", "")
        if name.strip().lower() == "multiattack" and "multiattack" in delta:
            desc = _patch_multiattack_desc(desc, action_names, int(delta["multiattack"]))
        else:
            desc = _patch_action_desc(desc, delta)
        a["desc"] = desc
        patched.append(a)
    return patched


def stage_tuned_statblock(
    original_path: Path,
    statblock: CompiledStatblock,
    delta: dict[str, float],
    *,
    apply: bool = False,
    scratch_path: Path = DEFAULT_SCRATCH_PATH,
) -> Path:
    """Emit ``original_path``'s page with ``delta`` patched into its
    ```statblock fence, staged at ``scratch_path`` (overwritten every call,
    never an accumulating log) unless ``apply=True`` writes ``original_path``
    directly. Refuses (never stages, never applies) a target carrying
    ``source_url``/``source_archive`` frontmatter — see
    :func:`guard_shared_reference`. Returns the path actually written."""
    original_markdown = original_path.read_text()
    guard_shared_reference(original_markdown, original_path)
    emitted = emit_statblock_markdown(original_markdown, statblock, delta)
    if apply:
        original_path.write_text(emitted)
        return original_path
    scratch_path.parent.mkdir(parents=True, exist_ok=True)
    scratch_path.write_text(emitted)
    return scratch_path
