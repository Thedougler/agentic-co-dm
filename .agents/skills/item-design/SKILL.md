---
name: item-design
description: >-
  Design, revise, audit, and file items for D&D 5.5e (2024 rules): magic
  weapons, armor, wondrous items, rings, rods, staffs, wands, potions,
  scrolls, consumables, artifacts, plot objects, and notable mundane gear,
  including cursed, sentient, and evolving items. Use when creating or
  improving a `type: item` page or any part of one (mechanics, rarity, look,
  history, curse, personality), or when a place or beat needs an item minted.
  Flora hazards use the hazard template.
---

# Item design

An item is **a decision the bearer carries**. Its rules text is the
deliverable: a DM can run it tonight from the page alone, in correct 2024
language, at a power its rarity pays for. Around that, it is **a real object**
with a maker, a history written on its surface, and people who want it; and it
has a **presence**, the way it shows itself in a room, in a hand, and when it
is hidden. Every property the item hides (a curse, a will, a second power)
leaves a **tell** on the object that a sharp player can notice; the DM page
states the truth behind it.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named item (existing page or one to mint), the caller's
  objective and brief (intended bearer, tier, where it is found), the party's
  PC pages, `wiki/templates/item.md`, and the vault canon the item touches.
- **Work:** The steps below, for this one item.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** Every check, save, and DC gets the mandatory
  `dnd5e-mechanics` pass. A sentient item's personality comes from
  `npc-design` (step 5). The portrait goes to `theatre-of-the-mind` with the
  packet from step 7. A creature the item summons, commands, or becomes goes
  to `monster-design`; a spell it grants that does not exist yet to
  `spell-design`; the place it is hidden in to `place-design`. A named owner the item needs is cast before it is minted
  (`docs/agents/table-ready.md` § Cast before minting): an in-play or
  unrevealed page that fits the role comes first, and its owner skill mints
  one only when none fits, before any text depends on it (AGENTS.md **HARD:
  entity-before-spoken**). Each child returns its page path or result; resume
  at the step that waited on it.

## Page rules

- **Canon.** User-said facts file immediately on the live path. Whatever the
  page needs that canon leaves silent, records as unknown, or contradicts,
  decide now as canon under the rule in `llm-wiki` (`docs/agents/table-ready.md` § Fill the
  silence): one concrete answer, stated on the page as world fact where the DM
  uses it, with the page marked `invention: true`. The response lists each
  proposal with the `[[pages]]` it grows from; a proposal that settles a
  contradiction names the sources and the reading it chose, so the DM picks the
  winner.
- **Preserve.** Improving an existing page keeps every established fact; a
  changed number replaces the old one and the proposal names the change. A
  recorded unknown (no appraiser can name its maker) is a fact about what
  people in the world know: keep it true for them, and write the DM answer
  behind it.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the steps and `## Done` below.
- **One callout.** `[!narration]` is the only callout. The item text is plain
  paragraphs with bold labels; curses and truths are plain sentences under
  Hidden Properties.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). Every tell
  has its truth on the page, and every hidden property states exactly what it
  does.
- **Original expression.** Borrow patterns from published items, never their
  names or text. Paraphrase every rule.
- **Process stays off the page.** The inventory, comparator matrix, power
  envelope, and packet are working notes. Each fact appears once on the page.

## Steps

[references/example.md](references/example.md) takes one item through every
step; read it before step 3.

### 1. Read the canon and the bearer

Retrieve before inventing (constitution XII), using QMD per AGENTS.md § Vault
retrieval.

1. Read the item page if it exists and every page that links to it:
   `grep -rliF "[[<name>" wiki/entities` for the slug, title, and each alias.
2. Read where it is found, who made it, who owns or wants it, and the lore it
   carries. `qmd get` every hit you will use.
3. Read the intended bearer's PC page (class, level, attuned items, signature
   tricks) and the rest of the party's gear, so the item fits a niche instead
   of taking one.

Write the **canon inventory** in working notes: `[[slug]]` · kind · the fact
that ties it to this item. Add the bearer line: class, level, attunement slots
used, and the niche the item should serve.

Done when every backlink and relevant hit is in the inventory or dropped with a
reason, and the bearer line is written (or "no set bearer").

### 2. Choose the kind and the path

- **Kind:** `consumable` (one use, then gone), `magic` (permanent magic item),
  `plot` (matters to the story, little or no mechanic), or `durable` (notable
  mundane gear). Artifacts are `magic` with artifact rules.
- **Branches:** cursed, sentient, evolving. Each adds step 5.
- **Disguised creature:** a creature that passes for an item (a mimic in
  object form) gets an item page for what it appears to be: the portrait, and
  the item text an *Identify* spell would report. Hidden Properties states the
  truth and links the creature page, which owns the statblock and the will.
  The item is sentient only when the object itself thinks; a mimic's will
  belongs to the creature.
- **Search before inventing.** Search the web for existing items that already
  do what the brief needs: the 2024 SRD and Free Rules first, then official
  books, then reputable published and homebrew sources (Kobold Press, DMs
  Guild, established creators). Search by effect and by fantasy ("compass
  that finds wrecks", "cursed ring that cannot be removed"). List three to
  five candidates in working notes with a working link, their rarity, and
  what each does.
- **Path:** co-opt the closest candidate first. Reskin it when only the
  fiction changes; narrow change for one altered property; equal exchange to
  trade one power for another; combine two items and reassess rarity; bespoke
  only when no candidate reaches the design. Write one line naming the
  candidate you co-opted, or why none fit. A co-opted item keeps its tested
  numbers; its text is paraphrased in your own words with the source linked
  in working notes.

Done when the candidate list is written and the path names a co-opted item or
the reason for bespoke.

### 3. Make it this item and no other

Read [references/concept.md](references/concept.md) for diversity axes and
weak-to-strong examples.

1. **Stock version.** One line: "+1 longsword", "potion of healing", "cloak
   of invisibility". Everything it predicts is the default.
2. **Twist.** Tie its making, material, or history to campaign canon so the
   stock version breaks: a blade forged from a wreck's anchor chain that pulls
   toward drowned iron; a healing draught brewed from a creature that only
   lives on one island.
3. **Form follows function.** Each property shows on the object: the charm
   that grants water breathing has gills cut into its rim; the charged wand
   has notches that fill with light as charges return.
4. **History on the surface.** Maker's mark, repairs, inscriptions, a previous
   owner's name scratched out, wear where hands held it.
5. **Pitch.** "This is a [item] for a [bearer] that lets them [experience] by
   paying [cost]."
6. **Swap test.** Put a published item's name in place of this one. Replace
   every line that stays true.

Done when the twist, the visible function, and the pitch all fail the swap
test.

### 4. Write the mechanics

Read [references/rules-2024.md](references/rules-2024.md) for rarity, prices,
attunement, activation, charges, spells from items, and 2024 wording.

1. **Comparators.** Fill the matrix in
   [references/research-and-comparators.md](references/research-and-comparators.md):
   a rules anchor, a chassis peer, an effect peer, and a boundary peer.
2. **Power envelope.** For offense, defense, action economy, spell access,
   exploration, and social use, write what it gives and what pays for it.
   Rarity is a ceiling: one axis near it, the rest well below.
3. **Item text.** Classification line, then the runnable text: trigger, action
   (Magic action, Bonus Action, Reaction, or none), frequency, range, targets,
   save or attack, effect, duration, concentration, charges and recovery, and
   edge cases.
4. **Engagement.** Tell → Choice → Cost → Payoff → Counterplay: when the
   bearer decides to use it, and what that decision costs.
5. **Audit.** Run [references/mechanical-audit.md](references/mechanical-audit.md)
   with the bearer line from step 1, then send every check and save through
   `dnd5e-mechanics`.

Done when the audit verdict is "safe as written" and the item text contains
every field its properties need.

### 5. Curse, sentience, evolution, artifact

Run only the branches that apply. Read
[references/cursed-sentient-evolving.md](references/cursed-sentient-evolving.md).

- **Cursed:** the curse's tell, trigger, effect, how it deepens, and the exit,
  including whether attunement can be ended while cursed.
- **Sentient:** load `npc-design` at scene scale and hand it the item's
  concept, maker, and history. It returns want, fear, limit, voice, three
  sample lines, posture changes, and tells. Add the sentient-item block
  (mental scores, alignment, communication, senses, special purpose, conflict)
  to the item text.
- **Evolving:** each stage's trigger, new property, cost, and tell; re-audit
  rarity at every stage.
- **Artifact:** its minor and major properties, its destruction condition, and
  who hunts it.

Done when every branch has its tell, its truth, and a way out or through for
the bearer.

### 6. Give it presence

How the item shows up in the world, for place pages, beats, and the DM:

- **Seen:** what anyone can see from across a room.
- **Held:** weight, temperature, balance, texture, sound in the hand.
- **Active:** what it looks, sounds, or smells like when used.
- **Unseen:** the tell it gives off when hidden or wrapped (a glow through
  cloth, a cold spot, dogs that will not settle, a compass needle that
  drifts); name "none" when it gives none.
- **Concealment:** how it can be hidden, and what finds it (a check with its
  DC, a spell, a person who knows).
- **Wanted by:** who looks for it, by owner link (cast from the vault first),
  why, the sign they are looking, and what they do when they learn the party
  carries it. A magic, plot, or artifact item has at least one seeker.

Done when every field is filled or marked none, Wanted by names a seeker for
any magic, plot, or artifact item, and a place or beat could place the item
from these fields alone.

### 7. Hand the look to theatre-of-the-mind

Build the **packet** as fragments, each with its source: the plain noun, size
against a hand or body, material and colour, wear and repairs, its parts, one
sense (weight, temperature, sound, smell), visible marks and inscriptions, and
every tell from steps 3 and 5 as plain appearance. Leave out: effects, rarity,
attunement, charges, the curse, the item's personality, and any name not
written on the object.

Load `.agents/skills/theatre-of-the-mind`, portrait mode, item recipe, and give
it the packet.

Done when the portrait passes theatre-of-the-mind's final check and carries
every tell.

### 8. File the page

Copy `wiki/templates/item.md`. Consumables stop after the item text. Omit
empty sections, write complete sentences, and wikilink every owner page.

| Section | Carries |
|---|---|
| Narration | The portrait from step 7 |
| Classification | Kind, rarity, and attunement, on one line |
| Item text | The runnable rules from steps 4 and 5, plain paragraphs with bold labels |
| At the Table | Presence from step 6; for a sentient item, its voice, sample lines, and what it wants from the bearer; the engagement loop when the item text leaves it unclear |
| Hidden Properties | Curse, hidden power, true history, and the truth behind every tell |
| Connections | Each tie by wikilink and what it does at the table |
| Provenance | Maker, owners, and how it came to be where it is |

Run `wiki lint <path>`, then `wiki lint fix <path>`, and rerun until green.

Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- The canon inventory and bearer line are complete.
- Existing items were searched on the web before inventing; the page co-opts
  the closest one, or the working notes say why none fit.
- The twist, visible function, and pitch fail the swap test.
- The item text is runnable in 2024 language: action, frequency, range,
  targets, save or attack, duration, concentration, charges, and edge cases.
- The comparator matrix and audit support its rarity; every check and save
  passed `dnd5e-mechanics`.
- Curse, sentience, evolution, and artifact branches have tells, truths, and
  exits; a sentient item's personality came from `npc-design`.
- Presence is filled, so a place or beat can place it seen or hidden; a
  magic, plot, or artifact item has a named seeker who acts when it surfaces.
- Every recorded unknown and every tell has its DM answer under Hidden
  Properties.
- The portrait came from theatre-of-the-mind and carries every tell.
- `[!narration]` is the only callout; each fact appears once.
- User-said canon is filed; every invention is canon under the rule in `llm-wiki`, marked on the
  page and listed in the response.
- Each new mint names, in the response, the candidates considered and why none
  fit (`docs/agents/table-ready.md` § Cast before minting).
- Every page filed passes the world-voice search (`docs/agents/table-ready.md` §
  Fill the silence).
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
