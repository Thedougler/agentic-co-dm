# Surface recipes

How to write each DM-facing surface. Find your surface, follow its recipe,
then run the final check in `SKILL.md`. The matching weak → strong pair is in
[examples.md](examples.md).

## Contents

- Session-beat pages: header lines; Situation, Cast, Space; rulings and checks;
  pressure and outcome tables; carry forward
- Session plan
- Run-guide cockpit (pass 2)
- Owner pages: At a Glance; At the Table; facts, Drive, Secrets
- Chat to the DM: reports and proposals

## Session-beat pages

The beat's type skill decides what goes on the page; this is how it reads.

### Header lines

The bold-labeled lines under the title (Card, Thread, Trigger, Stakes, Ends
when, Memorable element, and so on).

- One or two sentences per label. Lead with the fact.
- Name the people, places, and items with wikilinks.
- **Ends when** names an observable moment: "Ends when the party reaches the
  ladder or the second beam falls."

### Situation, Cast, Space, Opposition

- One bullet per fact, each a complete sentence that starts with its subject
  or a bold label.
- Cast rows: who (wikilink), what they want now, what they do next if nobody
  interferes, what they offer or hide, what changes their mind. Write the
  hidden part plainly.
- Space: distances in feet, what blocks what, each feature with its ruling
  ("The crates give half cover").
- Opposition: compact numbers on one line (AC, HP, Speed, the attack or save
  DC the DM rolls), then the tactics as short sentences in order: opening
  move, how it adapts, when it breaks, where it goes.

### Rulings and checks

- One row or labeled line per player action worth rolling.
- Format with `obsidian-markdown`: **Ability (Skill) — `DC n`**, then
  → success and → failure, each a clause with its own subject.
- Every result says what changes in the fiction and why it matters now.
  "→ Failure: the rope slips; the climber drops back to the basin floor and
  takes `2d6` bludgeoning damage."
- Sensible actions with no real doubt get an **Automatic** line, not a roll.

### Pressure and outcome tables

- One row per case. The first column is the condition ("If the party
  surrounds Mara", "Round 3"); the other columns say what happens, in the
  world's voice.
- Each cell reads as a statement with a subject: "Mara swings onto the barge
  and poles for the far bank," not "escape → barge."
- Include the "anything else" row the template asks for: what stays true
  whatever the party does.

### Carry forward

- One line per state variable the next beat inherits, with its possible
  values: "**Ledger.** Held by the party, or taken by Mara."
- Last line: what is now true because of the party's choice.

## Session plan

- **Compass** lines are one sentence each, stated as facts about tonight.
- **Beat Map** cells are short statements, not fragments: "Mara's first
  grab for the ledger ends; the party commits to a direction."
- **Pressure** steps describe what the opposition does, in order, in the
  opposition's voice ("Mara follows the party to the docks and waits for
  the ledger's carrier to be alone").
- **PC Touchpoints** name the PC, what matters to them tonight, and the beat.
- **Floating Clues** are true facts, one sentence each.

## Run-guide cockpit (pass 2)

Run-guide pass 1 built the cockpit; pass 2 makes its DM copy readable.

- Edit Scene ends when, At a Glance, Now, Action cards, Procedure, Be ready
  for, the threat clock, and How the Scene Resolves.
- **Scene ends when** starts with the end condition; the time budget follows.
- **At a Glance** bullets: stakes, the goal or exit, the danger, and what
  pulls players in. Readable in five seconds.
- **Now** gives positions in feet and compass directions in one paragraph.
- Keep every `[!narration]` body and narration cell empty; pass 3 fills them.
- A structural gap (a missing section, wrong order) is fixed from
  `run-guide` before polishing.

## Owner pages

Owner pages are reference the DM pulls up mid-improvisation. The page's kind
decides its sections (`wiki/AGENTS.md` Layout); the `[!narration]` portrait
belongs to `theatre-of-the-mind`.

House tone for campaign owner pages: deadly, political, weird, in that order.
Attach the strange to a noun and a consequence.

### At a Glance

- Three to five bullets or two to four sentences.
- What it is, in this campaign's specifics; why it matters now; the hook a DM
  can use tonight.
- Test: a DM who reads only this section could improvise a scene with it.

### At the Table

- How to run it when the party meets it: what it does first, what it wants,
  how it reacts to common approaches, the rulings the DM will need.
- Playable consequences only.
- Bold labels index the procedures so the DM finds one in under thirty
  seconds.

### Facts, Drive, Secrets

- Each fact is a present-tense sentence about the entity that changes a DM
  response.
- Drive: what they want, what they fear, how they go about it.
- Secrets: the truth, stated plainly, and how it could come out in play.
- History only where it explains something the party can meet now.

## Chat to the DM

### Report (done-summary)

- First sentence: what was done.
- Then what changed, with paths, grouped by kind.
- Then gaps or decisions for the DM, each one line.
- No preamble, no process narration.

### Proposal

- First sentence: the recommendation.
- Then the reason in one or two sentences, and the choices if there are any.
- End with the one decision needed.
