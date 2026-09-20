---
name: session-beats
description: >-
  Primary skill for planning a session, one-shot, adventure arc, or expedition
  evening. Composition only: Beat Chart assembly, thread map, polarity,
  escalation, transitions, recompute, agency gates. Typed fill (Hook,
  Development, Cliffhanger, Climax, Resolution) is pointed at the five
  type-beat skills. Does not stand-load type-card catalogs.
---

# Session beats

## Gates

Prep only. Follow `docs/agents/work.md` for Work protocol, invention, accept, and lifecycle.
Follow AGENTS.md **HARD: entity-before-spoken** and **HARD: dm-facing-explicit**.

## Filed session plan

After accept, file one session plan at `wiki/journal/sessions/<campaign-slug>/<session-number>/Session-<number>-00-<Title>.md` copied from `wiki/templates/session-plan.md` with `type: session-prep` and `kind: session-plan`. Jobs: compass, Beat Map, Floating Beats, Pressure, PC Touchpoints, and links to typed beat pages. The plan MUST NOT duplicate Scene ends when, Zones, or Be ready for. Live beats are typed pages filled by their type skills.

`references/session-skeleton.md` is the planning form. The filed page the DM opens is the filled session-plan template, not the planning skeleton.

Done when: the session plan answers those jobs, links every live beat, has `type: session-prep` and `kind: session-plan`, and contains only session-plan jobs.

Use a Beat Chart as a pacing palette, never as a script. Prepare pressures,
factions, clues, locations, offers, and hazards that can become beats. Let what
players do select which prepared situation fires, what it means, and whether a
new situation replaces it. Never force the next scene because a slot is empty.

## Pressure-point installation

Choose the pressure mode deliberately. **Mystery** hides information so the
players dig; **surprise** hides the bomb until it goes off; **suspense** reveals
that a bad thing is already moving and puts weight on choices under a fuse.
For sustained tension, install suspense rather than defaulting to mystery or
surprise. A pressure point is ready when the threat is visible enough to act
on, the fuse advances without permission, the clean answer remains uncertain,
and every response costs something.

## Composition

A Beat Chart is a **pacing instrument**: alternation controls audience energy.
Stacking action beats numbs — audiences groan when the hero finishes one fight
and immediately walks into another; stacking introspection beats stalls — the
players start checking their phones. Each Development makes the next
Cliffhanger's stakes legible; each Cliffhanger makes the next Development's
information urgent. The rhythm is the point.

The five beat types compose a session when they advance shared **threads** — a
faction clock, a PC goal, a mystery, a relationship under pressure, a depleting
resource. Plant threads in early beats. Let Developments reveal new facets. Let
Cliffhangers test them under cost. Let the Climax **harvest** what the middle
planted. A beat advancing no live thread is filler; a beat advancing an
abandoned thread is a railroad.

**Hook — reel in the line.** Its sole job is to start the action rolling and
get players committed. Skip fumbling for direction. An action Hook opens a
physical key; a cerebral Hook opens an informational key. The Climax resolves
the question the Hook opened, transformed by the middle's costs and
revelations.

**Developments set direction; Cliffhangers test it.** Each Development is the
**bump** — it reorients the party's trajectory, setting the direction of action
until the next Development changes it. Cliffhangers are contests whose outcome
stays in doubt; they test direction under cost and produce the changed state
the next Development must interpret. Developments can chain (meet the mentor →
learn the weakness → discover the ally); break chains with Cliffhangers so
knowledge is tested before the next piece arrives.

**How the Scene Resolves is the next beat's Trigger.** Prepare transitions, not
just beats. Each beat's carry-forward — what changed in the fiction, what the
party committed to, and the continuity change — is the next beat's entry state.
When different agents compose adjacent beats, the carry-forward is the contract
between them: the receiving beat's opening must inherit the sending beat's
changed world without teleporting past a live option, dropping a planted thread,
or contradicting what the party just experienced. A transition that requires the
reader to invent a bridge is a broken seam.

**Stakes escalate across the arc.** Early pairs explore at lower cost; later
pairs narrow the field and raise the price. Scale opposition across the arc:
early weaker foes teach strengths and weaknesses; later confrontations raise
stakes as both sides invest more. Save the strongest pressure for the Climax.
The Climax arrives where threads converge and the remaining choice carries the
session's highest cost.

## Run the chart

1. **State the promise and starting situation.** Name the experience, question,
   pressure, and player-created goals. Keep hidden truth, mechanics, clocks,
   and unused possibilities in GM notes.
2. **Set a flexible budget.** ~30 minutes per Beat. Reserve Hook + Climax +
   Resolution for ~90 minutes; fill remaining time with alternating D/C pairs.
   Record in the session plan's Beat Map. A Hook with a cover endpoint does not
   also run unbounded travel; the walk to the next landmark is the next beat.
3. **Prepare situations, not outcomes.** For each candidate: trigger, actors,
   stakes, visible information, fuse, costs, at least two viable responses,
   and what changes afterward. For a suspense candidate: three materially
   different response paths, a delay consequence, and a partial success shape.
   Label as Hook/D/C/Climax/Resolution only when it fires.
4. **Fire one Hook at the start.** The session's **strong start**: the first
   pressure landing in one spoken delivery. Prefer an opening that connects to
   the previous session's ending or an active PC goal. Only this first beat may
   recap. Filling the Hook slot is a `hook-beats` job.

   *Polarity handoff:* action Hook → next Development; cerebral Hook → next
   Cliffhanger.

   *Completion:* party committed to a response; DM can state what changed and
   the next beat's trigger. One Hook per session.
5. **Alternate the middle.** Developments change the *decision space*;
   Cliffhangers change the *physical situation*. Never two of the same type
   consecutively — each Development makes the next Cliffhanger's stakes
   legible; each Cliffhanger makes the next Development's information urgent.
   Filling Development slots: `development-beats`; Cliffhanger slots:
   `cliffhanger-beats`.

   A Development is complete when players can name what they now know or can
   decide that they could not before.
6. **Recompute after every beat.** Run the recompute loop in
   [references/agency.md](references/agency.md). Drop obsolete candidates,
   promote emergent situations, re-label or re-order as the new state demands.
   Treat a failed beat as a real world change, not a cue to replay it.
7. **Build fair obstacles.** Traps and puzzles: enough prior clues for a
   solution. Contests: transparent rolls, never GM fiat. Betrayal and Sabotage:
   detectable before irreversible. Second Chance, Back from Dead, and Heroes
   Escape: rare, costly, never erasing meaningful consequences.
8. **Escalate pressure without stacking fights.** Advance visible clocks when
   players delay; never turn an undisclosed trigger into hidden punishment.
   Keep Cliffhangers short and interleave social, investigative, travel, and
   recovery beats between them.
9. **Earn the Climax.** Threads Developments revealed and Cliffhangers tested
   converge into the highest-stakes confrontation players' choices made
   inevitable. Before an action Climax: end preceding beat with Development;
   before a cerebral Climax: end with Cliffhanger. Filling the Climax slot:
   `climax-beats`. Recognize formation: when most routes close and remaining
   paths converge on one high-stakes confrontation, call it when players
   commit, not when the chart says so. If the central question resolves early,
   that is the Climax — compress and deliver Resolution. If the anticipated
   Climax is avoided, consequences become new world state; recompute.
10. **Show the aftermath.** One Resolution follows Climax. Filling:
    `resolution-beats`. Match scope to Climax. Show what changed, what it cost,
    and what players can now pursue. Threads planted in Hook and middle show
    their final state; costs across the session are visible. Completion: players
    can name what is different and what they want next.

## Agency gates

Read [references/agency.md](references/agency.md) for the recompute loop and
agency checks. Additional session-level gates:

- Prepare situations and clocks, not required outcomes.
- Offer two or more meaningful options when fiction supports them.
- Let players ignore a Development, fail a Cliffhanger, or pursue a goal they
  create. Apply visible consequences and recompute; do not hide a correct path.
- Let the chart shrink, branch, pause, or end early when the new state warrants it.
- Make player-facing prose a theatre-of-the-mind fill inside the typed beat
  page's narration surface. Use dungeon-design for sites, routes, and decision
  graphs. Retrieve setting canon with qmd-retrieval; if the vault is silent,
  use a marked stub rather than inventing canon. Never paste WotC proprietary text.

## Dramatic spine

State a one-sentence dramatic spine for the session — the thematic through-line
every beat reinforces from a different angle. The spine guides preparation, not
play: situations are triggered by fiction, not forced by theme. Each beat on the
chart advances the spine through a different lens — the Hook introduces it, early
beats explore it at lower cost, later beats narrow and raise the price, and the
Climax inverts or resolves it. A spine that repeats the same lesson in every beat
is a lecture, not a through-line.

## Beat order audit

Before play, write `Hook → (D/C pairs) → Climax → Resolution` and check:

- **Polarity:** each transition satisfies the alternation rule? Climax prelude
  uses the correct opposite type?
- **Threads:** every prepared beat advances at least one live thread? Climax
  harvests threads the middle planted? Resolution shows their final state?
- **Escalation:** early pairs explore at lower cost, later pairs narrow and
  raise the price? Climax is the highest-stakes convergence?
- **Transitions:** How the Scene Resolves creates a visible trigger for the
  next? No teleports, time-skips, or forced options?

During play, cross out or rewrite candidates after each recompute.

Copy [references/session-skeleton.md](references/session-skeleton.md) for
preparation.

## Typed fill

This skill assembles the Beat Chart session plan. Composition filling a typed
slot → that type skill becomes primary for the fill.

| Slot | Skill |
|---|---|
| Hook | `hook-beats` |
| Development | `development-beats` |
| Cliffhanger | `cliffhanger-beats` |
| Climax | `climax-beats` |
| Resolution | `resolution-beats` |

Type-card catalogs live in those skills, not here.

## Session ritual

**Pre-session (30-40 min):** review PC goals/abilities and attach at least one
limelight moment per PC; pick a strong purposeful start; prepare ~10 floating
secrets/clues; write a hiccup list; keep a parachute file of off-map one-shots;
leave the chart as a skeleton. Prep only what is uncomfortable to improvise,
as modular pieces findable in under 30 seconds.

**In session:** use shorthand, keep clocks/fronts visible as scales, give
players useful roles (watcher, caller, mapper, negotiator, recorder) when a
procedure benefits. If an optional recording exists, route through
`session-transcript-ingest`; never make a transcript the session plan.

## Table-craft gates

Before filing, audit: every PC has a limelight moment; rails grow from stated
backstory and public stakes; agreed tone is honored; one striking image carries
visible energy; every choice or silence echoes in the fiction. `[!narration]`
carries sensory detail only — never secrets or DCs.
