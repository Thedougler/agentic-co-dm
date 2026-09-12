---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Dungeon subtype Phases 3-4 — map key, chokepoint test, topology, room keying — plus the output structure, Three Clue Audit format, treasure calibration, a one-room placeholder example, and the checklist to run before flipping `status:` to `pending`."
created: "2026-08-03"
updated: "2026-08-15"
tags: [exploration]
uid: 64edce01-b62a-4ee8-ac27-736dc55fa66e
---

# Draft — Location, Dungeon Subtype, Rooms + Output + Worked Example

Read this from `vault/refs/vault/location/references/dungeon.md` § The
Four-Phase Pipeline — Phases 3-4, the dungeon-subtype Output structure,
Three Clue Audit format, and Treasure Calibration — plus a worked example
and the checklist to run before flipping `status:` to `pending`.

## The Four-Phase Pipeline (continued)

### Phase 3 — Spatial Logic

Generate the map key: room connections, terrain features, tactical
structure. This is the prep artifact — not a rendered map. A future
`battlemap-render` skill consumes this key; this phase produces it.

Apply these structural standards:

- Multiple routes between significant rooms (minimum two paths through
  the site).
- At least one secret or non-obvious connection.
- Varied elevation or terrain (flooded, collapsed, elevated, narrow).
- Every space presents a meaningful choice (loud/fast vs. quiet/dangerous,
  fight vs. negotiate).

**Map Key format:**

```text
Room 1 -> Room 2 (west door), Room 4 (hidden passage behind altar)
Room 2 -> Room 1, Room 3 (archway), Room 5 (trapdoor, DC 14 to find)
Room 3 -> Room 2, Room 4 (stone door), Room 5 (crawl passage)
```

**The Chokepoint Test.** Draw the room connections as a graph. Remove the
entrance. If removing any single non-entrance room disconnects the graph
— rooms beyond it become unreachable — that room is a chokepoint.
Chokepoints force linearity; fix by adding an alternate connection.
**Exception:** a chokepoint is acceptable if it *is* the encounter (a
guardian, a locked gate, a collapsed passage) AND the party has at least
two ways to approach it.

**Topology patterns** — after choosing one, use it to sanity-check the
Map Key above, not as a separate diagram to maintain:

| Topology | Shape | Notes |
|---|---|---|
| Linear | `1→2→3→4→5→6` | Worst. Only for a lair with one natural passage; even then add a shortcut. |
| Branching | `1→2→3`, `2→4→5→6` | Players choose paths, but dead ends punish — add loops where possible. |
| Hub | central room connects to most others | Good for lairs, temples, throne rooms. The hub should be the most interesting space — players return to it. |
| Loop | `1→2→3→...→1` | Best. Players circle back, approach encounters from multiple directions. |
| Combined (6+ rooms) | hub + loop mixed | At least two routes between entrance and the most important room; secret connections add a third for resourceful parties. |

Record the chosen topology as a line in the page's `## Features`
(Architecture) section alongside room count — topology and room count
stay plain prose, never a governed frontmatter key of their own (unlike
`subtype:`, `.claude/skills/draft-content/references/location.md` § Template).

### Phase 4 — Micro-Detail

Key each room. Each Room entry splits across the location page's two
template halves, the same split
`vault/refs/vault/location/references/output.md` applies at the whole-page
level, just at room granularity:

- In the Player-Known material, an `### Room N — Name` subheading holding
  only the `[!read-aloud]` callout (3–4 sentences max, player-facing
  prose mode — hand the sentence-level work to `dnd5e-scene-narration`).
- In the DM-only material, the matching `### Room N — Name` subheading
  holding everything else: dimensions, features, mechanics, and a closing
  note on authorial intent.

**Room DM-Only format:**

```markdown
### Room N — Name

**Dimensions:** X × Y ft. Ceiling Z ft. [Terrain notes.]

**Features:**
- **Noun**: State. (Mechanic or DC)
- **NPC Name**: Role, current behavior. (Hidden agenda)
- *Item*: Description. (Effect or trigger)

**Intent:** [What this room teaches, rewards, or tests. One sentence.]
```

Typographic encoding: bold for monsters/NPCs/threats, italic for magic
items/treasure, plain for environment; lead with the noun; "the
characters," never "you," outside the `[!read-aloud]` callout.

Short on room-purpose or feature ideas?
`vault/refs/table-random-chambers.md` lists d20 chamber tables for
fifteen common site types — beasts' den, castle, caverns, necropolis,
wizard's lair, and more — for room-list and Room-name inspiration.
`vault/refs/table-random-monuments.md` gives Origin/Condition/Unusual-
Effect/Structure tables for dressing a **Features** entry (a monument,
statue, or altar) with a concrete detail instead of a generic one. Both
are ideation aids for the Features bullets above, not a substitute for
the Intent line.

**Empty Room Test:** no room is ever empty (No Space Without A Past,
`.claude/skills/draft-content/references/location.md`). If a room has no current
function, give it evidence of its original function, one piece of
environmental texture, and at least one interactable element.

**Encounter placement ratio.** A 6-room dungeon should mix: 1–2 combat
encounters, 1 social encounter (an NPC who can be talked to), 1
puzzle/exploration room, 1–2 atmosphere/transition rooms. Alternate —
three combat rooms in a row is a slog; three exploration rooms in a row
is a museum.

## Output structure (dungeon subtype, within `vault/refs/vault/location/references/output.md`)

All of the following are `###` subheadings in the DM-only material unless
marked otherwise:

- **Access** — how to get in, alternative entrances.
- **General Features** — light, ceilings, walls, sound, smell across the
  whole site.
- **Map Key** — the Phase 3 output.
- **Room 1** through **Room N** — the Phase 4 output, split per § above
  (read-aloud half lands in the Player-Known material).
- **Three Clue Audit** — if a hidden conclusion exists (format below).
- **Treasure Summary** — table: item, value, location (§ Treasure
  Calibration below).
- **Running This Dungeon** — pacing notes: if-loud / if-stealthy /
  if-negotiate variants.

The Phase 1 If-Ignored output lives in frontmatter (`consequence`)
and the body's situation framing — don't duplicate it as a separate section.

## Three Clue Audit

When a hidden conclusion exists, include this block:

```text
Conclusion: [One sentence — what players must understand]
Clue 1: [Room N] — [How discovered — specific mechanic]
Clue 2: [Different room] — [Different mechanic]
Clue 3: [Third room or NPC] — [Third mechanic]
Note: at least two clues reachable without combat.
```

If you can't name three distinct clues at three different rooms, the
dungeon is incomplete — add access points before finalizing
(`.claude/skills/composing-beats/references/audits.md` §3 owns the rule; this is only
the output shape).

## Treasure Calibration

Use the DMG treasure hoard tables as a ceiling, not a floor. Numbers, not
judgment:

| Party Level | Total Dungeon Value (gp) | Notes |
|---|---|---|
| 1–4 | 50–200 gp | Working stash, not a hoard |
| 5–10 | 200–1000 gp | Accumulated wealth, one notable item |
| 11–16 | 1000–5000 gp | Significant cache, 1–2 notable items |

Every magical item needs a specific physical description, the exact
manipulation to activate it, and one narrative draw. "+1 sword" fails
this test. For any homebrew item mechanic in the treasure — a new magic
item, not a reskinned RAW one — route through
`.claude/skills/draft-content/references/item.md` (with its own DM review gate) before
placing it in this table. Don't invent homebrew
mechanics inline; that's a different skill's contract to satisfy.

## Worked example — one room (fixture, placeholder names)

A flooded undercroft beneath a building the party has reason to search.
Placeholder slots stand in for whatever the actual prep grounds this in —
fill each `<…>` from the party's own threads, never from this page.

Player-Known material:

```markdown
### Room 3 — The Counting Vault

> [!read-aloud]
> The stairs bottom out in standing water, ankle-deep and black with silt.
> Three iron strongboxes sit on a raised stone shelf, all three lids
> thrown back and empty. Something has dragged a fourth box off the shelf
> — its track cuts a clean furrow through the silt toward the far wall.
```

DM-only material:

```markdown
### Room 3 — The Counting Vault

**Dimensions:** 20 × 15 ft. Ceiling 8 ft. Standing water, 6 in deep,
across the whole floor.

**Features:**
- **Strongboxes**: Three empty, lids open. (Original contents already
  moved — see Room 5.)
- **Drag furrow**: 12 ft long, ends at a loose stone in the far wall. (DC
  13 Investigation to find the gap behind the stone; leads to Room 4.)
- *Ledger page*: Waterlogged, half-legible, wedged under the fourth
  strongbox's original resting spot. (One of the Three Clue Audit clues —
  names <the thing the party came here to identify>.)

**Intent:** Confirms the party is on the right trail without handing them
the destination — the furrow is the toy, not the ledger page alone.
```

## Checklist addendum (dungeon subtype, in addition to `vault/refs/vault/location/references/checklist.md`'s)

- [ ] Phase gates respected — each phase confirmed by the DM before the
      next started (the Dungeon Phase Gate).
- [ ] Chokepoint Test run and pasted; any chokepoint found is either
      fixed or justified as an intentional guarded encounter with 2+
      approaches.
- [ ] Encounter placement ratio checked against room count.
- [ ] Three Clue Audit present if a hidden conclusion exists; all three
      clues at different rooms/NPCs, at least two reachable without
      combat.
- [ ] Any homebrew treasure item routed through
      `.claude/skills/draft-content/references/item.md`, not invented inline.
- [ ] No deterministic map spec, renderer invocation, or img2img language
      anywhere on the page — that craft belongs to `battlemap-render`,
      not this page.
