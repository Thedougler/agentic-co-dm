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
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Default page is the portrait, the italic classification line, and the key: what the party finds, area by area. Campaign facts come after the key, only when they exist. Delete unused comments and narration slots. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

> [!narration] {{title}}
> <!-- Place portrait: one third-person paragraph at body scale, a second only when the tells need it, with a visible tell for every secret, hazard, and presence on this page (theatre-of-the-mind). -->

<!-- Kind of site, its region, and who holds it now. Match YAML. -->

*Ruined watchtower in [[region]], held by [[faction]]*

<!-- Required. The key, as a published adventure keys a site. A small site is **Name.** paragraphs right here; a site with several areas gets one `##` per area, each opening with its `{Area}` narration. Each feature says what it is, what the party can do with it, and the check where the outcome is uncertain. Occupants link their page and say what they want and do; fighters are embedded, `![[owner#Statblock]]`. -->

## {Area}

> [!narration] {Area}
> <!-- Optional, titled with the area's name: what the party perceives on entering, "you" address. One paragraph when the area has one way in; immediate-fact bullets when it has several or who is there depends on play (theatre-of-the-mind: Zone cell, Box or bullets). -->

**Feature.** What it is and what the party can do with it: **Strength (Athletics)** — `DC 12` to climb, and on a failure the climber falls 10 feet.

<!-- Campaign facts after the key, as **Name.** paragraphs, each only when it exists: **Secret.** (the hidden truth and the clue that reveals it), **Exits.** ([[place]], the route, the distance, and what lies between). -->

> [!narration] Returning
> <!-- Only once the party has been here: what changed since their last visit (theatre-of-the-mind: Return to a known place). -->

## Log

- **[[Session]]** — what changed here.
