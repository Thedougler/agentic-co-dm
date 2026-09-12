---
name: writing-development-beats
description: >-
  Draft, revise, or audit a Development beat — the non-physical
  change-in-situation beat of a dramatic unit in a Campaign OS vault.
  Use when composing a new Development for a Beat Chart, when converting
  a clue, revelation, relationship, or opportunity into playable prep,
  or when repairing a Development that prescribes player actions, routes,
  or outcomes.
---

# Development Beats

Change the **situation**, not the players' choice about it.

A Development advances the campaign through information, relationships, capability, opportunity, warning, revelation, or changed circumstances — without requiring physical conflict. It gives the players something new to understand, value, exploit, fear, decide, or pursue. Think with four terms: **Gravity** (established character investment), **Delta** (what becomes different), **Surface** (meaningful ways players can engage), **Pressure** (what the world does without waiting). The GM prepares the irrigation; the players remain the water.

## Reference

Read `references/development-beats.md` when:

- selecting a Development pattern (information, relationship, pressure/reversal, access/capability);
- distinguishing a Development from a Cliffhanger-style Confrontation;
- repairing weak Gravity or a Surface that collapsed to one required route;
- placing the Beat in the Beat Chart's alternation rhythm;
- designing the DM-facing scan order or running the full quality test.

The reference owns Development semantics, all named patterns, the sandbox translation model, Surface design tests, beat-rhythm rules, the human-DM scan order, and the quality-gate checklist. Keep those details there.

## Workflow

### 1. Load the authoritative situation

Search the compiled vault before designing the Development.

Find the smallest set of pages that establishes:

- the PCs involved;
- their current goals, fears, commitments, relationships, unresolved history, or other established Gravity;
- the current location and active pressures;
- relevant factions, NPCs, threats, and prior consequences;
- the containing situation, narrative unit, or Beat Chart;
- the previous authored Beat and the expected downstream situation;
- any existing template or schema governing this beat type.

Follow relevant `[[wikilinks]]` rather than reconstructing linked canon from memory.

Treat the maintained vault as the source of truth for existing campaign facts. Prepared future events are hypotheses; played events become canon only through the repository's normal post-session evidence/ingest process.

**Complete when:** every fact the proposed Beat depends on has an authoritative source, the current situation is known, adjacent authored Beats are known when applicable, and at least one candidate Gravity anchor has been found or its absence has been explicitly established.

### 2. Define the Delta

Write one sentence describing the Beat's primary change — what becomes actionable after this Beat that was not actionable before it.

Prefer one dominant Delta. Secondary consequences may follow from it.

The Development must be capable of producing its Delta without requiring a physical fight. A conversation can be tense and consequential; when the scene becomes an uncertain contest of threats or coercive dominance, it belongs to a Cliffhanger. Consult `references/development-beats.md` for the full Development-versus-Cliffhanger distinction and the named pattern catalogue.

Player-initiated violence does not invalidate the prep. The human DM follows the fiction; actual play can turn a prepared Development into something else.

**Complete when:** the Delta is expressible in one sentence, changes the campaign state in a useful way, and does not depend on a predetermined player action or required physical conflict.

### 3. Anchor the Beat to Gravity

Record a **Link of Relevance** tying the Development to at least one established investment.

Use the strongest available anchor:

1. a PC's explicit goal, fear, oath, need, enemy, relationship, or backstory;
2. a commitment the party voluntarily made during play;
3. a consequence created by a previous player decision;
4. a relationship the players have repeatedly invested in;
5. an immediate problem the party has already chosen to engage.

Name the exact source page.

Example:

- **Link of Relevance:** [[Mara Venn]] — wants to learn what happened to her missing brother; the informant has seen his signet ring.

Use additional Gravity when it creates productive cross-pressure between characters, but one strong anchor is better than several weak ones.

Ground Gravity in evidence. Treat an inferred but unrecorded player preference as unknown rather than turning it into a rail.

When no meaningful established Gravity exists, return to the campaign state and find a better anchor before investing in detailed prep.

**Complete when:** the Link of Relevance identifies the character or party investment, explains why the Beat touches it, and points to its authoritative vault source.

### 4. Build the Surface

Prepare a situation the players can act upon.

Write actor behavior and consequences, not a script for the party: what is already true, what each important NPC wants and knows, what can change, what signs make the situation legible, what Pressure continues independently, and how relevant actors respond to plausible categories of player action.

Test the Surface against at least **two materially different engagement vectors** and a valid **delay/refusal/leave** vector. The vectors must not secretly collapse into the same required route. Consult `references/development-beats.md` for the full three-vector test and Surface design guidance.

Pressure keeps refusal meaningful without making refusal fake. The world may worsen, rivals may move, an opportunity may close — consequences of a living world, not punishments for declining the intended content.

**Complete when:** at least two distinct responses plus refusal/delay can produce fictionally coherent consequences, and none is required for the campaign to remain playable.

### 5. Place it in the Beat rhythm

Use the Beat Chart as pacing architecture. A Development commonly follows an action-heavy Hook or a Cliffhanger, and is a strong Beat immediately before an action-oriented Climax. Do not place two Development Beats consecutively on the same authored path. Consult `references/development-beats.md` for full rhythm rules and sandbox branching guidance.

Give the Development one or more plausible **Carry Forwards** — consequences, unresolved choices, or action opportunities produced by the fiction. Carry Forwards are not mandatory next scenes.

If the players bypass the Development, preserve the world's causal logic. Reuse its information, NPC, or pressure elsewhere only when the changed fiction naturally supports that reuse.

**Complete when:** the Beat has a valid place in the prepared rhythm, its Carry Forwards follow causally from its Delta, and campaign continuation does not depend on the party selecting one specific exit.

### 6. Write the vault note

Use the repository's current template and frontmatter schema as the source of truth. Do not cache or invent a competing schema inside this skill.

Preserve Obsidian compatibility:

- flat YAML frontmatter;
- `YYYY-MM-DD` dates where dates are required;
- YAML lists in block-list form;
- quoted wikilinks when a schema stores wikilinks in YAML;
- `[[wikilinks]]` for internal references;
- section embeds or other dynamic content when canonical content already lives elsewhere;
- standard Markdown rather than inline HTML.

Keep one fact in one authoritative place — link to NPC motives, location descriptions, faction rosters, or established lore rather than reproducing paragraph-length copies that can drift.

Optimize the top of the note for the DM running the table. Consult `references/development-beats.md` for the recommended scan order when the template leaves discretion.

Write preparation conditionally:

- `If the party tells Varo...`
- `Varo wants...`
- `The ledger can reveal...`
- `Unless interrupted, the courier leaves at dusk.`

Reserve factual past-tense assertions for circumstances already established in canon.

**Complete when:** the note conforms to the live repository schema, resolves internal links, remains DRY, exposes the playable core immediately, and clearly distinguishes established truth from conditional preparation.

### 7. Vault conformance

Instantiate from the beat template. Run `npm run lint -- <path>` and fix findings.

**Complete when:** the beat passes lint and conforms to its template.
