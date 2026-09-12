---
type: pc-stats
status: canon
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
owner_skill: ".claude/skills/combat-profiles/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
tags: []
pc: "{pc-slug}"
pc_level:               # total character level — must match [[<pc-slug>]]'s own `level:`
last_synced: ""         # date this page was last reconciled against the character sheet
uid: a6dff6ef-0cee-4703-8495-e0154df6901d
---

# <Name> — Attributes

Mechanical attributes for [[<pc-slug>]], transcribed from
`_assets/character-sheets/<pc-slug>-character-sheet.pdf`. A value the sheet
states wrongly is transcribed as printed and tagged `[verify]`, never
silently corrected. This page is the single source of truth for every
per-ability, per-skill, and per-speed value; `ac`, `hp_max`,
`class_levels`, and `level` stay in [[<pc-slug>]]'s frontmatter and are
never restated here.

## Ability Scores & Saves

| Ability | Score | Mod | Save | Proficient? |
|---|---|---|---|---|
| Strength |  |  |  |  |
| Dexterity |  |  |  |  |
| Constitution |  |  |  |  |
| Intelligence |  |  |  |  |
| Wisdom |  |  |  |  |
| Charisma |  |  |  |  |

Item bonuses fold into the Save column, with the item named in a line
under the table — a Cloak of Protection's +1 belongs in the number and in
the prose, so the source of the bonus stays traceable.

## Skills

Group by proficiency level — expertise, full proficiency, half proficiency,
untrained-but-notable — and give passive Perception, Insight, and
Investigation their own line.

## Combat Stats

| Stat | Value | Source |
|---|---|---|
| Initiative |  |  |
| Speed |  |  |
| Hit dice |  |  |
| Proficiency bonus |  |  |
| Damage resistances |  |  |
| Condition advantages |  |  |

AC and max HP live in [[<pc-slug>]]'s frontmatter (`ac:`, `hp_max:`) — the
roster `.base` views query them there; this table carries no rows for
them.

## Proficiencies & Languages

Armour, weapons, tools, and languages. A species trait that grants one is
named here and detailed on [[<pc-slug>-abilities]], not described twice.
