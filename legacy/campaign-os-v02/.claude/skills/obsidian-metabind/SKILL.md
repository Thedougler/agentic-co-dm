---
name: obsidian-metabind
description: The Meta Bind plugin syntax ("Metabind") for a Campaign OS repo (vault/ present). Use when adding a bound `INPUT[...]` field, a reactive `VIEW[...]` display, or a `meta-bind-button` action — an interactive tracker, toggle, dropdown, counter, or button. Not player-facing pages (no Quartz render).
---

# Obsidian Meta Bind

The installed plugin's real name is **Meta Bind** (`mProjectsCode/obsidian-meta-bind-plugin`, this vault runs v1.4.15); "Metabind" below is the repo's own shorthand. It turns frontmatter and in-memory state into interactive widgets embedded anywhere in a note's body, not just the properties panel.

## Quick syntax

One family, one line:

```
`INPUT[toggle(onValue(true), offValue(false)):poisoned]`
```

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```
*(this vault's actual convention — see `references/view-fields.md` and `.claude/skills/reference-images/SKILL.md`)*

```meta-bind-button
label: ➖ Deal Damage
style: destructive
action:
  type: updateMetadata
  bindTarget: hp_current
  value: "x - 1"
  evaluate: true
```

## What you need → which file

| Need | Family | Reference file |
|---|---|---|
| A value someone edits by hand — text, number, toggle, slider, date, select, list, suggester | `INPUT[...]` | `references/input-fields.md` |
| A computed/derived value shown, optionally written back — math, text, link, image | `VIEW[...]` | `references/view-fields.md` |
| A click that does something — run a command, edit a note, chain to another plugin | `BUTTON`/fence | `references/button-actions.md` |
| Any `:bindTarget` or `{...}` — which storage, which note, which property | addressing | `references/bind-targets.md` |
| A full feature composed from the above — tracker, checklist, per-row field, dashboard edit | worked patterns | `references/patterns.md` |

## What NOT to do

- Never rely on Metabind content for player-facing pages — it does not run in Quartz, so a `meta-bind`/`meta-bind-button` block renders nothing on the published site (`.claude/skills/reference-images/SKILL.md`) → publish-facing content stays plain markdown or a `.base` embed.
- Never write a dynamic or computed bind target — bind targets are static strings; this vault has `enableJs: false` (no JS Engine plugin installed), so the JS-Engine workaround for dynamic targets is unavailable → write the literal target, or flag a JS Engine install to the user first.
- Never quote a multi-value `option()` with double quotes — only single quotes support commas/spaces inside a value (`\'`/`\\` to escape) → `option('Yes, and', 'yes-and')`, never `option("Yes, and", ...)`.
- Never assume a block inside `_templates/*.md` is broken because it looks static — `excludedFolders: ["templates"]` means the template file itself doesn't render Metabind widgets live; a page instantiated from it does.
- Never address a frontmatter property with spaces via the bare dotted form (`field name#prop`) — it silently fails, no error → use the JS bracket form, `["field name"]`.
- Never reach for the Dataview-loop pattern in `references/patterns.md` without checking first — Dataview is not currently installed in this vault (`vault/.obsidian/community-plugins.json` has no `obsidian-dataview` entry).
- For "how do I subtract/add/reset a number bound to frontmatter" — reach for the button's own `updateMetadata` action (`references/button-actions.md`) before reaching for an external script or plugin; it's Meta Bind's native primitive for exactly this.

## Reference files

| File | Covers |
|---|---|
| `references/bind-targets.md` | The `storageType^storagePath#property` addressing scheme, storage types, cross-note targets, the spaces-need-brackets gotcha |
| `references/input-fields.md` | All `INPUT` field types, their arguments, and the quoting rule, with a worked example per type family |
| `references/view-fields.md` | `VIEW` types (math/text/link/image), arguments, circular-write blocking, the cross-note staleness caveat |
| `references/button-actions.md` | `meta-bind-button` config fields, inline `BUTTON[id]` references, all 13 action types and their required fields |
| `references/patterns.md` | 4 composed, copy-paste-ready examples for this vault's content shapes (creature/NPC/PC/template) |
