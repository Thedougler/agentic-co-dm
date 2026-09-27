---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", spell]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: spell
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
level: ""
school: ""
ritual: false
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Default page is the portrait, the italic level line, the casting fields, and the effect, as the Player's Handbook prints a spell. Campaign facts come after the effect, only when they exist. Delete unused comments and narration slots. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- Technique portrait: what a bystander sees, hears, and feels when it is cast (theatre-of-the-mind). -->

<!-- Level, school, and the classes that can learn it. Match YAML. -->

*Level 2 Evocation (Druid, Wizard)*

**Casting Time.** Action
**Range.** Self (60-foot Line)
**Components.** V, S, M (a pinch of salt)
**Duration.** Concentration, up to 1 minute

<!-- Required. The effect in 2024 rules language: targets, save, damage, conditions, and limits, then **Using a Higher-Level Spell Slot.** when it scales. -->

Each creature in the Line makes a Strength saving throw. On a failed save, a creature is pushed 15 feet away from you.

> [!narration] When cast
> <!-- Optional, when a player character can cast it: the caster's gesture, word, and component as "you", then what the magic does, a few sentences (theatre-of-the-mind: Declared action). -->

<!-- Campaign facts, as **Name.** paragraphs, each only when it exists: **Rulings.** (the tricks players will try, each with its answer), **Learned from.** ([[npc]], [[item]], or [[place]], the price, and the clue that points there). -->
