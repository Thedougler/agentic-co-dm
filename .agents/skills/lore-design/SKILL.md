---
name: lore-design
description: >-
  Write, edit, or create named lore pages for the campaign wiki. Use when a
  lore note, world truth, history, belief, rumor, legend, doctrine, custom, law,
  cosmology, prophecy, revelation, missing named lore note, Current Truth,
  discovery path, or table-facing lore handle needs a persistent page. Fill
  wiki/templates/lore.md.
---

# Lore design

A lore page answers **one durable question** about the world and turns the
answer into play. The DM gets the truth, stated plainly; the players get
**accounts** (what people in the world say, each wrong in a useful way),
**signs** they can notice, and **clues** that lead them to the truth if they
chase it. Lore earns its page when knowing it changes a choice: where to sail,
whom to trust, what to fear, what a thing is worth.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named lore question (existing page or one to mint), the
  caller's objective and brief, `wiki/templates/lore.md`, and the vault canon
  it touches: sessions, places, factions, NPCs, creatures, items, prior lore.
- **Work:** The steps below, for this one question. Keep the caller's
  objective.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** A named person, creature, place, item, or faction the
  truth or its clues need is cast before it is minted
  (`docs/agents/table-ready.md` § Cast before minting): an in-play or
  unrevealed page that fits comes first, and its owner skill mints one only
  when none fits, before any text depends on it (AGENTS.md **HARD:
  entity-before-spoken**, **Focused minting**). A site the party will enter is a
  place page (`place-design`); a creature they will fight is a creature page
  (`monster-design`). Checks → `dnd5e-mechanics`. A spoken telling →
  `theatre-of-the-mind`. Each child returns its page path or prose and its
  completion result; resume at the step that waited on it.

## Page rules

These hold in every step.

- **Canon.** User-said facts file immediately on the live path. Whatever the
  question needs that canon leaves silent, records as unknown, or contradicts,
  decide now as canon under the rule in `llm-wiki` (`docs/agents/table-ready.md` § Fill the
  silence): one concrete answer, stated on the page as world fact where the DM
  uses it, with the page marked `invention: true`. The response lists each
  proposal with the `[[pages]]` it grows from; a proposal that settles a
  contradiction names the sources and the reading it chose, so the DM picks the
  winner. What the world does not know stays unknown to the world, in Accounts
  and Who Knows; Current Truth carries the answer.
- **Table history is the table's.** What the party did, learned, or believes
  comes from session notes; the page records it and leaves their next
  conclusion to play.
- **Preserve.** Improving an existing page keeps every established detail
  (claims, tellings, witnesses, sources); fold each into the section that now
  owns it. A detail the new truth shows to be false becomes an account.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the steps and `## Done` below.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). Every sign,
  account, and clue has its truth on the page by name. `reveal` stays
  `unrevealed` until play reveals the lore.
- **Process stays off the page.** The inventory and question are working
  notes; the page carries only their facts.

## Steps

### 1. Take the canon inventory

Retrieve before inventing (constitution XII), using QMD per AGENTS.md § Vault
retrieval (`.agents/skills/qmd`).

1. Read the lore page if it exists and every page that links to it: run
   `grep -rliF "[[<name>" wiki/entities` once for the slug, the title, and each
   alias. Read every page it links to.
2. Search QMD for the question's subject, its places, creatures, people, and
   every session where it came up.
3. `qmd get` every hit you will use. Snippets are leads, not facts.

Write the **canon inventory** in working notes, one line per owner page:
`[[slug]]` · kind · what it claims or shows about this question.

Done when every backlink and relevant hit is in the inventory or dropped with a
one-line reason, and every inventory page was read in full.

### 2. Answer the question

Write the **question** in working notes: what this lore lets the DM answer or
the players act on. Several unrelated truths become linked pages.

Then write the **truth**: the answer, one concrete fact at a time. For a legend,
say which parts are real, which are distorted, and what is really behind each
distortion; where it is (a linked place or region, with a bearing and
distance); who or what is there now; and what happened to the people who went
before. Build the truth from the inventory: a creature, faction, event, or
place already on a canon page makes a better answer than a new one.

Make the truth **at least as good as the tale**, and **keep the wonder**. A
fantastic claim (a curse, the walking dead, a monster of impossible size)
either stays true in some form or gives way to a different wonder of equal
size: the drowned do not walk, but something wears their faces; the beast is
ordinary, but what it guards is not. A mundane explanation earns its place
only when it opens a bigger opportunity than the tale did (a smuggler's lie
that hides a cache). A legend explained away into weather and bones is a dead
lead. The truth also fits the canon's scale: distances, dangers,
and rewards match what the tellings imply (divers who avoid a hole dive near
it) and the party's level (treasure by the 2024 guidance for their tier).

Done when every claim in the canon's tellings is marked true, distorted (and
what is really there), or false (and why people believe it), and every
unknown or open item the old page listed has its answer.

### 3. Make it bite now

- **Why now.** What makes this truth matter to the current campaign: a person
  who acts on it this month, a deadline, a prize someone else is racing for.
- **Actors.** Who else knows or wants the truth or its prize: a named person
  or group with an NPC or faction page (a creature doing what it always does
  is scenery), what they do next, and when.
- **Stakes.** What the party gains by acting on it (the prize, the route, the
  ally) and what it costs or risks, in numbers where numbers apply (gold,
  days, the creature's CR, the DC of the dive).

Done when at least one named NPC or faction moves on this truth on their own
clock, and the stakes name what the party can win and lose, sized for their
level.

### 4. Build the accounts and the clue path

- **Accounts.** Two to four in-world versions (a sailors' telling, a scholar's
  note, a faction's official line, a survivor's story), each with who holds it
  and how it relates to the truth. Each is wrong or partial in a way that
  sends a believer somewhere interesting.
- **Common telling.** The version a tavern would actually say, in voice.
- **Revelation.** For each conclusion the party needs, three independent
  clues from different sources (a person, a place, a document, a physical
  sign), each naming its source page, what it reveals, and the check if one
  is uncertain (Ability (Skill) and DC).
- **Signs.** What the players notice in the world before anyone explains it.

Done when each account names its holder, each needed conclusion has three
clues from different sources, and each source is a linked page.

### 5. File the page

Copy `wiki/templates/lore.md` to `wiki/entities/lore/<kebab-name>.md` with
`type: lore`, `kind`, `truth`, `scope`, `region`, and `era`. Omit sections with
no job. Write complete sentences. Wikilink every owner page.

| Section | Carries |
|---|---|
| At a Glance | Core truth, why it matters now, scope |
| Current Truth | The truth from step 2; Limits carry exceptions and costs |
| At the Table | Players notice, this explains, this enables, this warns of, relevant now |
| Who Knows | Each knower, what they know, certainty, basis; Party Knowledge from session notes |
| Accounts | The accounts and the common telling |
| Discovery | Each revelation with its three clues |
| If This Is Changing | The actors from step 3, what they do next, and when |
| Consequences | Because true, if exposed, if exploited |

Leave out Canon Log until play witnesses the lore.

Run `wiki lint <path>`, then `wiki lint fix <path>` for deterministic repairs,
and rerun until green.

Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- The canon inventory is complete; every established claim is kept, as truth
  or as an account.
- The page answers one question; Current Truth answers every claim and every
  formerly open item with one concrete fact.
- The truth is at least as good as the tale and keeps the wonder: each
  fantastic claim stays true in some form or gives way to a wonder of equal
  size, at the canon's scale.
- A named NPC or faction moves on the truth on their own clock; the stakes name
  what the party can win and lose, with numbers sized for their level.
- Accounts name their holders; each needed conclusion has three clues from
  different linked sources; uncertain clues carry Ability (Skill) and DC.
- At the Table fills notice, explains, enables, and warns.
- Party knowledge comes from session notes; `reveal` stays
  `unrevealed`.
- Every owner was cast or minted first. Each new mint names, in the response,
  the candidates considered and why none fit (`docs/agents/table-ready.md` §
  Cast before minting).
- User-said canon is filed; every invention is canon under the rule in `llm-wiki`, marked on the
  page and listed in the response.
- Every page filed passes the world-voice search (`docs/agents/table-ready.md`
  § Fill the silence).
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
