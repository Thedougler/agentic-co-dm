# This vault's keyed-map convention

A leaflet-bearing note still goes through this vault's frontmatter schema
(`lint-frontmatter-schema`, keyed on `type:`) — there is no schema exemption
for it. The only precedent that ever used a bare, `type`-less frontmatter
block (`raw/2026-07/__Ghostly Ruins Map (Keyed)__.md`) sits under
`raw/`, which the schema linter never scans — that block was never
actually validated, and a `plugin/leaflet` tag it used is not, and never
was, part of `docs/tags.md`'s controlled vocabulary. Don't copy that shape.

## Frontmatter

Use `_templates/reference.md`'s spine — this is an agent-facing reference
page, the same type dashboards like `vault/dashboards/wiki-hub.md` use:

```yaml
---
type: reference
status: canon
publish: false
aliases: []
created: "{date}"
updated: "{date}"
tags: [reference, visibility/internal]
summary: "One sentence describing what the map covers and its markers."
cssclasses:
  - wide-view
---
```

- `publish: false` — matches the "never rely on Leaflet content for player-facing pages" rule in the parent `.claude/skills/obsidian-leaflet/SKILL.md`; Quartz doesn't render the block anyway.
- `cssclasses: [wide-view]` — the vault's convention for giving a map room to breathe, since a `​```leaflet` block's `height`/`width` params size the map itself, not its containing column.
- `tags: [reference, visibility/internal]` — `reference` is the canonical Meta tag for structural/tool pages; `visibility/internal` marks it DM-only, matching `publish: false`.

## Block skeleton

```leaflet
id: <unique-id>
image: [[_assets/maps/<image>.webp]]
bounds:
height: 900px
width: 95%
lat: <half the image height>
long: <half the image width>
minZoom: -3
maxZoom: 2
zoomDelta: 0.5
defaultZoom: -1
unit: miles
scale: 12
```

Fill `id` (unique per map — the plugin persists mutable markers/overlays keyed on it),
`image`, `bounds` (image-pixel corners), and `lat`/`long` (the image center) — all four
per `.claude/skills/obsidian-leaflet/references/map-params.md`.

Write `image:` as the asset's **full vault path**, matching every other embed in this
vault (`![[_assets/maps/campaign-overview-map.webp]]`).

A map that renders as an empty dark container has thrown during its build. The plugin
reports nothing in the note — open the developer console (`Cmd+Opt+I`) and read the
error; a marker-shape mistake (`.claude/skills/obsidian-leaflet/references/markers.md`) and an unresolvable `image:`
link both land there and nowhere else.

The plugin's own parser tolerates `minZoom:5` (no space after the colon) — real installed
content in this vault uses that form and renders correctly — but it is not valid YAML;
write `minZoom: 5` (with the space) in anything you author.

## Marker sizing

`vault/.obsidian/snippets/leaflet-marker.css` overrides the plugin's default pin size vault-wide:

```css
.block-language-leaflet .leaflet-div-icon {
    --marker-size: 35px;
    width: var(--marker-size) !important;
    height: var(--marker-size) !important;
}
```

Scope any further marker-appearance CSS to `.block-language-leaflet` the same way — it's
this vault's established scoped-selector pattern for plugin-rendered elements (the same
pattern a later CSS snippet, `reference-image.css`, explicitly reused).
