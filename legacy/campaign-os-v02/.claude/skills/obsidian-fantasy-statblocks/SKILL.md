---
name: obsidian-fantasy-statblocks
description: The Fantasy Statblocks plugin syntax (javalent/fantasy-statblocks), in a Campaign OS repo (vault/ present). Use when authoring/editing a `statblock` code block, choosing a layout, wiring a `![[<slug>-statblock]]` embed, registering/recalling a creature via `monster:`, or configuring the plugin's Settings. Not the 5e stat-block schema or `sim:` grammar (monster GUIDE, dndsim).
---

# Fantasy Statblocks

The installed plugin is **Fantasy Statblocks** (`javalent/fantasy-statblocks`, packaged
in this vault as `obsidian-5e-statblocks` v4.10.3). It renders a `​```statblock` code
block into a playable D&D stat block and maintains an internal **bestiary** — a
name-indexed cache other notes and the Initiative Tracker plugin recall from with
`monster: <name>`.

Every stat block in this vault lives on its own page under
`vault/campaigns/shattered-sea/monsters/{srd,homebrew}/` (`vault/_templates/_srd/_statblock.md`) — a creature or NPC
page never carries the fence itself; it embeds the statblock page instead:
`![[<slug>-statblock]]`. See `references/directory-and-embeds.md` for the
naming pattern and why the split exists.

For the full required-5e-field schema, WotC attack/save wording patterns, and the
`sim:` extension namespace dndsim reads, see
`vault/refs/vault/monster/references/statblock-format.md` and
`utils/dndsim/README.md` (schema/CLI source of truth, dndsim's monster data
source) — this skill covers the plugin's general
mechanics instead: config keys, layouts, and how the bestiary actually gets populated.

## Quick syntax

Real page, `vault/srd/monsters/roper.md`:

```statblock
layout: Basic 5e Layout
name: "Roper"
size: Large
type: aberration
alignment: "Neutral Evil"
ac: 20
hp: 93
hit_dice: "11d10 + 33"
speed: "10 ft., Climb 20 ft."
stats: [18, 8, 17, 7, 16, 6]
senses: "darkvision 60 ft.; Passive Perception 16"
cr: 5
```

Any creature/NPC page shows this with `![[roper]]` (field schema
in full: `vault/refs/vault/monster/references/statblock-format.md`).

## What you need → which file

| Need | Reference file |
|---|---|
| Required 5e fields, WotC wording, 2014/2024 grammar parity | `vault/refs/vault/monster/references/statblock-format.md` (not this skill) |
| The `sim:` extension schema | `utils/dndsim/README.md` (dndsim CLI/schema) — not this skill |
| Where a new statblock page goes, its filename, the embed syntax a creature/NPC page uses | `references/directory-and-embeds.md` |
| How bestiary registration works, recall (`monster:`), override/append/remove syntax | `references/bestiary-and-recall.md` |
| Config-mode keys (layout, dice, columns, source, bestiary), Plugin Settings screen, layout catalog | `references/config-and-settings.md` |
| Current dndsim parsing gaps for an action's `desc` grammar | `utils/dndsim/DIVERGENCES.md` (not this skill — gaps get fixed, a copy here would rot) |

## What NOT to do

- Never write a `statblock` fence inline on a creature, NPC, or encounter page —
  every fence lives on its own `vault/campaigns/shattered-sea/monsters/{srd,homebrew}/<slug>.md` page; the
  origin page gets `![[<slug>-statblock]]` instead (`references/directory-and-embeds.md`).
- Never type a layout name other than `Basic 5e Layout` for this campaign — the vault
  has zero custom layouts configured (`layouts: []`) and the Fate Core/Pathfinder
  2e/13th Age built-ins don't apply to a 5e-only game (`references/config-and-settings.md`).
- Never assume `actions+:`/`traits+:` merges with a recalled creature's inherited list
  — a bare `actions:`/`traits:` (no `+`) *replaces* the whole inherited array; remove
  one inherited entry by name with `actions-:` instead (`references/bestiary-and-recall.md`,
  also documented in `vault/refs/vault/monster/references/statblock-format.md`).
- Never leave a statblock page's `statblock: inline` frontmatter `name:` out of sync
  with its own codeblock `name:` — the plugin registers by the frontmatter value, so a
  mismatch orphans the creature from `monster:` recall with no error shown.
- Never reword an action's `desc` to dodge a dndsim parsing gap — write the
  RAW/SRD text accurately regardless (`vault/refs/vault/monster/references/statblock-format.md`'s grammar-parity rule);
  extend the parser instead. Check the parser's `warnings` array or run the
  `w-statblock-simulatable` lint before trusting a sim result — current known gaps
  live in `utils/dndsim/DIVERGENCES.md`, not here (they change as they get fixed).
- Never treat `monster: Goblin` resolving as proof it came from this vault's own
  `vault/campaigns/shattered-sea/monsters/` pages — the plugin also ships its own bundled 5e SRD (the
  "Disable 5e srd" plugin setting), independent of anything authored in this repo.

## Reference files

| File | Covers |
|---|---|
| `references/directory-and-embeds.md` | The `vault/campaigns/shattered-sea/monsters/{srd,homebrew}/` directories, the two filename patterns (a bare stat-block page vs an extracted `<slug>-statblock.md`), and the `![[...]]` embed convention |
| `references/bestiary-and-recall.md` | How registration works, recall (`monster:`), override, `+`/`-` append/remove |
| `references/config-and-settings.md` | Config-mode keys, Plugin Settings screen, built-in layout catalog, this vault's real settings snapshot |
