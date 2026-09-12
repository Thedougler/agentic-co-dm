---
name: writing-resolution-beats
description: >-
  Draft, revise, or audit a Resolution beat — the post-Climax fallout beat of a
  dramatic unit in a Campaign OS vault. Use when composing a new Resolution for
  a Beat Chart, when compiling actual fallout after a played Climax, when
  preparing a consequence envelope before an unplayed Climax, or when auditing a
  Resolution against the causality, agency, gravity-receipt, and sandbox
  integrity gates.
---

# Resolution Beats

Write the **fallout**, not a predetermined ending.

A Resolution is the final Beat of the current situation — it shows what became true because of the Climax. The GM prepares the **irrigation**: consequence rules, affected actors, gravity receipts, and the world's causal responses. The players remain the **water**: they earned the outcome, and the Resolution reflects it without deciding what they do next.

Use **fallout** as the governing concept: the Climax answers the dramatic question; the Resolution records the material difference that answer made.

## Reference

Read `references/resolution-beats.md` when:

- establishing the state delta (cause → new truth → visible evidence);
- building a consequence envelope in PREP mode;
- compiling actual fallout in COMPILE mode;
- designing gravity receipts;
- writing the DM-facing body contract;
- testing the special rule for overturning apparent results;
- running the full validation gate (placement/fallout/agency/gravity/sandbox/usability/wiki);
- diagnosing or repairing a Resolution that narrates atmosphere without state change.

Read `references/resolution-types.md` when:

- selecting the aftermath pattern (Happy Ending, Villain Killed, Villain Escapes, etc.);
- combining patterns;
- applying sandbox consequence lenses (Ownership, Cost, Exposure, Relationship, Vacuum, Obligation, Pressure).

The references own Resolution semantics, leading-concept definitions, state-delta construction, PREP/COMPILE branch procedures, the body contract, validation gates, failure modes, and the special overturning rule. Keep those details there.

## Workflow

### 1. Load the authoritative situation

Search the compiled vault before designing the Resolution.

Find the smallest set of pages that establishes:

- the PCs involved and their established Gravity (goals, fears, commitments, relationships, unresolved history);
- the containing adventure, situation, or Beat Chart;
- its central dramatic question;
- the associated Climax and its outcome (if known);
- post-play evidence when compiling after a session;
- affected PC pages or the current player-gravity map;
- affected NPCs, factions, locations, items, or relationships;
- any existing template or schema governing this beat type.

Follow relevant `[[wikilinks]]` rather than reconstructing linked canon from memory. Do not assume that a formerly prepared consequence still applies — current canon wins.

**Complete when:** the central dramatic question is identified, whether its answer is known, every entity whose state materially changed is located, relevant player-gravity anchors are known, and the applicable beat-page schema has been identified.

### 2. Determine mode

If the Climax has not happened: **PREP**. Produce a consequence envelope.

If the Climax outcome is known: **COMPILE**. Produce the actual Resolution.

If evaluating an existing Resolution: **REVIEW**. Test against the validation gate.

If repairing a failed Resolution: **REVISE**. Change the minimum to pass every failed gate.

### 3. Establish the state delta

Compare the pre-Climax state with the post-Climax state (or plausible post-Climax states in PREP) across the dimensions in `references/resolution-beats.md`.

For every material delta, establish: **cause → new truth → visible evidence**.

**Complete when:** every material state change caused by the Climax is represented once, every change has a traceable cause, and no consequence exists merely to decorate the ending.

### 4. Build the Resolution

Follow the mode-specific branch in `references/resolution-beats.md`:

- **PREP:** identify outcome variables, prepare consequence rules, and build the Resolution Envelope.
- **COMPILE:** establish what actually happened from authoritative evidence, apply immediate fallout, and select the aftermath pattern from `references/resolution-types.md`.

**Complete when:** PREP delivers a consequence envelope a DM can apply after play, or COMPILE delivers actual fallout traceable to authoritative play evidence.

### 5. Pay gravity receipts

For every materially implicated player-gravity anchor, record the changed external circumstance.

State what happened to the world around the investment, not how the character feels about it.

**Complete when:** every relevant player investment receives its earned external consequence, and no PC's internal response is predetermined.

### 6. Write the vault note

Use the repository's current template and frontmatter schema. Consult `references/resolution-beats.md` for the body contract when the template leaves discretion.

Write for a human DM scanning during or immediately after play. Lead with the landing. Keep lore on its owning pages — use `[[wikilinks]]` or embeds rather than reproducing maintained information. The runnable body normally stays under 250 words.

**Complete when:** the DM can scan the Resolution, understand what became true, present its visible consequences, and identify what remains open without rereading the adventure.

### 7. Vault conformance

Instantiate from the beat template. Run `npm run lint -- <path>` and fix findings. Run the full validation gate from `references/resolution-beats.md`.

**Complete when:** the beat passes lint, conforms to its template, and every applicable validation gate passes.
