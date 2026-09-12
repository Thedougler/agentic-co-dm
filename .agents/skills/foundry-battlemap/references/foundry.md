# Foundry import

The file is raw scene art. Foundry draws the grid, walls, lights, and tokens.

## Resolution

This skill is not constrained by DPI or resolution. Generate the most complete, detailed image the tool can produce. The image may be upscaled in a later pass by another agent — produce a full TTRPG battlemap, not a sketch or placeholder.

## Grid

The generated image carries no grid. Foundry draws the grid on import. Suggest a grid that fits the chosen FRAME ratio.

Foundry default is 100 px per square. Czepeku ships 140 px per square. The user upscales after if they want Czepeku-class sharpness. This skill does not upscale.

| FRAME | Suggested squares (W × H) | At 100 px | At 140 px |
|---|---|---|---|
| portrait 9:16 | 18×32 tight | 1800 × 3200 | 2520 × 4480 |
| portrait 9:16 | 25×45 tight | 2500 × 4500 | 3500 × 6300 |
| portrait 9:16 | 36×64 default | 3600 × 6400 | 5040 × 8960 |
| portrait 9:16 | 45×80 landscape | 4500 × 8000 | 6300 × 11200 |
| long-axial | 17×48 | 1700 × 4800 | 2380 × 6720 |
| long-axial | 12×40 | 1200 × 4000 | 1680 × 5600 |
| square | 30×30 | 3000 × 3000 | 4200 × 4200 |
| wide 16:9 | 45×25 | 4500 × 2500 | 6300 × 3500 |

If the generated file is smaller than the 100 px target, say so on the import line. Upscale is a separate workflow.

## Empty board

Leave tokens, walls, doors, and lights off the image. Those are Foundry layers.

## Chat

Show the saved PNG in the reply before the import line. Path-only delivery is a miss.

## Import line

One line per map (multi-level mode: one line per layer), this shape:

`artifacts/battlemaps/tavern-common-day.png — suggested 36×64 — Foundry grid 100 px/sq (Czepeku-class 140) — no baked grid — upscale after if needed`

Swap the slug, grid, path, and FRAME dimensions for the run.
