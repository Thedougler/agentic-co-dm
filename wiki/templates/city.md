---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", place]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: place
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
kind: city
region: ""
status: active
population: ""
government: ""
ruler: ""
controlling_faction: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Default page is the portrait, the italic classification line, and the districts. Keep a section, row, or bullet only when you have facts for it; delete unused sections, bullets, rows, narration slots, and these comments. A district that holds several playable locations gets its own place page. Faction detail lives on faction pages; here, only what they do in this city now. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- City portrait: the arrival or overlook, and the landmark that orients a newcomer (theatre-of-the-mind). -->

<!-- Size, who rules it, and what is unsettling it now. Match YAML. -->

*Port city of 9,000, ruled by [[npc]] for [[faction]], short of grain since the blockade*

## Districts

<!-- Required. Narration cells: a line or two in `_italic_` per district, the first impression as the party walks in (theatre-of-the-mind: Zone cell). -->

| District  | Known for | Trouble now | Narration |
| --------- | --------- | ----------- | --------- |
| [[place]] |           |             | _…_       |

<!-- **Getting around.** travel time across the city, what changes after dark, gates, and shortcuts, only when it changes play. -->

## Services

<!-- Places the party can seek on purpose: gates, inns, shops, fences, healers, information, transport. -->

| Need     | Go to     | District  | Catch |
| -------- | --------- | --------- | ----- |
| Lodging  | [[place]] | [[place]] |       |

## Factions

<!-- What each faction is doing in this city now, and the local rules that differ from what players would assume (law, weapons, magic, curfew). -->

| Faction     | Wants here | Leverage | Next move |
| ----------- | ---------- | -------- | --------- |
| [[faction]] |            |          |           |

## Conflicts

<!-- One `###` per live conflict: who is involved, what the party sees before investigating, what each side wants, and the next concrete change if nobody steps in. -->

### Conflict

## Random Encounters

<!-- Random tables for improvising: encounters that reveal the city, names, and incidental places. Narration cells: one `_italic_` line, the first sign the party perceives (theatre-of-the-mind: Tick cell). -->

| d6 | Encounter | Narration |
| -: | --------- | --------- |
| 1  |           | _…_       |

<!-- **Rumors.** and **Secret.** paragraphs after the tables, each with what is true and how the party learns it, only when they exist. -->

## Log

- **[[Session]]** — what changed, why, and which pages it affected.
