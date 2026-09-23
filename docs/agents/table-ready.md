# Table-ready beats

The content bar for every session beat — Hook, Development, Cliffhanger,
Climax, Resolution — and for the session plan and run-guide cockpit that carry
them. The type skills own *which* beat to build; this file owns *how complete*
the built beat must be.

A beat is **table-ready** when the DM can run it cold — mid-session, reading
only this page and the operative lines it copies from linked owners — without
inventing a name, number, motive, consequence, or picture. Every moment where
the players could act has an answer on the page: what the world does, what the
roll is, what changes.

Observed failure this bar exists for: Session 12's Climax said "apply Aruhe
convergence" without ever saying what convergence does, sent Skarn's AC and HP
to his owner page, and spent its pressure table on advice to the DM ("do not
make him immune") instead of what Skarn does. The structure was right; the DM
still had to invent the fight.

## Who owns what

Session content is built by several skills; each owns one layer, and each
reads the layers it depends on from the owner.

| Layer | Owner |
|---|---|
| Which beats, in what order, tracking which threads | `session-beats` |
| What one beat contains | its type skill (`hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats`) and this file |
| Named people, places, creatures, items | their owner skills (AGENTS.md routing), minted before text depends on them |
| Checks, saves, DCs | `dnd5e-mechanics`; encounter difficulty `encounter-prep` |
| How DM-facing text reads | `writing-for-humans` |
| How spoken player text reads (`[!narration]`, narration cells) | `theatre-of-the-mind` |
| Markdown, links, check notation, callouts | `obsidian-markdown` |
| The one-page table cockpit built from finished beats | `run-guide` |

## Beat anatomy

Every beat carries these parts. A type skill says which parts it trims; a part
this beat never spends at the table stays off the page.

1. **Entry state.** The previous beat's carry-forward, restated as facts:
   positions, conditions, HP or resources that matter, who holds what, what the
   party knows, which clocks sit where. The first beat of a session reads the
   last session's ending.
2. **Cast.** Every named actor links its owner page and states, for this beat:
   what it wants now; what it does next if nobody interferes; what it offers,
   withholds, or lies about; what shifts its posture. Opposition that may fight
   carries compact numbers copied from its owner statblock — AC, HP, Speed, the
   one or two attacks or save DCs the DM will actually roll, the trait that
   changes tactics — plus a tactics line: opening move → how it adapts when
   countered → break point → exit or surrender.
3. **Space.** Where the beat happens, with distances in feet where position
   matters; two or three interactive features, each with its obvious use and
   the ruling it produces (half cover, difficult terrain, a DC to climb, damage
   when it falls); one way the space changes during the beat.
4. **Pressure.** Why now. A fuse with three or four named ticks, each with its
   trigger and what newly becomes visible, threatened, blocked, or lost. What
   happens if the party does nothing.
5. **Handles.** At least two materially different approaches — fight, talk,
   sneak, trade, trick, flee, protect, sacrifice — each with its concrete
   upside and its cost. Handles are verbs the players can pick up from what
   they can see.
6. **Rulings.** Each uncertain action worth rolling has Ability (Skill), DC,
   success, and failure, with partial when the fiction has a middle
   (`dnd5e-mechanics` sets these). Sensible actions with no real doubt succeed
   automatically and say what they yield. Failure moves play: it costs time,
   position, resources, or exposure, and the beat still ends.
7. **Discoveries.** The actual truths, stated as facts, each with at least one
   way it surfaces. A conclusion the session cannot progress without gets three
   independent routes. Clues that nobody could use are cut.
8. **Payoff.** What the beat can earn and what it can cost, named: the item
   (owner link), coin amount, ally, leverage, route, favor, or information; the
   injury, spent resource, broken trust, or advanced clock.
9. **Outcomes and carry-forward.** A row for each outcome the beat can
   plausibly produce, each with the changed state and the next beat it hands
   to, plus one row for "anything else": which facts on this page stay true
   whatever the party does. The carry-forward lists the state variables the
   next beat inherits.
10. **Spoken layer.** `[!narration]` blocks filled through
    `theatre-of-the-mind`: what the characters perceive, ending on a moment
    they can act on.

## Define every consequence

A consequence the page names is defined where it is named: who or what acts,
when it triggers, the numbers (damage, DC, condition, duration, count), how it
ends or can be avoided, and what the players perceive. Phrases that name a
system — *the island responds*, *convergence*, *the curse spreads*,
*reinforcements arrive*, *the ritual advances*, *faction standing drops* —
carry their operative effect on the page. When the rule lives on a lore or
rules owner, link it and copy the lines this beat uses. When no owner defines
it and the user has not supplied it, the beat is incomplete: define it with the
owner skill first (**HARD: entity-before-spoken**), or return the gap as a
blocker.

## World voice

Write what the world does, case by case: "If the party surrounds Skarn, he
throws the chain around the nearest tree and swings 20 feet onto the ledge."
Player agency lives in the coverage of the outcome and handle rows — every
likely approach has a world response — so the page needs no coaching lines.
When a draft sentence tells the DM how to behave ("do not railroad", "let the
players decide", "do not script the theft"), replace it with the world
response it was protecting.

## Spoken and DM layers

Spoken text carries what the characters can perceive. Mechanics, DCs, hidden
truth, and consequence forecasts ("eating it will draw the island's anger")
stay in the DM layer; the players learn consequences by seeing tells or paying
costs. The DM layer states everything plainly — names, wants, true stakes, the
answer to every mystery the beat plants (**HARD: dm-facing-explicit**).

## Inform, entertain, push

Each beat informs (the table learns something), entertains (one memorable
element: a striking image, a set-piece feature that transforms, an NPC with an
edge, a reversal), and pushes the plot visibly forward (Pondsmith, *Scripting
the Game*). Name the memorable element in the DM layer so it reaches play.

## Spotlight

Each PC present has a reason to act in the beat: a personal tie, an obvious
job their abilities fit, or a stake in an outcome. Across a session every PC
gets at least one beat where their tie drives the scene.

## Lean page

The page carries what this beat spends. Owner essays, full statblocks, and
history stay on owners and are linked or embedded; the operative numbers and
facts the DM needs mid-play sit on the page. Cut a line when removing it
changes no choice, roll, spoken picture, risk, route, clock, resource, or NPC
response.

## Cold read (completion check)

Read the finished page top to bottom as a DM who has never seen the prep.
Stop at each moment the players could act — the opening, each handle, each
tick, each outcome — and answer from the page alone: what happens, what the
roll is, what changes. The beat is table-ready when:

- every moment has its answer on the page;
- every consequence term is defined;
- opposition that can fight has numbers and a tactics line;
- every named actor, place, and item has an owner link;
- the spoken layer carries only perception;
- the carry-forward names each state variable the next beat inherits.
