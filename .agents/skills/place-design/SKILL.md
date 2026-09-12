---
name: place-design
description: >-
  Design engaging playable places for D&D 5.5e (2024 / SRD 5.2.1): settlements,
  wilderness regions, dungeons and ruins, landmarks, encounter sites, and planar
  or reality-warped locations. Use when creating location kernels, topology,
  affordances, factions, information economies, pressure, location moves, or
  node keys, or when filing those facts into a campaign location note. Prefer
  situations over plots. Do not use for pure narration without structure (use
  theatre-of-the-mind) or for monster/item math alone.
---

# Place design
## Work gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

File durable output under `wiki/` (entities/journal as appropriate); templates live in `wiki/templates/`. Replace knowledge-bank language with wiki language, and point at `docs/agents/work.md` rather than restating its glossary. Keep craft procedure.


A place is **identity + topology + affordances + inhabitants + information +
pressure + consequences**. It is not a backdrop or a list of rooms. Design the
playable situation first, then write only details that change a choice, route,
risk, resource, clue, pressure, or response.

## Build the place in this order

1. **Kernel.** Write the five sentences below. State what is true now, not a
   history essay. Derive architecture, routes, people, clues, and consequences
   from the same premise.
2. **References.** Choose 2–4 recognizable references, then record what the
   place inherits, transforms, or rejects from each. References are design
   handles.
3. **Promise.** Tell players what kinds of decisions and experiences the place
   offers. Make the promise actionable, not just an adjective.
4. **Structure.** Draw nodes and edges before room prose. Mark loops, bypasses,
   retreats, vertical or strange connections, route tradeoffs, and the
   north/east/south/west neighbors with approximate days of travel.
5. **Life and information.** Give inhabitants goals, movement, and reactions;
   distribute essential knowledge over several clue vectors.
6. **Pressure and consequences.** Decide what changes while the party acts,
   rests, leaves, or returns. Then key only significant nodes.

## Five-sentence location kernel

1. **Function:** What was or is this place used for?
2. **Fantastic element:** What makes it impossible to mistake for an ordinary place?
3. **Present conflict:** Who or what currently wants incompatible things here?
4. **Player promise:** What compelling experience does the place offer?
5. **Trajectory:** What happens if nobody intervenes?

This is a situation, not a predetermined scene sequence. Prepare circumstances
and actors; let players determine what happens.

### Player-facing promise

| Promise | Players expect to… |
|---|---|
| Discovery | Uncover secrets, history, routes, or strange phenomena |
| Danger | Survive threats, manage exposure, or judge risk |
| Intrigue | Identify alliances, motives, lies, and leverage |
| Exploitation | Turn environmental features against a problem |
| Wonder | Encounter something unfamiliar and consequential |
| Refuge | Recover, form relationships, invest, and belong |
| Transformation | Change ownership, function, culture, or physical form |
| Mastery | Learn the place well enough to navigate or manipulate it efficiently |

Use one or two dominant promises. The promise decides which details deserve prep.

## Fast identity test: 3Fs, contradiction, signatures

Write the **3Fs**: **Fantastic** (what could exist only here), **Familiar** (what
lets players understand it quickly), and **Functional** (how inhabitants actually
use it). Add one productive contradiction that generates questions. Give three
concrete signature details that imply actions—not decorative scenery. Prefer
details players can climb, rotate, bargain with, break, follow, or exploit.

## Navigable structure

Represent the place as `node --edge--> node`. A node is a significant situation,
landmark, resource, threshold, or decision; an edge records route, cost,
information, danger, and consequence. Good topology usually includes:

- north, east, south, and west neighboring locations, each with a wikilink or
  explicit canon gap and an approximate `~ days of travel` distance where known;
- at least two approaches when fiction permits;
- one loop, one bypass, and one retreat or safe return route;
- a meaningful vertical, environmental, social, or reality-bending connection;
- a route tradeoff: fast/safe, hidden/exposed, costly/informative, or
  reversible/committing;
- reconnection after branches, unless isolation is the intentional pressure;
- a clear answer to “what changes if they use this edge?”

Do not make every fork a corridor fork. A bridge toll, faction invitation,
weather window, reputation gate, river, rooftop, or remembered shortcut can be an
edge. See [node-key-and-affordances](references/node-key-and-affordances.md).

## Significant nodes and affordances

Apply the **verb test**: each significant node should invite at least one useful
verb such as cross, bargain, hide, study, steal, reroute, rescue, harvest,
climb, consecrate, sabotage, or wait. Name what is actionable and what changes
when acted upon. Prepare affordances, not prescribed solutions: describe
materials, relationships, constraints, and observable responses so players can
invent methods. Every obstacle gets a sign, trigger, effect, counterplay,
bypass, and leverage; do not hide the only correct answer.

## Information economy

Classify clues as **operational** (how it works), **historical** (what happened),
or **directional** (where to go / whom to ask / what follows). For each required
secret, prepare about three independent clue vectors: witness or faction, physical
trace, document or symbol, spatial pattern, and/or consequence. Passive noticing
reveals the obvious sign; a declared Search, Study, Influence, or other action
can deepen it. A failed roll should cost time, safety, position, trust, or
resources—not erase a required revelation.

## Living place

Give each active faction a sheet: **Want, Fear, Method, Resources, Tell, Offer,
Response**, plus territory, red line, current move, and what changes between
visits. Give important creatures or groups a job and a reason to move. Keep a
roster for arrivals, absences, wounded, prisoners, and depleted resources.
Progression states can be quiet → alert → contested → transformed; define the
trigger and visible sign for each. A place should do something while the party
is elsewhere.

## Location moves and consequences

Prepare 2–4 moves a place or faction can make when a trigger occurs: close a
route, recruit help, relocate a resource, reveal a cost, make an offer, change
the terrain, escalate a ritual, or exploit a party choice. State trigger, actor,
visible result, new opportunity, and lasting consequence. On return, preserve
what is durable and update what is alive; do not reset rooms by default. Use
[life-info-pressure](references/life-info-pressure.md).

## Rules, capability, and type

Integrate 2024/SRD 5.2.1 mechanics briefly: use the rules vocabulary, a fair DC,
cover, Difficult Terrain, Search/Study/Influence/Utilize, and hazards with
telegraph, trigger, effect, and counterplay. Use
[references/rules-and-place-types.md](references/rules-and-place-types.md) for the
palette, tiers, and settlement/wilderness/dungeon/landmark/planar adjusters.
Do not negate flight, teleportation, burrowing, darkvision, social authority, or
other party capabilities arbitrarily; make them useful with honest costs,
exposure, limits, or consequences.

## Presentation and handoffs

Design with the [location skeleton](references/location-skeleton.md) and [node-key-and-affordances](references/node-key-and-affordances.md). File **facts** into `wiki/templates/place.md` as a scaffold. Pass is place jobs in `wiki/AGENTS.md` Layout, not heading-order match. `wiki/_raw/Old Gardens.md` and `wiki/_raw/River Line Bank.md` illustrate; do not require matching their headings.

| Design work | Place jobs |
|---|---|
| Identity image | After the title when art exists (`visual-aids`) |
| Spoken look | Theatre of the mind `[!narration]` |
| Situation now | What this place is, which linked places it sits between |
| Consequential moves | Player verbs that change the scene; omit no-op moves |
| Presence or sign of absence | Who is here, or the sign they are not |
| Table objects | Features, flora, fauna, objects; wikilink owner pages |
| Connections | Neighbors and how this place connects; name a canon gap when unknown |
| Purpose | Why a party comes, stays, or cares |
| Extra art | Battlemaps; omit when unused |

Kernel, 3Fs, promise, player-verb lists, topology audit, references, and the
quality checklist stay in this skill. A climactic or anchor location
(`Memorial Grove`) may carry kernel, topology, player verbs, hooks, secrets,
and provenance directly when those facts serve the DM at the table — but the
scaffold stays clean.

**Complete when:** the filed note answers place jobs in `wiki/AGENTS.md` Layout, empty sections are omitted, connections name neighbors or canon gaps, and the skeleton is not on the wiki page.

Run the audit: identity and promise are clear; topology has choices; nodes pass
the verb test; clues are robust; factions have goals and moves; pressure changes
play; the place works without combat; consequences persist; and the **final
enemies-vanished test** still leaves an interesting place to explore, bargain
with, alter, or understand.

Handoff deep dungeon or megadungeon graphs to `dungeon-design`; player-facing
prose to `theatre-of-the-mind`; session pacing to `session-beats`; and vault
canon retrieval to `qmd-retrieval`. Do not invent setting canon when the vault is
silent—mark a stub.

## World-bible and prep gates

Keep location notes modular and table-findable in under 30 seconds. File **facts**
into `wiki/templates/place.md` as a scaffold. Secrets remain DM truth and never enter
`[!narration]`; they live as facts that answer the jobs. A location
earns depth from responsive systems: inhabitants move, factions react, routes
change, and clocks advance — not from a larger lore block. Prepare only the
topology, affordances, clues, and pressure the DM will not improvise, then link
the atomic note to the nearest MOC or hub rather than creating parallel structure.
