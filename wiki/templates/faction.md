---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", faction]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: faction
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
kind: organization
status: active
scope: regional
region: ""
base: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. The page answers: what do they want, what will they do next, what changes if they succeed, and how can the party notice or interfere. Default page is the portrait, the italic classification line, and those answers. Other facts only when they exist; delete unused comments and narration slots. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- Faction portrait: their public face, ending on the name people use (theatre-of-the-mind). -->

<!-- Kind of group, leader, and base. Match YAML. -->

*Smuggling ring led by [[npc]], based at [[place]]*

<!-- Required when status is active. -->

**Wants.** The concrete change they are after, and why now.

**Next move.** What they attempt next and with what, the sign the party sees as it advances, and what becomes true if it succeeds.

<!-- Further facts, as **Name.** paragraphs, each only when it exists: **When met.** (what members are doing, how they treat the party, what they offer and what it costs), **When opposed.** (what they protect first and how they strike back), **Weakness.** (the dependency or exposure that can stop them), **People.** ([[npc]], their role, and where their loyalty cracks), **Standing.** (where the party stands with them and what would change it), **Secret.** (the hidden motive or fracture and the evidence that reveals it). Fighters are embedded, `![[owner#Statblock]]`. -->

> [!narration] When met
> <!-- Optional: members at work as the party runs into them, "you" address, ending on their first words (theatre-of-the-mind: Social scene). -->

## Log

- **[[Session]]** — move made, result, and who felt it.
