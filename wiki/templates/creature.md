---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", creature]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: creature
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
region: ""
role: ""
cr: ""
summary: ""
token: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Default page is the portrait, then the italic habitat line, then the statblock. Campaign facts come after the statblock, only when they exist. Delete unused comments and narration slots. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- Creature portrait: one third-person paragraph, true every time it is met, with a visible tell for each signature ability (theatre-of-the-mind). -->

<!-- Habitat and treasure, as the Monster Manual prints them. Match YAML. -->

*Habitat: Forest, Swamp; Treasure: Relics*

## Statblock

<!-- Required. The full 2024 statblock: every rule the creature runs on lives here. -->
```statblock
layout: Basic 5e Layout
name: "{{title}}"
size: Medium
type: monstrosity
alignment: unaligned
ac: 13
hp: 11
hit_dice: "2d8 + 2"
speed: "30 ft."
stats: [10, 10, 10, 10, 10, 10]
senses: "passive Perception 10"
languages: "—"
cr: "1/4"
traits:
  - name: "Trait Name"
    desc: "What it does, in 2024 rules language."
actions:
  - name: "Bite"
    desc: "*Melee Attack Roll:* +2, reach 5 ft. *Hit:* 4 (1d6 + 1) Piercing damage."
```

<!-- Only what the statblock does not already say, as **Name.** paragraphs, each only when it exists: **Tactics.** (opening move, what it does when countered, what shuts it down, when it flees), **Tracks and signs.** (tracks, spoor, and the trace it leaves before anyone sees it), **Secret.** (a hidden truth and how the party learns it), **Connections.** ([[page]] and what the tie does at the table). -->

**Tactics.** It opens from cover on the nearest lone target and flees at half its hit points.

> [!narration] In action
> <!-- Optional: the creature mid-fight, "you" address, each signature ability as it lands (theatre-of-the-mind: Creature in scene). -->
