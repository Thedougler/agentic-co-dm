---
name: writing-cliffhanger-beats
description: >-
  Cliffhanger beats — the action-oriented contest-or-peril beat of a
  Campaign OS Beat Chart. Use when a Development must hand into immediate
  danger, when encounter prep needs an agency, escalation, or handoff
  audit, or when a Cliffhanger prescribes player actions instead of
  preparing a responsive situation with open vectors.
---

# Cliffhanger Beats

Put **pressure in motion**, not a screenplay of player actions.

A Cliffhanger advances the campaign through an uncertain physical or coercive contest — chase, pursuit, battle, ambush, confrontation, hazard, or peril — whose outcome remains open through play. It is the *Scripting the Game* action-oriented beat. Think with seven terms: **Gravity** (why the characters already care), **Ignition** (what makes danger immediate now), **Pressure** (what active force makes inaction costly), **Vectors** (materially different ways players can engage), **Escalation** (how the situation worsens while unresolved), **Fallout** (how the world changes according to what happens), **Handoff** (the changed state from which a Development can emerge). The GM prepares the irrigation; the players remain the water.

## Reference

Read `references/cliffhanger-beats.md` when:

- distinguishing a Cliffhanger from a Development, Climax, or Resolution;
- designing opposition (intent + means + limits model);
- calibrating threat for credible uncertainty;
- building sandbox continuity after bypass, premature victory, or sequence drift;
- writing the DM-facing body contract or runtime payload;
- repairing a quality-gate failure;
- running a revision or review protocol.

Read `references/cliffhanger-patterns.md` when:

- selecting or classifying a pressure pattern (Chase, Pursuit, Race, Battle, Ambush, Confrontation, etc.);
- reviewing pattern-specific design checks or boundary cases.

The references own Cliffhanger semantics, all named patterns, core principles, opposition design, threat calibration, sandbox continuity, the runtime payload, the DM-facing body contract, revision/review protocols, classification routing, and the quality-gate checklist. Keep those details there.

## Workflow

### 1. Load the authoritative situation

Search the compiled vault before designing the Cliffhanger.

Find the smallest set of pages that establishes:

- the PCs involved;
- their current goals, fears, commitments, relationships, unresolved history, or other established Gravity;
- the current location and active pressures;
- relevant factions, NPCs, threats, and prior consequences;
- the containing situation, narrative unit, or Beat Chart;
- the previous authored Beat and the expected downstream situation;
- any existing template or schema governing this beat type.

Follow relevant `[[wikilinks]]` rather than reconstructing linked canon from memory.

Confirm that a Cliffhanger belongs in this slot: Development and Cliffhanger alternate; a previous Cliffhanger normally means this slot needs Development. When play has already changed the sequence, re-evaluate from the new state.

**Complete when:** every fact the proposed Beat depends on has an authoritative source, the current situation is known, adjacent authored Beats are known when applicable, and the slot is correctly classified as Cliffhanger.

### 2. Anchor to Gravity

Record a **Link of Relevance** tying the Cliffhanger to at least one established investment.

Use the strongest available anchor:

1. a PC's explicit goal, fear, oath, need, enemy, relationship, or backstory;
2. a commitment the party voluntarily made during play;
3. a consequence created by a previous player decision;
4. a relationship the players have repeatedly invested in.

Name the exact source page.

Weak:

> The party should stop the assassins because they are dangerous.

Strong:

> The assassins are hunting [[Ser Caldus]], the witness Mara promised to get safely to trial.

If no authentic Link of Relevance survives retrieval, change the Cliffhanger rather than inventing attachment.

**Complete when:** at least one established player investment makes engagement, avoidance, or consequence meaningful.

### 3. Choose the pressure pattern

Consult `references/cliffhanger-patterns.md`.

Choose the pattern that describes the **pressure**, not merely the scenery. A fight on horseback may still be a Race if reaching the bridge first determines the outcome. A dragon encounter may be a Pursuit if survival depends on escaping it.

Combine patterns only when both remain operationally useful to the DM.

**Complete when:** one primary pattern explains how pressure operates and any secondary pattern adds distinct runtime value.

### 4. Build the situation

Prepare three pieces:

**Ignition** — the event that turns potential danger into immediate action. Start as late as practical. Prefer pressures already in motion. Consult `references/cliffhanger-beats.md` for the full Ignition catalogue.

**Pressure** — the active force driving the danger: what it wants, what it can do, what constrains it, what happens if the PCs do nothing. Pressure advances without waiting politely. Consult `references/cliffhanger-beats.md` for pressure fields and opposition design.

**Vectors** — at least three materially different approach vectors the fiction supports. These are diagnostics for the DM, not a menu for players. Apply the Water test: if the prep depends on the PCs choosing the "intended" solution, redesign the pressure.

**Complete when:** the DM can begin the Cliffhanger with a concrete change that demands response, can answer "what happens if they hesitate?", and at least three credible approaches exist without any predetermined decision embedded.

### 5. Design escalation and consequences

**Escalation** — a short ladder of 2–4 state-change thresholds, not a round-by-round script. Later thresholds commit stronger opposition, deteriorate the environment, or approach irreversible consequence. The DM can skip, accelerate, or replace thresholds. Consult `references/cliffhanger-beats.md` for escalation dimensions.

**Fallout** — cover four result classes: success, complication, setback, and bypass. Each alters at least one meaningful campaign state. Where a result merely says "the PCs continue," the Cliffhanger has failed to matter.

**Handoff** — identify what becomes newly available for the next Development. Phrase as state, not scheduled scene.

Weak:

> After winning, the PCs interrogate the captain.

Strong:

> Captain Vey may be captured alive; she knows who paid for the attack.

**Complete when:** continued failure predictably increases danger, all four fallout classes produce intelligible world states, and at least one likely result naturally supports a Development without dictating the PCs' next action.

### 6. Write the vault note

Use the repository's current template and frontmatter schema as the source of truth.

Preserve Obsidian compatibility: flat YAML frontmatter, `YYYY-MM-DD` dates, block-list form, quoted wikilinks in YAML, `[[wikilinks]]` for internal references, section embeds for canonical content, standard Markdown.

Keep one fact in one authoritative place — link to NPC motives, location descriptions, faction rosters, or established lore rather than reproducing copies that can drift.

Optimize the top of the note for the DM running the table: what is happening, why it matters, what the active force wants, immediate danger, escalation, consequences. Consult `references/cliffhanger-beats.md` for the body contract and runtime compression guidance.

**Complete when:** the note conforms to the live repository schema, resolves internal links, remains DRY, exposes the playable core immediately, and clearly distinguishes established truth from conditional preparation.

### 7. Vault conformance

Instantiate from the beat template. Run `npm run lint -- <path>` and fix findings.

**Complete when:** the beat passes lint and conforms to its template.
