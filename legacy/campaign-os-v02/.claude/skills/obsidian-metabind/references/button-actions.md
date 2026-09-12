# Buttons

Two forms: a full `meta-bind-button` fenced config block, and an inline reference to one.

## Inline reference

```
`BUTTON[my-button-id]`
`BUTTON[id1, id2, id3]`
```

References a `meta-bind-button` block (matched by `id`) declared **elsewhere in the same note**. Group members are typically declared `hidden: true` so only the inline reference row renders.

## The config block

```yaml
```meta-bind-button
style: primary            # default | primary | destructive | plain
label: Deal Damage
icon: <lucide-icon-name>   # optional
class: my-css-class        # optional, space-separated
cssStyle: "color: red"     # optional
backgroundImage: path.png  # optional
tooltip: "..."             # optional, defaults to label
id: deal-damage             # optional, needed for BUTTON[id] refs
hidden: true                # optional
action:                     # OR actions: (array) — mutually exclusive, never both
  type: command
  command: obsidian-meta-bind-plugin:open-faq
```
```

`action:` and `actions:` are mutually exclusive — a block with both is invalid, pick one.

## All 13 action types

| `type` | Required fields | Notes |
|---|---|---|
| `command` | `command` | Runs an Obsidian command id |
| `open` | `link`, `newTab?` | File link `[[..]]` or URL |
| `input` | `str` | Inserts text at cursor in the focused element |
| `sleep` | `ms` | Pause between chained `actions:` |
| `createNote` | `fileName`, `folderPath?`, `openNote?`, `openIfAlreadyExists?` | Duplicate names get a ` 1`, ` 2`… suffix |
| `templaterCreateNote` | `templateFile`, `folderPath?`, `fileName?`, `openNote?`, `openIfAlreadyExists?` | Needs the Templater plugin |
| `runTemplaterFile` | `templateFile` | Executes every Templater command in the file |
| `insertIntoNote` | `line`, `value`, `templater?` | `line` is absolute or a relative expr (below) |
| `replaceInNote` | `fromLine`, `toLine`, `replacement`, `templater?` | Line-range replace |
| `regexpReplaceInNote` | `regexp`, `regexpFlags?` (default `g`), `replacement` (`$1` supported) | Whole-note regex replace |
| `replaceSelf` | `replacement`, `templater?` | Replaces the button's own code block — block-buttons only |
| `updateMetadata` | `bindTarget`, `evaluate` (bool), `value` | `evaluate: true` → `value` is a JS expr, current value available as `x`, other props via `getMetadata(bindTarget)` |
| `inlineJS` | `code` | Needs JS Engine + `enableJs` — **not available in this vault** |
| `js` | `file`, `args?` | Needs JS Engine + `enableJs` — **not available in this vault**; args land in `context.args` |

Relative line references (`insertIntoNote`/`replaceInNote`): `fileStart`, `fileEnd`, `frontmatterStart`, `frontmatterEnd`, `contentStart`, `contentEnd`, `selfStart`, `selfEnd` — e.g. `line: selfEnd + 1`.

## `updateMetadata` — the native primitive for counters/trackers

For "subtract/add/reset a number bound to frontmatter", reach for this first — it's Meta Bind's own answer, no external script needed:

```yaml
```meta-bind-button
label: "Deal Damage"
style: destructive
id: "deal-damage"
action:
  type: updateMetadata
  bindTarget: hp_current
  evaluate: true
  value: "x - getMetadata('damage')"
```
```
```
Damage: `INPUT[number:damage]` `BUTTON[deal-damage]`
```

## CSS styling

Target the child element, not the wrapper class alone: `.mb-button.<class> > button`, `.mb-input-wrapper.<class> > input`, `.mb-input-type-progressBar.<class> .mb-progress-bar-progress` — the wrapper class by itself is a common stumbling block.

## This vault's own button roster

Every live `meta-bind-button` in this vault uses `action: {type: command, command: obsidian-shellcommands:shell-command-<id>}`, chaining to the separate Shell Commands plugin — never `js`/`inlineJS` (no JS Engine installed here). That specific pattern (voice recording, scene music, combat sim) has its command roster in `vault/.obsidian/plugins/obsidian-shellcommands/data.json`; check it before adding a new Shell-Commands-backed button rather than reproducing its roster here. Reach for `updateMetadata` (above) instead of a new shell script whenever the goal is purely "change a frontmatter value" — Shell Commands is for genuinely external actions (recording audio, running the combat simulator), not for arithmetic Meta Bind already does natively.
