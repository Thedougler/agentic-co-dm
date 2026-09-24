---
name: resolution-beats
description: >-
  Write, edit, or create content for a Resolution — the short afterscene after
  the Climax that shows the changed world, pays off rewards and costs, gives
  each PC a closing moment, and leaves the players able to name what is
  different and what they want next. Card catalog (Pondsmith's Resolutions),
  fill steps, and table-ready check.
---

# Resolution beats

A Resolution is the **tag line**: a tiny afterscene where the session's ends
are tied off, or the sequel shows its face. It is the result of every beat
before it — threads planted in the Hook and middle at their final state,
costs visible, rewards in hand — and it is proportional to the Climax. It can
overturn the Climax's apparent result when the overturn grows from
established fiction.

## Gates

Prep only. Follow `docs/agents/work.md`. Follow AGENTS.md **HARD: entity-before-spoken** and **HARD: dm-facing-explicit**.
Cast and invent per `docs/agents/table-ready.md` § Cast before minting and § Fill the silence.

## Boundary contract

- **Input:** A named Resolution beat, the Climax's outcome rows and
  carry-forward, the session's threads and costs, and linked owner pages.
- **Work:** Build one Resolution to the table-ready bar with the Resolution
  craft below; spoken text is filled through `theatre-of-the-mind`.
- **Done:** The cold read passes and the completion test holds for every
  Climax outcome the Resolution answers.
- **Capability Handoff:** Return the Resolution page and the aftermath state.
  `session-beats` owns the next session's chart; a named entity goes to its
  wiki-kind owner; a missing entry fact returns as a named gap.

## Copy-start

Copy `wiki/templates/resolution.md`. File after accept to `wiki/journal/sessions/<campaign-slug>/<session-number>/Session-<n>-<BB>-<Label>.md`; when the request names no session, list `wiki/journal/sessions/<campaign-slug>/` and use the next session that has no plan page yet, and say so. Keep the template's jobs; omit a section only when this Resolution never spends it.

## Fill a Resolution

1. **Ground.** Read the Climax's outcome rows and carry-forward, the session
   plan's threads and PC touchpoints, each beat's costs, and the owner pages
   for the people, places, and items in the afterscene (retrieve with `qmd`).
   Done when each thread's final state and each cost paid are listed.
2. **Choose the card per outcome.** Read
   [references/resolution-cards.md](references/resolution-cards.md). For each
   Climax outcome the Resolution answers, pick the card that outcome produced.
3. **Cast owners.** Every named person, place, item, or faction in the
   afterscene has an owner page before any text depends on it: cast from the
   wiki first, and mint only what nothing fits (`docs/agents/table-ready.md` § Cast before minting).
4. **Read the bar.** Read `docs/agents/table-ready.md`, then build every
   anatomy part the afterscene spends, applying the Resolution craft below.
   Write every DM-facing line with `writing-for-humans`: lead with the
   point, name everything, conditionals in tables, secrets stated plainly.
5. **Set rewards and rulings.** Name every reward and its owner; load
   `dnd5e-mechanics` for any check, and `item-design` for a new
   magic item.
6. **Fill the spoken layer.** Load `theatre-of-the-mind` and fill the
   `Closing image` for each outcome branch.
7. **Record the aftermath.** Fill What Is True Now, Loose Ends, and Rewards &
   Accounting so the next session's planner reads the changed world from
   this page.
8. **Cold read.** Run the cold read from `docs/agents/table-ready.md` and the
   completion test. Fix every gap before filing.

## Resolution craft

- **Short and proportional.** About ten to twenty-five minutes of table time. A
  personal-stakes Climax gets a personal afterscene; a faction-scale Climax
  gets a power-vacuum afterscene. New fights, new villains, and new
  worldbuilding belong to the next session.
- **Branch by outcome.** When the Climax could end several ways, the page
  carries a branch per outcome — held or lost, captured or escaped — each
  with its own closing image, costs, and rewards.
- **Costs stay paid.** Lost allies stay lost; spent supplies stay spent;
  injuries and broken trust show in the scene. Convenient survivals and
  arriving merchants erase what the Climax proved.
- **Rewards are named.** Coin with amounts, items with owner links, XP or the
  milestone, favors and titles with who grants them, faction standing with
  its effect.
- **Echo the arc.** The Hook's question gets its answer; each thread gets
  Close, Carry, or Transform; each PC's touchpoint gets a closing moment,
  framed as a prompt the player answers.
- **Grounded overturns.** A reversal of the Climax's result — the villain's
  escape craft, the rescued ally changed by captivity — uses means planted
  earlier and names that beat. A threat with no roots belongs in the next
  session's Hook.
- **One door forward.** End on one clear next vector, or plain closure. An
  Ending Cliffhanger or Greater Threat card is that one door, chosen because
  the Climax's outcome exposed it.

## Completion test

Players can name what is different and what they want next; every Climax
outcome the page answers shows its costs, rewards, and thread states; and the
aftermath records are complete enough for the next session's plan. On the
page:

- each outcome's rewards are named with values: the loot the defeated side
  carried (owner links), coin amounts, favors and access with who grants
  them, and a milestone or XP proposal. These are canon under the rule in `llm-wiki` where canon
  is silent; "none" stands only when the fiction offers nothing;
- each actor's closing response is written, with what it changes;
- What Is True Now states values, not instructions to record them later.

## Named seams

- **Chart question** → load `session-beats` for position, polarity, threads,
  or transition only.
- **The closing names a next beat type** → load that type skill for the
  handoff only.
- **A named entity (vehicle, spell, faction, lore, quest, city, region)** →
  hand off to its wiki-kind owner.

Chart assembly, polarity rules, time budget, thread planting, escalation,
recompute, and the session plan belong to `session-beats`. Spoken player text
belongs to `theatre-of-the-mind`. Other type-card catalogs load only through a
seam above.
