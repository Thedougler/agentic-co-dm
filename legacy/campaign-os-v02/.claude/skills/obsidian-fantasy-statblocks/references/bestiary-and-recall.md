# Bestiary and recall

How a creature actually gets into the Fantasy Statblocks bestiary, and how to pull it
back out elsewhere in the vault.

## Registration

Every page under `vault/srd/monsters/` or `vault/campaigns/shattered-sea/monsters/` that
carries a fence also carries `statblock: inline` frontmatter with a `name:` matching
its own codeblock `name:` exactly (`_templates/statblock.md`) — the note's fence
auto-registers into the plugin's bestiary. The "Bestiary folders" plugin setting
lists both directories (`.claude/skills/obsidian-fantasy-statblocks/references/config-and-settings.md`),
matching exactly where every fence lives — no folder-scope mismatch to reason about.

Two other creation methods exist but aren't this vault's convention:

- **Manual "Save to Bestiary"** — render any fence, open its menu, click "Save to
  Bestiary." Writes straight into the plugin's own cache
  (`vault/.obsidian/plugins/obsidian-5e-statblocks/data.json`'s `monsters` list), works from
  any directory. A few pages were registered this way; new pages use frontmatter
  instead — it's git-tracked and reproducible, a cache entry isn't.
- **Homebrew Creatures settings screen** — an "Add Creature" button in Plugin
  Settings, YAML or JSON directly in settings, no source note in the vault at all.

## Recall

```statblock
monster: <SRD/Homebrew Monster Name>
```

Recall is by exact name only — no fuzzy search, no path lookup. The plugin also ships
its own bundled 5e SRD (toggle: "Disable 5e srd"), so `monster: Goblin` resolves even
before checking this vault's own `vault/campaigns/shattered-sea/monsters/` pages — a plain `monster:`
recall can't tell you which source it actually pulled from without checking.

## Override, append, remove

```statblock
layout: Basic 5e Layout
monster: Octopus
name: "My Octopus Friend"
```

A bare field (`name`, `hp`, `ac`, ...) **replaces** the recalled creature's value for
that field.

```statblock
layout: Basic 5e Layout
monster: Octopus
name: "My Octopus Friend"
actions+:
  - name: "Tentacles Akimbo"
    desc: "..."
```

`field+:` **appends** to an inherited array (`traits+:`, `actions+:`,
`bonus_actions+:`, `reactions+:`) — a bare `field:` (no `+`) replaces the whole array
instead, silently dropping every inherited entry. Remove one inherited entry by name
with `field-:` (e.g. `actions-:` with `- name: Scimitar`).

`vault/refs/vault/monster/references/statblock-format.md` also names `extends:` alongside `monster:` for this same
replace-vs-append landmine — treat any `extends:` recall the same way as `monster:`
above.
