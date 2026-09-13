---
name: narrative-islands
description: >-
  Quest-page situation topology. Primary for writing, editing, or creating a
  named `type: quest` page from `wiki/templates/quest.md`; also use to convert
  a linear plot into a playable situation or audit agency and connectivity.
  Beat charts stay with `session-beats`; typed beats stay with their beat skill.
---

# Narrative Islands

Build named quest pages as live situations: forces act, pressure advances, and
the party chooses the route. Campaign situation pages use `type: quest`.

## Work Gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept. Reject
leaves no page. Invention is required when the wiki lacks the fact: set
`invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]`
for wiki claims. Show the DM any contradiction with an existing page. Never
present invention as a wiki fact. Never write silent canon. A craft `type`
becomes `canon` only after DM accept.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention is
flagged, and grounding is named.

## Ownership

This skill is primary for write, edit, or create jobs on a named quest page.
Use `wiki/templates/quest.md` and fill `type: quest`.

Retarget composition work:

- Beat Chart or session plan structure: `session-beats`.
- Typed beat page or typed beat prose: the matching beat skill.
- Fight math inside a quest: `encounter-prep`.
- Missing or unplayable place: `place-design`; use `dungeon-design` for a
  multi-room dungeon complex.
- Named item, vehicle, spell, faction, lore, city, or region node: its owner.

There is no `quest-design` skill. This skill owns quests.

## Craft Basis

Use node-based and clue-rich prep: Justin Alexander's node and clue guidance,
Sly Flourish's secrets-and-clues prep, and Robin D. Laws's attention to turns of
pressure all point to the same outcome here: prepare actionable information,
several routes, and moving forces instead of a required sequence.

## Quest Method

Three states:

- **True:** established canon or explicit DM ruling.
- **Possible:** prepared pressure, leads, options, or consequences.
- **Happened:** events established through play evidence.

Unused preparation has no authority over play. Improvisation that lands at the
table outranks unused prep.

Write what the world does. Discover what the PCs do at the table.

## Workflow

Element catalogs and the audit live in `references/workflow-detail.md`.

### 1. Load the Current World

Search the compiled vault. Read the smallest set of pages for PC goals, active
factions, unresolved hooks, locations, clocks, and recent state changes.

Complete when: every reused fact traces to current canon and every new fact is
identifiable as new prep.

### 2. Choose the Quest Frame

Name the unstable situation in one sentence:

`[Forces] want [incompatible things] in or around [context] before [deadline or pressure matures].`

Define the table question the quest exists to answer. Keep the page about a
pursuable situation, not a scripted episode.

Complete when: the sentence names incompatible wants, the live pressure, and
what can change if nobody interrupts it.

### 3. Fill the Summary

Fill the summary callout and frontmatter fields from `wiki/templates/quest.md`:

- **Objective:** the result the party could accomplish, not the method.
- **Why now:** the pressure, opportunity, or danger that makes delay matter.
- **Deadline:** none, a date, or the fictional event after which the situation
  changes.

Complete when: objective, why now, and deadline are all explicit.

### 4. Write the Situation

Write the unstable present. Include what the party knows and what is really
happening. Do not prescribe the party's next action.

Complete when: a DM can explain the current tension, involved forces, and
visible hook without reading a plotted sequence.

### 5. Write the Stakes

Fill success, failure, walk-away, and play-to-find-out questions. The walk-away
entry names what continues without the party.

Complete when: success, failure, and walk-away each change the world
materially, and at least one question remains open for play.

### 6. Set World in Motion

Name the driver, what it wants, its current move, its next move if
uninterrupted, and the end state if it gets what it wants. Progress portents are
observable changes, not hidden bookkeeping.

Complete when: the driver and uninterrupted next move are concrete enough for
the DM to advance the quest without `world-tick`. `world-tick` does not advance
quest portents.

### 7. Build Leads and Routes

Write at least two independent leads. Each lead points to useful progress from
a different source, vector, or location. Losing one lead does not erase the
quest.

Complete when: the party has at least two independent routes and no required
sequence of actions.

### 8. Fill Support Sections

Add only table-useful rows under People & factions, Relevant places, Useful
things, Complications, and Rewards & consequences. Link detailed owners instead
of restating them.

Complete when: every filled row helps the DM run, update, or adjudicate the
quest.

### 9. Handle Resolution

Omit `## Resolution` while the quest is unresolved. Add it only when play or DM
ruling creates a stable outcome: resolved, failed, expired, or transformed.

Complete when: unresolved quests have no Resolution section, and resolved
quests record what actually happened plus lasting world changes and loose
threads.

### 10. Update an Existing Quest

After meaningful play, downtime, rolls, or DM ruling:

- Change `status`, `last_advanced`, and `updated` when needed.
- Rewrite Situation to the new present.
- Advance, alter, or cancel World in motion and portents.
- Update found, invalidated, or new leads.
- Update changed people, factions, places, rewards, fallout, and complications.
- Add one Quest log row.

Complete when: the page reflects the current playable situation and the Quest
log records what changed.

### 11. Audit the Page

Use `references/workflow-detail.md` for agency, causality, activity,
connectivity, gravity, persistence, and vault integrity.

Complete when: a DM can run the situation, name the walk-away consequence, and
point to at least two independent leads.

## Hard Gates

- Mint `type: quest` only.
- Retired campaign situations are quests; do not mint `type: front` or
  `type: encounter`.
- Do not create or invoke a `quest-design` skill.
- Night-only pressure stays in the session plan unless it needs a named quest
  page.

## Done Check

`NI: <objective + why now + deadline + walk-away + driver next move + two independent leads>`

## References

| File | Read when |
|---|---|
| `references/narrative-islands.md` | Converting linear adventures, diagnosing rails, repairing static situations |
| `references/workflow-detail.md` | Element catalogs, island audit |
