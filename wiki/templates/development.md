---
title: "{{title}}"
category: journal
tags: [shattered-sea, session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
kind: development
lifecycle: proposed
reveal: unrevealed
campaign: shattered-sea
session: ""
visibility: dm
summary: ""
---
<!-- Copy-start scaffold. Abstract; Opening; Run the beat; Situation; Revelations; Exits. Omit unused. Pass is those jobs. File Session-<n>-<BB>-<Label>.md. -->

# {{title}}

> [!abstract] Development
> **Purpose.** What this beat needs to change for the party.
>
> **Trigger.** What brings this situation on screen.
>
> **Turn.** The fact, warning, relationship, advantage, or complication that changes the party's understanding.
>
> **Exit.** The decision, actionable lead, or changed situation that means the beat has done its job.
>
> **Target.** ~30 minutes.

> [!narration] Opening
> Write 2–4 player-facing sentences establishing only what the characters can immediately perceive. End on something they can respond to.

## Run the Beat

1. **Present the situation.** What wants the party's attention right now?
2. **Let them engage.** What can they question, inspect, negotiate with, test, or refuse?
3. **Make the turn.** Surface the information or change that makes this beat matter.
4. **Hand back the choice.** State the changed situation clearly and ask what they do.

````col
```col-md
flexGrow=1
===
## Situation

- **Where.** [[Place]]
- **Present.** [[NPC]], [[NPC]]
- **Immediate want.** What the active person, faction, or situation wants right now.
- **Friction.** What makes getting a clean answer or agreement difficult.
- **Pressure.** What keeps the party from deliberating forever without forcing an outcome.
- **If ignored.** What proceeds without the party.
```

```col-md
flexGrow=2
===
## Revelations

<!-- Write truths, not scripts for how the party must discover them. Surface each through whatever method fits play. -->

- [ ] **Core.** The truth that materially changes what the party knows, wants, or can do. → **Leads:** [[Node]]
- [ ] **Support.** A fact that clarifies motives, stakes, history, or consequences. → **Leads:** [[Node]]
- [ ] **Optional.** A useful secret, connection, omen, or piece of texture. → **Leads:** [[Node]]
```
````

> [!tip]- Required conclusion — redundancy
> Use only when the adventure depends on the party reaching a particular conclusion.
>
> **Conclusion.** What the players need enough evidence to reasonably conclude.
>
> - [ ] **Route 1.** An independent clue, witness, observation, document, or consequence.
> - [ ] **Route 2.** A different source or method pointing to the same conclusion.
> - [ ] **Route 3.** A third independent route, preferably accessible from another person, place, or beat.

## Actors

| Actor   | Wants now | Offers / withholds | Posture changes when |
| ------- | --------- | ------------------ | -------------------- |
| [[NPC]] |           |                    |                      |
| [[NPC]] |           |                    |                      |

<!-- Link full NPC notes. Record only beat-specific wants, leverage, and posture here. -->

## Checks & Costs

<!-- Omit when nothing meaningful is uncertain. Essential progress should never depend on a single failed check. -->

- **Automatic.** What the characters learn or accomplish simply by taking the sensible action.
- **Action — DC __.** **Success:** what improves, opens, or becomes certain. **Failure:** a cost, delay, exposure, complication, or incomplete answer that still leaves play moving.
- **Action — DC __.** **Success:** . **Failure:** .

## Player Levers

- **Person.** [[NPC]] can be persuaded, pressured, helped, exposed, or questioned because…
- **Thing.** [[Item]] can be examined, used, traded, destroyed, or presented because…
- **Place.** [[Place]] can be searched, entered, watched, avoided, or revisited because…
- **Promise / problem.** Something the party can accept, reject, bargain over, or solve.

## Exits

| If the party…                     | The situation changes…                                                   | Next                             |
| --------------------------------- | ------------------------------------------------------------------------ | -------------------------------- |
| Pursues the clearest lead         |                                                                          | [[Session-{{session}}-BB-Label]] |
| Refuses, delays, or walks away    |                                                                          | [[Session-{{session}}-BB-Label]] |
| Changes the situation another way | Preserve the established truths; follow the consequence of their action. | [[Open Node]]                    |

> [!warning] If the Beat Stalls
>
> - Have an actor pursue their immediate want.
> - Surface the clearest unrevealed fact through something already in the scene.
> - Advance the pressure and show its consequence.
> - Restate what has changed and the obvious handles the party can act on; remain open to another approach.
> - Once the party has an actionable direction, end the beat and move on.

> [!note]- After Play
>
> - **What actually happened.**
> - **Revelations learned.**
> - **Decision made.**
> - **NPC / faction posture changes.**
> - **Resources gained or lost.**
> - **World state changed.**
> - **Next active node.** [[Beat]]
> - **Unresolved thread.** [[Thread]]
