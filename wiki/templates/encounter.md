---
title: "{{title}}"
category: journal
tags: ["{{campaign}}", session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
kind: encounter
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
summary: ""
---
<!-- Reusable encounter kept outside a session. A scene run tonight is a beat instead. Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when you have facts for it; delete unused sections, bullets, rows, narration slots, and these comments. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

<!-- Required. The lines the DM runs the encounter by, one fact each. -->

**Location.** [[place]]
**First threat.** The visible threat the table can act on first.
**If ignored.** What the opposition or world does without the party.

> [!narration] Opening
> <!-- Read first: immediate-fact bullets, since a reusable encounter's arrival is rarely fixed; one paragraph when the encounter fixes it (theatre-of-the-mind: Box or bullets). -->

## Actors

- **[[npc]].** What they want, and what they offer, refuse, or shift on when the encounter turns on it.
- **[[creature]] × 3.** What it wants, how it fights or bargains, and when it breaks or leaves; its statblock is in Statblocks.

> [!narration] {NPC}
> <!-- Optional, one per NPC, titled with their name, in the order the party meets them: their first look and first words (theatre-of-the-mind: NPC first look, Dialogue). -->

> [!narration] {Creature}
> <!-- Optional, one per creature kind, titled with its name, in the order the party meets them: a few sentences; its response to the party stays in Actors (theatre-of-the-mind: Creature in scene). -->

## Party Choices

<!-- At least three materially different responses, each with its upside and cost. Narration cells: a line or two in `_italic_` of what the party sees change (theatre-of-the-mind: Outcome cell). -->

| If the party… | The world responds | Narration |
| ------------- | ------------------ | --------- |
|               |                    | _…_       |

## Outcomes

<!-- Required. One row per outcome the beat can plausibly produce: what changes and the beat it hands to. Narration cells: a line or two in `_italic_` of the changed state (theatre-of-the-mind: Outcome cell). -->

| Outcome | What changes | Next | Narration |
| ------- | ------------ | ---- | --------- |
|         |              | [[page]] | _…_ |

## Statblocks

<!-- One embed per fighter kind the party could face, from its owner page. -->

![[creature#Statblock]]
