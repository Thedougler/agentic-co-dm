---
name: foundry-stage
description: >-
  Stage wiki entities into a running FoundryVTT world as playable actors,
  items, journals, and scenes. Use when the user says "push to Foundry",
  "stage this encounter", "create the NPC in Foundry", "set up tonight's
  session in Foundry", or wants any vault note converted into a live
  Foundry entity. Covers creatures (statblock → actor), items
  (magic-item → world item), journals (narrative notes → journal entries),
  quests, encounters (roster + notes → actors + journal), and session
  staging (batch all entities for a session). Not for generating images —
  hand off token art to **foundry-token** and battlemap art to
  **foundry-battlemap**. Not for in-session token movement, combat
  tracking, or player-facing chat.
---

# Foundry Stage
## Accepted-Work gate

Prep only. Follow `docs/agents/work.md`. Precondition: local `mcp.json` (copied from `Documents/ai-co-dm/mcp.json`) and `foundry-data` symlink to the same Foundry Data directory as `Documents/ai-co-dm/foundry-data`. Do not create a second world. Precondition: the source page is canon under the rule (`llm-wiki`). If it is not, refuse and name that gate. If `reveal: unrevealed`, do not stage player-visible text until the DM accepts a reveal. Wording matches accepted text.

Push vault content into FoundryVTT so the table can play it.

Three leading words:

- **check** — does this entity already exist in Foundry?
- **stage** — create the entity via MCP tool calls
- **wire** — attach features, items, or tokens to a staged entity

Wiki is the source of truth. Foundry is the runtime. Every staged entity
traces to a vault note.

## How Foundry works

**MCP tools** — primary for entity CRUD (actors, items, journals). The
world data is LevelDB; direct file edits corrupt it.

**Symlink** (`foundry-data/` → Foundry's Data directory) — primary for
asset placement. Recreate it from the campaign of record; do not invent a
new Data root. Copy vault images from `wiki/attachments/` into
`foundry-data/assets/` so Foundry can reference them by path.

Asset paths in Foundry reference from the Data root:
`foundry-data/assets/my-map.png` → reference as `assets/my-map.png`.

## Recipe 1 — Stage a creature

Source: a vault note with a ` ```statblock ` YAML block.

### Step 1: Check

Search Foundry for the creature by name.

```
tool: list-characters
params: { type: "npc" }
```

Scan the result for a name match. If found, report it and ask whether to
update or skip. Done when: you know the creature is absent or the user
said to proceed.

### Step 2: Read the statblock

Read the vault note. Find the ` ```statblock ` fence. The YAML inside
has these fields (all positional arrays and key-value maps):

```yaml
name: Wolfrabbit
size: Medium
type: beast
alignment: unaligned
ac: 14 (natural armor)
hp: 32 (5d8+10)
stats: [16, 14, 14, 3, 12, 6]
speed: 40 ft., burrow 10 ft.
senses: darkvision 60 ft.
cr: 2
traits:
  - name: Pack Tactics
    desc: "Advantage on attack rolls when an ally is within 5 ft."
actions:
  - name: Bite
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10+3) piercing damage."
```

Done when: you have the YAML fields extracted.

### Step 3: Stage the actor

Call `dnd5e-create-npc`. Map statblock fields to parameters:

| Statblock field | Parameter | How to convert |
|---|---|---|
| `name` | `name` | direct |
| `size` | `size` | lowercase: tiny, small, medium, large, huge, gargantuan |
| `type` | `creatureType` | enum: humanoid, beast, monstrosity, undead, fiend, etc. |
| `alignment` | `alignment` | direct |
| `ac` | `acMode: "flat"`, `acValue` | parse the number from "14 (natural armor)" → `14` |
| `hp` | `hpAverage` | parse the number before parentheses: "32 (5d8+10)" → `32` |
| `hp` parenthesized | `hpFormula` | the part inside parens: `"5d8+10"` |
| `stats` | `abilities` | positional: `{str: 16, dex: 14, con: 14, int: 3, wis: 12, cha: 6}` |
| `speed` | `walkSpeed`, `flySpeed`, `swimSpeed`, `burrowSpeed`, `climbSpeed` | split on comma; "40 ft." → `walkSpeed: 40`; "burrow 10 ft." → `burrowSpeed: 10` |
| `senses` | `darkvision`, `blindsight`, `tremorsense`, `truesight` | parse each: "darkvision 60 ft." → `darkvision: 60` |
| `cr` | `cr` | direct (accepts "1/4", "1/2", 0.25, 5) |
| `saves` | `savingThrows` | array of ability keys: `["dex", "wis"]` |
| `skillsaves` | `skills` | array: `[{skill: "Perception", proficiency: "proficient"}]` |
| `damage_immunities` | `damageImmunities` | array of strings |
| `damage_resistances` | `damageResistances` | array of strings |
| `condition_immunities` | `conditionImmunities` | array of strings |
| `languages` | `languages` | array of strings |

Always set `sourceRules: "2024"` (this campaign is 5.5e).

Set `biography` to the note's `[!narration]` block rendered as HTML.

Example call for the wolfrabbit above:

```json
{
  "name": "Wolfrabbit",
  "creatureType": "beast",
  "size": "medium",
  "cr": 2,
  "hpAverage": 32,
  "hpFormula": "5d8+10",
  "acMode": "flat",
  "acValue": 14,
  "abilities": {"str": 16, "dex": 14, "con": 14, "int": 3, "wis": 12, "cha": 6},
  "walkSpeed": 40,
  "burrowSpeed": 10,
  "darkvision": 60,
  "sourceRules": "2024"
}
```

Done when: `dnd5e-create-npc` returns success with an actor ID.

### Step 4: Wire compendium features

Collect all trait and action names from the statblock. Batch any that
match SRD features into one call:

```
tool: dnd5e-add-features-from-compendium
params: {
  actorIdentifier: "<actor name or ID>",
  featureNames: ["Pack Tactics", "Multiattack"]
}
```

The tool reports which names matched and which did not. Keep the
unmatched names for Step 5.

Done when: all SRD-matching features are imported, unmatched names listed.

### Step 5: Wire remaining features

For each unmatched trait or action, call `dnd5e-add-feature`. Pick the
`featureType` by pattern-matching the description text:

**Attack** — description contains "Weapon Attack:" and a to-hit bonus:

```json
{
  "featureType": "attack",
  "actorIdentifier": "<name>",
  "featureName": "Bite",
  "attackType": "melee",
  "damageParts": [{"number": 1, "denomination": 10, "type": "piercing", "bonus": 3}],
  "reachFt": 5,
  "description": "full description text"
}
```

**Save** — description contains "DC \d+ ... saving throw", no attack roll:

```json
{
  "featureType": "save",
  "actorIdentifier": "<name>",
  "featureName": "Breath Weapon",
  "saveAbility": "dex",
  "saveDC": 13,
  "damageParts": [{"number": 4, "denomination": 6, "type": "fire"}],
  "halfOnSave": true,
  "description": "full description text"
}
```

**Attack-with-save** — description has both an attack roll AND a save
after the hit:

```json
{
  "featureType": "attack-with-save",
  "actorIdentifier": "<name>",
  "featureName": "Venomous Bite",
  "attackType": "melee",
  "damageParts": [{"number": 1, "denomination": 6, "type": "piercing", "bonus": 3}],
  "saveAbility": "con",
  "saveDC": 12,
  "saveDamageParts": [{"number": 2, "denomination": 6, "type": "poison"}],
  "reachFt": 5,
  "description": "full description text"
}
```

**Passive** — everything else (traits, Multiattack text, reactions,
legendary actions):

```json
{
  "featureType": "passive",
  "actorIdentifier": "<name>",
  "featureName": "Keen Hearing",
  "description": "full description text"
}
```

For bonus actions, add `"activationType": "bonus"`.
For reactions, add `"activationType": "reaction"`.
For legendary actions, add `"activationType": "legendary"`.

See [references/feature-recipes.md](references/feature-recipes.md) for
spellcasting and area-effect patterns.

Done when: every trait and action from the statblock exists on the actor.

### Step 6: Token image

If `attachments/` has a token image for this creature, copy it into
Foundry's asset path:

```bash
cp "attachments/shattered-sea/creatures/<name>-token.png" \
   "foundry-data/assets/tokens/<name>-token.png"
```

The Foundry reference path is `assets/tokens/<name>-token.png`.

Done when: token image is placed, or no token image exists (report gap).

## Recipe 2 — Stage a scene

Source: a session-prep or encounter note with a Zones table and optionally
a battlemap image.

### Step 1: Check

```
tool: list-scenes
params: { filter: "<scene name>" }
```

If found, report and ask. Done when: scene status known.

### Step 2: Place the battlemap asset

If the note embeds a battlemap image, copy it from `attachments/` to
`foundry-data/assets/`:

```bash
cp "attachments/shattered-sea/battlemaps/<map-file>" \
   "foundry-data/assets/<map-file>"
```

The Foundry reference path is `assets/<map-file>`.

If no battlemap image exists and one is needed, hand off to
**foundry-battlemap** skill. Report the asset path and pause until the
map is ready.

Done when: battlemap asset is placed at a known path, or skipped.

### Step 3: Generate the scene

Two paths:

**AI-generated map** (no existing battlemap image):

```
tool: generate-map
params: {
  prompt: "<describe the tactical environment from the Zones table>",
  scene_name: "<creative scene name>",
  size: "medium",
  grid_size: 70
}
```

**Existing battlemap** (image placed in Step 2):
Report the asset path to the user. Foundry scene creation from an
existing image requires the Foundry UI — the MCP has no "create scene
from image" tool. Tell the user: "Battlemap placed at `assets/<file>`.
Create a scene in Foundry and set this as the background image."

Done when: scene exists or user has the asset path and instructions.

### Step 4: Stage the roster

For each creature in the encounter's Roster section, run Recipe 1 if the
creature is not already in Foundry. Check first:

```
tool: list-characters
params: { type: "npc" }
```

Done when: every roster creature exists as an actor in Foundry.

### Step 5: Place tokens (optional)

If a scene is active and the user wants token placement:

```
tool: create-actor-from-compendium
params: {
  names: ["Wolfrabbit Alpha", "Wolfrabbit"],
  packId: "<pack>",
  itemId: "<id>",
  quantity: 2,
  addToScene: true,
  placement: { type: "random" }
}
```

Or for actors already in the world (not from compendium), report which
actors need tokens and suggested positions from the Zones table.

Done when: tokens placed, or placement list reported.

## Recipe 3 — Stage an item

Source: vault note with `type: item` frontmatter.

### Step 1: Check

```
tool: manage-world-items
params: { action: "list", type: "<weapon|equipment|consumable|loot|tool>" }
```

Scan for name match. Done when: item status known.

### Step 2: Stage

```
tool: manage-world-items
params: {
  action: "create",
  items: [{
    name: "<from note title>",
    type: "<map vault kind to: weapon, equipment, consumable, loot, tool>",
    system: {
      description: { value: "<note description as HTML>" },
      rarity: "<common|uncommon|rare|very rare|legendary>",
      attunement: "<required or empty string>"
    }
  }],
  folder: "Foundry MCP Items"
}
```

Done when: item created.

### Step 3: Wire to actor (optional)

If the note's `owner` frontmatter names a creature or NPC in Foundry:

```
tool: manage-world-items
params: {
  action: "add-to-actor",
  actorIdentifier: "<owner name>",
  itemNames: ["<item name>"]
}
```

Done when: item attached to owner, or no owner specified.

## Recipe 4 — Stage a journal

Source: vault note without a statblock, for reference material in Foundry.

### Step 1: Build content

Extract the `[!narration]` block as player-visible HTML. Everything
outside narration becomes DM-facing content.

### Step 2: Stage

```
tool: create-quest-journal
params: {
  title: "<note title>",
  content: "<DM-facing content as HTML>",
  folderName: "<Locations|NPCs|Factions|Lore — match note type>",
  additionalPages: [{
    name: "Player View",
    content: "<narration block as HTML>"
  }]
}
```

Done when: journal created with separate DM and player pages.

### Step 3: Link to NPC (optional)

If the journal is a quest with a named NPC:

```
tool: link-quest-to-npc
params: {
  questTitle: "<quest title>",
  npcIdentifier: "<NPC name>"
}
```

## Recipe 5 — Session batch

Source: session-prep note or `hot.md`.

### Step 1: Inventory

Read the session prep. List every entity needed: creatures, items, NPCs,
locations.

### Step 2: Check what exists

```
tool: list-characters
params: {}
```

```
tool: manage-world-items
params: { action: "list" }
```

Diff against inventory. Done when: missing entities listed.

### Step 3: Stage missing entities

Run the matching recipe for each missing entity. Order: creatures first
(other recipes may reference them), then items, then journals, then
scenes.

### Step 4: Report

List what was staged, what already existed, what needs manual attention
(missing statblocks, missing art).

Done when: every entity in the session prep exists in Foundry, gaps
reported.

## Wikilink conversion

When writing Foundry journal HTML, convert `[[Target]]` wikilinks to
`@UUID[JournalEntry.{id}]{Target}` when the target journal exists in
Foundry. When it does not, render as plain bold text.

## Asset conventions

| Vault path | Foundry destination | Foundry reference path |
|---|---|---|
| `attachments/*-token.*` | `foundry-data/assets/tokens/` | `assets/tokens/{file}` |
| `attachments/*-battlemap.*` | `foundry-data/assets/` | `assets/{file}` |
| `attachments/<campaign>/*` | `foundry-data/assets/<campaign>/` | `assets/<campaign>/{file}` |
