---
type: runbook
status: draft
publish: false
aliases: []
created: "2026-08-01"
updated: "2026-08-10"
tags: [craft]
summary: "Every npm-run and wiki-cli command: 12 scoped search collections (content through ideas), 9 read-layer queries (wiki list/search/links in/out/breakdown/orphans/redundant/spread with shared --where/--sort/--format flags), the full lint surface (lint, sweep, drain, explain, debt, bench), and the dndsim combat engine."
phase: any
uid: 317e6092-7bf6-4466-9f40-37927697d408
---

# COMMANDS runbook (any: the command surface)

Every `npm run` command this repo exposes, and which question each one answers. Reach for the narrowest command that covers the question — a scoped search beats the whole-wiki one, a single-path lint beats a full sweep.

## Search

Hybrid semantic search over an indexed collection. `-- query "<text>"` is the argument form: `npm run search:content -- query "otar the foul"`.

| Command | Covers | Reach for it when |
|---|---|---|
| `search:content` | `vault/**` — every governed wiki page | Default. Any campaign fact: an NPC, place, faction, item, quest, rule, world state |
| `search:pcs` | `vault/campaigns/shattered-sea/pcs/**` | A player character's sheet, abilities, combat profile, gallery, or session log |
| `search:sessions` | `vault/episodes/**` | An episode's scenes, run guide, recap, or transcript |
| `search:craft` | `vault/refs/**` | House GM-craft doctrine and the vendored methodology library. Mandatory before improving any campaign-os element |
| `search:external` | The vendored 5e SRD tree — monsters, spells, items, classes, feats, species, backgrounds | A rules-as-written lookup, not a campaign fact |
| `search:guardrails` | `docs/**` | A guardrail checklist, an ADR, a ruling |
| `search:wiki` | `vault/**`, unscoped | A term that could sit anywhere and you do not know which subtree |
| `search:raw` | `raw/**` | Ingested source material, superseded specs, a page's fidelity record |
| `search:inbox` | `inbox/**` | Something dropped in but not yet ingested |
| `search:stories` | `vault/stories/**` | A narrative draft — story, arc, quest write-up |
| `search:ideas` | `vault/ideas/**` | A loose idea, fragment, or writers-room draft |
| `search:help` | — | The underlying `qmd` flags |

Collection paths live in `~/.config/qmd/index.yml`, outside this repo — `utils/qmd-collections.yml` is the checked-in source of truth, and `npm run search:sync` splices it in. A collection whose path no longer exists returns zero hits silently — it never errors — so a search that comes back empty against material you know exists means checking that file before concluding the material is missing.

## Read layer

Structural queries over the vault corpus — filter, sort, and cross-reference pages by frontmatter and link-graph metrics. All commands share `--where KEY<OP>VALUE` (repeatable), `--sort KEY`, `--format tsv|json|paths`, `--columns`, `--limit`. Engine is `utils/wiki-cli/` (ADR-0046).

| Command | Does | Reach for it when |
|---|---|---|
| `wiki list` | Every vault page, filtered/sorted by frontmatter + computed metrics | Which pages of a type exist, filtered and sorted, zero post-processing |
| `wiki search QUERY` | Semantic search via qmd with structural post-filters | A concept/term across the wiki, narrowed by type/tags/links |
| `wiki search --xml` | Raw qmd XML passthrough (what `npm run search:*` calls) | Backward-compatible search from npm scripts |
| `wiki links in PAGE` | Pages linking TO a page (backlinks) | Who references this page? |
| `wiki links out PAGE` | Pages a page links to (outlinks) | What does this page reference? |
| `wiki links breakdown --to ... [--from ...]` | Per-target backlink counts from a source set | How are items distributed across shops? |
| `wiki links orphans` | Pages with zero backlinks | Unlinked pages that need wiring into the graph |
| `wiki links redundant` | Same-section repeated wikilinks | Repeated links to prune within a section |
| `wiki links spread --to ... --from ...` | Under-represented targets for placement variety | Agents ensure player-relevant content sits in their potential paths |

Three-step shop workflow: `wiki list --where type=shop` → `wiki links breakdown --to type=shop --from type=item` → `wiki links spread --to type=shop --from type=item`.

## Lint

`lint` takes paths and is the edit loop; `lint:sweep` is the whole corpus.
Output is an instruction list (ADR-0064): every line is either a fix the tool
already applied or one imperative FIX to act on. The engine is
`utils/wiki-cli/` (Python, ADR-0045).

Every prose check reaches the file through this command. Vale is one producer
inside it, scoped per path by `wiki.toml`; a `vale` call made outside the
command reads a different scope and reports a different finding set, so its
verdict says nothing about the file this command gates.

| Command | Does | Reach for it when |
|---|---|---|
| `lint -- <path>` | Every edit-time rule and producer over those paths, autofixing what is mechanical | Any "lint this" — the default, prose included |
| `lint:sweep` | The whole corpus including cross-file rules; gc's the cache and prints a dispatch manifest, one line per dirty file | Sizing or dispatching corpus-wide work (~7 min) |
| `lint -- <path> --quiet` | Finding count only | Sizing a backlog before dispatching a drain |
| `lint -- <path> --json` | One JSON object per finding, newline-delimited; never autofixes | Driving a dispatch programmatically |
| `lint -- <path> --no-fix` (alias `--dry-run`) | Reports mechanical defects instead of repairing them; writes nothing | Previewing what autofix would change |
| `lint -- <path> --rule <id>` | Display filter to one rule id (repeatable); exit code still reflects full scope | Checking one rule's findings |
| `lint -- <path> --all` | Shows baselined debt too, uncapped | Reading the full debt on one page |
| `lint -- --rules` | Lists every rule id, tier, severity, and fix line | Auditing the rule roster |
| `lint -- <path> --only <rule\|producer>` | Execution-gating: runs only the named rule's producer (repeatable, prints timing) | Testing one rule without running every producer |
| `lint:explain -- <RULE>` | Prints that rule's guide page from `vault/refs/lint/` | A FIX line needs more than one imperative |
| `lint:help` | Agent-optimized reference for every command and flag | Discovering the CLI surface |
| `lint:bench` | Cold + warm benchmark; prints `PERF OVER BUDGET` past the `wiki.toml [bench]` budget | Measuring lint performance |
| `lint:drain` | The debt queue from the last sweep's cache, worst file first (`-- --path <glob>`, `-- --limit N`) | Starting a drain wave; `/drain` calls this |
| `lint:drain -- --over` | Every (file, rule, delta) pair above its floor, grouped by rule | A report prints `+N over floor` and you want the triage list (ADR-0062) |
| `lint:drain -- --claim N` | Leases the top N unclaimed files and prints their paths (`--agent-id`, `--claims`, `--release <path>`, `--release-all`) | Handing files to a dispatch wave without two agents colliding |
| `lint:debt -- check` | Exits 1 if any live count exceeds its floor | Before a commit |
| `lint:debt -- accept --force` | Accepts today's live counts as the floor | After a drain wave clears findings, or a new rule ships with live findings (ADR-0006) |

`lint:debt -- accept` refuses without `--force`: it re-raises floors already ratcheted down, absorbing any regression standing at the time it runs.

## dndsim (combat engine)

`utils/dndsim/` is the combat simulation engine — `npm run dndsim -- <verb>` (verbs: sim-combat, profile, parse, lint, sweep-corpus, sweep-count), tested via `npm run test:dndsim`. Behavioral divergences from the predecessor are recorded in `utils/dndsim/DIVERGENCES.md`.

Each rule's id, tier, severity, and fix line: `npm run lint -- --rules`. The
prose-lint arm is documented in `docs/vale-styles/README.md`. For the
whole-wiki health sweep these commands serve, see
`vault/refs/runbook-maintain.md`.
