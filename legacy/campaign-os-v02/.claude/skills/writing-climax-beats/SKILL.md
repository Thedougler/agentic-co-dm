---
name: writing-climax-beats
description: >-
  Draft, revise, or audit a Climax beat — the decisive convergence beat of a
  dramatic unit in a Campaign OS vault. Use when composing a new Climax for
  a Beat Chart, when the central dramatic question is ready to be answered
  through play, when an existing Climax prescribes player routes or outcomes,
  or when auditing a Climax against the earned-play, agency, pressure, and
  resolution gates.
---

# Climax Beats

Create a **convergence**, not a predetermined ending.

A Climax is the decisive Beat of the current situation — it answers the central dramatic question through play. Only a Resolution follows it. The GM prepares the **irrigation**: pressure, actors, objectives, terrain, leverage, consequences, and things already in motion. The players remain the **water**: their route and the resulting outcome belong to them.

Use **convergence** as the governing concept: independent threads from prior play becoming simultaneously relevant to one decisive situation, where established player investments, opposition, and consequences come together without scripting the players' route or outcome.

## Reference

Read `references/climax-beats.md` when:

- building the active pressure engine, escalation triggers, or decision handles;
- designing outcome dimensions and the consequence lattice;
- writing the DM-facing body contract;
- running the full validation gate (climax/gravity/agency/earned-play/pressure/resolution/vault);
- diagnosing or repairing a Climax that has become a predetermined finale.

Read `references/climax-modes.md` when:

- choosing among Final Battle, Final Revelation, or Convergent Climax;
- building mode-specific pressure components;
- translating a mode's failure patterns into sandbox-safe prep.

The references own Climax semantics, leading-concept definitions, pressure-component vocabulary, handle design, escalation-trigger construction, outcome-dimension guidance, the body contract, validation gates, and failure modes. Keep those details there.

## Workflow

### 1. Load the authoritative situation

Search the compiled vault before designing the Climax.

Find the smallest set of pages that establishes:

- the PCs involved and their established Gravity (goals, fears, commitments, relationships, unresolved history);
- the current situation, arc, adventure, or Beat Chart;
- the Beat immediately preceding this Climax;
- active NPCs, factions, fronts, clocks, and other forces;
- relevant locations and environmental conditions;
- discoveries, clues, weaknesses, alliances, resources, debts, injuries, promises, betrayals, and choices established by earlier play;
- consequences already in motion;
- any existing template or schema governing this beat type.

Follow relevant `[[wikilinks]]` rather than reconstructing linked canon from memory. Do not assume that a formerly planned antagonist, ally, objective, or solution still occupies that role — current canon wins.

**Complete when:** every actor and campaign fact on which the Climax depends has been verified against its current source-of-truth page, and the applicable beat-page schema has been identified.

### 2. Establish the Climax boundary

Identify the **single situation** this Beat is capable of deciding.

State:

- the unresolved dramatic question;
- what force currently prevents an easy answer;
- what meaningful state can change here;
- why this situation is ready to become decisive now.

The question must describe an uncertainty rather than predict an outcome. If the material still principally needs investigation, travel, recruitment, setup, or another intermediate confrontation, it is not ready for a Climax — route it to the appropriate Development or Cliffhanger.

**Complete when:** one unresolved dramatic question can be answered through the forthcoming play, and answering it will create fallout suitable for a Resolution.

### 3. Anchor to player Gravity

For every PC with a meaningful connection to the situation, identify the established investment that gives the Climax personal force.

Record a **Link of Relevance** for each:

`[[Character]] — established investment → how the live Climax presses on it`

Prefer **causal spotlight** over decorative spotlight — earlier play creating present consequence, not mere recognition.

**Complete when:** every prepared personal stake traces to something already established for that character, and every major prepared element has at least one clear reason to matter to the party.

### 4. Harvest earned setup

Search prior campaign state for anything that should matter now.

For every relevant setup, classify as: **edge**, **liability**, **relationship**, **knowledge**, **resource**, or **consequence**.

Make these things **actionable** — a payoff changes the present decision space rather than merely being mentioned.

**Complete when:** every relevant prior setup discovered during retrieval has an explicit disposition — either made materially usable in this Climax or intentionally carried forward.

### 5. Build the active situation

Choose a Climax mode from `references/climax-modes.md` (Final Battle, Final Revelation, or Convergent Climax) based on the dramatic mechanism.

Then build the pressure engine. Consult `references/climax-beats.md` for the full pressure-component vocabulary, handle design, escalation-trigger construction, and outcome-dimension guidance.

Define: the opposition objective, their immediate action, the no-intervention trajectory, active pressure, and the Threshold.

Prepare at least **two independent handles**. Prepare **escalation triggers** (When/Then/Because) that react to fictional state changes, never to prescribed player choices. Define **outcome dimensions** and their causal consequences without predetermining endings.

**Complete when:** the GM can answer "What happens if the party waits?" without inventing a new plot beat, any one handle can be removed and the situation stays playable, every escalation follows fictional state changes, and more than one coherent post-Climax state is possible.

### 6. Write the vault note

Use the repository's current template and frontmatter schema. Consult `references/climax-beats.md` for the body contract when the template leaves discretion.

Write for a human DM running the table. Lead with the situation. Keep lore on its owning pages — use `[[wikilinks]]` or embeds rather than reproducing maintained information. Write preparation conditionally; reserve past-tense assertions for established canon.

**Complete when:** the DM can run the situation from this page while opening linked pages only for detail, and the page contains no duplicated source-of-truth material.

### 7. Vault conformance

Instantiate from the beat template. Run `npm run lint -- <path>` and fix findings. Run the full validation gate from `references/climax-beats.md`.

**Complete when:** the beat passes lint, conforms to its template, and every applicable validation gate passes.
