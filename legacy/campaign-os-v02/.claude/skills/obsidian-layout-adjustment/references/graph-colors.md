# Graph view coloring — colorGroups procedure

Obsidian graph-view coloring for a Campaign OS vault (vault/ present),
by rewriting `vault/.obsidian/graph.json` colorGroups off this repo's own
tags/folders. A pure JSON config edit — no page content changes, no
frontmatter writes, no CSS. Read this when the DM says "color my graph",
"color code Obsidian", "colorize the graph", "color by tag/category",
"highlight visibility in graph", "make the graph colorful", or wants the
graph view tinted by tag, top-level folder, or `visibility/*` tag.

In this repo the Obsidian vault root is the git repo root — resolve it with
`git rev-parse --show-toplevel`, never assume a subfolder or an env var.

Obsidian stores graph settings in `vault/.obsidian/graph.json`. The
`colorGroups` array is a list of `{query, color}` pairs; the first matching
query wins per node. Queries use Obsidian's search syntax: `tag:#foo`,
`path:"content"`, `file:foo`, etc. Color is `{"a": 1, "rgb": <packed-int>}`
where the int is `(R << 16) | (G << 8) | B`.

## Before you start

1. Confirm `vault/.obsidian/` exists (it does once the vault has been
   opened in Obsidian at least once). If it doesn't, tell the user to open
   the vault once in Obsidian, then re-run.
2. **Warn the user if Obsidian is likely open**: Obsidian overwrites
   `graph.json` on close. Tell them to close the vault first, or be ready to
   reload (Cmd/Ctrl+R) and not touch the graph settings until they reload.

## Step 1: pick a mode

Infer the mode from the user's phrasing. If ambiguous, default to **by-tag**.

| User intent | Mode |
|---|---|
| "color by tag", "color my graph", "make it colorful" (default) | `by-tag` |
| "color by folder", "color by category", "color by directory" | `by-category` |
| "highlight visibility", "show internal/pii in graph", "visibility colors" | `by-visibility` |
| User provides explicit mapping (`tag:#foo = red`, or JSON blob) | `custom` |
| "combine tag and visibility" / "both" | `combined` (visibility first, then tag) |

## Step 2: build the `colorGroups` array

### Palette (10 distinct, colorblind-friendly colors)

Use in order. If more groups than colors, cycle and add a lightness shift by
dividing brightness ~20% via a second pass — or just cap at 10 and tell the
user the remaining tags share the "other" color.

| # | Hex | rgb (packed int) | Role |
|---|---|---|---|
| 0 | `#4E79A7` | `5142951` | blue |
| 1 | `#F28E2B` | `15896107` | orange |
| 2 | `#E15759` | `14767961` | red |
| 3 | `#76B7B2` | `7780786` | teal |
| 4 | `#59A14F` | `5873999` | green |
| 5 | `#EDC948` | `15583048` | yellow |
| 6 | `#B07AA1` | `11565217` | purple |
| 7 | `#FF9DA7` | `16751527` | pink |
| 8 | `#9C755F` | `10253663` | brown |
| 9 | `#BAB0AC` | `12234924` | gray |

Every color is wrapped as `{"a": 1, "rgb": <int>}`.

### Mode: `by-tag`

1. Glob `vault/**/*.md` excluding `raw/`, `vault/.obsidian/`,
   `node_modules/`, `tmp/`, and vendored SRD/craft reference material
   (not campaign tags).
2. Parse frontmatter `tags` from each page. Count usage per tag.
3. **Drop `visibility/*` tags** from the frequency list — they are reserved
   system tags, handled only in `by-visibility` or `combined` mode.
4. Take the top 10 tags by usage. If there are fewer than 10 unique tags, use
   all of them.
5. For each tag `T` at index `i`: emit `{"query": "tag:#T", "color": palette[i]}`.
6. Optionally, append a final catch-all entry for untagged pages at the end:
   `{"query": "-[\"tag\":]", "color": palette[9]}` — **skip** if color slot 9
   is already taken by a real tag.

### Mode: `by-category`

Use this repo's top-level folders in this fixed order so colors are stable
across runs:

| Folder | Color index |
|---|---|
| `content` | 0 (blue) |
| `pcs` | 1 (orange) |
| `sessions` | 2 (red) |
| `sys` | 3 (teal) |
| `docs` | 4 (green) |
| `Inbox` | 5 (yellow) |
| `archive` | 6 (purple) |

Emit one entry per folder that exists AND contains at least one `.md` file.
Each entry is:

```json
{"query": "path:\"<folder>\"", "color": {"a": 1, "rgb": <int>}}
```

### Mode: `by-visibility`

Emit exactly three entries, in this order (first-match wins, so most
restrictive comes first):

1. `visibility/pii` → `#E15759` (red, rgb 14767961)
2. `visibility/internal` → `#F28E2B` (orange, rgb 15896107)
3. `visibility/public` → `#59A14F` (green, rgb 5873999)

```json
{"query": "tag:#visibility/pii", "color": {"a": 1, "rgb": 14767961}}
```

Pages with no `visibility/` tag remain Obsidian's default color — do not add
a catch-all.

### Mode: `combined`

Emit `by-visibility` entries first, then `by-tag` entries. Visibility wins on
conflict because it appears first in the list.

### Mode: `custom`

If the user gave explicit mappings, honor them literally. Convert any hex
they give (e.g. `#FF00FF`) to packed int using `int(hex_without_hash, 16)`.
Wrap each as `{"a": 1, "rgb": <int>}`.

## Step 3: merge into graph.json (do not clobber)

1. Read the existing `vault/.obsidian/graph.json`. If it doesn't
   exist, start from this minimal default:

   ```json
   {
     "collapse-filter": true,
     "search": "",
     "showTags": false,
     "showAttachments": false,
     "hideUnresolved": false,
     "showOrphans": true,
     "collapse-color-groups": false,
     "colorGroups": [],
     "collapse-display": true,
     "showArrow": false,
     "textFadeMultiplier": 0,
     "nodeSizeMultiplier": 1,
     "lineSizeMultiplier": 1,
     "collapse-forces": true,
     "centerStrength": 0.518713248970312,
     "repelStrength": 10,
     "linkStrength": 1,
     "linkDistance": 250,
     "scale": 1,
     "close": true
   }
   ```

2. **Back up first**: copy the existing file to
   `vault/.obsidian/graph.json.backup-<YYYYMMDD-HHMM>` before writing. If a backup
   from the same minute exists, reuse it — don't pile up duplicates.
3. Replace **only** the `colorGroups` field with your new array. Leave
   every other field untouched. This preserves the user's zoom, physics,
   filter, search, and display preferences.
4. Write the file back with the same JSON style as the original (usually
   compact single-line or 2-space indent — preserve what's there).

## Step 4: report and log

Print a summary like:

```
Graph colorized → vault/.obsidian/graph.json
  Mode:    by-tag
  Groups:  7 color assignments
  Palette: blue, orange, red, teal, green, yellow, purple
  Backup:  vault/.obsidian/graph.json.backup-20260424-1432

Reload Obsidian (Cmd/Ctrl+R) to see the new colors.
If Obsidian is currently open, close it first OR reload immediately — Obsidian
overwrites graph.json on close and can erase these changes.
```

## Edge cases

- **No tags in vault** in `by-tag` mode → fall back to `by-category` and
  tell the user.
- **User wants to undo** → restore from the latest `graph.json.backup-*`.
- **User wants to clear all color groups** → set `colorGroups: []` and back
  up first.
- **`vault/.obsidian/` missing** → the vault hasn't been opened in Obsidian yet.
  Tell the user to open it once, then re-run. Don't create `vault/.obsidian/`
  yourself — Obsidian populates many files there on first open.
- **Query syntax gotchas**: folder paths with spaces need quoting
  (`path:"my folder"`); tags with nested slashes work literally
  (`tag:#visibility/internal`); don't URL-encode.
- **Obsidian open during edit**: surface the risk — Obsidian reads
  graph.json at startup and **rewrites it on close**. If the user is editing
  live, tell them to close Obsidian first or run the reload (Cmd/Ctrl+R)
  immediately and avoid opening graph settings before they do.

## Notes

- This is a pure config edit — no page content changes, no frontmatter writes.
- Re-running is safe: each run creates a new backup, only `colorGroups` is
  rewritten.
- If the user has manually curated color groups they want to keep, offer
  `combined` mode or ask before overwriting.
