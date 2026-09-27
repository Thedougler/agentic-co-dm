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
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section, row, or bullet only when you have facts for it; delete unused sections, bullets, rows, narration slots, and these comments. A site that needs its own key gets its own place page. `region` is the parent region.
scale: macro | regional | local. kind examples: realm, frontier, wilderness, forest, mountains, archipelago, sea. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

## At a Glance

<!-- Required. Lead sentence: the kind of adventure and choices this region creates. Then labelled facts, one bullet each. -->

- **Now.** What is normal here, and what just changed.
- **Pressure.** What is getting worse, and what people will notice next.
- **Known for.** What travelers expect.
- **Anchor.** [[place]]

> [!narration] {{title}}
> <!-- One third-person paragraph as a traveler first meets it: horizon, terrain, weather, footing, sound, the one feature that sets it apart from its neighbors (theatre-of-the-mind: Region portrait). -->

## Geography

<!-- The shape of the land: boundaries and neighbors, landmarks a traveler steers by, and subregions with their own character. -->

- **[[region]].** A neighbor or subregion, and what changes across the border.
- **[[place]].** A landmark, and its role in travel.

## Travel

<!-- Only what changes a travel choice. Give alternate routes genuinely different tradeoffs. -->

| Route    | Connects              | Time | Risk | Advantage |
| -------- | --------------------- | ---- | ---- | --------- |
| [[page]] | [[place]] ↔ [[place]] |      |      |           |

- **Navigation.** What makes staying on course easy or hard.
- **Weather.** What routinely alters travel, and when.
- **Rest and supply.** Where travelers recover or resupply, and what it costs.
- **Hidden route.** [[place]] ↔ [[place]] — a secret, seasonal, or broken connection and what opens it.
- **Regional rule.** One unusual rule that matters at the table.

> [!narration] On the road
> <!-- Optional: a stretch of travel here, "you" address, a short paragraph ending at camp, arrival, or the thing on the road (theatre-of-the-mind: Travel). -->

## Key Places

- [[place]] — what it offers or threatens now, and how the party learns it exists.

## Powers

<!-- The few factions and forces able to change this region now, including any threat that advances when ignored. -->

- [[faction]] — what it wants here, its next move, and the sign of that move.

<!-- A threat that advances when ignored (war, plague, storm, curse) gets its steps, each with what the party sees. -->

- **Threat.** What drives it and what becomes true if it succeeds.
- [ ] **First sign.** The first visible change.
- [ ] **Escalation.** A change that closes options.
- [ ] **Crisis.** The point where it cannot be ignored.

## Rumors

<!-- A d6 table only when you have six rumors; otherwise a list. Each rumor gives the party something to chase. -->

| d6 | Rumor | Truth | Points to |
| -: | ----- | ----- | --------- |
| 1  |       |       | [[page]]  |

## Encounters

<!-- A d6 table of encounters drawn from creatures and factions on this page, each with its warning sign spoken in the Narration cell: one `_italic_` line (theatre-of-the-mind: Tick cell). -->

| d6 | Encounter | Narration |
| -: | --------- | --------- |
| 1  | [[creature]] | _…_    |

## Secrets

<!-- Hidden routes, buried truths, and discoveries, each with how the party can find it. -->

## Connections

- [[region]] — the neighbor and what changes across the border.

## History

<!-- Past events that still leave something usable in the present. -->

## Log

- **[[Session]]** — what changed here and why.

