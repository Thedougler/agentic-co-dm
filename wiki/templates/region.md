---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", region]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: region
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
scale: regional
kind: wilderness
region: ""
structure: ""
as_of: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Default page is the portrait, the italic classification line, and how the party crosses it. Keep a section, row, or bullet only when you have facts for it; delete unused sections, bullets, rows, narration slots, and these comments. A site that needs its own key gets its own place page. `region` is the parent region.
scale: macro | regional | local. kind examples: realm, frontier, wilderness, forest, mountains, archipelago, sea. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- Region portrait: the land as a traveler first meets it, and the one feature that sets it apart from its neighbors (theatre-of-the-mind). -->

<!-- Kind of land, its parent region, and what is changing in it now. Match YAML. -->

*Wild jungle island in [[region]], where the fruit trees are dying back from the coast*

## Travel

<!-- Required. Only what changes a travel choice; alternate routes carry genuinely different tradeoffs. -->

| Route    | Connects              | Time | Risk | Advantage |
| -------- | --------------------- | ---- | ---- | --------- |
| [[page]] | [[place]] ↔ [[place]] |      |      |           |

<!-- Travel rules, as **Name.** lines, each only when it changes play: **Navigation.**, **Weather.**, **Rest and supply.**, **Hidden route.**, **Regional rule.** -->

> [!narration] On the road
> <!-- Optional: a stretch of travel here, "you" address, ending at camp, arrival, or the thing on the road (theatre-of-the-mind: Travel). -->

## Places

- [[place]] — what it offers or threatens now, and how the party learns it exists.

## Factions and Threats

<!-- The few factions and forces able to change this region now. A threat that advances when ignored gets its steps, each with what the party sees. -->

- [[faction]] — what it wants here, its next move, and the sign of that move.

## Random Encounters

<!-- A d6 table drawn from creatures and factions on this page, each fighter linked to its page. Narration cells: one `_italic_` line, the warning sign (theatre-of-the-mind: Tick cell). -->

| d6 | Encounter | Narration |
| -: | --------- | --------- |
| 1  | [[creature]] | _…_    |

## Rumors

<!-- A d6 table only when you have six rumors; otherwise a list. Each rumor gives the party something to chase. -->

| d6 | Rumor | Truth | Points to |
| -: | ----- | ----- | --------- |
| 1  |       |       | [[page]]  |

<!-- **Secret.** paragraphs after the tables, each with how the party can find it, only when they exist. -->

## Log

- **[[Session]]** — what changed here and why.
