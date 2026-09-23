---
name: session-beats
description: >-
  Primary skill for planning a session, one-shot, adventure arc, or expedition
  evening. Composition: Beat Chart (Pondsmith's three rules and half-hour
  budget), opposition agenda, threads, escalation ladder, clues, PC
  spotlight, transitions, recompute, agency gates; hands each typed slot
  (Hook, Development, Cliffhanger, Climax, Resolution) to its type-beat
  skill. Does not stand-load type-card catalogs.
---

# Session beats

A Beat Chart scripts the session's **pacing**, not its outcomes (Mike
Pondsmith, *Scripting the Game*; transcription at
`RTG-Scripting-the-Game-v1.2-agent-readable (2).md` in the repo root). Each
beat is a chunk of play that informs, entertains, and pushes the plot
visibly forward; their order keeps tension up and the story legible. Prepare
pressures, factions, clues, places, offers, and hazards that can become
beats; let what the players do select which one fires next.

## Gates

Prep only. Follow `docs/agents/work.md` for Work protocol, invention, accept, and lifecycle.
Follow AGENTS.md **HARD: entity-before-spoken** and **HARD: dm-facing-explicit**.

## Boundary contract

### Input

Take a named session owner or session-plan request, the parent session
objective, and the bounded brief, thread map, and linked owner pages. When the
owner is a session plan, enter this skill directly; do not route through a
generic beat or orchestration skill.

### Owner-specific Work

Work only the named session plan: preserve its objective and live threads,
compose the Beat Chart, and apply the pacing, agency, transition, and
completion craft below. A typed beat request is a local fill, not permission to
replace the parent session objective.

### Capability Handoff

Typed slot → owning beat skill (`hook-beats`, `development-beats`,
`cliffhanger-beats`, `climax-beats`, `resolution-beats`) with session state,
slot type, planted threads, and trigger. Recompute the parent chart on return;
the child does not re-plan the session.

### Done

Session-plan artifact filed, objective preserved, typed beats linked, each
child slot resolved or explicitly blocked.

## The three chart rules

1. **Start with a Hook** — a short piece of action or suspense that pulls the
   players in. One per session.
2. **End on a Climax, then a Resolution.** The Climax is the finale; the
   Resolution is the tag line showing what the Climax changed.
3. **Alternate Developments and Cliffhangers** in the middle, never two of a
   kind in a row. Developments are non-action beats (clues, revelations,
   conversations, character turns); Cliffhangers are contests in doubt
   (chases, fights, perils). An action Hook starts the middle with a
   Development; a cerebral Hook with a Cliffhanger. An action Climax follows a
   Development; a cerebral Climax follows a Cliffhanger.

**Budget.** One beat ≈ thirty minutes of real time. Hook + Climax +
Resolution ≈ ninety minutes; divide the remaining time into alternating
Development/Cliffhanger slots. A six-hour night leaves four and a half hours
— about nine middle beats. The count is a ceiling, not a quota.

Why the rules hold: stacked fights numb — finishing one fight and walking into
another makes the table groan — and stacked introspection stalls. Each
Development makes the next Cliffhanger's stakes legible; each Cliffhanger
makes the next Development's information urgent.

## Plan a session

1. **Ground.** Read `hot.md`, the previous session's recap and final beat,
   the campaign hub's table aim, each PC page, and active threads, clocks,
   and factions (retrieve with `qmd`). Done when the ending state is stated as
   facts and each PC's current goal is named. Missing table aim → ask per
   AGENTS.md before treating the plan as aimed.
2. **Compass.** Write the opening situation, the immediate pressure, the
   session question, what happens if the party does nothing, and a
   one-sentence dramatic spine each beat approaches from a different angle.
3. **Opposition agenda.** Name the opposition (owner page), its goal for this
   session, its means, and what it does step by step if nobody interferes
   (the Pressure table, steps 0–4). Cliffhanger opposition comes from this
   agenda or from the environment.
4. **Threads.** Name three to five live threads — PC goals, faction clocks,
   mysteries, relationships under pressure, depleting resources — and for
   each, the beats that plant, test, and harvest it.
5. **Chart the beats.** Fill the Beat Map in play order. Each row: form,
   card (index below), thread, trigger, what changes, handoff, budget; each
   Cliffhanger and the Climax also get an escalation tier; each row names its
   memorable element. Add Floating Beats for situations that can fire
   wherever they fit, and Climax candidates when more than one confrontation
   could be earned.
6. **Escalation ladder.** Assign tiers so fights rise across the night:
   Grunts → Minions → Henchmen → Villain (monsters: Scare → Fright → Horror →
   Terror). The first contest is one the party wins unless they blunder; the
   Villain waits for the Climax. `cliffhanger-beats` owns the tier ratios;
   `encounter-prep` owns the 5e difficulty.
7. **Routes and clues.** Each conclusion or access the session cannot
   progress without gets three independent routes (Critical Routes). Write
   about ten Floating Clues as true, concrete facts, each revealable through
   more than one interaction.
8. **Spotlight.** Each PC gets at least one beat where their goal, bond, or
   fear drives the scene (PC Touchpoints), and a thread the Climax harvests.
9. **Cast and owners.** List every named actor, place, item, and creature the
   beats need. Mint missing owners first with their owner skills, one focused
   subtask per page type (AGENTS.md Focused minting).
10. **Fill the typed beats.** In chart order, hand each live slot to its type
    skill; each beat opens from the previous beat's carry-forward, so the Hook
    fills first. Every typed beat meets `docs/agents/table-ready.md`.
11. **Audit.** Run the beat-order audit below and a cold read of the plan: a
    DM who has never seen the prep can say, from the plan, what starts the
    night, what the opposition does next, and which beat is on deck.
12. **File.** Write the plan's DM copy with `writing-for-humans`, file the
    session plan (below), and link every typed beat.

## Filed session plan

After accept, file one session plan at `wiki/journal/sessions/<campaign-slug>/<session-number>/Session-<number>-00-<Title>.md` copied from `wiki/templates/session-plan.md` with `type: session-prep` and `kind: session-plan`. Its jobs: Compass, Beat Map, Floating Beats, Branches & Skips, Threads, Critical Routes, Pressure (opposition agenda), PC Touchpoints, Floating Clues, Session Toolkit, and links to every typed beat page. The plan leaves Scene ends when, Zones, and Be ready for to the beat pages and run-guide cockpits.

Done when: the plan answers those jobs, links every live beat, has `type: session-prep` and `kind: session-plan`, and a cold read of it passes.

## Composition craft

**Hook — reel in the line.** The Hook's job is to get the players involved
and moving at once; the Climax answers the question the Hook opened,
transformed by what the middle cost. Prefer an opening that grows from the
previous session's ending or an active PC goal; only this first beat recaps.

**Developments set direction; Cliffhangers test it.** Each Development is the
bump that reorients the party until the next one. Each Cliffhanger is a
contest in doubt that tests that direction and produces the changed state the
next Development interprets. Developments may chain (mentor → training →
truth); break the chain with a Cliffhanger so each piece is tested.

**Threads make a session.** Plant threads early, reveal new facets in
Developments, test them under cost in Cliffhangers, harvest them in the
Climax. A beat advancing no live thread is filler; a beat advancing an
abandoned thread is a railroad.

**Transitions are contracts.** Each beat's outcome rows are the next beat's
entry state: what changed, what the party committed to, what is now true. The
receiving beat inherits that world without teleporting past a live option,
dropping a planted thread, or contradicting what the party just lived through.

**Pressure mode.** Mystery hides information so players dig; surprise hides
the bomb until it goes off; suspense shows the bomb and the fuse. For
sustained tension install suspense: the threat visible enough to act on, the
fuse advancing without permission, the clean answer uncertain, every response
costing something.

**Earn the Climax.** Threads converge where the party's choices made one
confrontation inevitable — call it when they commit, not when the chart
reaches the slot. Recognition, early and avoided Climaxes, and simultaneous
candidates: [references/agency.md](references/agency.md) § Climax and
resolution tests.

**Show the aftermath.** One Resolution follows the Climax, scaled to it:
changed world, costs paid, each thread's final state, what the players want
next.

**Fair obstacles.** Traps and puzzles carry their clues in the scene or
earlier. Contests use transparent rolls. Betrayal and sabotage are detectable
before they are irreversible. Second Chance, Back from the Dead, and Heroes
Escape are rare, costly, and keep earlier consequences.

## Agency and recompute

Read [references/agency.md](references/agency.md) before charting and after
every beat in replanning. Session-level gates:

- Prepare situations and clocks, not required outcomes.
- Offer two or more meaningful options when the fiction supports them.
- Let players ignore a Development, fail a Cliffhanger, or pursue a goal they
  create; apply visible consequences and recompute.
- Let the chart shrink, branch, pause, or end early when the new state
  warrants it.
- Player-facing prose is a `theatre-of-the-mind` fill inside the typed beat
  page. Sites, routes, and decision graphs → `dungeon-design`. Retrieve canon
  with `qmd`; mark silent areas and file what the user makes canon. Never
  paste WotC proprietary text.

## Beat-order audit

Before filing, write `Hook → (D/C …) → Climax → Resolution` and check:

- **Polarity:** every transition alternates; the Climax prelude has the
  opposite type.
- **Threads:** every beat advances a live thread; the Climax harvests threads
  the middle planted; the Resolution shows their final state.
- **Escalation:** tiers rise across the night; the Climax is the top tier and
  highest cost.
- **Transitions:** each outcome row gives a visible trigger for the next
  beat — no teleports, time-skips, or forced options.
- **Spotlight:** every PC has a beat and a harvested thread.
- **Pacing:** the budget sums to the night's usable time with cushion for
  breaks and rules lookups.

## Card index

Card names for charting; each type skill's catalog holds the shapes.

| Form | Cards |
|---|---|
| Hook | Kidnapped · Coronet Blue · Play a Cliffhanger · Play a Development · Discovery · Crisis · Revelation · Murder · False Accusation · Looming Threat |
| Development | Warning · Hidden Weakness · Revelation · Advantage Revealed · Clue · Retreat · Hesitation · Mistaken Identity · Villain's Monologue · Secret Meeting · Personal Stake · Second Chance · Gain Mastery · Alliance · Betrayal · Sabotage · Foreshadowing · Not What It Seems · Strange Bedfellows · Turnabout · Romance · Lie Revealed · Hazardous Quest · Puzzle · Framed · Obsession · Back from the Dead · Rescuers · Vengeance |
| Cliffhanger | Chase · Pursuit · Race · Fist Fight · Dogfight · Confrontation · Duel · Battle · Monster · Ambush · Obstacles · Contest · Skirmish |
| Climax | Final Revelation · Final Battle · Sacrifice · Desperate Gambit · Reckoning · Siege · Negotiation Under Duress · Catastrophe · Trial · Betrayal Cascade |
| Resolution | Happy Ending · Villain Is Killed · Villain Surrenders · Villain Escapes · Heroes Captured · Heroes Escape · Ending Cliffhanger · Greater Threat |

## Typed fill

| Slot | Skill |
|---|---|
| Hook | `hook-beats` |
| Development | `development-beats` |
| Cliffhanger | `cliffhanger-beats` |
| Climax | `climax-beats` |
| Resolution | `resolution-beats` |

## Session ritual

**Pre-session (30–40 minutes):** review PC goals and abilities; confirm each
PC's spotlight beat; rehearse the strong start; skim the Floating Clues;
note a few names for improvised extras; keep a parachute — an off-chart
situation that fits anywhere. Prep only what is uncomfortable to improvise,
as modular pieces findable in under thirty seconds.

**In session:** keep clocks visible; give players useful roles (watcher,
caller, mapper, negotiator, recorder) when a procedure benefits. A recording
goes through `session-transcript-ingest` afterward; the transcript never
becomes the session plan.
