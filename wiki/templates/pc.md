---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", pc]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: pc
lifecycle: proposed
reveal: revealed
campaign: "{{campaign}}"
visibility: dm
status: alive
player: ""
class_levels: ""
level:
ac:
hp_max:
init_mod:
pp:
speed: ""
summary: ""
---
<!-- Copy-start scaffold for type: pc.

     Jobs (distinct from Person/npc): spoken look; orientation + play-pattern thesis;
     named party/ship/faction ties; sheet + combat scan; abilities; spells (casters);
     inventory; short session deltas; voice; art. No First meeting / posture change required.
     Sheet + scan first — PC is not an NPC-with-tag.

     INGEST (blocking remediation): Flatten satellite dumps (abilities / sheet / spells /
     inventory / combat-profile / gallery / stats / session-combat-log) into the H2s below.
     FORBID additional H1s — never nest `# {{title}} — Facet` or `# PlayerName` dumps.
     Numbers live on this owner page. Other pages wikilink; they do not copy the sheet.
     Omit empty sections. One Markdown treatment = one meaning (at-table scan).
     Placeholders only — no invented lore.

-->

# {{title}}

> [!narration] Narration
> <!-- Load `.agents/skills/theatre-of-the-mind` → mode: standalone cold portrait → subject: person. -->
> Write a standalone cold portrait in flowing prose — as long as the character requires to be recognized at a table. Cover face, body, clothing, posture, and at least one non-sight detail (voice, gait, smell, habit). The portrait gives a player a picture they can sketch and distinguish from other PCs. Player-safe. No secrets, DCs, unearned names, or DM thesis.

## At a Glance

| **Role**         | PC |
| ---------------- | -- |
| **Class / Level** | {{class_levels}} (level {{level}}) |
| **Player**       |  |
| **Home vessel**   | [[vehicle]] |

> **DM thesis.** Write one sentence on how this PC plays at the table. Describe the lane, pressure, and party role. Do not describe NPC wants.

## Connections

- [[party member]]. State what this tie does at the table.
- [[vehicle]]. State the berth or station.
- [[faction]]. State the obligation or lean that changes a ruling.

<!-- Shared heading Connections — NOT `# Relationships`. Omit when unused. -->

## Sheet

<!-- Compact numbers for mid-round skim. Prefer this table; optional ```statblock``` below only when a combatant block helps — omit-empty. -->

| Ability | Score | Mod | Save |
| ------- | ----- | --- | ---- |
| STR     |       |     |      |
| DEX     |       |     |      |
| CON     |       |     |      |
| INT     |       |     |      |
| WIS     |       |     |      |
| CHA     |       |     |      |

**Skills.** List proficient / expertise skills with bonuses, or point that full skill lines live in this section.

| Combat skim | Value |
| ----------- | ----- |
| AC          |       |
| HP max      |       |
| Init        |       |
| PP          |       |
| Speed       |       |

<!-- Optional combatant block — omit when the table above is enough.
```statblock
layout: Basic 5e Layout
name: "{{title}}"
size: Medium
type: humanoid
ac: ""
hp: 1
speed: "30 ft."
stats: [10, 10, 10, 10, 10, 10]
```
-->

## Combat Profile

<!-- At-table combat scan. Omit entire ## Combat Profile when unused. -->

### Fast Read

Write one line covering the lane, key numbers, Achilles heel, and toughest matchup when known.

### Counters and Support

- **Hard counters.** What shuts them down.
- **Soft counters.** What pressures them.
- **Amplifies / Depends on.** Party support that changes a ruling.

## Abilities

<!-- Subsections as ### only. Never nest another `# {{title}} — Abilities`. No "What lives here and what does not" meta. -->

### Traits

| Trait | Effect |
| ----- | ------ |
|       |        |

### Features

| Feature | Source | Effect | Uses | Recovery |
| ------- | ------ | ------ | ---- | -------- |
|         |        |        |      |          |

### Actions

| Action | To-Hit / DC | Damage / Effect | Uses | Notes |
| ------ | ----------- | --------------- | ---- | ----- |
|        |             |                 |      |       |

### Bonus Actions

| Bonus Action | Trigger / Cost | Effect | Uses | Recovery |
| ------------ | -------------- | ------ | ---- | -------- |
|              |                |        |      |          |

### Reactions

| Reaction | Trigger | Effect | Uses | Recovery |
| -------- | ------- | ------ | ---- | -------- |
|          |         |        |      |          |

### Feats

| Feat | Source | Effect |
| ---- | ------ | ------ |
|      |        |        |

<!-- Omit any empty ### subsection. -->

## Spells

<!-- Omit entire ## Spells if non-caster. Never nest `# {{title}} — Spells`. -->

### Spellcasting

Ability, save DC, attack bonus, ritual notes, focus.

### Cantrips

| Cantrip | Notes |
| ------- | ----- |
| [[spell]] |       |

### Prepared

| Spell | Level | Notes |
| ----- | ----- | ----- |
| [[spell]] |     |       |

### Slots

| Level | Slots |
| ----- | ----- |
| 1st   |       |
| 2nd   |       |

## Inventory

<!-- Wikilink item owner pages. Never nest `# {{title}} — Inventory`. -->

### Attuned

| Item | Notes |
| ---- | ----- |
| [[item]] |    |

### Carried

| Item | Qty | Notes |
| ---- | --- | ----- |
| [[item]] |  |      |

### Stowed

| Item | Where | Notes |
| ---- | ----- | ----- |
| [[item]] |    |       |

### Currency

| Coin | Amount |
| ---- | ------ |
| gp   |        |

<!-- Omit any empty ### subsection. -->

## Session Log

<!-- Short combat/session deltas only. Replaces nested Session Combat Log dumps. Omit when unused. -->

| Session | Encounter | Note |
| ------- | --------- | ---- |
|         |           |      |

## Voice

<!-- Player voice notes for the DM. Omit when unused. -->

## Art

<!-- Art embeds: wiki/attachments/{subject-slug}-{role}.ext — roles: banner|portrait|token|battlemap|overview|reference|handout|teaser. Flat folder; omit Art when unused. -->
