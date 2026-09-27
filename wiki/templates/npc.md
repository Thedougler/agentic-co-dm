---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", npc]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: npc
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
status: alive
role: ""
location: ""
faction: ""
summary: ""
token: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Default page is the portrait, the italic identity line, and what the DM plays. Other facts only when they exist; delete unused comments and narration slots. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- Person portrait: one third-person paragraph, true every time they are met, with a visible tell for each secret (theatre-of-the-mind). -->

<!-- Identity: ancestry and calling, where the party meets them, allegiance. Match YAML. -->

*Human harbormaster at [[place]], sworn to [[faction]]*

<!-- What the DM plays, as **Name.** paragraphs, each only when it exists: **Wants.** (the concrete thing they are after now), **Voice.** (word choice, rhythm, one habit, and a line they would say), **What they share.** (what they tell freely, what opens them up or shuts them down, and what they never tell), **Secret.** (what they hide and how the party learns it), **Connections.** ([[page]] and what the tie does at the table). -->

**Wants.** The berth fees paid before the spring fleet arrives.

**Voice.** Clipped, counts on her fingers while she talks. "Coin first, questions after."

> [!narration] First meeting
> <!-- Optional: the moment the party first meets them, "you" address, what they are doing, then their first words (theatre-of-the-mind: NPC first look, Dialogue). -->

## Statblock

<!-- Only when they can fight: their full statblock, or `![[owner#Statblock]]` for a standard one filed on its own page. Guards or beasts they would set on the party are embedded from their own pages. -->

## Log

- **[[Session]]** — what changed for them.
