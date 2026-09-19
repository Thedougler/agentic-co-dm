---
name: traps-trials
description: >-
  Trap, hazard, trial, or puzzle craft — telegraph, affordances,
  fail-forward, escalation. Use when a beat, situation, or location
  needs a challenge the party can detect and beat by play, or when
  auditing telegraphing, multiple solutions, and cost on failure.
---

# Traps & Trials
File what constitution X makes canon. Follow `docs/agents/work.md`.

## Operating words

* **Telegraph** — expose actionable evidence before meaningful consequences.
* **Afford** — give fictional objects and conditions obvious ways to be investigated or manipulated.
* **Open** — prepare a problem with rules, not a prescribed player solution.
* **Fail-forward** — failure changes the situation while leaving play alive.
* **Escalate** — increase pressure through state changes rather than repeating the same check.
* **Spotlight** — create opportunities for different characters and player ideas to matter.
* **Sandbox** — make the challenge a world object that survives unexpected approaches.
* **Reveal, don’t punish** — telegraph enough for an informed choice; a hidden step → damage tax is not a challenge.
* **Fuse** — make waiting unsafe by advancing a visible threat or changing state.

---

## Workflow

### 1. Ground the challenge in the world

Read the smallest set of current vault pages needed to establish context.
Identify: location, builder/creator/source, purpose, current world
state, related entities, and facts owned by other pages. Use exact
`[[wikilinks]]`. Keep facts on their owning pages — link to existing
lore, repeat only what's needed to run the challenge.

Choose where the content belongs: **standalone page** (reusable,
substantial, complex), **section of another page** (inseparable and
small), or **embed** (content already has an authoritative home).

**Complete when:** the challenge has a clear fictional owner, purpose,
and context, with no duplicated canon.

### 2. Define the challenge contract

Reduce to one sentence: *Characters encounter [problem] caused by
[mechanism]; they risk [stakes] while trying to achieve [goal].*

Classify its dominant form and the kind it writes:

* **Trap** — intentional mechanism → the existing trap or hazard note type
* **Puzzle** — understanding or manipulation is the obstacle → the existing trial or encounter note type
* **Hazard** — ongoing environmental danger → the existing hazard note type
* **Trial** — structured test of competence, judgment, or sacrifice → the existing trial or encounter note type
* **Composite** — one page of the dominant form, linking the others

There is no standalone puzzle type; use the existing challenge or hazard template.

Establish: default state, activation condition, stakes, what changes
once engaged, reset/persistence behavior, what success makes possible,
what failure changes. Define the problem, not the party's answer.

**Complete when:** the challenge can be explained without predicting
what the PCs will do.

### 3. Model the hidden mechanism

Write the DM-facing truth before writing clues.

Simple challenge: trigger, mechanism, effect, duration,
reset/persistence. Dynamic challenge: model explicit states (e.g.
`Dormant → Disturbed → Active → Escalating → Resolved`) — for each
transition, specify cause, observable change, mechanical effect change,
and remaining actions. Magical mechanisms still need learnable rules.

**Complete when:** every meaningful state and transition has a cause
and an observable consequence.

### 4. Telegraph the challenge

Build a reveal ladder: **Immediate** (sensory evidence, no check),
**Investigated** (check-gated actionable information), **Understood**
(mechanism, pattern, timing, vulnerable component), **Mastered**
(control point, shutdown, safe window, redirect, weaponize). Essential
information must remain obtainable after a failed check.

Consult `references/challenge-craft.md` § Telegraph for sensory-evidence
examples and the full ladder detail.

**Complete when:** players can perceive a meaningful situation,
investigate it, and make an informed choice.

### Suspense gate: make the trap a scene

Use this gate for any challenge meant to sustain tension. Mystery hides
information so players dig; surprise withholds the bomb until it lands;
suspense reveals that a bad thing is already moving and puts weight on
choices under a fuse. Apply the five-part bomb test:

1. **Reveal the threat** — show enough that harm is in motion, not the whole
   picture. Use signs such as dart holes, scorch, dead insects, a clean sword
   on a dusty statue, or claw marks inside a door.
2. **Show the fuse** — waiting is unsafe and the situation worsens on its own.
3. **Hide the clean answer, not the problem** — preserve discovery without
   denying the players a fair chance to respond.
4. **Price every route** — time, HP, spells, gear, position, relationships,
   future leverage, or moral cost; no free clean solve.
5. **Let them act** — prepare the mechanism, not the ending. Accept a clever
   unplanned solution and let the world adapt afterward.

A revealed trap is a puzzle; a puzzle plus a fuse is a scene. Prefer dynamic
traps whose state changes (rising water, spreading gas, faster pendulum) over
hidden punishment. An environmental nudge or Passive Perception can surface
the sign, especially for a less experienced table.

**Complete when:** the threat, fuse, unknown clean answer, real costs, and at
least three materially different response paths are explicit.

### 5. Build the interaction surface

List physical/fictional things characters can act upon. Test distinct
solution vectors: avoid, disable, solve, redirect, endure, shield,
outrun, exploit, alter, satisfy, subvert. Adjudicate unanticipated
approaches from the established mechanism.

Consult `references/challenge-craft.md` § Interaction for affordance
examples, vector definitions, and roll criteria.

**Complete when:** at least two genuinely different approaches can
change the situation; suspense scenes should expose at least three.

### 6. Build consequences and recovery

Choose consequences arising from the fiction. Price every response in
fictional resources or future position; avoid damage that follows merely from
touching an undisclosed trigger. Use partial states where useful. For puzzles
and trials, a wrong answer should reveal information, advance the fuse, or
transform the problem. Define recovery after failure.

Consult `references/challenge-craft.md` § Consequences for consequence
types and partial-state patterns.

**Complete when:** every failure state leads to a playable next state.

### 7. Add escalation

Escalation changes the **problem**, not the difficulty number. Each
stage changes information, options, position, stakes, or mechanics.

Consult `references/challenge-craft.md` § Escalation for patterns.

**Complete when:** each escalation stage changes the situation.

### 8. Spotlight the party

Check whether different character types can contribute meaningfully.
Treat abilities that cleanly overcome the challenge as earned advantages.

Consult `references/challenge-craft.md` § Spotlight for contribution types.

**Complete when:** more than one player can contribute before or during
resolution.

### 9. Sandbox stress-test

Test the challenge as a world object against unexpected sequencing,
approach, and consequences. Resolve edge cases by clarifying the
mechanism, not adding arbitrary immunities.

Consult `references/challenge-craft.md` § Sandbox for stress-test
questions.

**Complete when:** the challenge survives unexpected sequencing without
requiring the DM to restore a predetermined path.

### 10. Tune the mechanics

Use the campaign's existing rules and stat math as the primary source
of truth. Tune four dimensions separately: detection difficulty,
interaction difficulty, consequence severity, pressure/escalation speed.

Consider: party level, expected resources, frequency, number affected,
compounding failure, whether optional, telegraph strength, recovery
availability, reward value.

Check type and DC → `dnd5e-mechanics`. Escalate the situation, not the number.

**Complete when:** mechanical threat is proportional to telegraphing,
frequency, recoverability, and narrative stakes.

### 11. Render for the human DM

Instantiate the relevant note type and template under `wiki/`. Write for scan speed: short bullets, explicit
triggers, DCs beside the action, consequences beside their trigger,
wikilinks instead of repeated lore. If the challenge needs a combatant
statblock, invoke `homebrew-monsters-5e`. If the host place lacks
physical logic, invoke `place-design` — or `dungeon-design` when
the host is a multi-room dungeon. If the challenge exists but
the fiction is still generic, invoke `flesh-out`.

Default to sensory bullets. Add `[!narration]` only when the DM must
speak a picture. Hidden mechanism stays in `[!secret]-`. Write triggers,
checks, and saves with the at-table grammar in `obsidian-markdown`:
**Trigger:**, **Ability (Skill) — `DC n`**, Success/Failure → outcomes,
damage as `` `2d6` ``.

**Complete when:** a DM unfamiliar with the design can run the challenge
from the page alone.

---

## Final gate

Run `references/quality-gate.md` before finishing.

## Table-prep gate

Prepare only the challenge facts the DM will not improvise: a compact mechanism,
telegraphs, affordances, costs, and recovery states. Keep them modular and
findable in under 30 seconds; attach at least one contribution/limelight route per
PC when the situation permits. Keep secrets in DM sections, never `[!narration]`,
and link the challenge's atomic owner through the nearest MOC.

## References

| File | Contents |
|------|----------|
| `references/challenge-craft.md` | Reveal ladder, solution vectors, consequences, escalation, spotlight, sandbox |
| `references/quality-gate.md` | 16-item completion checklist |
