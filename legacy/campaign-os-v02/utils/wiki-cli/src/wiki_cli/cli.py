from __future__ import annotations

import json
import uuid
from dataclasses import replace
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

import typer

from wiki_cli import baseline, db
from wiki_cli import bench as _bench
from wiki_cli import drain as _drain
from wiki_cli import rules as _rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.config import Config, load_config
from wiki_cli.contracts import (
    TIER_ORDER,
    BaseRule,
    Finding,
    ProducerRuleDoc,
    all_rules,
)
from wiki_cli.orchestrator import LintResult, rel_path, run_lint
from wiki_cli.producers import all_rule_docs
from wiki_cli.report import GUIDE_DIR, finding_to_json, render
from wiki_cli.report import exit_code as _lint_exit_code

app = typer.Typer(add_completion=False, no_args_is_help=True)

debt_app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="Debt-floor maintenance (ADR-0062). `accept` raises every floor to "
    "today's live counts and is orchestrator/human only, never part of a "
    "fixing agent's task; `check` gates a commit. The read-only triage view "
    "is `wiki drain --over`.",
)
app.add_typer(debt_app, name="debt")

links_app = typer.Typer(add_completion=False, no_args_is_help=True, help="Link-graph reports.")
app.add_typer(links_app, name="links")

baseline_app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="Ratchet floor maintenance (ADR-0062). `accept` raises every floor to "
    "today's live counts and is orchestrator/human only; `check` gates a commit.",
)
app.add_typer(baseline_app, name="baseline")


@app.callback()
def main() -> None:
    """wiki — Campaign OS llm-wiki CLI (ADR-0041)."""


_HELP_TEXT = """\
wiki-cli — vault linter and wiki tools

COMMANDS
  wiki lint PATHS...             Lint the named files/directories — the edit loop
    --rule RULE                  Display-filter to this rule id (repeatable)
    --only RULE|PRODUCER         Execution-gating (repeatable): runs only this rule's/producer's
                                  producer; always prints a timing footer
    --dndsim                     Include the dndsim statblock/combatant-block producer
    --quiet                      Minimal output: finding count only
    --json                       NDJSON output (one JSON object per finding); never autofixes
    --no-fix / --dry-run         Report mechanical defects instead of repairing them
    --all                        Show every hit; disable per-rule/output caps and
                                  baseline suppression
    --rules                      List every reportable rule id (registered rules plus
                                  external-producer families), tier, and fix line; exit 0

  wiki sweep                     Full corpus: every rule and producer including the
                                  cross-file ones, autofix, cache gc, dispatch manifest
    --dndsim --quiet --json --all --no-fix / --dry-run   As for `wiki lint`

  wiki list                      List vault pages with structural filtering/sorting
    --where KEY<OP>VALUE          Filter: = != ~ >= <= (repeatable)
    --sort KEY                    Sort key; prefix with - for descending
    --format FORMAT               tsv (default), json, or paths
    --columns A,B,C               Comma-separated column list
    --include-templates           Include vault/_templates/ pages
    --limit N                     Max rows to return

  wiki search QUERY              Semantic search via qmd with structural post-filters
    -c, --collection NAME        Collection to search (repeatable; default: content)
    --xml                        Raw qmd XML passthrough (incompatible with
                                  --where/--sort/--columns/--format)
    --where KEY<OP>VALUE          Filter: = != ~ >= <= (repeatable)
    --sort KEY                    Sort key; prefix with - for descending (default: -score)
    --format FORMAT               tsv (default), json, or paths
    --columns A,B,C               Comma-separated column list (default: path,type,score,collection)
    --include-templates           Include vault/_templates/ pages
    --limit N                     Max rows to return (default: 20)

  wiki links in PAGE             Pages linking TO this page (backlinks)
  wiki links out PAGE            Pages this page links to (outlinks)
  wiki links breakdown           Per-target backlink counts
    --to KEY<OP>VALUE             Target filter (repeatable, required)
    --from KEY<OP>VALUE           Source filter (repeatable)
  wiki links orphans             Pages with zero backlinks
  wiki links redundant           Same-section repeated wikilinks
    --where KEY<OP>VALUE          Filter (repeatable)
  wiki links spread              Under-represented targets for placement variety
    --to KEY<OP>VALUE             Target filter (repeatable, required)
    --from KEY<OP>VALUE           Source filter (repeatable, required)
  (wiki links common flags)
    --format FORMAT               tsv (default), json, or paths
    --columns A,B,C               Column list
    --sort KEY                    Sort key
    --limit N                     Max rows
    --include-templates           Include template pages

  wiki drain                     The debt queue from the last sweep's cache, worst
                                  offenders first (stale cache is fine — this is a queue)
    --rule RULE                  Only findings from these rule ids (repeatable)
    --path GLOB                  Only rel_paths matching this glob, e.g. 'vault/npcs/*'
    --limit N                    Show at most this many files
    --over                       Triage view: every (file, rule) pair above its floor
                                  with its delta, grouped by rule (runs a full corpus pass)
    --claim N                    Atomically claim the top N unclaimed files; prints only
                                  their rel_paths
    --agent-id ID                Claim/release owner; defaults to a fresh UUID on --claim
    --claims                     List active (non-expired) claims: key, owner, expires_at
    --release PATH               Release the claim on PATH
    --release-all                Release every claim

  wiki explain RULE              Print this rule's guide page from vault/refs/lint/

  wiki slug-scrub                Rewrite path-qualified wikilinks ([[path/to/slug|...]]) to
                                  slug-only ([[slug|...]]) across vault/ in one pass
    --dry-run                    Report rewrites without writing files
                                  (also available as `npm run vault:slug-scrub`)

  wiki bench                     Cold+warm full-vault sweep timing; appends one entry to
                                  .claude/.wiki-bench.jsonl and flags a >25% regression

  wiki debt accept --force       Raise every floor to current live counts from a full
                                  corpus pass (orchestrator/human only; refuses without --force)
  wiki debt check                Exit 1 if any live warning-severity count exceeds its
                                  floor (full corpus pass); exit 0 otherwise

EXAMPLES
  wiki lint vault/npcs/barnaby-rook.md       Single file
  wiki sweep                                 Whole corpus, dispatch manifest
  wiki lint vault/npcs --only W25            Only run W25's rule+producer
  wiki lint vault/npcs --all                 Show baselined debt too, uncapped
  wiki lint vault/npcs --json | jq '.rule'   Pipe findings to jq
  wiki explain W86                           What W86 wants and how to satisfy it
  wiki drain --limit 10                      Top 10 debt targets
  wiki drain --over                          Which (file, rule) pairs are over floor?
  wiki drain --claim 5                       Claim 5 files for a dispatch wave
  wiki debt accept --force                   Re-freeze the floor after a drain wave
  wiki list --where type=npc --format paths  All NPC pages
  wiki list --sort -links-in --limit 10      Top 10 most-linked pages
  wiki search "umberlee" --where type=location  Location pages matching query
  wiki search "umberlee" --xml               Raw qmd XML output
  wiki links in umberlee --format paths       Who links to Umberlee?
  wiki links orphans --where type=npc         Unlinked NPCs
  wiki links breakdown --to type=shop --from type=item  Shop link distribution
"""


@app.command("help")
def help_cmd() -> None:
    """Agent-optimized reference for all wiki-cli commands and their flags."""
    typer.echo(_HELP_TEXT)


def _load_config(command: str) -> Config:
    """`load_config()` with the CLI's usage/config exit code (2) on failure,
    named for the command the user ran."""
    try:
        return load_config()
    except Exception as error:
        typer.echo(f"wiki {command}: config error: {error}", err=True)
        raise typer.Exit(code=2) from error


def _git_root(repo_root: Path) -> Path:
    """The real repo root — the directory containing `.git`. When
    `config.repo_root` is `utils/wiki-cli/` (wiki.toml found there), go up
    two levels; when it's already the git root (`.git` found there), return
    as-is."""
    resolved = repo_root.resolve()
    if (resolved / ".git").exists():
        return resolved
    return resolved.parents[1]


def _is_template_path(path: Path, vault_root: Path) -> bool:
    try:
        rel = path.resolve().relative_to(vault_root.resolve())
    except ValueError:
        return False
    return rel.parts[:1] == ("_templates",)


def _collect_targets(
    config_repo_root: Path, vault_root: Path, paths: list[str] | None
) -> list[Path]:
    if paths:
        git_root = _git_root(config_repo_root)
        resolved: list[Path] = []
        missing: list[str] = []
        for p in paths:
            candidate = Path(p)
            # Repo-root-relative resolution wins over raw-cwd for a
            # relative PATH: `uv run --directory utils/wiki-cli` (the
            # hooks' own invocation form) runs this process with cwd
            # already inside utils/wiki-cli, which itself has files like
            # CLAUDE.md/README.md/pyproject.toml — checking `candidate.
            # exists()` first would silently lint THOSE instead of the
            # caller's intended repo-root-relative target. An absolute
            # PATH is unambiguous and always wins.
            if candidate.is_absolute():
                target = candidate.resolve()
            elif (git_root / p).exists():
                target = (git_root / p).resolve()
            elif candidate.exists():
                target = candidate.resolve()
            else:
                # Nothing on disk answers to this PATH. Collected rather
                # than resolved-and-appended: a nonexistent target is
                # dropped silently downstream, so the run reported
                # "0 files — clean" and exited 0. A typo, or a shell that
                # did not word-split a variable of paths, then reads as a
                # passing verification.
                missing.append(p)
                continue
            if target.is_dir():
                resolved.extend(sorted(target.rglob("*.md")))
            else:
                resolved.append(target)
        if missing:
            typer.echo(
                "wiki lint: no such path: " + ", ".join(missing),
                err=True,
            )
            raise typer.Exit(code=2)
        return resolved
    return sorted(p for p in vault_root.rglob("*.md") if not _is_template_path(p, vault_root))



def _apply_display_filters(result: LintResult, *, rules: list[str] | None, producer: str | None = None, severity: str | None = None) -> LintResult:
    """Narrow `result.findings` to the rule ids, producer, or severity `--rule`/`--producer`/`--severity` asked to see.
    Display-only (ADR-0023): the caller computes the exit code from the
    pre-filter `result`, never from this one. `stats` passes through
    unchanged — it describes the real run, not the filtered view of it."""
    filtered = result.findings
    if rules:
        allowed = set(rules)
        filtered = [f for f in filtered if f.rule_id in allowed]
    if producer:
        filtered = [f for f in filtered if f.producer == producer]
    if severity:
        filtered = [f for f in filtered if f.severity.value == severity]
    if not (rules or producer or severity):
        return result
    return replace(result, findings=filtered)


def _resolve_only(only_values: list[str]) -> tuple[list[str], list[str] | None]:
    """Resolve `--only` values into `(producers, rule_filter)`.

    A value matching a registered rule id (`all_rules()`, e.g. `"W25"`)
    resolves to that rule's own `producer` for execution gating and is
    added to the display `rule_filter`. A value matching no rule id is
    passed straight through as a producer identifier for gating — the
    same string `run_lint`'s `producers` param already understands
    (`"wiki"` for every native rule, or an external producer's own family
    id, e.g. `"W86"`/`"W87"`) — and adds nothing to `rule_filter`, since
    it names a producer's whole output rather than one rule."""
    rule_by_id = {rule.id: rule for rule in all_rules()}
    producers: list[str] = []
    rule_filter: list[str] = []
    for value in only_values:
        rule = rule_by_id.get(value)
        if rule is not None:
            if rule.producer not in producers:
                producers.append(rule.producer)
            rule_filter.append(value)
        elif value not in producers:
            producers.append(value)
    return producers, (rule_filter or None)


def _only_timing_footer(result: LintResult, producers: list[str]) -> str:
    """`--only`'s always-on timing footer (printed to stderr): the run's
    own summary line plus one line per producer it ran, reading
    `result.stats.per_producer_seconds`."""
    lines = [
        (
            f"LINT {result.stats.files} files — {len(result.findings)} findings"
            f" · {result.stats.seconds:.1f}s"
        )
    ]
    for producer_id in producers:
        seconds = result.stats.per_producer_seconds.get(producer_id, 0.0)
        count = sum(1 for f in result.findings if f.producer == producer_id)
        lines.append(f"  {producer_id}: {seconds:.1f}s  ({count} findings)")
    return "\n".join(lines)


def _print_rules() -> None:
    """Every id that can appear in a report: the registered rule classes,
    then the ids external producers emit under their own `RULE_DOCS` (a
    producer is a plain function, so its ids never reach `all_rules()`)."""
    entries: list[BaseRule | ProducerRuleDoc] = [*all_rules(), *all_rule_docs().values()]
    for entry in sorted(entries, key=lambda e: (TIER_ORDER.index(e.tier), e.id)):
        typer.echo(f"{entry.id}  {entry.tier.value}  {entry.severity.value}  {entry.fix}")


def _emit(
    result: LintResult,
    git_root: Path,
    *,
    as_json: bool,
    all_hits: bool,
    quiet: bool,
    rules: list[str] | None,
    sweep: bool,
) -> LintResult:
    """Print one run's report — NDJSON or the instruction list — and return
    the display view of it, which `--only`'s timing footer then describes."""
    display_result = _apply_display_filters(result, rules=rules)

    if as_json:
        # NDJSON is the machine surface: it carries every finding, floored
        # or not, so downstream tooling sees the unfiltered truth.
        for finding in display_result.findings:
            typer.echo(json.dumps(finding_to_json(finding)))
        return display_result

    # `--all` is the escape hatch that shows baselined debt too.
    # `display_result` itself is left intact — the `--only` timing footer
    # describes the real run, not this view of it.
    suppressed = 0
    rendered = display_result
    if not all_hits:
        shown, suppressed = baseline.partition(git_root, display_result.findings)
        rendered = replace(display_result, findings=shown)
    typer.echo(
        render(rendered, all_hits=all_hits, quiet=quiet, suppressed=suppressed, sweep=sweep)
    )
    return display_result


@app.command()
def lint(
    paths: Annotated[
        list[str] | None,
        typer.Argument(help="Files or directories to lint. Required — the whole corpus is `wiki sweep`."),
    ] = None,
    as_json: Annotated[
        bool, typer.Option("--json", help="One JSON object per finding, newline-delimited.")
    ] = False,
    all_hits: Annotated[
        bool,
        typer.Option(
            "--all",
            help="Show every hit — disables the per-rule/output caps and baseline suppression.",
        ),
    ] = False,
    rule: Annotated[
        list[str] | None,
        typer.Option("--rule", help="Show only these rule ids (repeatable). Display-only."),
    ] = None,
    quiet: Annotated[
        bool, typer.Option("--quiet", help="Minimal output: finding count only.")
    ] = False,
    list_rules: Annotated[
        bool, typer.Option("--rules", help="List registered rules, tiers, and fix lines; exit 0.")
    ] = False,
    dndsim: Annotated[bool, typer.Option("--dndsim", help="Include dndsim findings.")] = False,
    only: Annotated[
        list[str] | None,
        typer.Option(
            "--only",
            help="Execution-gating (repeatable): a rule id (e.g. W25) runs only its "
            "producer and filters display to that rule; a producer name (e.g. wiki, "
            "W86) runs only that producer. Always prints timing.",
        ),
    ] = None,
    no_fix: Annotated[
        bool,
        typer.Option(
            "--no-fix",
            "--dry-run",
            help="Report mechanical defects instead of repairing them (dry run).",
        ),
    ] = False,
) -> None:
    """Lint PATHS — the scoped edit loop. Cross-file (SWEEP) producers are
    skipped silently here; the whole corpus is `wiki sweep` (ADR-0064)."""
    if list_rules:
        _print_rules()
        raise typer.Exit(code=0)

    if not paths:
        # Predictable surface (ADR-0064): `lint` is the scoped edit loop and
        # `sweep` is the corpus. A bare `lint` that silently swept the vault
        # cost ~7 minutes to callers who meant one file.
        typer.echo("usage: wiki lint <paths> — full corpus is: wiki sweep", err=True)
        raise typer.Exit(code=2)

    config = _load_config("lint")
    vault_root = config.vault_root.resolve()
    targets = _collect_targets(config.repo_root, vault_root, paths)

    only_producers, only_rule_filter = _resolve_only(only) if only else (None, None)

    try:
        result = run_lint(
            config,
            targets,
            producers=only_producers,
            include_dndsim=dndsim,
            scoped=True,
            # `--json` is the machine surface: a caller reading NDJSON is
            # describing the corpus it was handed, so the run never
            # rewrites a byte of it (ADR-0064).
            no_fix=no_fix or as_json,
        )
    except Exception as error:
        typer.echo(f"wiki lint: internal error: {error}", err=True)
        raise typer.Exit(code=2) from error

    combined_rules = None
    if rule or only_rule_filter:
        combined_rules = list(dict.fromkeys((rule or []) + (only_rule_filter or [])))
    display_result = _emit(
        result,
        _git_root(config.repo_root),
        as_json=as_json,
        all_hits=all_hits,
        quiet=quiet,
        rules=combined_rules,
        sweep=False,
    )

    if only:
        assert only_producers is not None
        typer.echo(_only_timing_footer(display_result, only_producers), err=True)

    raise typer.Exit(code=_lint_exit_code(result))


@app.command()
def sweep(
    as_json: Annotated[
        bool, typer.Option("--json", help="One JSON object per finding, newline-delimited.")
    ] = False,
    all_hits: Annotated[
        bool,
        typer.Option(
            "--all",
            help="Show every hit — disables the manifest cap and baseline suppression.",
        ),
    ] = False,
    quiet: Annotated[
        bool, typer.Option("--quiet", help="Minimal output: finding count only.")
    ] = False,
    dndsim: Annotated[bool, typer.Option("--dndsim", help="Include dndsim findings.")] = False,
    no_fix: Annotated[
        bool,
        typer.Option(
            "--no-fix",
            "--dry-run",
            help="Report mechanical defects instead of repairing them (dry run).",
        ),
    ] = False,
) -> None:
    """The whole corpus: every rule and producer including the cross-file
    (SWEEP) ones, autofix, cache gc, and a dispatch manifest — one line per
    dirty file (ADR-0064)."""
    config = _load_config("sweep")
    vault_root = config.vault_root.resolve()
    targets = _collect_targets(config.repo_root, vault_root, None)

    try:
        result = run_lint(
            config,
            targets,
            include_dndsim=dndsim,
            scoped=False,
            no_fix=no_fix or as_json,
        )
    except Exception as error:
        typer.echo(f"wiki sweep: internal error: {error}", err=True)
        raise typer.Exit(code=2) from error

    git_root = _git_root(config.repo_root)
    # A COMPLETE corpus pass is the engine's own moment to ratchet the floor
    # down and to drop floors for files that have left the corpus
    # (ADR-0062). `wiki lint` must never reach it: a scoped run covers only
    # its own targets, and auto_sync_down reads the resulting live 0 as
    # "fixed".
    baseline.auto_sync_down(
        git_root, result.findings, [rel_path(target, git_root) for target in targets]
    )

    _emit(
        result,
        git_root,
        as_json=as_json,
        all_hits=all_hits,
        quiet=quiet,
        rules=None,
        sweep=True,
    )
    raise typer.Exit(code=_lint_exit_code(result))


def _needs_pagerank(where: list[str] | None, sort: str | None) -> bool:
    terms = list(where or []) + ([sort] if sort else [])
    return any("pagerank" in term for term in terms)


@app.command("list")
def list_cmd(
    where: Annotated[
        list[str] | None,
        typer.Option("--where", help="Filter: key<op>value (repeatable)."),
    ] = None,
    sort: Annotated[
        str | None,
        typer.Option("--sort", help="Sort key; prefix with - for descending."),
    ] = None,
    fmt: Annotated[
        str, typer.Option("--format", help="Output format: tsv, json, or paths.")
    ] = "tsv",
    columns: Annotated[
        str | None, typer.Option("--columns", help="Comma-separated column list.")
    ] = None,
    include_templates: Annotated[
        bool, typer.Option("--include-templates", help="Include template pages.")
    ] = False,
    limit: Annotated[int | None, typer.Option("--limit", help="Max rows to return.")] = None,
) -> None:
    """List vault pages with optional filtering, sorting, and formatting."""
    from wiki_cli.query.filters import FilterError, matches, parse_sort, parse_where, sort_rows
    from wiki_cli.query.output import render as render_rows
    from wiki_cli.query.runtime import load_context, rows_for

    try:
        ctx = load_context(needs_pagerank=_needs_pagerank(where, sort))
    except Exception as error:
        typer.echo(f"wiki list: {error}", err=True)
        raise typer.Exit(code=2) from error

    try:
        wheres = parse_where(where or [], ctx.legal_keys)
        sort_spec = parse_sort(sort, ctx.legal_keys)
    except FilterError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error

    all_rows = rows_for(ctx, include_templates=include_templates)
    filtered = [row for row in all_rows if matches(row, wheres)]
    sorted_rows = sort_rows(filtered, sort_spec)
    if limit is not None:
        sorted_rows = sorted_rows[:limit]
    col_list = columns.split(",") if columns else None
    typer.echo(render_rows(sorted_rows, fmt, col_list))


@app.command(
    "search",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def search_cmd(
    ctx: typer.Context,
    query: Annotated[str | None, typer.Argument(help="Search query.")] = None,
    collection: Annotated[
        list[str] | None,
        typer.Option("-c", "--collection", help="Collection to search (repeatable)."),
    ] = None,
    xml: Annotated[
        bool, typer.Option("--xml", help="Raw qmd XML passthrough.")
    ] = False,
    where: Annotated[
        list[str] | None,
        typer.Option("--where", help="Filter: key<op>value (repeatable)."),
    ] = None,
    sort: Annotated[
        str | None,
        typer.Option("--sort", help="Sort key; prefix with - for descending. Default: -score."),
    ] = None,
    fmt: Annotated[
        str, typer.Option("--format", help="Output format: tsv, json, or paths.")
    ] = "tsv",
    columns: Annotated[
        str | None, typer.Option("--columns", help="Comma-separated column list.")
    ] = None,
    include_templates: Annotated[
        bool, typer.Option("--include-templates", help="Include template pages.")
    ] = False,
    limit: Annotated[int, typer.Option("--limit", help="Max rows to return.")] = 20,
) -> None:
    """Semantic search via qmd, joined against the vault index for
    structural post-filtering/sorting/rendering."""
    collections = collection or ["content"]

    if xml:
        if where or sort is not None or columns is not None or fmt != "tsv":
            typer.echo(
                "wiki search --xml cannot be combined with --where/--sort/--columns/--format",
                err=True,
            )
            raise typer.Exit(code=2)
        import subprocess

        args = [query, *ctx.args] if query else list(ctx.args)
        cmd = ["qmd", *args, "--format", "xml"]
        for c in collections:
            cmd.extend(["-c", c])
        try:
            result = subprocess.run(cmd, capture_output=False, check=False)
        except FileNotFoundError:
            typer.echo("wiki search --xml needs the qmd CLI on PATH", err=True)
            raise typer.Exit(code=2) from None
        raise typer.Exit(code=result.returncode)

    if not query:
        typer.echo("wiki search: QUERY required (use --xml for raw passthrough)", err=True)
        raise typer.Exit(code=2)

    from wiki_cli.query.filters import FilterError, Row, matches, parse_sort, parse_where, sort_rows
    from wiki_cli.query.output import render as render_rows
    from wiki_cli.query.qmd import QmdError, QmdNotFoundError, run_qmd
    from wiki_cli.query.runtime import load_context, rows_for

    try:
        ctx_q = load_context(needs_pagerank=_needs_pagerank(where, sort))
    except Exception as error:
        typer.echo(f"wiki search: {error}", err=True)
        raise typer.Exit(code=2) from error

    legal_keys = ctx_q.legal_keys | {"score", "collection"}
    try:
        wheres = parse_where(where or [], legal_keys)
        sort_spec = parse_sort(sort, legal_keys)
    except FilterError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error

    try:
        hits = run_qmd(collections, query, limit * 5, ctx_q.config.repo_root)
    except (QmdNotFoundError, QmdError) as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error

    corpus_rows = {row.rel_path: row for row in rows_for(ctx_q, include_templates=include_templates)}
    result_rows: list[Row] = []
    for hit in hits:
        corpus_row = corpus_rows.get(hit.rel_path)
        if corpus_row is not None:
            computed = dict(corpus_row.computed)
            computed["score"] = hit.score
            computed["collection"] = hit.collection
            result_rows.append(
                Row(rel_path=hit.rel_path, frontmatter=corpus_row.frontmatter, computed=computed)
            )
        else:
            result_rows.append(
                Row(
                    rel_path=hit.rel_path,
                    frontmatter={},
                    computed={
                        "path": hit.rel_path,
                        "score": hit.score,
                        "collection": hit.collection,
                        "links-in": 0,
                        "links-out": 0,
                        "pagerank": None,
                        "mtime": 0.0,
                    },
                )
            )

    filtered = [row for row in result_rows if matches(row, wheres)]
    sorted_rows = sort_rows(filtered, sort_spec or ("score", True))[:limit]
    col_list = columns.split(",") if columns else ["path", "type", "score", "collection"]
    typer.echo(render_rows(sorted_rows, fmt, col_list))


@links_app.command("in")
def links_in_cmd(
    page: Annotated[str, typer.Argument(help="Page rel_path or slug.")],
    fmt: Annotated[
        str, typer.Option("--format", help="Output format: tsv, json, or paths.")
    ] = "tsv",
    columns: Annotated[
        str | None, typer.Option("--columns", help="Comma-separated column list.")
    ] = None,
    sort: Annotated[
        str | None,
        typer.Option("--sort", help="Sort key; prefix with - for descending."),
    ] = None,
    limit: Annotated[int | None, typer.Option("--limit", help="Max rows to return.")] = None,
    include_templates: Annotated[
        bool, typer.Option("--include-templates", help="Include template pages.")
    ] = False,
) -> None:
    """Pages linking TO PAGE (backlinks)."""
    from wiki_cli.query.filters import FilterError, parse_sort, sort_rows
    from wiki_cli.query.links import backlinks
    from wiki_cli.query.output import render as render_rows
    from wiki_cli.query.runtime import load_context

    del include_templates  # accepted for flag-set parity with the other links subcommands
    query_ctx = load_context()
    resolved = query_ctx.index.resolve(page)
    if resolved is None:
        typer.echo(f"wiki links in: cannot resolve '{page}'", err=True)
        raise typer.Exit(code=2)

    rows = backlinks(query_ctx, resolved.rel_path)
    try:
        sort_spec = parse_sort(sort, query_ctx.legal_keys)
    except FilterError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error
    sorted_rows = sort_rows(rows, sort_spec)
    if limit is not None:
        sorted_rows = sorted_rows[:limit]
    col_list = columns.split(",") if columns else None
    typer.echo(render_rows(sorted_rows, fmt, col_list))


@links_app.command("out")
def links_out_cmd(
    page: Annotated[str, typer.Argument(help="Page rel_path or slug.")],
    fmt: Annotated[
        str, typer.Option("--format", help="Output format: tsv, json, or paths.")
    ] = "tsv",
    columns: Annotated[
        str | None, typer.Option("--columns", help="Comma-separated column list.")
    ] = None,
    sort: Annotated[
        str | None,
        typer.Option("--sort", help="Sort key; prefix with - for descending."),
    ] = None,
    limit: Annotated[int | None, typer.Option("--limit", help="Max rows to return.")] = None,
    include_templates: Annotated[
        bool, typer.Option("--include-templates", help="Include template pages.")
    ] = False,
) -> None:
    """Pages PAGE links to (outlinks)."""
    from wiki_cli.query.filters import FilterError, parse_sort, sort_rows
    from wiki_cli.query.links import outlinks
    from wiki_cli.query.output import render as render_rows
    from wiki_cli.query.runtime import load_context

    del include_templates  # accepted for flag-set parity with the other links subcommands
    query_ctx = load_context()
    resolved = query_ctx.index.resolve(page)
    if resolved is None:
        typer.echo(f"wiki links out: cannot resolve '{page}'", err=True)
        raise typer.Exit(code=2)

    rows = outlinks(query_ctx, resolved.rel_path)
    try:
        sort_spec = parse_sort(sort, query_ctx.legal_keys)
    except FilterError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error
    sorted_rows = sort_rows(rows, sort_spec)
    if limit is not None:
        sorted_rows = sorted_rows[:limit]
    col_list = columns.split(",") if columns else None
    typer.echo(render_rows(sorted_rows, fmt, col_list))


@links_app.command("breakdown")
def links_breakdown_cmd(
    to: Annotated[
        list[str], typer.Option("--to", help="Target filter (repeatable, required).")
    ],
    from_filter: Annotated[
        list[str] | None, typer.Option("--from", help="Source filter (repeatable).")
    ] = None,
    fmt: Annotated[
        str, typer.Option("--format", help="Output format: tsv, json, or paths.")
    ] = "tsv",
    columns: Annotated[
        str | None, typer.Option("--columns", help="Comma-separated column list.")
    ] = None,
    sort: Annotated[
        str | None,
        typer.Option("--sort", help="Sort key; prefix with - for descending."),
    ] = None,
    limit: Annotated[int | None, typer.Option("--limit", help="Max rows to return.")] = None,
    include_templates: Annotated[
        bool, typer.Option("--include-templates", help="Include template pages.")
    ] = False,
) -> None:
    """Per-target backlink counts, least-linked first."""
    from wiki_cli.query.filters import FilterError, Row, matches, parse_sort, parse_where, sort_rows
    from wiki_cli.query.links import breakdown
    from wiki_cli.query.output import render as render_rows
    from wiki_cli.query.runtime import load_context, rows_for

    query_ctx = load_context()
    try:
        to_wheres = parse_where(to, query_ctx.legal_keys)
        from_wheres = parse_where(from_filter or [], query_ctx.legal_keys)
    except FilterError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error

    all_rows = rows_for(query_ctx, include_templates=include_templates)
    to_rows = [row for row in all_rows if matches(row, to_wheres)]
    from_rows = [row for row in all_rows if matches(row, from_wheres)] if from_filter else None

    bd = breakdown(query_ctx, to_rows, from_rows)
    result_rows: list[Row] = []
    for row, count, sources in bd:
        computed = dict(row.computed)
        computed["links-in-matched"] = count
        computed["sources"] = ",".join(sources)
        result_rows.append(Row(rel_path=row.rel_path, frontmatter=row.frontmatter, computed=computed))

    if sort is not None:
        try:
            sort_spec = parse_sort(sort, query_ctx.legal_keys | {"links-in-matched", "sources"})
        except FilterError as error:
            typer.echo(str(error), err=True)
            raise typer.Exit(code=2) from error
        result_rows = sort_rows(result_rows, sort_spec)
    if limit is not None:
        result_rows = result_rows[:limit]

    col_list = columns.split(",") if columns else ["path", "links-in-matched", "sources"]
    typer.echo(render_rows(result_rows, fmt, col_list))


@links_app.command("orphans")
def links_orphans_cmd(
    where: Annotated[
        list[str] | None, typer.Option("--where", help="Filter: key<op>value (repeatable).")
    ] = None,
    fmt: Annotated[
        str, typer.Option("--format", help="Output format: tsv, json, or paths.")
    ] = "tsv",
    columns: Annotated[
        str | None, typer.Option("--columns", help="Comma-separated column list.")
    ] = None,
    sort: Annotated[
        str | None,
        typer.Option("--sort", help="Sort key; prefix with - for descending."),
    ] = None,
    limit: Annotated[int | None, typer.Option("--limit", help="Max rows to return.")] = None,
    include_templates: Annotated[
        bool, typer.Option("--include-templates", help="Include template pages.")
    ] = False,
) -> None:
    """Pages with zero backlinks."""
    from wiki_cli.query.filters import FilterError, matches, parse_sort, parse_where, sort_rows
    from wiki_cli.query.links import orphans
    from wiki_cli.query.output import render as render_rows
    from wiki_cli.query.runtime import load_context, rows_for

    query_ctx = load_context()
    try:
        wheres = parse_where(where or [], query_ctx.legal_keys)
        sort_spec = parse_sort(sort, query_ctx.legal_keys)
    except FilterError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error

    all_rows = rows_for(query_ctx, include_templates=include_templates)
    filtered = [row for row in all_rows if matches(row, wheres)]
    orphan_rows = orphans(query_ctx, filtered)
    sorted_rows = sort_rows(orphan_rows, sort_spec)
    if limit is not None:
        sorted_rows = sorted_rows[:limit]
    col_list = columns.split(",") if columns else None
    typer.echo(render_rows(sorted_rows, fmt, col_list))


@links_app.command("redundant")
def links_redundant_cmd(
    fmt: Annotated[str, typer.Option("--format", help="Output format: tsv, json, or paths.")] = (
        "tsv"
    ),
    columns: Annotated[
        str | None, typer.Option("--columns", help="Comma-separated column list.")
    ] = None,
    limit: Annotated[int | None, typer.Option("--limit", help="Max rows to return.")] = None,
) -> None:
    """Pages with repeated same-section wikilinks to the same target."""
    from wiki_cli.query.filters import Row
    from wiki_cli.query.links import redundant
    from wiki_cli.query.output import render as render_rows
    from wiki_cli.query.runtime import load_context

    query_ctx = load_context()
    results = redundant(query_ctx.index)
    rows: list[Row] = []
    for source, section, target, count in results:
        rows.append(
            Row(
                rel_path=source,
                frontmatter={},
                computed={"path": source, "section": section, "target": target, "count": count},
            )
        )
    if limit is not None:
        rows = rows[:limit]
    col_list = columns.split(",") if columns else ["path", "section", "target", "count"]
    typer.echo(render_rows(rows, fmt, col_list))


@links_app.command("spread")
def links_spread_cmd(
    to: Annotated[
        list[str], typer.Option("--to", help="Target filter (repeatable, required).")
    ],
    from_filter: Annotated[
        list[str], typer.Option("--from", help="Source filter (repeatable, required).")
    ],
    fmt: Annotated[
        str, typer.Option("--format", help="Output format: tsv, json, or paths.")
    ] = "tsv",
    columns: Annotated[
        str | None, typer.Option("--columns", help="Comma-separated column list.")
    ] = None,
    limit: Annotated[int | None, typer.Option("--limit", help="Max rows to return.")] = None,
    include_templates: Annotated[
        bool, typer.Option("--include-templates", help="Include template pages.")
    ] = False,
) -> None:
    """Surface under-represented targets so you can place sources for exploration variety."""
    from wiki_cli.query.filters import FilterError, Row, matches, parse_where
    from wiki_cli.query.links import spread
    from wiki_cli.query.output import render as render_rows
    from wiki_cli.query.runtime import load_context, rows_for

    query_ctx = load_context()
    try:
        to_wheres = parse_where(to, query_ctx.legal_keys)
        from_wheres = parse_where(from_filter, query_ctx.legal_keys)
    except FilterError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error

    all_rows = rows_for(query_ctx, include_templates=include_templates)
    to_rows = [row for row in all_rows if matches(row, to_wheres)]
    from_rows = [row for row in all_rows if matches(row, from_wheres)]

    if not to_rows:
        typer.echo("wiki links spread: no pages match --to filter", err=True)
        raise typer.Exit(code=2)

    results = spread(query_ctx, to_rows, from_rows)
    rows: list[Row] = []
    for source, current, suggested, suggested_count in results:
        rows.append(
            Row(
                rel_path=source,
                frontmatter={},
                computed={
                    "source": source,
                    "current": current or "",
                    "suggested": suggested,
                    "suggested-count": suggested_count,
                },
            )
        )
    if limit is not None:
        rows = rows[:limit]
    col_list = columns.split(",") if columns else ["source", "current", "suggested", "suggested-count"]
    typer.echo(render_rows(rows, fmt, col_list))


@app.command()
def drain(
    rule: Annotated[
        list[str] | None,
        typer.Option("--rule", help="Only findings from these rule ids (repeatable)."),
    ] = None,
    path: Annotated[
        str | None,
        typer.Option("--path", help="Only rel_paths matching this glob, e.g. 'vault/npcs/*'."),
    ] = None,
    limit: Annotated[
        int | None, typer.Option("--limit", help="Show at most this many files.")
    ] = None,
    over: Annotated[
        bool,
        typer.Option(
            "--over",
            help="Triage view: every (file, rule) pair above its floor, grouped by rule.",
        ),
    ] = False,
    claim: Annotated[
        int | None,
        typer.Option(
            "--claim",
            help="Atomically claim the top N unclaimed files; prints only their rel_paths.",
        ),
    ] = None,
    agent_id: Annotated[
        str | None,
        typer.Option(
            "--agent-id",
            help="Claim/release owner; defaults to a fresh UUID on --claim. On --release/"
            "--release-all, restricts the release to that owner's own claims.",
        ),
    ] = None,
    claims: Annotated[
        bool, typer.Option("--claims", help="List active (non-expired) claims.")
    ] = False,
    release: Annotated[
        str | None, typer.Option("--release", help="Release the claim on this rel_path.")
    ] = None,
    release_all: Annotated[
        bool, typer.Option("--release-all", help="Release every claim.")
    ] = False,
) -> None:
    """The debt queue: one line per file from the last sweep's cache, worst
    offenders first (a stale cache is fine — this is a queue, not a gate).
    The single debt surface (ADR-0064): --over triages the baseline
    over-floor pairs, and --claim/--claims/--release/--release-all work the
    lease that keeps two fixing agents off one file."""
    modes = [over, claim is not None, claims, release is not None, release_all]
    if sum(1 for mode in modes if mode) > 1:
        typer.echo(
            "wiki drain: pass at most one of --over/--claim/--claims/--release/--release-all",
            err=True,
        )
        raise typer.Exit(code=2)

    config = _load_config("drain")

    if over:
        _print_over_floor(config)
        return

    conn = db.connect(config.cache_path)
    try:
        if claim is not None:
            owner = agent_id or str(uuid.uuid4())
            ttl_seconds = _drain.load_claim_ttl_seconds(config.repo_root)
            claimed = _drain.claim_top_n(
                conn, claim, owner, ttl_seconds, rules=rule, path_glob=path
            )
            for claimed_path in claimed:
                typer.echo(claimed_path)
        elif claims:
            active = _drain.list_active_claims(conn)
            if not active:
                typer.echo("CLAIMS — none active")
            else:
                typer.echo(f"CLAIMS — {len(active)} active")
                for key, owner, expires_at in active:
                    typer.echo(f"{key}  {owner}  expires_at={expires_at:.0f}")
        elif release_all:
            count = _drain.release_all(conn, agent_id=agent_id)
            typer.echo(f"released {count} claim(s)")
        elif release is not None:
            released = _drain.release_claim(conn, release, agent_id=agent_id)
            typer.echo(f"released {release}" if released else f"no claim held on {release}")
        else:
            entries = _drain.build_queue(conn, rules=rule, path_glob=path, limit=limit)
            age = _drain.cache_age_seconds(conn)
            typer.echo(_drain.format_queue(entries, cache_age_seconds=age))
    finally:
        conn.close()


def _guide_pages(guide_dir: Path, rule_id: str) -> list[Path]:
    """Guide pages for `rule_id`, case-insensitively. A page is named for
    the family it documents (`w22-w23-callouts.md`, `w86-vale-prose.md`), so
    a hyphen-separated token match finds the id wherever it sits in the name
    and never lets `W8` answer for `W86`."""
    wanted = rule_id.strip().lower()
    return sorted(
        page
        for page in guide_dir.glob("*.md")
        if wanted in page.stem.lower().split("-")
    )


@app.command()
def explain(
    rule: Annotated[str, typer.Argument(help="Rule id, e.g. W86 (case-insensitive).")],
) -> None:
    """Print this rule's guide page from vault/refs/lint/ — what the rule
    wants, and how to satisfy it (ADR-0064)."""
    config = _load_config("explain")
    guide_dir = _git_root(config.repo_root) / GUIDE_DIR
    pages = _guide_pages(guide_dir, rule)
    if not pages:
        available = ", ".join(sorted(page.stem for page in guide_dir.glob("*.md")))
        typer.echo(f"wiki explain: no guide page for {rule!r}", err=True)
        typer.echo(f"available: {available}", err=True)
        raise typer.Exit(code=2)
    for page in pages:
        typer.echo(page.read_text(encoding="utf-8").rstrip("\n"))


@app.command("slug-scrub")
def slug_scrub(
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Report rewrites without writing files."),
    ] = False,
) -> None:
    """Rewrite path-qualified wikilinks ([[path/to/slug|...]]) to slug-only ([[slug|...]]) across vault/.

    Runs a slug uniqueness check first and exits non-zero on any collision.
    """
    from wiki_cli.index import VaultIndex
    from wiki_cli.rules.duplicate_basename import DuplicateBasenameRule
    from wiki_cli.rules.path_wikilink import scrub_paths

    config = load_config()
    vault_root = config.vault_root.resolve()

    corpus = VaultIndex.build(config.repo_root, vault_root, ())
    collisions = list(DuplicateBasenameRule().check(corpus))
    if collisions:
        typer.echo("slug-scrub: basename collision(s) detected — resolve before scrubbing:", err=True)
        for f in collisions:
            typer.echo(f"  {f.file}: {f.message}", err=True)
        raise typer.Exit(code=1)

    files_changed = 0
    links_rewritten = 0

    for md_file in sorted(vault_root.rglob("*.md")):
        original = md_file.read_text(encoding="utf-8")
        rewritten, n = scrub_paths(original)
        if n:
            links_rewritten += n
            files_changed += 1
            if not dry_run:
                md_file.write_text(rewritten, encoding="utf-8")

    prefix = "[dry-run] " if dry_run else ""
    typer.echo(
        f"slug-scrub: {prefix}{files_changed} file(s) changed, {links_rewritten} link(s) rewritten"
    )


@app.command("build-gravity")
def build_gravity(
    full: Annotated[bool, typer.Option("--full", help="Reprocess all episodes, ignoring watermark.")] = False,
) -> None:
    """Roll up page_interactions into player_gravity and gravity_tier on page_metrics."""
    from wiki_cli.gravity import build_gravity as _build

    config = load_config()
    conn = db.connect(config.cache_path)
    updated, unencountered = _build(conn, config.gravity, full=full)
    typer.echo(f"build-gravity: {updated} pages scored, {unencountered} marked unencountered")


@app.command("build-agent-access")
def build_agent_access_cmd() -> None:
    """Ingest the agent-reads JSONL log into page_agent_access and roll up agent_reads."""
    from wiki_cli.agent_access import ingest_log, rollup_agent_reads

    config = load_config()
    conn = db.connect(config.cache_path)
    log_path = config.repo_root / ".wiki-cli" / "agent-reads.jsonl"
    inserted = ingest_log(conn, log_path)
    updated = rollup_agent_reads(conn, config.agent_access)
    typer.echo(f"build-agent-access: {inserted} records ingested, {updated} pages rolled up")


@app.command("report-hot-pages")
def report_hot_pages_cmd(
    redundant: Annotated[bool, typer.Option("--redundant", help="Show same-session re-reads.")] = False,
    divergent: Annotated[bool, typer.Option("--divergent", help="Show high-reads / low-importance pages.")] = False,
) -> None:
    """Pages ranked by agent_reads, with pagerank and gravity signals."""
    from wiki_cli.agent_access import (
        report_divergent,
        report_hot_pages,
        report_redundant,
    )

    config = load_config()
    conn = db.connect(config.cache_path)

    if redundant:
        rows = report_redundant(conn)
        if not rows:
            typer.echo("report-hot-pages --redundant: no same-session re-reads found")
            return
        typer.echo(f"{'page':<60} {'session_id':<40} {'reads':>5}")
        typer.echo("-" * 107)
        for r in rows:
            typer.echo(f"{r.page:<60} {r.session_id:<40} {r.read_count:>5}")
        return

    if divergent:
        rows_d = report_divergent(conn)
        if not rows_d:
            typer.echo("report-hot-pages --divergent: no divergent pages found")
            return
        typer.echo(f"{'page':<60} {'agent_reads':>11} {'pagerank':>10} {'gravity':>10} {'importance':>11}")
        typer.echo("-" * 104)
        for r in rows_d:
            pr = f"{r.pagerank:.4f}" if r.pagerank is not None else "-"
            pg = f"{r.player_gravity:.1f}" if r.player_gravity is not None else "-"
            typer.echo(f"{r.page:<60} {r.agent_reads:>11} {pr:>10} {pg:>10} {r.importance_score:>11.4f}")
        return

    rows_h = report_hot_pages(conn)
    if not rows_h:
        typer.echo("report-hot-pages: no agent reads recorded")
        return
    typer.echo(f"{'page':<60} {'agent_reads':>11} {'pagerank':>10} {'gravity_tier':>13}")
    typer.echo("-" * 96)
    for r in rows_h:
        pr = f"{r.pagerank:.4f}" if r.pagerank is not None else "-"
        gt = r.gravity_tier or "-"
        typer.echo(f"{r.page:<60} {r.agent_reads:>11} {pr:>10} {gt:>13}")


@app.command("conflict-signals")
def conflict_signals_cmd(
    page_a: Annotated[str, typer.Argument(help="rel_path of the first conflicting page.")],
    page_b: Annotated[str, typer.Argument(help="rel_path of the second conflicting page.")],
) -> None:
    """Structural rank and corroboration for a two-page continuity conflict.

    Outputs one line per page: rel_path, rank, corroboration count.
    Calls ensure_pagerank so values are fresh.  The DM decides which claim is
    correct — this command surfaces signal only, never a recommendation."""
    from wiki_cli.config import load_config
    from wiki_cli.query.conflict import conflict_signals
    from wiki_cli.query.pagerank import ensure_pagerank

    config = load_config()
    conn = db.connect(config.cache_path)
    ensure_pagerank(conn, weights=config.pagerank.weights)
    sig_a, sig_b = conflict_signals(conn, page_a, page_b)

    rank_a = f"{sig_a.pagerank:.4f}" if sig_a.pagerank is not None else "none"
    rank_b = f"{sig_b.pagerank:.4f}" if sig_b.pagerank is not None else "none"
    typer.echo(f"{sig_a.page}  rank={rank_a}  corroboration={sig_a.corroboration}")
    typer.echo(f"{sig_b.page}  rank={rank_b}  corroboration={sig_b.corroboration}")


@app.command("assign-uids")
def assign_uids() -> None:
    """Assign a UUID v4 `uid:` frontmatter field to every vault page that lacks one.

    Writes the uid to the file's frontmatter and records it in `pages.uid`.
    Idempotent: pages that already have a `uid:` are skipped.
    """
    from wiki_cli.index import VaultIndex
    from wiki_cli.markdown import render_page, round_trip_frontmatter

    config = load_config()
    vault_root = config.vault_root.resolve()
    conn = db.connect(config.cache_path)

    corpus = VaultIndex.build(config.repo_root, vault_root, ())

    assigned = 0
    skipped = 0

    for page in corpus.pages():
        existing_uid = page.frontmatter.get("uid")
        if existing_uid:
            skipped += 1
            continue

        new_uid = str(uuid.uuid4())

        fm = round_trip_frontmatter(page)
        if fm is None:
            skipped += 1
            continue

        fm["uid"] = new_uid
        updated = render_page(page, fm)
        (config.repo_root / page.rel_path).write_text(updated, encoding="utf-8")

        if not db.set_page_uid(conn, page.rel_path, new_uid):
            typer.echo(f"assign-uids: warning — no pages row for {page.rel_path!r}; UID written to file only", err=True)
        assigned += 1

    typer.echo(f"assign-uids: {assigned} assigned, {skipped} skipped")


@app.command("organize")
def organize(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show cluster assignments and moves without writing files.")] = False,
    check: Annotated[bool, typer.Option("--check", help="Exit non-zero if tree diverges from computed output (CI guard).")] = False,
    scope: Annotated[str | None, typer.Option("--scope", help="Limit materialisation to clusters whose anchor path starts with this prefix or whose anchor slug matches exactly.")] = None,
) -> None:
    """Cluster analysis and materialisation for vault reorganisation (ADR-0049).

    Args:
        dry_run: Print cluster assignments and pending moves; write nothing.
        check: Exit non-zero listing files out of place (CI guard). Implies no moves.
        scope: Restrict moves to clusters whose anchor path starts with this prefix.
    """
    from wiki_cli.materialise import apply_moves, compute_moves
    from wiki_cli.organizer import analyze

    config = load_config()
    conn = db.connect(config.cache_path)
    result = analyze(conn, config.organizer, config.pagerank.weights)
    type_map: dict[str, str] = {
        row[0]: row[1]
        for row in conn.execute("SELECT rel_path, type FROM pages WHERE type IS NOT NULL").fetchall()
    }
    moves = compute_moves(result, scope=scope, type_map=type_map)

    if check:
        if moves:
            typer.echo(f"organize --check: {len(moves)} file(s) out of place:", err=True)
            for op in moves:
                typer.echo(f"  {op.src} -> {op.dst}", err=True)
            raise typer.Exit(1)
        return

    if dry_run:
        if result.clusters:
            typer.echo(f"{'Cluster (anchor)':<40} {'Size':>5} {'Density':>8}")
            typer.echo("-" * 55)
            for cluster in result.clusters:
                typer.echo(f"{cluster.anchor:<40} {len(cluster.members):>5} {cluster.density:>8.2f}")
                for member in cluster.members:
                    typer.echo(f"  {member}")

        if result.ambiguous:
            typer.echo("")
            typer.echo("ANCHOR_AMBIGUOUS:")
            for label, members in result.ambiguous:
                typer.echo(f"  {label} ({len(members)} files)")
                for member in members:
                    typer.echo(f"    {member}")

        if result.unassigned:
            typer.echo("")
            typer.echo(f"Unassigned ({len(result.unassigned)} files):")
            for path in result.unassigned:
                typer.echo(f"  {path}")

        total = sum(len(c.members) for c in result.clusters) + len(result.unassigned) + sum(len(m) for _, m in result.ambiguous)
        typer.echo(f"\norganize: {len(result.clusters)} clusters, {len(result.unassigned)} unassigned, {len(result.ambiguous)} ambiguous, {total} total pages")

        if moves:
            typer.echo(f"\nPending moves ({len(moves)}):")
            for op in moves:
                typer.echo(f"  {op.src} -> {op.dst}")
        return

    if not moves:
        typer.echo("organize: already organised, no changes")
        return

    apply_moves(moves, config.repo_root)
    typer.echo(f"organize: moved {len(moves)} file(s)")


@app.command()
def bench() -> None:
    """Cold + warm full-vault sweep timing (Task 26): appends one entry to
    .claude/.wiki-bench.jsonl and flags a >25% regression vs the previous
    entry — same contract as the legacy `npm run lint:bench`."""
    config = load_config()
    vault_root = config.vault_root.resolve()
    git_root = _git_root(config.repo_root)

    previous = _bench.last_entry(git_root)

    cold, warm = _bench.run_bench(config, vault_root)
    typer.echo(f"cold: {cold['seconds']:.1f}s, {cold['findings']} findings")
    typer.echo(f"warm: {warm['seconds']:.1f}s, {warm['findings']} findings")
    for entry in (cold, warm):
        if entry.get("perf_over_budget"):
            typer.echo(entry["perf_over_budget"])

    entry = {"date": datetime.now(UTC).isoformat(), "cold": cold, "warm": warm}
    _bench.append_jsonl(git_root, [entry])

    regression = _bench.check_regression(cold, previous.get("cold") if previous else None)
    if regression:
        typer.echo(regression)


def _full_sweep_findings(config: Config) -> list[Finding]:
    """Findings from a full corpus pass, for `wiki drain --over` and the
    `debt` maintenance commands — always the whole vault, never a scoped
    subset, since a floor computed from a partial pass would be wrong for
    every file outside it.

    `no_fix`: a debt command measures the debt that exists, so it never
    rewrites a page on the way to counting it."""
    vault_root = config.vault_root.resolve()
    targets = _collect_targets(config.repo_root, vault_root, None)
    return run_lint(config, targets, no_fix=True).findings


@debt_app.command("check")
def debt_check() -> None:
    """Exit 1 when any live warning-severity count exceeds its floor (a full
    corpus pass); exit 0 otherwise."""
    config = _load_config("debt check")
    findings = _full_sweep_findings(config)
    git_root = _git_root(config.repo_root)
    ok, _over = baseline.check(git_root, findings)
    typer.echo(baseline.ratchet_token(git_root, findings))
    raise typer.Exit(code=0 if ok else 1)


def _print_over_floor(config: Config) -> None:
    """`wiki drain --over`: every (file, rule) pair above its floor, grouped
    by rule, chattiest rule first (ADR-0062)."""
    findings = _full_sweep_findings(config)
    entries = baseline.over_entries(_git_root(config.repo_root), findings)
    if not entries:
        typer.echo("ratchet OK — every (file, rule) pair is at or below its floor")
        return

    by_rule: dict[str, list[tuple[str, int]]] = {}
    for rel, rule_id, delta in entries:
        by_rule.setdefault(rule_id, []).append((rel, delta))

    total = sum(delta for _rel, _rule_id, delta in entries)
    typer.echo(f"ratchet +{len(entries)} over floor · {total} findings above floor")
    for rule_id, pairs in sorted(by_rule.items(), key=lambda item: (-len(item[1]), item[0])):
        typer.echo(f"{rule_id} — {len(pairs)} file(s), +{sum(d for _rel, d in pairs)}")
        for rel, delta in sorted(pairs, key=lambda pair: (-pair[1], pair[0])):
            typer.echo(f"  +{delta}  {rel}")


@debt_app.command("accept")
def debt_accept(
    force: Annotated[
        bool,
        typer.Option("--force", help="Required — rewrites every floor to today's counts."),
    ] = False,
) -> None:
    """Accept today's live counts as the debt floor, from a full corpus
    pass. Orchestrator/human maintenance only — refuses without --force,
    since it absorbs any regression standing at the time it runs."""
    if not force:
        typer.echo("wiki debt accept: refusing without --force", err=True)
        raise typer.Exit(code=2)
    config = _load_config("debt accept")
    findings = _full_sweep_findings(config)
    baseline.promote(_git_root(config.repo_root), findings)
    typer.echo("debt floors accepted from a full corpus pass")
