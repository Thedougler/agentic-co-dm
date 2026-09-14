# Contract: PC Owner Page

This is the agent-facing Markdown contract for `type: pc` owner pages. The canonical scaffold is `wiki/templates/pc.md`; `wiki/AGENTS.md` owns campaign fields and approval rules, while `obsidian-markdown` owns syntax.

## Destination and identity

- Live owner: `wiki/entities/pc/<kebab-slug>.md`.
- Copy-start scaffold: `wiki/templates/pc.md`.
- Required core frontmatter: `title`, `category`, `tags`, `sources`, `created`, `updated`.
- Required campaign frontmatter: `type: pc`, `lifecycle`, `reveal`, `campaign`, `visibility`, and `summary`.
- PC identity: `player`, `class_levels`, `level`, `ac`, `hp_max`, `init_mod`, `pp`, `speed`, and existing `status` when known.
- Preserve optional aliases, Foundry identity, provenance/confidence, tier, lifecycle dates, source list, and existing campaign state.
- Unknown source values remain unknown or `[verify]`; agents do not invent values or silently resolve conflicts.

## Semantic spine

```text
# {{title}}
> [!narration] Narration
## At a Glance
## Connections                 (omit only with no named ties)
## Sheet
## Combat Profile              (omit only when no useful profile exists)
## Abilities
### Traits                     (omit when empty)
### Features                   (omit when empty)
### Actions                    (omit when empty)
### Bonus Actions              (omit when empty)
### Reactions                  (omit when empty)
### Feats                      (omit when empty)
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
## Session Log                  (omit for a new PC with no session changes)
## Art                          (omit when no approved art exists)
```

The heading order is semantic. There is no `## Voice` section: the PC is player-controlled, and the DM page does not prescribe voice performance. Existing Voice facts are either moved into an existing decision-relevant home or left attributable in source evidence.

## Column syntax

Use exactly the supported nested fenced syntax for the two pairs below:

- Identity pair: `At a Glance` + `Connections`.
- Mechanical pair: `Sheet` + `Combat Profile`.

The parent `col` fence has more backticks than child `col-md` fences. Put each heading inside its child fence. Keep the leading narration callout outside all fences. Do not use `[!col]` for these PC pairs. Do not put callouts inside Markdown table cells. When a viewer cannot render columns, the headings and tables must read top-to-bottom without relying on visual placement.

## Section contracts

### At a Glance

Provide player handle, class/level, home ship or equivalent base, and one concise DM thesis about play pattern, party role, pressure, or decision-relevant weakness. Do not give the player a choice or write a voice-performance instruction.

### Connections

Use named Obsidian links. Each entry states what the tie changes at the table. Escape alias pipes as `\|` inside table cells. Do not duplicate the linked owner's full content.

### Sheet

This is the readable numerical authority. Include ability score/modifier/save rows, known skill bonuses/proficiencies, and a combat skim for AC, current/max HP, initiative, passive perception, speed, and character-specific resources/counters when known. Current and maximum HP are distinct. Frontmatter mirrors only the defined machine-reference values.

### Combat Profile

Use `Fast Read` and `Counters & Synergy` when they improve adjudication. Explain how the PC operates, what shuts them down, what pressures them, and what party conditions change a ruling. Point to the Sheet or Abilities for exact numbers instead of repeating them.

### Abilities

Each populated subsection uses a table whose entries state effect, uses, and recovery when applicable. Keep traits, features, actions, bonus actions, reactions, and feats distinct. A mechanical constraint moved from old voice-script material belongs here.

### Spells

Include only when the PC can cast or has another castable resource, including a minimal racial/spell-like resource when applicable. Keep multiclass pools distinct. Separate casting ability/calculations, cantrips, prepared/known spells, and slots or casting resources. Link spell owners when available.

### Inventory

Separate attuned, carried, stowed, and currency rows when present. Link item owners; retain only the quantity, state, and table consequence needed on the PC page.

### Session Log and Art

Session Log contains concise session-numbered or dated changes affecting current play. Art contains only existing approved embeds using repository attachment names and paths. Long-form historical source material stays attributable in `sources` or archive evidence.

## Safety and preservation

- Narration is a real `[!narration]` callout containing only player-safe sensory description. No secrets, DCs, unearned names, or DM thesis.
- Use complete-sentence DM-facing prose, Title Case headings, inline-code DCs/dice, and real newlines.
- Preserve all existing links, aliases, art references, source entries, player handles, lifecycle, reveal, visibility, and campaign meaning during structure-only conformance.
- For source conflicts, keep the current owner fact plus an explicit `[verify]` marker naming the disagreement. Do not choose an invented value.
- Flatten archive/satellite facts into the canonical home or a named owner link. Do not leave a competing live facet dump.
