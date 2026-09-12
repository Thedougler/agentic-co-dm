# Markers

Source: `javalent/obsidian-leaflet` README, plus this vault's installed plugin `data.json`.

## Inline syntax — all 7 fields

```
marker: <type>,<lat>,<long>,<link>,<description>,<minZoom>,<maxZoom>
```

```leaflet
marker: default, 39.983334, -82.983330, [[Note]], My Location, 3, 8
```

`type`, `lat`, `long` are required. `link`, `description`, `minZoom`, `maxZoom` are optional but positional — **omitting `description` while keeping `minZoom`/`maxZoom` still needs the empty slot**, e.g. `marker: default, 40, 90, [[Note]], , 3, 8`. Dropping the whole tail (`marker: default, 40, 90, [[Note]]`) is valid syntax but silently produces a marker with no pop-up text — not a syntax error, just a missing field.

## Multiple markers — one `marker:` key, a list of plain strings

```leaflet
marker:
  - default, 40, -80, [[Note1]], Abandoned watchtower
  - event, 41, -81, [[Note2]], Festival grounds, 2, 6
```

Each entry is a bare CSV string — the same 7 comma-separated fields as the
inline form, just indented under one key. The plugin runs every entry through
papaparse, so the entry must reach it as a **string**.

Two shapes that look right and kill the whole map, silently apart from a
console error:

- **Flow sequences** (`- [default, 40, -80, [[Note1]]]`) parse to arrays.
  papaparse gets a non-string, falls through to `FileReader.readAsText`, and
  throws `parameter 1 is not of type 'Blob'` out of `buildMap` — no image, no
  markers, no zoom controls, just an empty dark container.
- **Repeated `marker:` keys**, one per line, throw
  `YAMLParseError: Map keys must be unique`. The plugin catches that and falls
  back to a naive `split(":")` over the whole block, which discards `bounds`
  and every other structured parameter.

No commas inside a description, in either form: fields split on commas, and
CSV quoting does not rescue it because the space after `, ` means the quote is
not the field's first character.

## Markers from files

```leaflet
markerFile: [[WikiLinkToFile]]
markerFile: Direct/Path/To/Note

markerFolder: Direct/Path/To/Folder
markerFolder: Path/To/Folder/  # trailing slash limits recursion depth

markerTag: tag1, tag2
markerTag:
  - tag1
  - [tag2, tag3]

filterTag: "#location", "#active"

linksTo: [[Note]]
linksFrom:
  - [[Note1]]
  - [[Note2]]
```

Each note found this way supplies its own marker position/type via frontmatter (below).

## Frontmatter-driven markers (for `markerFile`/`markerFolder`/`markerTag`)

```yaml
---
location: [40, -89]
mapmarker: event
mapzoom: [2, 8]
mapmarkers:
  - [type, [lat, long], description, minZoom, maxZoom]
mapoverlay:
  - [color, [lat, long], 100 miles, description]
---
```

## Custom marker types — Settings tab only, no config file

There is **no `markers.json` or other per-note/per-folder config file** for defining custom marker types. A custom type (a distinct icon and/or color, referenced by name in `marker:`/`mapmarker:`) is created in exactly one place: **Obsidian Settings → Community plugins → Leaflet → marker types** — set a unique Marker Name and a Font Awesome Free icon name, then reference that name:

```leaflet
marker: watchtower, 40, 90, [[Widow's Hollow]], Abandoned watchtower
```

```yaml
mapmarker:
  icon: user
  color: 00ff00
  layer: false
```

This vault currently defines **zero** custom marker types (`markerIcons: []` in `data.json`) — every existing marker uses the plugin's built-in `default` type (`iconName: map-marker`).
