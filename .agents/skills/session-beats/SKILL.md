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
## Work gate

Prep only. Follow `docs/agents/work.md`.

## HARD: entity-before-spoken (Nick 2026-09-14)

**Production session content** (session-prep beats, TotM/`[!narration]`, action cards, spoken text) is **complete or it does not ship**. Vague/non-specific descriptions of unnamed people/things because the entity page is missing = **critical error**.

**Dependency order (recursive):** If a beat/scene names or requires an NPC, item, creature, place, faction, vehicle, spell, quest, or other entity — **mint/file that owner page first** (current standards: kebab basename, matching `wiki/templates/`, land under `wiki/_staging/` when `WIKI_STAGED_WRITES=true`), **then** write/update the session/TotM text that depends on it. Even when Nick asks for a session that introduces new names — create the entities first. The DM cannot describe what does not exist.

Agents MUST complete **all** recursive dependency steps to finish the goal — not only top-level, intermediary, or initial steps — in dependency order. This is a completeness gate; do **not** thin narrative craft to satisfy it.


Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

Remap durable session-prep to `wiki/journal/sessions/<campaign-slug>/<session-number>/`. Templates live in `wiki/templates/`. Replace knowledge-bank terminology with wiki terminology, but do not change geographic river-bank language. Point at `docs/agents/work.md` rather than restating the glossary.


## HARD: dm-facing-explicit (Nick 2026-09-14)

**DM-facing content** (`visibility: dm`, action cards, Be ready for, secrets, situation facts, Wiki facts, owner pages): **no vagueness, non-specific placeholders, coy narration, or invented mystery.** The DM must have **all** scene/world facts available immediately. Making the DM decode coy agent writing = **critical error**.

**Clarify vs player-safe TotM:** Player-facing `[!narration]` may withhold from *players*; it must still be grounded in named entities that exist (**HARD: entity-before-spoken**). DM layers must state who/what/where/why concretely — names, wants, true stakes — with a DM answer on the page for every planted mystery.

**FAIL:** “a woman in the woods,” “unnamed survivors,” “something watches,” mystery with no DM answer on the page.
**PASS:** Named `[[npc]]` with look/want/voice; named place; stated true invitation/threat.

Pairs with entity-before-spoken. Completeness/explicitness gates — do **not** thin narrative craft.

## Filed session plan

After accept, file one session plan at `wiki/journal/sessions/<campaign-slug>/<session-number>/Session-<number>-00-<Title>.md` copied from `wiki/templates/session-plan.md` with `type: session-prep` and `kind: session-plan`. Jobs: compass, Beat Map, Floating Beats, Pressure, PC Touchpoints, and links to typed beat pages. The plan MUST NOT duplicate Scene ends when, Zones, or Be ready for. Live beats are typed pages filled by their type skills.
When planning includes a player, read that PC's `## Stated Goals` when present. Do not write the PC owner page.


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

The five beat types compose a session when they advance shared **threads** — a
faction clock, a PC goal, a mystery, a relationship under pressure, a depleting
resource. Plant threads in early beats. Let Developments reveal new facets. Let
Cliffhangers test them under cost. Let the Climax **harvest** what the middle
planted. A beat advancing no live thread is filler; a beat advancing an
abandoned thread is a railroad.

**Developments set direction; Cliffhangers test it.** Each Development is a
"bump" that reorients the party's trajectory — setting the direction of action
until the next Development changes it again. Cliffhangers are contests whose
outcome stays in doubt up to the end; they test the direction a Development
set and produce the changed state the next Development must interpret.
Developments can chain: one Development (meet the mentor) leads to another
(learn the weakness) that leads to a third (discover the ally), each building
capability toward the Climax. When Developments chain, break them with
Cliffhangers so the knowledge is tested under cost before the next piece
arrives.

**The Hook sets the session's key.** An action Hook (pursuit, fight, crisis)
opens a physical key — the middle explores and survives a dangerous situation.
A cerebral Hook (discovery, offer, revelation) opens an informational key — the
middle decides what to do with knowledge. The Climax resolves the question the
Hook opened, transformed by the middle's costs and revelations.

**How the Scene Resolves is the next beat's Trigger.** Prepare transitions, not
just beats — the seam carries momentum. A Cliffhanger ending in a new place
opens the next Development with what can be learned there. A Development
revealing a betrayal triggers the Cliffhanger where the betrayer acts. A
transition that teleports past a live option is a railroad.

**Stakes escalate across the arc.** Early Development/Cliffhanger pairs
explore the problem space at lower personal cost — gathering information,
meeting actors, testing terrain, choosing sides. Later pairs narrow the field
and raise the price — alliances tested, resources committed, routes foreclosed.
The Climax arrives where threads converge and the remaining choice carries the
session's highest cost.

**Balance action and introspection.** A session of pure Cliffhangers is
exhausting; a session of pure Developments is inert. The chart keeps a
balance — action to process, danger to plan, spend to invest — and the
alternation rule is how that balance works mechanically.

**Resolution echoes the whole arc,** not only the Climax's immediate outcome.
Threads planted early show their final state. Costs paid in the middle are
visible. PC goals pursued since the Hook have a clear new status.

## Run the chart

1. **State the promise and starting situation.** Name the experience, question,
   pressure, and player-created goals that matter now. Keep hidden truth,
   mechanics, clocks, and unused possibilities in GM notes.
2. **Set a flexible budget.** Treat roughly 30 minutes of real play as one Beat.
   Reserve Hook, Climax, and Resolution for about 90 minutes together; fill
   additional time with alternating Development/Cliffhanger pairs. Adjust for
   table speed, not the clock alone. Record the budget in the session plan's
   Beat Map. A Hook with a cover endpoint does not also run unbounded travel;
   the walk to the next landmark is the next beat (Sly Flourish: Watch the Time).
3. **Prepare situations, not outcomes.** For each candidate, record trigger,
   actors, stakes, visible information, fuse, costs, at least two viable
   responses, and what changes afterward. For a suspense candidate, require
   three materially different response paths, a delay consequence, and a partial
   success shape. Mark the candidate as a Hook, Development, Cliffhanger,
   Climax, or Resolution only when it fires.
4. **Fire one Hook at the start.** The Hook is the session's **strong start**:
   the first pressure the party faces, landing in one spoken delivery. Present
   an actionable problem, offer, threat, discovery, or opening. Prefer an
   opening that connects to the previous session's ending or an active PC goal.
   Only this first beat may recap the previous session. Later beats start from
   the immediate current situation and do not summarize earlier beats or
   prior-session events. Filling the Hook slot is a `hook-beats` job.

   *Polarity handoff:* if the Hook is action-heavy (pursuit, fight, crisis,
   ambush), make the next beat a Development so the party can process what
   happened. If the Hook is cerebral or conversational (discovery, revelation,
   offer), make the next beat a Cliffhanger to raise physical stakes.

   *Completion:* the party has committed to a response — they can name what
   they are doing about the opening pressure. The DM can state what changed
   and what the next beat's trigger is. One Hook per session; a session with
   two Hooks has a pacing problem, not an energy surplus.
5. **Alternate the middle.** Developments change the *decision space* — what
   players know, can reach, or choose between. Cliffhangers change the
   *physical situation* — position, resources, safety. Use Developments for
   clues, talk, revelation, planning, alliance, or character change. Use
   Cliffhangers for action, peril, pursuit, fights, ambushes, and immediate
   obstacles. Do not place two Developments or two Cliffhangers consecutively.
   Each Development makes the next Cliffhanger's stakes legible; each
   Cliffhanger makes the next Development's information urgent. Two of the
   same type dulls both — Cliffhanger after Cliffhanger dulls danger faster
   than it builds excitement. Filling Development slots is a `development-beats`
   job; filling Cliffhanger slots is a `cliffhanger-beats` job.

   A Development is complete when players can name what they now know or can
   decide that they could not before. A player-caused pause, detour, or
   departure is not a license to force the next prepared beat.
6. **Recompute after every beat.** Update actors, knowledge, resources, routes,
   clocks, relationships, and player goals. Drop obsolete candidates, promote
   emergent situations, and change labels or order as the new state demands.
   Treat a failed beat as a real world change, not a cue to replay it.
7. **Build fair obstacles.** Put enough clues in the current or earlier fiction
   for a Trap or Puzzle to have a solution; provide multiple approaches where
   possible. Resolve Contests with transparent player skill, choices, or rolls,
   never GM fiat. Give players a chance to notice Betrayal or Sabotage before
   it becomes irreversible. Keep Second Chance, Back from Dead, and Heroes
   Escape rare, costly, and unable to erase meaningful consequences.
8. **Escalate pressure without stacking fights.** Advance visible clocks and
   change the problem when players delay; do not turn an undisclosed trigger
   into a hidden punishment. Scale opposition across the arc: early Cliffhangers
   use weaker, avoidable, or partial opposition that teaches strengths and
   weaknesses on both sides; later Cliffhangers use tougher or more
   consequential opposition as the party's capabilities and the threat's
   desperation grow together.
   Keep Cliffhangers short and legible, save the strongest pressure for the
   Climax, and interleave social, investigative, travel, and recovery beats.
   As threads advance, narrow the options and raise the personal cost — the
   arc escalates through what players have invested, not through stacking
   opponents.
9. **Earn the Climax.** The Climax harvests what the middle planted — threads
   that Developments revealed and Cliffhangers tested converge into the
   highest-stakes confrontation the players' choices made inevitable. Before
   an action Climax, end the preceding
   beat with a Development; before a cerebral Climax, end it with a Cliffhanger.
   A final battle is one shape among many: sacrifice, defense, desperate gambit,
   reckoning, negotiation under duress, catastrophe survival, trial, betrayal
   cascade, or reframing can be the climax. Filling the Climax slot is a
   `climax-beats` job. Recognize formation: when player
   choices close most open routes and the remaining paths converge on one
   high-stakes confrontation, the climax is near — call it when players commit,
   not when the chart says it is due. If the central question resolves early,
   that early resolution is the climax; compress and deliver the Resolution
   rather than padding the session to reach a planned slot. If the party avoids
   the anticipated climax entirely, the avoided confrontation's consequences
   become the new world state; recompute and let a different confrontation earn
   the role or close with a Resolution.
10. **Show the aftermath.** Follow Climax with one Resolution. Filling the
    Resolution slot is a `resolution-beats` job. Match scope to the Climax: a
    relationship-scale climax gets a relationship-scale resolution; a
    faction-scale climax gets a power-vacuum resolution. Show what changed,
    what it cost, and what the players can now pursue. Honor the outcome — a
    surviving threat earns its place only when its survival follows from
    established fiction and leaves the players with consequential knowledge or
    options. Threads planted in the Hook and middle show their final state;
    costs paid across the session are visible. Completion: the players can name
    what is different in the world and what they want to do next.

## Agency gates

- Prepare situations and clocks, not required outcomes.
- Reveal a moving threat before asking players to pay for choices; hide the clean answer, not the problem.
- Accept clever solutions that were not prepared; update the world and let the opposition adapt later.
- Offer two or more meaningful options when the fiction supports them: routes,
  alliances, bargains, fights, retreats, investigation, or refusal.
- Let players ignore a Development, fail a Cliffhanger, or pursue a goal they
  create. Apply visible consequences and recompute; do not hide a correct path.
- Let the chart shrink, branch, pause, or end early when the new state warrants it.
- Make player-facing prose a theatre-of-the-mind fill inside the typed beat
  page's narration surface. Use dungeon-design for sites, routes, pressure
  procedures, and decision graphs. Retrieve setting canon with qmd-retrieval;
  if the vault is silent, use a marked stub rather than inventing canon. Never
  paste WotC proprietary text.

## Beat order audit

Before play, write `Hook → (D/C pairs as needed) → Climax → Resolution` and
check:

- **Polarity:** does each transition satisfy the alternation rule? Does the
  Climax prelude use the correct opposite type?
- **Threads:** does every prepared beat advance at least one live thread? Does
  the Climax harvest threads the middle planted? Does the Resolution show
  their final state?
- **Escalation:** do early pairs explore at lower cost while later pairs narrow
  and raise the price? Is the Climax the highest-stakes convergence, not a
  flat peer of the middle beats?
- **Transitions:** does How the Scene Resolves create a visible trigger for the
  next? Are there teleports, time-skips, or forced options between beats?

During play, cross out or rewrite candidates after each recompute. A chart is
healthy when it creates pressure and openings without deciding what players
must choose.

Read [references/agency.md](references/agency.md) for the recompute loop and
anti-railroad tests. Copy [references/session-skeleton.md](references/session-skeleton.md)
for preparation. Run [evals/evals.json](evals/evals.json) against drafts.

## Typed fill

This skill assembles the Beat Chart session plan. Composition filling a typed slot → That type skill; type becomes primary for the fill.


| Slot | Skill |
|---|---|
| Hook | `hook-beats` |
| Development | `development-beats` |
| Cliffhanger | `cliffhanger-beats` |
| Climax | `climax-beats` |
| Resolution | `resolution-beats` |

Type-card catalogs live in those skills, not here. A planning job produces a
valid session plan without opening a type-card catalog.

## Session ritual

**Pre-session (30-40 minutes):** review PC goals/abilities and attach at least
one possible limelight moment to each PC; pick a strong purposeful start from the
cliffhanger or agreed plan; prepare a floating bank of about ten secrets/clues;
write a hiccup list; keep a parachute file of off-map one-shots; and leave the
chart as a skeleton. Prep only what is uncomfortable to improvise, as modular
pieces findable in under 30 seconds.

**In session:** use shorthand, keep clocks/fronts visible as scales, and give
players useful roles (watcher, caller, mapper, negotiator, recorder) when a
procedure benefits from them. If an optional recording exists, route it through
`session-transcript-ingest`; never make a transcript the session plan or handoff.

## Table-craft gates

Practice **silence discipline**: state the actionable situation, ask what the
players do, and wait. Do not panic-fill a quiet table; players learn that play
advances when they act. If they choose not to act, show the visible consequence
of inaction and return the decision, rather than inventing a rescue or forcing a
beat. Keep the flexible prep toolbox ready so waiting is safe for the DM.

Before play, audit: spotlight players, pause when they should drive, build rails
from stated PC backstory and public stakes, honor the agreed tone, frame one
striking image with visible energy, and ensure every choice or silence has an
echo in the fiction. Cinematic framing never moves secrets or DCs into
`[!narration]`.
