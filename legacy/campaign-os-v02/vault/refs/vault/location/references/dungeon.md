---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Dungeon subtype fork of the location guide — the four-phase pipeline, topology, chokepoint test, room key format, encounter ratio, and treasure calibration."
created: "2026-08-03"
updated: "2026-08-15"
tags: [exploration]
uid: d8d98d9e-fa26-47ed-a6b3-f02b9636b276
---

# Draft — Location, Dungeon Subtype

Read this when `.claude/skills/draft-content/references/location.md`'s interview establishes
`subtype: dungeon` — a lair, ruin, smuggler hideout, temple, or any
multi-room site the party explores room-by-room. Assumes the shared
interview, stub check, and Toy Chest from that guide already ran; this
file covers only what's dungeon-specific.

Rendering belongs to the `battlemap-render` skill, not this prep
methodology — the deterministic map-plate pipeline (JSON spec, renderer
script, img2img handoff, print upscaling). The Map Key in
`vault/refs/vault/location/references/dungeon-example.md` is the prep
artifact that skill consumes, not a substitute for it.

## Interview additions (dungeon subtype)

Ask these in addition to the hub's shared interview:

- What is this site? (temple, smuggler hideout, sunken ruin, monster lair)
- Who built it, and who occupies it now?
- Approximate room count (default 6–10)?
- Is there a hidden conclusion the party must reach? (triggers the
  Three-Clue Rule, `.claude/skills/composing-beats/references/audits.md` §3)

## The Four-Phase Pipeline

The Dungeon Phase Gate (hub hard rule): write each phase to disk and get
DM review before starting the next.

```text
Phase 1 Architecture -> Phase 2 Entities -> Phase 3 Spatial Logic -> Phase 4 Micro-Detail
      |  (DM review)         |  (DM review)         |  (DM review)
```

### Phase 1 — Architecture

Structure only: room list and connections, no room descriptions, NPC
names, or secrets yet.

**Outputs:**

- Overarching conflict — one sentence: what is building toward a breaking
  point? (This becomes the page's `unstable_condition`.)
- The site's original purpose vs. current use — one sentence each.
- Major factions present (1–3), each with a single proactive goal
  (`.claude/skills/composing-beats/references/audits.md` §1 Independent NPC Agency — a
  vector, not a state waiting for the party).
- Room list: names and connections only.
- If-Ignored — what happens to this site if the party never enters
  (`.claude/skills/composing-beats/references/audits.md` §4; stored in frontmatter
  `consequence`).

Short on a site premise? Roll or pick from
`vault/refs/ideas/core-adventure-generators.md` (Location/Monument/Item
and Condition-Description-Origin tables) and
`vault/refs/vault/quest/references/templates.md` (10 quest archetypes —
Kill the Boss, Find Something, Clear the Dangers, etc.) for a fast
starting premise, then fill in the specifics the interview surfaced.
Neither table replaces the outputs above; both just speed getting to them.

**Three-Clue pass:** if the interview flagged a hidden conclusion, identify
three distinct, mechanically discoverable clues now, one per room, before
detailing any room — two clues in the same room fails the redundancy rule
(`.claude/skills/composing-beats/references/audits.md` §3; the Three Clue Audit output format
lives in `vault/refs/vault/location/references/dungeon-example.md`).
`vault/refs/ideas/creating-secrets-and-clues.md`'s four prompt categories
(Character, Historical, NPC/Villain, Plot secrets) are ideation input for
clue content — cite there, don't restate here.

### Phase 2 — Entities

Populate the site with NPCs and creatures.

- **Named NPCs** route through
  `vault/refs/vault/location/references/npcs.md` — resolve against an
  existing page or spawn a pending stub. Dungeon-specific: every NPC needs
  a proactive objective that advances without the party — what they're
  doing when the party arrives, not what they're waiting for
  (`.claude/skills/composing-beats/references/audits.md` §1).
- **Creatures and stat blocks** route to `encounter-prep` for full
  calibration; this file only requires, before finalizing anything here: a
  looked-up stat block (never invented), a one-line tactical behavior (how
  they open, escalate, retreat), and a morale threshold (a specific HP
  total or named condition, never a vibe). Unsure what fits this site
  type? `vault/refs/vault/location/references/monsters-by-adventure-location.md`
  pairs twelve common adventure locations (ancient ruins, crypts, sewers,
  wizard's tower, volcano lair, and more) with level-appropriate
  monster/NPC groupings. For a wandering-monster table during exploration,
  `vault/refs/table-random-dungeon-monsters.md` gives dungeon-level-banded
  d20 tables — optional, only when random encounters fit this site.

Read `vault/refs/vault/location/references/dungeon-example.md` for Phase 3
(Spatial Logic) and Phase 4 (Micro-Detail), the dungeon-subtype Output
structure, Three Clue Audit format, Treasure Calibration, a worked
example, and the checklist addendum to run before flipping `status:` to
`pending`.
