---
name: spell-design
description: >-
  Write, edit, or create named spell pages for the campaign wiki. Use when a
  spell needs a persistent page, missing named spell, casting narration,
  classification, 2024 rules effect, discovery source, or spell history. Fill
  wiki/templates/spell.md.
---

# Spell design

A named spell is a **choice with a signature**: the caster gets a lever no
other spell gives, the target gets a way to answer it, and anyone watching
knows what they saw. A good campaign spell is peer-balanced against 2024 spells
of its level, grows from the world's own magic, and comes with a source the
party can reach and a cost for reaching it.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named spell (existing page or one to mint), the caller's
  objective and brief, `wiki/templates/spell.md`, and the vault canon it
  touches: casters, creatures or items that use it, its source, the party's
  casters.
- **Work:** The steps below, for this one spell. Keep the caller's objective.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** A named teacher, book, scroll, patron, or site the
  spell's discovery needs is cast before it is minted
  (`docs/agents/table-ready.md` § Cast before minting): an in-play or
  unrevealed page that fits comes first, and its owner skill (`npc-design`,
  `item-design`, `place-design`, `faction-design`) mints one only when none
  fits, before any text depends on it (AGENTS.md **HARD:
  entity-before-spoken**). Saves, DCs, and edge rulings → `dnd5e-mechanics`.
  The casting look → `theatre-of-the-mind` with the packet from step 7. Each
  child returns its page path or prose and its completion result; resume at the
  step that waited on it.

## Page rules

These hold in every step.

- **Canon.** User-said facts file immediately on the live path. Whatever the
  spell needs that canon leaves silent, records as unknown, or contradicts,
  decide now as a **canon proposal** (`docs/agents/table-ready.md` § Fill the
  silence): one concrete answer, stated on the page as world fact where the DM
  uses it, with the page marked `invention: true`. The response lists each
  proposal with the `[[pages]]` it grows from; a proposal that settles a
  contradiction names the sources and the reading it chose, so the DM picks the
  winner.
- **Preserve.** Improving an existing page keeps every established detail
  (name, level, school, components, users, history); fold each one into the
  section that now owns it. A statblock that already uses the effect stays
  consistent with the page, or the response names the change.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the steps and `## Done` below.
- **Own words.** Write the effect in your own words; reference official spells
  by name as peers. A scroll item page is an item, not a spell exemplar.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). The source,
  the cost, and every truth behind the casting's look are on the page by name.
- **Process stays off the page.** The inventory, identity sentence, peer
  comparison, and packet are working notes; the page carries only their facts.

## Steps

### 1. Take the canon inventory

Retrieve before inventing (constitution XII), using QMD per AGENTS.md § Vault
retrieval (`.agents/skills/qmd`).

1. Read the spell page if it exists and every page that links to it: run
   `grep -rliF "[[<name>" wiki/entities` once for the slug, the title, and each
   alias. Read every statblock or item that already produces the effect.
2. Search QMD for the spell, its effect in plain words, its tradition or
   school in this setting, its casters, and the party's spellcasters.
3. `qmd get` every hit you will use. Snippets are leads, not facts.

Write the **canon inventory** in working notes, one line per owner page:
`[[slug]]` · kind · what it says about this spell or its magic.

Done when every backlink and relevant hit is in the inventory or dropped with a
one-line reason, and every inventory page was read in full.

### 2. Find the lever

In working notes, write the **identity sentence**:

> This is a [level/school] spell that [table effect], recognized by
> [casting signature], and it gives players [choice or pressure].

Then name the **lever**: the one thing this spell lets a caster do that no
2024 peer at its level does, and the decision it puts in front of the caster
each time (where to aim it, what to spend, when to drop it). A spell that is a
peer with new paint needs a lever or a campaign tie that earns the page.

Done when the lever is one sentence and the choice it offers is named.

### 3. Tie it to the world

1. **Tradition.** Who in this setting casts it, where they learned it, and
   what that says about them (a sea-witch's hex, a navy weather-rite, a
   thieves' trick).
2. **Signature.** What the casting looks, sounds, or smells like, rooted in
   that tradition, so a witness can name the kind of caster.
3. **Price.** What using it costs beyond the slot: a material the setting
   makes scarce, a mark it leaves, a law it breaks, a rival it alerts.
4. **Swap test.** Put a generic spell name in place of this one. Every
   sentence that stays true is furniture; replace it from the inventory or the
   tradition.

Done when the tradition names a person, faction, or creature page, and the
signature and price each fail the swap test.

### 4. Set the numbers

Read [references/spell-craft.md](references/spell-craft.md). Pick two or three
2024 peers of the same role (single-target damage, area control, mobility,
utility, ward) and set the level where the effect matches them; use the damage
table there for damage spells. Then fill: Casting Time, Range (and area or
target count), Components (with the material and any cost), Duration
(Concentration when it lingers), save or attack with the ability, damage dice
and type, conditions, how it ends, and scaling with slot level or character
level.

Done when every field holds a 2024 value and the peers and their levels are in
the working notes.

### 5. Write the rulings and the counterplay

- **Rulings.** The three to five tricks players will try with it (on an
  object, on an ally, in water, around a corner, stacked with a common spell),
  each with the answer.
- **Counterplay.** How a target or rival caster answers it: the save, cover,
  distance, breaking Concentration, *counterspell* or *dispel magic*, a
  countermeasure the tradition knows.
- **In enemy hands.** Which named creature or NPC casts it against the party,
  and how they open with it.

Done when every likely trick has one answer and a DM could run the spell from
either side of the table.

### 6. Place the discovery

- **Source.** One specific source with its own page under
  `wiki/entities/npc/`, `item/`, or `place/`: a named teacher, a book or
  scroll, a patron, or a site, cast before minting. A creature page describes
  a kind of caster, so when the teacher is one of a kind (one tidehex captain,
  one sea hag), cast or mint that individual through `npc-design` and link the
  kind from their page. The source has its own reason to teach or sell, a want
  the party can meet.
- **Access.** The price of learning it (coin, favour, a task, a risk) and the
  copying or training time.
- **Clue.** How the party learns the source exists.
- **Consequence.** Who notices when a PC casts it, and what they do.

Done when the source is one named NPC, item, or place page with a reason to
deal, the clue says where and how the party meets it, and access has a
concrete price.

### 7. Hand the look to theatre-of-the-mind and file

Build the **narration packet**: what a bystander sees, hears, and feels during
the casting and the effect; the signature from step 3; leave out DCs, names
not earned, and the truth of the tradition. Load
`.agents/skills/theatre-of-the-mind`, portrait mode, technique recipe, and
give it the packet.

Copy `wiki/templates/spell.md` to `wiki/entities/spell/<kebab-name>.md` with
`type: spell`, `level`, `school`, and `ritual`. Omit empty sections. Write
complete sentences. Wikilink every owner page.

| Section | Carries |
|---|---|
| Narration | The narration, nothing else |
| Classification and casting fields | Level, school, ritual; the four casting fields |
| Effect | The runnable effect block and scaling |
| Rulings | Likely tricks with answers; counterplay; how enemies use it |
| Discovery | Source, access price, clue, and who notices a casting |
| Lore | The tradition, its casters, and history that changes a present choice |

Run `wiki lint <path>`, then `wiki lint fix <path>` for deterministic repairs,
and rerun until green.

Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- The canon inventory is complete; every established detail is kept and every
  statblock using the effect agrees with the page.
- The lever gives the caster a choice no peer at its level gives.
- The tradition, signature, and price tie the spell to named campaign pages
  and fail the swap test.
- Level and numbers match named 2024 peers; every casting field and the effect
  are concrete and runnable; scaling is stated when it scales.
- Rulings answer the likely tricks; counterplay and enemy use are on the page.
- Discovery names one specific source whose link resolves under
  `wiki/entities/npc/`, `item/`, or `place/`, with its reason to deal, a concrete access price, a clue that says where to meet it,
  and who notices a casting.
- The narration came from theatre-of-the-mind and holds no DC or unearned name.
- Every owner was cast or minted first. Each new mint names, in the response,
  the candidates considered and why none fit (`docs/agents/table-ready.md` §
  Cast before minting).
- User-said canon is filed; every invention is a canon proposal, marked on the
  page and listed in the response.
- Every page filed passes the world-voice search (`docs/agents/table-ready.md`
  § Fill the silence).
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
