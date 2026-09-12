# Map parameters

Core, zoom, tile-server, and display parameters for the `​```leaflet` code block. Source: `javalent/obsidian-leaflet` README.

## Core

| Parameter | Purpose | Example |
|---|---|---|
| `id` | Unique identifier (required) — the plugin persists mutable (app-drawn) markers/overlays per `id` in its own `data.json` | `id: ghostly ruins` |
| `image` | Image layer, as a wikilink — for a fantasy/dungeon image map | `image: [[Ghostly Ruins.webp]]` |
| `lat` / `long` | Initial view center, image maps included | `lat: 384` / `long: 688` |
| `height` | Map height | `height: 900px` or `height: 100%` |
| `width` | Map width | `width: 95%` |

Multiple images (layered/alternate views), YAML list form (v3.11.0+):

```leaflet
image:
  - [[Image1.jpg|Alias1]]
  - [[Image2.jpg|Alias2]]
```

## Bounds (image maps)

```leaflet
bounds:
  - [<top-left-lat>, <top-left-long>]
  - [<bottom-right-lat>, <bottom-right-long>]
```

Maps marker/overlay `[lat, long]` coordinates onto that box — typically the image's pixel dimensions. **No `bounds:` set** → the plugin falls back to Leaflet's default CRS.Simple percentage space (fractional coordinates like `[-2.09, 1.28]`), not pixels.

`lat` counts **up from the image's bottom edge**, `long` right from its left
edge. Pixel coordinates read off an image editor count down from the top, so
convert: `lat = <image height> - <pixels from top>`. Skipping the conversion
mirrors every marker vertically — a valid-looking map with every pin in the
wrong district.

With `bounds:` set, an omitted `lat`/`long` does not center the image: the
plugin falls back to `[50, 50]`, a corner of a pixel-scale map. Set them to
the image's center — half its height, half its width.

## Zoom

```leaflet
minZoom: 1
maxZoom: 10
defaultZoom: 5
zoomDelta: 1
```

When `bounds:` is set to raw image-pixel units (hundreds/thousands wide),
zoom is still CRS.Simple powers-of-2 — `defaultZoom: 1` renders at ~2x
native pixel scale, so only a crop of the image fits the container, not
the whole map. For pixel-scale bounds, use a small **negative** zoom range
instead (the plugin's own documented example for a 1600px-wide image:
`minZoom: -2`, `maxZoom: 1`, `defaultZoom: -1` — see
`javalent/obsidian-leaflet-plugin` discussion #130).

## Distance & scale

```leaflet
unit: feet
scale: 30
```

`unit` is the real-world unit a scale bar / overlay radius is measured in (`feet`, `meters`, `miles`, `km`); `scale` is how many of that unit one map unit represents.

## Real-world tile servers

For a real-world map (`lat`/`long`, no `image:`):

```leaflet
tileServer: https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png|Dark
tileOverlay: https://tiles.wmflabs.org/hillshading/{z}/{x}/{y}.png|Hills|on
tileSubdomains: 1,2,3
osmLayer: false
```

This vault's plugin defaults (`vault/.obsidian/plugins/obsidian-leaflet-plugin/data.json`): CartoDB Voyager tiles, `defaultUnitType: imperial`.

## Display options

```leaflet
darkMode: true
draw: true
drawColor: "#3388ff"
showAllMarkers: false
preserveAspect: false
noUI: false
lock: false
recenter: false
noScrollZoom: false
```

YAML treats `#` as a comment — quote hex colors: `drawColor: "#3388ff"`.
