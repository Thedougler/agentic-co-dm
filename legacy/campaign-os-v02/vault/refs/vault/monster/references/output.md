---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Section-by-section creature page layout — the opening Wants/Morale block, the Player-Known/DM-Only drafting lens, Stats & Combat wiring."
created: "2026-08-03"
updated: "2026-08-08"
tags: [combat]
uid: e3b4ad04-da55-4b30-8148-075f5154f2d9
---

# Output structure — mapped onto the creature template

Content flows top-to-bottom under the page's one-line description, in
this order, before `## Stats & Combat` — no sub-headings of its own; the
Player-Known/DM-Only distinction below is a *drafting* lens (what the
table can learn through play vs. what only the DM sees), not a page
structure:

**Opening block**, directly under the H1, before Player-Known material —
content and mandatory/omit conditions are The Wants And Morale Lines
(`.claude/skills/draft-content/references/monster.md`):

- **`**Wants:**`** — write the Toy Chest first, then compress it into
  this line; a DM improvising unscripted interaction reads this one
  line, not a history section.
- **`**Morale:**`** — the pre-decided condition, not derived from the Toy
  Chest.

**Player-Known material** — what the table can learn about this *kind*
through play, ordinary observation, or common knowledge/rumor — never DM
secrets:

- **Read-aloud first encounter** as a `[!read-aloud]` callout (1–2
  sentences, sensory, present tense) — hand the actual paragraph to
  `dnd5e-scene-narration`'s two-draft protocol; this guide states only
  what it needs to convey (The Wants And Morale Lines).
- **Common knowledge** — what a local or a Nature/Survival/Arcana check
  might reasonably surface: habitat, behavior patterns, folk warnings.
  Keep it to what's plausibly *known*, not the DM-only material below.

**DM-only material** — everything that runs the creature but hasn't
reached the table yet, written after the Player-Known material and before
`## Stats & Combat`:

- **Ecology** — 2–4 sentences: true nature, what it actually is beneath
  the folk knowledge, where it fits in the region's food chain or magic
  economy. Point-first, terse.
- **Toy Chest** — the table in `vault/refs/vault/monster/references/toy.md`.
- **Prepped reveals** — anything the DM plans to surface once the party
  investigates further (a weakness, a hidden intelligence, a controller
  behind its behavior).

**`## Stats & Combat`** — the bestiary-registered stat block (The
Standalone Stat Block), designed per `vault/refs/vault/monster/references/cr-design.md` and
written per `vault/refs/vault/monster/references/statblock-format.md`'s codeblock syntax. Legendary
or lair-worthy → that same file's § Solo boss / elite suite. Optionally
followed by a **Behavior states** table (State/Trigger/Behavior, one row
per state) for a creature with distinct tactical phases — comment-gated in
the template, delete for a creature that doesn't need it.
