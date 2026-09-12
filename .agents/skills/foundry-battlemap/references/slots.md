# Slots

## PLACE

Name the space and the walkable plan, not the adventure plot. Resolve the owner page with qmd-retrieval and read it before filling architecture.

Good: `two-storey coaching inn common room with bar north, hearth east, stairs west, open floor center`
Bad: `the party fights goblins here`

Roof rule:

- Exterior yards, streets, roofs, wilderness — roofs on
- Interiors and dungeon rooms — roofs cut away, walls as thick painted bands with a slim outer face so doors and windows read

## BIOME

Climate plus the two or three materials that dominate.

Examples:

- `temperate farmland, packed dirt, oak, red clay tile`
- `cold limestone dungeon, wet flagstone, rusted iron, pale moss`
- `tropical river gorge, basalt, hanging roots, silt water`

## TIME

Default: `bright overcast daylight, even overhead illumination, soft painted form shadow only`

Presets:

- dawn — `low warm sidelight from the east edge, long painted shadows, gold haze`
- dusk — `warm low light from the west edge, cooler fill`
- night — `moonlit blues and practical lantern pools painted into the surfaces`
- planar — name the plane and the light (`fey gold-green, no sun`)

## WEATHER

Default: `clear`

Presets: `light rain sheen on stone`, `fresh snow cover with paths kicked through`, `mist in the low ground only`, `dry heat shimmer off sand`, `ashfall on horizontal surfaces`

## TACTICS

One sentence describing how combat movement feels in this space. The spatial plan (zones, routes, cover positions) lives in ZONES and ROUTES_AND_COVER — TACTICS captures the encounter tempo.

Default if they gave none: `medium skirmish with toe-to-toe and flanking options, cover along the long edges`

Examples:

- `running retreat down a long hall, pursuers closing from behind`
- `defensive stand at a chokepoint with pressure from multiple angles`
- `ambush in dense cover, short sight lines, close-range engagement`
- `open arena, nowhere to hide, forced commitment`

## SCALE

Suggested grid dimensions for the chosen FRAME ratio. Foundry draws the grid — this sets the spatial feel. Default is zoomed-out so more of the place fits. Tight boards only when the user asks for one.

| FRAME | Label | Squares (W × H) | Use |
|---|---|---|---|
| portrait 9:16 | default | 36×64 | zoomed-out place — more forest, grass, river, land left and right |
| portrait 9:16 | landscape | 45×80 | still larger valley or canopy |
| portrait 9:16 | tight | 18×32 | single room, boss dais — only when asked |
| portrait 9:16 | encounter | 25×45 | room-scale fight — only when asked for a tight board |
| long-axial | hall | 17×48 | ceremonial hall, canyon |
| long-axial | ship | 12×40 | vessel deck |
| square | arena | 30×30 | arena, tower floor, clearing |
| wide 16:9 | bridge | 45×25 | wide deck, bridge, shoreline |

If they named a grid, use theirs. Match the chosen FRAME ratio. Features stay small enough that this many squares of the place fit on the canvas.

## STYLE

Default:

`hand-drawn painted Czepeku battlemap, visible ink line, soft watercolor-oil fill, warm technicolor fantasy, high narrative prop density, clear walkable floors, professional VTT cartography`

Presets:

- grim — `same overhead language, dirtier palette, soot, chipped stone, less decorative flourish`
- fey — `same overhead language, luminous plant life, pollen, impossible color`
- ruin — `same overhead language, collapsed roofs as rubble piles, roots through flagstone`
- sci-fi — `same overhead language, panel lines, hazard stripes, clean alloys, Czepeku sci-fi cartography`

Do not switch to photoreal, satellite, Dyson ink-only, or Forgotten Adventures token style unless they named that.

## FRAME

Aspect ratio chosen in the Design step from the tactical footprint. See [design.md — FRAME](design.md#frame) for the selection table.

Default: `tall portrait 9:16 rectangle`

Keep 9:16 unless the site's footprint demands another ratio and the user did not already name 9:16. Do not substitute a nearby ratio.

Presets:

- portrait — `tall portrait 9:16 rectangle`
- long-axial — `tall portrait rectangle, approximately 9:24 or fitted to the zone plan`
- square — `square 1:1 rectangle`
- wide — `wide landscape 16:9 rectangle`

## ZONES

One sentence naming the major zones and their spatial relationship, drawn from the Design step's zone plan. Aim for the macro read — what separates at thumbnail.

Examples:

- `Three zones along the long axis: open approach lane south, circular arena center, raised sanctum north`
- `Radial layout: central bonfire clearing, perimeter stall ring, rocky cliff border, river margin south`
- `Two zones divided by a creek ford: dense jungle west, open pebble beach east`

## ROUTES_AND_COVER

One sentence naming the primary route, one alternate route, and the major cover/blockers, drawn from the Design step's route grammar and cover inventory.

Examples:

- `Red carpet central axis as primary route, lateral edge lanes for flanking; equestrian statues as LoS blockers, side recesses for cover`
- `Creek ford as primary crossing, stepping-stone riffle upstream as alternate; boulders and root clusters for cover on both banks`
- `Central deck spine as primary route, side cabins for flanking; cargo crates and mast base as cover`

## MATERIALS

A ranked material ladder from the Design step. State three or more materials from dominant (most area, neutral) to accent (least area, saturated).

Examples:

- `cream marble floor, red carpet runner, green-gold geometric tile, gold gilding`
- `olive-green grass, warm brown wood and earth, teal-blue water, orange firelight accents`
- `warm timber planking, burgundy carpet and upholstery, cool blue cabin walls, violet arcane glow`

## IDENTITY

One sentence naming the culture, function, or story the map's architecture and props serve, drawn from the Design step's authored identity and the PLACE owner page. Architecture and crossings are what that page names.

Examples:

- `Ottoman-baroque royal audience hall built for ceremony and processional theatre`
- `Traveling carnival campsite mid-festival, invaded by a creature from the surrounding wilds`
- `Abandoned stacked fruiting terraces swallowed by canopy, wild pale-stone ford through grassland river`

## BEAT_JOBS

One sentence of what this board must do for the session beat (or the fight/exploration this map is for), drawn from the Design step's beat jobs.

Examples:

- `Development: stacked fruiting terraces, eight-foot grass, pale-stone ford, and canopy pockets to drop into and read from above`
- `Cliffhanger hunt: open sky over terrace lip, grass river east, beach line south, canopy cover as the exit`
- `Skirmish on this tavern floor with bar cover and two exits`
