# Human DM runtime surface and after-play procedure

## The composition surface

The Beat Chart is a **control surface**, not a screenplay. Optimize it for
rapid scanning during play. It lives on the owning `type: situation` page
(`vault/_templates/_campaigns/_situation.md` governs the sections):

- **Dramatic Question** — one sentence.
- **Player Gravity** — `[[PC]] — relevant established investment`, one row per PC.
- **Current State** — material facts, one per line.
- **Active Beat** — wikilink.
- **Beat Spine** — ordered `[[Beat]] — entry trigger or state` rows.
- **Live Branches** — `**state condition** → [[Beat]]` rows.
- **Climax Readiness** — the eight gate conditions, each `ready` or `missing <condition>`.
- **Unused Possibilities** — `[[Beat]] — what could reactivate it`.

Keep full beat content on its atomic Beat page. Use wikilinks for
navigation. Use section embeds only when the DM benefits from seeing the
authoritative content inline during play. Use dynamic vault mechanisms for
rosters, inventories, or other queryable entity sets rather than
maintaining duplicate static lists.

The night's at-table walk remains the run-guide; it may transclude beat
content in play order.

## After play

The prepared composition is not evidence of what occurred. After a
session:

1. let the campaign's normal transcript-ingest workflow establish canon;
2. read the updated compiled vault;
3. determine which prepared Beats actually occurred, were bypassed, or became impossible;
4. preserve actual consequences;
5. retire stale branches;
6. identify newly active gravity and pressures;
7. determine the next required dramatic function;
8. re-orchestrate from the new state.

Rewrite prep to match actual play, and only in that direction. Prep
follows canon.

## Session shapes

The kind of night. The overview names one primary shape in
`session_shape:`. A night may mix; the primary shape decides which objects
enter the opening stretch first. Shapes are not page types — combat,
social, exploration, travel, and cold open stay a property of one Beat,
not of the night.

Pick from this closed set. Do not invent a tenth.

| Shape | The night is | Opening stretch selects | Other walks |
|---|---|---|---|
| **crossing** | Travel. The adventure can be the way. | Live `type: route` pages plus Situations that can surface on them. One plot-weight Beat only for a heading choice, a landmark peak, or arrival that changes the world. | Other routes that share water or road; Situations that fire on any crossing. |
| **site** | Inside one place: dungeon, wreck, island, building. | Situations that live in that location. Plot-weight Beats for irreversible rooms or the peak. | Adjacent locations, the route that got them here. |
| **town** | A settlement at work: harbour, market, claims, errands. | Situations and drips in that port or city. Plot-weight only for a public deed or a decision that changes standing. | Factions watching the town; the next route out. |
| **intrigue** | Faction pressure, court, audience, negotiation. | Situations whose actors have asks. One Live Branches row if the party's choice splits future situations. | Other factions' if-ignored clocks. |
| **investigation** | A hidden conclusion the table can reach. | Situations plus three distinct clue vectors (rumour, secret, NPC, place). No single locked path. | Adjacent mysteries; red herrings that are real rumours with a truth value. |
| **set-piece** | One prepared action is the spine: fight, heist, ritual, rescue. | That encounter's Situation and its plot-weight Beat. Travel and town are approaches, not the night. | Escape routes, rival arrivals, if they refuse the door. |
| **hunt** | Pursuit. The party hunts or is hunted. | The pursuer Situation plus the Route they share. Plot-weight for contact or escape. | Side water, shelters, the hunted's if-ignored move. |
| **downtime** | Time passing: craft, festival, bottle, character. | Claims, rumours, NPC asks, one Situation that can interrupt. Combat is overflow, not the spine. | The Front that advances while they rest. |
| **climax** | A relocatable tentpole. The prepared peak lands wherever the party is. | One peak Situation or Beat. Other islands reskin here. | The cut peak relocates; it is not spent. |

### Rules

1. **Name one primary.** Mixed nights are legal (a town open then a crossing). The primary shape is the one that fills most of the four hours.
2. **Menu, not graph.** Do not author a passage or a Beat to make a shape feel real. Select Routes and Situations; add a Beat only when Q10's gate holds.
3. **Drip in every shape.** Opening-stretch spoken samples carry at least one rumour, secret presentation, NPC line, or environmental tell as ordinary texture, sourced from a real page.
4. **World stays reactive.** NPCs and Fronts move in every shape. Downtime is not a flat backdrop; climax is not a scripted win.
5. **Strong Start is not a shape.** Open with one of `.claude/skills/writing-hook-beats/references/hook-beats.md` § Strong starts (session openers)'s five types, varied from last session, inside whichever shape tonight is.

### Picking

- Party will spend the night on a route → **crossing**
- Party will spend it inside one keyed place → **site**
- Party is in port with no forced departure → **town**
- The live pressure is a faction or an audience → **intrigue**
- Play fails unless they can reach a hidden conclusion → **investigation**
- One prepared action is why tonight exists → **set-piece**
- Someone is closing or fleeing → **hunt**
- The table asked for craft, festival, or a quiet night → **downtime**
- A season hinge or relocatable tentpole → **climax**

## Check tables

After every spoken picture of a place, person, or object, write one
`[!check]`. Title is the picture. Body is the table. Contract:
`.claude/skills/callouts/references/check.md`.

Source every row from a Discoverable line, an Actor want, a secret, or
an object already on the pictured page. A four-band group roll is a row
in this same table — Failure holds CF and F, Pass holds S and CS.

Worldview sets an NPC's starting social DC: § NPCs and social checks, below.

## NPCs and social checks — worldview and social-check DCs

Read when filling the NPCs section. Source: `vault/refs/ideas/npc-generator.md`.

### Roster entry format

Every roster NPC opens with a scannable **Wants:** line — the motivation
the DM improvises from, stated as a want, not a backstory fact — then
voice, then mannerism (SKILL.md Hard Rule 13):

```markdown
**<NPC Name>**
**Wants:** <what they're pushing for right now, one sentence>
**The ask:** <what they want the party to do next, and its register>
**Voice:** <how they sound — cadence, vocabulary, a verbal tic>
**Mannerism:** <one physical tell a DM can perform without thinking>
**Opening:** <job they're mid-way through> · <their first line, a question>
```

**Wants** is the motivation the DM improvises from; **the ask** is the line
the party can act on. The register is a choice about how hard the party is
being steered — subtle (an aside, a complaint, something said while the work
continues) or direct (a stated request carrying a reason and a cost or
deadline). Full rule, including what to do when a subtle ask goes unheard:
`vault/refs/npc-guidance.md` §2.

A roster NPC who never speaks to the party has no ask — drop the line for
them. In any one Beat only one NPC addresses the party
(`vault/refs/npc-guidance.md` §1), so a Beat drawing three NPCs from
this roster still has one asking and two working.

The **Opening:** line exists so the DM never has to invent an entrance at
table speed. The NPC is doing something when the party arrives and speaks
first, asking — that hands initiative straight back instead of leaving the
table with a description to react to
(`vault/refs/stories/prose-and-character-craft.md` § NPC entrance).

This is the roster-slice version of the npc guide's full want + method +
problem Toy Method — a full NPC page still gets that complete treatment;
this format exists so a DM scanning the guide mid-session finds the want
in one glance instead of buried in prose. Link the NPC's own page if it
has one rather than duplicating its Toy Method fields here.

### Worldview sets the starting DC

Give a key NPC a one-word worldview (surly, friendly, brash, suspicious,
loyal, opportunistic, greedy, cautious...) — it sets their starting
social-check DC before the party's approach adjusts anything. The DC
technique itself (the scale, the default, the approach adjustment) is
the npc guide's — load `vault/refs/vault/npc/references/social-checks.md`'s
§ Worldview and social checks rather than restating it here.

### Improvised NPCs

Most NPCs at the table are improvised, not prepped. Keep ready:

- A curated name list (`vault/refs/table-npc-names.md`, or
  `vault/refs/tools-for-5e-improvisation.md` § Names) — don't invent
  names cold at the table.
- 2–3 archetypes from popular fiction (the mentor, the rival, the desperate
  merchant) to wrap a name and worldview around on the spot.
- A job for their hands. An improvised NPC gets the same entrance as a
  prepped one: caught mid-task, turning to the party, speaking first with a
  question.

Only the NPCs critical to this session's planned events need a full name +
connection prepped in advance; everyone else can be worldview + archetype,
improvised live.

## Secrets and clues — the four-category prompt method

Read when filling the Secrets & Clues section. Source:
`vault/refs/ideas/creating-secrets-and-clues.md` (Sly Flourish's LGMRD).

This section is about *what kind* of secret to write — a generative prompt
method. It doesn't own how many independent clues a single conclusion
needs; that structural rule is `audits.md`
§ Three-Clue Rule (`runtime-surface.md` §4 points there too) — read that
file for seeding a mystery so no one failed check dead-ends it. Use this
section to decide the *content* of each clue once you know how many you need.

A secret or clue is written **before** deciding how it's discovered — keep
it abstract from its place of discovery so it can be dropped in wherever
play makes sense, rather than gated behind one specific room or roll.

### The four categories

Spread your 7–10 secrets across these categories rather than writing them
all from one angle. Each is a prompt list — pick freely or roll a d10.

**Character secrets** (tie a PC to the world): family history revealed,
what ties them to this location, what NPC they think is dead still lives,
what previous event ties them to the story.

**Historical secrets** (local/world history, bite-sized): what dead god has
a connection here, what ancient civilization once thrived here, what
horrific monster once ruled here.

**NPC and villain secrets** (introduce a villain before the fight): what
dark history follows them, what do they desire, what secret do they want
kept hidden.

**Plot and story secrets** (move the larger campaign forward): what
villainous event will soon come to pass, what dungeon entrance just became
revealed, what armies just invaded the realm.

Full 10-entry prompt list per category: `vault/refs/ideas/creating-secrets-and-clues.md`.

### Mouths for tonight

A secret stays unbound to its discovery method — that is the whole point of
writing it this way. What the run guide's `## NPCs` roster records instead is
which NPC is *able* to say a given secret if the party presses them: a
capability, never an assignment. The DM still improvises which channel it
actually arrives through.

Nothing forces a secret through a mouth. A session where every reveal comes
from someone talking has under-used its other channels
(`vault/refs/npc-guidance.md` §3) — move at least one to a document, a
physical trace, or an overheard line.

### Rule of thumb

Seed 1 secret per player tied to their background or class (Character
category), then fill the rest across Historical/NPC/Plot so the session has
texture beyond "things about the party." Don't overthink a secret's
perfection — it exists to serve the table, not to be a puzzle in itself.

## Rewards — a default gold-per-level pacing convention

Read when filling the Rewards section, or when `.claude/skills/draft-content/references/run-guide.md`'s "Degrade by
asking" fires for Rewards (no established loot-pacing convention on file).
Source: `vault/refs/vault/item/references/treasure-generator.md`.

Check `vault/campaigns/shattered-sea/pcs/*.md` for an established rhythm first (per `.claude/skills/draft-content/references/run-guide.md` § Degrade
by asking) — an existing pattern always wins over this default. When
there's genuinely nothing on file, propose the table below to the DM
instead of asking cold; it turns "what feels earned?" into an accept/reject
call.

### Gold per level (default proposal)

| Level | Gold per Parcel |
| --- | --- |
| 1st–4th | 100 gp (3d6 × 10 gp) |
| 5th–10th | 1,300 gp (3d8 × 100 gp) |
| 11th–16th | 7,000 gp (2d6 × 1,000 gp) |
| 17th–20th | 70,000 gp (2d6 × 10,000 gp) |

Award roughly four parcels per level, or combine parcels for one larger
reward. Vary the exact numbers slightly (two 1,300 gp parcels might become
1,145 gp and 1,422 gp) so hoards don't look uniform.

### Beyond coin

Magic items if the session's story earns one — a consumable (potion,
scroll) for a smaller beat, a permanent item for a bigger one. Story
rewards (renown, favors, information, titles) count too, and a magic item
is itself a good delivery mechanism for a secret or clue
(§ Secrets and clues, above).

A reward that's a physical document — a deed, a letter of introduction, a
contract — is a handout, not a description of one: run `.claude/skills/draft-content/references/handout.md`'s
stub check first (a hit means link the existing page; nothing on file
means hand off to create it) and link its page here rather than
paraphrasing its contents.

## Living world detail and town arrival

Read when filling the Living World Detail section, or when a Strong Start
or scene opens with the party arriving somewhere. Source: `vault/refs/table-random-town-events.md`, `vault/refs/table-living-world-events.md`.

### Living World Details (the section's own table)

One small thing changed while the party was elsewhere. Pick or roll:

1. The favorite shopkeeper sold the business to someone new.
2. Locals are talking about an amazing performance a few nights ago.
3. A noticeable fashion trend begins.
4. Locals are celebrating an oppressive tax being outlawed.
5. Locals are lamenting a new heavy tax on their wealth.
6. The favorite tavern shuts down.
7. A known NPC dies in an accident.
8. A local economy is thrashed by a natural disaster.
9. A known NPC is hard to reach after celebrating a new child's birth.

Full d10 table: `vault/refs/table-living-world-events.md`.

### Town arrival — four quick rolls

When a session opens in (or returns to) a settlement, four small tables
build the texture in seconds: the town's current **sentiment** (happy,
suspicious, harried...), a **mundane event** in progress (market day, a
funeral, a brawl), the **weather**, and — occasionally — a **fantastic
event** (an unexpected eclipse, a meteor shower) for when the session needs
a bigger opening beat. Full tables: `vault/refs/table-random-town-events.md`.

This pairs naturally with a Strong Start's Interrupted Routine type
(`.claude/skills/writing-hook-beats/references/hook-beats.md` § Strong starts (session openers), authored by
`writing-hook-beats` for the session's opening Beat) — the mundane event is the
routine, the fantastic event or Living World Detail is what interrupts it.

## Fantastic locations — the six-item checklist

Read when filling the Fantastic Locations section. Source: `vault/refs/vault/location/references/tips.md`.

Check every location against all six before calling it done:

- **One defining trait** — a single image the location is known for (a
  giant sundial, brains in jars), blown up rather than buried in a list of
  details.
- **Familiar** — an anchor the players recognize (stone pillars) before the
  fantastic twist lands.
- **Functional** — the location has a reason to exist; who built it, and
  why here.
- **Fantastic** — the twist on the familiar anchor (those pillars hum with
  arcane lightning).
- **Description** — 2–3 atmospheric details beyond the defining trait:
  smells, sounds, textures.
- **Change** — older, bigger, more dangerous, or the only one of its kind;
  a location is more memorable when it's an extreme, not an average
  example of its type.

### Worked example

*The Sunspire* — defining trait: a blazing beam of light shining straight
to the heavens. Familiar: a stone watchtower. Fantastic: the beam is solid
enough to climb, and it's slowly sinking into the ground. Functional: built
to hold a captured star; a captured star. Description: the air here hums
faintly, and the stone floor is warm underfoot even at night. Change: the
last of three such towers still standing.

## Prep-entity floor

Read this before generating any prep entity: `.claude/skills/draft-content/references/npc.md`,
`.claude/skills/draft-content/references/location.md`, `.claude/skills/draft-content/references/faction.md`,
encounter-prep, `.claude/skills/draft-content/references/item.md`, `.claude/skills/draft-content/references/monster.md`,
`.claude/skills/draft-content/references/quest.md`, `.claude/skills/draft-content/references/lore.md`, rule-prep,
`.claude/skills/draft-content/references/campaign.md`, travel-events, draft-run-guide, or any
skill instantiating a template at `status: pending`. Cite this file from the skill's SKILL.md
instead of restating these rules.

### 1. Stub check (before creating anything)

Before instantiating a new template, grep for an existing page:

```bash
grep -ril "<entity name>" vault/ 2>/dev/null
```

If a stub or page already exists, expand it in place — never create a duplicate. If
two hits might describe the same entity, stop and ask the DM. Ambiguous identity is a
DM escalation, not an auto-merge (L6: name the specific question, don't guess).

### 2. The PC-Connection Requirement

Every prep entity must name the specific PC whose backstory, goal, fear, or wound it
pulls on. This is non-negotiable — an element with no named PC connection isn't ready
to generate. The reason it is non-negotiable is `vault/refs/blm-player-gravity.md`:
material anchored to what a character is already invested in needs no one to opt into
it, which is what makes prepared content worth preparing.

- **Ask, don't invent.** If the interview or the user's message doesn't already answer
  this, ask before generating. Ask every open question the entity needs **at once**,
  never one at a time — a weak model that asks serially burns the DM's turns.
- **"Connects to the party" is not an answer.** State the mechanism: name the PC, the
  specific thread (a debt, a grudge, a family tie), and the entity or faction pressuring
  it — never "ties into the group's arc."
- **State it in the output.** The connecting PC and the specific pull go in the page
  body (not just the DM's head), so a later session can grep for it.
- If genuinely nothing connects — a pure scenery element with no PC pull — that is
  still a DM call, not a default. Ask.

### 3. Toy fields

Entity pages carry "toy" frontmatter the DM can play in five seconds, kept in sync
with a body table. The four fields a toy carries, and what each is for, are Brennan
Lee Mulligan's Toy Method (`vault/refs/blm-toy-method.md`) — goal, method, problem,
and the performance cues that make the entity playable on sight. Each prep skill
decides which of them its own type requires (an NPC's `goals` differ from a
faction's); these three rules bind how every field is written, regardless of type:

- **Goals are vectors, not states.** Write what the entity moves toward, not a trait
  it has. Bad: `is ambitious`. Good: `accumulate enough to retire before the audit`.
  A vector keeps advancing whether or not the party ever meets this entity.
- **Methods are table-doable behaviors, not personality analysis.** Write something
  the DM can voice or enact in a scene. Bad: `manipulative`. Good: `offers a favor
  before naming the ask; never states a threat directly`.
- **Problems are situations, not feelings about them.** Bad: `insecure about status`.
  Good: `owes a creditor three favors with no clean way to repay them`.

These three fields are the entity's individual toy mechanics. The properties that make
the *whole entity* playable as a toy (clarity, agency, reactivity, portability) are
`audits.md` § Sandbox agency audit and `vault/refs/blm-toy-method.md` —
read those for the entity-level check, this section for the field-level one.

### 4. Three-Clue Rule

For any conclusion the players must *reach* — a culprit, a hidden door, a betrayal —
seed at least three independent clues pointing to it, placed across different
scenes/sources, so no single failed check or skipped room dead-ends the thread. Don't
gate a revelation behind one roll.

Full structural checklist (naming the conclusion, per-clue location + discovery
mechanic, the anti-railroading framing) lives in
`audits.md` § Three-Clue Rule — this is the reminder
that applies it; read that file before closing any mystery/situation/dungeon element.

### 5. Combat calibration

Before finalizing anything with combat numbers (creatures, encounters, dungeons,
items), read party stats from `vault/campaigns/shattered-sea/pcs/*.md` frontmatter and paste them. CR alone is not
calibration — check the numbers against what this party actually does at the table,
not the generic assumption for a party of that level.

`combat-profiles` (`.claude/skills/`) owns the deeper, persisted
difficulty-calibration methodology — `encounter-prep`'s own reference reads its
output as the mandatory pre-read; this rule is the floor every combat-bearing prep
skill meets even when no `combat-profiles` profile exists yet.

### 6. Prose pass

Before finalizing any prose — read-aloud text, DM notes, lore sheets, toy-field prose,
NPC handles — read it back once for voice and naming consistency before shipping it.
`[!read-aloud]` boxes are `dnd5e-scene-narration`'s craft (two-draft protocol); this
file doesn't restate that skill's rules.

### 7. Sandbox discipline

The Player Character Boundary, Independent NPC Agency, and Pressures-Not-Plots
constraints bind everything written into `vault/` at any status. They live in
`audits.md` § Sandbox agency audit — read that section, don't infer these
rules from habit. The short version, so you recognize a violation while
drafting: never write what a PC decides, feels, thinks, or wants; NPC/faction
goals predate the party and advance independently; frame consequences as
pressures and possibilities, not `if players do X then Y` chains more than one
step deep.

### 8. No visibility-split headings

`publish:`/`status:` frontmatter is the page-level visibility gate — no
template adds a second, per-section Player-Known/DM-Only split on top of it.
Organize by content function (what a section is about), never by who's
allowed to know it. A genuinely hidden fact (a secret identity, an
unrevealed twist) is written inline, where its content actually lives —
in prose, or via the entity's own per-field mechanism (a faction [[front|Front]]'s
`Per-PC awareness` field, a quest's Three-Clue-gated reveal) — never
partitioned into its own heading. Enforced repo-wide by lint (W20/W21,
`npm run lint -- --rules`) — a page
still carrying either heading is on the old schema regardless of type.

### 9. Creative-domain rider

Inside every rail above, invent boldly. Facts, canon, structure, and
visibility are governed; *style is free*. A timid entry — "is dangerous",
"feels tense", a generic read-aloud paragraph, a minimum-risk draft that
commits to nothing — is a contract violation, the same as a wrong fact.
Push for the specific, table-tested detail; where the source is silent and
the choice is flavour rather than fact, pick the vivid option and write it
down.

The rider governs authoring only. A skill whose job is *fidelity* —
`find-guidelines`, `llm-wiki-ingest`, `content-fixer` — is exempt by its own
contract: inventing a detail it was not given is a violation there, not
licence.

## The lazy prep toolkit and eight-step checklist

Source: the Sly Flourish Lazy DM material. This section is the low-prep,
improvisational-running counterpart to the session-shape and beat-composition
material above — read it for table tools and the 8-step session-prep
checklist, not for beat structure.

### Toolkit

Dice, pencils, and dry-erase markers; a GM's notebook; a campaign worksheet;
a curated random name list (`vault/refs/table-npc-names.md`); 3x5 index
cards; numbered initiative cards; a GM screen or cheat sheet; a dry-erase
flip mat; published books and adventures; miniatures, maps, and terrain as
needed.

### Building a lazy campaign

- Develop a spiral campaign with the characters at the center.
- Build a campaign draw focusing on a single major goal.
- State the six truths of your campaign.
- Define three fronts incorporating goals and grim portents.
- Run a session zero to help build the characters and tie them together.

See `vault/refs/ideas/spiral-campaign-development.md` for the spiral method,
campaign pitch table, six truths, and campaign fronts table, and
`vault/refs/session-zero-checklist.md` for the full session zero walkthrough.

### The eight-step session-prep checklist

For a typical game session:

1. **Review the characters.** Spend a few minutes before doing anything
   else. What are their names? What do they want? What plays into their
   backgrounds? What do the players of these characters enjoy at the table?
   You might not write anything down during this step, but reviewing the
   characters wires them into your mind and ensures the rest of your
   preparation fits around them.
2. **Create a strong start.** How a game starts is likely the most
   important piece of preparation you can do — see
   `.claude/skills/writing-hook-beats/references/hook-beats.md` § Strong
   starts (session openers) for the operational form and the forty example
   openers.
3. **Outline potential scenes.** A short list of potential scenes that
   might unfold, mostly so you feel as though you have a handle on the
   game before you start — throw it away when the game goes a different
   direction, as it often does. Usually a few words per scene is enough;
   expect one or two scenes per hour of play. Skip this step entirely when
   you don't think you need it.
4. **Define secrets and clues.** Second only in importance to the strong
   start — see § Secrets and clues, above, for the method and prompt
   tables.
5. **Develop fantastic locations.** See § Fantastic locations, above, for
   the six-item checklist.
6. **Outline important NPCs.** The NPCs most critical to the adventure,
   focusing on a name and a connection to the adventure, then wrapping the
   NPC in a character archetype from popular fiction. Many other NPCs —
   maybe even most — can be improvised right at the table.
7. **Choose relevant monsters.** What monsters are the characters most
   likely to face, and what makes sense for this location and situation?
   "Monster" is used loosely, to include enemy NPCs as well as truly
   monstrous foes. Most of the time, list a number of monsters and
   improvise encounters based on what's happening; for boss battles, do
   more work — see `vault/refs/lazy-combat-encounter-building.md` for the
   deadliness formula and benchmark.
8. **Select magic item rewards.** See § Rewards, above, for the
   gold-per-level pacing convention and the beyond-coin options.

These steps work identically whether play happens online or at the table.

**The 5-minute reduced checklist**, when time is very short: create a
strong start, define secrets and clues, develop fantastic locations.

### Running your game

- Relax.
- Focus on your strong start.
- Listen to the players, and build off of the ideas they bring you.
- Trust your preparation to help you run a creative, flexible game.
- Ask the players to summarize the events of the previous game session.
- Draw players into the story by asking them to describe killing blows,
  define monster characteristics, and describe interesting events during
  travel.
- Imagine the world as a living place when building scenes and situations.
- Let the world and the NPCs react to the characters' actions.
- Use a mixture of combat styles, including theater of the mind, gridded
  maps, and abstract maps.
- Maintain a good pace by staying close to the action.
- Cycle between action and relaxation, and alternate upward and downward
  emotional beats.
- Use specific hopeful or fearful beats to send the action in a specific
  direction.

### Thinking about your game

- Prime your GM's brain with great books, movies, and TV shows.
- Remind yourself of the player characters' names and backgrounds.
- Ask what the villains and NPCs are doing right now.

### Embrace the GM's truths

- Players don't care as much as you think.
- Players want to see their characters do awesome things.
- The GM is not the enemy of the characters.
- Be a fan of the characters.

### Lazy RPG tricks

- Award levels at key points in the story.
- Improvise ability and skill checks.
- Delegate certain tasks to the players.
- Use static monster damage.
