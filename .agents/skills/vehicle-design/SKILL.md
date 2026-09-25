---
name: vehicle-design
description: >-
  Design named, playable vehicle pages for the campaign wiki, especially ships
  and boats. Use when a craft needs a persistent identity, travel role, crew,
  components, handling, chase or boarding play, or a DM-ready vehicle note.
  Fill wiki/templates/vehicle.md, including the sheet and component figures.
---

# Vehicle design

A named vehicle is a **place that moves, with a crew that wants something**.
The party chases it, flees it, boards it, sails it, hides aboard it, or sells
it. Players meet it by its silhouette first, so everything the craft hides (its
true flag, its cargo, its damage, its crew's intent) leaves a **tell** they can
spot across the water. The DM page states the truth behind every tell and the
numbers to run the craft tonight.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named craft (existing page or one to mint), the caller's
  objective and brief, `wiki/templates/vehicle.md`, and the vault canon the
  craft touches: owner, captain, crew, berth, routes, cargo, pursuers.
- **Work:** The steps below, for this one craft. Keep the caller's objective.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** A named captain, crew member, owner, berth, item, or
  creature the craft needs is cast before it is minted
  (`docs/agents/table-ready.md` § Cast before minting): an in-play or
  unrevealed page that fits comes first, and its owner skill (`npc-design`,
  `faction-design`, `place-design`, `item-design`, `monster-design`) mints one
  only when none fits, before any text depends on it (AGENTS.md **HARD:
  entity-before-spoken**, **Focused minting**). Checks and DCs →
  `dnd5e-mechanics`. The spoken look → `theatre-of-the-mind` with the packet
  from step 6. Each child returns its page path or prose and its completion
  result; resume at the step that waited on it.

## Page rules

These hold in every step.

- **Canon.** User-said facts file immediately on the live path. Whatever the
  craft needs that canon leaves silent, records as unknown, or contradicts,
  decide now as canon under the rule in `llm-wiki` (`docs/agents/table-ready.md` § Fill the
  silence): one concrete answer, stated on the page as world fact where the DM
  uses it, with the page marked `invention: true`. The response lists each
  proposal with the `[[pages]]` it grows from; a proposal that settles a
  contradiction names the sources and the reading it chose, so the DM picks the
  winner.
- **Preserve.** Improving an existing page keeps every established detail
  (name, class, chassis, owner, berth, crew, damage, history); fold each one
  into the section that now owns it. A craft keeps its class: an upgrade is a
  proposal on the same chassis.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the steps and `## Done` below.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). Every tell
  has its truth on the page: who, what, why, and what is at stake, by name.
- **Choices stay with the players.** The page gives the craft's orders, crew
  responses, and consequences; what the party does aboard or against it is
  left to play.
- **Process stays off the page.** The inventory, identity sentence, and packet
  are working notes; the page carries only their facts.

## Steps

### 1. Take the canon inventory

Retrieve before inventing (constitution XII), using QMD per AGENTS.md § Vault
retrieval (`.agents/skills/qmd`).

1. Read the craft page if it exists and every page that links to it: run
   `grep -rliF "[[<name>" wiki/entities` once for the slug, the title, and each
   alias.
2. Search QMD for the craft, its class or sister ships, its owner, captain,
   berth, routes, cargo, and any session where it appeared.
3. For every craft this one chases, fights, carries, or is compared with, run
   `qmd search "<its name>" -c wiki` and read every page about it (the craft,
   its manifest, deck plans, crew roster); list those pages in the inventory.
   Their numbers are canon this page must respect.
4. `qmd get` every hit you will use. Snippets are leads, not facts.

Write the **canon inventory** in working notes, one line per owner page:
`[[slug]]` · kind · the fact that ties it to this craft.

Done when every backlink and relevant hit is in the inventory or dropped with a
one-line reason, and every inventory page was read in full.

### 2. Give it an errand

In working notes, write the **identity sentence**:

> This is a [ship/boat/other] that [role], recognized by [silhouette or
> operational signature], and it gives players [choice or pressure].

Then the craft's **errand**: who commands it now (a named NPC page), what it is
doing this week and for whom, its standing orders when it meets the party (hail,
inspect, pursue, flee, trade, board), and what it does next if nobody
interferes. A vehicle with an errand collides with play; a vehicle at anchor is
scenery. Take the errand from the inventory whenever it offers one: a patrol
route, a debt, a cargo run, a hunt.

Done when the captain is named, the orders say what the craft does on meeting
the party, and the errand has a next step with a time.

### 3. Make it this craft and no other

1. **Stock version.** Name the generic craft ("a navy cutter", "a fishing
   smack"). Everything that line predicts is furniture.
2. **Signature.** One silhouette tell recognizable at a mile (a patched sail,
   an odd rig, a figurehead, a smoke plume) and one close-up detail a boarder
   meets.
3. **Quirk.** One way this craft handles differently from its class, with its
   limit and how a crew or a watcher can learn it (it points higher into the
   wind but loses way in a turn; its stern gun cannot bear on the port
   quarter).
4. **Hold.** One thing aboard someone would pay, fight, or lie for: cargo,
   papers, a prisoner, a flag it should not carry. Its tell and its truth.
5. **Swap test.** Put a sister ship's name in place of this one. Every sentence
   that stays true is furniture; replace it from the inventory, the errand, or
   the quirk.

Done when the signature, quirk, and hold each fail the swap test.

### 4. Put numbers on it

Read [references/vehicle-craft.md](references/vehicle-craft.md). Anchor the
numbers on the closest official 5e craft of the same role and size, adjusted by
the quirk:

- **Sheet:** Size, Type, Speed (with mode), Crew (min), Passengers, Cargo.
- **Components:** Hull AC, HP, and damage threshold; Helm AC and HP and what is
  lost when it is disabled; Movement AC and HP and what is lost; each weapon's
  attack bonus or save DC, range, damage, crew to fire, and reload.
- **Comparisons hold.** A canon comparison (faster than, better armed than,
  larger than a named craft) holds against that craft's established numbers.
  Open its page and every page it links for cargo, manifest, or deck detail,
  and write the comparison in the working notes as numbers: speed against
  speed, length against length, and for armament the total average damage
  per round of every weapon each craft can fire. The other craft's canon stays
  as it is; when the comparison fails, raise this craft's numbers. The page
  states only this craft's numbers; the arithmetic stays in the notes.
- **Crew as fighters.** Size the crew to the craft's job and the party's
  level: the officers the party will cross blades with carry a statblock that
  makes a boarding a real fight for this party (a navy captain is a Veteran or
  better). Everyone the party could fight aboard carries compact numbers: the captain's own statblock link or a named standard statblock
  (AC, HP, Speed, the attacks or save DCs the DM will roll), the rank-and-file
  crew by count and statblock, and any beast or guard aboard.

Done when every Sheet and Components line holds a number, every fighter
aboard has numbers, and each canon comparison is written in the working notes
as two numbers with this craft's ahead.

### 5. Lay out the decks and the play loop

- **Decks.** For boarding and stowaways, three to five areas at body scale
  (weather deck, quarterdeck, hold, captain's cabin, rigging), each with its
  size in feet, one feature a fight or a sneak can use (a ladder, a hatch, a
  swinging boom, powder kegs), and who stands there on watch.
- **Crew stations.** Each station: who mans it now against the minimum, the
  action or check it runs, and what fails when it is empty.
- **Handling.** Two to four manoeuvres or conditions that change a choice, each
  with its check (Ability (Skill) and DC) and its result: the quirk, wind and
  current, tight water, repairs underway.
- **Chase and boarding.** How a pursuit with this craft runs, in **chase
  turns** sized so the gap changes by a real step each turn and the chase ends
  in three to eight turns (a round when ships are close, a minute or ten when
  they are far, a watch across open sea): its speed against a typical pursuer
  or quarry, what closes or opens the distance each turn,
  when grapples or boarding planks become possible, ramming damage, and when
  the crew strikes colours, cuts loose, or fights to the last. Leave out the
  Combat section only when the craft will never be chased, fought, or boarded.

Done when a DM could run a chase, a boarding, and a stowaway sneak from the
page alone.

### 6. Hand the look to theatre-of-the-mind

Build the **narration packet** as fragments, each with its source:

- **Frame:** size at body scale, silhouette, rig, and how it sits in the water.
- **Focus:** the signature from step 3, made visible.
- **Access:** where a boat comes alongside, where a climber gets up, what the
  deck looks like from the rail.
- **Senses:** at least one beyond sight, with its source.
- **Tells:** the perceivable sign of the hold, the quirk, and any damage or
  false flag, never their truth.
- **Leave out:** every truth, DC, mechanic, and name the players have not
  earned.

Load `.agents/skills/theatre-of-the-mind`, portrait mode, vehicle recipe, and
give it the packet.

Done when the returned narration passes theatre-of-the-mind's final check and
contains every tell. A missing tell goes back to theatre-of-the-mind named.

### 7. File the page

Copy `wiki/templates/vehicle.md` to `wiki/entities/vehicle/<kebab-name>.md`
with `type: vehicle` and a `kind` for the craft (ship, boat, or other). Fill
the vehicle jobs from `wiki/AGENTS.md` Layout. Omit empty sections. Write
complete sentences. Wikilink every owner page.

| Section | Carries |
|---|---|
| Narration | The narration from step 6, nothing else |
| Sheet, Components | The numbers from step 4 |
| Decks | The areas from step 5; omit for a craft too small to walk |
| Crew stations | Stations, who mans them now, and the fighters' compact numbers |
| Handling | Manoeuvres, the quirk, and the chase loop |
| Combat | Initiative, boarding, ramming, component targeting, surrender, sinking |
| At a Glance | The captain, the errand and its next step, standing orders on meeting the party, and why the party cares |
| Hidden Cargo & History | The hold and every other tell's truth, by name, with how it is found |
| Connections | Each tie by owner link and what it does at the table |

Run `wiki lint <path>`, then `wiki lint fix <path>` for deterministic repairs,
and rerun until green.

Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- The canon inventory is complete, including every page about each craft this
  one chases or is compared with; every established detail is kept.
- The captain is named with a page; the errand, standing orders, and next step
  with a time are in At a Glance.
- The signature, quirk, and hold fail the swap test; each tell in the narration
  has its truth and its find on the page.
- Every Sheet and Components line holds a number anchored on a 5e peer craft;
  every weapon has attack or DC, range, and damage; every canon comparison to
  another craft holds against that craft's numbers.
- Every fighter aboard has compact numbers, and the officers make a boarding a
  real fight for the party's level.
- Decks, stations, handling, and the chase and boarding loop let a DM run
  pursuit, boarding, and a stowaway from the page alone; each check has
  Ability (Skill) and DC; the chase resolves in three to eight chase turns.
- Every other page the work edits stays whole: one narration callout, its
  established sections and numbers kept; an edit there only fills blanks.
- The narration came from theatre-of-the-mind and holds no truth, DC, or
  unearned name.
- Every owner was cast or minted first. Each new mint names, in the response,
  the candidates considered and why none fit (`docs/agents/table-ready.md` §
  Cast before minting).
- User-said canon is filed; every invention is canon under the rule in `llm-wiki`, marked on the
  page and listed in the response.
- Every page filed passes the world-voice search (`docs/agents/table-ready.md`
  § Fill the silence).
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
