---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Craft guidance for what an NPC page's Player-Known and DM-only material should say — the opening Wants line, read-aloud sizing, and what the DM-only prose should cover. Layout is owned by the template, not this file."
created: "2026-08-03"
updated: "2026-08-08"
tags: [intrigue]
uid: b080a60f-4d8e-4286-8751-a34fd1c2250e
---

# Output craft — content for the npc template's open prose

`vault/_templates/_campaigns/_npcs/_npc.md` owns this page's layout —
every heading, its order, and which ones are optional. This guide never
adds or reorders a heading or block; it only says what to write inside
the space the template already leaves open. The template scaffolds
`**Wants:**`, the `[!read-aloud]` callout, and (optional) `## Stats &
Combat`, `## Relationships`, `## Goals & Fronts` — everything below is
guidance for the free-flowing prose the template leaves between the
callout and `## Stats & Combat`, written as plain paragraphs, never as
labeled sub-headings or bold-lead blocks of its own (no visibility-split
headings, `.claude/skills/composing-beats/references/runtime-surface.md` §8). The Player-Known/DM-Only
distinction below is a *drafting* lens (what the table can learn through
play vs. what only the DM sees), not a page structure. The page's own
`status: pending` frontmatter is the provenance marker for the
Player-Known material (page-level only, no inline tag; `transcript-ingest`
flips it to `canon` once the table actually sees this NPC) — nothing here
surfaces in a recap or the site regardless, but staging it now means
`transcript-ingest` only has to confirm or correct, not draft from
scratch.

**`**Wants:**`**, the template's own opening line: one bold-led line
derived from the Toy Chest's `primary_goal` + `active_problem` (write the
Toy Chest first, then compress it). The R12 exemplar device: a DM
improvising unscripted interaction reads this one line, not a history
section. Never independent of the Toy Chest fields it compresses.

**Player-Known material** — what the table can learn through play:

- **A quote**, if you write one: one sentence, in character, as a speaker
  line (`*<Name>*: <the sentence>`). If it could belong to any NPC,
  rewrite it. The DM reads the text after the colon aloud, then speaks as
  them.
- **The template's `[!read-aloud]` callout** — sensory, present tense. One
  callout, one job. Size it by whether the NPC is actually coming to a
  table:
  - **Appearing in a session** (named in an upcoming session's prep, or on
    a run guide's NPC roster) → the full sweep, head to feet in that
    order, closing on the signature detail *in motion*. Eight concrete
    details is not too many. The constraint or oddity that makes them
    memorable lands in the middle of the sweep, not at the front of it.
    Method: `vault/refs/stories/prose-and-character-craft.md`
    § NPC entrance, moves 1–3.
  - **No session in view** → 1–2 sentences: build, coloring, bearing, one
    signature detail. Expand it later, when a session claims them.

  Expanding an existing callout merges into it. Never delete a specific,
  vivid line to make room for a generic one: the sweep is a structure to
  hang detail on, not a licence to replace detail that already works. A
  line another field references (a `performance_hooks` tic naming a prop in
  the callout) is load-bearing, and cutting it breaks both.

**DM-only material** — everything below shares the same open prose area,
written point-first and terse rather than as separately labeled sections:

- A roleplaying crib note for embodying the voice, if useful: a mashup of
  [cultural shorthand you can inhabit instantly] + [role that shouldn't
  work but does].
- An opening move for any NPC appearing in a session: the job they're
  mid-way through when the party first sees them, who speaks first, and
  their first line as a speaker line (`*<Name>*: <text>`). The NPC
  speaking first, with a question, is the default that hands initiative
  back to the table. Skip it for a page with no session in view. Method:
  `vault/refs/stories/prose-and-character-craft.md` § NPC entrance,
  moves 4–5.
- A short dossier of usable facts (2–4 sentences), not a backstory — each
  sentence gives you something usable at the table: point-first, terse,
  bold for NPCs/threats, plain for environment. No single NPC should hold
  every fact the party needs — split what a scene requires across more
  than one page rather than over-stuffing one NPC's page (§ Villain NPC
  additions' Antagonists note applies this same principle to subordinates).
- The Toy Chest table itself — the template's own `**Wants:**` line
  refers to "the Toy Chest table below," so this table is real, required
  content, not this guide's invention. Fields: `vault/refs/vault/npc/references/toy.md`.
- Voice & delivery notes: speech pattern, 2–3 table-ready lines as speaker
  lines (`*<Name>*: <text>`, delivery cues as `*(rising)*` after the colon),
  physical mannerisms, emotional default. If the interview named a worldview, note
  it here too — `vault/refs/vault/npc/references/social-checks.md` ties it to a DC.
- Villain additions, if this is a recurring antagonist — see
  `vault/refs/vault/npc/references/villains.md`.

**`## Stats & Combat`**, **`## Relationships`**, **`## Goals & Fronts`** —
the template's own optional headings; see the template for when each
applies. `## Relationships` is wikilinks only (the Relationships Are Links
rule): the PC-Connection entity, allies, rivals, faction ties, anyone else
this page names. See `vault/refs/vault/npc/references/villains.md` for the
`## Stats & Combat` calibration approach.

**`## Session Log`** — no template scaffolds this heading; it doesn't
exist on the page until the NPC actually appears at a table. This is
`transcript-ingest`'s territory (`vault/refs/runbook-wiki.md` § Who writes
what): `transcript-ingest` appends `- [[sNN-slug]] — one line of what
happened` on first appearance. Don't pre-fill it, and never retroactively
edit an entry once one exists — if a later session contradicts an earlier
one, that's a `CONTRADICTION:` block on the page (`vault/refs/runbook-wiki.md`
rule 6), not a silent rewrite.
