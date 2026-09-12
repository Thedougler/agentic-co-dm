---
name: obsidian-leaflet
description: >
  The Leaflet plugin syntax (javalent/obsidian-leaflet) for a Campaign OS repo
  (vault/campaigns/shattered-sea/locations/ present). Use when authoring or editing a `leaflet` code block — an
  interactive pannable/zoomable image or tile map — adding a marker/pin, shading a region,
  importing GeoJSON/GPX, or layering an overlay. Not for player-facing pages — Leaflet does
  not render in Quartz.
---

# Obsidian Leaflet

The installed plugin is **Leaflet** (`javalent/obsidian-leaflet`, this vault runs v6.0.5). It renders a `​```leaflet` code block as a pannable/zoomable Leaflet.js map — an image map (fantasy/dungeon maps) or a real-world tile map — with pins, overlays, GeoJSON, and GPX routes.

## Quick syntax

One family, one block — this vault's real Ghostly Ruins map, extended with a second marker showing the full 7-field form:

```leaflet
id: ghostly ruins
image: [[Ghostly Ruins.webp]]
bounds:
  - [0, 0]
  - [205, 154]
height: 900px
width: 95%
defaultZoom: 7
unit: feet
scale: 30
marker: default, 40, 90, [[Widow's Hollow]], Abandoned watchtower, 3, 10
```

`marker:` is 7 positional fields — `type,lat,long,link,description,minZoom,maxZoom` — see `references/markers.md`.

## What you need → which file

| Need | Reference file |
|---|---|
| Core map params — id/image/bounds/zoom/height-width/unit-scale, real-world tile servers, display options | `references/map-params.md` |
| Add/edit a pin — inline marker syntax, markers from note frontmatter/folder/tag, custom marker types | `references/markers.md` |
| Shade a region, import GeoJSON/GPX, layer a second image | `references/overlays-geojson-gpx.md` |
| This vault's keyed-map convention — frontmatter, block skeleton, marker CSS | `references/patterns.md` |

## What NOT to do

- Never omit the description field when adding a marker — it's positional field 5 of 7: `marker: <type>,<lat>,<long>,<link>,<description>,<minZoom>,<maxZoom>`; the 4-field shorthand `[type, lat, long, link]` silently drops the pop-up/tooltip text (`references/markers.md`).
- Never write multiple markers as flow sequences (`- [default, 40, 90, [[Note]]]`) or as repeated `marker:` lines — both abort the map build and render an empty dark container -> instead: one `marker:` key over a list of plain CSV strings, no comma inside any description (`references/markers.md`).
- Never invent a `markers.json` config file for custom marker icons/colors — no such file format exists. Custom marker types are defined only in the plugin's own Settings tab (Community plugins → Leaflet → marker types), then referenced by name in `marker:`/`mapmarker:` (`references/markers.md`).
- Never rely on Leaflet content for player-facing pages — Quartz's static build has no handler for the `leaflet` block language, so it renders nothing on the published site (same non-portability class as `obsidian-metabind`) → publish-facing content stays plain markdown or a linked image.
- Never assume image-map marker coordinates are literal pixels unless `bounds:` is set — `bounds: [[0,0],[205,154]]` maps a marker's `[lat, long]` onto that box; a map with no explicit `bounds:` uses Leaflet's default CRS.Simple percentage space instead (this vault's own marker data stores fractional coords like `[-2.09, 1.28]` for exactly that case).
- Never hand-write a `mapmarkers`/`mapoverlay` frontmatter block that duplicates a marker already drawn in-app — app-drawn (mutable) markers persist to the plugin's own `data.json`, not the note; only code-block or frontmatter markers round-trip through git.

## Reference files

| File | Covers |
|---|---|
| `references/map-params.md` | `id`/`image`/`bounds`/zoom family/`height`/`width`/`unit`/`scale`, real-world tile-server params, display/control options |
| `references/markers.md` | Full 7-field inline `marker:` syntax, YAML list form, `markerFile`/`markerFolder`/`markerTag`/`filterTag`/`linksTo`/`linksFrom`, frontmatter-driven markers, custom marker types (Settings-tab only) |
| `references/overlays-geojson-gpx.md` | `overlay:`/`overlayTag`, image overlays, GeoJSON, GPX routes |
| `references/patterns.md` | This vault's keyed-map convention — real frontmatter shape, block skeleton, `leaflet-marker.css` sizing override |
