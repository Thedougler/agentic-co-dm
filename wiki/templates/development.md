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
summary: ""
---
<!-- Copy-start scaffold for `development-beats`. Jobs: Abstract; Opening; Run the beat; Situation; Revelations; Actors; Checks & costs; Player levers; Exits. Omit a section only when this Development never spends it. Bar: docs/agents/table-ready.md. File Session-<n>-<BB>-<Label>.md. -->

# {{title}}

**Card.** Development card from `development-beats`.
**Thread advanced.** The live thread and the new facet this beat reveals.
**Entry state.** What the party carries in from the previous beat: position, condition, what they believe.
**Trigger.** What brings this situation on screen.
**Turn.** One sentence: the fact, warning, relationship, advantage, or complication that changes the party's understanding.
**New direction.** The direction of action the turn sets — what the party can now do or pursue that it could not before.
**Memorable element.** The image, person, or reveal the table will remember.
**Target.** ~30 minutes.

> [!narration] Opening
> <!-- Load `.agents/skills/theatre-of-the-mind` → references/scenes.md → Development opening. -->
> Spoken text the DM reads aloud, written to that recipe.

## Run the Beat

1. **Present the situation.** What wants the party's attention right now.
2. **Let them engage.** The physical anchor they can work — a site to search, a body to examine, a map to read, a ritual to witness — and the people they can question, bargain with, or refuse.
3. **Make the turn.** How the turn surfaces through what they are already doing.
4. **Hand back the choice.** State the changed situation and the new direction. Ask what they do.

````col
```col-md
flexGrow=1
===
## Situation

- **Where.** [[Place]]
- **Present.** [[NPC]], [[NPC]]
- **Physical anchor.** The thing to do with their hands, and the revelation it surfaces.
- **Friction.** What makes a clean answer or agreement hard.
- **Pressure.** What ends the talking if it circles — a deadline, an interruption, a clock tick — and when.
- **If ignored.** What proceeds without the party.
```

```col-md
flexGrow=2
===
## Revelations

<!-- Truths stated as facts, each with where it surfaces. The story may be whole; the solution to the next contest stays for the party to earn. -->

- [ ] **Core.** The truth that changes what the party knows, wants, or can do. → **Surfaces through:** [[Node]] / person / object
- [ ] **Support.** A fact that clarifies motives, stakes, history, or consequences. → **Surfaces through:**
- [ ] **Optional.** A useful clue, connection, omen, or texture. → **Surfaces through:**
```
````

### Required conclusion

<!-- Keep when the session depends on the party drawing one conclusion. -->

**Conclusion.** What the players need enough evidence to reasonably conclude.

- [ ] **Route 1.** An independent clue, witness, observation, document, or consequence.
- [ ] **Route 2.** A different source or method pointing to the same conclusion.
- [ ] **Route 3.** A third independent route, from another person, place, or beat.

## Actors

| Actor   | Wants now | Knows (true) | Offers | Withholds / lies about — and the tell | Price for help | Posture shifts when |
| ------- | --------- | ------------ | ------ | ------------------------------------- | -------------- | ------------------- |
| [[NPC]] |           |              |        |                                       |                |                     |
| [[NPC]] |           |              |        |                                       |                |                     |

<!-- Full NPC notes stay on owner pages. Quoted lines the DM can speak are filled through `theatre-of-the-mind`. -->

## Checks & Costs

<!-- `dnd5e-mechanics` sets every check. Essential progress rests on more than one check. -->

- **Automatic.** What the characters learn or accomplish by taking the sensible action.
- **Action.** **Ability (Skill)** `DC __`. **Success:** what improves, opens, or becomes certain. **Failure:** a cost, delay, exposure, or incomplete answer that keeps play moving.
- **Cost of the good part.** What the best information or help costs, and why it bites: a favor owed, a promise, world time on a clock that is running, exposure.

## Player Levers

- **Person.** [[NPC]] can be persuaded, pressured, helped, exposed, or questioned because…
- **Thing.** [[Item]] can be examined, used, traded, destroyed, or presented because…
- **Place.** [[Place]] can be searched, entered, watched, avoided, or revisited because…
- **Promise / problem.** Something the party can accept, reject, bargain over, or solve.

### Preparation states

<!-- Keep when this Development is the party preparing for the next contest. -->

| If the party prepares… | The next Cliffhanger opens with… |
| ---------------------- | -------------------------------- |
| Thoroughly             |                                  |
| Partly                 |                                  |
| Not at all             |                                  |

## Exits

| If the party…                     | The situation changes…                                                      | Next                             |
| --------------------------------- | --------------------------------------------------------------------------- | -------------------------------- |
| Pursues the clearest lead         |                                                                             | [[Session-{{session}}-BB-Label]] |
| Refuses, delays, or walks away    |                                                                             | [[Session-{{session}}-BB-Label]] |
| Changes the situation another way | The established truths stand; the world follows the consequence of their act. | [[Open Node]]                    |

**Carry forward.** One line per state variable the next Cliffhanger inherits — new knowledge, the party's direction, who is where, what they prepared.

### After Play

- **What actually happened.**
- **Revelations learned.**
- **Decision made.**
- **NPC / faction posture changes.**
- **Resources gained or lost.**
- **World state changed.**
- **Next active node.** [[Beat]]
- **Unresolved thread.** [[Thread]]
