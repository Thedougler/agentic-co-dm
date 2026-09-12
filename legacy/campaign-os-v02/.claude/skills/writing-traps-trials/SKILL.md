---
name: writing-traps-trials
description: >-
  Design, revise, or audit challenge content — a trap, puzzle, hazard, or
  trial — in a Campaign OS repo (vault/ present). Use when a beat,
  situation, location, or quest needs a challenge the party can detect,
  interact with, and beat by play; when drafting a `type: puzzle` page or a
  trap/hazard block; or when auditing existing challenge content against
  the quality gate (fair telegraphing, multiple solutions, cost on
  failure).
---

# Writing Traps & Trials

Author runnable challenge content for an LLM-maintained campaign wiki
that doubles as a fast-reference Obsidian vault for the human DM.

This skill owns the **challenge itself**: what exists in the fiction,
what characters can perceive, how it works, what can be done about it,
and how the world changes when characters interact with it.
Session-planning systems own placement and orchestration.

## Operating words

* **Telegraph** — expose actionable evidence before meaningful consequences.
* **Afford** — give fictional objects and conditions obvious ways to be investigated or manipulated.
* **Open** — prepare a problem with rules, not a prescribed player solution.
* **Fail-forward** — failure changes the situation while leaving play alive.
* **Escalate** — increase pressure through state changes rather than repeating the same check.
* **Spotlight** — create opportunities for different characters and player ideas to matter.
* **Sandbox** — make the challenge a world object that survives unexpected approaches.

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

Classify its dominant form:

* **Trap** — intentional mechanism triggered by intrusion or behavior.
* **Puzzle** — understanding or manipulating information is the primary obstacle.
* **Hazard** — terrain, weather, magic, or environmental conditions create ongoing danger.
* **Trial** — a deliberately structured test of competence, judgment, or sacrifice.
* **Composite** — two or more forms operate as one challenge.

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

### 5. Build the interaction surface

List physical/fictional things characters can act upon. Test distinct
solution vectors: avoid, disable, solve, redirect, endure, shield,
outrun, exploit, alter, satisfy, subvert. Adjudicate unanticipated
approaches from the established mechanism.

Consult `references/challenge-craft.md` § Interaction for affordance
examples, vector definitions, and roll criteria.

**Complete when:** at least two genuinely different approaches can
change the situation.

### 6. Build consequences and recovery

Choose consequences arising from the fiction. Use partial states where
useful. For puzzles and trials, a wrong answer should reveal information
or transform the problem. Define recovery after failure.

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

Consult `vault/refs/table-random-traps.md` for DC and damage-severity
bands. Consult `vault/refs/gameplay-toolbox-traps.md` for SRD trap
examples.

**Complete when:** mechanical threat is proportional to telegraphing,
frequency, recoverability, and narrative stakes.

### 11. Render for the human DM

Instantiate `vault/_templates/_srd/_puzzle.md`. Write for scan speed:
short bullets, explicit triggers, DCs beside the action, consequences
beside their trigger, wikilinks instead of repeated lore.

Default to sensory bullets rather than boxed narration. Add polished
read-aloud prose only when explicitly requested or when the repository
format requires it.

**Complete when:** a DM unfamiliar with the design can run the challenge
from the page alone.

---

## Final gate

Run `references/quality-gate.md` before finishing.

## References

| File | Contents |
|------|----------|
| `references/challenge-craft.md` | Detailed craft for steps 4–9: reveal ladder, solution vectors, consequence types, escalation, spotlight, sandbox |
| `references/quality-gate.md` | 16-item completion checklist |
| `vault/refs/table-random-traps.md` | DC and damage-severity bands by level |
| `vault/refs/gameplay-toolbox-traps.md` | SRD trap anatomy and worked examples |
