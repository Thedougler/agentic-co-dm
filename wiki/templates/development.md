---
title: "{{title}}"
category: journal
tags: ["{{campaign}}", session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
kind: development
reveal: unrevealed
campaign: "{{campaign}}"
session: ""
visibility: dm
card: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this Development spends it at the table; delete unused sections, bullets, rows, narration slots, and these comments. Completeness bar: docs/agents/table-ready.md. File as Session-<n>-<BB>-<label>.md. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

<!-- Required. The lines the DM runs the beat by, one fact each. The truth this beat turns on lives in Clues; the card is a design note for agents and goes in the frontmatter. -->

**Starting situation.** What the party carries in: position, condition, what they believe.
**Starts when.** What brings this scene on screen.
**Next beat.** [[Session-{{session}}-BB-label]]

> [!narration] Opening
> <!-- Read first: one paragraph, or immediate-fact bullets when the arrival is not fixed (theatre-of-the-mind: Development opening). -->

````col
```col-md
flexGrow=1
===
## Situation

- **Location.** [[place]]
- **Evidence.** The thing to search, examine, or witness, and what it reveals.
- **Obstacle.** What makes a clean answer hard.
- **Time limit.** What ends the talking if it circles, and when.
- **If ignored.** What happens to the truth or the lead if the party walks past it.
```

```col-md
flexGrow=1
===
## Actors

- **[[npc]].** What they want now and what they will tell. What they hide and its tell, their price, or what changes their mind go here only when the scene turns on it.
```
````

> [!narration] {NPC}
> <!-- Optional, one per NPC, titled with their name, in the order the party meets them: their first look and first words (theatre-of-the-mind: NPC first look, Dialogue). -->

## Party Choices

<!-- What the party can work on here, why it works, and what it costs. -->

- **[[npc]]** can be persuaded, pressured, or exposed because…
- **[[item]]** can be examined, used, or traded because…
- **[[place]]** can be searched, entered, or watched because…
- **Cost.** What the party pays for the best version of this information.

## Checks

| Intent | Approach | DC | Success | Failure |
| ------ | -------- | -- | ------- | ------- |
|        | **Intelligence (Investigation)** | `DC 13` |  |  |

<!-- Sensible actions with no real doubt succeed automatically; say what they yield in Clues. -->

## Clues

<!-- Truths stated as facts, each with where it surfaces. A conclusion the session needs gets three independent routes. -->

- [ ] **Core.** The truth that changes what the party knows or can do → surfaces through [[page]].
- [ ] **Support.** A fact about motive, stakes, or history → surfaces through [[page]].

> [!narration] Revelation
> <!-- Once, after Clues: the moment the Core clue lands, one short paragraph (theatre-of-the-mind: Revelation). -->

## Outcomes

<!-- Required. One row per outcome the beat can plausibly produce: what changes and the beat it hands to. Narration cells: a line or two in `_italic_` of the changed state (theatre-of-the-mind: Outcome cell). -->

| If the party… | What changes | Next | Narration |
| ------------- | ------------ | ---- | --------- |
| Follows the clearest lead |  | [[Session-{{session}}-BB-label]] | _…_ |
| Refuses or delays |  | [[Session-{{session}}-BB-label]] | _…_ |

**Carry forward.** Each state the next beat inherits: new knowledge, direction, who is where, what they prepared.
