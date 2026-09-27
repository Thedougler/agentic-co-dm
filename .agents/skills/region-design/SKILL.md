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

- **Factions.** Two to four groups or creatures that can change the region
  now, each a linked page: hold, want now, next move with a time, and what
  reveals that move.
- **Threats.** One or two threats grown from the inventory (a faction's want,
  a hazard's season, a debt, a hunt), each with what drives it and what
  becomes true if it succeeds, a time, and three visible signs from subtle to
  unmistakable as First sign, Escalation, and Crisis checkboxes.

Both go under Factions and Threats.

Done when each faction's next move has a time and a sign, and each threat has
three visible signs.

### 5. Fill the road

- **Random Encounters.** A d6 or d8 table of who and what the party meets (creatures,
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
- **Finds** (as **Secret.** paragraphs). A resource, a shelter with its cost,
  a wonder, a hidden lore fact, and a shortcut: each a thing the party can
  take, use, or visit, and a past fact only when it leaves evidence a
  traveller can find. The wonder is a sight a traveller would sail out of the
  way for, and it gives something back.

Done when every encounter has a sign and a source, every rumor has its truth,
and every fightable encounter links a creature page with a statblock.

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
page. The italic identity line under the portrait gives the kind of land, its
parent region, and what is changing in it now. Step 3 fills Travel (the routes
table, including each neighbor and what changes across the border, then the
travel rules that change a choice: navigation, weather, rest and supply,
hidden routes, the regional rule) and Places (landmarks and sites, each with
how the party learns it exists); step 4 fills Factions and Threats (each
with its visible steps); step 5 fills Random Encounters and Rumors, then **Secret.**
paragraphs for finds. Keep a section only when you have facts for it
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
- Each active faction has a next move with a time and a sign; each threat has
  three visible signs and a time.
- Every edge names what lies beyond it.
- Encounters are creatures, crews, or wonders that act, with signs, sources,
  and numbers where fightable; every canon creature or group of the region
  appears on the page.
- Every rumor's truth is a world fact; the **Secret.** finds list things the
  party can take, use, or visit, and the wonder gives something back.
- When the party will travel the region, `[!narration] On the road` under
  Travel renders a stretch of the journey.
- The narration came from theatre-of-the-mind and holds no truth, DC, or
  unearned name.
- Every owner was cast or minted first. Each new mint names, in the response,
  the candidates considered and why none fit (`docs/agents/table-ready.md` §
  Cast before minting).
- User-said canon is filed; every invention is canon under the rule in `llm-wiki`, marked on the
  page and listed in the response.
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
