---
name: climax-beats
description: >-
  Write, edit, or create content for a Climax — the session's highest-stakes
  confrontation, earned by the middle, that harvests its threads: final
  battle, final revelation, siege, trial, sacrifice, negotiation, catastrophe.
  Card catalog, harvest table, phases, fill steps, and table-ready check.
---

# Climax beats

A Climax is the big finale — the showdown where good beats evil (maybe) or
the murderer is named. It **harvests** the session: Developments armed the
party, Cliffhangers taught both sides their strengths and raised the ante,
and now the toughest thing the opposition has meets a party holding what it
needs to win — barely. The Climax is whatever confrontation the party's
choices made inevitable; a final battle is one shape among several.

## Gates

Prep only. Follow `docs/agents/work.md`. Follow AGENTS.md **HARD: entity-before-spoken** and **HARD: dm-facing-explicit**.

## Boundary contract

- **Input:** A named Climax beat, its session-plan row (card, trigger), the
  preceding carry-forward, every live thread with the beats that planted and
  tested it, and opposition, place, and item owner pages.
- **Work:** Build one Climax to the table-ready bar with the Climax craft
  below; spoken text is filled through `theatre-of-the-mind`.
- **Done:** The cold read passes and the completion test holds for every
  outcome row.
- **Capability Handoff:** Return the Climax page and its carry-forward per
  outcome to the Resolution, which shows that aftermath; a missing entry fact
  returns as a named gap.

## Copy-start

Copy `wiki/templates/climax.md`. File after accept to `wiki/journal/sessions/<campaign-slug>/<session-number>/Session-<n>-<BB>-<Label>.md` with `type: session-prep`, `kind: climax`, `category: journal`. Keep the template's jobs; keep **Final Battle** or **Final Revelation** sections only for the shape in play.

## Fill a Climax

1. **Ground.** Read the preceding carry-forward, the session plan (threads,
   opposition agenda, escalation ladder), each earlier beat's outcome rows,
   and the owner pages for the opposition, stage, and items in play (retrieve
   with `qmd`). Done when the entry state and every live thread's current
   status are stated.
2. **Choose the shape.** Read
   [references/climax-cards.md](references/climax-cards.md) and pick the shape
   the party's choices earned. When the party negotiated, exposed, or fled
   their way here, that shape is the Climax.
3. **Mint owners first.** Every creature, NPC, place, item, or rule the
   Climax needs has an owner page before any text depends on it; a creature
   you will roll without an owner goes to `monster-design`.
4. **Build the harvest.** Fill the harvest table (craft below) before
   anything else; the stage, forces, and phases grow from it.
5. **Read the bar.** Read `docs/agents/table-ready.md`, then build every
   anatomy part the Climax spends, applying the Climax craft below.
   Write every DM-facing line with `writing-for-humans`: lead with the
   point, name everything, conditionals in tables, secrets stated plainly.
6. **Set numbers and rulings.** `encounter-prep` sets difficulty for the
   villain tier and the live party; `dnd5e-mechanics` sets every check, save,
   and DC. Copy compact numbers for every combatant onto the page.
7. **Fill the spoken layer.** Load `theatre-of-the-mind` and fill `Opening
   image`, plus any phase-shift signal the players must perceive.
8. **Write the outcomes.** One row per outcome the Climax can produce —
   victory, costly victory, defeat, withdrawal, reframed or negotiated end —
   each with the changed world, the costs paid, and each thread's final
   state. That row is the Resolution's entry state.
9. **Cold read.** Run the cold read from `docs/agents/table-ready.md` and the
   completion test. Fix every gap before filing.

## Climax craft

- **Harvest table.** One row per live thread: where it was planted, where it
  was tested, the **lever** it gives the party here (a concrete mechanical
  or fictional effect — Advantage against the villain while the ward-stone
  burns, twelve allied spears holding the east stair, the password that opens
  the vault), and what happens if the party lacks it. Harvesting nothing is
  spectacle without payoff.
- **Stronger opposition, winnable fight.** The opposition is the session's
  top tier. The harvest levers are how the party can win; a party that
  gathered none of them faces a fight they should consider fleeing, and the
  page says how the opposition reacts to flight.
- **Phases.** Two or three phases, each opened by a named trigger (a
  threshold of HP, a destroyed asset, a clock tick, a revealed truth), with
  the players' signal, what changes on the stage or in the opposition's
  behavior, and the new opportunity it opens.
- **A stage that transforms.** Three features with rulings, and at least one
  that transforms the fight when it breaks, floods, burns, or falls.
- **The opposition's plan runs.** State what the opposition accomplishes each
  round or tick nobody stops it, its tactics (opening, control, punish,
  desperation), its break point, and every exit it holds — plus how the
  party can close each exit.
- **Win and lose conditions.** Name what wins besides the last hit point
  (seize the Spinner, break the ritual circle, hold until dawn) and what
  loses without a total party kill (the villain escapes with the prize, the
  town burns).
- **Every PC's moment.** Each PC has a thread, foe, or feature in the Climax
  that calls on them specifically.
- **Earned timing.** The Climax fires when the party commits, not when the
  chart reaches the slot. A central question resolved early is the Climax;
  compress and hand to the Resolution. An avoided Climax becomes new world
  state and returns to `session-beats` to recompute.
- **Budget.** About forty-five to sixty minutes. Name the compression if the
  table runs behind: fewer phases, a faster clock — the central question
  still resolves on this page.

## Completion test

The highest-stakes confrontation resolves on the page's rulings; every live
thread has a harvest row with its lever; and every outcome row states the
changed world, the costs, and each thread's final state for the Resolution.

## Named seams

- **Chart question** → load `session-beats` for position, polarity, threads,
  or transition only.
- **The shape borrows a contest** (a Duel, a Chase mid-Climax) → load
  `cliffhanger-beats` for that contest's shape only.
- **A named entity (vehicle, spell, faction, lore, quest, city, region)** →
  hand off to its wiki-kind owner.

Chart assembly, polarity rules, time budget, thread planting, escalation,
recompute, and the session plan belong to `session-beats`. Spoken player text
belongs to `theatre-of-the-mind`. Other type-card catalogs load only through a
seam above.
