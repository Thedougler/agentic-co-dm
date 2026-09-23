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
- **Done:** Every assigned narration slot is filled and passes the final check
  at the bottom of this file, and the return carries the art note and, for a
  situated block, the handle note.
- **Capability Handoff:** Return the filled prose to the parent beat, owner
  page, or run-guide pass. A missing owner page or missing fact the prose
  depends on returns as a named gap (owner, path, what is missing).

## Steps

### 1. Pick the mode and surface

**Situated.** A moment in play, where the party is somewhere and something is
happening. Session-beat slots, scene openings, NPC meetings, combat, recaps,
transitions. Second person ("you"), present tense. Read
[references/scenes.md](references/scenes.md) and use the recipe for your
surface.

**Portrait.** A wiki owner page's `[!narration]` with no party and no current
scene. A person, creature, place, item, hazard, faction, vehicle, or technique
described as it always is. Third person, present tense. Read
[references/portraits.md](references/portraits.md) and use the recipe for your
subject.

No party, encounter, or table state supplied for an owner page → portrait.

### 2. Gather the facts

1. Read the parent: the beat page (entry state, Situation, Cast, Space) or the
   owner page. Then read every owner page the scene touches: the place and
   region it stands in, and every person, creature, item, and hazard present
   or linked. Owner pages hold what the beat leaves out.
2. Read the spoken blocks that come before this one (the previous beat's
   closing, this beat's Initial Narration) and any earlier narration of this
   place or person. Facts already spoken stay true; on a return, the anchor
   they were given comes back, described fresh and changed by whatever has
   happened since.
3. Write a private fact list: what the characters can **see, hear, smell, or
   touch right now**, plus what they already know. Note each fact as bare
   keywords with its source (`ferryman: map, lantern, charcoal circle`), never
   a phrase from a page: keywords carry the fact and leave the wording behind.
   This list is yours; the players never see it.
4. When the target already has narration, or the parent or owner page carries
   its own, mine it like any other source: move its facts onto your list as
   fragments, then close it. Its phrasing is what you are replacing, and a
   draft written with the old block open comes out as the old block.
5. When a fact the scene needs is missing (what the room looks like, what the
   NPC wears), get it from the owner skill for that page, or return the gap.
   Leave it out of the prose rather than guessing.
6. List every thing the players can act on in this scene. These are the
   **handles**. The beat page is where the list starts, never where it ends;
   beats routinely miss things. Pull from every source:
   - the beat's Situation, Cast, Space, Zones, and Stage;
   - the place and region pages: landmarks, routes, water, flora, fauna,
     hazards, and every tell in their weave;
   - each person, creature, and item page: what they carry, wear, and do,
     and their visible tells;
   - the art: everything drawn into this scene (the pot on the coals, the
     baskets, the fallen branch);
   - the previous beat's end state: who is where, what broke, what was left;
   - hidden things, as the trace a careful look would catch
     ([references/boundary.md](references/boundary.md) § Hidden things);
   - the place's history and working life, told by what remains (tracks,
     patched walls, scorch marks, leftovers, something out of place).

   Every handle comes from one of those sources. A thing no source supports is
   a gap you return, not something you invent.

Done when the parent, every owner page, and every earlier spoken block are
read, their facts are on your list with sources, and the handle list draws on
every source above.

### 3. See the art

Whenever the block shows how a person, creature, place, item, vehicle, or
scene looks, read [references/vision.md](references/vision.md) and run it:
**search** for related images, not only the ones the pages embed, then open
each one and analyze the **pixels** into your fact list. Art is often the only
source for color, marks, layout, and light, and it is where the anchor usually
hides. Skip only blocks that show no look (a line of dialogue from someone
already described, a past-tense recap).

Done when every subject in the block has a search note: the images you opened,
with the facts each added, or "none found" with what you searched.

### 4. Keep only what they perceive

Cross off anything the characters cannot perceive or know: secrets, hidden
causes, mechanics, DCs, the future, and anything painted into the art that
the characters cannot see from where they stand. When the scene involves a
handled object, a creature with special abilities, a hidden threat, or an
uncertain fact, read [references/boundary.md](references/boundary.md) first.

Done when every fact left on the list has a source and a way the characters
perceive it.

### 5. Choose the anchor and layer the handles

Pick the **anchor**: the one feature the players will still remember next
session, such as the jade mask at chest height, the tavern built around a
wrecked ship's mast, the log that turns out to be a boat. Everything else in
the block is arranged around it, and the place or person keeps it on every
return. Check the art first: the thing your eye went to in the picture is
often the anchor. When nothing striking survives, choose the most unusual
true fact.

Then sort the handles into **layers**, the way a DM discloses a room:

1. **Entry.** Small: what the first decision needs, in this priority:
   immediate danger, what the decision turns on, exits and routes, the
   creatures and people who matter, the features most likely to be grabbed
   first, the anchor, one useful sense. Texture and decoration come
   after; lore comes only when it bears on the decision.
2. **Attention.** What a closer look shows: the zone cells, the creature
   slot, the detail that rewards a question.
3. **Interaction.** What handling, opening, or testing reveals: the outcome
   cells, an object's inside or weight ([boundary.md](references/boundary.md)
   § object states).

Across a beat's narration slots, every handle gets its line in the layer
where it belongs, so nothing important hides by omission. Attention and
interaction handles stay out of the opening; their own slots carry them.
When the entry
layer will not fit the opening's length without sentences past one breath,
it is too big: move handles down to attention. Length never grows by
cramming a sentence.

Done when the anchor fits in one short phrase and every handle has a layer.

### 6. Draft

Set the fact list aside and **stand in it**: picture one of the characters
arriving, and say what reaches them in the order it would. Start with the
**schema**: one broad sentence that says what kind of place or situation this
is, in words that let the listener supply the ordinary (an old dockside
tavern packed with sailors, a flooded quarry at dusk). When the recipe leads
with danger, the danger is the schema. Then the anchor, one sense that does
a second job, the entry-layer handles, and the pressure that ends the block
(the spine below). Write in flowing, connected sentences using the recipe for
your surface and the craft rules below, with no source narration in view. Go
back to the list only to check accuracy and to tick off every entry handle.
Drafting down the list produces an **inventory**: every fact true, nothing
felt.

Read [references/examples.md](references/examples.md) for the matching example
and match its **quality and shape**, never its words.

Done when the whole block exists and every entry-layer handle is in it.

### 7. Revise, check, and return

A first draft always keeps traces of its sources and its fact list. Revise it
in three passes, each a separate read of the whole block:

1. **Echo pass.** Lay the draft beside the parent page, the old block, and
   every owner page you read. Any phrase of the draft you could find in them
   (quoted speech aside) is an **echo**; rewrite that phrase from the picture
   in your head, with a detail the old wording lacked: "the planks creak
   under its weight" might become "the jetty dips a hand's width each time
   it shifts". Run this
   pass even when the draft feels clean. An echo never looks wrong from
   inside the draft, and it hides best when the source reads well: a good old
   block is a fact source, never a draft. Carried-over **paint-chip** colors and page labels go in the
   same pass (craft rules: Spoken grammar, Everyday words).
2. **Ear pass.** Say each sentence aloud. Split any you cannot say in one
   breath. Regroup any sentence that hands the listener more new, separate
   details than they can hold at once. Turn every **grid** distance into
   body-scale words and every **legend** into routes hung on landmarks
   (Speakable distance). Merge one-sentence paragraphs (Flow).
3. **Hands-off pass.** Find every "you". Keep it where the world acts on the
   characters (spray on your faces, cold through your boots), where it places
   them, or where it gives what their senses or training plainly take in.
   Rewrite it where it decides for them: an action, a word, a feeling, a
   belief, an intention, or a **conclusion** the players should draw
   themselves ("you realize someone moved the piles"). Show the evidence
   instead (hard line 1).

Then run the final check at the bottom of this file, fix every item that
fails, and run it again. Return the block with, outside the narration:

- the art note (vision.md § Report);
- for a situated block, the handle note: each attention- or interaction-layer
  handle with the slot it belongs in (`lantern hooks under the eaves → Zones: Porch`), or
  "all handles in the block".

Done when a fresh read of each pass changes nothing and every final check
answer is yes.

## The spine of a scene

Every situated scene opening is built from these parts. They are an order of
**attention**, not a paragraph template: fold them together, and when danger
is immediate, lead with it.

1. **Frame.** The schema: what kind of place this is and how big, at body
   scale (a ceiling a tall person could touch, a courtyard a short sprint
   across). Ground, light, air.
2. **Anchor.** The one memorable feature (step 5).
3. **Sense.** One nonvisual sense, with its source, doing a second job
   (below).
4. **Handles.** The entry layer, placed relative to each other and to the
   party: a door hanging half-open, a rope bridge with a plank missing, a
   guard whose hands shake on the spear. Give each one the concrete property
   that invites action, and group what goes together (crates stacked into
   waist-high lanes) rather than listing it.
5. **Motion.** Something is already happening: laundry snapping overhead, a
   guard dragging a sack, smoke drifting. A threat in motion beats a threat
   standing still.
6. **Live edge.** End on the pressure that demands a response: the arrival,
   the demand, the windup, the thing that just changed. The last image is the
   one still ringing when the DM stops talking. The DM asks "What do you do?";
   the block ends just before it.

## Craft rules

- **You are there.** Second person, present tense, from where the party
  stands. "You are halfway across the ford when the far bank starts to move."
- **Compress.** Choose words that imply many others: "a storm-battered
  fishing village" gives the listener the nets, the boats, and the gulls
  without a list. Name what they could not guess; let them supply the
  ordinary.
- **A few new details at a time.** A listener holds only a few new, separate
  things per breath. More than that must form one group ("crates
  stacked into lanes, a crane above them, an iron stair to the office"), or
  wait for a later sentence or a lower layer. A group is several things of
  one kind; the features of one body (skin, ears, hair, cloak, boots) are
  separate details, never a group.
- **One sense, two jobs.** Sight carries structure; add one nonvisual sense
  that also tells the players something: warm air deeper in the tunnel
  (something ahead), a smell that names the place, a sound that shows
  movement. Touch and temperature land on the characters' bodies (spray on
  their faces, mud sucking at their boots, heat off the forge on their skin),
  and that is what turns a scene from seen into felt. One is enough; a tour
  of all five senses is a checklist.
- **Evidence, not conclusions.** Show what the characters can see and let
  the players reason: "small muddy footprints cross the dust toward the
  stairs", not "goblins passed through". Weather shows by what it does
  (rainwater ankle-deep in the gutter, horses steaming), magic by its effect
  on the world (frost racing out across the floorboards), a place's history
  and working life by what it left (newer walls on older footings, a locked
  grate over the only fountain). In suspense, show the consequence before the
  cause, and never hide what the characters would plainly see.
- **Show size by what it does.** A number on a body is a spec; a body moving
  things is a picture. "It rolls, and the wave off its back slaps the
  pilings" shows a huge eel better than "a thirty-foot eel". When
  magnitude matters, compare it to something familiar (two wagon lengths, a
  three-story house). Unusual size is often why the creature matters: show
  it, never drop it.
- **People and creatures in a few strokes.** A person gets their role or
  first read, one distinctive feature, and one behavior. The feature is the
  one a player would use to describe them to a friend next week ("the old man
  with fishhooks braided into his beard"); the rest waits for later scenes; a creature gets its
  silhouette, how it moves, its dangerous parts, and its scale, with its
  name only when the characters would recognize it. A full physical
  inventory (height, skin, eyes, hair, cloak, boots) is an inventory: the ear
  takes it in and the mind's eye sees nothing. Recipes in scenes.md.
- **Picture first, then likeness.** Name the real thing, then compare it if
  the comparison makes it easier to picture: "a log that rolls over and
  becomes a boat", "wings folding like closing knives". A likeness that needs
  interpreting is decoration. One per block is plenty.
- **Concrete nouns, strong verbs.** "Rain drums on the tin roof" beats "it is
  raining." Prefer verbs that show shape or motion (leans, spans, drips,
  buckles, lurches, sags, hisses) over is, seems, appears, moves; keep a
  plain verb when the plain verb is clearer. One specific noun beats a stack
  of adjectives: "a burned-out watchtower", not "a dark, ancient, ruined
  tower".
- **Fold details onto their owner.** "A lean old half-orc with one ear notched
  like a tally stick." Color, scars, and gear ride inside the sentence about
  the body that owns them.
- **Everyday words.** Say it the way you would at a kitchen table: river
  mouth, not embouchure. Campaign and page labels get the name a stranger
  standing there would use: the still pool, the camp, the clearing.
- **Speakable distance.** Place things by relation: directly ahead, behind
  you, across the courtyard, between you and the stairs, above the doorway.
  Distance in body terms: within reach, a few steps, across the room, a
  bowshot. Foot counts are the **grid**, and the grid stays in the DM's
  tables; give a number only when a player must act on it this instant (the
  gap they are about to jump). Each route leaves from something the party can
  see and leads toward something they want: "past the well, an alley climbs toward
  the bell tower", "behind the stables, a path drops to the ford".
  A tour of the compass, one direction after another, is a **legend**; the
  players cannot picture it.
- **Spoken grammar.** Each sentence has one clear subject doing a strong
  verb, and a DM can say it in one breath. Join clauses with "and", "as",
  "while", "when", or a period; semicolons and colons read on the page, not
  aloud. One well-chosen modifier on a noun usually beats several. A color is
  one plain word or a comparison ("grey", "black as wet bark", "the color of
  old honey"). Two colors hyphenated together are a **paint-chip** (the kind
  of name printed under a swatch); translate it into one color or a
  comparison, even when the source page uses one. End sentences on their strongest word, not on a
  "with…" tail hanging more details.
- **Flow and tempo.** A scene opening is one paragraph, two when the scene is
  loaded, and each paragraph moves the eye once. Match the sentences to the
  moment: longer, connected sentences for calm and wonder; controlled
  sentences that hold something back for suspense ("Something is walking
  above you. Slowly."); short full sentences for action ("The mast snaps.
  Rigging whips across the deck.").
- **Every sentence earns its place.** It adds clarity, atmosphere, a handle,
  continuity, or tension. Say each fact once. A sentence you could remove
  without losing any of those goes.
- **Read the scene through the characters.** When the beat names who is
  present, let one detail land where a character's background would catch
  it: the sailor hears the hull working, the hunter reads the tracks. State
  it as what shows.
- **People sound like people.** An NPC who speaks gets a want, a physical cue,
  and one line that asks, offers, presses, or threatens, then stops so the
  players can answer.

## Length

Length follows the job, never a count. A scene opening is as short as its
entry layer allows and stops well before it becomes a monologue; the rest of
the scene lives in its other slots. Go shorter in danger, pursuit, and fast
cuts; give a little more room to a first arrival at an important place, a
major reveal, awe, horror, or a climax.

| Surface | Size |
|---|---|
| Scene opening (Initial Narration, Open on, Opening, Open on Action, Opening image) | A short paragraph: schema, anchor, entry handles, pressure |
| Closing image (Resolution) | A short paragraph that lets the change land |
| Creature entering a scene | A few sentences, ending before contact |
| NPC first look | A few strokes, plus a line of speech if they talk |
| Zone or tick cell (`==_italic_==`) | A line or two |
| Outcome cell (state change) | A line or two; a turn in the fight earns a little more |
| How the Scene Resolves / Exit | A few sentences |
| Wiki portrait | One full paragraph covering the whole subject |
| Place portrait with a place-design packet | As long as every tell in the packet needs, folded onto owner nouns first |
| Recap | A short story paragraph, then tonight's opening |

A scene opening with no anchor, handle, or pressure is a stub; expand it from
your fact list. One that needs its sentences stretched past a breath to fit is
carrying too much entry; move handles down a layer.

## Hard lines

These hold in every block.

1. **The players own their characters.** The prose never decides for a PC:
   no action, speech, choice, intention, belief, emotion, or bodily reaction
   (sweat, racing heart, turning stomach) the player has not declared, and no
   conclusion the players should draw themselves. Put the cause in the world
   instead: "the scream makes the lantern glass tremble", not "terror fills
   you".
2. **Only what they can perceive.** No secrets, hidden causes, DCs, hit
   points, exact ranges, spell or ability names the characters have not
   learned, or forecasts of what will happen ("if you touch it, it will…").
   Show the sign; the table finds out the rest by playing.
3. **Stop before contact.** A first look at a threat ends on the windup: the
   bowstring drawn, the beam groaning, the wings folding for the dive. No hit
   lands, no grab completes, no trap springs until a player acts.
4. **Canon only.** Every name has an owner page. Every fact comes from the
   parent, the owner pages, the images, or the user. Source silence is not
   evidence: leave out what the sources do not say, including claims that
   something is absent.
5. **No echoes.** Take facts from the parent, the old block, the art, and
   your own art note; take none of their phrasing. Repeating narration
   verbatim does nothing for the players: they have heard it or will read it
   on the page, and hearing it again makes it no clearer. Describing the same
   fact fresh does work, because each new description adds a specific detail
   that sharpens their picture. Quoted speech an NPC already said stays word
   for word. Details that only record a passing
   moment (a gesture, a glance, a grin, a pose) are not who someone is; the
   story decides what they do now. Examples in this skill teach shape, never
   wording.
6. **Clean page.** No em dashes (`—`) in player prose; use commas, periods, or
   parentheses. Craft labels from this skill (live edge, windup, anchor,
   schema, layer, cold portrait) stay out of the narration.

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
| a body as a list of attributes | one feature and one behavior |
| isolated verbless fragments ("Chin drips. Eyes red.") | a sentence where the body does something |
| an "if they…" branch in the spoken text | stop at the live edge; branches live in the DM tables |

## Callouts and ingest

The only callout on a session card is `[!narration]`, and callouts never go
inside table cells; which slots a beat carries is in
[references/scenes.md](references/scenes.md) § Beat slots. On wiki owner
pages, mechanics stay in `[!mechanic]` and secrets in collapsed `[!secret]-`,
outside the narration.

When `wiki-ingest` loads this skill, named ingest is DM approval for those
sources (`docs/agents/work.md`): polish existing stubs into narration that
passes the final check, keeping their facts and meaning.

## Final check

Run after the three revision passes (step 7). Fail and fix if any answer is no.

- [ ] (Situated) Hearing it once, could the players answer: Where are we? What
      stands out? Where can we go? What can we use or reach? What matters
      right now? What has changed? What would my character notice?
- [ ] (Portrait) Does the paragraph cover the whole subject from its recipe,
      with no party, scene, or event, so a player could sketch it?
- [ ] Does the first sentence set the schema (or the danger), and is there one
      anchor the players will remember?
- [ ] Is every entry-layer handle in the block, grouped so no breath carries
      more new things than a listener can hold, and is every other handle in the
      handle note?
- [ ] Was every related image searched for and opened, and does the block
      carry the few pixel details that set each subject apart?
- [ ] (Situated) Does one nonvisual sense do a second job, and does something
      land on the characters' bodies?
- [ ] Does each person and creature come across in a few strokes (a first
      read, one feature, one behavior), rather than a list of features, even
      a list spread across several sentences?
- [ ] Is the block the size its job needs (Length), with no sentence
      stretched past a breath to fit?
- [ ] Could any sentence go without losing clarity, atmosphere, a handle,
      continuity, or tension? Cut it.
- [ ] Echo: held beside the parent page, the old block, and each owner page,
      does no phrase of the block appear in them (quoted speech aside), and
      is every color one plain word or a comparison, even where the source
      hyphenates two?
- [ ] Ear: can every sentence be said in one breath, with each route leaving
      from a landmark and no grid distance?
- [ ] Hands-off: does every "you" place the characters or let the world act
      on them, with no action, feeling, or conclusion decided for them?
- [ ] Hard lines, one by one:
  1. Every PC action, word, choice, feeling, and conclusion is left to its
     player?
  2. Every fact is one the characters can perceive now, with no DC, secret,
     unlearned ability name, or forecast?
  3. The last sentence stops on the windup: no hit lands, no grab or pull
     completes, no trap springs? The block ends before "What do you do?",
     which the DM asks.
  4. Every name has an owner page and every fact a source?
  5. No passing gesture or pose from the art or the page is carried over?
  6. Searching the block for `—` finds nothing, and no craft label appears?
- [ ] Nothing from the slop table survives?
- [ ] Reading it aloud, does it sound like a confident DM talking?
