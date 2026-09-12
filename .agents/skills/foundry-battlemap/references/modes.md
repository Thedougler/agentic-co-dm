# Modes

Standard mode covers most battlemaps. Two alternative modes modify the Design and Judge steps when the site has a different spatial grammar.

Detect mode in Step 2 (Design) before writing the brief.

## Vehicle / deck-plan mode

**Trigger:** PLACE names a ship, airship, cart, wagon, raft, or other craft.

A vehicle map turns a craft into encounter architecture. The hull is the dungeon — its deck, rooms, thresholds, and edges are the tactical grammar. Sails, rigging, spars, and scenic superstructure expand the vessel's silhouette without pretending every surface is walkable.

### Design additions

Add these fields to the tactical brief alongside the standard fields:

**Hull outline.** The craft's footprint shape and overall dimensions in squares.

**Deck inventory.** Name each playable deck or zone within the hull: what it is, its position, and its size. An airship might have a broad open main deck, a furnished captain's cabin, a chart room, and a helm platform.

**Room and threshold map.** Name doors, hatches, stairs, and narrow passages between decks/zones. Every threshold is a chokepoint and a tactical decision.

**Vertical transitions.** Name hatches, ladders, stairs, and drops that connect different elevations on the craft. State which zones they connect and their grid position.

**Dangerous edges.** Name the boundaries where falling off is lethal or costly. Rail, open hull edge, wing junction, rigging gap. The edges are environmental hazards — forced movement near them changes the fight.

**Playable floor vs scenic envelope.** Distinguish the solid deck the tokens stand on from the non-playable silhouette (sails, rigging, wing spars, translucent membrane, decorative bowsprit). The scenic envelope gives the craft its shape and scale; it is not walkable terrain. Communicate the distinction through value, contour, and material — not labels.

**Default FRAME:** long-axial. Most vessels are longer than wide. Choose the ratio from the hull's actual proportions.

### Judge additions

Check these after the standard eight-category judge:

- Vessel orientation is obvious at thumbnail — bow, stern, and hull shape readable.
- Playable deck is distinguishable from rigging, sails, and scenic spars by value and material.
- Route widths are consistent across the deck — a corridor the same width as a cabin door reads correctly.
- Doors, hatches, stairs, and thresholds between zones are visible without zooming.
- The deck is articulated — rooms, zones, furniture, and cargo create distinct tactical spaces, not one undifferentiated plank surface.
- Micro-detail (ropes, lanterns, fittings) rewards inspection without burying movement lanes.

The map communicates a playable deck plan, not a ship-shaped illustration.

---

## Multi-level / map-set mode

**Trigger:** the user asks for linked levels, floors, layers, or a site with above/below vertical topology (fortress with battlements and tunnels, building with multiple storeys, cave with upper and lower chambers).

A multi-level map set is one site at multiple elevations. Each layer is a separate importable image that shares the same footprint and orientation. The layers together communicate vertical topology — what is above, what is below, and how to move between them.

### Design additions

Add these fields to the tactical brief alongside the standard fields:

**Shared site footprint.** Define the outline that recurs on every layer — the shoreline, the outer wall, the building perimeter, the cave mouth. Draw it once. Every layer inherits it.

**Orientation anchors.** Name the landmarks that lock registration across layers — a tower that appears on battlements and ground floor, a stairwell that appears on every level, a shore edge that stays fixed. At least two anchors. The viewer uses these to mentally align one layer with another.

**Layer inventory.** Name each layer, its tactical role, and its elevation relative to the others.

Example:
> 1. Battlements (top) — exposed wall walks, towers, open sky, defensible positions.
> 2. Ground floor (middle) — furnished rooms, corridors, thresholds, cover.
> 3. Underground tunnels (bottom) — dark irregular passages, chambers, hidden routes, chokepoints.

**Per-layer zone plan.** Write a zone plan for each layer. Each layer has its own tactical grammar — the battlements offer broad exposed space and elevation advantage, the ground floor offers room-to-room cover and threshold fights, the tunnels offer ambush and pursuit in narrow passages. Repeating the same grammar on every level wastes the vertical dimension.

**Vertical connection inventory.** Name every stair, ladder, hatch, shaft, collapse, or passage that connects adjacent layers. State which layers it connects, its grid position, and its direction (up, down, both). Vertical connections must appear on both adjacent layers in the same grid position.

### Generate changes

Generate one image per layer. Each layer uses the same FRAME ratio and the same footprint. The shared outline and orientation anchors must align across images.

Optional: on underground or interior layers, a faint ghost of the surface footprint behind the active layer helps orientation. This is a visual aid, not playable terrain.

### Judge additions

Each layer passes the standard eight-category judge on its own. Then check set registration:

- Shared footprint outline (shore, walls, building perimeter) aligns across all layers within one square of tolerance.
- Orientation anchors (towers, stairwells, walls) appear in the same grid position on every layer where they should be visible.
- Vertical connections (stairs, hatches, ladders) appear on both adjacent layers in matching positions.
- Each layer has distinct tactical grammar — not the same map repainted at different color temperatures.
- Presentation labels, separator rules, and branding from reference images are overlays, not map art. Generated layers carry no baked labels or branding.

Reject layers that drift in footprint alignment, hide vertical connections, or repeat identical tactical grammar across levels.

### Deliver changes

Give one import line per layer, in elevation order (highest first). Name the layer in the slug:

```
artifacts/battlemaps/island-fort-battlements.png — suggested 25×45 — Foundry grid 100 px/sq — no baked grid — upscale after if needed
artifacts/battlemaps/island-fort-ground-floor.png — suggested 25×45 — Foundry grid 100 px/sq — no baked grid — upscale after if needed
artifacts/battlemaps/island-fort-tunnels.png — suggested 25×45 — Foundry grid 100 px/sq — no baked grid — upscale after if needed
```

If an orientation/reference sheet would help the DM align layers in Foundry, offer to generate one as a separate image showing all layers at reduced scale with alignment guides. This is optional — ask before generating.
