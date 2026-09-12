---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Which vault/ path a draft guide or prep skill owns, the draft-to-pending status ladder, and the canon and publish gates that belong elsewhere."
created: "2026-08-03"
updated: "2026-08-15"
tags: [craft]
uid: d881f879-843b-4e76-9fe1-9307dd00c519
---

# Draft — Owned Paths and Status Lifecycle

Every guide under `vault/refs/vault/<type>/`, and every prep skill that
writes a typed page (`composing-beats` and its `writing-*-beats` skills,
`encounter-prep`, `rule-prep`), writes its own type's `vault/` path and
nothing else. Every rule below binds whichever of the two owns the page
in hand.

## Initial, then planned

Two depths, one page. `prep_depth: initial | planned`.

| Depth | When | The page holds |
|---|---|---|
| `initial` | The idea lands, or it cannot hit in the next two sessions | Name, premise, Pass/Fail or if-ignored, links to atoms that exist. Thin is honest. Iterate freely. |
| `planned` | The party could conceivably interact with it this session or the next | Current template, current prose budgets, spoken siblings, linked entities the DM would invent cold, a run-guide |

Promote on any one trigger: composing-beats IX7b, player gravity already
names it, or the session story for this night or the next requires it.
No trigger → stay `initial`.

A planned pass aims by `vault/campaigns/shattered-sea/player-gravity.md` and
`vault/campaigns/shattered-sea/threads.md`. Linked
entities created in that pass start as `initial` unless they too sit in
the two-session window.

`status: draft` is compatible with either depth. Flip `status: pending`
only when `prep_depth: planned` and the type's QC profile passes.

## Instantiate, never compose

Copy the page's typed template under `vault/_templates/` -> never retype a
template from memory or compose freeform. Resolution rules (which template
matches this page's `type:`) live in `vault/_templates/CLAUDE.md`. The
template is the sole authority on frontmatter shape and heading order; a
pattern absent from the template is stripped, however common elsewhere.

## The status ladder

| Value | Means | Set by |
|---|---|---|
| `draft` | Incomplete, or stopped before the DM Review Gate | the draft guide |
| `pending` | Table-ready, not yet played | the draft guide |
| `canon` | Actually happened at the table | `transcript-ingest` |

A new page starts at `status: draft` and stays there until it is genuinely
table-ready -> never open a page at `pending` on the assumption it will be
finished this turn. `draft` is a normal resting state, not a failure state:
a page left at `draft` is an honest record that something is still missing.

Stopping mid-build leaves `status: draft` -> never flip to `pending` on an
approval that did not happen.

## Two gates that are never a draft guide's move

- **`status: canon`** belongs to `transcript-ingest`, triggered by the
  entity actually reaching the table -> a guide that sets it is claiming
  something happened.
- **`publish: true`** belongs to the publish proposal exclusively
  (default-deny) -> list the page in the proposal instead of setting the
  key.

## DM Review Gate

A type whose guide names a review gate presents its named decisions to the
DM and waits -> leave `status: draft` if stopping before approval. Which
decisions those are is per-type; the guide names them.
