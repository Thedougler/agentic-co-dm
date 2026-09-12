"""The ``dndsim`` command-line entry point."""

from __future__ import annotations

import glob
import json
import sys
import time
from pathlib import Path
from typing import Annotated

import typer

from dndsim import __version__, plugins
from dndsim.core.adaptive import AdaptiveConfig, AdaptiveResult, run_adaptive
from dndsim.core.audit import append_audit_line, build_audit_line
from dndsim.core.policy import policies
from dndsim.core.rng import random_seed, substream_seed
from dndsim.core.stats import wilson_interval
from dndsim.core.universe import UniverseBatch
from dndsim.lint.run import lint_paths
from dndsim.profile import ProfileError, build_pc_profile, load_compiled_statblock
from dndsim.report import render_combat_report, render_pc_profile_report
from dndsim.rules.dnd5e_2014.combat import CombatResult, run_combat
from dndsim.rules.dnd5e_2014.fixture import PARTY_VS_ENEMIES_FIXTURE
from dndsim.rules.dnd5e_2014.side_spec import SideSpecError, resolve_side
from dndsim.rules.dnd5e_2014.statblock import (
    StatblockContent,
    StatblockImporter,
    StatblockParseError,
)
from dndsim.rules.dnd5e_2014.sweep import (
    DEFAULT_CORPUS_DIRS,
    DEFAULT_MAX_COUNT,
    DEFAULT_MIN_COUNT,
    DEFAULT_PARTY_GLOB,
    CorpusSweepResult,
    CountSweepResult,
    SweepLoadError,
    corpus_sweep,
    count_sweep,
    party_corpus_sweep,
    render_corpus_sweep_report,
    render_count_sweep_report,
)
from dndsim.rules.exhaustion import exhaustion_rules
from dndsim.tools.srd_to_statblock import SrdToStatblockError
from dndsim.tools.srd_to_statblock import convert_file as convert_srd_file
from dndsim.tui.monitor import run_with_monitor
from dndsim.tui.progress import ProgressReporter, RunProgress

MONITOR_HELP = (
    "Attach the live run monitor (issue #56) — opt-in, off by default. "
    "Degrades cleanly with no monitor when stdout isn't a live terminal. "
    "Never changes report output."
)

app = typer.Typer(name="dndsim", help="Rules-agnostic Monte-Carlo combat simulation engine.")

# dndsim's own append-only audit log (issue #50).
# src/dndsim/cli.py -> parents[2] is utils/dndsim/.
DEFAULT_AUDIT_LOG = Path(__file__).resolve().parents[2] / "dndsim-audit.jsonl"

#: Issue #55: the Rules pack a run selects when its own caller passes no
#: ``--edition`` — 2024, matching ``combat.py``'s own
#: ``DEFAULT_EXHAUSTION_RULES_ID``. Every statblock this engine currently
#: compiles has ``exhaustion_level`` 0, so this default changes no existing
#: report's output.
DEFAULT_EDITION = "dnd5e_2024"


def _exhaustion_rules_id(edition: str) -> str:
    """``--edition dnd5e_2024`` -> ``"dnd5e_2024:rules/exhaustion"`` — the
    naming convention every Rules pack's own ``exhaustion.py`` registers
    under (`dnd5e_2014/exhaustion.py`, `dnd5e_2024/exhaustion.py`)."""
    return f"{edition}:rules/exhaustion"


@app.callback()
def _main() -> None:
    """Rules-agnostic Monte-Carlo combat simulation engine."""


@app.command("sim-combat")
def sim_combat(
    party: Annotated[
        str | None,
        typer.Argument(
            help='Party-side spec (X): a slug or path, "<slug>:<count>", a comma list of '
            'either, or the literal keyword "party" (expands --party-glob). Omit both X and '
            "Y to run the bundled walking-skeleton fixture."
        ),
    ] = None,
    enemies: Annotated[
        str | None,
        typer.Argument(help="Enemy-side spec (Y). Same grammar as X."),
    ] = None,
    party_glob: Annotated[
        str, typer.Option("--party-glob", help='Glob the "party" keyword expands to.')
    ] = DEFAULT_PARTY_GLOB,
    seed: Annotated[
        int | None,
        typer.Option(help="RNG seed; identical seed -> identical output. Omit to generate one."),
    ] = None,
    universes: Annotated[
        int, typer.Option("--universes", "-u", help="Number of Monte-Carlo universes per cell.")
    ] = 10_000,
    round_cap: Annotated[
        int, typer.Option("--round-cap", help="Max rounds before a matchup is scored a draw.")
    ] = 20,
    policy: Annotated[
        str,
        typer.Option(
            "--policy", help="Registered Policy id to select for this run (dndsim.policies)."
        ),
    ] = "dndsim:policy/greedy",
    edition: Annotated[
        str,
        typer.Option(
            "--edition",
            help=(
                "Rules pack to select for this run (dndsim.rules entry-point group), e.g. "
                "dnd5e_2014 or dnd5e_2024 (issue #55)."
            ),
        ),
    ] = DEFAULT_EDITION,
    adaptive: Annotated[
        bool,
        typer.Option(
            "--adaptive",
            help=(
                "Stop once the win-rate interval converges (within floor/cap) "
                "instead of running a fixed --universes batch."
            ),
        ),
    ] = False,
    adaptive_chunk: Annotated[
        int, typer.Option("--adaptive-chunk", help="Universes per adaptive chunk.")
    ] = 500,
    adaptive_floor: Annotated[
        int,
        typer.Option("--adaptive-floor", help="Minimum universes before stopping is considered."),
    ] = 500,
    adaptive_threshold: Annotated[
        float,
        typer.Option("--adaptive-threshold", help="Stop once the 95% CI half-width is <= this."),
    ] = 0.02,
    adaptive_cap: Annotated[
        int, typer.Option("--adaptive-cap", help="Maximum universes regardless of convergence.")
    ] = 10_000,
    audit_log: Annotated[
        Path, typer.Option("--audit-log", help="Append-only audit log path for this invocation.")
    ] = DEFAULT_AUDIT_LOG,
    no_audit_log: Annotated[
        bool, typer.Option("--no-audit-log", help="Suppress the audit line for this invocation.")
    ] = False,
    out: Annotated[
        Path | None, typer.Option("--out", help="Write the report here instead of stdout.")
    ] = None,
    monitor: Annotated[bool, typer.Option("--monitor", help=MONITOR_HELP)] = False,
    debug: Annotated[
        bool,
        typer.Option(
            "--debug",
            help=(
                "Print every compiled combatant's CompiledStatblock warnings (dropped/"
                "unmodeled actions), then a full run_combat event trace for universe 0, "
                "to stderr. Never changes report output."
            ),
        ),
    ] = False,
) -> None:
    """Run ``party`` (X) vs. ``enemies`` (Y) and print a markdown report
    (issue #67). X takes the party role and Y the enemy role regardless of
    what either page's own ``sim: side`` says. Omitting both X and Y runs
    the bundled walking-skeleton fixture (``rules/dnd5e_2014/fixture.py``'s
    ``PARTY_VS_ENEMIES_FIXTURE``) — the explicit no-argument default, not
    the only way to run this command; passing only one of X/Y is an error.
    """
    plugins.load_rules_packs()
    plugins.load_policies()

    if policy not in policies:
        typer.echo(f"dndsim sim-combat: unknown policy id: {policy!r}", err=True)
        raise typer.Exit(code=1)
    exhaustion_rules_id = _exhaustion_rules_id(edition)
    if exhaustion_rules_id not in exhaustion_rules:
        typer.echo(f"dndsim sim-combat: unknown edition: {edition!r}", err=True)
        raise typer.Exit(code=1)
    if (party is None) != (enemies is None):
        typer.echo(
            "dndsim sim-combat: pass both <X> and <Y>, or neither (to run the bundled "
            "fixture) — see utils/dndsim/README.md",
            err=True,
        )
        raise typer.Exit(code=1)

    seed_was_generated = seed is None
    if seed is None:
        seed = random_seed()

    if party is None:
        party_specs, enemy_specs = PARTY_VS_ENEMIES_FIXTURE
    else:
        assert enemies is not None  # enforced by the both-or-neither check above
        try:
            party_side = resolve_side(party, role="party", party_glob=party_glob)
            enemy_side = resolve_side(enemies, role="enemy", party_glob=party_glob)
        except SideSpecError as err:
            typer.echo(f"dndsim sim-combat: {err}", err=True)
            raise typer.Exit(code=1) from err
        party_specs = list(party_side.combatants)
        enemy_specs = list(enemy_side.combatants)

    party_label = ", ".join(c.entity.name for c in party_specs)
    enemy_label = ", ".join(c.entity.name for c in enemy_specs)
    monitor_label = f"sim-combat: {party_label} vs. {enemy_label}"
    started_at = time.perf_counter()
    debug_universe: int | None = None

    if debug:
        debug_universe = 0
        for spec in (*party_specs, *enemy_specs):
            if spec.compiled is None:
                typer.echo(f"[debug] {spec.entity.name}: no compiled kit (flat profile)", err=True)
            elif spec.compiled.warnings:
                for warning in spec.compiled.warnings:
                    typer.echo(f"[debug] {spec.entity.name}: {warning}", err=True)
            else:
                typer.echo(f"[debug] {spec.entity.name}: compiled kit, no warnings", err=True)

    if adaptive:
        config = AdaptiveConfig(
            chunk=adaptive_chunk,
            floor=adaptive_floor,
            threshold=adaptive_threshold,
            cap=adaptive_cap,
        )

        def run_adaptive_monitored(reporter: ProgressReporter) -> AdaptiveResult:
            # Chunks run sequentially in this thread (core/adaptive.py's own
            # contract), so accumulating successes/trials here mirrors
            # run_adaptive's internal accumulator exactly and lets each
            # chunk's win-rate interval be reported the instant it lands —
            # genuinely live, not a post-hoc replay.
            cumulative_successes = 0

            def run_chunk(start: int, size: int) -> int:
                nonlocal cumulative_successes
                chunk_batch = UniverseBatch(size=size, seed=substream_seed(seed, start))
                chunk_result = run_combat(
                    party_specs,
                    enemy_specs,
                    chunk_batch,
                    round_cap=round_cap,
                    policy_id=policy,
                    exhaustion_rules_id=exhaustion_rules_id,
                    debug_universe=debug_universe,
                )
                successes = round(chunk_result.party_win_rate * size)
                cumulative_successes += successes
                cumulative_trials = start + size
                reporter.report(
                    RunProgress(
                        label=monitor_label,
                        iterations_done=cumulative_trials,
                        iterations_target=config.cap,
                        win_ci=wilson_interval(cumulative_successes, cumulative_trials),
                        started_at=started_at,
                    )
                )
                return successes

            return run_adaptive(run_chunk, config)

        adaptive_result = run_with_monitor(
            run_adaptive_monitored, enabled=monitor, label=monitor_label
        )
        wall_ms = (time.perf_counter() - started_at) * 1000
        interval = adaptive_result.interval
        assert interval.p is not None and interval.lo is not None and interval.hi is not None
        report_lines = [
            "# Combat simulation report (adaptive)",
            "",
            f"- **Engine**: dndsim v{__version__}",
            f"- **Seed**: {seed}",
            f"- **Adaptive**: chunk={config.chunk}, floor={config.floor}, "
            f"threshold={config.threshold}, cap={config.cap}",
            "",
            f"## {party_label} vs. {enemy_label}",
            "",
            "| Metric | Value |",
            "|---|---|",
            f"| {party_label} win rate | {interval.p:.1%} |",
            f"| 95% CI | [{interval.lo:.1%}, {interval.hi:.1%}] |",
            f"| Trials run | {adaptive_result.trials:,} |",
            f"| Stopped early | {adaptive_result.stopped_early} |",
            "",
            f"**Policy**: {policy}",
            f"**Edition**: {edition}",
            "",
        ]
        report = "\n".join(report_lines)
        cell_lines = [
            {
                "trials": adaptive_result.trials,
                "successes": adaptive_result.successes,
                "winCi": {"p": interval.p, "lo": interval.lo, "hi": interval.hi},
                "stoppedEarly": adaptive_result.stopped_early,
            }
        ]
        totals = {"cells": 1, "universes": adaptive_result.trials, "wallMs": wall_ms}
    else:
        # A single fixed-size batch has no intermediate chunk boundary to
        # report progress at (run_combat resolves it in one call) — the
        # monitor still attaches and shows an indeterminate bar plus the
        # elapsed clock, so a slow fixed batch is still distinguishable
        # from a genuinely hung process even without incremental progress.
        batch = UniverseBatch(size=universes, seed=seed)

        def run_fixed(reporter: ProgressReporter) -> CombatResult:
            reporter.report(
                RunProgress(
                    label=monitor_label,
                    iterations_target=universes,
                    started_at=started_at,
                )
            )
            return run_combat(
                party_specs,
                enemy_specs,
                batch,
                round_cap=round_cap,
                policy_id=policy,
                exhaustion_rules_id=exhaustion_rules_id,
                debug_universe=debug_universe,
            )

        result = run_with_monitor(run_fixed, enabled=monitor, label=monitor_label)
        wall_ms = (time.perf_counter() - started_at) * 1000
        report = render_combat_report(result) + f"**Policy**: {policy}\n**Edition**: {edition}\n"
        cell_lines = [
            {
                "index": 0,
                "seed": seed,
                "partyWinRate": result.party_win_rate,
                "enemyWinRate": result.enemy_win_rate,
                "universes": result.universes,
            }
        ]
        totals = {"cells": 1, "universes": result.universes, "wallMs": wall_ms}

    if seed_was_generated:
        report += f"**Seed generated**: {seed}\n"

    if out is not None:
        out.write_text(report)
    else:
        typer.echo(report)

    if not no_audit_log:
        line = build_audit_line(
            engine_version=__version__,
            seed=seed,
            argv=sys.argv[1:],
            subject={
                "party": party_label,
                "enemies": enemy_label,
                "partySpec": party,
                "enemySpec": enemies,
                "policy": policy,
                "edition": edition,
                "adaptive": adaptive,
            },
            totals=totals,
            cells=cell_lines,
            report_text=report,
        )
        append_audit_line(audit_log, line)


@app.command("parse")
def parse_cmd(
    files: Annotated[
        list[Path], typer.Argument(help="Statblock-bearing markdown file(s) to parse.")
    ],
    json_output: Annotated[
        bool, typer.Option("--json", help="Emit normalized content as JSON instead of a summary.")
    ] = False,
) -> None:
    """Parse each file's native statblock fence and print the normalized content.

    Scope is the native fence keys only (name, ac, hp, stats, saves, damage
    tags, cr, speed, senses) — ADR-0009. A missing required key or an
    unparseable value raises naming the offending field; an empty fence is
    a stub page, reported as such rather than as an error.
    """
    plugins.load_rules_packs()
    importer = StatblockImporter()

    parsed: list[tuple[Path, StatblockContent | None]] = []
    for path in files:
        text = path.read_text()
        try:
            content = importer.parse(text, str(path))
        except StatblockParseError as err:
            typer.echo(f"dndsim parse: {err}", err=True)
            raise typer.Exit(code=1) from err
        parsed.append((path, content))

    if json_output:
        payload = [
            {
                "path": str(path),
                "content": content.model_dump(mode="json") if content is not None else None,
            }
            for path, content in parsed
        ]
        typer.echo(json.dumps(payload, indent=2))
        return

    for path, content in parsed:
        if content is None:
            typer.echo(f"{path}: (stub — empty statblock fence)")
        else:
            typer.echo(
                f"{path}: {content.name} — AC {content.ac}, HP {content.hp}, CR {content.cr}"
            )


@app.command("convert-srd")
def convert_srd_cmd(
    files: Annotated[
        list[Path], typer.Argument(help="SRD bullet+table monster page(s) to convert.")
    ],
    write: Annotated[bool, typer.Option("--write", help="Apply the conversion in place.")] = False,
) -> None:
    """Convert an SRD monster page's bullet+table stat block into a native
    ```statblock fence, verbatim (issue #55). Prints the converted page to
    stdout by default; ``--write`` applies it in place. Verbatim structural
    extraction only — never rewords, never invents a number."""
    for path in files:
        try:
            rendered = convert_srd_file(path, write=write)
        except SrdToStatblockError as err:
            typer.echo(f"dndsim convert-srd: {err}", err=True)
            raise typer.Exit(code=1) from err
        if write:
            typer.echo(f"dndsim convert-srd: wrote {path}")
        else:
            typer.echo(rendered)


@app.command("lint")
def lint_cmd(
    files: Annotated[
        list[Path] | None,
        typer.Argument(
            help="Statblock/character-sheet file(s) to lint. Default: the full scoped corpus."
        ),  # noqa: E501
    ] = None,
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Emit markdownlint-obsidian-shaped JSON instead of a summary."),
    ] = False,
) -> None:
    """Lint every statblock and character-sheet combatant-sheet page dndsim owns (ADR-0010).

    The parser IS the validator: a ```statblock fence that won't parse, or an
    action whose prose drifted off the SRD attack grammar the sim reads, or a
    character-sheet page missing a valid party-side Combatant Block, fails
    here rather than silently producing a wrong report later.

    ``--json`` emits the same payload shape
    ``markdownlint-obsidian --output-formatter json`` emits — one entry per
    file, ``errors: []`` for a clean file — so
    ``utils/scripts/lib/lint-findings.mjs`` can merge this producer's
    findings with markdownlint-obsidian's before the one lint ratchet
    (docs/adr/0005, docs/adr/0006) evaluates them.
    """
    plugins.load_rules_packs()
    payload = lint_paths(files)
    total = 0
    for entry in payload:
        errors = entry["errors"]
        assert isinstance(errors, list)
        total += len(errors)

    if json_output:
        typer.echo(json.dumps(payload, indent=2))
        raise typer.Exit(code=1 if total > 0 else 0)

    for entry in payload:
        errors = entry["errors"]
        assert isinstance(errors, list)
        for err in errors:
            location = f"{entry['filePath']}:{err['line']}"
            typer.echo(f"{location} {err['ruleName']}/{err['ruleCode']}: {err['message']}")
    if total == 0:
        typer.echo("dndsim lint: clean.")
        raise typer.Exit(code=0)
    typer.echo(f"dndsim lint: {total} finding(s).")
    raise typer.Exit(code=1)


@app.command("profile")
def profile_cmd(
    path: Annotated[
        Path, typer.Argument(help="Markdown file with a ```statblock fence to profile.")
    ],
    ac_min: Annotated[
        int, typer.Option("--ac-min", help="Lowest AC in the closed-form hit-chance/DPR sweep.")
    ] = 10,
    ac_max: Annotated[
        int, typer.Option("--ac-max", help="Highest AC in the closed-form hit-chance/DPR sweep.")
    ] = 20,
    attack_bonus_min: Annotated[
        int,
        typer.Option(
            "--attack-bonus-min", help="Lowest incoming attack bonus in the be-hit/EHP sweep."
        ),
    ] = 2,
    attack_bonus_max: Annotated[
        int,
        typer.Option(
            "--attack-bonus-max", help="Highest incoming attack bonus in the be-hit/EHP sweep."
        ),
    ] = 10,
    iterations: Annotated[
        int,
        typer.Option("--iterations", help="Monte Carlo samples per AC for the DPR distribution."),
    ] = 2000,
    seed: Annotated[
        int | None,
        typer.Option(
            help="RNG seed for the DPR distribution; identical seed -> identical output. "
            "Omit to generate one."
        ),
    ] = None,
    audit_log: Annotated[
        Path, typer.Option("--audit-log", help="Append-only audit log path for this invocation.")
    ] = DEFAULT_AUDIT_LOG,
    no_audit_log: Annotated[
        bool, typer.Option("--no-audit-log", help="Suppress the audit line for this invocation.")
    ] = False,
    out: Annotated[
        Path | None, typer.Option("--out", help="Write the report here instead of stdout.")
    ] = None,
) -> None:
    """Profile one character with no opposition: exact closed-form hit
    chance across an AC ladder, a sampled damage-per-round distribution,
    exact closed-form chance to be hit, and effective hit points.
    """
    plugins.load_rules_packs()

    if ac_max < ac_min:
        typer.echo("dndsim profile: --ac-max must be >= --ac-min", err=True)
        raise typer.Exit(code=1)
    if attack_bonus_max < attack_bonus_min:
        typer.echo("dndsim profile: --attack-bonus-max must be >= --attack-bonus-min", err=True)
        raise typer.Exit(code=1)

    seed_was_generated = seed is None
    if seed is None:
        seed = random_seed()

    text = path.read_text()
    try:
        statblock, block = load_compiled_statblock(text, str(path))
    except (StatblockParseError, ProfileError) as err:
        typer.echo(f"dndsim profile: {err}", err=True)
        raise typer.Exit(code=1) from err

    pc_profile = build_pc_profile(
        statblock,
        block,
        ac_sweep=list(range(ac_min, ac_max + 1)),
        attack_bonus_sweep=list(range(attack_bonus_min, attack_bonus_max + 1)),
        iterations=iterations,
        seed=seed,
    )
    report = render_pc_profile_report(pc_profile, seed=seed, iterations=iterations)
    if seed_was_generated:
        report += f"**Seed generated**: {seed}\n"

    if out is not None:
        out.write_text(report)
    else:
        typer.echo(report)

    if not no_audit_log:
        line = build_audit_line(
            engine_version=__version__,
            seed=seed,
            argv=sys.argv[1:],
            subject={"path": str(path), "name": pc_profile.name},
            totals={"iterations": iterations, "acRange": [ac_min, ac_max]},
            report_text=report,
        )
        append_audit_line(audit_log, line)


@app.command("sweep-corpus")
def sweep_corpus_cmd(
    subject: Annotated[
        str,
        typer.Argument(
            help='Path to a statblock/character-sheet page, or the literal keyword "party" to '
            "sweep every PC in --party-glob and concatenate their reports."
        ),
    ],
    corpus_dir: Annotated[
        list[Path] | None,
        typer.Option("--corpus-dir", help="Corpus directory (repeatable)."),
    ] = None,
    party_glob: Annotated[
        str, typer.Option("--party-glob", help='Glob "party" expands to.')
    ] = DEFAULT_PARTY_GLOB,
    seed: Annotated[
        int | None,
        typer.Option(help="RNG seed; identical seed -> identical output. Omit to generate one."),
    ] = None,
    universes: Annotated[
        int, typer.Option("--universes", "-u", help="Monte-Carlo universes per cell.")
    ] = 10_000,
    round_cap: Annotated[
        int, typer.Option("--round-cap", help="Max rounds before a matchup is scored a draw.")
    ] = 20,
    policy: Annotated[
        str,
        typer.Option(
            "--policy", help="Registered Policy id to select for this run (dndsim.policies)."
        ),
    ] = "dndsim:policy/greedy",
    workers: Annotated[
        int,
        typer.Option(
            "--workers",
            help="Thread count across sweep cells (one per opponent); never changes output.",
        ),
    ] = 1,
    audit_log: Annotated[
        Path, typer.Option("--audit-log", help="Append-only audit log path for this invocation.")
    ] = DEFAULT_AUDIT_LOG,
    no_audit_log: Annotated[
        bool, typer.Option("--no-audit-log", help="Suppress the audit line for this invocation.")
    ] = False,
    out: Annotated[
        Path | None, typer.Option("--out", help="Write the report here instead of stdout.")
    ] = None,
    monitor: Annotated[bool, typer.Option("--monitor", help=MONITOR_HELP)] = False,
) -> None:
    """Sweep one subject against every creature in the corpus, one
    independently-seeded cell per opponent (issue #53). ``subject`` the
    literal keyword ``party`` chains one sweep per PC in ``--party-glob``
    and concatenates their reports.
    """
    plugins.load_rules_packs()
    plugins.load_policies()

    if policy not in policies:
        typer.echo(f"dndsim sweep-corpus: unknown policy id: {policy!r}", err=True)
        raise typer.Exit(code=1)

    seed_was_generated = seed is None
    if seed is None:
        seed = random_seed()

    dirs = tuple(corpus_dir) if corpus_dir else DEFAULT_CORPUS_DIRS
    monitor_label = f"sweep-corpus: {subject}"
    started_at = time.perf_counter()

    def run_sweep(
        reporter: ProgressReporter,
    ) -> tuple[list[CorpusSweepResult], list[str]]:
        def on_progress(done: int, total: int, _name: str) -> None:
            reporter.report(
                RunProgress(
                    label=monitor_label,
                    cells_done=done,
                    cells_total=total,
                    started_at=started_at,
                )
            )

        if subject.strip() == "party":
            pc_paths = sorted(Path(p) for p in glob.glob(party_glob))
            if not pc_paths:
                typer.echo(
                    f'dndsim sweep-corpus: --party-glob "{party_glob}" matched no files', err=True
                )
                raise typer.Exit(code=1)
            sweep_results, warnings = party_corpus_sweep(
                pc_paths,
                corpus_dirs=dirs,
                seed=seed,
                universes=universes,
                round_cap=round_cap,
                policy_id=policy,
                max_workers=workers,
                on_progress=on_progress,
            )
            if not sweep_results:
                typer.echo(
                    f"dndsim sweep-corpus: every PC in {party_glob!r} failed to compile: "
                    f"{'; '.join(warnings)}",
                    err=True,
                )
                raise typer.Exit(code=1)
            return sweep_results, warnings
        return [
            corpus_sweep(
                Path(subject),
                corpus_dirs=dirs,
                seed=seed,
                universes=universes,
                round_cap=round_cap,
                policy_id=policy,
                max_workers=workers,
                on_progress=on_progress,
            )
        ], []

    try:
        results, party_warnings = run_with_monitor(run_sweep, enabled=monitor, label=monitor_label)
    except (StatblockParseError, ProfileError, SweepLoadError) as err:
        typer.echo(f"dndsim sweep-corpus: {err}", err=True)
        raise typer.Exit(code=1) from err

    for warning in party_warnings:
        typer.echo(f"dndsim sweep-corpus: WARN {warning}", err=True)

    report = "\n\n".join(render_corpus_sweep_report(r, policy=policy) for r in results)
    if seed_was_generated:
        report += f"**Seed generated**: {seed}\n"

    if out is not None:
        out.write_text(report)
    else:
        typer.echo(report)

    if not no_audit_log:
        cell_lines = [
            {
                "subject": r.subject,
                "opponent": c.opponent,
                "path": c.path,
                "seed": c.seed,
                "partyWinRate": c.result.party_win_rate,
                "band": c.rating.band,
            }
            for r in results
            for c in r.cells
        ]
        totals = {
            "cells": sum(r.cell_count for r in results),
            "universes": sum(r.total_universes for r in results),
            "wallMs": sum(r.wall_ms for r in results),
        }
        line = build_audit_line(
            engine_version=__version__,
            seed=seed,
            argv=sys.argv[1:],
            subject={"subject": subject, "corpusDirs": [str(d) for d in dirs], "policy": policy},
            totals=totals,
            cells=cell_lines,
            report_text=report,
        )
        append_audit_line(audit_log, line)


@app.command("sweep-count")
def sweep_count_cmd(
    party: Annotated[
        str,
        typer.Argument(
            help="Comma-separated path(s) to the fixed party-side page(s) (typically PC sheets)."
        ),
    ],
    monster: Annotated[
        Path, typer.Argument(help="Path to the single monster page whose count is swept.")
    ],
    seed: Annotated[
        int | None,
        typer.Option(help="RNG seed; identical seed -> identical output. Omit to generate one."),
    ] = None,
    universes: Annotated[
        int, typer.Option("--universes", "-u", help="Monte-Carlo universes per cell.")
    ] = 10_000,
    min_count: Annotated[int, typer.Option("--min-count", help="Swept range floor.")] = (
        DEFAULT_MIN_COUNT
    ),
    max_count: Annotated[int, typer.Option("--max-count", help="Swept range ceiling.")] = (
        DEFAULT_MAX_COUNT
    ),
    round_cap: Annotated[
        int, typer.Option("--round-cap", help="Max rounds before a matchup is scored a draw.")
    ] = 20,
    policy: Annotated[
        str,
        typer.Option(
            "--policy", help="Registered Policy id to select for this run (dndsim.policies)."
        ),
    ] = "dndsim:policy/greedy",
    workers: Annotated[
        int,
        typer.Option(
            "--workers",
            help="Thread count across the known [min-count, max-count] cells; never changes "
            "output.",
        ),
    ] = 1,
    audit_log: Annotated[
        Path, typer.Option("--audit-log", help="Append-only audit log path for this invocation.")
    ] = DEFAULT_AUDIT_LOG,
    no_audit_log: Annotated[
        bool, typer.Option("--no-audit-log", help="Suppress the audit line for this invocation.")
    ] = False,
    out: Annotated[
        Path | None, typer.Option("--out", help="Write the report here instead of stdout.")
    ] = None,
    monitor: Annotated[bool, typer.Option("--monitor", help=MONITOR_HELP)] = False,
) -> None:
    """Fixed party vs. a swept count of one monster type — "how many should
    I throw at them" (issue #53). Reports the smallest count reaching each
    difficulty band, then the full count matrix.
    """
    plugins.load_rules_packs()
    plugins.load_policies()

    if policy not in policies:
        typer.echo(f"dndsim sweep-count: unknown policy id: {policy!r}", err=True)
        raise typer.Exit(code=1)
    if min_count < 1:
        typer.echo("dndsim sweep-count: --min-count must be >= 1", err=True)
        raise typer.Exit(code=1)
    if max_count < min_count:
        typer.echo("dndsim sweep-count: --max-count must be >= --min-count", err=True)
        raise typer.Exit(code=1)

    seed_was_generated = seed is None
    if seed is None:
        seed = random_seed()

    party_paths = [Path(p.strip()) for p in party.split(",") if p.strip() != ""]
    if not party_paths:
        typer.echo("dndsim sweep-count: party must name at least one page", err=True)
        raise typer.Exit(code=1)

    monitor_label = f"sweep-count: {monster}"
    started_at = time.perf_counter()

    def run_sweep(reporter: ProgressReporter) -> CountSweepResult:
        def on_progress(done: int, total: int, _name: str) -> None:
            reporter.report(
                RunProgress(
                    label=monitor_label,
                    cells_done=done,
                    cells_total=total,
                    started_at=started_at,
                )
            )

        return count_sweep(
            party_paths,
            monster,
            seed=seed,
            universes=universes,
            min_count=min_count,
            max_count=max_count,
            round_cap=round_cap,
            policy_id=policy,
            max_workers=workers,
            on_progress=on_progress,
        )

    try:
        result = run_with_monitor(run_sweep, enabled=monitor, label=monitor_label)
    except (StatblockParseError, ProfileError, SweepLoadError) as err:
        typer.echo(f"dndsim sweep-count: {err}", err=True)
        raise typer.Exit(code=1) from err

    report = render_count_sweep_report(result, policy=policy)
    if seed_was_generated:
        report += f"**Seed generated**: {seed}\n"

    if out is not None:
        out.write_text(report)
    else:
        typer.echo(report)

    if not no_audit_log:
        cell_lines = [
            {
                "count": c.count,
                "seed": c.seed,
                "partyWinRate": c.result.party_win_rate,
                "band": c.rating.band,
            }
            for c in result.cells
        ]
        totals = {
            "cells": len(result.cells),
            "universes": result.total_universes,
            "wallMs": result.wall_ms,
        }
        line = build_audit_line(
            engine_version=__version__,
            seed=seed,
            argv=sys.argv[1:],
            subject={
                "party": [str(p) for p in party_paths],
                "monster": str(monster),
                "policy": policy,
            },
            totals=totals,
            cells=cell_lines,
            report_text=report,
        )
        append_audit_line(audit_log, line)


if __name__ == "__main__":
    app()
