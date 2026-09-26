---
name: region-design
description: >-
  Write, edit, or create named region pages for the campaign wiki. Use when a
  region, realm, province, frontier, wilderness, forest, mountains,
  archipelago, sea, valley, district, route-scale area, missing named region
  note, regional spoken look, geography, travel routes, active powers, existing
  pressure, or regional change log needs a persistent page. Fill
  wiki/templates/region.md. place-design is the place hub and defers region page
  work here.
---

# Region design

A region page is a **map of choices and motion**: the party asks "which way do
we go?" and the page answers with routes that trade time, risk, supply, and
discovery; then the region answers back with powers that move, hazards with
signs, and things worth finding. A good region gives travel its own play:
navigation that can go wrong, encounters that tell a story about who lives
there, and at least one pressure heading somewhere soon.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named region (existing page or one to mint), the caller's
  objective and brief, `wiki/templates/region.md`, and the vault canon it
  touches: parent and neighbouring regions, places, routes, powers, creatures,
  sessions.
- **Work:** The steps below, for this one region. Keep the caller's objective.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** A named place, faction, NPC, creature, or quest the
  region needs is cast before it is minted (`docs/agents/table-ready.md` § Cast
  before minting): an in-play or unrevealed page that fits comes first, and its
  owner skill (`place-design`, `city-design`, `faction-design`, `npc-design`,
  `monster-design`) mints one only when none fits, before any text depends on it
  (AGENTS.md **HARD: entity-before-spoken**, **Focused minting**). Full faction
  agendas stay on faction pages; off-screen turns → `world-tick`. The travel
  look → `theatre-of-the-mind` with the packet from step 6. Each child returns
  its page path or prose and its completion result; resume at the step that
  waited on it.

## Page rules

These hold in every step.

- **Canon.** User-said facts file immediately on the live path. Whatever the
  region needs that canon leaves silent, records as unknown, or contradicts,
  decide now as canon under the rule in `llm-wiki` (`docs/agents/table-ready.md` § Fill the
  silence): one concrete answer, stated on the page as world fact where the DM
  uses it, with the page marked `invention: true`. The response lists each
  proposal with the `[[pages]]` it grows from; a proposal that settles a
  contradiction names the sources and the reading it chose, so the DM picks the
  winner. An uncharted region stays uncharted for sailors in the world; the DM
  page carries its geography.
- **Preserve.** Improving an existing page keeps every established detail
  (scale, boundaries, landmarks, hazards, powers, tone, history); fold each one
  into the section that now owns it.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the steps and `## Done` below.
- **Named means paged.** A place, power, or creature the page names links a
  page. A feature the party only crosses (a current, a reef line, a fog bank)
  is described, not named.
- **Choices stay with the players.** The page gives routes, costs, and what
  the region does; the party's travel choices are left to play.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). Every sign,
  rumor, and hazard has its truth on the page by name. `[!narration]` is the
  only callout. `type: region`; `type: front` stays retired.
- **Process stays off the page.** The inventory, identity sentence, and packet
  are working notes; the page carries only their facts.

## Steps

Read [references/region-craft.md](references/region-craft.md) before step 3.

### 1. Take the canon inventory

Retrieve before inventing (constitution XII), using QMD per AGENTS.md § Vault
retrieval (`.agents/skills/qmd`).

1. Read the region page if it exists, its parent and neighbours, and every page
   that links to it: run `grep -rliF "[[<name>" wiki/entities` once for the
   slug, the title, and each alias.
2. Search QMD for the region, its landmarks, routes, hazards, creatures,
   powers, and every session set in or bound for it.
3. `qmd get` every hit you will use. Snippets are leads, not facts.

Write the **canon inventory** in working notes, one line per owner page:
`[[slug]]` · kind · the fact that puts it in this region.

Done when every backlink and relevant hit is in the inventory or dropped with a
one-line reason, and every inventory page was read in full.

### 2. Name the region's character

In working notes, write the **identity sentence**:

> This is a [scale/kind] region known for [public identity], crossed by [route
> choices], and changeable by [active powers].

Then the **regional rule**: one thing that works differently here for
travellers (the current runs backwards at the new moon, compasses swing near
the drowned towers, no fire stays lit on the flats), its limit, and how a
traveller learns it before it costs them.

Done when the identity sentence names routes and powers, and the regional rule
has its limit and its tell.

### 3. Lay out the ground and the routes

- **Shape.** Boundaries, what changes across each edge, and scale in days of
  travel. Every edge names what lies beyond it, past the charts too: the DM
  knows what the sailors do not.
- **Landmarks.** Three to five a navigator steers by, each with what it tells
  a traveller.
- **Routes.** Two to four ways across or through, each with days, the check
  that keeps it (Ability (Skill) or tool, and DC), what failure costs (days,
  supplies, a hazard, an encounter), what the route passes, and what it offers
  that the others do not.
- **Travel procedure.** How a day of travel runs here, as the bullets under
  the routes table: **Navigation**, **Weather** (a d6 or d8 table with effects
  when weather varies), **Rest and supply**, one **Hidden route** per secret,
  seasonal, or broken connection with what opens it, and the **Regional
  rule**.
- **Key places.** The places the party can reach, each a linked page with one
  line on why they would go.

Done when every route has days, a check with DC, a failure cost, and a
tradeoff against the others, and every key place links a page.

### 4. Set the powers moving

- **Powers.** Two to four groups or creatures that can change the
  region now, each a linked page: hold, want now, next move with a time, and
  what reveals that move.
- **Pressure** (under Powers). One or two fronts grown from the inventory (a power's want, a
  hazard's season, a debt, a hunt), each a **Threat** bullet with what drives
  it and what becomes true if it succeeds, a time, and three portents from
  subtle to unmistakable as the First sign, Escalation, and Crisis checkboxes.
- **Stakes** (under Powers). One to three questions that play will answer.

Done when each power's next move has a time and a sign, and each front has
three portents.

### 5. Fill the road

- **Encounters.** A d6 or d8 table of who and what the party meets (creatures,
  crews, travellers, wonders that act; weather and terrain live in the weather
  table), each with its sign before contact spoken as an `_italic_` line in the
  Narration column, its source page, what it wants,
  what it does if the party does nothing, and numbers or a statblock link when
  it can be fought. Every creature or group the canon places in the region
  appears in the table or elsewhere on the page.
- **Rumors.** A d6 table, each with its truth and where it points.
  The truth is a fact about the world (the dragon is there, in this lair, or
  the dragon is a wreck's figurehead), never a note on what is confirmed or
  recorded.
- **Finds** (under Secrets). A resource, a shelter with its cost, a wonder, a
  hidden lore fact, and a shortcut: each a thing the party can take, use, or
  visit. The wonder is a sight a traveller would sail out of the way for, and
  it gives something back.
- **History.** Past facts that leave evidence a traveller can
  find.

Done when every encounter has a sign and a source, every rumor has its truth,
and every fightable encounter has numbers.

### 6. Hand the travel look to theatre-of-the-mind

Build the **narration packet** as fragments, each with its source: horizon,
terrain or water, weather, light, movement, one sound and one smell with
sources, the one feature no traveller forgets, and the tell of the regional
rule. Leave out truths, DCs, secret coordinates, and names not earned. Load
`.agents/skills/theatre-of-the-mind`, portrait mode, place recipe, and give it
the packet. For the optional `On the road` block under Travel, ask for a
situated moment (Travel recipe): the ground underfoot, the weather, what the
day's march shows, ending at camp or arrival.

Done when the returned narration passes theatre-of-the-mind's final check and
carries the regional rule's tell.

### 7. File the page

Copy `wiki/templates/region.md` to `wiki/entities/region/<kebab-name>.md` with
`type: region`, `scale`, and `kind`; add parent `region` only when it names a
page. At a Glance opens with one sentence on the region's job at the table,
then Now, Pressure, Known for, and Anchor. Step 3 fills Geography (a
`[[region]]` bullet per neighbor or subregion with what changes across the
border, a `[[place]]` bullet per landmark), Travel (routes table, travel
procedure bullets, hidden routes, regional rule), and Key Places (each with
how the party learns it exists); step 4 fills Powers (powers and fronts with
portents); step 5 fills Encounters and Rumors, with finds under Secrets and
past facts under History. Keep a section only when you have facts for it
(fact-only, `wiki/AGENTS.md` Layout). Write complete sentences. Wikilink every
owner page.

Run `wiki lint <path>`, then `wiki lint fix <path>` for deterministic repairs,
and rerun until green.

Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- The canon inventory is complete; every established detail is kept.
- The regional rule has its limit and its tell.
- Two or more routes each carry days, a check with DC, a failure cost, and a
  tradeoff; the travel procedure covers navigation, supply, weather, and rest.
- Every named place, power, and creature links a page.
- Each active power has a next move with a time and a sign; each front has
  three portents and a time.
- Every edge names what lies beyond it.
- Encounters are creatures, crews, or wonders that act, with signs, sources,
  and numbers where fightable; every canon creature or group of the region
  appears on the page.
- Every rumor's truth is a world fact; the finds under Secrets list things the
  party can take, use, or visit, and the wonder gives something back.
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
