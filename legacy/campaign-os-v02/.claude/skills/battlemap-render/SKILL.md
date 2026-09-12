---
name: battlemap-render
description: >
  Render a top-down, grid-accurate battlemap in a Campaign OS repo (vault/ present) — a
  dungeon room, lair, cave, building interior, or ship deck. Triggers: "make a battlemap", "map
  this room", "map the dungeon", "render a map for the fight". Not for scene illustrations,
  portraits, or banners — that's `visual-aids`.
---

# battlemap-render

## Overview

battlemap-render turns a **paint-by-numbers guide you author** into a print-ready, grid-perfect,
hand-painted battlemap. A bundled deterministic script (`map.mjs`) owns all the geometry, so the
1-inch grid is **exact by construction**; a SOTA image model (nano-banana) does only the styling and
never invents layout — the guide pins it. Quality bar: **2-Minute Tabletop-class** painterly top-down
art that reads as **a little window looking down into this exact place in the DM's world** —
grounded in canon *geometry* **and** canon *atmosphere*, never a generic tile. `prompting-nano-banana-2`
chain-loads by default (Skill tool, not optional) for the beautify prompt (pipeline step 4).

**The load-bearing idea — you author the legend.** There is no fixed token library boxing you in.
For each map you write a tiny **scene** — a character grid plus a legend *you choose*: which colors
flood-fill as surfaces and which are outlined, labeled regions, in whatever colors/labels fit the
scene. `render` draws the guide; your prompt tells the model what each color/label becomes; it
repaints; the script composites its crisp vector grid on top last. Model sees **only the guide image and your prompt** — no other noise.

```text
author scene.json ─► preview ─► render ─► beautify ──────────► composite ─► finished map
                     (free)     (free)    (beautify.mjs · $)    (free)
```

## When to use

Any space players fight or move through room-by-room: dungeon rooms, lairs, caves, ship decks,
building interiors, ambush sites. Usually invoked by **`.claude/skills/draft-content/references/location.md`** (dungeons are a location
genre; it designs the layout, battlemap-render draws it) or **encounter-prep**. NOT for scene
illustration/portraits/banners → use `visual-aids`.

**Setup (first run only):** `cd .claude/skills/battlemap-render/scripts && npm install` (installs
sharp, isolated + gitignored).

## Standard queries

Ground the room in canon **before** authoring a scene — both halves below are load-bearing:

```bash
grep -ril "<room/dungeon/location name>" vault/ 2>/dev/null
grep -rl --include=transcript.md -i "<room/dungeon/location name>" vault/campaigns/ 2>/dev/null
```

(Two commands, not one glued together — per
`.claude/skills/world-update/references/shell-safety-notes.md`.)

Pull two things from the hits, both load-bearing:

- **Geometry & layout** — dimensions, ceiling, every exit and where it leads, terrain, keyed
  features. The map must match **exactly** what the DM will describe, tile for tile.
- **Atmosphere & vibe** — materials, light/colour, wear, signs of recent use, mood and narrative
  function. Mine this from the room's `[!read-aloud]` block and the parent location's feel. Not
  optional dressing — a map that nails the grid but paints a generic tile has failed half the job.

Geometry drives the grid; atmosphere drives the legend `as:` notes and the beautify THEME (pipeline
step 4). Empty grep output means a wholly new, uncanonized room — invent freely, consistent with the
parent location's established feel.

## The scene file

A scene is a small JSON: a `grid` of row-strings (one char per cell, a **space = void**, which lets
rooms be non-rectangular) plus a `legend` mapping each char to how it draws.

```json
{
  "grid": [
    "########",
    "#..RB..#",
    "#.~~~.C#",
    "L..~~..#",
    "########"
  ],
  "legend": {
    "#": { "fill": "dimgray",     "as": "rough wet stone wall" },
    ".": { "fill": "#cfc9ba",     "as": "damp flagstone floor" },
    "~": { "outline": "deepskyblue", "label": "WATER",     "as": "ankle-deep standing water" },
    "L": { "outline": "limegreen",   "label": "ARCHWAY",   "as": "an open tunnel-mouth exit" },
    "R": { "outline": "sienna",      "label": "RUBBLE",    "as": "a heap of fallen masonry (half cover)" },
    "B": { "outline": "orange",      "label": "BARRELS",   "as": "a stack of powder barrels" },
    "C": { "outline": "gold",        "label": "CHEST",     "as": "a banded strongbox" }
  }
}
```

- **`fill`** = a flood-filled surface. Use it for **only** the base surfaces — walls and default floor.
- **`outline` + `label`** = an outlined, labeled **region**. Contiguous cells of the same key merge
  into **one** labeled region (three `T` cells in a row = one 15-ft `TRAP` region).
- **`as`** is your own note of what to paint there, for prompt-writing; the renderer ignores it.

Fill **only** wall + floor; make everything else an `outline` region (solid blobs leak/drift). Use
simple, distinct colors. Frame the room with wall on every side and put exits in that border ring.

**Author it in one pass** — this schema is complete; don't read `map.mjs`, `scene.mjs`, the token
library, or a prior scene to learn the format. **Size to canon — 1 cell = 5 ft** (a 35 × 30 ft room
is 7 × 6 interior cells). Exits are one border cell + a short label (`TO ROOM 3`, `ARCHWAY`) — the
renderer auto-clamps every edge label on-canvas, so never widen a cell or re-render to stop a label
clipping. **`preview` once, `render` once** — re-render only for wrong *geometry*, never to chase
label placement.

## Commands

Run from the repo root. `--ppi` = pixels per tile = pixels per inch (300 = print master).

| Command | Cost | Produces |
|---|---|---|
| `map.mjs preview <scene.json>` | free | ASCII map + dims / legend size |
| `map.mjs render <scene.json> [--ppi N] [--out dir]` | free | `base.png` (the **guide**), `grid.png`, `flat.png` |
| `beautify.mjs <base.png> <prompt.txt> --out <art.png> [--model id] [--res 1K\|2K\|4K] [--in px]` | **$** | the styled `art.png` (aspect locked) |
| `map.mjs composite <art.png> <scene.json> [--ppi N] [--out dir]` | free | `<stem>.player.png` (finished, gridded) |

`render`/`composite` also accept a `.csv` (legacy token path) or `dungeon.json` (see
[token-library.md](references/token-library.md) § Dungeons, which also covers the `compose`
multi-room workflow for stitching several rooms into one dungeon map). `beautify.mjs` downsamples
the guide, locks output aspect to it, and defaults to `google/nano-banana-pro` (on `nano-banana-2`
it also forces web search **off** so it can't invent geometry). It is the only paid step, and it
calls out to Replicate for the actual generation — see `use-replicate` for the client/auth backend.

## Pipeline — one room

1. **Ground it in canon FIRST — run the Standard queries above.** Empty output means a wholly new
   room — invent freely, staying consistent with the parent location.
2. **Author `scene.json`** — grid + legend, built from that canon. Frame with wall; exits in the border.
3. **`preview` then `render --ppi 300` (free).** `render` writes the `base.png` guide. Look at it —
   confirm every region is outlined and labeled where you meant, matching the wiki's layout.
4. **Write the prompt — chain-load `prompting-nano-banana-2` first (Skill tool, by default),** then
   write it with [beautify-prompt.md](references/beautify-prompt.md): name what each color/label
   becomes, **preserve-lock** the walls + aspect, keep the **edge exit labels**, replace every
   interior label with its entity, one of each. **Hidden things (secret doors, traps, caches) are NOT
   on the map at all** — fog of war covers them, the DM tracks them from canon. The THEME line is
   where the Standard-queries atmosphere brief lands. Save as `prompt.txt`.
5. **Beautify ($) → composite (free).**

   ```bash
   node .claude/skills/battlemap-render/scripts/beautify.mjs room.base.png prompt.txt --out room.art.png --res 2K
   node .claude/skills/battlemap-render/scripts/map.mjs composite room.art.png room.json --ppi 300 --out <dir>
   ```

   → `room.player.png` (styled art + crisp grid).
6. **Validate:** geometry/exits/terrain match **both the guide and the canon**; aspect unchanged;
   only edge exit labels survive; nothing invented (wrong terrain extent is an *authoring* bug —
   fix the grid, don't re-prompt). Then write it to its owned path (below).

**Choosing the model:** default `google/nano-banana-pro` is right for a deliverable, not a draft — it
reliably obeys the "paint over every colored box" erase-instruction (nano-banana-2 only sometimes
does). For **cheap layout/prompt iteration**, pass `--model google/nano-banana-2` (~⅓ the cost); do
the final on pro. Don't ship an nb2 map.

## Outputs

Per-file breakdown of what `render`/`beautify.mjs`/`composite` each produce: `references/output-files.md`.

## Owned paths

Writes map images and their source `scene.json`/`prompt.txt` into the top-level `vault/_assets/battlemaps/`
tree, never co-located with the page they illustrate.

- **Non-session-scoped** (a location's own dungeon/room, prepped ahead of any specific session)
  → `vault/_assets/battlemaps/<page-slug>-<room-slug>.<ext>`, flat. A "sunken crypt" location page's
  guard-room map gets `vault/_assets/battlemaps/sunken-crypt-guard-room.base.png` / `.player.png` /
  `-guard-room.scene.json`.
- **Session-scoped** (a map authored for a specific session's encounter) →
  `vault/_assets/battlemaps/session-NN/<description>.<ext>`, nested one level further by session number.

Never sets `status:`/`publish:` on any page — this skill only produces image files; the calling
prep skill embeds the finished `<stem>.player.png` with a standard Obsidian wikilink embed once
this skill hands the path back.

## Degrade by asking

| Situation | Do |
|---|---|
| `CONFIG.md` sets `feature_battlemap_render: false` | Stop — this subsystem is turned off on this installation; point the DM at `CONFIG.md`. Don't render a map. |
| Standard-queries hits contradict (two rooms same name, or canon vs. transcript dimensions differ) | Ask the DM which is authoritative; don't average or silently pick one. |
| No canon dimensions found, room isn't clearly a new invention | Ask for approximate size/shape before authoring — don't guess a generic box. |
| Beautify keeps leaking boxes or duplicating features after two prompt-rewrites | Stop; ask the DM whether to accept the flat (unbeautified) `flat.png` instead of burning further paid generations. |
