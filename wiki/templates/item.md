---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", item]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: item
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
kind: consumable
rarity: ""
region: ""
attunement: false
owner: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Default page is the portrait, then italic classification, then what it does. Extra campaign facts only after the rules, only when they exist. Lore about the world goes on a lore page. Delete unused comments. kind: consumable | magic | plot | durable. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- Item portrait: the object as seen, true every time (theatre-of-the-mind). -->

<!-- Classification: type, rarity, attunement, cost, weight. Match YAML. Weapon or armor: damage or AC on the next line (`1d8` slashing; AC +2). -->

*Potion, rare, ½ lb.*

<!-- What it does. 2024 rules: trigger, action, uses, range, targets, save, damage, duration, limits. One to three sentences. Further properties as **Name.** paragraphs after that block, still before any lore. -->

When you drink this potion, your Strength score changes to 23 for 1 hour. The potion has no effect on you if your Strength is equal to or greater than that score.
