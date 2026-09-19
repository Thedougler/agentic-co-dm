---
name: plan-session
description: >-
  Collaborative session brainstorming with the DM. User-invoked only — use when
  the DM says "/plan-session" or "let's plan the next session". Reads the
  previous session and wiki context, then grills the DM about their ideas in a
  friendly creative conversation, shaping intent into a beat chart concept ready
  for session-beats to file.
---

# Plan Session

A collaborative brainstorming conversation that turns the DM's raw ideas for
the next session into a beat chart concept. This is the creative phase — talk
first, file later.

## What this skill does

1. Gathers context (previous session, active threads, wiki state)
2. Grills the DM about what they want the session to feel like
3. Shapes their answers into beat chart structure (Hook → D/C pairs → Climax → Resolution)
4. Produces a session concept the DM can hand off to `session-beats` for formal planning

This skill writes nothing to the wiki. It is pure conversation.

## Gather context

Before asking the DM anything, pull campaign state so your questions are
grounded in what actually happened, not generic prompts.

1. **Resolve config** — follow the Config Resolution Protocol in
   `llm-wiki/SKILL.md` to get `OBSIDIAN_VAULT_PATH`.
2. **Read `hot.md`** — recent activity snapshot; orients you fast.
3. **Find the previous session.** Look in
   `wiki/journal/sessions/<campaign-slug>/` for the highest-numbered session
   directory. Read the session plan (`Session-<N>-00-*.md`) and the recap
   (`Session-<N>-Recap.md`) if one exists. These tell you where play left off,
   what threads are live, and what the players said they want next.
4. **Query active threads.** Use `wiki-query` to pull:
   - Active PC goals and unresolved backstory threads
   - Faction clocks and NPC agendas in motion
   - Dangling clues, promises, or consequences from recent sessions
   - Any prep the DM already started (notes)

Summarize what you found in 5–10 lines before starting the grill. The DM
should see that you know where the campaign stands.

## Grill the DM — creative mode

Use the `grilling` skill's design-tree method, but tuned for creative
collaboration rather than adversarial stress-testing. The tone is two friends
at a whiteboard, not a deposition.

**Round format** — same as grilling (numbered questions, each with your
recommended answer, wait for the DM's replies before the next round), but:

- Lead with **what excites you** about their idea, then probe. Creative energy
  first, refinement second.
- Your recommended answers should be **concrete and evocative** — suggest
  specific NPCs, locations, and situations from the wiki, not abstract
  categories. "The Thornwall ambush from Session 8 could echo here" beats
  "consider a callback to earlier events."
- When the DM's idea is vague, offer two or three **specific** options pulled
  from campaign context rather than asking them to be more specific. Give them
  something to react to.
- When the DM's idea is already sharp, say so and move the frontier forward
  instead of interrogating what's already clear.

### The frontier

Work the design tree in rounds. The frontier roughly follows this progression,
but skip or reorder based on what the DM already told you:

**Round 1 — Intent and energy.**
What do you want this session to *feel* like? What's the promise to the
players? What threads are you most excited to advance? Is there a moment
you've been waiting to deliver?

**Round 2 — Hook and opening pressure.**
How does the session start? What's in the players' faces when we open? Does
this connect to last session's ending or a PC goal? Action start or cerebral
start — and what does that polarity choice mean for the first middle beat?

**Round 3 — Middle beats and threads.**
Which threads get Development beats (new information, new direction)? Which
get Cliffhanger beats (contest, cost, test)? What alternation pattern feels
right? Where does the party gain capability and where is it tested?

**Round 4 — Climax and harvest.**
What's the highest-stakes confrontation the middle is building toward? Which
threads converge here? What did Developments reveal and Cliffhangers test that
the Climax now harvests? Can the party arrive equipped by what the middle
taught them?

**Round 5 — Resolution and forward threads.**
What's the tag line — the tiny afterscene that echoes the Climax? What's
changed, what did it cost, and what can the players now pursue? What threads
seed the next session?

The frontier is empty when every beat slot has a situation concept the DM is
excited about, or when the DM says they're ready.

### Staying grounded

Throughout the grill:

- **Cite wiki pages.** When you suggest an NPC, place, faction, or thread,
  name the `[[page]]`. If the wiki is silent, say so — the DM decides whether
  to invent or defer.
- **Flag pacing.** If the DM's plan stacks two action beats or two
  introspection beats consecutively, name the alternation concern and suggest a
  reorder. Explain the energy reason: numbing vs. stalling.
- **Flag unearned climaxes.** If the planned Climax introduces elements the
  middle didn't plant, name what's missing and suggest where to seed it.
- **Flag scale mismatch.** If the Resolution is bigger than the Climax, name
  the proportion concern.
- **Respect player agency.** Prepare situations, not outcomes. If the DM plans
  a required sequence, help reshape it into triggered situations with
  alternatives.

## Produce the session concept

When the grill is done, synthesize a **session concept** — a compact summary
the DM can hand to `session-beats` or use as their own planning notes:

```
## Session <N+1> Concept: <working title>

**Promise:** One sentence — the experience this session delivers.
**Tone:** The emotional register.
**Threads advanced:** Which live threads this session moves.

### Beat sketch

| # | Type | Situation concept | Threads | ~Min |
|---|------|-------------------|---------|------|
| 1 | Hook | ... | ... | 30 |
| 2 | Dev/Cliff | ... | ... | 30 |
| ... | ... | ... | ... | ... |

**Open questions:** What the DM still needs to decide.
**Wiki gaps:** Pages that need to exist before formal planning.
**Handoff:** "When ready, run session-beats to build the formal plan."
```

The concept is conversation output — chat text, not a wiki page. The DM takes
it into `session-beats` when they're ready to file.

## Boundaries

- This skill is **conversation only**. No wiki writes, no
  filed plans.
- `session-beats` owns formal Beat Chart assembly and filing.
- `campaign-planning` owns arc-level and season-level planning.
- Typed beat skills (`hook-beats`, `development-beats`, etc.) own individual
  beat filling.
- This skill owns the creative brainstorming phase that feeds all of those.
