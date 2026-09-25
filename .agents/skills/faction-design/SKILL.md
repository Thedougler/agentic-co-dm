---
name: faction-design
description: >-
  Write, edit, or create named faction pages for the campaign wiki. Use when a
  faction, organization, order, guild, cult, polity, crew, movement, or cell
  needs a persistent page — public face, DM thesis, active agenda, faction turn,
  assets, people, territory, or relationships. Also use when a missing named
  faction blocks a beat, scene, or session prep. Covers fronts, faction turns,
  and off-screen motion for sandbox play.
---

# Faction design

A faction is a source of **off-screen motion**: a group with a want, a way of
getting it, and a reason it must act now, so the world moves whether or not
the party is watching. The party meets a faction through its **faces** (the
few named people who deal with outsiders) and its **portents** (the signs its
plans leave on the world). A faction page is done when the DM knows what the
group does next, what the party can do about it, and what it offers or costs
them.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named faction (existing page or one to mint), the caller's
  objective and brief, `wiki/templates/faction.md`, and the vault canon it
  touches: members, base, territory, rivals, sessions.
- **Work:** The steps below, for this one faction. Keep the caller's
  objective.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** A named leader, face, base, asset, or rival the
  faction needs is cast before it is minted (`docs/agents/table-ready.md` §
  Cast before minting): an in-play or unrevealed page that fits comes first,
  and its owner skill (`npc-design`, `place-design`, `item-design`,
  `vehicle-design`, `monster-design`) mints one only when none fits, before any
  text depends on it (AGENTS.md **HARD: entity-before-spoken**, **Focused
  minting**). Off-screen resolution of turns → `world-tick`. The public face →
  `theatre-of-the-mind` with the packet from step 6. Each child returns its page
  path or prose and its completion result; resume at the step that waited on
  it.

## Page rules

These hold in every step.

- **Canon.** User-said facts file immediately on the live path. Whatever the
  faction needs that canon leaves silent, records as unknown, or contradicts,
  decide now as canon under the rule in `llm-wiki` (`docs/agents/table-ready.md` § Fill the
  silence): one concrete answer, stated on the page as world fact where the DM
  uses it, with the page marked `invention: true`. The response lists each
  proposal with the `[[pages]]` it grows from; a proposal that settles a
  contradiction names the sources and the reading it chose, so the DM picks the
  winner.
- **Preserve.** Improving an existing page keeps every established detail
  (members, customs, contracts, history, session appearances); fold each one
  into the section that now owns it.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the steps and `## Done` below.
- **Scale to importance.** A faction the party will deal with this arc gets
  the full page; the template's sections that change no current play are
  omitted, never left empty.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). Every portent
  and secret has its truth on the page: who, what, why, and what is at stake,
  by name. `[!narration]` is the only callout.
- **Process stays off the page.** The inventory, identity sentence, and packet
  are working notes; the page carries only their facts.

## Steps

Read [references/faction-craft.md](references/faction-craft.md) before step 2.

### 1. Take the canon inventory

Retrieve before inventing (constitution XII), using QMD per AGENTS.md § Vault
retrieval (`.agents/skills/qmd`).

1. Read the faction page if it exists and every page that links to it: run
   `grep -rliF "[[<name>" wiki/entities` once for the slug, the title, and each
   alias. Read every member's page.
2. Search QMD for the faction, its members, base, territory, rivals, patrons,
   and every session where it appeared or was named.
3. `qmd get` every hit you will use. Snippets are leads, not facts.

Write the **canon inventory** in working notes, one line per owner page:
`[[slug]]` · kind · the fact that ties it to this faction.

Done when every backlink and relevant hit is in the inventory or dropped with a
one-line reason, and every inventory page was read in full.

### 2. Set the engine

In working notes, write the **identity sentence**:

> This is a [kind/scope] faction that [wants concrete change], acts through
> [signature method], and gives players [choice or pressure].

Then fill the engine: **Want** (a concrete change in the world, present
tense), **Method**, **Pressure** (why now: a deadline, rival, scarcity,
exposure, or fracture), and **Collision** (a named faction, person, or place
whose want crosses this one). Take each from the inventory whenever it offers
one: a debt, a contract, a rival, a loss already on a canon page.

Done when the want names what changes and for whom, and the collision names
the other side by page.

### 3. Put faces on it

- **Leader:** who decides, with an NPC page.
- **Faces:** the two or three members the party will actually talk to, trade
  with, or fight, each with an NPC page, a role, and what they personally want
  that the faction does not.
- **Fracture:** one internal split the party could widen or heal.
- **Custom:** one habit, oath, mark, or practice that makes a member
  recognizable and that a clever party can use.

Done when every face links an NPC page and the custom fails the swap test (put
a rival faction's name in: if the custom still fits, sharpen it).

### 4. Write the agenda and its clock

Fill the Active Agenda: goal, why, planned action, needs, opposition, next
signal, player opening, and if completed. Turn it into three to five
**milestones**, each a concrete event with a time (a date, a number of days, or
a trigger), a portent the party could notice, and what changes in the world
when it lands. The first milestone lands soon enough that the party's next
session can see it.

Done when each milestone has a time, a portent, and a changed fact, and "if
completed" changes something the campaign will feel.

### 5. Hand the party levers

- **Offer.** One job, deal, or favour the faction would put to this party now,
  with who offers it, the pay, and the catch.
- **Running the Faction.** When encountered, helped, opposed, ignored, and
  broken: what the world does in each case, by name.
- **Hidden truth.** One thing the faction hides that changes the deal once
  the party learns it: a hidden employer, a debt, a betrayal in motion, a
  weakness, a crime. Three clues the party can find in the world, each a
  different kind (a person who talks, a thing they can see or take, a place
  they can visit), with the check where one is uncertain.
- **Numbers.** When the party could fight them, the rank-and-file as a count
  and a statblock, and the faces' statblock links or compact numbers.

Done when the offer has a named offerer, pay, and catch, and every Running the
Faction row says what happens.

### 6. Hand the public face to theatre-of-the-mind

Build the **narration packet** as fragments, each with its source: how members
look and move in public, the custom from step 3, one sign a bystander could
spot that they have been somewhere, and the name people use for them. Leave
out goals, leaders' plans, the hidden truth, and names not earned. Load
`.agents/skills/theatre-of-the-mind`, portrait mode, faction recipe, and give
it the packet.

Done when the returned narration passes theatre-of-the-mind's final check.

### 7. File the page

Copy `wiki/templates/faction.md` to `wiki/entities/faction/<kebab-name>.md`
with `type: faction`; `wiki/templates/contracts/faction.yml` owns which
sections are required. Fill the DM thesis as one sentence of campaign pressure.
Set Current Turn from step 4's next milestone; leave the Turn Log for
`world-tick`. Omit sections that change no current play. Write complete
sentences. Wikilink every owner page.

Run `wiki lint <path>`, then `wiki lint fix <path>` for deterministic repairs,
and rerun until green.

Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- The canon inventory is complete; every established detail is kept.
- The want, method, pressure, and collision are concrete and named; the DM
  thesis is one sentence of pressure.
- The leader and every face link NPC pages; the fracture and custom are
  usable in play.
- The agenda has milestones with times, portents, and changed facts; the first
  lands by the party's next session.
- The offer names who, pay, and catch; Running the Faction answers encountered,
  helped, opposed, ignored, and broken; the hidden truth changes the deal and
  has three in-world clues of different kinds.
- Every fighter the party could face has compact numbers or a statblock link.
- The public face came from theatre-of-the-mind and holds no secret or
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
