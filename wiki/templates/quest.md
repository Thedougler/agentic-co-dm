---
title: "{{title}}"
category: campaign
tags: [quest]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: quest
lifecycle: proposed
reveal: unrevealed
campaign: shattered-sea
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
<!--
Copy-start scaffold. Track the situation, not a plotted sequence.

Status: rumored | offered | active | stalled | resolved | failed | expired
Scope: personal | local | regional | realm | world

Keep this page current rather than exhaustive. Link the NPCs, factions, places,
items, creatures, and subquests that hold detailed material elsewhere.

Design basis: prep situations and what happens without PC intervention rather
than predetermined plot beats; expose several independent routes through the
situation; track active forces with goals, portents, and consequences; keep
campaign threads concise enough to review before play.
-->

# {{title}}

> [!summary] Quest
> **Status:** Offered
> **Objective:** What can the party accomplish? State the result, not the method.
> **Why now:** What makes this matter now?
> **Deadline:** None, or the fictional event after which the situation changes.

## At a Glance

|                 |                                            |
| --------------- | ------------------------------------------ |
| **Quest giver** | [[page]]                                   |
| **Region**      | [[place]]                                  |
| **Scope**       | Local                                      |
| **Opposition**  | [[npc-or-faction]]                         |
| **Reward**      | What is promised or plausibly gained.      |
| **Last change** | What most recently altered this situation. |

## Situation

Write the minimum facts needed to understand the quest **as it exists now**. Describe the unstable situation, the forces involved, and what each side is already doing. Do not prescribe what the party does next.

### What the party knows

> [!narration] Player-facing brief
> State the hook, request, rumor, evidence, or visible problem using only information the characters currently possess.

### What is really happening

Write the DM-facing truth behind the quest. Keep uncertain outcomes unresolved.

## Stakes

* **If the party succeeds:** What materially changes in the world?
* **If the party fails:** What materially changes instead?
* **If the party walks away:** What continues without them?
* **Question:** What important outcome should play decide?
* **Question:** Who or what might change sides, survive, fall, or gain power?

<!-- Stakes are questions to play to find out, not answers you have already decided. -->

## World in motion

|                  |                                                   |
| ---------------- | ------------------------------------------------- |
| **Driver**       | [[npc-faction-creature-or-force]]                 |
| **Wants**        | The concrete outcome it is pursuing.              |
| **Current move** | What it is doing right now.                       |
| **Next move**    | What it will attempt if nothing interrupts it.    |
| **End state**    | The lasting consequence if it gets what it wants. |

### Progress

* [ ] **Portent 1.** First observable change if the situation advances.
* [ ] **Portent 2.** A more serious change that alters options or relationships.
* [ ] **Portent 3.** The situation becomes difficult to reverse.
* [ ] **End state.** The world changes even if the quest remains unresolved.

> [!warning] Current pressure
> Record the next consequence that can enter play. Advance this only when fiction, elapsed time, or player action justifies it.

## Leads & routes

<!--
Do not build a required sequence. Each row is somewhere the party could push
the situation next. For any conclusion the party must reach, seed multiple
independent clues or leads rather than relying on one chokepoint.
-->

| Lead                                                         | Points toward       | Found? | State     |
| ------------------------------------------------------------ | ------------------- | ------ | --------- |
| Evidence, rumor, invitation, witness, trail, or opportunity. | [[place-or-entity]] | No     | Available |
| Independent route to useful progress.                        | [[place-or-entity]] | No     | Available |
| Independent route to useful progress.                        | [[place-or-entity]] | No     | Available |

## People & factions

| Entity   | Role in the quest                                            | Wants / pressure                         |
| -------- | ------------------------------------------------------------ | ---------------------------------------- |
| [[page]] | Patron, rival, victim, witness, hunter, ally, obstacle, etc. | What they are trying to make happen now. |
| [[page]] |                                                              |                                          |

## Relevant places

| Place     | Why it matters now                                                     |
| --------- | ---------------------------------------------------------------------- |
| [[place]] | What can be learned, changed, obtained, prevented, or confronted here. |
| [[place]] |                                                                        |

## Useful things

| Entity                  | Use in play                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| [[item-or-resource]]    | Leverage, evidence, key, payment, vulnerability, tool, or prize. |
| [[creature-or-vehicle]] | How it can alter the situation.                                  |

## Complications

* **Pressure:** A problem that can appear without dictating how the party responds.
* **Tradeoff:** Something valuable that cannot be protected without cost.
* **Reaction:** How an involved force changes tactics when the party interferes.
* **Reversal:** A fact that can reframe the situation if discovered.

<!-- Omit unused complications. Prefer reusable pressures over scripted scenes. -->

## Rewards & consequences

### Promised

* What the quest giver explicitly offers.

### Possible

* Treasure, access, reputation, alliances, information, territory, favors, or other gains that emerge from play.

### Fallout

* Who gains or loses power.
* Which relationship changes.
* Which place changes.
* Which new problem or opportunity appears.

## Quest log

| Date / Session           | Change                                                                        |
| ------------------------ | ----------------------------------------------------------------------------- |
| YYYY-MM-DD / [[Session]] | Quest offered, accepted, advanced, redirected, stalled, or changed by events. |

<!--
After meaningful play or campaign downtime:
1. Change status if needed.
2. Rewrite "Situation" to match the new present.
3. Advance, alter, or cancel portents based on what actually happened.
4. Update leads the party found or invalidated.
5. Record changed NPC/faction goals.
6. Add one Quest log row.
7. Update frontmatter `last_advanced` and `updated` (YAML keys; not DM-visible labels).
-->

## Resolution

<!-- Fill when the quest reaches a stable outcome. Omit while unresolved. -->

**Outcome:** Resolved / Failed / Expired / Transformed

Write what actually happened without rewriting it into the outcome that had originally been expected.

### World changes

* [[page]] — Lasting change caused by the resolution.
* [[page]] — Lasting change caused by the resolution.

### Loose threads

* [[quest-or-entity]] — What remains unresolved, escalates, or becomes newly possible.
