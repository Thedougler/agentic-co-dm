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
kind: flora hazard
region: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Default page is the portrait, the italic classification line, and the Trigger, Effect, and Countermeasures lines, as the Dungeon Master's Guide prints a hazard. Delete unused comments and narration slots. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- Hazard portrait: what a careful traveler sees before touching it, with a warning sense beyond sight (theatre-of-the-mind). -->

<!-- Kind and where it grows. Match YAML. -->

*Flora hazard, found in [[place]]*

<!-- Required. The rules, each line with its ruling. -->

**Trigger.** A creature enters the stand or touches a blade.
**Effect.** The creature makes a **Dexterity** saving throw — `DC 13`, taking `2d6` slashing damage on a failure or half as much on a success.
**Countermeasures.** **Wisdom (Perception)** — `DC 13` spots the fixed glints; a creature that moves at half speed takes no damage.

> [!narration] On contact
> <!-- Optional: what the character feels and the others see when it hits, "you" address (theatre-of-the-mind: On contact). -->

<!-- **Secret.** a delayed or hidden effect and how the party learns it, only when it exists. -->
