---
name: city-design
description: >-
  Write, edit, or create named city pages for the campaign wiki. Use when a
  city, metropolis, capital, port city, districted settlement, missing named
  city note, city arrival, urban orientation, gazetteer, local table rules,
  city pressure, active urban situation, or city change log needs a persistent
  page. Fill wiki/templates/city.md. place-design is the place hub and defers
  kind: city page work here.
---

# City design

A city page is a **table interface for a crowd**: the party arrives, finds its
way, gets what it came for, and walks into trouble already in motion. The DM
needs districts the party can choose between, places they can seek on
purpose, local rules that change a choice, named people with wants, and two or
more **situations**: opposed wants between named sides, each heading somewhere
soon if nobody steps in. Everything a newcomer can see leaves a **tell**; the
DM page carries the truth.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named city (existing page or one to mint), the caller's
  objective and brief, `wiki/templates/city.md`, and the vault canon it
  touches: region, districts, landmarks, factions, NPCs, quests, sessions.
- **Work:** The steps below, for this one city. Keep the caller's objective.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** A named person, faction, site, item, or creature the
  city needs is cast before it is minted (`docs/agents/table-ready.md` § Cast
  before minting): an in-play or unrevealed page that fits comes first, and its
  owner skill (`npc-design`, `faction-design`, `place-design`, `item-design`,
  `monster-design`) mints one only when none fits, before any text depends on
  it (AGENTS.md **HARD: entity-before-spoken**, **Focused minting**). Full
  faction agendas stay on faction pages; off-screen turns → `world-tick`. The
  header look → `theatre-of-the-mind` with the packet from step 6. Each child
  returns its page path or prose and its completion result; resume at the step
  that waited on it.

## Page rules

These hold in every step.

- **Canon.** User-said facts file immediately on the live path. Whatever the
  city needs that canon leaves silent, records as unknown, or contradicts,
  decide now as canon under the rule in `llm-wiki` (`docs/agents/table-ready.md` § Fill the
  silence): one concrete answer, stated on the page as world fact where the DM
  uses it, with the page marked `invention: true`. The response lists each
  proposal with the `[[pages]]` it grows from; a proposal that settles a
  contradiction names the sources and the reading it chose, so the DM picks the
  winner.
- **Preserve.** Improving an existing page keeps every established detail
  (districts, landmarks, customs, population, authorities, history); fold each
  one into the section that now owns it. Closed campaign history stays history.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the steps and `## Done` below.
- **Template.** `type: place`, `kind: city`, on `wiki/templates/city.md`;
  sections that change no current play are omitted, never left empty.
- **Choices stay with the players.** The page gives what the city does and
  what each approach costs; the party's civic choices are left to play.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). Every tell,
  rumor, and situation has its truth on the page: who, what, why, and what is
  at stake, by name. `[!narration]` is the only callout.
- **Process stays off the page.** The inventory, identity sentence, and packet
  are working notes; the page carries only their facts.

## Steps

Read [references/city-craft.md](references/city-craft.md) before step 3.

### 1. Take the canon inventory

Retrieve before inventing (constitution XII), using QMD per AGENTS.md § Vault
retrieval (`.agents/skills/qmd`).

1. Read the city page if it exists, its region page, and every page that links
   to it: run `grep -rliF "[[<name>" wiki/entities` once for the slug, the
   title, and each alias.
2. Search QMD for the city, its districts and landmarks, its authorities,
   every faction and NPC tied to it, and every session set there.
3. `qmd multi-get` every related hit you will use, in one call. Snippets are leads, not facts.

```bash
# CORRECT — comma-separated #docid values from search results
qmd multi-get "#abc123,#def456" --format md

# CORRECT — brace-expanded paths
qmd multi-get 'entities/faction/{the-passage.md,antheri.md}' --format md

# WRONG — qmd:// URIs (rejected with "File not found")
qmd multi-get "qmd://entities/faction/the-passage.md,qmd://entities/faction/antheri.md"
```

Pass `#docid` values from the query, comma-separated, or a brace glob. `--format md`. One hit: `qmd get` with that identifier. Rejected id: serial `qmd get`.

Write the **canon inventory** in working notes, one line per owner page:
`[[slug]]` · kind · the fact that puts it in this city.

Done when every backlink and relevant hit is in the inventory or dropped with a
one-line reason, and every inventory page was read in full. A person, faction,
business, or creature based in the city always gets a place on the page (in
Power, the gazetteer, a situation, or the street); only pages that mention the
city in passing are dropped.

### 2. Find the city's engine

In working notes, write the **identity sentence**:

> This is a [kind/scope] city known for [public identity], pressured by
> [current instability], and it gives players [choice or opportunity].

Then the **engine**: what the city lives on (a trade, a toll, a shrine, a yard,
a court) and who controls each part of it. The situations in step 4 grow from
the engine: whoever controls it, whoever wants it, whoever it squeezes.

Done when the engine names what the city lives on and who holds each part by
page.

### 3. Lay out the city

- **Districts.** Three to six, each with the reason a visitor goes there, who
  holds it, one danger or opportunity there now, and its street-level look as
  a spoken `_italic_` line in the table's Narration column.
- **Landmarks and getting around** (bullets under the Districts table). Two or
  three **Landmark** bullets a newcomer steers by; one **Getting around**
  bullet: how long crossing takes, what changes after dark, and where movement
  is restricted and by whom.
- **Services.** Arrive and leave (who meets a ship, what it costs, what
  papers), stay, buy supplies, sell cargo and loot (a named buyer and the rate
  they pay, and a fence for goods with a history), services: each entry a named
  place and its keeper, a price, and one detail that makes it this city's.
- **Local Rules.** Two to four local laws or customs that change a
  choice, each with who enforces it, how, and the penalty.

Done when a party could arrive, find lodging, sell cargo, and cross the city
from the page alone, and each rule names its enforcer and penalty.

### 4. Set the situations in motion

Two or more **situations**. A situation is opposed wants: someone named wants
a change here that someone else named will act to stop, take, or expose. For
each: the sides by page, the visible signs a newcomer could notice, what each
side wants, **If nobody intervenes** (what happens, and when: within days of
the party's arrival), and two or more handles the party could pick up, with
what each costs. At least one situation touches something the party already
cares about (a PC's tie, a thread from play, the reason they came).

Each situation is a `###` with **Involved**, **Visible signs**, **Wants**, and
**If nobody steps in** bullets, then its handles.

Then **Power**: each faction's local posture (public position, local
objective, leverage, current move here), then **Who holds what** (who rules,
keeps order, controls money, information, and the streets) and the **Fault
line** that keeps these powers from settling. Pressure clocks and upcoming events
with dates sit on the situation they drive. Each faction in Power
has a **local face**: the named person (an NPC page) who carries its current
move in this city and whom the party can meet, bribe, or cross.

At least one situation turns physical: a heist, chase, raid, brawl, rescue,
storm, or creature the party meets with steel or daring, staged at a
**set piece**, a city location built for action (a bridge, a crane, a reef
gap, a rooftop), with its size and two features a fight or chase can use.

Done when every situation has named sides, signs, a trajectory with a time,
and two handles with costs; one of them is physical and staged at a set
piece; and every faction in Power has a named local face.

### 5. Fill the street

- **Rumors.** What people say, each with its truth on the DM layer.
- **Random Encounters.** A d6 or d8 table of street moments, each tied to a
  conflict, a district, or a faction, with what happens if the party engages
  and a spoken `_italic_` line in the Narration column.
- **Names.** Under Random Encounters, six to ten names in the city's naming style, for
  improvised people.
- **Faces.** Everyone who drives a situation, holds power, or keeps a gazetteer
  place the party will use this arc is a named NPC page, cast first; a person no
  page covers is minted through `npc-design` at Incidental or Scene scale.
- **Numbers.** The watch, guards, or gangs the party could fight: a count and
  a statblock with compact numbers.

Done when every rumor has its truth, every encounter has its hook, and every
face named on the page links an NPC page.

### 6. Hand the look to theatre-of-the-mind

Build the **narration packet** as fragments, each with its source: scale and
silhouette from the approach, movement at the gate or harbour, one sound and
one smell with sources, the landmark a newcomer steers by, and the tells of the
situations a newcomer could see. Leave out truths, DCs, and names not earned.
Load `.agents/skills/theatre-of-the-mind`, portrait mode, place recipe, and give
it the packet. The result is the `[!narration]` under the title,
titled with the city's name. The Districts and Random Encounters Narration cells are
situated lines from the same skill (zone-cell recipe).

Done when the returned narration passes theatre-of-the-mind's final check and
carries the situations' visible signs.

### 7. File the page

Copy `wiki/templates/city.md` to `wiki/entities/place/<kebab-name>.md` with
`type: place` and `kind: city`; add region, population, government, ruler, and
controlling_faction only when they have values. The italic identity line
under the portrait gives size, who rules, and the current pressure. Step 3
fills Districts (getting around under the table) and Services; step 4 fills
Factions (its table, then the local rules that differ from what players
assume) and Conflicts (one `###` each); step 5 fills Random Encounters, then **Rumors.**
and **Secret.** paragraphs. A city that depends on outside food, water, fuel,
or trade says so in a **Depends on.** paragraph, with what happens when that
route fails. Keep a section only when you have facts for it (fact-only,
`wiki/AGENTS.md` Layout). Write complete sentences. Wikilink every owner page.

Run `wiki lint <path>`, then `wiki lint fix <path>` for deterministic repairs,
and rerun until green.

Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- The canon inventory is complete; every established detail is kept.
- The engine names what the city lives on and who holds it.
- Every person, faction, business, or creature based in the city has a place
  on the page.
- Districts, landmarks, getting around, and the gazetteer let a party arrive,
  lodge, buy, sell cargo, and cross the city from the page alone; gazetteer
  entries have keepers and prices.
- Each local rule names its enforcer and penalty.
- Two or more situations have named sides, visible signs, a trajectory within
  days of arrival, and two handles with costs; one touches what the party
  already cares about; one is physical and staged at a set piece with its
  features.
- Every faction in Power has a named local face with an NPC page.
- Rumors carry their truths; encounters tie to situations; the fighters the
  party could face have numbers.
- Every face named on the page links an NPC page.
- The header narration came from theatre-of-the-mind and holds no truth, DC, or unearned
  name.
- Every owner was cast or minted first. Each new mint names, in the response,
  the candidates considered and why none fit (`docs/agents/table-ready.md` §
  Cast before minting).
- User-said canon is filed; every invention is canon under the rule in `llm-wiki`, marked on the
  page and listed in the response.
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
