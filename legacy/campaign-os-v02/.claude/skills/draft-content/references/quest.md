
# Draft — Quest

A multi-session objective, mystery, or throughline the party can pursue.
Done means the DM can open a session and run the next scene from the
`## Secrets & Clues` seed alone.

## Template

`vault/_templates/_srd/_quest.md` — copy it, never retype it. Headings fixed and in
order: `## Secrets & Clues · ## Beats · ## Outcome`.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — party agency, world
   independence.
3. `vault/refs/vault/_common/hard-rules.md` — the shared rules; they
   bind this type and are never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now and
   paste the output.

`DQ1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The Subtype Boundary.** No party objective, just one side's plan ->
  stop, route to `.claude/skills/draft-content/references/faction.md`: a quest is never a front wearing a
  different heading.
- **The Structural Pattern Choice.** Before writing anything else -> pick
  a pattern matching the quest's actual shape
  (`vault/refs/vault/quest/references/structure.md`); default to the plain
  single-thread shape rather than forcing a named pattern.
- **The Quest Status Ladder.** `quest_status` (`rumored | active |
  complete | failed | abandoned`) is separate from the shared `status:`
  lifecycle (The Status Gate). It starts at `rumored`, advancing only on
  session evidence -> this guide sets the starting value only;
  `transcript-ingest` alone advances it further.
- **The Beats Handoff.** Beat-by-beat prose in `## Beats` -> stop; that's
  `draft-story`'s DS4 step. This guide's job ends at the seed:
  hook, pattern, `link_of_relevance`.

## Interview — this type only

Ask these in the same message as
`vault/refs/vault/_common/interview.md`'s shared questions:

- What's the objective, mystery, or throughline, in one sentence? None
  yet -> offer `vault/refs/vault/quest/references/content.md` § Objective
  Archetypes.
- Does the party have a real objective here, or is this one side's plan
  with no party stake yet (The Subtype Boundary)?
- What structural pattern fits (The Structural Pattern Choice)? Unsure ->
  offer `vault/refs/vault/quest/references/structure.md`'s options.
- Is there an opposing faction or NPC already established? Wikilink it,
  don't re-describe it here. What does failure or abandonment look like,
  concretely?

## Secrets & Clues

Hook, stated objective, structural pattern, true stakes/opposition,
`link_of_relevance`, and prepped reveals — written once under
`## Secrets & Clues`, no visibility split.
Fields and Strongest Objection: `vault/refs/vault/quest/references/output.md`.
Fuel: `vault/refs/vault/quest/references/content.md`.

## Before you ship

Lifecycle `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md` and
`vault/refs/vault/quest/references/checklist.md`.

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/quest/references/structure.md` | Picking a structural pattern, or diagnosing a stalled `active` quest |
| `vault/refs/vault/quest/references/content.md` | Sparking an objective, secrets/clues fuel, or Outcome rewards |
| `vault/refs/vault/quest/references/output.md` | Filling `## Secrets & Clues`/`## Beats`/`## Outcome`, Strongest Objection |
| `vault/refs/vault/quest/references/checklist.md` | Quest-only checklist additions |
| `vault/refs/vault/quest/references/templates.md` | Ten general-purpose adventure archetype templates from Sly Flourish's LGMRD, each customizable and randomly selectable via d10 roll |
| `vault/refs/vault/quest/references/example.md` | A full worked fixture, interview through filled template |
| `vault/refs/ideas/villains-and-themes.md` | Weaving a moral dilemma or thematic throughline into the quest's shape |
