# Composed patterns

Four features built from `input-fields.md` + `view-fields.md` + `button-actions.md` + `bind-targets.md` together. Each names a real vault path — adapt the bind targets to the actual page's frontmatter, don't invent new property names when an equivalent already exists.

## 1. HP / damage tracker

For `vault/campaigns/shattered-sea/monsters/**/*.md` or `_templates/pc-sheet.md`'s Stats & Combat section — a number field, a live display, and a native `updateMetadata` damage button (see `button-actions.md` for why this beats an external script):

```
Current HP: `INPUT[number:hp_current]`
```
```meta-bind
VIEW[{hp_current} / {hp_max}][text]
```
```
Damage: `INPUT[number:damage]`
```meta-bind-button
label: "Deal Damage"
style: destructive
action:
  type: updateMetadata
  bindTarget: hp_current
  evaluate: true
  value: "x - getMetadata('damage')"
```
```

## 2. Condition-toggle checklist

For an NPC or creature page — combat-only state that shouldn't pollute frontmatter, so it binds to `memory` (ephemeral, per-file — see `bind-targets.md`) instead:

```
`INPUT[toggle:memory^#poisoned]` Poisoned
`INPUT[toggle:memory^#stunned]` Stunned
`INPUT[toggle:memory^#prone]` Prone
```

## 3. Dataview-loop per-row `INPUT` fields

**Not currently installed in this vault** — `vault/.obsidian/community-plugins.json` has no `obsidian-dataview` entry. Documented here for when/if it's added; confirm with the user before using. The community pattern: a `dataviewjs` block emits one `INPUT[...]` string per row, interpolating `file.path` so each row edits a different note:

```dataviewjs
for (const page of dv.pages('"vault/campaigns/shattered-sea/npcs"')) {
  dv.paragraph("`INPUT[inlineSelect(option(active), option(retired)):" + page.file.path + "#status]`");
}
```

## 4. Dashboard remote-edit pattern

A single note editing a bound field on a *different* note, via a full-path cross-note bind target (`bind-targets.md`):

```
`INPUT[toggle:vault/campaigns/shattered-sea/quests/kalowe-takowan#resolved]`
```

**Repeat the VIEW staleness caveat here, not three clicks away**: if the dashboard also shows a `VIEW[{vault/campaigns/shattered-sea/quests/kalowe-takowan#resolved}]`, that display freezes the moment `vault/campaigns/shattered-sea/quests/kalowe-takowan.md` itself is closed — the INPUT above still writes correctly regardless (INPUT writes are not affected by the staleness limitation, only VIEW reads are).
