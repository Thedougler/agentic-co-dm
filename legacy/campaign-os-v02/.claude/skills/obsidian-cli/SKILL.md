---
name: obsidian-cli
description: >
  The `obsidian` CLI for a Campaign OS repo's Obsidian vault. Use when reading, creating,
  searching, or setting properties on notes from the command line against a running Obsidian
  instance (not just editing .md files on disk), or when developing or debugging an Obsidian
  plugin or theme — reloading it, running JS in the app context, inspecting the DOM or CSS, or
  taking a screenshot.
---

# Obsidian CLI

Use the `obsidian` CLI to interact with a running Obsidian instance. Requires Obsidian to be open.

## Command reference

Run `obsidian help` to see all available commands. This is always up to date. Full docs: https://help.obsidian.md/cli

## Syntax

**Parameters** take a value with `=`. Quote values with spaces:

```bash
obsidian create name="My Note" content="Hello world"
```

**Flags** are boolean switches with no value:

```bash
obsidian create name="My Note" silent overwrite
```

For multiline content use `\n` for newline and `\t` for tab.

## File targeting

Many commands accept `file` or `path` to target a file. Without either, the active file is used.

- `file=<name>` — resolves like a wikilink (name only, no path or extension needed)
- `path=<path>` — exact path from vault root, e.g. `<folder>/<note>.md`

## Vault targeting

Commands target the most recently focused vault by default. Use `vault=<name>` as the first parameter to target a specific vault:

```bash
obsidian vault="My Vault" search query="test"
```

## Common patterns

```bash
obsidian read file="My Note"
obsidian create name="New Note" content="# Hello" template="Template" silent
obsidian append file="My Note" content="New line"
obsidian search query="search term" limit=10
obsidian daily:read
obsidian daily:append content="- [ ] New task"
obsidian property:set name="status" value="done" file="My Note"
obsidian tasks daily todo
obsidian tags sort=count counts
obsidian backlinks file="My Note"
```

Use `--copy` on any command to copy output to clipboard. Use `silent` to prevent files from opening. Use `total` on list commands to get a count.

## Plugin development

Reloading a plugin/theme after a code change, checking for errors, verifying visually
(screenshot/DOM inspection), reading console output, running JS in the app context,
inspecting CSS, or toggling mobile emulation: `references/plugin-development.md`.

## Reference files

| File | Covers |
|---|---|
| `references/plugin-development.md` | Develop/test reload cycle, error/console checks, screenshot/DOM/CSS inspection, JS eval, mobile emulation |
