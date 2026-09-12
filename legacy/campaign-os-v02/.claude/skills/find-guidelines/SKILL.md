---
name: find-guidelines
description: Faithfully recreate an external reference/methodology guide as a standardized guide page routed into `vault/refs/`, in a Campaign OS repo (vault/ present). Use for "add this guide to the wiki", "standardize this reference doc", "make a guide page for X", or process/methodology material with no campaign-specific facts. Faithful recreation only — never invention or lossy summary.
---

# Find Guidelines

Instantiates `vault/_templates/_refs/_guide.md` — the standardized home for an external
reference/methodology guide (a city-design method, a mystery-making
framework, a dungeon-creation technique — an official or high-quality
third-party source found outside this repo) once it's worth
keeping in the wiki for agent lookup, instead of sitting as an ad-hoc file
under `raw/` or nowhere at all. Lives at root `.claude/skills/` (not
`.claude/skills/`) because it's cross-cutting — it recreates guides
across many topically-appropriate `vault/` directories, not one owned page
type — see `.claude/rules/skills.md` § Directory scoping.

**This is fidelity work, not authoring.** The name is deliberate: this
skill *finds and faithfully recreates* guidelines that already exist, it
does not write new ones. The specific steps, sequences, numbers, and
methods the source states are preserved precisely — never paraphrased into
a lossy summary, never reordered in a way that changes what a reader would
do differently, never filled in where the source is silent. Only the
*formatting* adapts: headings restructured for scannability, human-oriented
framing/preamble trimmed, the same discipline `llm-wiki-ingest` runs (its
Hard Rule 1 — a thin source produces a thin, cited page, never a
plausible-sounding guess).

## Subtype boundary (read before doing anything)

A `guide` page holds **process/methodology reference with no campaign-
specific facts** — no NPC, location, faction, item, quest, or lore claim.
Before creating one, confirm it's genuinely a guide and not one of these:

- **A campaign fact of any kind** (an NPC's traits, a location's history, a
  faction's agenda) → that claim's own template (`npc`/`location`/
  `faction`/etc.), per `llm-wiki-ingest`'s claim buckets — never folded into
  a guide page.
- **A document `internal-equivalent-check` already covers** (llm-wiki-ingest's
  triage table) — a system/meta doc whose function an existing skill
  already provides. Map to the existing skill instead of creating a
  duplicate guide page.
- **A session run-guide or narrative-island prospective plan** → that's
  `draft-run-guide`'s to build fresh from live wiki state, never
  migrated as a static guide page (llm-wiki-ingest Hard Rule 5's
  narrative-island row).

What's left — a reusable design method, a craft technique, a rules-
adjacent framework with no campaign-specific content — is this skill's
actual territory.

## Workflow

The main loop's job is preparing exact inputs and confirming the result —
never assembling, formatting, rewriting, or archiving anything itself. All
of that is `guideline-recreator`'s job (`vault/refs/runbook-agents.md`), so this stays
cheap regardless of source size: one dispatch, one confirmation.

1. **Confirm the source.** Every guide page traces to exactly one
   `source:` path — the `raw/<YYYY-MM>/<filename>` path the
   source will land at once archived (`inbox/CLAUDE.md`'s convention if it
   arrived via `inbox/`) — and, optionally, one `source_url:`. No source,
   no page — this mirrors `llm-wiki-ingest`'s Hard Rule 2 (provenance is
   page-level frontmatter, never invented).
2. **Stub check first**, same standard queries `llm-wiki-ingest` runs
   (`grep -ril "<title/topic>" vault/refs/`, searching the whole tree since
   the routing below spans several subdirectories) — an existing guide
   covering near-identical territory gets expanded in place (hand its
   current content to the subagent as additional context to merge into,
   same isolation rules), never duplicated.
3. **Prepare every input the subagent needs**, so it never has to explore:
   - **Route the destination, then compute the slug and target path.**
     Pick exactly one:
     - Prose/voice and storytelling craft → `vault/refs/stories/<slug>.md`.
     - Idea-generation and campaign-shaping craft → `vault/refs/ideas/<slug>.md`.
     - Craft specific to one wiki content type → `vault/refs/vault/<type>/references/<slug>.md`
       (`<type>` one of: monster, npc, location, faction, quest, item, ship,
       campaign, lore, season, event, handout, puzzle, loot, species,
       background, table, world).
     - Cross-cutting GM doctrine belonging to no single stage → flat
       `vault/refs/<slug>.md`.
     - Non-craft source material still routes outside this tree entirely —
       e.g. `vault/srd/spells/<school>/<slug>.md` (`vault/_templates/_srd/_spell.md`).
       SRD species text routes to `.claude/skills/draft-content/references/species.md`
       instead, not this skill.
   - Read the matching template yourself — `vault/_templates/_refs/_guide.md`
     for any `vault/refs/` destination above, or the target directory's own
     type-specific template when one exists — and pass its exact contents
     (or path) to the subagent.
   - Pick 1-2 tags from `docs/tags.md`'s existing canonical list
     (add a new canonical tag there yourself first if genuinely nothing
     fits — never hand the subagent a tag that isn't already valid).
   - Name the exact lint command: `npm run lint -- <routed target path>`.
   - Name the exact archive command, if the source arrived via `inbox/`:
     `npm run inbox:archive -- -f <original Inbox path>` (`inbox/CLAUDE.md`)
     — or state "N/A" if the source didn't come from `inbox/` (e.g. pasted
     text, a non-Inbox path). The written page's own `source:` frontmatter
     is what records which page cites the archive, not this command.
4. **Dispatch `guideline-recreator` once, with everything from step 3.**
   This is deliberate context isolation, not a convenience: a great many
   of these sources exist specifically to challenge or improve how this
   repo already does something, and *you* (the main loop) already know
   this repo's templates, skills, and conventions — recreating the source
   yourself risks unconsciously filtering it through that knowledge. The
   subagent writes the finished page directly to its target path,
   self-lints, and archives its own source before returning — you do not
   rebuild, reformat, re-paste its content, or run the archive command
   yourself. `.claude/agents/guideline-recreator.md` missing → don't fall
   back to doing the recreation yourself; tell the DM the agent needs
   building first (chain-load `writing-for-agents`) rather than risk a
   biased recreation.
5. **Confirm, don't redo.** Check the target path exists, then run the
   same lint command yourself once as independent confirmation (contract
   item 3 — zero unresolved hard `WIKI-LINT` findings), and confirm the
   source actually left `inbox/` if archiving applied. A subagent report
   of FAIL, or a lint/archive result that doesn't match what it claimed →
   don't silently fix it yourself (that reintroduces the exact
   inefficiency this design removed); re-dispatch the subagent with the
   specific finding, or degrade by asking if it fails twice (iron rule 7).

## Owned paths

The routed target path from step 3 above (`vault/refs/<slug>.md`,
`vault/refs/stories/<slug>.md`, `vault/refs/ideas/<slug>.md`,
`vault/refs/vault/<type>/references/<slug>.md`, or the source's other
topically-appropriate `vault/` directory) — create or expand, written by
`guideline-recreator`, never hand-assembled by the main loop. Never invents
a fact the source (`source:`/`source_url:`) doesn't state, never compresses
away an actual step or method. `vault/refs/` holds house canon and
recreated guides side by side, distinguished by frontmatter, not folder:
house canon is `type: craft`/`status: canon`; a recreation is `type: guide`/
`status: draft` with a `source:` (same principle as `status: srd`
for SRD content).

## Degrade by asking

- The source is ambiguous between guide material and a genuine campaign
  fact → ask, don't guess (a wrong triage sends real canon into a page
  that's exempt from the usual claim-bucket templates).
- No `raw/` source exists for the content (the DM is describing a guide
  from memory, not handing over a document) → ask for the source first;
  this skill never originates guide content without one.
