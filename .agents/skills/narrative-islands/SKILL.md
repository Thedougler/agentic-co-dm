---
name: narrative-islands
description: >-
  Situation topology for sandbox play — forces, gravity, bridges, tide,
  wake. Use when creating or revising a type: front, quest, or encounter (choose the existing owner) page, converting
  a linear plot into a playable island, or auditing agency and
  connectivity. Night-only pressure stays a session-plan section.
---

# Narrative Islands

## Work gate

Prep only. Follow `docs/agents/work.md`. Load `wiki/AGENTS.md`, `copy-writer`, and `obsidian-markdown` on every vault write.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

Remap durable output paths from `campaigns/<slug>/` to `wiki/`; use `wiki/templates/`. Replace knowledge-bank wording with wiki wording. Keep the craft procedure.

Build **narrative islands**: bounded, causally live situations that give
players meaningful things to pursue without prescribing the route.

**Island** is the method. The page is `type: front, quest, or encounter (choose the existing owner)` when another
page, a future session, or a Beat Chart must refer to this topology as
a node. A night-only pressure stays a session-plan Situations section.
There is no `type: narrative-island`; use the nearest existing `type` and template.

The island owns **situation topology**: what is happening, who wants
what, why it matters, how it changes, how the PCs can engage, and what
changes afterward. The players choose the route.

## Method

Three states:

- **True:** established canon or explicit DM ruling.
- **Possible:** prepared pressure, clues, options, or consequences.
- **Happened:** events established through play evidence.

Unused preparation has no authority over play. Improvisation that lands
at the table outranks unused prep.

Legal prep: an NPC makes an offer; a faction searches; a storm drives
ships off course; a clue exists in three discoverable forms.

Seed broadly, observe play, identify attention, deepen selectively.

A Live Branches row on the Beat Chart is legal only when the party's
own choice creates materially different future situations — the collapse
test in `session-beats/references/audits.md`. If outcomes
reconverge, collapse them into one beat.

## Core model

Think in an **archipelago**, not a plot chain. An island contains:

- a live **situation**
- competing **forces** with independent goals
- **gravity** that can attract the PCs
- several **bridges**
- useful **affordances**
- a **tide** that changes the situation when ignored
- several possible **state changes**
- a **wake** into the wider campaign

Prepare what the world **does**. Discover what the PCs **do** at the table.

## Threat-in-motion gate

When an island is meant to carry suspense, reveal a bad thing already moving
without revealing the whole picture. Show its fuse and make waiting unsafe;
hide the clean answer, not the problem; attach a real cost to every route; then
leave the players free to act, including with an unplanned clever solution.
Mystery hides information for digging, while surprise withholds the bomb; do not
use either as a substitute for a visible pressure point. A threat is not live if
factions pause for shopping or rest.

**Complete when:** the threat, early tell, fuse, unknown clean answer, delay
change, costs, and at least three materially different response paths are
written, with a playable partial success.

## Workflow

Element catalogs and the audit: `references/workflow-detail.md`.

### 1. Load the current world

Search the compiled vault. Read the smallest set of pages for PC goals,
active factions, unresolved hooks, locations, clocks, and recent state
changes.

**Complete when** every reused fact traces to current canon and every
new fact is identifiable as new prep.

### 2. State the situation

**[Forces] want [incompatible things] in or around [context] before
[pressure matures].** Define the dramatic question. Test at least three
materially different end states.

**Complete when** the sentence names incompatible wants, a threat already
in motion, and a maturing pressure/fuse.

### 3. Establish gravity

Connect to existing PC goals, fears, loyalties, and interests. Prefer
multiple weak pulls over one compulsory hook. Declining remains
legitimate.

**Complete when** engagement follows from things the PCs already value.

### 4. Build active forces

Every load-bearing actor: want, reason, constraint, leverage, next
action, tell. Every major force can advance the situation without the
party; shopping, travel, or rest does not pause its plan.

**Complete when** no load-bearing actor waits politely for the PCs.

### 5. Build bridges

At least two materially different entry vectors (three or four is
strong). Losing one bridge does not erase the island.

**Complete when** two bridges remain after any one is lost.

### 6. Prepare affordances

What PCs can manipulate **in this situation**. Durable physical logic
belongs on the spatial page — invoke `place-design` when the place
cannot be run. If an obstacle has only one answer, add an affordance
or remove the gate.

**Complete when** unscripted combinations can change the situation.

### 7. Set the tide

The smallest useful progression for when PCs are elsewhere. Treat it as
the fuse: for each step record cause, what changes, visible evidence, what
opens or closes, and the cost of delay.

**Complete when** ignoring the island still changes the world.

### 8. Add candidate beats

Attach beats to triggers or states, not timestamps. Delegate craft to
`session-beats` and the `writing-*-beats` skills.

**Complete when** candidate beats remain conditional.

### 9. Define state changes

Consequence logic, not endings. Who gains leverage, what becomes true
or impossible, who learns, which clocks and bridges change.

**Complete when** more than one persistent state is possible.

### 10. Write the wake

Propagate into NPCs, factions, other situations, reputation.

**Complete when** the island points toward more than one future situation.

### 11. Write the page

Mint `type: front, quest, or encounter (choose the existing owner)` from `templates/Session prep.md or the nearest existing campaign note template`
when the threshold is met. Otherwise write the same topology into the
session-plan Situations section. If a place the island occupies is
missing or unplayable, invoke `place-design` first — or
`dungeon-design` when it is a multi-room dungeon complex. If a notable
object must be cited as a node and has no page, invoke `dnd-5e-magic-item-design`.
If a named conveyance must be cited as a node and has no page, invoke
`vehicle-design`. If a node exists but has no presence, invoke
`flesh-out`.

List playable `type: location` sites in a `locations:` property when the existing template supports it; wikilink other spatial notes in the body.

**Complete when** a DM can scan the page and run the situation.

### 12. Run the island audit

`references/workflow-detail.md`: agency, causality, activity,
connectivity, gravity, persistence, vault integrity.

**Complete when** every audit question has a concrete answer in the
page or current canon.

## Cold opens

A cold open is authored by `cold-opens`. An island that opens
on one delegates the whole frame to that skill.

## Done check

`NI: <situation premise + pressure + if-ignored change + table-open question>`

## GM-prep gates

A situation is a toolbox of actors, locations, motivations, and pressures in
tension, not a screenplay. Prepare only the uncertain pieces: a skeleton of
states, modular clues, likely hiccups, and a few independent moves. Keep secrets
floating across multiple clue vectors rather than assigning each to one room.
Before play, check that each PC has at least one possible limelight connection,
that the opening is purposeful, and that a parachute situation exists if the
party leaves the prepared area. Keep the page atomic and link its nearest
Organizer-owned hub/MOC.

## References

| File | Read when |
|---|---|
| `references/narrative-islands.md` | Converting linear adventures, diagnosing rails, repairing static islands |
| `references/workflow-detail.md` | Element catalogs, island audit |

## Eruptible-conflict gate

Make each island able to erupt without a scripted trigger: competing actors keep
moving, pressure has visible tells, and a PC arrival, choice, or silence can
collide with the current state. Consequences of inaction should be real but
legible. Let strongholds, routes, and relationships create political leverage,
and keep at least one interruptible off-ramp for an unexpected approach.
