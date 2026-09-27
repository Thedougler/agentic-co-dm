---
title: "{{title}}"
category: journal
tags: ["{{campaign}}", session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
kind: climax
reveal: unrevealed
campaign: "{{campaign}}"
session: ""
visibility: dm
card: ""
tier: ""
question: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this Climax spends it at the table; keep Final Battle or Final Revelation for the shape in play. Delete unused sections, bullets, rows, narration slots, and these comments. Completeness bar: docs/agents/table-ready.md. File as Session-<n>-<BB>-<label>.md. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

<!-- Required. The lines the DM runs the beat by, one fact each. What the opposition wants lives in Actors and what each ending changes lives in Outcomes; the card and the question this beat settles are design notes for agents and go in the frontmatter. -->

**Starting situation.** Positions, resources, allies, and what the party prepared.
**Party goal.** What the characters can accomplish here.
**If running late.** How to compress it (fewer phases, faster Pressure) and still settle it.
**Next beat.** [[Session-{{session}}-BB-label]]

> [!narration] Opening
> <!-- Read first: one paragraph, or immediate-fact bullets when the arrival is not fixed (theatre-of-the-mind: Climax opening). -->

## Party Assets

<!-- What the party earned this session that helps it win here: one line per item, ally, or truth, with what it does in this fight and what the fight is like without it. -->

- **[[page]]** — Advantage on attacks against the villain while the ward-stone burns; without it he regains 10 HP each round.

## Actors

<!-- Statblocks live in the Statblocks section; each line here carries only this fight's state (HP when not full, spent resources) and what the actor does. Add what they want, their leverage, or a line they will not cross only when it changes what they do at the table. -->

- **[[npc]].** The primary opposition, at its HP and resources this fight.
  - **Tactics.** Opening move → response when countered → desperation → exit, and how the party can close the exit.
- **[[creature]] × 4.** Role (henchman, minion, or hazard) and what they do.

> [!narration] {NPC}
> <!-- Optional, one per NPC, titled with their name, in the order the party meets them: their first look and first words (theatre-of-the-mind: NPC first look, Dialogue). -->

> [!narration] {Creature}
> <!-- Optional, one per creature kind, titled with its name, in the order the party meets them: a few sentences; its response to the party stays in Actors (theatre-of-the-mind: Creature in scene). -->

````col
```col-md
flexGrow=1
===
## Terrain

| Feature | What characters can do | Ruling |
| ------- | ---------------------- | ------ |
| [[page]] |                       |        |

**Distances.** The distances in feet that make positioning matter.

**Collateral.** Who or what nearby can be lost if the fight spills over.
```

```col-md
flexGrow=1
===
## Pressure

- [ ] **1. Warning.** What the players see coming.
- [ ] **2. Escalation.** The safety removed or opposition strengthened.
- [ ] **3. Crisis.** The hard choice.
- [ ] **4. Consequence.** The opposition gets what it wants.

**Ticks when.** A round passes, an action fails, or a threat is ignored.

**If it goes static.** The move that breaks a stalemate.
```
````

## Final Battle

**Lose when.** The opposition gets what it wants.

<!-- Narration cells: a line or two in `_italic_` per phase of what the party sees and hears change (theatre-of-the-mind: Tick cell). -->

| Phase | Trigger | What changes | Narration |
| ----- | ------- | ------------ | --------- |
| 1     | Opening |              | _…_       |

## Final Revelation

- **The truth.** What actually happened, stated as fact.
- **Proof on the table.** [[page]] — what it establishes.
- **Resistance.** [[npc]] — their claim, what breaks it, and their last move when cornered.
- **Wrong accusation.** What happens if the party names the wrong culprit.

> [!narration] Revelation
> <!-- Only with Final Revelation: the moment the truth lands, one short paragraph (theatre-of-the-mind: Revelation). -->

## PC Hooks

- **[[pc]].** The thread, foe, or feature that calls on them here.

## Outcomes

<!-- Required. One row per way the climax can end: what becomes true and the cost paid. Narration cells: a line or two in `_italic_` that lets that ending land (theatre-of-the-mind: Outcome cell). -->

| If the climax ends with… | What becomes true | Cost paid | Narration |
| ------------------------ | ----------------- | --------- | --------- |
| **Victory**              |                   |           | _…_       |
| **Costly victory**       |                   |           | _…_       |
| **Opposition wins**      |                   |           | _…_       |

**Carry forward.** Who and what remains active, and each state the Resolution inherits.

## Statblocks

<!-- One embed per fighter kind the party could face, from its owner page. -->

![[creature#Statblock]]
