---
name: npc-design
description: >-
  Design, revise, and run engaging NPCs and villains for D&D 5.5e (2024 rules).
  Use when creating incidental extras, scene NPCs, recurring allies, patrons,
  rivals, faction faces, villains, lieutenants, or social encounters. Covers
  wants, leverage, limits, portrayal, Influence/Attitude, villain plans, and
  monster-style combat packages. Do not use for pure monster design without a
  personal identity (use homebrew-monsters-5e) or for player-character builds
  (hard stop: use player-characters). Do not create, rewrite, or prescribe
  `type: pc` pages.
---

# NPC design
## Work gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). New NPCs are Work: chat first, `type: npc` page only after accept. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. `type: npc` becomes `lifecycle: canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the DM has a chat proposal they can accept or reject; after accept, the filed `type: npc` page is inspectable Work.

File durable output under `wiki/` (entities/journal as appropriate). Copy `wiki/templates/npc.md` as a scaffold. Pass on person jobs in `wiki/AGENTS.md` Layout. Add optional extra depth from `specs/003-npc-page-standard/contracts/npc-page.md` only when those facts exist.

## Hard stop: player characters

If the job is a player-created character or a `type: pc` page, stop. Use `player-characters`. Do not create, rewrite, or prescribe a PC page.


## Central principle

An NPC is a legible, interruptible source of **agency and consequence**, not a
biography. Spend prep in proportion to table importance. Every useful NPC
should make a choice, reveal a pressure, or create an actionable opportunity.
Keep the economy of attention: a name, a want, and one memorable signal often
beat a page of lore.

| Importance | Prep | At the table |
| --- | --- | --- |
| Incidental extra | Name/job, immediate want, one signal | One line, reaction, exit |
| Scene NPC | Want, leverage, limit, contradiction, 2–3 signals | Ask/offer/refuse; leave a hook |
| Recurring/significant | Card plus relationships, activity log, change trigger | Pursues goals between appearances |
| Villain/faction face | Recurring card plus front, clock, contingencies | Acts off-screen and responds to players |

## Build the person

1. **Function + identity `role`.** State what the NPC does this session (craft function: informant, gatekeeper, foil, … — see `references/npc-templates.md`). Set wiki identity `role` to exactly one of `rival`, `patron`, or `contact`. Do not default `role`. Do not put craft labels in frontmatter.
2. **Immediate want.** Write a concrete, present-tense want that can change the
   next scene: “get the ledger before dusk,” not “be respected.”
3. **Leverage + need.** Leverage is what this NPC can grant, deny, expose, or
   mobilize. Need is what they lack or fear losing. Give leverage a cost and
   need a playable way to address it.
4. **Limit.** Name the line, resource, skill, oath, fear, or time constraint
   that prevents easy solutions. A limit makes consent, refusal, and failure
   legible.
5. **Productive contradiction.** Pair two truths that generate decisions:
   “protective of the ward, indebted to its abuser.” Do not resolve it in prose;
   put it under pressure.
6. **Four portrayal signals.** Give: one **visual anchor**, one **repeatable
   behavior**, one **voice principle** (sentence length, vocabulary, habits—
   not an accent), and one **sample line** that carries rhythm, worldview, and
   current want. One reliable pattern beats an elaborate voice you cannot
   reproduce next session.
7. **Connect to characters.** Give each PC one invitation: shared value, useful
   ask, relevant history, vulnerability, or reason for distrust. Never require a
   PC to care; offer a decision with stakes.

## Social play

Use ordinary conversation first. Attitude (Friendly, Indifferent, Hostile)
is the NPC’s starting disposition, not a verdict on a character. Willing,
Unwilling, and Hesitant describe the particular request; an NPC can be friendly
but unwilling, or hostile yet willing when leverage is strong. Influence is the
structured procedure for changing a creature’s disposition or securing a
reasonable concession: establish what the NPC wants, state the approach and
stakes, then use an appropriate check only when outcome is uncertain and
meaningful. Apply advantage/disadvantage or set the DC from the fiction. A
successful check earns movement, not mind control; a failed check changes
position, costs time, spends leverage, or closes an approach. Do not roll to
withhold essential information; seed it through about three independent clues.

**Efficient introduction:** anchor the NPC in the place or current problem;
show one signal; let them make a consequential move; state what they want from
the party; leave a clear answer, refusal, or next action.

**Participants loop:** each round of conversation, let the NPC pursue a want,
let players answer with action or question, resolve only the uncertain point,
then update attitude/willingness, leverage, and cost. Repeat until agreement,
refusal, interruption, departure, or a changed objective.

## Run recurrence and villains

After each appearance, add an activity-log entry: **date/scene — action taken,
new information, changed relationship, next move**. On return, show one change
caused by play; do not reset the NPC to their first impression.

For a villain, use: **understandable desire + unacceptable method + capacity
to act + collision with the characters**. Define Goal, Why, Method, Lie,
Line, Assets, Vulnerabilities, and Connection to the party. Also record
public face, leverage, need, limit, contradiction, allies, tell, plan clock,
escalation threshold, and stop condition. Break the plan into interruptible steps with a trigger,
objective, resource, visible sign, consequence, and fallback. The villain
reacts to player choices; they do not predict the party perfectly. Put presence
before the finale through rumors, traces, agents, consequences, messages, or
brief appearances. Never grant cutscene immunity: let the players interrupt,
injure, expose, bargain with, or bypass the plan.

A betrayal must be earned, possible to notice, and not the default personality
of every trusted ally. Give competing incentives and an off-ramp. Design more
than one conclusion: defeat, compromise, escape, exposure, alliance, or
redemption only when actions satisfy stated conditions. Redemption is a future
choice with risk, not a predetermined moral reward.

## File the wiki note

Copy `wiki/templates/npc.md` as a scaffold. Pass is person jobs in `wiki/AGENTS.md` Layout: who and want, look, first minutes and posture change, named ties. Combat only if they can fight.

At a Glance is a cue table: Role, Nature, Home, Wants. Extra rows only when they change how the DM runs the NPC. End with a one-sentence **DM thesis**.

Spoken look is `[!narration]` `{Name}`. Theatre of the mind. No secrets, DCs, unearned names, or DM thesis.

Running the NPC: first move and the change that shifts posture.

Relationships: wikilink + table meaning. Omit the section only on a stub with no named ties.

Omit unused optional sections. No empty History, Combat, activity log, knobs, or extra forms.

Named-ingest stubs: identity fields + complete sentences. No optional scaffolding.

Identity defaults live on the template. `location` is `unknown` when unknown. `faction` is `none` when unknown. Omit `aliases` when unused. `role` must be supplied (`rival` \| `patron` \| `contact`).

`wiki/_raw/Hinewai.md`, `wiki/_raw/Talon Skarn.md`, `wiki/_raw/Nona Black-Jaw.md`, and `wiki/_raw/Thunk.md` illustrate density. They are not required classes and not clone targets. Landmark/skirmish/patron/contact remain useful density examples.

`specs/003-npc-page-standard/contracts/npc-page.md` is optional extra depth when facts exist.

### Extra depth when true

When the NPC is fightable, add Combat (encounter rule plus sheet or one pointer). When origin, extra form, live pressure, or a secret exists, file those facts. Thin people omit unused extra depth; they are not incomplete.

## Combat handoff

Add `# Combat` only if the NPC can enter a fight. Open with a one-sentence **encounter rule**. Provide either a runnable on-page fight sheet or exactly one pointer to a `type: creature` sheet. Do not duplicate numbers.

Landmark stages: one sheet per named condition the party can change. Hand off numbers, balance, and chassis to `homebrew-monsters-5e`.

If the NPC is not expected to fight, omit the heading.

Hand off dialogue/narration to `theatre-of-the-mind`, place context to
`place-design`, pacing to `session-beats`, and vault lookup to
`.agents/skills/qmd` plus `specs/004-qmd-search-default/contracts/retrieval-precedence.md`.

## Templates, audits, and references

Use `references/npc-templates.md` for fast cards, craft functions, activity logs, and
failure modes. Use `references/villain-front.md` for clocks, reactions,
presence, betrayal, conclusions, and a villain audit. Use
`references/social-and-combat.md` for Influence procedure, introductions,
combat packages, boss economy, confrontation objectives, and tests. Before
play, audit: Can the table tell what this NPC wants? What can players change?
What happens if they ignore them? What is the cost of cooperation? What is the
limit or contradiction? What will the NPC do next, and how can players
interrupt it?

## GM-prep and world-bible gates

Prep only what the DM cannot comfortably improvise: a want, leverage, limit,
signals, next move, and one or two modular responses. Keep active NPCs distinct
from past/inactive figures and show how play changed a recurring NPC. File durable
improvisations as typed atomic owner notes; link the nearest MOC and keep
Organizer responsible for index structure. Secrets and unearned names stay out of
`[!narration]`, and a DM should recover the actionable card in under 30 seconds.
