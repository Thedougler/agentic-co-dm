---
name: place-design
description: >-
  Design and file playable site places for D&D 5.5e (2024 / SRD 5.2.1):
  dungeons and ruins, wilderness sites, landmarks, shops and buildings,
  encounter sites, and planar or reality-warped locations. Use when creating or
  improving a `type: place` page or any part of one: identity, canon weave,
  secrets, hazards, items, topology, inhabitants, pressure, location moves, or
  its spoken look. Hub for all places: cities go to city-design, regions to
  region-design, narration alone to theatre-of-the-mind.
---

# Place design

A place is a **situation with topology**: something is happening in a space the
party can move through, and the space is built from the campaign's own canon.
Players meet it through its narration first, so everything the place holds (its
secrets, items, hazards, people, and history) leaves a **tell** in the spoken
look: a plain, ordinary-sounding detail a sharp player can pull on. The DM page
states the truth behind every tell.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named place (existing page or one to mint), the caller's
  objective and brief, `wiki/templates/place.md`, and the vault canon the place
  touches.
- **Work:** The steps below, for this one place. Keep the caller's objective.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** `kind: city` → `city-design`; region → `region-design`;
  a deep dungeon graph → `dungeon-design`. A named person, creature, item,
  faction, lore, or quest the place needs is cast before it is minted
  (`docs/agents/table-ready.md` § Cast before minting): an in-play or
  unrevealed page that fits comes first, and its owner skill mints one only
  when none fits, before any text depends on it (AGENTS.md **HARD:
  entity-before-spoken**, **Focused minting**). The spoken look →
  `theatre-of-the-mind` with the packet from step 6. Each child returns its
  page path or prose and its completion result; resume at the step that waited
  on it.

## Page rules

These hold in every step.

- **Canon.** User-said facts file immediately on the live path. Whatever the
  place needs that canon leaves silent, records as unknown, or contradicts,
  decide now as canon under the rule in `llm-wiki` (`docs/agents/table-ready.md` § Fill the
  silence): one concrete answer, stated on the page as world fact where the DM
  uses it, with the page marked `invention: true`. The response lists each
  proposal with the `[[pages]]` it grows from; a proposal that settles a
  contradiction names the sources and the reading it chose, so the DM picks the
  winner.
- **Preserve.** Improving an existing page keeps every established detail;
  fold each one into the section that now owns it.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the steps and `## Done` below.
- **One callout.** `[!narration]` in Overview is the only callout on the page.
  Truths, DCs, mechanics, and GM notes are plain complete sentences in the
  section that owns the feature.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). Every tell has
  its truth on the page: who, what, why, and what is at stake, by name. When
  canon is silent, the truth is decided and becomes canon under the rule in `llm-wiki`
  (`docs/agents/table-ready.md` § Fill the silence); a gap is never written as
  mystery ("something waits below").
- **Honest capabilities.** Flight, teleportation, burrowing, darkvision, and
  social authority work here; give them costs, exposure, or limits with a
  reason in the fiction.
- **Process stays off the page.** The inventory, kernel, weave map, and packet
  are working notes; the page carries only their facts.

## Steps

[references/example.md](references/example.md) takes one place through every
step; read it before step 3.

### 1. Take the canon inventory

Retrieve before inventing (constitution XII), using QMD per AGENTS.md § Vault
retrieval (`.agents/skills/qmd`).

1. Read the place page if it exists, its region page, and every page that
   links to it: run `grep -rliF "[[<name>" wiki/entities` once for the slug,
   the title, and each alias (links use all three).
2. Search QMD for the place name, its aliases, its region, and each neighbour.
   Then search for what a place holds: people, factions, creatures, items,
   hazards, lore, quests, and session events tied to it or to its owner.
3. `qmd get` every hit you will use. Snippets are leads, not facts.

Write the **canon inventory** in working notes, one line per owner page:
`[[slug]]` · kind · the fact that could put it physically in this place.

Done when every backlink and every relevant hit is either in the inventory or
dropped with a one-line reason, and every inventory page was read in full.

### 2. Write the kernel

Five sentences, in working notes: **Function** (what the place is for),
**Fantastic element**, **Present conflict**, **Player promise** (one or two of
discovery, danger, intrigue, exploitation, wonder, refuge, transformation,
mastery), and **Trajectory** (what happens if nobody intervenes). Take the
fantastic element and the conflict from the inventory whenever it offers them:
a hunt, a debt, a rival, or a threat already on a canon page. A **conflict**
is opposed wants: someone named wants something here that someone else named
will act to stop, take, or expose. A refuge has a conflict too: what threatens
it. A routine (opening hours, a daily delivery) is life, not conflict.

Done when the conflict names who presses on whom, by name, and the trajectory
names what the other side does here, and when, if nobody intervenes (the
place is taken, closed, exposed, destroyed, or claimed), soon enough that the
party's visit can change it.

### 3. Make it this place and no other

1. **Stock version.** Write one line naming the generic version: "a dockside
   fish stall", "a sea cave", "a ruined watchtower". Everything that line
   predicts is furniture.
2. **Twist.** Push the fantastic element into the physical structure. The place
   is built from, shaped by, or bent around a piece of campaign canon: the
   creature's shed hide roofs the stalls, the flood left the chapel's bell in
   the treetops, the faction's toll chain is also the only handrail.
3. **Rule of the place.** One reliable thing that works differently here, its
   limit or price, and one way players can test it before they depend on it.
4. **Signatures.** Three concrete details players can act on: one spatial (a
   shape to climb, cross, or hide in), one sensory with its source, and one
   behavioural (a habit the people or creatures here keep).
5. **Swap test.** Put a neighbour's name, or a generic label, in place of this
   place's name. Every sentence that stays true is furniture; replace it with
   something from the inventory, the twist, or the rule. Then write one
   sentence contrasting this place with its linked neighbours. It goes into
   At a Glance.

Done when the twist, rule, and signatures all fail the swap test, meaning each
is true only here.

### 4. Weave the canon into the ground

Read [references/weave.md](references/weave.md). Build the **weave map** in
working notes: one row for every inventory entry and every invented element.

| Element | Where | Tell | Truth | Use | Find |
|---|---|---|---|---|---|
| `[[slug]]` or invention | the node or feature it sits in, and why there | the durable perceivable sign it leaves | the DM answer, by name | the verb it invites and what that changes | how a closer look, check, or action turns the tell into the truth |

Environmental storytelling lives here: for one or two past events the inventory
supports, leave the evidence in the place and keep the explanation on the DM
page, so players rebuild what happened from the traces.

Done when every inventory entry has a filled row or a written reason it does
not live here, every required secret has three clue vectors across different
features, every hazard has sign, trigger, effect, counterplay, bypass, and
leverage, and no Truth cell is vague.

### 5. Build the structure and the life

Read [references/topology-and-life.md](references/topology-and-life.md) for
the node card, faction sheet, location moves, and pressure; read
[references/rules-and-place-types.md](references/rules-and-place-types.md) for
2024 mechanics and the adjuster for this place type.

- **Topology.** Nodes and edges before prose. Aim for two or more approaches, a
  loop, a bypass, a retreat, and a route tradeoff. Every edge changes a choice.
- **Neighbours.** North, East, South, and West, each a wikilink with
  `~n days of travel` (or hours, for a site inside a settlement). Where canon
  names no neighbour, say what lies that way at the scale play needs (open
  water, unbroken jungle); when play will travel there, cast a neighbour from
  existing places or propose one.
- **Verb test.** Every significant node invites a verb that changes a route,
  clue, resource, relationship, or pressure.
- **Life.** Who is here now, doing what, wanting what; or the sign of who is
  gone. A working place (a shop, stall, inn, or post) has its keeper on duty.
  Anyone the party will talk to, bargain with, or be stopped by is a named
  person with an NPC page, cast before minting; a person no page covers is
  minted through `npc-design` at Incidental or Scene scale before the page
  names them. Only rank-and-file the party will not single out share one
  faction or creature page. Two to four location
  moves with a named actor, trigger, visible result, new opportunity, and lasting
  consequence; at least one runs on its actor's own clock (the conflict's next
  step), whatever the party does.
- **Enemies vanished.** With every hostile removed, players still have things
  to learn, use, alter, bargain over, navigate, or choose.

Done when every significant node passes the verb test, every row of the
weave map sits on a node, and every person the party will deal with is named
and links an NPC page.

### 6. Hand the look to theatre-of-the-mind

The Overview `[!narration]` is the players' first look and the surface that
carries every tell. Build the **narration packet** as fragments, each with its
source:

- **Frame:** size and shape at body scale or travel time; ground, light, air.
- **Focus:** the one image players will remember, usually the twist made
  visible.
- **Routes:** ways in, out, up, and down, in the directions the page states.
- **Senses:** at least one beyond sight, each with its source.
- **Tells:** every Tell cell from the weave map, written as the perceivable
  fact only ("the bars of the end cage bend outward"), never its truth.
- **Affordances:** at least one thing a visitor can use.
- **Leave out:** every Truth, DC, and mechanic; names the players have not
  earned; current inhabitants and events (they belong to Who and to scenes).

Load `.agents/skills/theatre-of-the-mind`, portrait mode, place recipe, and
give it the packet. Its place recipe owns how tells are written and how long
the portrait runs.

Done when the returned narration passes theatre-of-the-mind's final check and
contains every tell. A missing tell goes back to theatre-of-the-mind named.

### 7. File the page

Copy `wiki/templates/place.md` and fill the place jobs from `wiki/AGENTS.md`
Layout. Omit empty sections. Write complete sentences. Wikilink every owner
page; numbers and stat blocks stay on their owner page ("resolve on
[[owner]]").

| Section | Carries |
|---|---|
| Overview | The narration from step 6, nothing else |
| At a Glance | What the place is now, what it sits between, the relative-identity sentence, the rule of the place, the present conflict by name and its trajectory with a time, and what skipping it costs |
| If the party | Navigation verbs first (arrive, cross, climb, descend, leave by), then interaction verbs. Each entry: the changed situation, a 2024 check only when the outcome is uncertain, what they find, and what it costs |
| Who | Who is here, how many, doing what, wanting what; location moves with trigger and visible result; or the sign of absence and who is not here |
| What | Features, items, hazards, flora, and fauna. Each entry opens with its tell, quoting the narration phrase in italics, then states its truth and its find |
| Where | **North:** / **East:** / **South:** / **West:** lines with wikilinks and travel time, or what lies that way |
| Why | Why a party comes, stays, returns, or cares |

The quoted phrase in What is the **narration key**: when a player pulls on a
detail from the spoken look, the DM finds its truth in one glance.

Run `wiki lint <path>`, then `wiki lint fix <path>` for deterministic repairs,
and rerun until green.

Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- The canon inventory is complete; every entry is woven onto a node or dropped
  with a reason.
- The twist, rule of the place, and signatures fail the swap test.
- Every secret, item, hazard, trace, and presence has a tell in the narration
  and, in What or If the party, its truth and its find. Required secrets have
  three clue vectors.
- The narration came from theatre-of-the-mind, passes its final check, and
  holds no truth, DC, or unearned name; its tells read as ordinary description.
- Topology offers real choices; every significant node passes the verb test;
  Where has four cardinal lines, each a neighbour with travel time or what
  lies that way.
- The conflict has named sides and a trajectory with a time; at least one
  location move runs on its actor's own clock; everyone the party will deal
  with is named and links an NPC page.
- Each new mint names, in the response, the candidates considered and why none
  fit (`docs/agents/table-ready.md` § Cast before minting).
- Every page filed passes the world-voice search (`docs/agents/table-ready.md` §
  Fill the silence).
- The enemies-vanished test passes; a revisited place keeps its history.
- `[!narration]` is the only callout; the DM layer names who, what, and why.
- Every owner was cast or minted first. User-said canon is filed; every
  invention is canon under the rule in `llm-wiki`, marked on the page and listed in the response.
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
