---
name: writing-narrative-islands
description: >-
  Situation authoring for sandbox campaigns in a Campaign OS repo (vault/ present).
  Use when creating or revising a Situation page, converting a linear plot or quest
  into player-driven sandbox architecture, connecting hooks/factions/locations/beats
  into an agency-preserving adventure graph, or auditing an existing island's agency
  and connectivity.
---

# Narrative Islands

Build **narrative islands**: bounded, causally live situations that give
players meaningful things to pursue without prescribing what they choose or
how those situations resolve.

The island owns **situation topology**: what is happening, who wants what,
why it matters, how it changes, how the PCs can engage, and what changes
afterward. The players choose the route.

The human DM is the runtime. Agents work around play: before play, maintain
canon and prepare fast, direct DM references; after play, reconstruct what
happened from noisy transcripts and update canon, state, and future
preparation.

## Method

The vault distinguishes three states:

- **True:** established canon or explicit DM ruling.
- **Possible:** prepared pressure, clues, options, or consequences.
- **Happened:** events established through play evidence.

Unused preparation has no authority over play. Improvisation that lands at
the table outranks unused prep.

Prepare situations, not plots. Write what the world pushes on the table;
leave the players' answer unwritten.

Legal prep: an NPC makes an offer; a faction searches for evidence; a storm
drives ships off course; a clue exists in three discoverable forms; an
ignored prisoner is moved, killed, rescued, or transformed by world logic.

Bad prep: the party accepts the offer; the players discover the evidence in
the intended room; the heroes defeat the assassin and recover the map; a
fork exists only to preserve a preferred route.

Seed broadly, observe play, identify attention, deepen selectively. Do not
expand a subject only because the agent finds it interesting.

Situations stay the default island. A Live Branches row on the Beat Chart
is legal only when the party's own choice or outcome creates materially
different future situations — the collapse test
(`.claude/skills/composing-beats/references/audits.md` § Branch collapse
test). If multiple outcomes reconverge with the same world state, collapse
them into one Beat.

## Core model

Think in an **archipelago**, not a plot chain. An island contains:

- a live **situation**;
- competing **forces** with independent goals;
- **gravity** that can attract the PCs;
- several **bridges** by which it can be discovered or approached;
- useful **affordances** rather than prescribed solutions;
- a **tide** that changes the situation when time passes or actors act;
- several possible **state changes**;
- a **wake** that propagates consequences into the wider campaign.

An island may be entered, ignored, abandoned, revisited, transformed,
destroyed, allied with, or accidentally collided with. Prepare what the
world **does**. Discover what the PCs **do** at the table.

## Workflow

For element catalogs and the full audit checklist, read
[`references/workflow-detail.md`](references/workflow-detail.md).

### 1. Load the current world

Search the compiled vault. Read the smallest set of current pages to
establish PC goals, active factions, unresolved hooks, relevant locations,
active clocks, and recent state changes. Every reused fact traces to current
canon; every new fact is identifiable as new DM preparation.

### 2. State the situation

Compress the island: **[Forces] want [incompatible things] in or around
[context] before [pressure matures].** Define the dramatic question. Test at
least three materially different plausible end states.

### 3. Establish gravity

Connect the island to existing PC goals, fears, loyalties, and interests.
Prefer multiple weak pulls over one compulsory hook. Engagement follows
naturally from things the PCs already value; declining the island remains a
legitimate campaign decision.

### 4. Build active forces

Give every load-bearing actor: want, reason, constraint, leverage, next
action, tell. Actors pursue their own goals rather than waiting for the
party. Every major force can advance the situation without PC involvement.

### 5. Build bridges

Prepare several materially different entry vectors (minimum two, three or
four is a strong default). Different bridges reveal different information,
risks, or advantages. Losing one bridge does not erase the island.

### 6. Prepare affordances

Record what PCs can manipulate: relationships, secrets, vulnerabilities,
resources, terrain, schedules, laws. Write what things **are** and what they
**can do**. Let players combine them into plans. If an obstacle has only one
answer, add another affordance or remove the gate.

### 7. Set the tide

Create the smallest useful progression of state changes for when PCs are
elsewhere. For each step: what causes advancement, what changes, what
evidence becomes visible, which opportunities appear or disappear.

### 8. Add candidate beats

Attach beats to triggers or states, not timestamps. Keep detailed beat
craft in the repository's dedicated beat workflows. Prepared beats help the
DM respond to likely dramatic states without becoming required scenes.

### 9. Define state changes

Prepare consequence logic, not endings. For each major objective, consider
relevant states and ask: which actors gain or lose leverage, what becomes
newly true or impossible, who learns about it, which relationships change,
which clocks advance or appear, which bridges open or close.

### 10. Write the wake

Propagate consequences through existing campaign structures: NPC
relationships, faction agendas, regional politics, resources, reputation,
other narrative islands. A normal island points toward more than one future
situation.

### 11. Write the vault page

Use the repository's situation template. Optimize for DM scanning:
front-load decisions and active pressure, use short bullets, keep motives
next to actors, keep consequences next to states, use headings as retrieval
targets, preserve specific names, numbers, and triggers.

### 12. Run the island audit

Test every island against the audit checklist in
[`references/workflow-detail.md`](references/workflow-detail.md): agency,
causality, activity, connectivity, character gravity, persistence, vault
integrity. Every question has a concrete answer in the page or current
canon.

## Cold opens

A cold open — a short frame where the table temporarily plays one NPC or NPC
group instead of their own PCs — is authored by `writing-cold-opens`. An
island that opens on one delegates the whole frame to that skill.

## Completion contract

A narrative island is complete only when:

1. its unresolved situation is explicit;
2. its active forces can operate independently;
3. player motivation comes from established gravity;
4. multiple bridges permit genuine approach variation;
5. affordances support unscripted solutions;
6. the tide changes the island when ignored;
7. candidate beats remain conditional;
8. multiple persistent states are possible;
9. consequences create a wake;
10. the vault page is concise, linked, DRY, and immediately usable by the DM.

The finished artifact makes the next session easier to **respond to**, not
easier to predict.

## Done check

Before handing back, state:

`NI: <situation premise + pressure + if-ignored change + table-open question>`

## References

| File | Read when |
|---|---|
| [`references/narrative-islands.md`](references/narrative-islands.md) | Converting linear adventures, designing connections, diagnosing railroading, auditing agency, repairing static islands |
| [`references/workflow-detail.md`](references/workflow-detail.md) | Building any step's element catalog, running the island audit |
