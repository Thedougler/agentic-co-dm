# Overlays, GeoJSON, GPX

Source: `javalent/obsidian-leaflet` README.

## Overlays

Colored circle centered at a coordinate, with a radius in a real-world unit:

```
overlay: [<color>, [<lat>, <long>], <radius> <unit>, <description>]
```

```leaflet
overlay: [blue, [32, -89], 25 mi, 'Description']

overlay:
  - ['#FF0000', [32, -89], 25 km, 'Red zone']
  - ['rgb(0,255,0)', [40, -90], 500 ft, 'Green zone']
```

YAML rule: a hex color starts with `#`, and any value with a comma inside it, must be quoted, or the YAML parse breaks.

```leaflet
overlayTag: nearby
overlayColor: blue
```

Overlays also generate from a note's `mapoverlay` frontmatter (`.claude/skills/obsidian-leaflet/references/markers.md`), and can be right-clicked on the rendered map to edit radius/color or remove.

## Image overlays

Layer a second image over the base map at a bounding box:

```leaflet
imageOverlay:
  - [[[Image|Optional-Alias]], [top-left-lat, top-left-long], [bottom-right-lat, bottom-right-long]]
  - [[[Image2]], [40, -80], [39, -81]]
```

## GeoJSON

```leaflet
geojson: [[File.json]]
geojson:
  - [[File1.json]]
  - [[File2.json]]|alias|[[linked-note]]

geojsonColor: "#3388ff"
geojsonFolder: ./path
```

## GPX routes

```leaflet
gpx: [[Route.gpx]]
gpxMarkers:
  start: start_marker_type
  waypoint: waypoint_marker_type
gpxColor: "#3388ff"
gpxFolder: ./routes
```

`gpxMarkers` values are marker type names — same names as `.claude/skills/obsidian-leaflet/references/markers.md`'s custom types, defined in the plugin Settings tab.
