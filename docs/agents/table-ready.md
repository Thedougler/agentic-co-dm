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

Observed failure this bar exists for: a Climax page said "apply the island's
convergence" without ever saying what convergence does, sent the villain's AC
and HP to his owner page, and spent its pressure table on advice to the DM
("do not make him immune") instead of what the villain does. The structure was
right; the DM still had to invent the fight.

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
2. **Cast.** Every actor on the page, named or rank-and-file, links its owner
   page and states, for this beat:
   what it wants now; what it does next if nobody interferes; what it offers,
   withholds, or lies about; what shifts its posture. Every side the party could
   choose to fight carries compact numbers copied from its owner statblock — AC, HP, Speed, the
   one or two attacks or save DCs the DM will actually roll, the trait that
   changes tactics — plus a tactics line: opening move → how it adapts when
   countered → break point → exit or surrender. An owner with no statblock
   gets one as a proposal (a named standard 5e statblock, adjusted, is fine),
   filed on the owner before the beat depends on it. Opposition with no owner
   at all is minted through `monster-design`'s Reskin path first.
3. **Space.** Where the beat happens, with distances in feet where position
   matters; two or three interactive features, each with its obvious use and
   the ruling it produces (half cover, difficult terrain, a DC to climb, damage
   when it falls); one way the space changes during the beat.
4. **Pressure.** Why now. A fuse with three or four named ticks, each with its
   trigger and what newly becomes visible, threatened, blocked, or lost. Ticks
   run on world time (rounds, hours, dusk) or on visible triggers; a tick that
   advances on table time says so. What
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

## Cast before minting

A beat's actors, places, items, and creatures come from the wiki first. Before
minting an owner, search the campaign with `qmd` for a page that can fill the
role, and cast in this order:

1. **In play.** A page the fiction already points to: a revealed actor
   returning, a place the party has been, an item they carry.
2. **Unrevealed.** A page with `reveal: unrevealed` that fits the role. The
   players have not met it, so it lands as a discovery while paying off prep
   already made. A page's canon facts (the rule in [`llm-wiki`](../../.agents/skills/llm-wiki/SKILL.md#canon)) stay;
   unrevealed details may be reshaped for the beat (its want, location, or
   ties) through its owner skill. A page an unplayed beat already depends on stays
   consistent with that beat.
3. **Mint.** Only when no page fits: the role needs a fact no existing page
   carries, or every candidate would contradict canon or the beat. Mint it
   with its owner skill before any text depends on it.

Done when every owner the beat needs is linked, and each new mint names, in
the response to the DM, the candidates considered and why none fit.

## Fill the silence

**Decide the world; leave the party's choices open.** Prep is where invention happens. Retrieve first; where canon is silent or
contradicts itself on something the beat needs (a motive, a name, a statblock, a reaction, a
reward, the opposition's next move, a deadline), decide it (constitution XII).
Each decision is stated plainly where the DM will use it, filed on its owner
page when it belongs to an owner, marked by the page's `invention: true`, and
listed in the response to the DM. A decision that resolves a contradiction
names the conflicting sources and the reading it chose. Canon follows the rule
in [`llm-wiki`](../../.agents/skills/llm-wiki/SKILL.md#canon).

The world is proactive. The opposition, the clocks, and the people with wants
act on their own schedule whether or not the party engages, and the page says
what they do and when. Player agency is the party's answer to that pressure,
so a beat that waits for the party to start it has not been prepped.

Canon that records something as unknown, unconfirmed, or open is silence
too: it names what has not been decided yet, and prep decides it with a
proposal when the beat needs it.

A fact the page leaves open hands the DM an invention job mid-session and
fails **HARD: dm-facing-explicit**. Fill it with a proposal, and make each
proposal one concrete answer: the named suspect, the real hiding place, the
specific object. A list of possibilities is silence left unfilled.

## Define every consequence

A consequence the page names is defined where it is named: who or what acts,
when it triggers, the numbers (damage, DC, condition, duration, count), how it
ends or can be avoided, and what the players perceive. Phrases that name a
system — *the island responds*, *convergence*, *the curse spreads*,
*reinforcements arrive*, *the ritual advances*, *faction standing drops* —
carry their operative effect on the page. When the rule lives on a lore or
rules owner, link it and copy the lines this beat uses; when that owner points
onward, follow it to the page that holds the numbers. When no owner defines
it, decide it now (§ Fill the silence) and file it on its owner with the owner
skill before the beat depends on it (**HARD: entity-before-spoken**).

## World voice

Write what the world does, case by case: "If the party surrounds the smuggler, she
cuts the lantern rope and swings 20 feet onto the barge." Every DM-facing
sentence is a fact, a ruling, or a world response. Player agency lives in the
coverage of the outcome and handle rows: every likely approach has a world
response, so the page speaks about the world and never about the DM's conduct.
When a draft sentence addresses the DM's behavior, replace it with the world
response it was protecting.

## Spoken and DM layers

Spoken text carries what the characters can perceive. Mechanics, DCs, hidden
truth, and consequence forecasts ("drinking it will wake the curse")
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
- the pressure has named ticks, and hesitation advances it by one
  concrete, visible step;
- every consequence term is defined;
- every side the party could choose to fight has numbers and a tactics line;
- every outcome resolves on this page or hands to a beat that exists or is
  charted; no row sends play to an encounter, statblock, or page not yet made;
- every actor, creature, place, and item the page shows has an owner link,
  unnamed rank-and-file included (one creature page covers the group);
- the spoken layer carries only perception;
- every fact, clue, and route is one concrete answer (who, what, where),
  with proposals listed for the DM;
- every DM-facing sentence is a fact, a ruling, or a world response;
- every link resolves to an owner file's basename, and no template
  placeholder text remains;
- the carry-forward names each state variable the next beat inherits.
