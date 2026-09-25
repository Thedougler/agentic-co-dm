# Obsidian Wiki — Agent Context

A **skill-based framework** for building and maintaining an Obsidian knowledge base. Skills and instructions carry the behavior; `tools/` and `scripts/` implement the checks they call.

## Repo map

Top-level paths, one purpose each; the vault itself is explored under "Vault map" below. Which artifact owns which fact → "Sources of Truth".

| Path | What it is, and what sends you there |
| --- | --- |
| `CONTEXT.md` | Domain glossary. Reach it for terminology, architecture, template, or beat-design decisions. |
| `.agents/skills/<name>/` | Skill source (`SKILL.md`, `references/`, `evals/`). Edit here; imported skills are pinned in `skills-lock.json`. |
| `.agents/skills/llm-wiki/` | The llm-wiki spec: three-layer architecture (raw sources → wiki → schema), page templates, provenance and trust model, wiki environment variables. The authority behind the vault map below and "Core Principles". |
| `docs/agents/` | Procedure docs: Work, table-ready casting, hybrid SDD, maintenance loop, token and context measurement, harness and skill-design dispatch. |
| `docs/adr/`, `docs/*.md` | Decision records; human-facing documentation. |
| `tools/` | Python implementation: `lint_wiki.py`, `wiki_ops/` (transactions, health, identity, template contracts), `creative_lint/` (Vale engine, rule registry, evaluators), `token_count.py`. |
| `scripts/` | CLI entrypoints — `wiki`, `wiki-lint`, `wiki-maintain`, `wiki-bulk-ops`, `manifest.py`, `error-ledger.py`, `luna-eval`, `wiki-reveal`, plus focused `check-*` / `lint-*` / `remorph-*` helpers. Unknown command → list the directory; each is `--help`-able. |
| `tests/` | Pytest suite over `scripts/` and `tools/`. Run `./scripts/run-pytest`. |
| `specs/<feature>/` | Spec, plan, tasks, contracts. Current feature: `029-agent-loop-closure`. |
| `.specify/` | Constitution, templates, extensions, generated adapters (adapters disposable). |
| `wiki/` | The live vault, at the path `.env` `OBSIDIAN_VAULT_PATH` and `pyproject.toml` `[tool.agentic-co-dm]` both name. Campaign pages, templates, session journals, indexes. Load `wiki/AGENTS.md` before any read or write here. Expanded below. |
| `rules/`, `styles/`, `.vale.ini` | Creative-lint rule registry, bundles, waivers, Vale styles. Rule or prose-lint work. |
| `config/efficiency.yaml` | Maintainer-owned efficiency policy; agents read and propose only. |
| `.omp/` | OMP runtime: `config.yml`, `AGENTS.md`, `RULES.md`, `rules/`, `hooks/`, `commands/`, `agents/`. Harness behavior, hooks, subagent definitions. |
| `.claude/`, `.cursor/`, `.kiro/`, `.pi/`, `.windsurf/`, `.grok/`, `.agent/`, `.github/`, `.hermes.md`, `CLAUDE.md`, `CODEX.md`, `GROK.md` | Other harness entrypoints. Their `skills/` are copies or symlinks of `.agents/skills/` — edit the source, not the copy. |
| `.qmd/` | QMD collections in `index.yml` (`wiki` canonical; `shattered-sea` and `legacy-ss` read-only legacy), plus the gitignored local index. |
| `errors.md`, `sittings.jsonl` | Error ledger and sitting ledger data, at repo root. Runtime failure; sitting record. |
| `mcp.json`, `foundry-data/` | Local Foundry MCP config and data (gitignored). Foundry staging. |

Local-only, neither canon nor hand-edited: `.venv/`, `_archive/`, `legacy/`, `*-workspace/` (skill-creator eval runs), `.local/efficiency/`, `wiki/.obsidian/` UI state.

### Vault map (`wiki/`)

Explored layout of the live vault. Vault semantics stay in `wiki/AGENTS.md`; page format stays in `llm-wiki`.

```text
wiki/                          # the live campaign vault
├── AGENTS.md                  # vault owner conventions — load before any read or write here
├── index.md                   # master index, every page listed
├── log.md                     # chronological ingest/update/retcon log
├── hot.md                     # ~500-word snapshot of recent activity — read this first
├── .manifest.json             # ingested-source ledger; query via scripts/manifest.py, never load whole
├── entities/{type}/           # campaign pages, depth 1 by frontmatter type — creature, faction, item,
│                              #   lore, npc, pc, place, quest, region, spell, vehicle (kebab basenames)
├── journal/sessions/<campaign-slug>/<NN>/   # plan, typed beats, recap (e.g. shattered-sea/12/)
├── synthesis/                 # players, story-so-far, dm-voice-notes, party-combat-profile
├── templates/                 # one page template per kind; contracts/*.yml = per-type frontmatter contract
├── attachments/               # flat {subject-slug}-{role}.{ext}; roles in attachments/README.md
├── _meta/                     # taxonomy.md (controlled tag vocabulary), lint-cache.json
├── _raw/                      # capture inbox — the next ingest promotes from here
├── _archive/                  # promoted and demoted pages; not canon
└── .obsidian/                 # vault UI config, graph colors, CSS snippets
```

Every page carries required frontmatter and connects by `[[wikilinks]]` (`OBSIDIAN_LINK_FORMAT=wikilink` here; `markdown` switches to standard links). The generic llm-wiki categories `concepts/`, `skills/`, `references/`, and `projects/` are unused in this vault — campaign knowledge files under `entities/{type}/`.

## Project domain terms

Before campaign architecture, session design, beat or skill guidance, template changes, or any terminology decision, read [`CONTEXT.md`](CONTEXT.md). It is the reusable project glossary: use its canonical terms, surface conflicts, and update it in the same change when a domain term is clarified. Keep it free of implementation details and transient campaign facts.

## README Translation Parity

`README.md` and `README_TW.md` are one documentation surface. Keep headings, examples, links, and user-facing behavior aligned between the two translations. The check is advisory and never blocks a PR: the `readme-translation-drift` CI job only reports drift. Run `python3 tools/check_readme_sync.py` to list commits that changed `README.md` without a later `README_TW.md` update, along with the pending English diff — then translate and backfill those changes into `README_TW.md`. Reviewers assess translation quality.
## Spec Kit Git Automation

Spec Kit auto-commit is enabled for the configured before/after hooks. The commit style is fixed (`commit_style: fixed`); use the configured `[Spec Kit] ...` messages rather than generating Conventional Commit messages. `.specify/extensions/git/git-config.yml` is the source of truth.

## Hybrid SDD routing

Before writing substantial engineering, agent-system, campaign-architecture, or creative-system work, classify it once and follow the full route in [`docs/agents/hybrid-sdd.md`](docs/agents/hybrid-sdd.md). Routine established campaign content stays on its existing skill, template, and Work route; split mixed requests into their system-changing and routine-content slices. Keep the managed Spec Kit block below disposable.

**Capability loop:** For every incomplete owner boundary, `observe → act → re-observe`; continue only on owner-relative progress or a passed completion guard. An unchanged observation requires a materially different sanctioned path or a specific blocker. Use [`docs/agents/hybrid-sdd.md`](docs/agents/hybrid-sdd.md) for the full rule and blocker fields.

<a id="friction-rule"></a>**Friction rule:** Friction is a failing command, a stale path, or wrong or missing guidance, including an instruction you routed around because the command, path, or step it names does not exist. On friction, identify its cause, fix the authoritative source with the smallest change, then prove the fix with the check or test that catches the cause, adding one when none exists (for a script path in a skill or AGENTS.md, run `scripts/check-current-commands` and see that file pass), then continue the original task. Friction is a branch of the capability loop, not a new workflow, command, or skill.

## Carve-outs

Constitution XXV. The user's named set is the work set. *Everything* means that whole set.
Implement one *uniform* *composed* path.

A filter, except list, hardcoded special case, or smallest-slice reading of a whole-set
instruction is a carve-out. Add one only after that rule already failed in this repo; name
the failure on it.

**Done when:** the change applies to the named set; the written rule has no proactive exclude list.

## Canon and done-summary

Canon: apply the rule in [`llm-wiki`](.agents/skills/llm-wiki/SKILL.md#canon) (constitution X) and file what it makes canon.

Lint contract (constitution XXI): `wiki lint` runs every checker, Vale included, and every finding it reports is an issue to fix. Use `next.path`, then `wiki lint fix <next.path>` for deterministic repairs; rerun `wiki lint <next.path>` for the remaining issues. `--full` is accepted as a compatibility no-op. Iterate until clean: zero issues. Do not ask. Do not interrupt with findings.

When clean, one short done-summary: what changed, where. No question. No wait.

Mixed request: do every requested slice, then one done-summary when clean.

FR-002 repair, template conformance of existing content, named ingest, and bookkeeping run unattended. Dedup merge without a user ask still confirms (destructive, not a Work wait). User-asked merge files.

**Done when:** requested work is filed; `wiki lint` is clean; every other checkable rule passes; one done-summary was emitted.

## Project identity

Primary deliverables are skills, agent instructions, and guidance documents. Scripts and tooling support those. Review of agent-skill changes uses the `skill-creator` eval loop (held-out prompts, with-skill vs without-skill, graded assertions grounded in live wiki content — not vacuum scenarios). Every skill evaluation, behavioral test, benchmark, and related validation MUST use the weakest available model that can complete the task with cold, focused context; weaker models expose unclear guidance, and stronger models benefit from the same clarity. The `skill-creator` workflow is reserved for modifying agent skills; other instruction, documentation, and system changes use their applicable workflow. MUST NOT add a checklist, PR template, or review skill. Coverage and type-safety MUST NOT be the primary bar.


## Configuration

Resolve config:

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

Load `wiki/AGENTS.md` before any write to `wiki/` (campaign `type`, `reveal`, complete-sentence prose).
Load `docs/agents/work.md` before Co-DM prep or wrapup output (table aim and reflection; file what constitution X makes canon).

The 019 loop lives in this file plus `docs/agents/work.md`. Reflection is offered after a session sitting outside `session-recap` (that skill is narrative recap only). No new skill.

### Table aim

If table aim is `missing`, ask the DM to name the players (at least one; tests use three) and the current campaign intent before treating Work as aimed.

### HARD: entity-before-spoken (Nick 2026-09-14)

**Production session content** (session-prep beats, TotM/`[!narration]`, action cards, spoken text) is **complete or it does not ship**. Vague/non-specific descriptions of unnamed people/things because the entity page is missing = **critical error**.

**Dependency order (recursive):** If a beat/scene names or requires an NPC, item, creature, place, faction, vehicle, spell, quest, or other entity — load that kind's **owner skill** (Wiki kind routing, Beat skill routing, or Skill Routing), **cast or mint that owner page first** (cast before minting: `docs/agents/table-ready.md`; kebab basename, matching `wiki/templates/`, live vault path), **then** write/update the session/TotM text that depends on it. A new named owner the user asked to introduce is filed first; spoken that depends on it follows. Existing wiki content MUST NOT wait. The DM cannot describe what does not exist.

Agents MUST complete **all** recursive dependency steps to finish the goal — not only top-level, intermediary, or initial steps — in dependency order. Applies to `session-beats`, typed beat skills, `theatre-of-the-mind`, `cold-opens`, `session-recap`, and Session Architect orchestration. Completeness gate — do **not** thin narrative craft.

### Focused minting

Problem: minting several new page types in one task blurs ownership and wastes context. When a task requires new owners of multiple types, create one focused subtask per type and delegate each mint to a subagent using that type's owner skill. Keep dependent types serial; run independent types in parallel only when their canonical write surfaces are disjoint. The parent agent owns dependency order, integration, and final verification. This follows Mike Shea's practice of separating characters, NPCs, locations, and session notes for legible prep ([source](https://slyflourish.com/organizing_notes.html)).

### HARD: dm-facing-explicit (Nick 2026-09-14)

**DM-facing content** (`visibility: dm`, action cards, Be ready for, secrets, situation facts, Wiki facts, owner pages): **no vagueness, non-specific placeholders, coy narration, or mystery without a DM answer.** The DM must have **all** scene/world facts available immediately. Making the DM decode coy agent writing = **critical error**.

**Clarify vs player-safe TotM:** Player-facing `[!narration]` may withhold from *players*; it must still be grounded in named entities that exist (**HARD: entity-before-spoken**). DM layers must state who/what/where/why concretely — names, wants, true stakes — with a DM answer on the page for every planted mystery.

**FAIL:** “a woman in the woods,” “unnamed survivors,” “something watches,” mystery with no DM answer on the page.
**PASS:** Named `[[npc]]` with look/want/voice; named place; stated true invitation/threat.

Applies to the same session-prep / TotM / recap / Session Architect surfaces. Pairs with entity-before-spoken — do **not** thin craft.

### Gaps

A missing wiki fact or missing Co-DM practice MUST NOT prevent playable Work in that sitting — **except** the entity-before-spoken and dm-facing-explicit HARD gates above (missing owners for named production-session dependencies, and coy/vague DM layers, are not allowed gaps). When Work is offered despite a non-HARD gap, name the gap. A gap that is only wasted context is closed without a DM proposal — token cost, helpers, and layout below.

### Token cost

Record every finished prep or wrapup sitting with the ledger helper. Compare only same-kind sittings. The DM MUST NOT be asked to record or accept it.

Example: `python3 scripts/error-ledger.py sitting record --kind prep --job "…" --path-read "…" --skill "…" --helper error-ledger`

Cut wasted context without waiting. A change MUST NOT count as an improvement if it lowers token cost by lowering Work quality. A change MUST NOT count as an improvement if it raises token cost for the same jobs without preventing a named failure.

**Token measurement:** anything labeled tokens (including `WIKI_TOKEN_WARN_THRESHOLD`) uses tiktoken via `scripts/token-count.py` — default encoding `cl100k_base` (override `WIKI_TOKEN_ENCODING`). Do **not** use `file_size/4` as tokens. Method: `docs/agents/token-measurement.md` (issue #86).

**Context waste:** max tokens on content + reasoning, not plumbing. Prefer `hot.md`, `scripts/manifest.py`, and Retrieval Primitives over whole `index.md` / `log.md` / `.manifest.json`. **Highest priority:** reconcile conflicting/redundant skill+AGENTS instructions only when surviving text keeps (or improves) agent output quality; do not thin narrative, mechanics, or craft that raises outputs. Byte-count is not a success metric. Method: `docs/agents/context-waste-method.md` (issue #71). Run `python3 scripts/context-waste-scan.py` for path+metric leads (size flags are investigation leads, not delete mandates). No prose-quality scoring.

## Wiki writes

Every wiki write goes to its live path. `_raw/` remains the ingest inbox; `_archive/` holds promoted sources. Every file entering `wiki/` is complete only when `wiki lint` is clean for it.

## Edit discipline

Re-read the target file before a multi-hunk edit. Stale line numbers produce overlapping hunks that the edit tool rejects wholesale. When replacing a large section, use one replacement covering the full range rather than multiple adjacent hunks that share boundary lines. Deletions are standalone operations — do not prefix deletion directives with replacement-body syntax.

**Manual merges only.** When merging wiki pages (dedup, digest, consolidation), agents MUST read both files and edit the canonical page by hand — no scripts, no automated merge tools, no batch text-processing commands. The agent reads, decides what to keep, and writes the result through the Edit/Write tools.

**Inline extraction over shell one-liners.** When extracting or transforming tool output (lint JSON, manifest records, search results), use Python with `json.loads` in a script file or a clean `python3 -c` invocation. Nested shell-in-Python-in-shell quoting (backticks inside `$()` inside single quotes) breaks silently or raises parse errors. Write a short script to the scratchpad directory when the extraction has more than one step.

## Helpers

**Wiki maintenance loop:** weekday Layer A scans + fleet routing — `docs/agents/wiki-maintenance-loop.md` (issue #90). Quiet when clean. Never auto lore invent or craft cuts. Filename kebab / Aruhe / `00` remorph runs unattended. Dedup merge without a user ask still confirms.

Wiki canon (`wiki/` campaign pages, ingest, recap, `hot.md`/`index.md`/`log.md`): commit on `main` and push `main`. Agent instructions (skills, `AGENTS.md`, `docs/agents`, harness, agent-facing scripts): feature branch and PR. Mixed sitting: split those two commits. After merges, `./scripts/git-sync-main` from a feature branch (`--force-clean` only for stranded dirt).

If a job will repeat and no existing command does it, create an agent-shaped helper without being asked; load `cli-for-agents` first (constitution VI). Arguments in, text or JSON out, exit done vs failed. Use it on the next same-kind sitting. Keep it current or remove it. No helper for a one-off. No wrap of an existing command.

### Error ledger

A runtime failure is friction: fix and verify its source, then continue ([friction rule](#friction-rule)). `errors.md` holds only causes still open. Record one with `error append --source <path the fix lands in>` only when that fix cannot land in the current task. Drain it with `error drain --id e-N` in the same commit as the verified fix; an entry whose cause is already fixed is wasted context, so drain it when you find it. The ledger is agent-owned: the DM never fills, reviews, or drains it.

Same cause: `append` attaches an identical cause on the same source by itself. For a differently worded failure, pass `--attach e-N` when the fix for e-N would also remove it; otherwise `append` creates a new entry. Undo a wrong attach with `error detach --id e-N --index k`, using the `occurrence_index` that `append` reported. Invocations and examples: `python3 scripts/error-ledger.py error append --help`.

### Layout

As agent-facing files and the wiki (llm-wiki) grow mixed, regroup so one job or layout kind does not load unrelated trees. Trigger is `growth` (mixed dump / unrelated load). Not `tidiness`. One-off files MUST NOT be reorganized solely for tidiness. Live `wiki/entities/` growth uses the depth-1 `entities/{type}/` map in `wiki/AGENTS.md` (deterministic from frontmatter `type`); do not invent ad-hoc nests.

Wiki layout kinds: Encounters, Rules, Campaign State, DM Intelligence. Agent-facing layout kinds: System, Source Material. MUST NOT duplicate an existing `type`. Do not add `type: encounter` or `type: rules`. No layout-kind frontmatter.

Wiki layout moves have `facts_changed` false, `type_changed` false, and `links_resolve` true after the move. Source Material is `wiki/_raw/` staging. System is skills/`AGENTS.md`/`docs/agents`. System and Source Material MUST NOT be treated as wiki canon. Copying table aim onto DM Intelligence is not a layout move. Wiki fact changes file under constitution X.

## Writing and visual authorities

Reader is `agent` | `DM` | `players`. Unknown reader → `DM`. Vault is `true` if the destination is a wiki vault note, else `false`. Authorities are every matching row; they stack and do not cancel. Incomplete until all matching authorities are applied.

| Classifier | Authority |
|---|---|
| An agent will follow the text | writing-for-agents |
| The DM will read the text | writing-for-humans |
| Players will hear or see the text | theatre of the mind |
| Destination is a wiki vault note | obsidian-markdown |
| Working with visual references for a depiction | visual-references |
| Producing (attach, ground, generate, promote, place) a visual aid | visual-aids |

## Capability execution contract

Root routing selects the existing owner capability directly from intent or
artifact kind. Each capability owns its procedure, specialized craft, local
handoffs, and completion guard.

Every capability boundary is legible through four concepts, using headings or
clear equivalents:

- **Input** — owned intent, target, evidence, and constraints.
- **Work** — owner-specific procedure and safeguards using the minimum context
  projection; focused retrieval resumes the same owner when evidence is insufficient.
- **Done** — observable output-contract, evidence, or scoped-validation result.
  Prose existence is never enough.
- **Capability Handoff** — the bounded artifact or operation, receiving owner,
  return evidence, and parent resume point when ownership changes.

The parent operation retains the user's objective. Children own only bounded
artifacts or operations and return evidence before the parent resumes. Real
prerequisites run first; disjoint canonical write surfaces may run concurrently;
a shared surface has one active writer. Read capabilities return cited evidence
without mutating canonical wiki pages, manifests, indexes, or logs.

Load only owner instructions, target evidence, relevant canon, governing
template or contract, validation evidence, dependencies, and deliberate
omissions for the current capability. Do not inherit unrelated artifact groups.
Do not create a generic router, workflow engine, global DAG, second owner
registry, or persistent execution ledger.

Use `docs/agents/hybrid-sdd.md` for substantial cross-capability composition
and `wiki/AGENTS.md` for wiki semantics. Neither duplicates owner procedure.

## Beat skill routing

| Job | Skill |
|---|---|
| Plan a session, one-shot, adventure arc, or expedition evening | `session-beats` |
| Write, edit, or create content for a Hook | `hook-beats` |
| Write, edit, or create content for a Development | `development-beats` |
| Write, edit, or create content for a Cliffhanger | `cliffhanger-beats` |
| Write, edit, or create content for a Climax | `climax-beats` |
| Write, edit, or create content for a Resolution | `resolution-beats` |

Unknown typed-beat job → classify the type first; do not default to `session-beats` for filling a beat. Every beat and run guide is written from the session's filed session plan (the short form of the DM's intent); when none exists, `plan-session` shapes the intent with the DM and `session-beats` files the plan first. Named seams: `specs/017-session-beats-skills/contracts/beat-skill-routing.md`. Before filling any typed beat or TotM spoken block, satisfy **HARD: entity-before-spoken** (mint required owners first via the **owner skill**) and **HARD: dm-facing-explicit** (DM layers concrete; no coy placeholders).

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

`place-design` is the hub for all places. It defers to `city-design` for `kind: city` and to `region-design` for region jobs. Unknown kind → Skill Routing.

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

**QMD before grep.** Search QMD first for wiki content; use grep only for targeted evidence QMD cannot answer (exact line numbers, regex matches, file existence checks). Grep-first for wiki content violates retrieval precedence and produces lower-quality results.

Search is on by default against collection `wiki`. Empty `QMD_WIKI_COLLECTION` still means `wiki`.

Load `.agents/skills/qmd` for query/get. Snippets are leads — `qmd get` / `qmd multi-get` before citing facts.

### Exact QMD retrieval

Search the selected collection first, then pass the exact returned `#docid` or
`qmd://` source to `qmd get` / `qmd multi-get` verbatim. Use collection `wiki`
when `QMD_WIKI_COLLECTION` is empty. Never construct, URL-encode, or infer a
QMD document path from an Obsidian filename; the search result is the identifier.
`multi-get` takes comma-separated `#docid` values (`"#a,#b"`) or brace-expanded
paths — not `qmd://` URIs, not percent-encoded strings. If `multi-get` rejects
an identifier, fall back to serial `qmd get`.

**`qmd get` line-range syntax:** the range goes on the path, not `--format`.

```bash
# CORRECT — line range on the path argument
qmd get "qmd://entities/faction/the-passage.md:1:20" --format md

# WRONG — line range in --format (CLI rejects md:1:20)
qmd get "qmd://entities/faction/the-passage.md" --format md:1:20
```

**`multi-get` accepts `#docid` values or path globs, not search-result URIs:**

```bash
# CORRECT — comma-separated #docid values from search results
qmd multi-get "#abc123,#def456" --format md

# CORRECT — brace-expanded paths
qmd multi-get 'entities/faction/{the-passage.md,antheri.md}' --format md

# WRONG — qmd:// URIs (rejected with "File not found")
qmd multi-get "qmd://entities/faction/the-passage.md,qmd://entities/faction/antheri.md"
```

When `multi-get` rejects an identifier, do not retry with a different format — fall back to serial `qmd get` immediately.

**`qmd skill show` may time out** (~30s). If it does, skip it and use `qmd query` / `qmd get` directly — the bootstrap skill in `.agents/skills/qmd/SKILL.md` is sufficient.

Order (`specs/004-qmd-search-default/contracts/retrieval-precedence.md`): `-c wiki` first; if silence `-c shattered-sea`; if silence `-c legacy-ss`; if still silence, say the wiki is silent. `-c archive` holds `wiki/_archive/` (not canon, out of default search): use it only for a page's history.

Wiki hit = current canon. Legacy hit = campaign-of-record context. File user-said canon immediately. Wiki vs legacy disagreement → cite wiki.


If `qmd status` fails at session start, run `scripts/qmd-maintain.sh`. After wiki writes, wiki-ingest Step 8 runs that script. Exit 1: report the failure; already-written wiki pages stay.
`qmd query`, `qmd embed`, and `qmd vsearch` need the local LLM. Agent harnesses set `CI=true`, which makes qmd refuse those calls. Prefix them with `env -u CI`. The maintain script already does this.

### Direct `main` push protocol

When pushing commits directly to `main`, use native Git in this order:

1. Run `git fetch origin main`.
2. Run `git rebase origin/main` and resolve any conflict before continuing.
3. Run `git push origin HEAD:main`.
4. If the push is rejected as non-fast-forward, repeat fetch → rebase → push
   at most two more times. Stop after three total attempts or immediately on a
   rebase conflict; leave the branch for manual resolution.

`scripts/git-sync-main` remains the pre-work sync/reset helper and does not
replace this push protocol or perform pushes.

## Skill Routing

Match the user's intent to the right skill. Beat-type routing and wiki-kind routing have their own tables above — this table covers everything else. Minting a named campaign page loads that kind's **owner skill** first.

### Wiki

| User says something like… | Skill |
|---|---|
| "set up my wiki" / "initialize" | `wiki-setup` |
| "ingest" / "add this to the wiki" / "process these docs" / "/ingest-url <url>" / logs, transcripts | `wiki-ingest` |
| "what's the status" / "what's been ingested" / "show the delta" | `wiki-status` |
| "wiki insights" / "hubs" / "wiki structure" | `wiki-status` (insights mode) |
| "what do I know about X" / "find info on Y" / any question | `wiki query` for retrieval; `wiki-query` owns synthesis and citations |
| "use my vault as context" / "context pack for X" / "bounded context" | `wiki-context-pack` |
| "narrate" / "briefing" / "explain this topic" | `wiki-narrate` |
| "lint" / "lint <page>" / "fix broken links" / "audit" | `wiki lint` — full finding dump |
| "wiki health" / "health check" | `wiki health`; act on `context.act`, then `next`, then remaining `focus` |
| "dedup my wiki" / "merge duplicates" / "identity resolution" | `wiki-dedup` (standalone deep identity-resolution scan; wiki-lint Check 14 handles dedup in normal lint flow) |
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
| "restyle Obsidian" / "CSS snippet" / "tune tabs/sidebars/graph panes" | `obsidian-layout-adjustment` |

### Wiki CLI

```bash
wiki lint [path ...]
wiki query "<phrase>"
wiki health
```

stderr `tune` names a checker. Fix it this sitting.

### Co-DM — session lifecycle

| User says something like… | Skill |
|---|---|
| "run the session" / "start the sitting" / live-play guidance | `run-guide` |
| "session wrapup" / "post-session" / "session recap" / "what happened last session" / recap for players | `session-recap` (sole narrative skill → `Session-<NN>-Recap.md`; `session-wrapup` retired) |
| "/plan-session" / "let's plan the next session" / "brainstorm the session" / "what should happen next session" | `plan-session` |
| "plan the campaign" / "campaign arc" / "what's the long-term plan" | `campaign-planning` |
| "cold open" / "how should the session start" | `cold-opens` |
| "prep this encounter" / "build an encounter" / "encounter balance" | `encounter-prep` |
| "reconcile session evidence" / "what actually happened vs. wiki" | `reconciling-session-evidence` |

### Co-DM — world-building and design

| User says something like… | Skill |
|---|---|
| "design a dungeon" / "dungeon layout" / "map this dungeon" | `dungeon-design` |
| "design a monster" / "homebrew monster" / "build a creature" / "stat block" | `monster-design` + mandatory `dnd5e-mechanics` pass |
| "design an item" / "design a magic item" / "homebrew item" | `item-design` + mandatory `dnd5e-mechanics` pass |
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
| "polish this prose" / "rewrite for the DM" / DM-facing copy | `writing-for-humans` |
| visual reference for a depiction | `visual-references` |
| produce / attach / place a visual aid | `visual-aids` |
| "Foundry battlemap" / "build a map in Foundry" | `foundry-battlemap` |
| "Foundry scene" / "stage this in Foundry" | `foundry-stage` |
| "Foundry token" / "create a token" | `foundry-token` |

### Tooling and meta

| User says something like… | Skill |
|---|---|
| "search the wiki" / `qmd query` / semantic retrieval | `qmd` |
| create or change a repository command: new script, flags, `--help`, errors, output | `cli-for-agents` |
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

Two kinds of skill read agent session caches, and they are not interchangeable:

- `wiki-agent` **ingests** — finds sessions about one topic in an agent's history and distils them into vault pages.
- `session-brain` / `session-search` **retrieve** — build a topic graph over the raw sessions and find or load one. They write a sidecar at `~/.claude/session-brain/` and never touch the vault.

If the user wants knowledge preserved, ingest with `wiki-agent`. If they want to find the session where something happened, retrieve.

## Cross-Project Usage

The main use case: you're working in some other project and want to sync knowledge into your wiki, query it, or compile bounded context. Three portable skills handle this — `wiki-update`, `wiki-query`, and `wiki-context-pack`. They work from any directory.

### wiki-update (write to wiki)

1. Resolve config using the Config Resolution Protocol to get `OBSIDIAN_VAULT_PATH`
2. Scan the current project: README, source structure, git log, package metadata
3. Distill what's worth remembering (architecture decisions, patterns, trade-offs — not code listings)
4. Write to `$VAULT/projects/<project-name>.md`, cross-linking to concept/entity pages as needed
5. Record a completed source once with `python3 scripts/manifest.py record … --pages …` (not a whole-file read), plus `index.md` and `log.md`

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
- **Track llm-wiki operations.** After ingest or another source-backed update, record the source with `python3 scripts/manifest.py record`; update `index.md`, `log.md`, and `hot.md`. Lint and lint repair do not write `log.md`.
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
`.omp/AGENTS.md` is the OMP-only runtime addendum; when operating under OMP, read it for harness-specific edge cases.
When operating under Codex or Grok Build, read `CODEX.md` or `GROK.md` respectively for harness-specific companion guidance.

Orchestrator procedure: `docs/agents/harness-dispatch.md`.

## Workflow

Spec Kit artifacts are the handoff protocol. When `specs/<feature>/{spec,plan,tasks}.md` exist, consume them — do not reconstruct. Behavior changes update the spec first, then plan/tasks, then code. One writer per artifact at a time. Changing harness passes repo state (paths, commits, phase), not pasted copies.

## Validation

- **Python runtime:** use `.venv/bin/python` for pytest and repository tooling — system `python3` may lack project dependencies. `python3 scripts/*.py` works because those scripts import only stdlib and local modules; test runs and library imports require the venv.
- **Spec Kit availability:** Invoke `specify --version` before deciding the CLI
  is absent. If shell resolution fails, inspect the existing executable at
  `~/.local/bin/specify` and its resolved target; `uv tool list` is not
  authoritative for an executable already on disk. Repair a stale uv
  registration with the documented install command rather than running
  `specify init` over this already-initialized checkout.
- Spec Kit status: `specify integration status --json` — must be `ok`, default `omp`, four integrations installed.
- OMP baseline: `scripts/check-omp-baseline.sh` — exit 0.

## Architecture Reference

Wiki architecture, page templates, provenance, or trust model → `llm-wiki`.

Human-facing documentation lives in `docs/` — `installation.md`, `agents.md`, `skills.md`, `cli.md`, `configuration.md`, `architecture.md`, `session-brain.md`, `contributing.md`. `README.md` is a landing page only; when you add a skill, CLI command, or config variable, update the matching `docs/` page rather than the README.

The vault format is structurally conformant with the [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — markdown files with YAML frontmatter, category subfolders, reserved `index.md`/`log.md`. `wiki-export` (OKF mode) and `wiki-import` are the bridge: they translate between our native frontmatter (`title`/`category`/`tags`/`sources`/`created`/`updated` + `summary`) and OKF (`type`/`title`/`description`/`resource`/`tags`/`timestamp`), making vaults exchangeable with any OKF tool. The OKF round-trip is lossless; the `graph.json` round-trip is not.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
at specs/030-self-improving-architecture/plan.md
<!-- SPECKIT END -->
