---
type: craft
status: canon
publish: false
aliases: []
created: "2026-08-07"
updated: "2026-08-12"
tags: [craft]
summary: "The structure, character, scene, and line craft floor for campaign prose, with word-choice and weak-to-strong construction tables, applied directly by content-fixer."
uid: f2878478-bf7a-47d8-8b87-9f48e475bea6
---

# Developmental craft — the floor every prose page clears

Structure, character, scene, and line craft for campaign prose: recaps,
lore pages, quest prose, NPC page prose, handouts, and boxed-text drafts
(final sentence craft for boxed text stays with `dnd5e-scene-narration`).
Paired with [prose-aesthetic.md](prose-aesthetic.md) (the GM's specific
voice) and [banned-patterns.md](banned-patterns.md) (the prose contract) —
this file is the general craft floor underneath both. `content-fixer`
applies it directly during its lint-to-clean pass; well-written is the
default bar, never a finding that has to be raised first.

## Structural pass (big picture)

- Does the opening land? A recap's first line makes a player want the next;
  a lore page's first line says why the page matters.
- Does the middle build, or sag? Cut any section that could go entirely.
- Does tension rise and fall, with quiet moments placed deliberately?
- Is the ending earned — does the recap land on the live thread, does the
  lore page resolve the question it opened?
- Digressions integrated, not distracting (in wiki prose: a digression that
  wants its own page becomes a wikilink instead).

## Character pass

- Each named NPC's voice distinct and maintained.
- Actions align with the character established on their wiki page; reactions
  match what that character *knows* at this point in the timeline.
- Dialogue reveals character, not just information — subtext present where
  it matters, nobody explains themselves too much.

## Scene pass

- Grounded in time and place; sensory details beyond the visual.
- Conflict or tension present in every scene-shaped unit.
- Begins late, ends early — trim entries and exits.
- Key emotional moments shown; transitions and connective tissue told.
- POV consistent — no head-hopping mid-passage.

## Line pass

Clarity floor: `.claude/skills/writing-player-prose/references/prose-quality.md`
— six rules, four faults (dying metaphors, verbal false limbs, pretentious
diction, meaningless words), and the prose inflation filters. Applies to
every sentence in every pass, not only this one.

- Sentence length varies; no three adjacent sentences share a skeleton. This
  is the generic floor — [prose-aesthetic.md](prose-aesthetic.md) sets this
  GM's specific override (long, comma-linked sentences as the default
  carrier of intensity); where the two conflict, the override governs.
- Strong verbs over weak verb + adverb; active voice predominates.
- Specific nouns over generic noun + adjective.
- Vocabulary fits the register — a player-facing recap and a DM-only note
  carry different registers (`register.md`).
- "Said" carries dialogue tags most often; action beats over adverb-heavy tags.

### Words to eliminate

| Word | Problem | Fix |
|---|---|---|
| just | Weakens | Delete |
| really | Tells, doesn't show | Show instead |
| very | Lazy intensifier | Stronger word |
| suddenly | Telling surprise | Show the reaction |
| began to / started to | Delays action | Do the action directly |
| could see / could hear | Filter word | Show what's seen or heard |
| felt | Telling emotion | Show the body's response |
| that | Often unnecessary | Read the sentence without it |

### Weak → strong constructions

| Weak | Strong |
|---|---|
| There was a hound in the courtyard | A hound paced the courtyard |
| She was running for the gate | She ran for the gate |
| The knight was tall and thin | The knight towered, thin as a pike |
| The crypt was dark | Darkness pooled between the coffins |
| He felt afraid | His hand found the hilt without asking him |
