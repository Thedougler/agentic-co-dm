# Composition — core model, modes, workflow detail, branch discipline

The full composition procedure behind the `.claude/skills/composing-beats/SKILL.md` workflow skeleton.

## Core model

### Beat

A Beat is an atomic playable unit with a dramatic function, instantiated
from its `vault/_templates/_episodes/_beat_<type>.md` template. Its
specialized skill owns its internal construction.

The orchestrator cares about:

- **type** — Hook, Development, Cliffhanger, Climax, or Resolution (`beat_type:`);
- **entry state** — conditions under which the Beat becomes playable;
- **Link of Relevance** — why players already care;
- **pressure** — what makes engagement meaningful now;
- **possible state changes** — materially different conditions play may produce;
- **handoff** — what kinds of Beats become appropriate afterward.

Every state in **possible state changes** is a legal exit; the beat ends
on whichever one play produces.

### State

A **state** is what is materially true before or after play:

- who possesses something;
- who knows something;
- where someone is;
- who trusts whom;
- which threat is active;
- what resource remains available;
- which faction has leverage;
- what danger has become immediate;
- what objective has become possible;
- what consequence has already occurred.

Compose Beats through **state transitions**, not scripted scenes.

### Gravity

**Gravity** is established player investment.

Prefer pressures connected to something the characters already pursue,
fear, protect, resent, owe, desire, or need. The Link of Relevance records
that connection explicitly. A Beat with strong gravity needs little
coercion.

### Irrigation

**Irrigation** is preparation that shapes an interesting route while
leaving route selection to the players.

Place obstacles, opportunities, enemies, allies, costs, revelations,
deadlines, conflicting interests, and consequences — where player gravity
makes collision plausible.

The obstacle supplies dramatic shape. Player choice supplies direction.

### Rhythm

**Rhythm** is the alternation of dramatic functions. For a complete
adventure-level Beat Chart:

1. begin with a Hook;
2. follow the Hook with a Development or Cliffhanger;
3. alternate Development and Cliffhanger thereafter;
4. enter the Climax when the central question becomes decisively contestable;
5. follow the Climax with Resolution.

An action-heavy Hook normally hands off to Development. A cerebral or
low-action Hook normally hands off to Cliffhanger. For an action-oriented
Climax, prefer Development as the final pre-Climax Beat. For a primarily
mental, revelatory, social, or intellectual Climax, prefer Cliffhanger as
the final pre-Climax Beat.

Apply these rules to the **path that becomes active**, not by forcing
every prepared candidate to occur. Pacing heuristics:
`rhythm-and-pacing.md`.

### Escalation

Later Beats should inherit consequences from earlier play and make the
situation more consequential. Escalation may increase danger, cost,
intimacy, exposure, opposition, urgency, uncertainty, moral difficulty,
political consequence, or personal relevance.

Escalation means **more consequential**, not merely larger.

## Composition modes

Choose the mode from the current state of play.

### Beat Spine

Use a **Beat Spine** when player action has already established a
sufficiently clear direction. A Beat Spine is the most plausible current
dramatic sequence:

```text
Hook → Development → Cliffhanger → Development → Cliffhanger → Development → Climax → Resolution
```

The spine predicts dramatic **functions**, not player decisions or
outcomes. Every future Beat remains conditional on the state needed to
activate it.

### Beat Field

Use a **Beat Field** when several genuinely different directions remain
live. A Beat Field contains multiple candidate Beats connected by
state-dependent transitions:

```text
                         → Cliffhanger: pursuit
                        /
Development: revelation
                        \
                         → Cliffhanger: defend the ally

either changed state → Development candidates → eventual Climax when earned
```

Prepare branches around **materially different states**, not hypothetical
lists of every action players might attempt.

Good branch:

> If Captain Vara keeps the relic, the Church moves openly against her.

Good branch:

> If the party gains the relic, Vara instead seeks an alliance before the
> Church reaches them.

Weak branch structure: "If the players attack... If the players
negotiate... If the players sneak..." Those are methods. Players invent
methods. Prepare consequences of changed states.

### Re-orchestration

Use **Re-orchestration** after play invalidates or bypasses prepared
material. Treat the newly established state as authoritative. Then:

1. preserve consequences that still exist;
2. retire Beats whose entry conditions can no longer occur;
3. identify newly activated pressures;
4. determine the next appropriate Beat type;
5. compose or select the next Beat from current gravity;
6. rebuild only as far ahead as preparation remains reliable.

Skipped prep is not a failure. It is unused possibility.

## Workflow detail

### Step 1 — Compile the current playable state

Retrieve the smallest authoritative set of vault material sufficient to
understand: the PCs currently involved; their relevant gravity; the
current location or situation; active actors and factions; unresolved
threats; established relationships; current knowledge; prior consequential
player actions; existing prepared Beats; the dramatic question, if already
defined.

Prefer compiled entity and campaign pages over raw session material.
Follow the repository's retrieval ladder rather than reading the entire
vault reflexively.

**Complete when** every fact needed to compose the next dramatic structure
is either supported by current vault material or explicitly identified as
new prep rather than established canon.

### Step 2 — State the dramatic question

Write one question whose answer would materially change the situation.

Examples:

- Will the party expose the duke before he secures control of the council?
- Can Mara reconcile with her brother before the rebellion forces them onto opposite sides?
- Who will control the Ember Crown when the three claimants converge?
- Will the town accept the witches' protection once the truth about the abbey becomes public?

The question must permit multiple meaningful answers. Prefer questions
about **contested situations** over questions whose ending is already
implied. The dramatic question may evolve as play changes what matters.

**Complete when** the question identifies a real conflict; at least two
materially different answers remain possible; player action can influence
which answer becomes true; and answering it would justify a Climax.

### Step 3 — Map player gravity

For each relevant PC, identify only the investments bearing on this
situation, from established vault material: explicit goals, fears,
enemies, loyalties, relationships, promises, beliefs, debts, unresolved
history, desired resources, threatened people or institutions.

Do not manufacture a new backstory fact merely to make preparation
convenient. Record the strongest applicable gravity beside the
composition.

**Complete when** every Beat intended for advance preparation can carry at
least one concrete Link of Relevance to established player material.

### Step 4 — Determine the current Beat position

Identify: whether this is a new bounded adventure requiring a Hook;
whether play is already inside an existing Beat structure; the most
Beat type completed last; the dramatic function now needed; whether
the situation is already Climax-ready.

For ongoing campaign play, a new session does **not** automatically imply
a new Hook. Sessions may begin halfway through an existing dramatic
structure. The Beat Chart belongs to the **playable situation or
adventure**, not to the calendar.

**Complete when** exactly one of these is true: a Hook is required;
Development is the next structural function; Cliffhanger is the next
structural function; the Climax readiness gate must be evaluated;
Resolution follows an already-played Climax.

### Step 5 — Choose Spine or Field

Choose a Beat Spine when current player direction makes the near future
reasonably predictable. Choose a Beat Field when several materially
different state transitions remain plausible.

For a Beat Field, branch only when a different result would change:
opposition, available allies, stakes, location, information, leverage,
resources, objective, or the dramatic question itself.

Let different methods leading to the same meaningful state share the same
continuation. Prefer a small number of high-value branches over
speculative combinatorics.

**Complete when** every retained branch corresponds to a materially
distinct playable state and no branch exists solely to predict a player
method.

### Step 6 — Compose atomic Beats

For each needed Beat:

1. assemble a context packet;
2. delegate creation or revision to its specialized beat skill;
3. store the Beat at its owning path, instantiated from its beat-type template;
4. reference it from the composition rather than duplicating its body.

The context packet passes the specialized skill: dramatic question;
current state; relevant PCs; Link of Relevance; active opposition;
preceding Beat and its known consequences; required Beat type; intended
escalation; known downstream constraints; authoritative wikilinks; facts
that remain unknown. For a candidate branch, include its entry condition
explicitly.

**Complete when** every required Beat exists as a valid atomic unit and
every composition reference resolves to its single source of truth.

### Step 7 — Connect Beats by state

For every transition, ask:

> What must be true after the first Beat for the next Beat to become
> appropriate?

Connect Beats only through conditions the preceding play could actually
establish. A transition may use a **shared invariant** when several
outcomes all activate the same next pressure:

> Whether the envoy escapes or is captured, the attack publicly exposes
> the conspiracy.

That shared consequence may support the same next Development. A
transition that requires one specific player decision is too narrow unless
that decision has already happened.

**Complete when** every edge in the composition is justified by an
achievable world state rather than an assumed player choice.

### Step 8 — Audit rhythm

For every prepared path, verify the Beat grammar (see Rhythm above and
`rhythm-and-pacing.md`). All branches preserve the
Development/Cliffhanger alternation unless they terminate by legitimately
reaching the Climax. The Hook selects its first handoff according to its
dominant energy. The final pre-Climax Beat contrasts with the Climax's
dominant mode where practical.

**Complete when** every currently plausible path has coherent dramatic
rhythm and no Beat exists merely to satisfy a numeric quota.

### Step 9 — Audit escalation and repetition

Compare each Beat to the previous Beats. Each should create a meaningful
change in at least one dimension: knowledge, relationship, leverage,
danger, urgency, available choices, resources, allegiance, stakes,
position.

Later Cliffhangers should generally apply greater pressure than earlier
ones. A later Development should exploit consequences already created
rather than restating information the party already possesses. Prefer
escalation by **specificity and consequence** before escalation by
spectacle.

**Complete when** every retained Beat changes the playable state and no
two adjacent Beats perform substantially the same dramatic job.

## Branch discipline

Sandbox preparation can explode combinatorially when every imagined
decision becomes a branch. Control branching through **state
convergence**.

- **Branch on consequence** — create a branch when a choice produces a
  substantially different world state.
- **Converge on shared facts** — when several approaches create the same
  important consequence, reconnect them.
- **Prepare fronts, not menus** — actors continue pursuing their own goals
  when ignored. This gives the DM material for unexpected player routes
  without requiring a bespoke branch for every possibility.
- **Prepare nearest pressure first** — detail the next likely Beat
  heavily; detail later Beats progressively less as uncertainty increases.
  The farther preparation sits from established player action, the more it
  should describe actor intent, pressure, prerequisites, consequences, and
  likely escalation — and the less it should prescribe scene detail.

## Transitions between beats

Read when writing a Beat's opener `[!read-aloud]` box for a Beat a Live
Branches row lands on, where that row's state condition demands a
bridge — a time skip, a journey, a followed lead — the box can't just start
cold. A Beat has no sub-units, so there is no separate `Transition` box
construct — the bridge lives inside the landing Beat's own opener, folded
into its first sentence or two before the box does its normal
full-establishing job (name every subject the Live Branches row names,
close on a live element).

Read the Beat's predecessor field to find every predecessor. More than one
entry means the party can arrive here by more than one route, and the
bridge must work from each of them — or the opener carries a plain-prose
handling note per arrival, and the DM reads the one that happened.

A transition-carrying opener is 1–3 sentences of bridge, then the rest of
the opener's usual work. Its job: close the outgoing Beat, carry the
party through time and space, and land the table oriented in the new
frame — so a landing feels like the story moving, not the DM shuffling
files. In order, it answers: what just closed, what passes (time or
distance), where the party stands now and what is already in motion there.

### The four cuts

| Cut | When | Shape |
|---|---|---|
| **Travel compression** | The party moves somewhere with nothing playable between | One clause leaving, one arriving — steal a sensory detail from each end so both places feel touched |
| **Time skip** | Hours or days pass (rest, downtime, waiting) | Name the elapsed time concretely; show one thing that changed while it passed |
| **Follow the clue** | The prior Beat produced the lead the party is chasing | Restate the lead in-fiction as the connective tissue — the trail itself carries them to the new frame |
| **Hard cut** | Peak-moment cut to another place, group, or timeline | End mid-motion, open the new frame cold — no smoothing; the jolt is the point (`rhythm-and-pacing.md` § The dramatic cut) |

### Example

> [!read-aloud]
> You leave the smuggler zip-tied to the mooring post as the dawn bell
> rings. By the time the fog burns off, the runner's trail has carried you
> over three rooftops and down into the warehouse quarter — where one
> door stands ajar, lamplight leaking under it. [...establishing continues:
> layout, who else is present, what's moving...]

### Rules

- **1–3 sentences of bridge**, then the opener's normal establishing work —
  a bridge alone, with no full opener following, means the landing Beat
  is under-written, not that the bridge ran long.
- **Orient before anything happens.** New place, elapsed time, and who is
  present all land before any NPC speaks or any check is called.
- **Execute the state condition, never make a choice.** The bridge carries
  out what the Live Branches row already resolved ("we head for the
  warehouse") — a box that says "you decide to…" is a railroad line, not a
  landing.
- **Player-known information only** — same contract as every read-aloud
  box (`callouts` skill, references/read-aloud.md): no DCs, no DM-only
  facts riding in on the scenery.
- **Be ready to throw it away.** A written bridge covers the Live Branches
  rows on the page; when the table lands somewhere else, improvise the
  same three-part shape — close, pass, orient — instead of reading a box
  that no longer fits.

Sentence craft: `dnd5e-scene-narration`. Container: `callouts` skill,
references/read-aloud.md.

## Running a Beat at the table

Read when writing a Beat's own content, or running any *non-combat*
branch point at the table. Source: `vault/refs/tools-for-5e-improvisation.md`,
`vault/refs/quick-tricks-for-lazier-5e-games.md` (the non-combat tricks only).
This section owns the generic describe/intent/adjudicate loop and DC-setting
— nothing combat-specific. For a combat branch point, load `encounter-
prep`'s `.claude/skills/encounter-prep/references/running-the-encounter.md` instead: positioning
without a grid, identifying monsters and picking targets, improvised
stat blocks, zone movement, passive monster initiative, and cinematic
advantage all live there now, not here — this section doesn't duplicate
them.

### The core loop

Every branch point, combat or not, runs the same three-beat loop:

1. **Describe the situation** — what's true right now, in the fiction.
2. **Ask for intent** — what does the player want to accomplish? Push past
   a vague answer ("I move close to the orcs") toward a specific one ("I
   want two orcs in reach of my glaive").
3. **Adjudicate** — call for a check only if there's real uncertainty and
   an interesting failure; otherwise just say what happens.

Work with the players, not against them — be generous, and favor the
characters when a call is close.

### The page's half of the loop

The Beat page owns step 1 and nothing below it. Steps 2 and 3 happen at
the table, with the players in the room, and a page that writes them has
done the table's job badly and in advance — it cannot know what the party
reached for. So the page loads the situation: what is here, who wants what
and how they pursue it, what is already in motion, what is hidden, and what
changes if nobody intervenes. Then it stops.

Three shapes that mean the page has crossed into step 2:

- **The scheduled beat.** A named PC handed a night, a reveal, or a private
  thing of their own — "three days of enforced closeness surface four
  private things, one apiece". The party arrives together; whatever surfaces
  surfaces because a player reached for it, so the page never budgets beats
  per head or promises a count of them.
- **The choice menu.** A named PC with outcome branches under them — press
  or let go, build it or ship it, sit in it or leave it dark. Those are the
  player's two answers written down before the question was asked.
- **The borrowed toy.** A toy pointed at a PC instead of at the opposition.
  A toy is profiled the way `vault/refs/vault/faction/references/toy.md`
  profiles a faction — want as a vector, table-doable method, current
  problem, off-screen action — and every one of those fields belongs to
  something acting *on* the party: the NPC with an ask, the hazard
  advancing, the window closing, the rival moving while nobody watches.

#### Before and after

**Before** — the page decides for the players:

> Three days of enforced closeness surface four private things, one apiece.
> **Day one, the crate.** [[perrin-black-jaw|Perrin]] finds Jean-Claude in
> the hold with a crate he loaded himself in [[calveno|Calveno]].
> *Pressed:* his face gives it up before his
> mouth does. *Let go:* the seal holds, and the question comes back harder.

**After** — the page loads the situation and leaves the answer open:

> Jean-Claude sleeps against a crate that predates the crew's ownership of the ship, at the bottom of
> the hold where the spare cordage lives, so the crew has business down
> there whether or not they have questions. The seal sweats a little more
> each warm day and the smell coming up the hatch is sharper by the third —
> crushed leaves steeped in alcohol, the same note the [[rattkin|Rattkin]] on the
> Calveno docks would place in one breath. His Mortis curse permits him no
> lie past a direct question and compels him no answer, and he will move
> the crate to the chain locker the first night nobody is watching it.

The after is longer, not shorter. **Detail about the world is the point;
detail about what a player will do is the defect.** A vague, low-risk
situation fails this file as badly as an assigned beat does — cut a line
only when it decides a player's answer, never because it is specific.

### Setting the DC

- **DC 10** easy, up to **DC 20** very hard; DC 12 is a solid default when
  nothing else points higher or lower (§ NPCs and social checks,
  `runtime-surface.md`, covers the social-check version of this).
- **Trivial task → no roll.** If there's no real chance of failure, the
  character just succeeds.
- **Don't roll if failure isn't interesting.** Never bury vital or useful
  information behind a single ability check — a failed roll should change
  what happens next, not just withhold the plot.

#### Write the check so it can be declared aloud

The two techniques below are `vault/refs/blm-mechanic-theatricalization.md`;
this section states what they demand of the page.

- **Both outcomes, on the page, before the roll.** A high-stakes check is
  announced — DC and what each result costs — and only then rolled, in the
  open. That only works if the page already carries both branches written
  out, so the DM is reading them rather than inventing a consequence after
  seeing the die. A page that states only the success branch forces a
  fudge.
- **Tier an investigative or social check rather than passing it.** Prep
  three thresholds, not one: the low tier still yields a crumb that moves
  the situation, the high tier reveals what was actually hidden. This is
  what keeps the previous rule's "failed roll should change what happens
  next" true in practice — no tier is a dead end.

### Combat branch points

Positioning without a grid, identifying monsters and picking targets,
improvised stat blocks, zone movement, and monster-initiative/cinematic-
advantage tricks are all `encounter-prep`'s territory now — load
`.claude/skills/encounter-prep/references/running-the-encounter.md` there rather than adjudicating a
fight from this section.

### Keep the Beat alive

Go big with description between turns — the Beat goes stale if the DM
stops reinforcing what's happening. Ask players to describe their own
killing blows and interesting actions; it costs nothing and buys in the
whole table.

## NPC guidance — NPCs speaking, the ask, and overheard gossip

Read when a Beat has an NPC who talks to the party, or when the opener
could carry background chatter. Doctrine and its reasoning:
`vault/refs/npc-guidance.md`. This section covers only how it lands in a
Beat page.

### One NPC addresses the party

Exactly one NPC speaks to the party in an opener. Every other NPC present
gets a clause naming what their hands are doing instead of talking — enough
that a player can walk over and start a conversation, never enough to make
the opener a scene the table watches.

Never stage two [[vault/refs/vault/location/references/npcs|NPCs]]
conversing with each other in front of the party. A
short line thrown over a shoulder, not involving the party, is the only
exception (`vault/refs/npc-guidance.md` §1).

Pick the speaker by who wants something from the party right now. Three
NPCs drawn from the run guide's roster means one asking and two working.

### Filling `**The ask:**`

The `**The ask:**` line states what the speaking NPC wants the party to do
next, in one line, with its register named:

- **subtle** — an aside, a complaint, a half-finished sentence, something
  said while the work continues. The party decides it is a lead.
- **direct** — a stated request carrying a reason and, usually, a cost or a
  deadline.

The ask states the NPC's own want and stops there. It never states the
party's answer, never names the PC most likely to take it, and never
carries the reasons a PC would care — the want is the NPC's, the response
is the table's.

Delete the line when no NPC speaks to the party in this Beat.

A subtle ask nobody picks up is a clue, not a failure — clues come in threes
(`audits.md` §3). Plan the next one on a
different channel rather than repeating the line louder.

### Folding in gossip

Workflow step 1 queries the gossip pool:

```bash
npm run search:content -- query "<the Beat's place or subject>"
```

A hit is foldable as an overheard line when the party would recognize its
subject — a named NPC, a place they have been, a thread they are carrying, a
rumour with its own page (`vault/refs/vault/lore/references/rumour.md` owns those). No open objective is
required; recognition is the gate.

No hit means no chatter, not chatter invented to fill the space. One or two
overheard lines is a living street; more is a wall of voices the DM has to
perform.

Write each as a complete voiced line the DM can say aloud, never a topic
fragment.

## Sandbox narrative devices

A mindset lens on classic narrative devices: how to apply each one when the
campaign is sandbox/emergent rather than scripted. Read this alongside prep
work when the content being shaped is prep material (an NPC, location,
faction, encounter) rather than a finished draft. The anti-railroading
doctrine these devices must satisfy is `audits.md` § Sandbox doctrine — this
section owns only the device-by-device application.

In a sandbox, narrative devices are tools for **world-building**, not tools
for **plot control**.

- **Railroading**: you place a gun AND decide when it fires AND who it hits.
- **Sandbox narrative**: you place a gun in a visible location. Players
  decide if, when, and how it fires.

Every device below is applied through this lens — you create narrative
*potential*, not narrative *inevitability*.

| Device | Sandbox application | In prep |
|---|---|---|
| **Chekhov's Gun** | Seed the world with loaded guns across locations, NPCs, factions. Don't aim them. | Ask *what is one thing here that could become significant later?* Place it. Note it. Don't plan its payoff. |
| **Foreshadowing** | Foreshadow *conditions and threats*, not *events* — "the [[kraken\|Kraken]] has been sighted further north than usual" foreshadows danger without scripting an encounter. | Lives in NPC rumors, environmental detail, faction behavior changes, recurring symbols. Layer 2-3 per session, pointed at different possible futures. |
| **Dramatic irony** | Player-facing, not DM-hoarding — most powerful when players know the villain's plan but their characters don't. | Reveal via documents, overheard conversation, visions — then let players decide how to act. Never withhold information players would enjoy having. |
| **In medias res** | Begin every session *after* the boring part — not "you wake at the inn" but "the rope breaks on the third floor — what do you do?" | Write the Strong Start (`.claude/skills/writing-hook-beats/references/hook-beats.md` § Strong starts) in medias res by default. Ask *what is the most interesting moment to drop players into?* |
| **Escalating stakes** | Stakes escalate *because of what players did*, not a planned act two. | Maintain a live consequence chain — for each major decision, note what changes in the world because of it. |
| **Reversal (peripeteia)** | Discovered, not scripted — emerges when a player assumption turns out wrong, an ally betrays, a "solved" problem resurfaces transformed. | Give every significant NPC a secret goal contradicting the apparent one (per `.claude/skills/draft-content/references/npc.md`). Players learning the truth IS the reversal. |
| **The ticking clock** | Primary anti-passivity tool — factions pursue goals on timelines regardless of player engagement; pressure without forcing specific actions. | Every faction/villain gets a timeline of what they accomplish if unopposed. Share early steps as rumors. |
| **Anagnorisis (recognition)** | Most powerful when player-generated — the party figures out the cult's real agenda themselves. | Plant recognizable patterns across NPCs/factions/locations; design for discoverability, not revelation-on-schedule. |
| **The iceberg** | Build 3x more world than you'll use — NPCs have lives outside the party, factions have conflicts players never witness. | For every major NPC/faction, write one true thing players are unlikely to ever learn directly — it shapes how you play them. |
| **False victory / pyrrhic win** | Don't engineer these — let them emerge from real consequences (the saved fleet's cargo turns out terrible; the defeated gang's enemies fill the power vacuum). | Ask *what happens in this faction/region if the players win?* "Everything is fine" means the world isn't living yet. |

### Structural patterns: sandbox-GM failure modes

Full shape, origin, and multi-scale application for every pattern below live in
`.claude/skills/draft-story/references/story-structures.md` — the
repo's canonical structure catalog index. This section adds only the live-table
improv angle that catalog doesn't cover: common failure modes and
practical notes for running these patterns in sandbox play.

- **Episodic arc**: don't treat the island as a corridor between two fixed
  points — islands have shores on all sides, players can arrive/leave from any
  direction. Pace within an episode: establish the situation already in
  motion, raise the cost of action/inaction through the middle, force a real
  choice at the end and stop there or just after.
- **The slow burn**: seed with a symbol in three unconnected locations, a name
  a dying NPC drops that recurs in a later document, or a recurring NPC always
  present at pivotal moments but never involved.
- **The cliffhanger**: `writing-cliffhanger-beats` skill owns construction;
  cut when the table is loudest/most uncertain.
- **The Hero's Journey**: don't force the Ordeal — the low point must feel
  earned through consequences, not manufactured by the DM.
- **In medias res**: applies within scenes too, not just session openings —
  don't narrate travel or preparation, start at the moment of arrival or the
  moment the thing goes wrong.
- **The escalation ladder**: for each major threat/faction, identify which
  rung they currently occupy; track when player actions (or inaction) push
  them up a rung.
- **Convergence arc / three-act structure**: nothing sandbox-specific to add —
  read the canonical entry directly.
- **Diagnosing pacing problems**: use `audits.md` § Diagnosing a stalled or
  flat journey — it already covers the sandbox symptom set (nothing
  happening, flat escalation, repetitive sessions, disengaged players,
  ignored main plot) plus the quest-scale cross-reference.

### Layering with prep skills

This is a mindset lens, not a content generator — apply the targeted prep skill
first to generate content, then ask: *which devices are present here? Which are
missing? What would make this feel more alive?*

- **the npc guide** — apply Chekhov's Gun, Reversal, and the Iceberg when building NPCs.
- **the location guide** — apply In Medias Res and Foreshadowing to read-aloud and design.
- **.claude/skills/draft-content/references/faction.md** — apply the Ticking Clock and Convergence Arc to faction timelines.
- **encounter-prep** — apply Escalating Stakes and False Victory to combat/social encounters.
- **player-gravity** — point narrative devices at player gravity wells, not away from them.

## Opposition and reward design checklist

GM advice checklist for designing villains, antagonists, encounters, allies,
and rewards — the complement to the location checklist in
`runtime-surface.md` § Fantastic locations.

### Villains

- Start with good motivation. Good villains believe that what they are
  doing is right.
- Expect your villain to die.
- Make them memorable — what would make players do a double-take?
- A villain's progress should be visible in the world, and a villain
  should respond to character interference in their plans.
- Good villains interact with characters directly and indirectly.

### Antagonists

Contribute to the villain's agenda and often interface with the party
instead of the villain directly. Use a variety of antagonists that
represent the villain and their themes, each with clear motivations of
their own, and let them react to the story as it unfolds.

### Encounters

Good encounters serve a story purpose — avoid roadblocks. Use a variety of
encounters (combat, social interaction, physical or intellectual
challenges, puzzles), leave room for creative solutions, and vary
difficulty to aid session pacing. Design encounters to be played, and keep
them easy to run.

### Allies

No one NPC knows everything, and each should act in accordance with their
own motivations — including reacting to the villains, not just the party.
A useful ally provides clear benefits (items, information, labor) and is
written to be as memorable as any antagonist.

### Rewards

Give magic items interesting stories, and be generous with consumables.
Items that are useful only in a certain time or place create texture; so
do social rewards that make players feel important — status, property,
titles. Gold-per-level pacing convention: `runtime-surface.md` § Rewards.
