"""Corpus and count sweeps (issue #53): "how does this subject perform
against everything" and "how many of this monster does it take" — the DM
questions #38's user stories 3/13 name directly. Replaces #50's `--cells`/
`--workers` stand-in on ``sim-combat`` (identical matchup, replicated only
to prove the threading mechanism) with cells that vary the matchup itself:
one cell per opponent in a corpus sweep, one cell per count in a count
sweep.

Every page load goes through :func:`~dndsim.profile.load_compiled_statblock`
— the one page-to-``CompiledStatblock`` assembly path, never re-inlined
here. :func:`combatant_spec_from_statblock` is the one new seam this module
adds: it attaches the loaded :class:`~dndsim.rules.dnd5e_2014.compile.
CompiledStatblock` onto the built
:class:`~dndsim.rules.dnd5e_2014.fixture.CombatantSpec` (issue #60), so
``run_combat`` (``rules/dnd5e_2014/combat.py``) fights every sweep cell with
the statblock's real compiled kit — Multiattack/routine, every declared
action, and every ability Primitive — never a flat single-attack reduction.
Legendary status is now read from content (``CompiledStatblock.
legendary_actions_per_round``, sourced from the fence's own
``legendary_actions`` preamble); lair status still isn't — ``CompiledStatblock``
carries no such field, so it still defaults off. Every cell is seeded via
:func:`~dndsim.core.rng.cell_seed` on its own stable identity (subject +
opponent, or subject + monster + count), so any single reported cell
reproduces exactly by re-running with a plain ``sim-combat``-shaped
seed — never by its position in a larger sweep.
"""

from __future__ import annotations

import time
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path

from dndsim import __version__
from dndsim.core.rng import cell_seed
from dndsim.core.threaded import run_threaded
from dndsim.core.universe import UniverseBatch
from dndsim.difficulty import DifficultyInputs, DifficultyRating, rate_difficulty
from dndsim.profile import ProfileError, load_compiled_statblock
from dndsim.rules.dnd5e_2014.combat import CombatResult, run_combat
from dndsim.rules.dnd5e_2014.compile import CompiledStatblock
from dndsim.rules.dnd5e_2014.dice import parse_dice_expr
from dndsim.rules.dnd5e_2014.fixture import CombatantSpec, make_combatant
from dndsim.rules.dnd5e_2014.primitives import AttackPrimitive
from dndsim.rules.dnd5e_2014.statblock import StatblockParseError

DEFAULT_CORPUS_DIRS: tuple[Path, ...] = (
    Path("vault/srd/monsters"),
    Path("vault/campaigns/shattered-sea/monsters"),
)
DEFAULT_PARTY_GLOB = "vault/campaigns/shattered-sea/pcs/character-sheets/*-sheet.md"
DEFAULT_MIN_COUNT = 1
DEFAULT_MAX_COUNT = 8
_HARD_COUNT_CEILING = 20


class SweepLoadError(ValueError):
    """A page has no attack action a sweep cell can fight with."""


def enumerate_corpus(dirs: Sequence[Path] = DEFAULT_CORPUS_DIRS) -> list[Path]:
    """Every ``*.md`` file directly inside each corpus dir, sorted, matching
    ``runner.mjs``'s ``enumerateCorpus`` — stable enumeration order so a
    sweep's cell order never depends on filesystem iteration order."""
    files: list[Path] = []
    for dir_path in dirs:
        if not dir_path.is_dir():
            continue
        files.extend(sorted(p for p in dir_path.iterdir() if p.suffix == ".md"))
    return files


def primary_attack(statblock: CompiledStatblock) -> tuple[AttackPrimitive, str] | None:
    """The attack a sweep cell fights with: the first attack step of the
    compiled routine, or (no routine resolved) the first attack action —
    the same priority :func:`~dndsim.profile.build_pc_profile` uses for its
    own DPR routine, applied here to picking one representative attack
    instead of a sampled sequence of them."""
    action_by_id = {ability.id: ability for ability in statblock.compiled_actions}
    for step in statblock.routine:
        ability = action_by_id.get(step.ref)
        if ability is not None and isinstance(ability.step, AttackPrimitive):
            return ability.step, ability.name
    for ability in statblock.compiled_actions:
        if isinstance(ability.step, AttackPrimitive):
            return ability.step, ability.name
    return None


def combatant_spec_from_statblock(statblock: CompiledStatblock, *, suffix: str) -> CombatantSpec:
    """Build the :class:`~dndsim.rules.dnd5e_2014.fixture.CombatantSpec`
    ``run_combat`` executes from a parsed page's :class:`CompiledStatblock`
    (issue #60): ``compiled=statblock`` is what makes ``run_combat`` fight
    with the statblock's real kit — every declared action, its
    Multiattack/authored routine, and its ability Primitives — rather than
    the lossy single-attack reduction :func:`_reduce_damage` used to
    perform (deleted, not bypassed, per issue #60's own acceptance
    criterion). The legacy scalar attack_bonus/damage fields are seeded
    from :func:`primary_attack` purely as the physical-shape fallback an
    opportunity attack or a legendary-action window still resolves through
    (neither is driven by the compiled kit in this pass) — never read for
    the combatant's own turn once a compiled statblock is attached.
    ``suffix`` disambiguates the entity id when the same statblock page
    fights itself, or when several copies of one monster share a
    count-sweep side — ``run_combat`` keys its per-combatant state by
    ``entity.id`` across *both* sides, so two combatants sharing one id
    would silently overwrite each other's state.
    """
    if not statblock.compiled_actions:
        raise SweepLoadError(f"{statblock.id}: no compiled action to simulate")
    primary = primary_attack(statblock)
    to_hit = primary[0].to_hit if primary is not None else 0
    dice_count, dice_sides = (1, 4)
    bonus = 0
    if primary is not None and primary[0].damage:
        parsed = parse_dice_expr(primary[0].damage[0].dice)
        bonus = parsed.flat
        if parsed.dice:
            dice_count, dice_sides = parsed.dice[0].count, parsed.dice[0].sides
    return make_combatant(
        entity_id=f"{statblock.id}{suffix}",
        name=statblock.name,
        hp_max=statblock.hp,
        armor_class=statblock.ac,
        attack_bonus=to_hit,
        damage_bonus=bonus,
        damage_dice_count=dice_count,
        damage_dice_sides=dice_sides,
        compiled=statblock,
        legendary=statblock.legendary_actions_per_round > 0,
    )


def _load_statblock(path: Path) -> CompiledStatblock:
    """Load and compile one page through the shared loader, narrowing every
    failure mode — a bad fence (:class:`StatblockParseError`), no fence
    (:class:`~dndsim.profile.ProfileError`), or a compile-time defect in the
    page's own authored content unrelated to this module's own logic (a
    ``pydantic`` validation error, a primitive-construction ``TypeError``) —
    to one exception type callers can catch uniformly. A corpus of 274 pages
    is bound to contain content the compiler doesn't yet handle; one bad
    page must never abort the whole sweep (matching ``runCorpusSweep``'s own
    ``tryLoadEnemy`` contract)."""
    text = path.read_text()
    try:
        statblock, _block = load_compiled_statblock(text, str(path))
    except StatblockParseError, ProfileError:
        raise
    except Exception as err:
        raise SweepLoadError(f"{path}: failed to compile ({type(err).__name__}: {err})") from err
    return statblock


def load_combatant_spec(path: Path, *, suffix: str) -> CombatantSpec:
    """Load one page, through the shared loader, into a combat-ready
    :class:`CombatantSpec`. Raises :class:`StatblockParseError`,
    :class:`~dndsim.profile.ProfileError`, or :class:`SweepLoadError` —
    every reason a page can't stand as a sweep subject/opponent."""
    return combatant_spec_from_statblock(_load_statblock(path), suffix=suffix)


ProgressCallback = Callable[[int, int, str], None]


# --- corpus sweep ------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class CorpusSweepCell:
    """One subject-vs-opponent matchup's own result inside a corpus sweep."""

    opponent: str
    path: str
    seed: int
    result: CombatResult
    rating: DifficultyRating


@dataclass(frozen=True, slots=True)
class CorpusSweepResult:
    """A subject swept against every creature in a corpus."""

    subject: str
    subject_path: str
    seed: int
    corpus_count: int
    cell_count: int
    total_universes: int
    wall_ms: float
    cells: tuple[CorpusSweepCell, ...]
    warnings: tuple[str, ...]


def _load_opponent(path: Path, *, warnings: list[str]) -> CombatantSpec | None:
    try:
        return load_combatant_spec(path, suffix="/opponent")
    except (StatblockParseError, ProfileError, SweepLoadError) as err:
        warnings.append(f"skipped {path}: {err}")
        return None


def corpus_sweep(
    subject_path: Path,
    *,
    corpus_dirs: Sequence[Path] = DEFAULT_CORPUS_DIRS,
    seed: int,
    universes: int,
    round_cap: int = 20,
    policy_id: str = "dndsim:policy/greedy",
    max_workers: int = 1,
    on_progress: ProgressCallback | None = None,
) -> CorpusSweepResult:
    """``subject_path`` vs. every creature in ``corpus_dirs``, one
    independently-seeded cell per opponent (:func:`~dndsim.core.rng.
    cell_seed` keyed on subject name + opponent path — never the cell's
    position), run across ``max_workers`` threads via
    :func:`~dndsim.core.threaded.run_threaded` (thread count is a
    performance knob only; output is identical at any worker count).
    Cells are returned sorted ascending by the subject's win rate (most
    dangerous opponent first), matching ``runCorpusSweep``'s own ordering.
    """
    warnings: list[str] = []
    subject_statblock = _load_statblock(subject_path)
    subject_spec = combatant_spec_from_statblock(subject_statblock, suffix="/subject")

    corpus = enumerate_corpus(corpus_dirs)
    opponents: list[tuple[Path, CombatantSpec]] = []
    for path in corpus:
        spec = _load_opponent(path, warnings=warnings)
        if spec is not None:
            opponents.append((path, spec))

    def make_cell(path: Path, opponent_spec: CombatantSpec) -> Callable[[], CorpusSweepCell]:
        def run() -> CorpusSweepCell:
            key = f"x:{subject_statblock.name}|opp:{path}"
            c_seed = cell_seed(seed, key)
            batch = UniverseBatch(size=universes, seed=c_seed)
            result = run_combat(
                [subject_spec], [opponent_spec], batch, round_cap=round_cap, policy_id=policy_id
            )
            rating = rate_difficulty(
                DifficultyInputs(
                    win_probability=result.party_win_rate,
                    any_down_probability=result.any_down_probability,
                    tpk_probability=result.tpk_probability,
                    mean_party_hp_loss=result.mean_party_hp_loss,
                )
            )
            return CorpusSweepCell(
                opponent=opponent_spec.entity.name,
                path=str(path),
                seed=c_seed,
                result=result,
                rating=rating,
            )

        return run

    started_at = time.perf_counter()
    total = len(opponents)
    cell_calls = [make_cell(path, spec) for path, spec in opponents]
    cells = run_threaded(cell_calls, max_workers=max_workers)
    if on_progress is not None:
        for index, cell in enumerate(cells, start=1):
            on_progress(index, total, cell.opponent)
    wall_ms = (time.perf_counter() - started_at) * 1000

    cells_sorted = tuple(sorted(cells, key=lambda c: c.result.party_win_rate))
    total_universes = sum(c.result.universes for c in cells_sorted)

    return CorpusSweepResult(
        subject=subject_spec.entity.name,
        subject_path=str(subject_path),
        seed=seed,
        corpus_count=len(corpus),
        cell_count=len(cells_sorted),
        total_universes=total_universes,
        wall_ms=wall_ms,
        cells=cells_sorted,
        warnings=tuple(warnings),
    )


def party_corpus_sweep(
    pc_paths: Sequence[Path],
    *,
    corpus_dirs: Sequence[Path] = DEFAULT_CORPUS_DIRS,
    seed: int,
    universes: int,
    round_cap: int = 20,
    policy_id: str = "dndsim:policy/greedy",
    max_workers: int = 1,
    on_progress: ProgressCallback | None = None,
) -> tuple[list[CorpusSweepResult], list[str]]:
    """One :func:`corpus_sweep` per PC in ``pc_paths``, chained — the
    ``party`` keyword's expansion (``runner.mjs``'s ``DEFAULT_PARTY_GLOB``
    behavior). Each PC's sweep is threaded internally; PCs themselves run
    sequentially, in ``pc_paths`` order, so a caller streaming progress
    sees one PC's sweep complete before the next starts. A PC whose own
    page fails to compile (:class:`StatblockParseError`,
    :class:`~dndsim.profile.ProfileError`, :class:`SweepLoadError`) is
    skipped with a warning rather than aborting every other PC's sweep —
    the same "one bad page never aborts the sweep" contract
    :func:`corpus_sweep` already applies to corpus opponents, extended to
    the party side. Returns ``(results, warnings)``.
    """
    results: list[CorpusSweepResult] = []
    warnings: list[str] = []
    for pc_path in pc_paths:
        try:
            results.append(
                corpus_sweep(
                    pc_path,
                    corpus_dirs=corpus_dirs,
                    seed=seed,
                    universes=universes,
                    round_cap=round_cap,
                    policy_id=policy_id,
                    max_workers=max_workers,
                    on_progress=on_progress,
                )
            )
        except (StatblockParseError, ProfileError, SweepLoadError) as err:
            warnings.append(f"skipped {pc_path}: {err}")
    return results, warnings


# --- count sweep --------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class CountSweepCell:
    """One count's own result inside a count sweep."""

    count: int
    seed: int
    result: CombatResult
    rating: DifficultyRating


@dataclass(frozen=True, slots=True)
class CountSweepResult:
    """``party_paths`` (fixed) vs. a swept count of one monster type."""

    monster: str
    monster_path: str
    seed: int
    party_size: int
    total_universes: int
    wall_ms: float
    cells: tuple[CountSweepCell, ...]
    recommended_count_by_band: dict[str, int | None]


_BANDS_LIGHT_TO_DEADLY = ("Trivial", "Easy", "Medium", "Hard", "Deadly")


def _recommended_counts(cells: Sequence[CountSweepCell]) -> dict[str, int | None]:
    """Smallest swept count reaching each band — same selection rule
    ``runCountSweep``'s recommended-count table uses. A band never reached
    in the swept range is ``None``; the caller renders that band-specific
    "unreachable"/"not reached" phrasing, since only it knows whether
    ``min_count``/``max_count`` were user-narrowed."""
    by_band: dict[str, int | None] = dict.fromkeys(_BANDS_LIGHT_TO_DEADLY, None)
    for cell in cells:
        if by_band.get(cell.rating.band) is None:
            by_band[cell.rating.band] = cell.count
    return by_band


def count_sweep(
    party_paths: Sequence[Path],
    monster_path: Path,
    *,
    seed: int,
    universes: int,
    min_count: int = DEFAULT_MIN_COUNT,
    max_count: int = DEFAULT_MAX_COUNT,
    round_cap: int = 20,
    policy_id: str = "dndsim:policy/greedy",
    max_workers: int = 1,
    on_progress: ProgressCallback | None = None,
) -> CountSweepResult:
    """``party_paths`` (fixed, resolved once) vs. ``min_count..max_count``
    copies of ``monster_path``, extended past ``max_count`` (up to
    ``_HARD_COUNT_CEILING``) until the break-even point (win rate crossing
    50%) is found — the practical "how many of these" answer shouldn't
    silently truncate at an arbitrary count, matching ``runCountSweep``.
    Each count copy gets its own suffixed entity id (``/enemy0``,
    ``/enemy1``, ...) so ``run_combat`` never collides two copies' state.
    """
    if min_count < 1:
        raise ValueError(f"count_sweep: min_count must be >= 1, got {min_count}")
    if max_count < min_count:
        raise ValueError(f"count_sweep: max_count ({max_count}) must be >= min_count ({min_count})")

    party_specs = [load_combatant_spec(p, suffix=f"/party{i}") for i, p in enumerate(party_paths)]
    monster_statblock = _load_statblock(monster_path)

    def make_cell(count: int) -> Callable[[], CountSweepCell]:
        def run() -> CountSweepCell:
            enemy_specs = [
                combatant_spec_from_statblock(monster_statblock, suffix=f"/enemy{i}")
                for i in range(count)
            ]
            key = f"monster:{monster_statblock.id}|count:{count}"
            c_seed = cell_seed(seed, key)
            batch = UniverseBatch(size=universes, seed=c_seed)
            result = run_combat(
                party_specs, enemy_specs, batch, round_cap=round_cap, policy_id=policy_id
            )
            rating = rate_difficulty(
                DifficultyInputs(
                    win_probability=result.party_win_rate,
                    any_down_probability=result.any_down_probability,
                    tpk_probability=result.tpk_probability,
                    mean_party_hp_loss=result.mean_party_hp_loss,
                )
            )
            return CountSweepCell(count=count, seed=c_seed, result=result, rating=rating)

        return run

    started_at = time.perf_counter()

    # Break-even discovery is sequential-by-count (each step's stop decision
    # depends on the previous count's result), but the *known* range
    # [min_count, max_count] is independent per count and safe to thread —
    # every cell's seed and result depend only on (seed, monster, count),
    # never on execution order.
    known_counts = list(range(min_count, max_count + 1))
    known_cells = run_threaded([make_cell(c) for c in known_counts], max_workers=max_workers)
    cells: list[CountSweepCell] = list(known_cells)

    extra_count = max_count + 1
    break_even_found = any(c.result.party_win_rate < 0.5 for c in cells)
    while not break_even_found and extra_count <= _HARD_COUNT_CEILING:
        cell = make_cell(extra_count)()
        cells.append(cell)
        if cell.result.party_win_rate < 0.5:
            break_even_found = True
        extra_count += 1

    if on_progress is not None:
        for index, cell in enumerate(cells, start=1):
            on_progress(index, len(cells), f"{cell.count}x {monster_statblock.name}")
    wall_ms = (time.perf_counter() - started_at) * 1000

    total_universes = sum(c.result.universes for c in cells)

    return CountSweepResult(
        monster=monster_statblock.name,
        monster_path=str(monster_path),
        seed=seed,
        party_size=len(party_specs),
        total_universes=total_universes,
        wall_ms=wall_ms,
        cells=tuple(cells),
        recommended_count_by_band=_recommended_counts(cells),
    )


# --- report rendering ---------------------------------------------------------
# report.py's render_combat_report is deliberately not reused for the
# per-cell rows below: a sweep's per-cell full per-PC/per-combatant
# breakdown would make a 270-cell corpus sweep unreadable. A sweep report
# is a table of cells, not a concatenation of full single-matchup reports.


def render_corpus_sweep_report(result: CorpusSweepResult, *, policy: str | None = None) -> str:
    """One subject-vs-corpus sweep as a markdown table, sorted ascending by
    win rate (most dangerous opponent first, matching ``runCorpusSweep``)."""
    lines = [
        f"# Corpus sweep — {result.subject}",
        "",
        f"- **Engine**: dndsim v{__version__}",
        f"- **Seed**: {result.seed}",
        f"- **Subject**: {result.subject} (`{result.subject_path}`)",
        f"- **Corpus**: {result.corpus_count} pages "
        f"({result.cell_count} simulated, {len(result.warnings)} skipped)",
        f"- **Universes simulated**: {result.total_universes:,}",
        f"- **Wall clock**: {result.wall_ms:.1f} ms",
        "",
        "| Opponent | Band | Win % | Seed |",
        "|---|---|---|---|",
    ]
    for cell in result.cells:
        lines.append(
            f"| {cell.opponent} | {cell.rating.band} | "
            f"{cell.result.party_win_rate:.1%} | {cell.seed} |"
        )
    lines.append("")
    if result.warnings:
        lines.append("## Warnings")
        lines.append("")
        lines.extend(f"WARN {w}" for w in result.warnings)
        lines.append("")
    if policy is not None:
        lines.append(f"**Policy**: {policy}")
        lines.append("")
    return "\n".join(lines)


def render_count_sweep_report(result: CountSweepResult, *, policy: str | None = None) -> str:
    """A fixed-party-vs-swept-count sweep: the recommended count per band,
    then the full count matrix, matching ``runCountSweep``'s report shape."""
    lines = [
        f"# Count sweep — {result.monster}",
        "",
        f"- **Engine**: dndsim v{__version__}",
        f"- **Seed**: {result.seed}",
        f"- **Monster**: {result.monster} (`{result.monster_path}`)",
        f"- **Party size**: {result.party_size}",
        f"- **Universes simulated**: {result.total_universes:,}",
        f"- **Wall clock**: {result.wall_ms:.1f} ms",
        "",
        "## Recommended count per band",
        "",
        "| Band | Smallest count reaching it |",
        "|---|---|",
    ]
    for band in _BANDS_LIGHT_TO_DEADLY:
        count = result.recommended_count_by_band.get(band)
        lines.append(f"| {band} | {count if count is not None else 'not reached in swept range'} |")
    lines.extend(
        ["", "## Count matrix", "", "| Count | Band | Win % | Seed |", "|---|---|---|---|"]
    )
    for cell in result.cells:
        lines.append(
            f"| {cell.count} | {cell.rating.band} | "
            f"{cell.result.party_win_rate:.1%} | {cell.seed} |"
        )
    lines.append("")
    if policy is not None:
        lines.append(f"**Policy**: {policy}")
        lines.append("")
    return "\n".join(lines)
