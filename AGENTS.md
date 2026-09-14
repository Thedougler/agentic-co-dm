# Obsidian Wiki — Agent Context

A **skill-based framework** for building and maintaining an Obsidian knowledge base. No scripts or dependencies — everything is markdown instructions that you execute directly.

## README Translation Parity

`README.md` and `README_TW.md` are one documentation surface. Keep headings, examples, links, and user-facing behavior aligned between the two translations. The check is advisory and never blocks a PR: the `readme-translation-drift` CI job only reports drift. Run `python3 tools/check_readme_sync.py` to list commits that changed `README.md` without a later `README_TW.md` update, along with the pending English diff — then translate and backfill those changes into `README_TW.md`. Reviewers assess translation quality.
## Spec Kit Git Automation

Spec Kit auto-commit is enabled for the configured before/after hooks. The commit style is fixed (`commit_style: fixed`); use the configured `[Spec Kit] ...` messages rather than generating Conventional Commit messages. `.specify/extensions/git/git-config.yml` is the source of truth.

## Configuration

Resolve config using the Config Resolution Protocol in `llm-wiki/SKILL.md`:

0. **Inline vault override (`@name`)** — if the request contains an `@<name>` token, resolve `~/.obsidian-wiki/config.<name>` directly, overriding the steps below. See "Targeting a specific vault" right after this list.
1. **Walk up from CWD** — look for a `.env` file in the current directory, then each parent, up to `$HOME`. Stop at the first `.env` that contains `OBSIDIAN_VAULT_PATH`.
2. **Global config** — if no local `.env` is found, read `~/.obsidian-wiki/config`.
3. **Prompt setup** — if neither exists, tell the user to run `wiki-setup`.

The resolved config sets `OBSIDIAN_VAULT_PATH` (where the wiki lives). It may also set `OBSIDIAN_WIKI_REPO` (where this repo is cloned) and other optional variables.

### Targeting a specific vault

You can maintain multiple vaults (each a `~/.obsidian-wiki/config.<name>` file managed by `wiki-switch`) and reach any of them from any directory:

- **`@name` (per-invocation override)** — prefix or mention `@<name>` anywhere in a request to route that one command to that vault, e.g. `@work save this` or `wiki-query @personal what do I know about X`. It overrides the CWD `.env` and the active symlink **for that invocation only** — it does **not** flip your default vault. If `config.<name>` doesn't exist, the skill reports it and lists available vaults; do **not** silently fall back to the default. The `@name` is stripped before the rest of the request is used as content.
- **`/wiki-switch <name>` (persistent default)** — re-points the active symlink so all future requests use that vault. This is your default "brain" vault; use `@name` to dip into the other one without switching.

**After reading config, always read `$OBSIDIAN_VAULT_PATH/AGENTS.md` if it exists.** It contains owner-specific conventions (domain vocabulary, ingest preferences, writing style, project scoping) that override framework defaults for all skills. Apply it for the duration of the session.

## Campaign Co-DM

Load `wiki/AGENTS.md` before any write to `wiki/` (campaign `type`, `lifecycle`, `reveal`, complete-sentence prose).
Load `docs/agents/work.md` before Co-DM prep or wrapup output (Work gate: chat proposal; wiki write after DM accept).

The 019 loop lives in this file plus `docs/agents/work.md`. Wrapup owns the required reflection. No new skill.

### Table aim

If table aim is `missing`, ask the DM to name the players (at least one; tests use three) and the current campaign intent before treating Work as aimed.

### Gaps

A missing wiki fact or missing Co-DM practice MUST NOT prevent playable Work in that sitting. When Work is offered despite a gap, name the gap. A gap that is only wasted context is closed without a DM proposal — token cost, helpers, and layout below.

### Token cost

Record every finished prep or wrapup sitting with the ledger helper. Compare only same-kind sittings. The DM MUST NOT be asked to record or accept it.

Example: `python3 scripts/error-ledger.py sitting record --kind prep --job "…" --path-read "…" --skill "…" --helper error-ledger`

Cut wasted context without waiting. A change MUST NOT count as an improvement if it lowers token cost by lowering Work quality. A change MUST NOT count as an improvement if it raises token cost for the same jobs without preventing a named failure.

**Token measurement:** anything labeled tokens (including `WIKI_TOKEN_WARN_THRESHOLD`) uses tiktoken via `scripts/token-count.py` — default encoding `cl100k_base` (override `WIKI_TOKEN_ENCODING`). Do **not** use `file_size/4` as tokens. Method: `docs/agents/token-measurement.md` (issue #86).

**Context waste:** max tokens on content + reasoning, not plumbing. Prefer `hot.md`, `scripts/manifest.py`, and Retrieval Primitives over whole `index.md` / `log.md` / `.manifest.json`. **Highest priority:** reconcile conflicting/redundant skill+AGENTS instructions only when surviving text keeps (or improves) agent output quality; do not thin narrative, mechanics, or craft that raises outputs. Byte-count is not a success metric. Method: `docs/agents/context-waste-method.md` (issue #71). Run `python3 scripts/context-waste-scan.py` for path+metric leads (size flags are investigation leads, not delete mandates). No prose-quality scoring.

### Helpers

**Wiki maintenance loop:** weekday Layer A scans + fleet routing — `docs/agents/wiki-maintenance-loop.md` (issue #90). Quiet when clean. Never auto lore invent, mass kebab rename, dedup merge, or craft cuts.

After merges (or when starting box work), sync with `./scripts/git-sync-main` (feature branches only; never leave `main` dirty). Refuse unique local main commits; use `--force-clean` only to discard stranded dirt.

If a job will repeat and no existing command does it, create an agent-shaped helper without being asked. Arguments in, text or JSON out, exit done vs failed. Use it on the next same-kind sitting. Keep it current or remove it. No helper for a one-off. No wrap of an existing command.

### Error ledger

On runtime failure, append to `errors.md` before the sitting is complete. Drain matching entries when a wiki improvement or other landed fix actually removes the cause. Leftover entries for already-fixed causes are wasted context. The DM MUST NOT fill, review, or drain the ledger. A wiki fact write that is the fix still waits on accept; drain after that write lands.

Examples:
- `python3 scripts/error-ledger.py error append --cause "…" --sitting "prep: …"`
- `python3 scripts/error-ledger.py error drain --id e-N --cause-fixed true`
- `python3 scripts/error-ledger.py error list`

### Layout

As agent-facing files and the wiki (llm-wiki) grow mixed, regroup so one job or layout kind does not load unrelated trees. Trigger is `growth` (mixed dump / unrelated load). Not `tidiness`. One-off files MUST NOT be reorganized solely for tidiness. Live `wiki/entities/` growth uses the depth-1 `entities/{type}/` map in `wiki/AGENTS.md` (deterministic from frontmatter `type`); do not invent ad-hoc nests.

Wiki layout kinds: Encounters, Rules, Campaign State, DM Intelligence. Agent-facing layout kinds: System, Source Material. MUST NOT duplicate an existing `type`. Do not add `type: encounter` or `type: rules`. No layout-kind frontmatter.

Wiki layout moves have `facts_changed` false, `type_changed` false, and `links_resolve` true after the move. Source Material is `wiki/_raw/` staging. System is skills/`AGENTS.md`/`docs/agents`. System and Source Material MUST NOT be treated as wiki canon. Copying table aim onto DM Intelligence is not a layout move. Wiki fact changes still wait on accept.

## Writing and visual authorities

Reader is `agent` | `DM` | `players`. Unknown reader → `DM`. Vault is `true` if the destination is a wiki vault note, else `false`. Authorities are every matching row; they stack and do not cancel. Incomplete until all matching authorities are applied.

| Classifier | Authority |
|---|---|
| An agent will follow the text | writing-for-agents |
| The DM will read the text | copy-writer |
| Players will hear or see the text | theatre of the mind |
| Destination is a wiki vault note | obsidian-markdown |
| Working with visual references for a depiction | visual-references |
| Producing (attach, ground, generate, promote, place) a visual aid | visual-aids |

## Beat skill routing

| Job | Skill |
|---|---|
| Plan a session, one-shot, adventure arc, or expedition evening | `session-beats` |
| Write, edit, or create content for a Hook | `hook-beats` |
| Write, edit, or create content for a Development | `development-beats` |
| Write, edit, or create content for a Cliffhanger | `cliffhanger-beats` |
| Write, edit, or create content for a Climax | `climax-beats` |
| Write, edit, or create content for a Resolution | `resolution-beats` |

Unknown typed-beat job → classify the type first; do not default to `session-beats` for filling a beat. Named seams: `specs/017-session-beats-skills/contracts/beat-skill-routing.md`.

## Wiki kind routing

| Job | Skill |
|---|---|
| Write, edit, or create a named vehicle page | `vehicle-design` |
| Write, edit, or create a named spell page | `spell-design` |
| Write, edit, or create a named faction page | `faction-design` |
| Write, edit, or create a named lore page | `lore-design` |
| Write, edit, or create a named quest page | `narrative-islands` |
| Write, edit, or create a named city page | `city-design` |
| Write, edit, or create a named region page | `region-design` |
| Write, edit, or create a site place | `place-design` |

`place-design` is the hub for all places. It defers to `city-design` for `kind: city` and to `region-design` for region jobs.

## Skill design dispatch

Classify before any in-scope instruction file changes. Class is `design-impact` | `not`. Length MUST NOT be the gate.

Design-impact if the change is a novel skill, a skill redesign, or a major skill-file change. Creating a new skill or subagent is design-impact. Smaller edits to established files, Spec Kit pattern tweaks, and `AGENTS.md` are class `not`. Conserve Claude Code; use it only when necessary.

| Class | Writer |
|---|---|
| `design-impact` | designated writer |
| `not` | session agent |
| owner explicitly skips dispatch | session agent |

Writer is designated writer if design-impact (unless owner overrule), else session agent. Overrule is explicit owner skip only; silence is not overrule.

In-scope: source skill; standing instruction / sticky rule; subagent definition; writing-for-agents.
Out-of-scope: constitution; feature specs; generated Spec Kit adapters; campaign wiki.

Design-impact work: `docs/agents/skill-design-dispatch.md`.

## Vault retrieval

Search is on by default against collection `wiki`. Empty `QMD_WIKI_COLLECTION` still means `wiki`.

Load `.agents/skills/qmd` for query/get. Snippets are leads — `qmd get` / `qmd multi-get` before citing facts.

Order (`specs/004-qmd-search-default/contracts/retrieval-precedence.md`): `-c wiki` first; if silence `-c shattered-sea`; if silence `-c legacy-ss`; if still silence, say the wiki is silent.

Wiki hit = current canon. Legacy hit = campaign-of-record context; wiki write only after DM accept. Wiki vs legacy disagreement → cite wiki.

Collection `legacy` is the `legacy/` archive. Search it only with `-c legacy`. Do not add it to the wiki / shattered-sea / legacy-ss order.

If `qmd status` fails at session start, run `scripts/qmd-maintain.sh`. After wiki writes, wiki-ingest Step 8 runs that script. Exit 1: report the failure; already-written wiki pages stay.
`qmd query`, `qmd embed`, and `qmd vsearch` need the local LLM. Agent harnesses set `CI=true`, which makes qmd refuse those calls. Prefix them with `env -u CI`. The maintain script already does this.

## Vault Structure

```
$OBSIDIAN_VAULT_PATH/
├── index.md                # Master index — every page listed, always kept current
├── log.md                  # Chronological activity log (ingests, updates, lints)
├── hot.md                  # Session hot cache — ~500-word semantic snapshot of recent activity
├── .manifest.json          # Tracks every ingested source: path, timestamps, pages produced
├── _meta/
│   ├── taxonomy.md         # Controlled tag vocabulary
│   └── *.base              # Obsidian Bases dashboard definitions (wiki-dashboard skill)
├── _insights.md            # Graph analysis output (hubs, bridges, dead ends)
├── _raw/                   # Staging area — drop rough notes here, next ingest promotes them
├── _readouts/              # Derived narrative readouts saved by wiki-narrate — not knowledge pages
├── concepts/               # Abstract ideas, patterns, mental models
├── entities/               # Concrete things — people, tools, libraries, companies
├── skills/                 # How-to knowledge, techniques, procedures
├── references/             # Factual lookups — specs, APIs, configs
├── synthesis/              # Cross-cutting analysis connecting multiple concepts
├── journal/                # Time-bound entries — daily logs, session notes
└── projects/
    └── <project-name>.md   # One page per project synced via wiki-update
```

Every wiki page has required frontmatter: `title`, `category`, `tags`, `sources`, `created`, `updated`. Pages connect via internal links — `[[wikilinks]]` by default, or standard Markdown links when `OBSIDIAN_LINK_FORMAT=markdown` is set in config.

## Skill Routing

Skills live in `.agents/skills/<name>/SKILL.md`. Match the user's intent to the right skill. Beat-type routing and wiki-kind routing have their own tables above — this table covers everything else.

### Wiki

| User says something like… | Skill |
|---|---|
| "set up my wiki" / "initialize" | `wiki-setup` |
| "/wiki-history-ingest claude" / "import my Claude history" / "mine my Copilot sessions" / any agent-history ingest | `wiki-history-ingest` |
| "ingest" / "add this to the wiki" / "process these docs" / "/ingest-url <url>" / logs, transcripts | `wiki-ingest` |
| "what's the status" / "what's been ingested" / "show the delta" | `wiki-status` |
| "wiki insights" / "hubs" / "wiki structure" | `wiki-status` (insights mode) |
| "what do I know about X" / "find info on Y" / any question | `wiki-query` |
| "use my vault as context" / "context pack for X" / "bounded context" | `wiki-context-pack` |
| "narrate" / "briefing" / "explain this topic" | `wiki-narrate` |
| "audit" / "lint" / "find broken links" / "wiki health" | `wiki-lint` |
| "dedup my wiki" / "find duplicate pages" / "merge duplicates" | `wiki-dedup` |
| "rebuild" / "start over" / "archive" / "restore" | `wiki-rebuild` |
| "link my pages" / "cross-reference" / "connect my wiki" | `cross-linker` |
| "fix my tags" / "normalize tags" / "tag audit" | `tag-taxonomy` |
| "update wiki" / "sync to wiki" / "save this to my wiki" | `wiki-update` |
| `@work update wiki` / `wiki-query @personal ...` | Any matching wiki skill + Config Resolution Protocol `@name` override |
| "export wiki" / "export graph" / "export to OKF" | `wiki-export` |
| "import wiki" / "import from export" / "import OKF bundle" | `wiki-import` |
| "color my graph" / "color code obsidian" | `graph-colorize` |
| "save this" / "/wiki-capture" / "capture this" / "quick capture" / "drop to raw" | `wiki-capture` |
| "/wiki-research [topic]" / "research X" / "find everything about Y" | `wiki-research` |
| "create a dashboard" / "vault dashboard" / "show all X as a table" | `wiki-dashboard` |
| "synthesize my wiki" / "find connections" | `wiki-synthesize` |
| "/wiki-claude [topic]" / "/wiki-codex [topic]" / "/wiki-hermes [topic]" | `wiki-agent` |
| "/memory-bridge" / "browse codex memory" / "cross-tool memory" | `memory-bridge` |
| "/session-brain" / "build my session map" / "what topics have gone stale" | `session-brain` |
| "/wiki-sessions [topic]" / "which session did I do X in" | `session-search` |
| "/daily-update" / "morning sync" / "refresh the wiki index" | `daily-update` |
| "/wiki-switch NAME" / "switch vault" / "list my wikis" | `wiki-switch` |
| "/wiki-digest" / "weekly digest" / "what's new in my wiki" | `wiki-digest` |
| "/wiki-stage-commit" / "review staged pages" / "commit staged writes" | `wiki-stage-commit` |
| "restyle Obsidian" / "CSS snippet" / "tune tabs/sidebars/graph panes" | `obsidian-layout-adjustment` |

### Co-DM — session lifecycle

| User says something like… | Skill |
|---|---|
| "run the session" / "start the sitting" / live-play guidance | `run-guide` |
| "session wrapup" / "post-session" / end-of-session processing | `session-wrapup` |
| "session recap" / "what happened last session" / recap for players | `session-recap` |
| "plan the campaign" / "campaign arc" / "what's the long-term plan" | `campaign-planning` |
| "cold open" / "how should the session start" | `cold-opens` |
| "prep this encounter" / "build an encounter" / "encounter balance" | `encounter-prep` |
| "reconcile session evidence" / "what actually happened vs. wiki" | `reconciling-session-evidence` |

### Co-DM — world-building and design

| User says something like… | Skill |
|---|---|
| "design a dungeon" / "dungeon layout" / "map this dungeon" | `dungeon-design` |
| "homebrew monster" / "build a creature" / "stat block" | `homebrew-monsters-5e` |
| "design a magic item" / "homebrew item" | `dnd-5e-magic-item-design` |
| "design an NPC" / "build an NPC" / "NPC stat block" | `npc-design` |
| "design a trap" / "trial" / "puzzle" / "hazard" | `traps-trials` |
| "travel event" / "random encounter" / "journey event" | `travel-events` |
| "world tick" / "what happens off-screen" / "advance the world" | `world-tick` |
| "sandbox" / "player-driven narrative" / "open world" | `sandbox-narrative` |
| "interview my PC" / "character interview" / "backstory session" | `pc-interview` |
| "5e rules" / "how does X work in 5e" / mechanics question | `dnd5e-mechanics` |

### Co-DM — presentation and Foundry VTT

| User says something like… | Skill |
|---|---|
| "theatre of the mind" / "narrate this scene" / TotM description | `theatre-of-the-mind` |
| "polish this prose" / "rewrite for the DM" / DM-facing copy | `copy-writer` |
| visual reference for a depiction | `visual-references` |
| produce / attach / place a visual aid | `visual-aids` |
| "Foundry battlemap" / "build a map in Foundry" | `foundry-battlemap` |
| "Foundry scene" / "stage this in Foundry" | `foundry-stage` |
| "Foundry token" / "create a token" | `foundry-token` |

### Tooling and meta

| User says something like… | Skill |
|---|---|
| "search the wiki" / `qmd query` / semantic retrieval | `qmd` |
| "create a new skill" | `skill-creator` |
| "/vault-skill-factory" / "make a skill from my wiki" | `vault-skill-factory` |
| "research X" (general, not wiki-research) | `research` |
| "domain model" / "model this domain" | `domain-modeling` |
| "grill me" / "challenge my design" / "poke holes" | `grilling` |
| "grill with docs" / "challenge against the spec" | `grill-with-docs` |
| "write for agents" / "agent-facing prose" | `writing-for-agents` |
| "obsidian markdown" / link/frontmatter standards | `obsidian-markdown` |
| TDD / "write a test first" | `tdd` |

Spec Kit adapters (`speckit-*`) are generated harness integrations, not primary intent routes. Invoke them via `/speckit-<phase>` directly.

### Session history: ingest vs. retrieve

Three skills read agent session caches, and they are not interchangeable:

- `wiki-history-ingest` **ingests** — distils sessions into permanent vault pages. Handles all agent variants (Claude, Copilot, Codex, Hermes, OpenClaw, Pi) as modes.
- `wiki-agent` **ingests a slice** — finds sessions about one topic in another agent's history and pulls them into the vault.
- `session-brain` / `session-search` **retrieve** — build a topic graph over the raw sessions and find or load one. They write a sidecar at `~/.claude/session-brain/` and never touch the vault.

If the user wants knowledge preserved, ingest. If they want to find the session where something happened, retrieve.

## Cross-Project Usage

The main use case: you're working in some other project and want to sync knowledge into your wiki, query it, or compile bounded context. Three portable skills handle this — `wiki-update`, `wiki-query`, and `wiki-context-pack`. They work from any directory.

### wiki-update (write to wiki)

1. Resolve config using the Config Resolution Protocol to get `OBSIDIAN_VAULT_PATH`
2. Scan the current project: README, source structure, git log, package metadata
3. Distill what's worth remembering (architecture decisions, patterns, trade-offs — not code listings)
4. Write to `$VAULT/projects/<project-name>.md`, cross-linking to concept/entity pages as needed
5. Update the ingest ledger via `python3 scripts/manifest.py upsert …` (not a whole-file read), plus `index.md` and `log.md`

On repeat runs, use `scripts/manifest.py` (`has`/`get`/`delta`) for ledger checks — do not load all of `.manifest.json` into context. Project sync may still use `git log <last_commit>..HEAD` when `last_commit_synced` is present on the relevant entry.

### wiki-query (read from wiki)

1. Resolve config using the Config Resolution Protocol to get `OBSIDIAN_VAULT_PATH`
2. Scan titles, tags, and `summary:` frontmatter fields first (cheap pass)
3. Only open page bodies when the index pass can't answer
4. Return a synthesized answer with `[[wikilink]]` citations

### wiki-context-pack (read-only context)

1. Resolve the target vault and read its owner `AGENTS.md`
2. Rank existing notes without requiring schema migration
3. Compile summaries and selected excerpts within a hard token budget
4. Return a provenance-rich pack; never write it back to the vault

## Visibility Tags (optional)

Pages can carry a `visibility/` tag to mark their intended reach. **This is entirely optional** — untagged pages behave exactly as they always have (visible everywhere). The system stays single-vault, single source of truth.

| Tag | Meaning |
|---|---|
| *(no tag)* | Same as `visibility/public` — visible in all modes |
| `visibility/public` | Explicitly public — visible in all modes |
| `visibility/internal` | Team-only — excluded when querying in filtered mode |
| `visibility/pii` | Sensitive data — excluded when querying in filtered mode |

**Filtered mode** is opt-in, triggered by phrases like "public only", "user-facing answer", "no internal content", or "as a user would see it" in a query. Default mode shows everything.

`visibility/` tags are **system tags** — they don't count toward the 5-tag limit and are listed separately from domain/type tags in the taxonomy.

See `wiki-query` and `wiki-export` skills for how the filter is applied.

## Core Principles

- **Compile, don't retrieve.** The wiki is pre-compiled knowledge. Update existing pages — don't append or duplicate.
- **Track everything.** After ingest, `python3 scripts/manifest.py upsert` for the source (never whole-file read of `.manifest.json`); update `index.md`, `log.md`, and `hot.md` after writes.
- **Connect with `[[wikilinks]]`.** Every page should link to related pages. This is what makes it a knowledge graph, not a folder of files.
- **Frontmatter is required.** Every wiki page needs: `title`, `category`, `tags`, `sources`, `created`, `updated`.
- **Single source of truth.** Visibility tags shape how content is surfaced — they don't duplicate or separate it.
- **Keep context warm.** `hot.md` is a ~500-word semantic snapshot of recent activity. Every write skill updates it so the next session can pick up where the last one left off without crawling the full vault.

## Sources of Truth

Each fact has one owner. Do not restate these in harness config, generated adapters, or orchestrator skills.

| Owner | Owns |
|---|---|
| `.specify/memory/constitution.md` | Non-negotiable project principles |
| `specs/<feature>/spec.md` | Feature behavior and requirements |
| `specs/<feature>/plan.md` | Feature technical design |
| `specs/<feature>/tasks.md` | Feature implementation work graph |
| `docs/` | Architecture, domain docs, harness dispatch procedure |
| Source + tests | Executable truth |
| Harness runtime files (`.omp/config.yml`, etc.) | That harness's runtime concerns only |
| Spec Kit generated adapters | Harness invocation of Spec Kit phases (disposable) |

Orchestrator procedure: `docs/agents/harness-dispatch.md`.

## Workflow

Spec Kit artifacts are the handoff protocol. Harness files must not copy feature requirements.

- **Read, don't re-specify.** When a feature already has `specs/<feature>/{spec,plan,tasks}.md`, consume those artifacts. Do not reconstruct the feature from the original prompt.
- **Spec-first changes.** When intended behavior must change, update the specification first, then reconcile plan and tasks, then implement. Do not silently redefine requirements in `tasks.md` or code.
- **One writer per artifact.** At any moment each canonical artifact (spec, plan, tasks, writable workspace) has at most one writer. Others may inspect, review, test, or propose.
- **Separate workspaces for parallel work.** Multiple write-capable harnesses must not share one writable workspace.
- **Handoff is repository state.** Changing harness passes paths, commits, artifacts, expected phase, and only constraints absent from the repo — not pasted copies of canonical documents.

## Validation

- Spec Kit status: `specify integration status --json` — must be `ok`, default `omp`, four integrations installed.
- OMP baseline: `scripts/check-omp-baseline.sh` — exit 0.

## Architecture Reference

For the full pattern (three-layer architecture, page templates, project org), read `.agents/skills/llm-wiki/SKILL.md`.

Human-facing documentation lives in `docs/` — `installation.md`, `agents.md`, `skills.md`, `cli.md`, `configuration.md`, `architecture.md`, `session-brain.md`, `contributing.md`. `README.md` is a landing page only; when you add a skill, CLI command, or config variable, update the matching `docs/` page rather than the README.

The vault format is structurally conformant with the [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — markdown files with YAML frontmatter, category subfolders, reserved `index.md`/`log.md`. `wiki-export` (OKF mode) and `wiki-import` are the bridge: they translate between our native frontmatter (`title`/`category`/`tags`/`sources`/`created`/`updated` + `summary`) and OKF (`type`/`title`/`description`/`resource`/`tags`/`timestamp`), making vaults exchangeable with any OKF tool. The OKF round-trip is lossless; the `graph.json` round-trip is not.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
at specs/019-self-improving-codm/plan.md
<!-- SPECKIT END -->
