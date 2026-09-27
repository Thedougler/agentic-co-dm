---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", vehicle]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: vehicle
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
kind: vessel
region: ""
berth: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Default page is the portrait, the italic classification line, and the statblock. Campaign facts come after the statblock, only when they exist. Numbers live in Statblock only. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- Vehicle portrait: the craft at its berth, how people get aboard, and the features a character can use (theatre-of-the-mind). -->

<!-- Size, type, captain, and berth. Match YAML. -->

*Gargantuan sailing ship (80 ft. by 20 ft.), captained by [[npc]], berthed at [[place]]*

## Statblock

<!-- Required. Every number the craft needs. -->

- **Speed.** 4 mph sailing
- **Crew.** 20 minimum; 12 passengers; 100 tons cargo
- **Hull.** AC 15, HP 300, damage threshold 15
- **Helm.** AC 18, HP 50
- **Movement.** Sails: AC 12, HP 100; speed drops 5 feet for every 25 damage.
- **Weapons.** Ballista (crew 3): `+6` to hit, range 120/480 ft., `3d10` piercing damage.

<!-- Campaign facts, as **Name.** paragraphs, each only when it exists: **Current voyage.** (what it is doing this week and its next stop with a time), **Crew.** (stations and who holds them now; each fighter embedded once, `![[owner#Statblock]]`), **Decks.** (each area at body scale with one usable feature), **Handling.** (chase, ramming, boarding, and what happens when it sinks), **Secret.** (hidden cargo, a false flag, or who hunts it, and how the party learns it). -->

> [!narration] Underway
> <!-- Optional: the craft in motion from its deck, "you" address (theatre-of-the-mind: Vehicle). -->
