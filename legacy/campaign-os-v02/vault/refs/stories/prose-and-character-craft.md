---
type: craft
status: canon
publish: false
aliases: []
created: "2026-07-31"
updated: "2026-08-15"
tags: [craft]
summary: "Fiction-craft reference: scene grammar, character depth and the lie/want/need arc, NPC voice and entrances, speaker-line dialogue (italic single-party, bold [!dialogue] exchanges) with its failure-mode table, description, show vs tell, POV, pacing — technique foundation for every prose-producing skill."
uid: 01f53e6f-b4de-4297-b70c-b459452fed10
---

# Prose and Character Craft

The craft reference behind every prose-producing skill in the system. When a
recap reads flat, an NPC sounds like every other NPC, a villain is a
cardboard obstacle, or a lore page drones, the diagnosis and the fix live
here.

## Scene grammar

Prose scenes alternate two units. When a scene feels shapeless, check which
unit it is and whether all three parts are present:

- **Proactive**: Goal → Conflict → Disaster. The character wants something
  concrete, something resists, and the outcome is worse than expected.
- **Reactive**: Reaction → Dilemma → Decision. The character absorbs the
  disaster, faces options that all cost something, and commits — which
  becomes the next goal.

Every scene needs a viewpoint character with a clear goal, an obstacle,
stakes if they fail, and an outcome (usually not what they wanted). A recap
section or quest scene with none of these is an inventory, not a scene.

**Stakes-and-pettiness blend** (a content mixture, not a beat sequence —
layers onto either unit above): combine a real external threat, a petty
internal conflict, stylish presentation, fast verbal escalation, and
consequences that remain real. Use it for any scene that should feel like
competent people sabotaged by their own baggage rather than pure competence
or pure farce.

## Character depth: the five layers

| Layer | Question | Example (campaign NPC) |
|---|---|---|
| Surface | What do they show? | The harbormaster: jovial, unhurried |
| Behavior | What do they do? | Waves through smugglers, logs every navy ship |
| Motive | What do they want? | Coin enough to buy back her impounded ship |
| Need | What do they actually need? | To forgive herself for the wreck that lost it |
| Ghost | What wound drives them? | Sailed into the storm on a bet; her crew paid |

The arc runs: **lie they believe → want (conscious goal) → need
(unconscious truth)**. The story confronts them with the cost of the lie
until they learn the truth — or refuse it. Villains are characters who
refuse it — for the villain-specific axes (motivation, method,
vulnerability, escalation, mirror) this general model expands into, see
[vault/refs/ideas/villains-and-themes.md](../ideas/villains-and-themes.md).

## NPC voice

Every NPC wants something — *especially* the shopkeeper. The blacksmith
wants the masterwork done before the festival; the guard wants a quiet
shift. A want makes an NPC alive before they say a word. Then differentiate
the voice by varying:

- **Sentence length and complexity** — clipped soldier, meandering scholar
- **Vocabulary** — level, specificity, trade jargon
- **Speech patterns, not accents** — a nervous merchant who speaks in
  questions ("You want the blue one? The blue is good? Yes?"); a soldier who
  never uses contractions; a noble who speaks of herself in the third
  person; a child who narrates their own actions
- **What they notice and mention** — the priest sees who didn't come to
  service
- **What they omit or avoid** — the topic they steer around is a draw
- **Metaphor domains** — the fisherman compares everything to tides and nets

NPCs hold opinions about the world and each other. When two NPCs disagree
about something the party cares about, that's a scene. Show personality
through behavior: not "she is nervous" but "she folds her napkin into
smaller and smaller squares."

## NPC entrance

How an NPC arrives decides whether the table remembers them. Six moves, in
order of play, applying to a prepped NPC and an improvised one alike.
Technique observed from Matt Mercer's introduction of Zorth, Critical Role
C2E52.

**1. Description before dialogue.** Deliver the whole physical sweep before
the NPC says a word, head to feet in that order: hair, face, the feature
that dominates, then dress, then what the feet are doing. Eight concrete
details is not too many for an NPC a session is built around. A pop-culture
or actor anchor is legitimate shorthand spoken aloud, not merely a DM crib
note. It buys the table an instant image for the price of one sentence.

**2. The draw is a constraint, revealed mid-sweep.** Give a memorable NPC one
thing their body or circumstance denies them, and drop it into the middle of
the description rather than leading with it. Announced first it reads as a
label. Arriving between the face and the clothes, it is a reveal the table
leans into.

**3. Demonstrate the draw, never assert it.** The NPC works around the
constraint on stage: wrapping a rope around a pole with one foot, snapping
with their toes. Write what they are seen doing, never the conclusion
("dextrous with his feet") for the players to be handed. A draw the table
watches beats a draw the table is informed of.

**4. Enter mid-task, then turn.** The NPC is finishing a job when first seen,
then turns to the party. An NPC standing idle has been waiting for them,
which tells the table the world starts when they walk in.

**5. The NPC speaks first, and asks.** Their opening line is a question that
hands initiative straight back. The party then has something to answer
instead of a description to react to.

Related: `.claude/skills/writing-player-prose/references/exemplary-player-facing-prose.md`
§ NPC Embodiment distills this into a Drive/Here/Body prep triad.

**6. The want arrives as usable information, and the NPC tracks the room.**
Whatever the NPC is pushing for carries the payload: world state (prices are
up because war parties are buying), mechanics (jumps thirty feet from
standing, no run-up), and a danger seed (bonds to one rider, may eat the head
of the wrong one). Then react to what a PC just said. Catch the invention,
call back a line from a minute ago, stay willing to be undignified.
Reactivity is what separates an NPC from a vending machine.

## Dialogue

**Subtext**: characters rarely say what they mean. "Fine weather for it,"
says the ferryman, meaning *I know what you're carrying.* Important
conversations run on what isn't said.

**The speaker line.** Dialogue is a line of its own, prefixed with the
speaker: narration carries the bodies and the room, the speaker line carries
only what is said.

```markdown
Oskar checks the lantern oil anyway.

*Oskar*: I'm not going back down there.
```

The form, exactly:

- `*Name*: text` at line start. The asterisks close *before* the colon —
  `*Name:*` reads as dialogue to a human and as prose to every check
  (enforced: `CampaignLiterary.SpeakerLineFormat`).
- No quotation marks. The prefix delimits the speech
  (`CampaignLiterary.SpeakerLineQuoteMarks`).
- No dialogue tag. `, he said` restates the prefix; an action worth keeping
  becomes its own narration line, where it can show something
  (`CampaignLiterary.RedundantDialogueTag`).
- Delivery cue, optional and sparse, immediately after the colon:
  `*Oskar*: *(flat)* I'm not going back down there.` The cue directs the
  voice and is never spoken.
- Non-vocal speech — telepathy, sending — keeps the prefix and italicises
  the body: `*The shape*: *You knew it while you were naming her.*`
- Consecutive lines by one speaker collapse into one speaker line.
- Inside a callout the speaker line is a beat like any other, separated by a
  lone `>` (`.claude/skills/callouts/references/read-aloud.md`). A single-line
  `[!dialogue]` box is the exception: its title carries the speaker, so its
  body takes no prefix.
- A multi-party `[!dialogue]` exchange (two or more speakers trading lines,
  no narration between them) uses **bold**, `**Name**: text`, instead of
  italic — the sole place in the vault bold means dialogue rather than a
  label prefix like `**Resolved**:`. Everywhere else, `**Name**:` stays a
  label (`CampaignLiterary.SpeakerLineFormat`,
  `.claude/skills/callouts/references/dialogue.md`).

Never "she exclaimed angrily" — if the line needs an adverb, rewrite the
line.

**Fixes for common failures**:

| Problem | Symptom | Fix |
|---|---|---|
| On-the-nose | "I am angry at your betrayal!" | Bury it in subtext and action |
| Talking heads | Pages of dialogue, no bodies | Add beats, gestures, setting |
| Info dump | NPC lectures the plot | Make the info cost something; conflict over info |
| Same voice | Every NPC sounds alike | Apply the voice levers above |
| Maid and butler | "As you know, the tunnels were sealed" | The listener knows already — let them dispute it, get it wrong, or demand it |
| Vocative name-drop | "&lt;name&gt;, we had an arrangement" | People rarely use names mid-conversation; cut it unless it lands as a weapon |
| Greeting ritual | The line opens on "Good morning" | Start already moving; cut to the first line that costs the speaker something |
| Transcribed filler | "Um, I mean, the door was open" | Real talk has it, the page reads cluttered with it — carry hesitation with a short sentence |
| Monologue | One speaker line past 60 words | Break it across beats, or let someone cut in |

Each row above has a check: `CampaignLiterary.{AsYouKnow, VocativeNameDrop,
GreetingRitual, SpeechFiller, MonologueLength, OnTheNoseEmotion}`. They fire
only on speaker lines, which is what the form above buys.

## Description

**Layer senses.** Sight and sound come free; smell and taste are the
underused memory-triggers, touch and temperature the intimacy-and-dread
channel. Two or three senses per passage, never a mechanical tick through
five.

**Meaningful detail does double duty** — atmosphere plus revelation:

> Dust furred the shrine's offering bowls. All but one.

**Purple prose fix**: cut stacked adjectives, strengthen the verb, keep the
one detail that earns its place. "The ancient, crumbling, moss-covered
tower loomed ominously" becomes "Moss had eaten the tower's name from its
cornerstone."

## Show vs tell

Show the moments that matter: not "the duke was afraid" but "the duke's
seal wobbled in the wax." But telling is a tool, not a sin — tell for
transitions ("three days up the coast road"), unimportant information,
pacing through slow stretches, and emotional summary after an intense
scene. A recap that shows everything is twice too long; one that tells
everything is a ledger.

## Point of view

Recaps and lore prose default to a consistent stance: pick one head (or a
true narrator's distance) per passage and hold it. Show only what that
viewpoint could perceive, filtered through its psychology. Head-hopping
mid-scene is the most common POV fault in recap drafts. Second person
belongs to read-aloud text only.

## Pacing problems

| Symptom | Cause | Fix |
|---|---|---|
| Drags | Too much description, no friction | Cut; add conflict or cut the scene |
| Rushed | Summary where a scene belongs | Slow down, add beats and reaction |
| Confusing | Unmarked time/place jumps | Add transitions; one tell per jump |
| Boring | Nothing at stake | Raise consequences or cut |
