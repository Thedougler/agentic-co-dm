# Repair lines

Send one line on a new generation. Keep the rest of the prompt.

- First-person or hero shot — `Reject scene illustration. Orthographic top-down battlemap only. Camera straight down. No horizon.`
- Isometric city tilt — `Flatten to true overhead. Roofs and tabletops as flat tops. No 30-degree isometric.`
- Grid burned in — `Delete every grid line, hex, and measurement mark. Clean painted floor only. No grid whatsoever.`
- Tokens or people — `Remove all characters and tokens. Furniture and terrain only.`
- UI, caption, watermark — `Delete text, compass, frame, and UI. Full-bleed map art.`
- Photoreal satellite — `Repaint in hand-drawn Czepeku style. Ink line, painted fill, VTT cartography.`
- Ratio mismatch — `Reframe to {FRAME}. Play-space fills the canvas. Keep 9:16 when that is the declared FRAME.`
- Too-tight zoom — `Zoom out. Shrink the perceptual grid to {SCALE}. More of the place on the canvas: more forest, grass, river, and land left and right. Trees and ruins stay small. No baked grid.`
- Invented architecture — `Remove roads, bridges, paved courtyards, and buildings the owner page does not name. Keep only the architecture and crossings that page describes.`
- Beat jobs missing — `Redraw for this beat: {BEAT_JOBS}. Put those jobs on the board at {SCALE}.`
- Generic center or missing zones — `Redraw with distinct zones: {ZONES}. Each zone reads by silhouette and value at thumbnail.`
- Dead space or accidental seam — `Fill every region of the canvas with intentional terrain or edge detail. No blank rectangles.`
- Cover/blockers missing or unreadable — `Place and sharpen cover: {cover items from brief}. Keep walkable floor open around them.`
- Repeated props or tile collage feel — `Vary prop shapes, orientations, and placements. Each element belongs to one specific place.`
- Unreadable clutter — `Open the staging areas. Keep detail on the edges and at landmarks. Movement lanes stay clear.`
- Roof covering an interior the user wanted playable — `Cut the roof away. Interior walls as thick bands. Furniture visible from above.`
- Soft muddy materials — `Sharpen stone, wood grain, and water edges. Keep the same layout.`
- Ungrounded props — `Anchor every prop with contact shadows and consistent light. No pasted-on objects.`
