---
name: theatre-of-the-mind
description: >-
  Write all player-facing prose for TTRPG play: read-aloud and boxed text,
  `[!narration]` blocks, scene openings, NPC first looks and dialogue, creature
  reveals, combat outcomes, recaps, handouts, visions, transitions, and wiki
  `[!narration]` portraits of creatures, places, items, hazards, factions,
  vehicles, and techniques. Use whenever text crosses the DM/player boundary,
  including run-guide pass 3 and every narration slot on a session beat. Produces
  vivid, speakable, second-person narration the table can picture and act on at
  once. Reader `players` → theatre of the mind. Does not own DM procedure,
  hidden truth, or agent instruction.
---

# Theatre of the mind

You write the words the DM says out loud. Narration is **compressed world
simulation**: the fewest spoken words that give the whole table one shared
picture of where they are, what stands out, what they can use, and what is
pressing on them, and that make the place feel physical and lived in. It
worked when the players start proposing actions without asking the DM to
explain the scene again. It sounds like a confident DM talking, not a novel
and not a list.

You are telling a **story**, not filing a **witness statement**. A witness
lists height, clothes, and what the hands were doing, in the words they were
given. A storyteller knows every fact, then chooses the few that make the
listener see and feel the scene, and says them in words made for this moment.

DM-facing text on the same page belongs to `writing-for-humans`; what a beat
contains belongs to its type skill (`docs/agents/table-ready.md` § Who owns
what). File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named narration target (a session-beat slot, a situated moment,
  or a wiki `[!narration]` portrait), its owner page or beat page, the current
  table state when there is one, and its related images, whether embedded or
  found by search.
- **Work:** Write only the player-facing prose for that target, following the
  steps below. Named people, places, and things come from existing owner pages
  (AGENTS.md **HARD: entity-before-spoken**).
- **Done:** Every assigned narration slot passes the final check, and the
  return carries the art note and, for a situated block, the handle note.
- **Capability Handoff:** Return the filled prose to the parent beat, owner
  page, or run-guide pass. A missing owner page or missing fact the prose
  depends on returns as a named gap (owner, path, what is missing).

## Steps

### 1. Pick the mode

**Situated.** A moment in play, where the party is somewhere and something is
happening: session-beat slots, scene openings, NPC meetings, combat,
transitions. Second person ("you"), present tense. Read
[references/scenes.md](references/scenes.md): its handle, layer, and spine
sections, then the recipe for your surface.

**Portrait.** A wiki owner page's `[!narration]` with no party and no current
scene: a person, creature, place, item, hazard, faction, vehicle, or technique
described as it always is. Third person, present tense. Read
[references/portraits.md](references/portraits.md) and use the recipe for your
subject.

**Recap.** A retelling of play that already happened: a session recap page,
or the recap read aloud as a session starts. Past tense, the party as "you".
Read [references/recaps.md](references/recaps.md); it replaces steps 2 to 6
with its moment list and story, and its final check replaces the situated
items below.

No party, encounter, or table state supplied for an owner page → portrait.

### 2. Gather the facts

Read the parent (the beat page or the owner page), every owner page the scene
touches (the place and region, and every person, creature, item, and hazard
present or linked), and every spoken block before this one, including earlier
narration of this place or person. Owner pages hold what the beat leaves out.

Write a private fact list of what the characters can **see, hear, smell, or
touch right now**, plus what they already know. Note each fact as bare
keywords with its source (`ferryman: map, lantern, charcoal circle`).
Keywords carry the fact and leave the wording behind, so the draft starts
fresh. Existing narration on the target or its owner page is mined the same
way and then closed: its phrasing is what you are replacing.

A fact the scene needs and no source gives (what the room looks like, what
the NPC wears) comes from the owner skill for that page, or returns as a gap.

For a situated block, also build the **handle list**: every thing the players
can act on, drawn from every source in
[scenes.md § Handles](references/scenes.md#handles). The beat page is where
that list starts, never where it ends.

Done when every source is read, every fact is on the list as keywords with a
source, and (situated) the handle list draws on every handle source.

### 3. See the art

Whenever the block shows how a person, creature, place, item, vehicle, or
scene looks, read [references/vision.md](references/vision.md) and run it:
**search** for related images, not only the ones the pages embed, then open
each one and analyze the **pixels** into your fact list. Art is often the only
source for color, marks, layout, and light, and it is where the anchor usually
hides.

Done when every subject in the block has a search note: the images opened,
with the facts each added, or "none found" with what you searched.

### 4. Keep only what they perceive

Cross off anything the characters cannot perceive or know: secrets, hidden
causes, mechanics, DCs, the future, and anything painted into the art that
the characters cannot see from where they stand. For a handled object, a
creature with special abilities, a hidden threat, or an uncertain fact, read
[references/boundary.md](references/boundary.md) first.

Done when every fact left has a source and a way the characters perceive it.

### 5. Choose the anchor

Pick the **anchor**: the one feature the players will still remember next
session (the jade mask at chest height, the tavern built around a wrecked
ship's mast, the log that turns out to be a boat). Everything in the block is
arranged around it, and the place or person keeps it on every return,
described fresh. The thing your eye went to in the art is often the anchor;
when nothing striking survives, take the most unusual true fact.

For a situated block, sort the handles into **layers**
([scenes.md § Layers](references/scenes.md#layers)): the opening carries only
the **entry** layer, and every other handle goes to the slot that holds it.

Done when the anchor fits in one short phrase and (situated) every handle has
a layer.

### 6. Draft

Set the fact list aside and **stand in it**: picture one of the characters
arriving, and say what reaches them in the order it would. Start with the
**schema**, one sentence that gives the **situation**: what is happening and
to whom, set in a kind of place the listener can fill in on their own (a
caravan stalled at a washed-out ford while its drivers shout at each other,
a dockside tavern packed wall to wall for a wedding). When danger is present,
the danger is the schema. When nobody is there, the situation is what the
place shows was just happening (a camp left mid-meal, a forge still warm, a
door kicked in from the outside). Terrain alone is a **caption**; the ground,
light, and air come in later, where the body meets them, and every sentence
after the schema serves the situation. Build the rest from your keywords and
the picture in your head, following the recipe and the craft rules. Drafting down the list
produces an **inventory**: every fact true, nothing felt.

Read [references/examples.md](references/examples.md) for the matching example
and match its **quality and shape**, never its words.

Done when the whole block exists and (situated) every entry handle is in it.

### 7. Revise and return

Run the final check at the bottom of this file as a revision: each item is a
fresh read of the whole block, and each "no" gets rewritten before the next
item. An **echo** never looks wrong from inside the draft, so the echo item is
read against the sources, never from memory. Repeat until every answer is
yes.

Return the block with, outside the narration:

- the art note (vision.md § Report);
- for a situated block, the handle note: each attention- or interaction-layer
  handle with the slot it belongs in (`lantern hooks under the eaves →
  Zones: Porch`), or "all handles in the block".

Done when a full pass of the final check changes nothing.

## Craft rules

- **You are there.** Second person, present tense, from where the party
  stands: "You are halfway across the ford when the far bank starts to move."
  When the beat names who is present, let one detail land where a
  character's background would catch it (the sailor hears the hull working),
  stated as what shows.
- **Compress.** Choose words that imply many others: "a storm-battered
  fishing village" gives the nets and the gulls without a list. A listener
  holds only a few new things per breath; more must form one group (crates in
  lanes, three doors), and the features of one body are separate things,
  never a group. A person is a first read, one feature, and one behavior; the
  feature is the one a player would use to describe them to a friend next
  week ("the old man with fishhooks braided into his beard"), and the rest of
  their clothes, gear, and coloring waits for a closer look. A creature is
  its silhouette, how it moves, the one dangerous part about to be used, and
  its scale, named only when the characters would know it. Someone the
  table already knows (a returning villain, the enemy from last session's
  fight) needs no reintroduction: their name, what they are doing now, and
  the one part about to be used. Companions the
  players already know are already in their picture: one enters the block
  only by doing something that matters now, and a line of known faces is a
  **roll call**. One specific noun beats a stack of
  adjectives ("a burned-out watchtower"). Every sentence adds clarity,
  atmosphere, a handle, continuity, or tension, or it goes.
- **Felt.** Something is already moving. One nonvisual sense does a second
  job (warm air deeper in the tunnel says something is ahead). Something lands
  on the characters' bodies (spray on their faces, mud sucking at their
  boots, heat off the forge on their skin): that is what turns a scene from
  seen into felt. The world acts; the reaction is the player's.
- **Show, don't tell.** The schema says plainly what kind of place or
  situation this is, as anyone standing there would (a charcoal burners'
  camp, a toll gate, a shrine). Everything the players should work out for themselves
  (who, why, how recently, how dangerous) comes as evidence. Give the
  evidence and let the players reach the conclusion: "small muddy footprints cross the dust toward the stairs", not
  the verdict that someone came through. Every judgment word (abandoned,
  recent, dangerous, strange, unusually, angry, afraid, important) is a
  conclusion you reached from something you saw, so say the thing you saw:
  "a bowl of stew skinned over on the table" instead of abandoned, "still
  turning after you have counted ten" instead of an unusually long spin, "he
  sets the cup down hard enough to slop it" instead of angry. A person's
  mood shows in what their body does, a thing's purpose in how it is used,
  and a page label (the name a DM's notes give a voice, a zone, or a plan)
  becomes what the characters actually meet. Something the characters
  cannot see exists only as what they sense of it (a step with no body on
  it, a chain ticking in empty air), however well you know what it is. Size shows by
  what it does ("it rolls, and the wave off its back slaps the pilings"), or
  by a familiar comparison (two wagon lengths). Weather, magic, and a place's
  history and working life show by their effects (rainwater ankle-deep in the
  gutter, frost racing across the floorboards, newer walls on older
  footings). Name the real thing first, then compare it if the comparison
  makes it easier to picture; one likeness per block is plenty.
- **Speakable.** Each sentence has one clear subject doing a strong verb and
  fits in one breath, joined with "and", "as", "while", "when", or a period.
  Colors are one plain word or a comparison ("grey", "black as wet bark");
  any hyphenated color compound is a **paint-chip**, translated even when
  the source uses one. Places and things get the name a stranger standing
  there would use (the still pool, the camp, the clearing), and a person is
  named only once the party has learned the name; until then they are what
  the characters see (a tall woman among the flowers). Distance is
  relational and body-scale (within reach, across the courtyard, between you
  and the stairs, a bowshot); foot counts are the **grid** and stay in the
  DM's tables unless a player must act on the number this instant.
  Directions are the ones a body knows (ahead, behind, to your left, uphill,
  downstream, across the pool); compass bearings belong to the map, and
  spoken they make a **legend**. Each route leaves from something the party
  can see and leads toward something they want ("past the well, an alley
  climbs toward the bell tower"). A scene opening is one paragraph (two when
  loaded) that moves the eye, with sentences matched to the tempo: longer for
  calm and wonder, held back for suspense, short and full for action.
- **People sound like people.** An NPC who speaks gets a want, a physical
  cue, and one line that asks, offers, presses, or threatens, then stops so
  the players can answer.

## Length

Length follows the job, never a count. A scene opening is as short as its
entry layer allows: short enough that the players still hold its first
sentence when the DM stops talking, well before it becomes a monologue; the rest of
the scene lives in its other slots. Go shorter in danger, pursuit, and fast
cuts; give a little more room to a first arrival at an important place, a
major reveal, awe, horror, or a climax. A block that only fits by stretching
sentences past a breath is carrying too much entry; move handles down a
layer.

| Surface | Size |
|---|---|
| Scene opening (Initial Narration, Open on, Opening, Open on Action, Opening image) | A short paragraph: schema, anchor, entry handles, pressure |
| Closing image (Resolution) | A short paragraph that lets the change land |
| Creature entering a scene | A few sentences, ending before contact |
| NPC first look | A few strokes, plus a line of speech if they talk |
| Zone, tick, or outcome cell (`==_italic_==`) | A line or two; a turn in the fight earns a little more |
| How the Scene Resolves / Exit | A few sentences |
| Wiki portrait | One full paragraph covering the whole subject |
| Place portrait with a place-design packet | As long as every tell in the packet needs, folded onto owner nouns first |
| Recap (read aloud, or the session recap page) | recaps.md |

## Hard lines

These hold in every block.

1. **The players own their characters.** The prose never decides for a PC:
   no action, speech, choice, intention, belief, emotion, or bodily reaction
   (sweat, racing heart, turning stomach) the player has not declared, and no
   conclusion the players should draw themselves. Put the cause in the world:
   "the scream makes the lantern glass tremble", not "terror fills you".
2. **Only what they can perceive.** No secrets, hidden causes, DCs, hit
   points, exact ranges, spell or ability names the characters have not
   learned, or forecasts ("if you touch it, it will…"). Show the sign; the
   table finds out the rest by playing.
3. **Stop before contact.** A first look at a threat ends on the windup: the
   bowstring drawn, the beam groaning, the wings folding for the dive. No hit
   lands, no grab completes, no trap springs until a player acts. The block
   ends before "What do you do?", which the DM asks.
4. **Canon only.** Every name has an owner page. Every fact comes from the
   parent, the owner pages, the images, or the user. Source silence is not
   evidence: leave out what the sources do not say, including claims that
   something is absent.
5. **No echoes.** Take facts from the parent, the old block, the art, and
   your own art note; take none of their phrasing. The source's nouns said
   back in the source's order are still an echo; say the fact through a new
   specific detail instead (a broken cart becomes an axle snapped clean
   through, one wheel still turning). Repeating narration
   verbatim does nothing for the players: they have heard it or will read it
   on the page, and hearing it again makes it no clearer. Describing the same
   fact fresh does work, because each new description adds a specific detail
   that sharpens their picture. Quoted speech an NPC already said stays word
   for word. A passing moment (a gesture, a glance, a grin, a pose) is not who
   someone is; the story decides what they do now. Examples in this skill
   teach shape, never wording.
6. **Clean page.** Player prose joins its clauses with commas, "and", or a
   period; em dashes (`—`), semicolons, and colons stay out of it, and speech
   follows "says" or a comma. Craft labels from this skill (anchor, schema, layer, live
   edge, windup) stay out of the narration.

## Slop: cut and replace

| Cut | Replace with |
|---|---|
| "a sense of", "you can't help but", "you feel that" | the thing in the world that causes it |
| "the air is thick with", "charged", "crackles with tension" | smoke, heat, silence, or a sound with a source |
| mysterious, ancient, ominous, eerie, strange, bustling, majestic | the evidence: "no birds call here, and every trunk is stripped of bark below shoulder height" |
| "not X, but Y", "not just X" | the fact itself |
| tapestry, testament, dance of light, the very air | the object doing the work |
| a mood sentence that explains what the scene means | the sight, sound, or smell that creates the mood |
| lore before the players know what they are looking at | the evidence now; the history when curiosity or mechanics make it matter |
| stat-block words (large monstrosity, 30-foot aura, DC 15) | its body, its behavior, what happens around it |
| a list of furniture viewed from nowhere | the frame, then what is happening here right now |
| isolated verbless fragments ("Chin drips. Eyes red.") | a sentence where the body does something |
| an "if they…" branch in the spoken text | stop at the live edge; branches live in the DM tables |

## Callouts and ingest

The only callout on a session card is `[!narration]`, and callouts never go
inside table cells; which slots a beat carries is in
[scenes.md § Beat slots](references/scenes.md#beat-slots). On wiki owner
pages, mechanics stay in `[!mechanic]` and secrets in collapsed `[!secret]-`,
outside the narration.

When `wiki-ingest` loads this skill, named ingest is DM approval for those
sources (`docs/agents/work.md`): polish existing stubs into narration that
passes the final check, keeping their facts and meaning.

## Final check

Each item is a fresh read of the whole block. Rewrite on every "no", then run
the list again.

- [ ] **Echo.** Held beside the parent page, the old block, and each owner
      page, does no phrase of the block appear in them (quoted speech aside),
      and is every color one plain word or a comparison?
- [ ] **Picture.** (Situated) Hearing it once, could the players say where
      they are, what stands out, where they can go, what they can use, what
      matters right now, and what has changed? (Portrait) Does every Build
      item the sources give and every tell appear, so a player could sketch
      and handle the whole subject, with no party, scene, or event?
- [ ] **Compress.** Does the first sentence give the situation or the
      danger (a caption fails), is there one anchor, does each person and
      creature come across as one feature and one behavior (not a list of
      features, even one spread across sentences), does every known companion
      in the block act, and could any sentence go without losing anything?
- [ ] **Show.** Is every judgment word, mood, and page label replaced by
      the thing the characters see or hear, so the players draw every
      conclusion themselves, and is every person the party has not yet
      learned the name of called what the characters see?
- [ ] **Layers.** (Situated) Is every entry handle in the block, and every
      other handle out of it and in the handle note?
- [ ] **Art.** Was every related image searched for and opened, and does the
      block carry the few pixel details that set each subject apart?
- [ ] **Felt.** (Situated) Is something already moving, does one nonvisual
      sense do a second job, and does something land on the characters'
      bodies?
- [ ] **Speakable.** Read aloud, does every sentence fit one breath, with
      every place named as a stranger would, every direction one a body
      knows (no north, south, east, or west), no grid distance, no
      semicolon, colon, or em dash (search the block for each), and one
      paragraph (two when loaded) that moves
      the eye?
- [ ] **Hands off.** Does every "you" place the characters, let the world act
      on them, or give what their senses plainly take in, with nothing
      decided for them?
- [ ] **Hard lines.** Do all six hold, one by one?
- [ ] **Size.** Is the block the size its job needs (Length), with nothing
      from the slop table left in it?
