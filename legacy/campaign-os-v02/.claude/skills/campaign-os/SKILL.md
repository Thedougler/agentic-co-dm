---
name: campaign-os
description: The orchestration authority for a Campaign OS repo — an Obsidian vault/LLM-wiki for TTRPG campaign management. Read this FIRST, before any other skill, whenever the user mentions their campaign repo, a session, canon, prep, co-DM setup, or any architecture/component question. Routes to its owning mode; enforces content composed from typed `_templates/` units, never freeform prose.
---

# Campaign OS

The system router: it holds the map and the laws, every contract lives in
the file that enforces it, and this skill sends you there first. A task
routed straight to another skill skips the atomicity check and dispatch
default below — always land here before acting.

## Route the task, by mode

Each row is one **mode**: a distinct mindset, skill set, and reference
corpus that produces its own standard output. Identify the mode, then read
only that row's doc — it owns the procedure from there.

| Mode | You are about to... | Read |
|---|---|---|
| Orientation | Understand the system for the first time, or explain it to the DM | `vault/refs/runbook-campaign-os-overview.md` (the 60-second map) |
| Session loop | Run or debug a pipeline phase end to end | its phase runbook: PREP `vault/refs/runbook-session.md` · CAPTURE `vault/refs/runbook-capture.md` · INGEST `vault/refs/runbook-ingest.md` · RECAP `vault/refs/runbook-recap.md` · PUBLISH `vault/refs/runbook-publish.md` |
| Session loop | Assist live at the table, right now (RUN) | `co-dm` skill |
| Session loop | Prep the next session's overview or run guide | `composing-beats` skill |
| Session loop | Prep a journey, voyage, or route crossing the party will actually play | `travel-events` skill — a leg is a `type: route`, never a passage file |
| Session loop | Author or rework one table-ready situation frame | `composing-beats` skill |
| Session loop | Test a divergence, then write the Live Branches it earns | `composing-beats` skill |
| Session loop | Build or calibrate a fight, social encounter, or skill challenge | `encounter-prep` skill |
| Wiki authoring | Create or edit any wiki page, or check who may write a path | `vault/refs/runbook-wiki.md` |
| Wiki authoring | Draft or expand a typed content page (NPC, location, item, …) | `draft-content` skill — the path → GUIDE router |
| Wiki authoring | Decide which prep scope (campaign/season/quest/session/scene) a request belongs to | `vault/refs/runbook-prep-ladder.md` |
| Wiki authoring | Design or reference a page's format/shape | `_templates/<type>.md` (`vault/_templates/CLAUDE.md`) |
| Wiki authoring | Write, revise, or polish campaign prose | `draft-story` skill |
| Wiki authoring | Pin a campaign term, settle naming drift, or record a DM ruling | `campaign-domain-modeling` skill |
| Wiki authoring | Work the Obsidian frontend — dashboards, plugins, attachments | `obsidian-vault` skill |
| Wiki authoring | Understand *why* this compiles instead of retrieves; route a wiki operation | `llm-wiki` skill |
| Wiki authoring | Answer a canon/lore question, or search when grep misses | `llm-wiki-query` skill |
| Review | Check wiki/pipeline health, coverage, or staleness | `llm-wiki-status` skill |
| Review | Verify a finished document against a quality profile | `content-quality-checker` agent — its description carries the dispatch gate |
| Review | Catch ambiguity in narrative prose just drafted or re-edited | `cold-context-reviewer` agent; any finding → `cold-context-fixer` |
| Dispatch | Tune an encounter's roster against a stated difficulty via simulation | `vault/refs/runbook-encounter-tuning.md` |
| Dispatch | Recreate an external methodology source and challenge this repo with it | `vault/refs/runbook-craft-improvement.md` |
| Dispatch | Turn a product-critic report into filed, labeled GitHub issues | `vault/refs/runbook-issue-triage.md` |
| Publish | Build or troubleshoot the player site, or anything touching visibility | `vault/refs/runbook-publish.md` |
| Process engineering | Write, refactor, or place a campaign skill | `.claude/rules/skills.md` |
| Process engineering | Define or spawn a subagent, or write its shared clauses | `vault/refs/runbook-agents.md` |
| Process engineering | Configure hooks, write a lint rule, or design lint output | `references/hooks-and-linters.md` |
| Process engineering | Pick the lever for a new guardrail | `references/instruction-levers.md` |
| Process engineering | Set up or modify audio → transcript tooling | `utils/tools/audio/README.md` |
| Self-improvement | Fix friction with this repo's own setup | `flag-the-gap` skill; `vault/refs/runbook-self-improve.md` |

## Atomicity: the wiki is built from templated units, not prose

`_templates/<type>.md` is the unit of composition (law L4,
`vault/refs/runbook-campaign-os-overview.md`). The moment you are about to
write or edit content that bundles more than one distinct entity or concept
— a session prep page that also fully develops an NPC, a location writeup
folded into a quest doc — that bundle is a missing split, not a
formatting choice:

- **No template exists yet for the type you're about to write** → chain-load
  `content-type-scaffold` before drafting a single page of it. Never
  freehand a new content type "just this once."
- **An existing page has grown to bundle 2+ types**, or the user asks
  whether a page should be split → dispatch the `content-orchestrator`
  agent on it; it derives the split against today's `vault/_templates/`
  catalog
  and dispatches the extraction.
- Each resulting unit stays self-contained, composable, and minimal — only
  the fields and sections its type actually needs, cross-referenced by
  `[[wikilink]]` rather than restated (`vault/refs/runbook-wiki.md` § New
  pages and edits, rule 6).

## Validate: blind-proof gates every improvement

A **simple fix** — a typo, a dead link, a stale path, a frontmatter key —
ships on the linter alone. Anything more — new or reworded skill guidance,
a changed `_templates/<type>.md`, a `.claude/skills/draft-content/references/<type>.md`
guide, a runbook, a rule — is not trusted until `blind-proof` proves it:
dispatch a fresh Haiku tester blind on the realistic task the material
exists for, then judge its returned plan or output yourself, quoting the
line that shows the change landed. An improvement you haven't blind-proofed
is `EDITED-UNVERIFIED`, not done.

The pass bar doubles as the atomicity ceiling above: `content-drafter`, the
default drafting agent (§ Dispatch default below), runs on Haiku — so no
atomic unit's template or guide may be too complex for a Haiku tester's
*first* blind attempt to produce the correct format, needing nothing past
the kind of minor, linter-fixable correction `references/hooks-and-linters.md`
already covers. A tester that needs more than that isn't a capability gap;
it's the unit still bundling more than one concern — split it further
(`content-type-scaffold`, `content-orchestrator`) or sharpen the guide's
completion criteria, then re-run `blind-proof`. First-attempt reliability
is the bar, never "an agent gets there eventually with iteration."

## Decompose, order, dispatch: one file, one agent

Any request that will create or update 2+ files runs this three-step —
never one agent free-handing several files in sequence. Dispatch the
`content-orchestrator` agent to run all three and keep the decomposition
out of this session's context; run them inline only when it is unavailable:

1. **Decompose** — enumerate every atomic unit the request implies: the
   routed rung's own artifact checklist (its skill or guide names them),
   plus every entity the story names that has no page yet — each one a
   unit per `draft-content`'s path table; a type with no template →
   `content-type-scaffold` first.
2. **Order** — group the units into staged waves by reference direction:
   a unit whose *brief needs facts from* another unit goes in a later
   wave; units that merely wikilink each other share a wave — the stub
   rule (`vault/refs/vault/_common/handoffs.md`) covers the link. Typical
   order: entities (NPC, location, item, faction) → compositions
   (encounters, moments, forks, travel legs) → aggregators (index,
   run guide).
3. **Dispatch** — within a wave, one focused subagent per file, in
   parallel: `content-drafter` is the default drafting agent for a new
   page from an already-decided brief; pick a narrower agent from
   `vault/refs/runbook-agents.md`'s roster when the file's job is
   narrower than "draft this page." Between waves, sequential — the next
   wave dispatches only after the previous one closes. Wave mechanics —
   brief construction, the eight-point worker contract, staging, the
   verify-before-trust close — live in `vault/refs/runbook-dispatch-wave.md`.

Only a batch that cannot be partially ordered at all — every unit needing
every other's output — is single-agent, full-context work instead, not a
wave forced onto dependent files.

## Detect and route

**Invoked with no task named** — the user typed only `/campaign-os` or named
the skill with no ask attached → read `vault/refs/runbook-campaign-os-overview.md`
and explain it **in your own words, in plain conversational sentences**.
Never paste its raw markdown — not the ASCII diagram, not the L1–L6 labels,
not this file's routing table. Cover the same ground (what the repo is, why
it compiles instead of retrieves, the session loop, a quick tour of what
exists), then ask what they want to do. A no-arg call is a request to *see*
the system, not to act on it.

**Once a task is named**, route it through the table above; the repo is
assumed already set up. A request naming a single component ("write the
recap") is OPERATE mode — verify its upstream gate first
— each phase runbook opens with its own `GATE:` line — because a recap
built from an un-ingested transcript is exactly the pipeline rot `vault/refs/runbook-campaign-os-overview.md`'s
L2 exists to prevent.
