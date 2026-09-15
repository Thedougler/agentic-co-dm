# Contract: PC Owner Page

This is the agent-facing Markdown contract for `type: pc` owner pages. The canonical scaffold is `wiki/templates/pc.md`. `wiki/AGENTS.md` owns campaign fields, approval, and wiki-kind routing. `obsidian-markdown` owns syntax. `.agents/skills/player-characters/SKILL.md` is the sole skill owner for recording these pages.

## Destination and identity

- Live owner: `wiki/entities/pc/<kebab-slug>.md`.
- Copy-start scaffold: `wiki/templates/pc.md`.
- Required core frontmatter: `title`, `category`, `tags`, `sources`, `created`, `updated`.
- Required campaign frontmatter: `type: pc`, `lifecycle`, `reveal`, `campaign`, `visibility`, and `summary`.
- PC identity: `player`, `class_levels`, `level`, `ac`, `hp_max`, `init_mod`, `pp`, `speed`, and existing `status` when known.
- Preserve optional aliases, Foundry identity, provenance/confidence, tier, lifecycle dates, source list, and existing campaign state.
- Live PC pages include `cssclasses` containing `pc-sheet`.
- Unknown source values are omitted, not invented. Do not write `[verify]` or a user question onto the live page.

## Semantic spine

```text
# {{title}}
> [!narration] Narration
[featured portrait | ## Identity]   (pair only when art exists; else ## Identity full-width)
## Combat Stats                     (full-width)
[## Ability Scores | ## Skills | ## Actions / ## Spells / ## Inventory / ## Features]
### Attacks                    (omit when empty)
### Actions                    (omit when empty)
### Bonus Actions              (omit when empty)
### Reactions                  (omit when empty)
## Spells                      (always present; state none when the PC has no spells)
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
## Connections                 (omit when no named ties)
## Stated Goals                (omit when no transcript-supported player-stated goal)
## Session Log                 (omit for a new PC with no session changes)
## Art                         (omit when no leftover pictures remain)
```

The heading order is semantic and follows D&D Beyond information groups. Identity through Features, including Spells, MUST appear on every filed page. There is no `## Voice`, `## At a Glance`, `## Sheet`, `## Combat Profile`, or `## Abilities`. The PC is player-controlled. The page records options and numbers; it does not prescribe actions, voice, or play pattern. The featured portrait is an embed, not an H2.

## Column syntax

Use nested fenced `col` / `col-md` for these rows. Parent fence has more backticks than child fences. Put each heading inside its child fence. Keep the leading narration callout outside all fences. Do not use `[!col]` for these PC rows. Do not put callouts inside Markdown table cells. When a viewer cannot render columns, the headings and tables must read top-to-bottom without relying on visual placement. Do not recreate D&D Beyond cards, site colors, or non-Markdown chrome.

1. **Header pair** (when art exists): featured portrait embed + `Identity`. Left `col-md` contains only the portrait embed. Right `col-md` contains `## Identity`. When no pictures exist, `Identity` is full-width with no empty portrait column.
2. **Combat Stats:** full-width immediately after Identity. Not inside a column fence.
3. **Sheet row:** three `col-md` children — `## Ability Scores` | `## Skills` | `## Actions`, `## Spells`, `## Inventory`, and `## Features` stacked in that order.

Campaign extras stay full-width after the sheet. Do not pair `Identity` with `Combat Stats`. Do not pair `Connections` with `Session Log`. Column widths are CSS (`pc-sheet.css`), not markdown `flexGrow`, unless CSS cannot set them.

## Section contracts

### Identity

Provide player handle, class/level, and other D&D Beyond identity facts when known (species/race, background). Home ship or equivalent base, when known, appears here or in Connections and MUST NOT be dropped. Do not require a DM thesis or prescribed play pattern. When at least one picture of the character exists, pair one featured portrait with this section as specified under Column syntax.

### Combat Stats

Readable combat-bar authority: AC, current/max HP, initiative, passive perception, speed, and character-specific resources when known. Current and maximum HP are distinct. Frontmatter mirrors only the defined machine-reference values.

### Ability Scores

Ability score, modifier, and save rows for Strength through Charisma. Saves live here so each ability's save is one glance. Do not add a second Saves heading.

### Skills

Known skill bonuses and proficiencies. This is the middle column of the sheet row (spec: "Skills and saves"). Do not duplicate Combat Stats or Ability Scores numbers as a second authority.

### Actions

Attacks, actions, bonus actions, and reactions as listed options. Each populated row states effect and uses or recovery when applicable. Do not write what the player will do. Omit empty subsections. If the section has no rows, state none rather than a placeholder table.

### Spells

Always include this heading. Keep multiclass pools distinct. Separate casting ability/calculations, cantrips, prepared/known spells, and slots or casting resources. Link spell owners when available. A character with no spell access still has `## Spells` and MUST state that they have no spells. Omit empty subsections.

### Inventory

Separate attuned, carried, stowed, and currency rows when present. Link item owners; retain only the quantity, state, and table consequence needed on the PC page. Omit empty subsections. If there are no items, state none rather than a placeholder table.

### Features

Traits, class features, and feats. Each populated row states effect and uses or recovery when applicable. Omit empty subsections.

### Connections, Stated Goals, Session Log, and Art

Connections use named Obsidian links. Each entry states what the tie changes at the table. Escape alias pipes as `\|` inside table cells. Do not duplicate the linked owner's full content. Omit when there are no named ties.

Stated Goals lists only goals the player clearly stated in a game-session transcript, in character or out of character. Cite the session. A session summary MAY help locate or paraphrase a transcript-supported goal and MUST NOT be the sole source. Omit the section when none exist. Do not infer from play, connections, or DM thesis. After every session that included that player, refresh from that session's transcript: add newly stated goals; remove a goal only if the player said it is done or abandoned. Sessions that did not include the player do not refresh this section. Session planning that includes the player MUST read this section when present.

Session Log contains concise session-numbered or dated changes affecting current play.

Art contains leftover approved embeds after the featured portrait and any in-section pictures, using repository attachment names and paths. Omit when none remain. Additional pictures MAY appear next to the section they illustrate. One picture only is the featured portrait; then omit Art. Blank embeds are omitted. Every image wikilink or embed MUST resolve to an existing vault file.

Preserve existing DM-only `[!secret]` callouts. They are not a spine heading. Do not put them in narration.

## Skill and ingest

- Agents MUST use `player-characters` for `type: pc` wiki work. They MUST NOT use `npc-design` to create, rewrite, or prescribe a PC page.
- The skill transcribes supplied source: PDF character sheet, prose description, Foundry VTT actor via the existing MCP server, or another DM-supplied file.
- The skill MAY file a new `type: pc` page for a character the player already made. It MUST refuse work that invents a PC, generates stats, or writes the character's actions.
- When a newer supplied source disagrees with the live wiki page on the same number, keep the newer source's value and overwrite the wiki number (and matching frontmatter mirror) in place. Structure-only conformance is not a newer source.
- One source that internally conflicts with itself: omit the contested number from the live page and file a GitHub issue. Do not invent a resolution. Do not write `[verify]`.
- If a PDF cannot be read, Foundry MCP is unavailable, or another source fails: record what can be read; omit unread numbers. Do not invent replacements. Do not abort a usable partial page when some source remains.
- After a session that included the player, refresh Stated Goals from that session's transcript as specified above. Do not invent goals.

## Safety and preservation

- Narration is a real `[!narration]` callout containing only player-safe sensory description. No secrets, DCs, unearned names, or DM thesis.
- Use complete-sentence DM-facing prose, Title Case headings, inline-code DCs/dice, and real newlines.
- Preserve all existing links, aliases, art references, source entries, player handles, lifecycle, reveal, visibility, and campaign meaning during structure-only conformance.
- Flatten archive/satellite facts into the canonical home or a named owner link. Do not leave a competing live facet dump.
- Live PC pages include `cssclasses: [pc-sheet]`. Vault-wide CSS stays in `ttrpg-styles.css` and `wide-note-surface.css`. PC-only scan tweaks live in `pc-sheet.css` and MUST NOT add a decorative theme, cards, or D&D Beyond chrome.
- Live pages and the template MUST NOT contain `[verify]`, user questions, or superseded numbers beside current ones.
