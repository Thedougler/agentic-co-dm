---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", place]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: place
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
kind: site
region: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when you have facts for it; delete unused sections, glance bullets, and these comments. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

## At a Glance

<!-- Required. Lead sentence: why the party comes here and what is happening now. Then labelled facts, one bullet each. -->

- **Who is here.** [[npc]] or [[creature]], how many, doing what.
- **Danger.** The threat and its trigger.
- **Draw.** What the party can gain here.

> [!narration] {{title}}
> <!-- One third-person paragraph at body scale, a second only when the tells need it: size, ground, air, light, exits, one sense beyond sight, one thing to use, a visible tell for every secret, hazard, and presence on this page (theatre-of-the-mind: Place portrait). -->

## Features

<!-- The people, creatures, objects, and terrain a DM can put on the table, each with what it does or how it can be used. Link owner pages. Use `###` for rooms or areas when the place has several. -->

- **Feature.** What it is and what the party can do with it.

> [!narration] {Area}
> <!-- Optional, one per `###` area, under its heading, titled with the area's name: what the party perceives on entering, "you" address. One paragraph when the area has one way in; immediate-fact bullets when it has several or who is there depends on play (theatre-of-the-mind: Zone cell, Box or bullets). -->

## At the Table

<!-- What the party is likely to try and what happens. Add a check only when the outcome is uncertain. -->

- **If the party** does this — what changes, with the check and its result.

> [!narration] Returning
> <!-- Only once the party has been here: what changed since their last visit, a short paragraph (theatre-of-the-mind: Return to a known place). -->

## Secrets

<!-- Hidden truths here, each with the clue that reveals it. -->

## Connections

- [[place]] — how it connects: route, distance, what lies between.

## History

<!-- Past events that still change what the party finds. -->

## Log

- **[[Session]]** — what changed here.

