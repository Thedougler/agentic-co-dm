# Output files

`render` → the guide; `beautify.mjs` → styled art; `composite` → the finished map.

| File | What it is |
|---|---|
| `<stem>.base.png` | The **guide** (filled surfaces + outlined labeled regions) — the beautify input. |
| `<stem>.flat.png` | base + grid: a flat schematic you can play from as-is if you skip beautify. |
| `<stem>.grid.png` | Transparent grid layer (the script reuses it; rarely opened directly). |
| `<stem>.art.png` | The styled painting from `beautify.mjs` — aspect-locked, not yet gridded. |
| `<stem>.player.png` | **Finished, table-ready map:** styled art + crisp grid. |
