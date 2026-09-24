---
name: foundry-battlemap
description: Generate Foundry VTT top-down TTRPG battlemap images in Czepeku painted style. Use when the user wants a battlemap, encounter map, VTT map, top-down scene, Czepeku-style map, tactical map, or a map for Foundry. One clean image per run, shown in chat. No grid, tokens, UI, or labels baked in. Do not use for overhead tokens, character portraits, dungeon room keys, or first-person establishing shots.
metadata:
  type: workflow
  version: "2.1"
---

# Foundry Battlemap
## Accepted-Work gate

Prep only. Follow `docs/agents/work.md`. Precondition: the source page is canon under the rule (`llm-wiki`). If it is not, refuse and name that gate. If `reveal: unrevealed`, do not stage player-visible text until the DM accepts a reveal. Wording matches accepted text.

Make one Czepeku-grade overhead battlemap the table can drop into Foundry. The floor is a tactical architecture, not a backdrop — zones, routes, cover, staging, and identity are designed before the prompt is written.

Generate the most complete image the tool can produce. This skill is not constrained by DPI or resolution. The image may be upscaled in a later pass by another agent. Produce a full, finished TTRPG battlemap, not a sketch.

Hand off creature stamps to **foundry-token**. Hand off room keys and site spines to **dungeon-architect**. This skill is the floor, not the actors and not the key.

Each new place or tactical moment needs its own map. Existing battlemaps may guide vibe, layout density, palette, or terrain language, but a map of a different site is not a deliverable for this site. Reusing it makes locations feel interchangeable and confuses players. A variant is allowed only for the same site and same layout with a changed time, weather, damage state, or other explicitly requested state change.

## Output

One generated image on disk, the same image shown in chat, plus a short import line.

- Portrait rectangle by default. The Design step sets the FRAME ratio from the tactical footprint (default 9:16). Default SCALE is zoomed-out `36×64` so more of the place fits; a tight board only when the user asks for one.
- Orthographic top-down, Czepeku painted style
- Clean art only — terrain, architecture, and environmental props
- No grid, no tokens, no UI, no labels, no watermark, no fog, no light overlays

Default destination `artifacts/battlemaps/`. Use the path the user named when they named one.

Never deliver a path with no picture. The user must see the map in the reply.

**Done when** the image is overhead, matches the declared FRAME ratio, the board is empty of creatures and chrome and grid, the image is visible in chat, and the import line names file path plus a suggested Foundry grid.

## Process

### 1. Intake

Infer from the conversation. Ask only for slots that would force a guess.

Need:

- `PLACE` — what this rectangle is (tavern floor, ruined nave, creek ford, ship deck). Resolve the owner page with qmd-retrieval, and read it (plus linked site pages) before placing any architecture.
- `BEAT` — when the map serves a session beat, load that whole beat note. Type (Hook, Development, Cliffhanger, Climax, Resolution), Scene ends when, and Goal are map jobs. Design the board for those jobs at the beat's scale.
- `BIOME` — climate and dominant materials
- `TIME` — default daylight
- `WEATHER` — default clear
- `TACTICS` — one sentence of how combat movement feels (tempo, not spatial plan)
- `SCALE` — suggested squares for the chosen FRAME. Default zoomed-out `36×64` (portrait 9:16, 5 ft squares) so more of the place fits — more forest, grass, river, and land left and right. Tight board (`18×32` or `25×45`) only when the user asks for one.
- `STYLE` — default Czepeku painted if they did not name one
- `FRAME` — default tall portrait 9:16. Keep 9:16 unless the site's footprint demands another ratio and the user did not already name 9:16.

Do not ask for grid color, DPI, wall-layer JSON, or token placement.

A variant of an earlier map is a new run for the same site. Reuse PLACE, TACTICS, and SCALE only when the prior map depicts that exact site and layout. Change only TIME, WEATHER, or damage state.

**Done when** PLACE and BIOME are filled, the PLACE owner page is read or flagged missing, and a session-serving map has BEAT type and purpose.

### 2. Design

Write a tactical brief before touching the prompt template. The brief designs the encounter architecture of the map — what the player fights around, not just what the player sees.

**Detect mode:**

- PLACE names a ship, airship, cart, or craft → **vehicle/deck-plan mode**. Read [references/modes.md](references/modes.md) for additions.
- User asks for linked levels, floors, or layers → **multi-level/map-set mode**. Read [references/modes.md](references/modes.md) for additions.
- Otherwise → **standard mode** (this step alone).

**Write the brief** with these fields. Definitions, examples, and completion tests live in [references/design.md](references/design.md).

- **Beat jobs** — from Intake BEAT (or the fight/exploration this map is for). Design the board holistically for those jobs at the beat's scale. A Development puts things to explore and learn on the map. A Cliffhanger or action Hook puts the routes, cover, and exits the contest uses. A Climax puts the confrontation ground. A Resolution shows the place as it now is.
- **Zone plan** — name at least two zones, their positions, and their tactical jobs — including the beat's explore/learn or contest jobs.
- **Route grammar** — a primary route (toe-to-toe lane) and at least one alternate route (flanking, bypass). Name chokepoints and threshold crossings.
- **Cover and blocker inventory** — at least three items with grid-scale footprint and tactical effect (half cover, full LoS block, elevation, difficult terrain).
- **Staging reservation** — where open floor is reserved for tokens. State position and approximate size.
- **Elevation reads** — stairs, dais, pit, bank, balcony. Only what reads from overhead.
- **Material ladder** — three or more materials ranked dominant (neutral ground) to accent (focal landmark).
- **Authored identity** — one sentence: culture, function, story from the owner page. Architecture and crossings are what that page names. Unclaimed land stays wild: terraces, canopy, grass, river, and pale-stone fords as the page describes.
- **FRAME** — aspect ratio from the tactical footprint. Default portrait 9:16. Keep 9:16 unless the site's footprint demands another ratio.
- **SCALE** — zoomed-out default `36×64` on 9:16 so more of the place fits. Tight `18×32` or `25×45` only when the user asked for a tight board.

**Done when** the brief names beat jobs, at least two zones, a primary and alternate route, three cover/blockers with footprint, one staging area, a material ladder, an identity sentence grounded in the owner page, a FRAME ratio, and SCALE. Vehicle and multi-level modes add their own fields — see [references/modes.md](references/modes.md).

### 3. Build

Copy the locked prompt in [references/prompt.md](references/prompt.md). Fill every slot from the tactical brief and the Intake slots. Do not soften camera language.

Slot tables, style lock, and composition recipes live in [references/slots.md](references/slots.md).

New slots from the brief: `{FRAME}`, `{ZONES}`, `{ROUTES_AND_COVER}`, `{MATERIALS}`, `{IDENTITY}`, `{BEAT_JOBS}`.

If Nick attached a sketch or asked to keep a liked frame's layout, add this line after PLACE:

`Keep this layout. Same walls, paths, and major props. Change only paint, light, and weather as specified.`

**Done when** every slot in the prompt is a concrete phrase, not a placeholder.

### 4. Generate

Send the filled prompt to the host image tool. Read [.agents/references/image-hosts.md](.agents/references/image-hosts.md) for the tool call on the current host. Generate a new image. Identity/owner refs only.

- Set orientation to match the FRAME (portrait, landscape, or square). One image. Do not tile. Do not stitch.
- Do not bake a grid. Do not ask the image tool for DPI. Do not constrain resolution — generate the most complete image possible.
- Save under `artifacts/battlemaps/` with a slug name (`tavern-common-day.png`).

Multi-level mode: generate one image per layer, same FRAME, same footprint. See [references/modes.md](references/modes.md).

**Done when** an image file exists (one per layer in multi-level mode).

### 5. Judge

Pass only if all eight categories are true. Full checklist lives in [references/judge.md](references/judge.md).

Three-scale check:

1. **Thumbnail** — zones separate by silhouette and value, orientation obvious, no dead rectangles.
2. **Normal VTT zoom** — walkable squares, cover, LoS breaks, routes, doors, stairs readable.
3. **Grid scale** — props have believable multi-square footprints, staging areas hold tokens, material hierarchy works. The perceptual grid matches SCALE: a valley, canopy, or other large place shows more of the place, not room-scale trees filling the canvas.

Plus: camera orthographic, FRAME is the declared ratio (default 9:16, not a nearby substitute), board empty (no grid, no tokens, no chrome), style is Czepeku painted with owner-page identity and grounded depth, architecture matches the owner page, beat jobs are on the board at that SCALE.

A beautiful image that lacks tactical reads fails. A generic map that is technically overhead and clean fails. A map of place-and-terrain alone that ignores the session beat fails.

Vehicle and multi-level modes add judge criteria — see [references/modes.md](references/modes.md).

**Done when** the image is marked pass or reject, with the failing check named.

### 6. Repair

On reject, do not rewrite the prompt. Send one repair line from [references/repair.md](references/repair.md). Generate a new image (image-hosts Generate) with that line added. Cap at two repairs, then show the best frame and name what still fails.

**Done when** the image passes, or two repairs are spent.

### 7. Deliver

Give the user, in this order:

1. The map image in the chat reply — preview the saved file so they see the art, not just a path
2. One import line — path, suggested grid, Foundry px/square note, upscale-after note
3. Next cut — they upscale if they want sharper squares; they draw walls and lights in Foundry

Import shape is in [references/foundry.md](references/foundry.md).

Multi-level mode: one import line per layer, in elevation order. See [references/modes.md](references/modes.md).

Do not write a Foundry tutorial. Do not generate a second variant unless they asked for another run.

**Done when** the image is visible in chat, the import line is present, and the file is in `artifacts/battlemaps/` or the path they named.
