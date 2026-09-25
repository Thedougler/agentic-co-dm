---
name: dungeon-design
description: >-
  Design and stock ordinary dungeons and campaign megadungeons for D&D 5.5e
  (2024 rules). Use when creating a micro-delve, session dungeon, large site,
  megadungeon, island or region pointcrawl, outdoor megadungeon, expedition
  loop, faction stocking, pressure or rest procedures, location keys, or
  decision graphs. Use before writing room-by-room fiction or theatre-of-the-mind
  prose for a site.
---

# Dungeon design

A dungeon is a **site the party explores by choosing routes under
pressure**: something is happening inside, someone wants something there, the
ways through branch and reconnect, and every room gives the players something
to learn, use, alter, or decide. The DM needs a decision graph, keyed areas
findable in seconds, a pressure procedure that moves when the party dawdles,
and the numbers for everything they could fight.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named dungeon, site, or expedition (existing page or one to
  mint), the caller's objective and brief, `wiki/templates/place.md`, the
  skeletons in `references/`, and the vault canon the site touches: builders,
  occupants, factions, creatures, items, the party's level and goals.
- **Work:** The seven-part test, the construction pipeline, and the filing step
  below, for this one site. Keep the caller's objective.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** A named occupant, faction, creature, item, or
  neighbouring place the dungeon needs is cast before it is minted
  (`docs/agents/table-ready.md` § Cast before minting): an in-play or
  unrevealed page that fits comes first, and its owner skill (`npc-design`,
  `faction-design`, `monster-design`, `item-design`, `place-design`) mints one
  only when none fits, before any key depends on it (AGENTS.md **HARD:
  entity-before-spoken**, **Focused minting**). Encounter difficulty →
  `encounter-prep`; hazards → `traps-trials`; checks → `dnd5e-mechanics`. The
  site's spoken look and room first impressions → `theatre-of-the-mind`. Each
  child returns its page path or prose and its completion result; resume at the
  step that waited on it.

## Page rules

These hold in every step.

- **Canon.** User-said facts file immediately on the live path. Whatever the
  dungeon needs that canon leaves silent, records as unknown, or contradicts
  (rooms, defenders, entrances, contents), decide now as canon under the rule in `llm-wiki`
  (`docs/agents/table-ready.md` § Fill the silence): one concrete answer,
  stated on the page as world fact where the DM uses it, with the page marked
  `invention: true`. The response lists each proposal with the `[[pages]]` it
  grows from; a proposal that settles a contradiction names the sources and the
  reading it chose, so the DM picks the winner.
- **Preserve.** Improving an existing page keeps every established detail;
  fold each one into the key or section that now owns it.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the seven-part test, the pipeline, and
  `## Done` below.
- **Honest capabilities.** Flight, teleportation, and divination work here;
  the site answers them with costs, exposure, or limits that have a reason in
  the fiction.
- **The owner's power shows.** A site made or held by a powerful creature
  carries that power: wards, guardians, and lair features in its style, and the
  owner's awareness or return on the pressure clock. Danger beyond the party's
  level is telegraphed and avoidable; the way to the objective runs through
  danger the party can beat.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). Every tell,
  secret, and hidden route has its truth on the page by name. Truths, clocks,
  and DCs stay out of `[!narration]`.
- **Process stays off the page.** The seven-part test, truth sentences, graph
  notes, and stocking ledger are working notes; the page carries the facts,
  the graph, the keys, and the procedures.

## Run the seven-part test

| Part | Ask | If blank |
|---|---|---|
| Promise | What experience, image, or question does this site promise? | Cut generic dressing. |
| Purpose | Why does it exist, and why does it matter now? | Give it a function or delete it. |
| Pressure | What advances, notices, depletes, or worsens? | Add a visible clock, cost, or consequence; telegraphed danger beats an ambush HP tax. |
| Paths | What are the meaningful routes, loops, bypasses, and retreats? | Redraw the graph before keying. |
| Powers | Who wants, fears, uses, or contests the site? | Add active factions, not stat blocks. |
| Payoffs | What information, leverage, treasure, access, or change can play earn? | Replace encounter quota with rewards. |
| Persistence | What remains, changes, or becomes known after the party leaves? | Add causal restocking and campaign memory. |

These are the seven engagement conditions: promise, purpose, pressure, paths,
powers, payoffs, and persistence. A blank Pressure or Paths makes a flat
dungeon even when the rooms are vivid.

## Choose scale before detail

| Scale | Practical default | Design consequence |
|---|---|---|
| Micro-delve | 1–5 keyed locations | One strong situation; finish in a short outing. |
| Session dungeon | 10–20 locations | A route, loop, faction problem, and one or two sessions of choices. |
| Large site | 30+ locations | Zones, multiple approaches, rest decisions, and a durable relationship map. |
| Megadungeon | Campaign-sized | Repeated expeditions, route mastery, restocking, changing occupants, and a goal portfolio. |

Use Justin Alexander's structural distinction: a megadungeon is not merely a
large map; it supports repeated expeditions whose routes and consequences
matter. If the intended use is one session, do not build campaign machinery.
If the intended use is a campaign, do not make one linear clear-the-site quest.

## Ordinary construction pipeline

Start with the **canon inventory**: read the site page if it exists and every
page that links to it (`grep -rliF "[[<name>" wiki/entities` for the slug,
title, and each alias), search QMD per AGENTS.md § Vault retrieval for its
builders, occupants, factions, creatures, items, and sessions, and `qmd get`
every hit you use. Write one working-note line per owner page: `[[slug]]` ·
kind · the fact that puts it in this site. Each history layer, faction, and
payoff below comes from the inventory before it is invented.

1. **Write dungeon truth in five sentences:** Original purpose; Rupture;
   Current conflict; Immediate promise; Deep truth. Keep these as GM truth, not
   read-aloud. From one premise you should get architecture, history, factions,
   present action, and a discoverable reward.
2. **Add 2–3 history layers.** For each layer record builders/occupants,
   purpose, surviving trace, and the conflict it leaves behind. Delete lore that
   does not affect a choice, clue, route, faction, or payoff.
3. **Divide into zones.** Give each zone a job, sensory signature, dominant
   obstacle, inhabitants, access routes, escalation, and likely payoff. A zone is
   a playable relationship, not just a color on a map.
4. **Draw the decision graph before the detailed map.** Nodes are situations or
   decision points; edges are routes, costs, information, and consequences.
   Pressure nodes should expose at least three materially different response
   paths; never make one hidden answer the only route forward. As
   practical defaults, use two entrances when fiction allows, at least one loop,
   one bypass, one vertical or otherwise unusual connection, one optional danger,
   and two approaches to each major objective. This is Xandering: make choices
   branch and reconnect without turning every corridor into a maze. A linear
   dead-end branch map fails unless linearity is the deliberate pressure.
5. **Give each active faction a sheet:** Want, Fear, Method, Resources, Tell,
   Offer, Response. State what each faction does between visits and what changes
   if the party bargains, helps, deceives, or attacks.
6. **Stock for interaction, not a fight quota.** Mix inhabitants, social
   situations, hazards, clues, discoveries, resources, empty/quiet spaces,
   treasure, and transitions. For every quiet room ask: what can the players
   learn, use, alter, or use as a route or mood beat? If the answer is nothing,
   merge or cut it.
7. **Treat information as a reward economy.** Give essential revelations
   multiple vectors: witness, physical trace, document, faction offer, spatial
   pattern, and consequence. A clue should point to a decision, route, power, or
   payoff; never make one failed roll the only way to know a necessary fact.
   Separate Passive Perception (what is noticed without an active search) from a
   declared Search/Investigation or other action (what a character examines and
   may resolve). Do not use a hidden check to decide whether play can continue.
8. **Build obstacles with six fields:** Sign, Trigger, Effect, Counterplay,
   Bypass, Leverage. Telegraph the sign, name the trigger in fiction, make the
   effect consequential, and add a fuse when delay should change the problem. A
   revealed trap is a puzzle; a puzzle plus a fuse is a scene. Do not use a
   hidden step → damage tax with no informed choice. Provide at least one fair
   counterplay and one bypass. Leverage rewards prior information, faction
   relationships, tools, or terrain rather than a single correct key.
9. **Design encounters by job, not creature count.** Record Function,
   Objective, Stakes, Terrain, Information, Escalation, Off-ramps, and
   Aftermath. Calibrate a 2024-rules encounter as Low/Moderate/High only after
   deciding its job and stakes; budgets estimate difficulty, not quality. Give
   every hostile encounter a readable non-combat option, retreat, bargain, or
   objective that can end the scene.
10. **Set the pressure procedure.** Choose the moving threat, visible clock,
    advance trigger, alert state, delay cost, and consequence before keying. Use
    the procedure in
    [references/procedures.md](references/procedures.md), then test whether a
    party can understand and influence it.
11. **Make rest a strategic choice.** Short Rest is 1 hour; Long Rest is 8 hours
    or more, and after a Long Rest use a 16-hour wait before another Long Rest
    as the practical 2024-rules procedure. Fiction answers safety: a haven,
    defensible shelter, host, or hostile site changes the result. Record what
    factions do while the party waits.
12. **Key only after the graph works.** Use the keying order: obvious first
    impression → current activity → interactives → hidden information →
    mechanics. Quiet landmarks need less text; hazards and decision nodes need
    more. The template is diagnostic, not a quota.

## Megadungeon deltas

- Build a **portfolio of goals**, not one clear-it quest: recover, map, ally,
  escape, investigate, exploit, protect, change, and return are different goal
  engines. Let players choose what matters.
- Build a **region graph** outside the site. Prepare the next frontier, not the
  whole campaign. Distinguish durable geography from mutable occupants.
- Use an expedition loop: choose goal and loadout; travel and spend resources;
  enter and gather information; make a risk/route choice; take a payoff or
  consequence; retreat or push; resolve the return; update the site.
- Restock causally, not by reset. Ask who moved in, what was repaired, what was
  stolen, what faction learned, what route changed, and what the party's actions
  made possible. Preserve opened doors, dead leaders, alliances, damage, and
  learned routes unless the fiction changes them.
- Keep a site ledger: discovered routes, unresolved leads, faction clocks,
  depleted resources, changed landmarks, and the next prepared frontier.

## Outdoor and island megadungeons

Use [references/outdoor-scaling.md](references/outdoor-scaling.md). Nest Island or
Region → Landmark → Nested Site, and classify routes as Coast, River, Terrace,
Forest, Air, or Underway. Use a risk gradient, not level walls. Flight must be
honest: make it useful, costly, exposed, weather-dependent, or strategically
incomplete rather than silently cancelling it. An inhabited outdoor dungeon is
not a monster room to empty; progress means changing a political landscape,
relationships, access, or obligations without turning a society into loot.

## File the dungeon

Use the forms in [references/ordinary-skeleton.md](references/ordinary-skeleton.md)
or [references/megadungeon-skeleton.md](references/megadungeon-skeleton.md) as
working notes, and run [references/procedures.md](references/procedures.md) for
pressure, rest, stocking, encounters, obstacles, and QC. Cite only the public
links in [references/sources.md](references/sources.md).

Copy `wiki/templates/place.md` to `wiki/entities/place/<kebab-name>.md` (or
improve the existing page) with `type: place` and `kind: dungeon`. Fill:

| Section | Carries |
|---|---|
| Overview | The approach, from `theatre-of-the-mind`: what the party perceives where they first reach the site, with a tell for each entrance and for the pressure; room contents stay in their keys |
| At a Glance | The promise, the present conflict by name, the pressure and what happens if nobody intervenes (with a time), and the site's scale and session count |
| If the party | The approaches and big choices: each entrance, the bargain, the bypass, the retreat |
| Who | Each occupant or faction by page, with want, fear, offer, response, and what they do between visits; fighters with compact numbers or statblock links |
| What | Treasure, items, hazards, and clues, each by owner link or with its numbers. Treasure fits the party's level and the danger: coin by amount and at least one magic item, cast from existing item pages first (`item-design` mints one when none fits) |
| Where | The neighbours and what lies outside each exit |
| Why | Why a party comes, and what they leave with |
| Map and keys | The decision graph as a node list with edges (route, cost, what it reveals), then one keyed subsection per area in the keying order: first impression, current activity, interactives, hidden information, mechanics |
| Running the dungeon | The pressure procedure (site turn, alert states, advance triggers, the clock with its ticks), rest safety, and restocking after a visit |

Each keyed area names its size in feet where position matters, carries every
check as Ability (Skill) and DC, and every creature by count, page link, and
compact numbers. Encounters carry their job, 2024 difficulty for the party's
level, and an off-ramp.

Run `wiki lint <path>`, then `wiki lint fix <path>` for deterministic repairs,
and rerun until green.

Then run the **cross-reference pass**: for every key, list each other area,
creature, item, or count it names, open that area's key, and make both say
the same thing (where a route leads, how many guards, where the key or item
lies); then check each graph edge against both areas' keys. Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- All seven parts of the test are answered on the page: promise, purpose,
  pressure, paths, powers, payoffs, persistence.
- The decision graph has two entrances where the fiction allows, a loop, a
  bypass, an unusual connection, a retreat, and two approaches to each major
  objective; no hidden answer is the only way forward.
- Every keyed area gives something to learn, use, alter, or decide, in the
  keying order, with checks as Ability (Skill) and DC.
- Every occupant and faction links a page and states want, offer, and response;
  every fighter has compact numbers; every encounter has a job, a 2024
  difficulty for the party, and an off-ramp. Ordinary fights sit at Moderate,
  at least one fight reaches High by the 2024 XP budget, and anything deadlier
  is telegraphed with a way around it.
- The owner's power shows in wards, guardians, or lair features, and its
  awareness or return sits on the pressure clock.
- One signature area, built from the owner's canon, changes during play (it
  floods, wakes, collapses, turns, or burns).
- Each essential revelation has three vectors; each obstacle has sign,
  trigger, effect, counterplay, bypass, and leverage.
- The pressure procedure has a visible clock with ticks and triggers; rest
  safety and what occupants do while the party rests are stated.
- Payoffs name the treasure (coin by amount, and at least one magic item by
  owner link), information, and leverage, sized for the party's level and the
  danger faced.
- Every keyed area appears in the decision graph, and every edge in the graph
  appears in the keys of both areas it joins.
- Every mechanic that more than one key mentions (a trigger, a clock tick, a
  door, a timing) reads the same in each.
- The Overview came from theatre-of-the-mind, shows the approach rather than a
  list of rooms, and holds no truth, DC, or unearned name.
- Every owner was cast or minted first. Each new mint names, in the response,
  the candidates considered and why none fit (`docs/agents/table-ready.md` §
  Cast before minting).
- User-said canon is filed; every invention is canon under the rule in `llm-wiki`, marked on the
  page and listed in the response.
- Every page filed passes the world-voice search (`docs/agents/table-ready.md`
  § Fill the silence).
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
