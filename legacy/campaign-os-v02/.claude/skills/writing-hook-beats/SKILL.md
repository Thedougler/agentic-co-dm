---
name: writing-hook-beats
description: >-
  Draft, revise, or audit a Hook beat — the opening-pressure beat of a
  dramatic unit in a Campaign OS vault. Use when composing a new Hook
  for a Beat Chart, when an opening lacks established player gravity or
  preserves too few player routes, or when auditing a Hook against the
  bite/route/refusal/outcome stress tests.
---

# Hook Beats

Write the opening **pressure**, not its answer.

A Hook succeeds when play begins with something worth responding to **now**, the party has an established reason to care, and the players retain meaningful control over what they do about it.

Use **gravity** as the governing concept: preparation attracts characters through things they already care about instead of requiring them to accept a plotted route.

## Reference

Read `references/hook-beats.md` when:

- selecting a Hook architecture;
- adapting an action-heavy or premise-heavy Hook to sandbox play;
- repairing weak player gravity;
- checking whether a Hook has become a rail;
- deciding how the Hook should hand off into later beats.

The reference owns Hook archetypes, diagnostics, pacing guidance, and the DM-facing body contract. Keep those details there.

## Workflow

### 1. Retrieve the live campaign context

Search the compiled vault before designing the Hook.

Find the smallest set of pages that establishes:

- the PCs involved;
- their current goals, fears, commitments, relationships, unresolved history, or other established gravity;
- the current location and active pressures;
- relevant factions, NPCs, threats, and prior consequences;
- the containing situation, narrative unit, or Beat Chart;
- any existing template or schema governing this beat type.

Follow relevant `[[wikilinks]]` rather than reconstructing linked canon from memory.

Treat the maintained vault as the source of truth for existing campaign facts. Add genuinely new preparation as new preparation; do not silently turn assumptions about existing characters or canon into facts.

**Complete when:** every existing fact the Hook depends on is grounded in the vault, the relevant character gravity is known, and the applicable beat-page schema has been identified.

### 2. Establish player gravity

Choose at least one **primary gravity anchor** from something a player character already cares about.

Good anchors include an established:

- goal;
- fear;
- relationship;
- enemy;
- obligation;
- promise;
- home or community;
- unresolved event;
- personal value;
- desired object or knowledge;
- consequence of previous play.

Prefer anchors that are already active over invented reasons the character ought to care.

Record a **Link of Relevance** that answers:

> What established character investment makes this situation difficult to ignore?

Name the relevant PC or PCs with `[[wikilinks]]` when their pages exist.

A party-wide Hook may have several Links of Relevance, but one concrete link is stronger than several vague ones.

**Complete when:** the Hook has at least one explicit Link of Relevance supported by established campaign material.

### 3. Build the Hook kernel

Reduce the Hook to five pieces:

1. **Catalyst** — what changes or intrudes when play begins.
2. **Gravity** — why these characters care.
3. **Pressure** — why responding now matters.
4. **Vectors** — materially different ways the situation can be approached.
5. **Consequence** — what the world does if the situation develops without successful intervention.

Choose a Hook architecture from `references/hook-beats.md` only after these pieces are known.

The Hook may begin with action, discovery, social pressure, danger, revelation, or another immediate source of interest. The architecture serves the kernel; it does not replace it.

**Complete when:** all five pieces can each be stated concretely in one sentence and none requires a predetermined player decision.

### 4. Draft for the human DM at the table

Write the beat for fast runtime use.

Lead with the situation the DM can put in front of the players immediately. Put actionable information before explanation.

Use the body contract in `references/hook-beats.md`:

- `## Hook`
- `## Player Gravity`
- `## First Look`
- `## Pressure`
- `## Open Vectors`
- `## If Unanswered`
- `## Handoff`

Keep lore on its owning pages. Use `[[wikilinks]]` or an appropriate embed when the DM needs access to existing material rather than copying that material into the Hook.

`Open Vectors` are prep coverage for the DM, not a menu the DM must read to the players.

**Complete when:** the DM can begin running the Hook from the first section and can adjudicate several plausible player responses without searching the prose for the situation's essential facts.

### 5. Run the gravity-and-agency audit

Test the drafted Hook before accepting it.

#### Bite test

For every stated Link of Relevance, ask:

> What established fact makes this character care?

Strengthen or remove any link whose answer depends on presumed player motivation.

#### Route test

Identify at least three materially different response classes that could produce continued play when the fiction permits them, such as:

- confront;
- investigate;
- negotiate;
- protect;
- pursue;
- evade;
- expose;
- exploit;
- seek allies;
- deliberately leave the problem alone.

These are tests, not required player options. Count genuinely different approaches rather than cosmetic variations of the same route.

#### Outcome test

Verify that success, failure, compromise, delay, and unexpected solutions can change what follows.

Prep the world's situation and pressures deeply enough to respond to player action; leave the players' solution and final outcome unresolved.

#### Refusal test

Ask what happens if the party rejects, delays, escapes, or ignores the apparent invitation.

A sandbox Hook remains playable after refusal. The world moves, stakes change, other actors act, and consequences can create later opportunities without converting refusal into a hidden failure state.

#### Information test

Verify that the players receive enough observable information to make an informed first decision.

Mystery may conceal answers. It should not conceal the existence of every actionable lead.

**Complete when:** player interest comes from gravity, at least three materially different response classes remain playable where fiction allows them, refusal has a world-state consequence rather than a dead end, and no required outcome is prewritten.

### 6. Check the beat handoff

Classify the Hook by its dominant table energy.

- An action-heavy Hook normally benefits from quieter discovery, conversation, investigation, or revelation afterward.
- A cerebral or low-action Hook normally benefits from a later increase in immediate peril or confrontation.

Use this as pacing preparation, not as a required player route.

Write `## Handoff` as the **most likely pressure transition** plus any alternate transition that becomes relevant if the players take a substantially different approach.

When this Hook belongs to a larger Beat Chart, preserve that chart's intended rhythm while allowing player action to determine how the transition actually occurs.

**Complete when:** the next prepared pressure changes the table's dramatic texture instead of merely repeating the Hook.

### 7. Vault conformance

Instantiate from the beat template. Run `npm run lint -- <path>` and fix findings.

**Complete when:** the beat passes lint and conforms to its template.
