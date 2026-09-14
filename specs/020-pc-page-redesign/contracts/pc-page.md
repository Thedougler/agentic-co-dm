# Contract: PC Owner Page

This is the agent-facing Markdown contract for `type: pc` owner pages. The canonical scaffold is `wiki/templates/pc.md`. `wiki/AGENTS.md` owns campaign fields, approval, and wiki-kind routing. `obsidian-markdown` owns syntax. `.agents/skills/player-characters/SKILL.md` is the sole skill owner for recording these pages.

## Destination and identity

- Live owner: `wiki/entities/pc/<kebab-slug>.md`.
- Copy-start scaffold: `wiki/templates/pc.md`.
- Required core frontmatter: `title`, `category`, `tags`, `sources`, `created`, `updated`.
- Required campaign frontmatter: `type: pc`, `lifecycle`, `reveal`, `campaign`, `visibility`, and `summary`.
- PC identity: `player`, `class_levels`, `level`, `ac`, `hp_max`, `init_mod`, `pp`, `speed`, and existing `status` when known.
- Preserve optional aliases, Foundry identity, provenance/confidence, tier, lifecycle dates, source list, and existing campaign state.
- Unknown source values remain unknown or `[verify]`. Agents do not invent values.

## Semantic spine

```text
# {{title}}
> [!narration] Narration
## Identity
## Combat Stats
## Ability Scores
## Skills
## Actions
### Attacks                    (omit when empty)
### Actions                    (omit when empty)
### Bonus Actions              (omit when empty)
### Reactions                  (omit when empty)
## Spells                      (casters or other castable resources only)
### Spellcasting               (omit when no calculations apply)
### Cantrips                   (omit when empty)
### Prepared or Known          (omit when empty)
### Slots or Casting Resources (omit when empty)
## Inventory
### Attuned                    (omit when empty)
### Carried                    (omit when empty)
### Stowed                     (omit when empty)
### Currency                   (omit when empty)
## Features
### Traits                     (omit when empty)
### Class Features             (omit when empty)
### Feats                      (omit when empty)
## Connections                 (omit only with no named ties)
## Session Log                 (omit for a new PC with no session changes)
## Art                         (omit when no approved art exists)
```

The heading order is semantic and follows D&D Beyond information groups. There is no `## Voice`, `## At a Glance`, `## Sheet`, `## Combat Profile`, or `## Abilities`. The PC is player-controlled. The page records options and numbers; it does not prescribe actions, voice, or play pattern.

## Column syntax

Use exactly the supported nested fenced syntax for these pairs:

- Header pair: `Identity` + `Combat Stats`.
- Ability pair: `Ability Scores` + `Skills`.

The parent `col` fence has more backticks than child `col-md` fences. Put each heading inside its child fence. Keep the leading narration callout outside all fences. Do not use `[!col]` for these PC pairs. Do not put callouts inside Markdown table cells. When a viewer cannot render columns, the headings and tables must read top-to-bottom without relying on visual placement. Do not recreate D&D Beyond cards, site colors, or non-Markdown chrome.

`Connections` and `Session Log` MAY use the same column pattern when both exist.

## Section contracts

### Identity

Provide player handle, class/level, and other D&D Beyond identity facts when known (species/race, background). Home ship or equivalent base, when known, appears here or in Connections and MUST NOT be dropped. Do not require a DM thesis or prescribed play pattern.

### Combat Stats

Readable combat-bar authority: AC, current/max HP, initiative, passive perception, speed, and character-specific resources when known. Current and maximum HP are distinct. Frontmatter mirrors only the defined machine-reference values.

### Ability Scores

Ability score, modifier, and save rows for Strength through Charisma.

### Skills

Known skill bonuses and proficiencies. Do not duplicate Combat Stats numbers as a second authority.

### Actions

Attacks, actions, bonus actions, and reactions as listed options. Each populated row states effect and uses or recovery when applicable. Do not write what the player will do.

### Spells

Include only when the PC can cast or has another castable resource. Keep multiclass pools distinct. Separate casting ability/calculations, cantrips, prepared/known spells, and slots or casting resources. Link spell owners when available.

### Inventory

Separate attuned, carried, stowed, and currency rows when present. Link item owners; retain only the quantity, state, and table consequence needed on the PC page.

### Features

Traits, class features, and feats. Each populated row states effect and uses or recovery when applicable.

### Connections, Session Log, and Art

Connections use named Obsidian links. Each entry states what the tie changes at the table. Escape alias pipes as `\|` inside table cells. Do not duplicate the linked owner's full content. Session Log contains concise session-numbered or dated changes affecting current play. Art contains only existing approved embeds using repository attachment names and paths.

## Skill and ingest

- Agents MUST use `player-characters` for `type: pc` wiki work. They MUST NOT use `npc-design` to create, rewrite, or prescribe a PC page.
- The skill transcribes supplied source: PDF character sheet, prose description, Foundry VTT actor via the existing MCP server, or another DM-supplied file.
- The skill MAY file a new `type: pc` page for a character the player already made. It MUST refuse work that invents a PC, generates stats, or writes the character's actions.
- When a newer supplied source disagrees with the live wiki page on the same number, keep the newer source's value and overwrite the wiki number (and matching frontmatter mirror). Structure-only conformance is not a newer source.
- One source that internally conflicts with itself keeps the disagreement or `[verify]`; do not invent a resolution.
- If a PDF cannot be read, Foundry MCP is unavailable, or another source fails: record what can be read; mark unread fields unknown or `[verify]`.

## Safety and preservation

- Narration is a real `[!narration]` callout containing only player-safe sensory description. No secrets, DCs, unearned names, or DM thesis.
- Use complete-sentence DM-facing prose, Title Case headings, inline-code DCs/dice, and real newlines.
- Preserve all existing links, aliases, art references, source entries, player handles, lifecycle, reveal, visibility, and campaign meaning during structure-only conformance.
- Flatten archive/satellite facts into the canonical home or a named owner link. Do not leave a competing live facet dump.
