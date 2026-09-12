---
type: runbook
status: draft
publish: false
aliases: [Reading These Pages]
created: "2026-08-01"
updated: "2026-08-01"
tags: [craft]
summary: "What each callout (including [!dialogue]) on a generated prep page means and how those pages are structured — the page every run guide and scene file links from its opening line."
phase: any
uid: 837753f0-faba-47b6-ba62-2b0393f08827
---

# READING-CONVENTIONS runbook (any: how to read a generated page)

Run guides, scene files, and recaps all open by pointing here. This page says what their callouts mean and how they are laid out, so a page never has to explain itself twice — for the wiki's own editing rules, see `vault/refs/runbook-wiki.md` instead.

## The callouts

| You see | It means | At the table |
|---|---|---|
| `> [!read-aloud]` | Prose written to be spoken verbatim | Read it out. Cut or reword freely — it is a floor, not a script |
| `> [!dialogue]` | One NPC's spoken line, or a multi-party exchange | Perform it in that NPC's voice, or each party's in turn |
| `*Name*: text` | Dialogue — the speaker, then what they say | Speak the text; the name is never read aloud |
| Plain prose | A DM-only handling note — a secret, a constraint, a stage direction | Never read aloud |
| `> [!mechanic]` | A rule you apply — a hazard, trap, trigger, or condition | Applies whether or not anyone rolls |
| `> [!check]` | A roll-gated branch with its outcomes already written | Call for the roll, then read the matching branch |
| `> [!spoiler]` | Canon the party has not reached | Never read aloud; it is here so you stay consistent |
| `> [!visual-aid]` | An image placeholder or a rendered asset | Show it, or skip it |
| `> [!warning] CONTRADICTION` | Two pages disagree and nobody has ruled yet | Do not resolve it mid-session — rule at the table and record it after |

The full per-type prose contract lives in the `callouts` skill; this table is the reader's view of it, not a second source of truth.

## How a page is laid out

A scene file runs top to bottom in play order: what the party sees, what they can act on, and where each branch goes. A run guide is not linear — it is the DM's operating surface for the whole session, so its sections are entry points you jump between rather than a sequence you follow.

Every beat gives the players something to do. A beat with nothing to touch, choose, or roll against is a defect on the page, not a quiet moment to narrate past.

A `[[wikilink]]` points at the page that owns that fact. The owning page is authoritative — where a prep page and an entity page disagree, the entity page wins, and the disagreement is worth recording. [[commands]] lists the search and lint commands that maintain these pages.
