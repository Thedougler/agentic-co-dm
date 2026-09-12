---
name: travel-events
description: Design what happens on a journey leg — travel and sea events derived from the party's own threads, never rolled at random — in a Campaign OS repo (vault/ present). MANDATORY for any leg, crossing, or voyage the party will play, even a routine one. Use for "travel/sea encounter", "what happens on the way to [place]", "design the crossing", "the party sails/rides to [place]". Not ship stats (ship GUIDE), stat blocks (encounter-prep), or the route's standing facts (route GUIDE).
---

# Travel Events

Prep family, Phase 1 (PREP). **A travel event advances something; a random
encounter fills time.** Every event is chosen for this party — a named PC
thread, faction front, or spotlight need colliding with the leg — never
rolled into existence. Epic is structural, never travelogue
(`vault/refs/stories/influences.md` § J.R.R. Tolkien). Cites
`.claude/skills/composing-beats/references/runtime-surface.md` and `.claude/skills/composing-beats/references/audits.md`.

## The journey shape

Five slots, every leg, in order — full craft: `references/journey-shape.md`.
(1) **Departure cost** — what going now leaves behind or owes. (2)
**Landmark** — ≥1 named, steerable thing on the way; where wonder and
choice live. (3) **Events** — typed and composed per the sections below.
(4) **Toll** — ≥1 stated cost (Hard Rule 9). (5) **Arrival changed** —
how the party arrives different.

## Standard queries

Run the query set in `references/standard-queries.md` before deriving any
event, and paste every hit: the route-page baseline, the stub check, the
encounter-table check, faction fronts, and PC Arc Notes.

## Deriving events from the party (never random)

Inventory the live material first: Arc Notes threads, faction fronts
reaching the leg, unresolved backstory, the spotlight PC, standing party
pressures (a debt, a pursuer, a dwindling supply). Each event is the
collision of one piece of that material with a fact of the leg — terrain,
weather, traffic, the landmark, a route page's hazards — and states its
derivation in one clause: "<PC name>'s smuggler thread × the lane's thin
patrols." No live material reaches the leg → § Degrade by asking, never a
generic filler event.

## Spotlight balancing

The PC longest without a meaningful moment gets the leg's PC-connection
event and first role pick; a spotlight PC already named by
`draft-run-guide` is used, never re-picked.

## Travel roles

Every leg of 2+ events offers the roles — Trailhand, Scout, Quartermaster
(at sea: [[ship-operations|Ship Operations]] § Stations Underway, one
station per PC) — to real PCs by name; a failed check is the next
complication, never a flat penalty (`references/travel-roles.md`).

## Event typing (Pointy Hat TES, kept — the load-bearing taxonomy)

A register-balance palette to compose with, never a random table to roll:

| Color | Type | Focus |
|---|---|---|
| Red | Combat | Fight with narrative stakes |
| Blue | Roleplay | NPC, faction, or moral-dilemma beat |
| Yellow | Exploration | Terrain/navigation hazard, wonder, skill challenge |
| Purple | Roleplay + Combat | Combo |
| Green | Exploration + Roleplay | Combo |
| Orange | Combat + Exploration | Combo |
| White | All three | Rare, save for a centerpiece leg |

**Travel method shapes the palette** — same six types, different dressing
per method (Ship/Overland/Aerial/Planar):
`references/event-tables.md` § Travel method dressing. This campaign
crosses [[shattered-sea|the Shattered Sea]] — **ship is the default
method** unless the leg says otherwise, and the party's own vessel (page,
crew, condition) is live material for derivation like any thread.

## Distance → event count

Keep stated distances vague — "a few days" beats "four days"; exact
figures enter play only from a route page's `travel_time:` or a live
deadline.

| Distance | Events | Notes |
|---|---|---|
| Close | 1 | +1 if this leg is dramatically loaded (a thread is actively hot) |
| Far | 2 | 3 if this leg is the session's centerpiece |
| Very Far | 3–4 | 5 for an epic, session-spanning voyage |

## Composition rules (numbers, not judgment)

- **Never the same type twice in a row** — two Reds back-to-back is a
  slog, not drama.
- **≥1 non-combat event per leg** of 2+ events; **≥1 event connects to an
  active PC thread** (Hard Rule 1); **every event states its party
  derivation** (Hard Rule 2).
- **≥1 wonder/landmark beat per leg** — nothing established suggests one →
  pick and cite the `vault/refs/table-wilderness-encounters.md` row that
  resonates with the party's live material (picked, never rolled).
- **The arrival-changed line is mandatory** — a leg that ends emotionally
  where it started was a transition, not a journey.
- **No event stars two casts of never-met strangers** — cut or ground one
  first. **Leave loose ends** — a fully self-resolving event is wasted
  prep (`.claude/skills/composing-beats/references/audits.md` §4's If-Ignored requirement).

## Where travel events land (owned paths: none)

This skill writes nothing to `vault/` — it designs the leg and hands the
material on. Four destinations, tested per finding
(`references/route-escalation.md`): (1) default, drip or a plot-weight
moment on the `type: route`; (2) the way's standing facts →
`type: route` via `.claude/skills/draft-content/references/route.md`; (3) reusable rolls →
`type: table` via `.claude/skills/draft-content/references/table.md` (row seeds only);
(4) a named entity with a future → its own drafting guide.

## Hard rules

1. **PC-Connection Requirement** (`.claude/skills/composing-beats/references/runtime-surface.md` §2): at
   least one event names the specific PC and mechanism — "the smuggler
   crew flying &lt;PC name&gt;'s old house colors," not "ties into the group's arc."
   Ask if unanswered.
2. **Event selection is never random** — every event states its party
   derivation (§ Deriving events from the party). Dice enter only
   in-fiction — role checks, hazard checks, opposed rolls — through a real
   roller (`roll-dice`), the check, DC tier, and result cited for audit.
   Never an invented number; never a die deciding what the party
   encounters.
3. **Combat or drama-suite stakes hand off to `encounter-prep`** — a Red
   event, or any Purple/Orange/White with real fight/social stakes,
   invokes it with premise and PC connection, folding the returned Toy
   table/Enemy Roster/Drama Suite into that event's beat, never re-derived.
4. **A named entity that might recur hands off to
   `.claude/skills/draft-content/references/npc.md`** before dialogue or a "wants" field —
   a one-off name with no future stays inline.
5. **Pure Yellow (exploration/hazard) events are this skill's own** — no
   hand-off. DC tiers: `references/event-tables.md` § Hazard resolution;
   cite the DC/consequence tier, same audit requirement as Hard Rule 2.
6. **Sandbox discipline binds every event**
   (`.claude/skills/composing-beats/references/audits.md` §1): never write what a PC decides,
   feels, or wants; the opposition/hazard is independent of engagement;
   consequences are pressures, never an if-then chain past one step.
7. **Standing facts, tables, and entities escalate as hand-offs only** —
   per § Where travel events land; this skill never writes the page,
   flips a `status:`, or touches `publish:`. Genuinely unsure →
   § Degrade by asking, not a coin flip.
8. **Every event names what it advances** — a thread, a relationship, a
   resource, a piece of world knowledge. "It fills the day" → cut it or
   redesign it.
9. **Every leg states its toll**, and any pace, exhaustion, or hazard
   number quoted comes from `vault/refs/gameplay-toolbox.md` (via the toll
   menu, `references/event-tables.md`), never invented.

## Workflow

1. **Method and distance** (ship default; Close/Far/Very Far, ask if
   unstated), then **run the Standard queries** and paste every hit.
2. **Name the spotlight PC** and **offer the travel roles**.
3. **Pick the event count** from § Distance → event count.
4. **Derive each event from the party material**, composing type balance
   per § Composition rules — derivation stated on every event.
5. **Fill the journey slots** — departure cost, landmark (wonder-table row
   cited if used), toll, arrival changed.
6. **Route each event** per Hard Rules 3–5: combat/drama →
   `encounter-prep`; recurring entity → its drafting guide; pure hazard →
   `references/event-tables.md` § Hazard resolution.
7. **Build each event's beat** — TES type sets the register, derivation
   and PC connection named in the body.
8. **Hand off** — events, slots, roles to the Route page's samples or a
   plot-weight moment; route/table/entity gaps flagged per § Where travel
   events land. Before calling the leg done, run
   `references/travel-checklist.md`.

## Degrade by asking

- Method unstated → ship (this campaign's mode); ask only when the leg
  could plausibly be otherwise. Distance unstated → ask, never guess.
- No PC thread, front, or pressure plausibly reaches the leg → ask which
  thread to pull on; "ties into the group's arc" is never an answer (Hard
  Rule 1), and a generic filler event is never the fallback (Hard Rule 8).
- Unclear whether the leg recurs (route page), a table would be reused, or
  a named entity returns → ask; never guess a page into existence.

## Creative-domain rider

Facts, canon, structure, and visibility are bound (Hard rules above, all
ten project rules; `.claude/skills/composing-beats/references/runtime-surface.md`'s rider). **Prose style
is free.** A generic "pirates attack" event is a contract violation —
push for the specific.

## Reference files

| File | Read when |
|---|---|
| `references/standard-queries.md` | Running the party-material inventory |
| `references/journey-shape.md` | Filling the five slots, or a leg feels flat |
| `references/travel-roles.md` | Offering roles, or resolving a failed role check |
| `references/event-tables.md` | Resolving a Yellow hazard, or picking a toll |
| `references/route-escalation.md` | Deciding where a leg's material lands |
| `references/worked-examples.md` | Wanting a worked derivation example |
| `references/travel-cross-skill-coordination.md` | Which skill an event hands off to |
| `references/travel-checklist.md` | Final check before calling a leg done |
| `references/out-of-scope.md` | Full out-of-scope list with owning skill per item |
