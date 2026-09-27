---
name: narrative-islands
description: >-
  Quest-page situation topology. Primary for writing, editing, or creating a
  named `type: quest` page from `wiki/templates/quest.md`; also use to convert
  a linear plot into a playable situation or audit agency and connectivity.
  Beat charts stay with `session-beats`; typed beats stay with their beat skill.
---

# Narrative Islands
## Boundary contract

### Input

Take a named quest owner, the caller's objective, the relevant brief,
`wiki/templates/quest.md`, and current canon/evidence for its forces, places,
leads, clocks, and recent play. The owner is a live situation page, not a beat
chart or a scripted episode.

### Owner-specific Work

Work only the quest topology: preserve True/Possible/Happened status, independent
world motion, agency, routes, stakes, and walk-away consequences. Fill the quest
template through the situation workflow below; do not absorb typed beats,
encounter math, or another entity's page.

### Capability Handoff

Encounter math → `encounter-prep`. Multi-room site → `dungeon-design`. Place
→ `place-design`. Named entity → its owner skill.

### Done

Every item in `## Done` below holds, checked by its written audit.
Completion is observable when the named quest path, template/situation
contract, agency and connectivity checks, and any child return evidence are
reported.


Build named quest pages as live situations: forces act, pressure advances, and
the party chooses the route. Campaign situation pages use `type: quest`.

## Work Gate

Prep only. Follow `docs/agents/work.md`. Follow AGENTS.md **HARD:
entity-before-spoken** and **HARD: dm-facing-explicit**. Cast and invent per
`docs/agents/table-ready.md` § Cast before minting and § Fill the silence.

- **Canon.** User-said facts file immediately on the live path. Whatever the
  quest needs that canon leaves silent, records as unknown, or contradicts,
  decide now as canon under the rule in `llm-wiki`: one concrete answer (what
  the hidden thing truly is, what the driver does next and when), stated on
  the page as world fact, with the page marked `invention: true`. The response
  lists each proposal with the `[[pages]]` it grows from and names any
  contradiction it settles, so the DM picks the winner.
- **Explicit DM layer.** Situation, Pressure, and Complications state the
  truth by name: what is really happening, who acts next and when, and what
  each portent and reversal turns out to be. "Unclear", "may", "for play to
  establish", and lists of possibilities are silence left unfilled. The
  player-facing narration withholds from players, never from the DM.
- **Process stays off the page.** Provenance, contradictions, and the proposal
  list live in the response.

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

### 3. Fill At a Glance

Copy `wiki/templates/quest.md` and fill At a Glance and the frontmatter:

- **Lead sentence:** the result the party could accomplish, not the method.
- **Why now:** the pressure, opportunity, or danger that makes delay matter.
- **Deadline:** a date or the fictional event after which the situation
  changes, when one exists.
- **Opposition:** who wants a different outcome, and what they want instead.
- **Narration** (beside At a Glance): the player-facing brief, from what the characters know.

Complete when: objective and why now are explicit, and a deadline appears
only when the situation has one.

### 4. Write the Situation

Write the unstable present: what is really happening, the forces involved, and
what each is already doing. What the party knows lives in the narration beside At a Glance.
Do not prescribe the party's next action.

Complete when: a DM can explain the current tension, involved forces, and
visible hook without reading a plotted sequence.

### 5. Write the Stakes

Fill success, failure, and walk-away, and the **Open question** bullet: who
might change sides, survive, fall, or gain power, left for play to decide. The walk-away
entry names what continues without the party.

Complete when: success, failure, and walk-away each change the world
materially, and at least one question remains open for play.

### 6. Set the Pressure

Name the driver, what it wants, its current move, its next move if
uninterrupted, and the end state if it gets what it wants. Progress portents are
observable changes, not hidden bookkeeping. Portents advance on the driver's
timeline — early arrival sees an earlier state than late arrival. If the prompt
ties escalation only to party presence or arrival, convert it to an independent
timeline the driver controls.

Complete when: the driver and uninterrupted next move are concrete enough for
the DM to advance the quest without `world-tick`, and portents produce a
different situation depending on when the party engages. `world-tick` does not
advance quest portents.

### 7. Build Leads

Write at least two independent leads, each a checkbox the DM ticks when the
party finds it. Each lead points to useful progress from
a different source, vector, or location. Losing one lead does not erase the
quest. If the prompt prescribes a single approach, open alternatives — the
prompt describes a possible route, not the only route.

Complete when: the party has at least two independent routes, no required
sequence of actions, and no single method (combat, stealth, negotiation) is
the only viable path.

### 8. Fill Support Sections

Add Complications (a tradeoff, a reaction when the party interferes, a
reversal and where it is found), Rewards (what play can earn beyond the promise), and Connections (each
person, faction, place, or thing by link, with its role in the quest) only
when they help the DM run the quest. Link detailed owners instead of restating
them.

Complete when: every filled row helps the DM run, update, or adjudicate the
quest.

### 9. Handle Resolution

Omit `## Resolution` while the quest is unresolved. Add it only when play or DM
ruling creates a stable outcome: resolved, failed, expired, or transformed.
State what actually happened, who gained or lost power, the lasting change to
each linked page, and the loose threads.

Complete when: unresolved quests have no Resolution section, and resolved
quests record what actually happened plus lasting world changes and loose
threads.

### 10. Update an Existing Quest

After meaningful play, downtime, rolls, or DM ruling:

- Change `status`, `last_advanced`, and `updated` when needed.
- Rewrite Situation to the new present.
- Advance, alter, or cancel the Pressure driver and portents.
- Update found, invalidated, or new leads.
- Update changed connections and rewards.
- Add one Log bullet.

Complete when: the page reflects the current playable situation and the Log
records what changed.

### 11. Audit the Page

Use `references/workflow-detail.md` for agency, causality, activity,
connectivity, gravity, persistence, and vault integrity.

Complete when: a DM can run the situation, name the walk-away consequence, and
point to at least two independent leads.

## Hard Gates

- Mint `type: quest` only.
- Retired campaign situations are quests; do not mint `type: front` or
  `type: encounter`.
- Night-only pressure stays in the session plan unless it needs a named quest
  page.
- Reject anti-patterns from the prompt, not just in the audit. If the prompt
  prescribes a frozen island (escalation paused until party arrives), a single
  approach (only one method works), or a keyhole island (one chokepoint gates
  all progress), convert it: give the world its own timeline, open alternative
  routes, and add redundant bridges. The prompt describes the DM's intent; the
  quest page must be playable.

## Done

- The quest frame sentence names incompatible wants, the live pressure, and
  what changes if nobody interrupts.
- At a Glance names the objective, why now, the Opposition and what it wants
  instead, and the reward; the narration came from `theatre-of-the-mind` and
  holds no secret or unearned name.
- Every question, portent, and reversal the page raises has its DM answer on
  the page; the driver's next move has a time or trigger.
- Stakes cover success, failure, walk-away, and an Open question; at least two
  independent leads are checkboxes pointing to different pages.
- Every owner was cast or minted first. Each new mint names, in the response,
  the candidates considered and why none fit.
- User-said canon is filed; every invention is canon under the rule in
  `llm-wiki`, marked on the page and listed in the response.
- Every page filed passes the world-voice search (`docs/agents/table-ready.md`
  § Fill the silence).
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.

Finish with a written audit in working notes: each Done item beside the page
line that satisfies it; fix the page where none does.

## References

| File | Read when |
|---|---|
| `references/narrative-islands.md` | Converting linear adventures, diagnosing rails, repairing static situations |
| `references/workflow-detail.md` | Element catalogs, island audit |
