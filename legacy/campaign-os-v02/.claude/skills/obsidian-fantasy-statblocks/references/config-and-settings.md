# Config keys, layouts, and Plugin Settings

## Config-mode keys (rendering/behavior, not creature data)

```yaml
layout: Basic 5e Layout   # exact string match — see landmine in SKILL.md
name: "..."                # the only key the plugin's own docs call unconditionally required
dice: true                 # clickable dice rollers via the Dice Roller plugin
columns: 2                  # forceColumns: true to force a column split on a small block
source: "Homebrew"
bestiary: true               # false excludes this specific fence from bestiary registration entirely
```

`dice: true` is the per-block way to turn on dice-roller integration; the "Integrate
dice roller" Plugin Setting turns it on vault-wide instead of per-block.

## Plugin Settings screen (Community Plugins → Fantasy Statblocks)

Verified fields, from the plugin's own docs site:

- **General**: Enable export to png, Integrate dice roller, Render dice rolls, Try to
  render wikilinks, Disable 5e srd, Enable debug messages.
- **Note parsing**: Parse frontmatter for creatures, Bestiary folders (this vault:
  `vault/campaigns/shattered-sea/monsters/srd` and `vault/campaigns/shattered-sea/monsters/homebrew`).
- **Advanced**: Try to save data atomically.
- **Layout settings**: Import from json, Add new layout, Default layout (this vault:
  `Basic 5e Layout`), Show advanced options, Layout list.
- **Homebrew creatures**: Import homebrew creatures, Adding creatures ("Add Creature"
  button — YAML or JSON), Filtering creatures, List.

## Built-in layout catalog

| Layout | Use in this campaign |
|---|---|
| Basic 5e Layout | Yes — the only layout this vault uses (`data.json` default: `basic-5e-layout`) |
| Basic Fate Core Layout | No — this campaign is 5e only |
| Basic Pathfinder 2e Layout | No |
| Basic 13th Age Monster Layout | No |

This vault has **no custom layouts** configured (`layouts: []` in `data.json`) — layout
customization (Duplicate and Edit a Layout, Editing Layouts, Custom CSS) is greenfield
here, not an existing convention to match.

## This vault's actual settings snapshot

`vault/.obsidian/plugins/obsidian-5e-statblocks/data.json`:

- `default: "basic-5e-layout"`
- `paths: ["vault/campaigns/shattered-sea/monsters/srd", "vault/campaigns/shattered-sea/monsters/homebrew"]` — the "Bestiary
  folders" setting
- `autoParse: true`
- `layouts: []`
- `version: {major: 4, minor: 10, patch: 3}`
