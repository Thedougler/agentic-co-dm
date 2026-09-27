---
title: "{{title}}"
category: campaign
tags: ["{{campaign}}", quest]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: quest
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
status: offered
scope: local
region: ""
quest_giver: ""
factions: []
deadline: ""
last_advanced: YYYY-MM-DD
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Track the situation as it is now, not a plotted sequence. Default page is the portrait, the italic offer line, and the situation. Other facts only when they exist; delete unused comments and narration slots.
status: rumored | offered | active | stalled | resolved | failed | expired. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- What the characters know: the request, rumor, or visible problem as the party meets it (theatre-of-the-mind: Dialogue, or Handout when it is posted). -->

<!-- Who offers it, the reward, and the deadline. Match YAML. -->

*Offered by [[npc]] for 200 gp, before the spring tide*

<!-- Required. -->

**The truth.** What is really happening, and what each force involved is already doing.

**If the party walks away.** What happens without them, as the visible steps it takes.

<!-- Further facts, as **Name.** paragraphs, each only when it exists: **Opposition.** ([[npc]] or [[faction]], what it wants instead, and how it reacts when the party interferes), **Leads.** (each with how it enters play → [[page]]; any conclusion the party must reach gets two independent leads), **Stakes.** (what changes if the party succeeds or fails), **Rewards.** (what play can earn beyond the promise). -->

## Log

- **[[Session]]** — offered, accepted, advanced, or changed by events.
