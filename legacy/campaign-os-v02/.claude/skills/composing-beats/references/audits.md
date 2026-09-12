# Audits — agency, gravity, revision, failure patterns, validation gate

## Sandbox doctrine

Read this before designing session structure, campaign arcs, faction timelines, any
situation/quest/dungeon file, or any time content needs an anti-railroading pass. Every
prep and creative skill cites this file instead of restating it.

Core principle: narrative devices are tools for world-building, not plot control. You
place loaded guns — players decide when they fire.

**Anti-railroading check**, apply before shipping any device: does this require
a *specific* player choice to pay off? If yes, it's a railroad — restructure so
multiple player paths lead to equally valid outcomes.

### The three sandbox constraints

Bind everything written into `vault/` at any status. These are load-bearing, not stylistic:

- **Player Character Boundary.** Never write what a PC decides, feels, thinks,
  intends, or wants. Write what the environment does and what NPCs do.
  (Prose-level enforcement: `.claude/skills/writing-player-prose/references/player-agency.md`.)
- **Independent NPC Agency.** NPC and faction goals predate the party and advance on
  their own timeline. Write a vector the entity moves toward, not a static state that
  waits for the party to arrive.
- **Pressures, Not Plots.** Frame consequences as pressures and possibilities. No
  `if players do X then Y` chain more than one step deep — that's a plot, not a
  sandbox. Recorded in this repo as a Front (clock, trigger, consequence) —
  `.claude/skills/draft-content/references/faction.md` owns the mechanic that implements this
  doctrine.

### Universal Toy Properties

"Toy" is Brennan Lee Mulligan's term and its field-level definition is
`vault/refs/blm-toy-method.md`. Any prep element players can't help but interact with
satisfies all four of these entity-level properties:

1. **Clarity** — instantly understandable, zero lore dump required.
2. **Agency** — fight it, negotiate it, exploit it, ignore it, each with real
   consequences.
3. **Reactivity** — moves even when untouched; the world pushes back.
4. **Portability** — works in any town, any party, without hidden setup dependencies.

**Three Draws Rule.** Every major toy needs a moral, a personal, and an opportunistic
draw. A toy only one type of player would care about misses half the table.

This is the entity-level check (does the whole toy work). The field-level rules
(goals as vectors, methods as behaviors) are
`runtime-surface.md` § Prep-entity floor § 3 — read that file for individual
toy-field prose.

### Three-Clue Rule

Structural requirement, not a suggestion: any situation where players must reach a
hidden conclusion to engage needs three distinct, mechanically discoverable clues
before the file is complete. Two clues in the same room fails the redundancy rule —
clues must span different nodes.

Before closing any situation, dungeon, or mystery element:

- [ ] One conclusion named
- [ ] Clue 1: location/NPC + discovery mechanic
- [ ] Clue 2: different location/NPC + different mechanic
- [ ] Clue 3: third location/NPC + third mechanic
- [ ] At least two of the three reachable without combat

DM-notes format:

```text
Conclusion: [what players must understand]
Clue 1: [location/NPC], [how to find it], [what it reveals]
Clue 2: [different location/NPC], [how to find it], [what it reveals]
Clue 3: [third location/NPC], [how to find it], [what it reveals]
```

### The If-Ignored Requirement

Every situation, location draw, NPC objective, and prep beat must answer: what
happens if the party doesn't engage? This is the single highest-leverage sandbox
technique — it makes the world feel alive without forcing a specific choice.

Write a concrete, observable consequence the DM can show at the table:

```text
Good: If ignored — the commission assembles and departs; the wreck isn't
      empty when the party reaches it.
Bad:  If ignored — tensions rise. (Unshowable. Rise how? Who notices?)
```

**The tick test.** If you can't name a single visible, in-world change the DM can
narrate or the players can stumble across, the consequence isn't concrete enough yet.

### PC Gravity

Every prep element must pull on at least one PC's internal tension, not just their
backstory facts (`runtime-surface.md` § Prep-entity floor § 2 owns *naming* the PC connection; this is
*where* to place it). The doctrine underneath is Brennan Lee Mulligan's Player
Gravity (`vault/refs/blm-player-gravity.md`): a draw attached to something a
character already wants is one the table takes without being steered, which is why
gravity is what makes rails unnecessary rather than invisible.

- **Two Dials** — a PC's two core behavioral axes in tension (e.g. family loyalty vs.
  reckless ambition), not surface traits.
- **Terminal Node** — their deepest long-term desire. Asymptotic: prep approaches it,
  never resolves it outright.
- **Active Friction** — what currently blocks them. Place toys here.

**The Gravity Filter.** Does this element pull on a PC's dials or terminal node? Yes →
include it, name which PC and how. No → cut it, or find the connection before writing
more.

### Narrative devices

Tools for seeding weight, not scripting outcomes. Full device catalog — every
device, its sandbox application, and how it layers into each prep skill — is
`composition.md` § Sandbox narrative devices; that section owns the
device-by-device detail, this section owns only the anti-railroading doctrine those
devices must satisfy.

### Relationship to the Toy Method (dnd5e-scene-narration)

`dnd5e-scene-narration`'s Toy Method governs a single read-aloud paragraph: every
sensory detail in that paragraph must be a toy a player can pick up, ask about, or act
on. This doctrine governs the same "toy" idea one level up — a whole NPC, faction,
location, or situation as an interactive object in the sandbox. When a scene
narrates one of these toys, apply the Universal Toy Properties above (clarity, agency,
reactivity, portability) to decide *what the toy is*, then hand it to
`dnd5e-scene-narration` to decide *which detail of it earns a sentence*. Neither
skill restates the other's rules.

## Sandbox agency audit

Run this audit across the entire composition.

- **Route** — players can choose where and how to engage. Prepared
  transitions react to state rather than prescribe method.
- **Outcome** — every unresolved Beat preserves more than one plausible
  result unless prior play has already eliminated alternatives.
- **Information** — revelations provide facts, evidence, testimony, or
  interpretations. Players retain control over what their characters
  conclude and believe.
- **Relationships** — NPC desires and reactions may be prepared. PC
  affection, trust, loyalty, forgiveness, hatred, and agreement remain
  player decisions.
- **Conflict** — opposition pursues goals according to the world state. It
  does not gain unexplained power merely to restore the planned sequence.
- **Bypass** — a clever player solution may bypass, invalidate, combine,
  or prematurely trigger prepared material. The composition updates around
  the resulting state.
- **Failure** — failure changes the situation. It creates cost, exposure,
  lost leverage, danger, changed relationships, enemy progress, or another
  playable consequence rather than requiring the planned result to occur
  anyway.
- **Success** — success remains successful. The campaign may reveal
  further consequences, but it does not secretly nullify an earned result
  merely to preserve planned content.

## Branch collapse test

A divergence earns a **Live Branches** row on the Beat Chart only when it
passes this test. Most apparent divergences do not; the commonest right
answer is *this is one Beat*.

Take the predecessor Beat and the candidate outcomes. Ask of each: do they
lead to different represented world states — a different location, a
different NPC alive, a different faction owed — and does the difference
persist into the Beats it lands on? Then the working test, per outcome:
**which named PC's story is different afterward, and what did this
consequence cost them?** No answer for at least one outcome, and the
branch does not earn a row yet. "The difference is what they carry in with
them" is the tell of that failure: knowledge alone, with no later Beat
that reads it back, is not a difference that persists.

Three outcomes, and the first is the common one:

- **Collapse.** The Beat carries one entry on the Beat Spine and the
  variation goes in its own state as colour the DM narrates. If two
  candidate outcomes would land on the same next Beat, collapse them
  unless their different future state is represented by a different
  landing Beat. Add no Live Branches row.
- **Redesign.** The divergence is real but drawn in the wrong place —
  usually on an NPC's move rather than the party's own decision or
  outcome. Redraw the hinge at the party's decision or outcome, then
  re-run this test.
- **Branch.** Every outcome answers the working test. Add the Live
  Branches row: `**state condition** → [[Beat]]`.

An NPC offering, challenging, proposing, or laying out options is never
itself the hinge — it is content inside the preceding Beat's state. The
hinge is always the party's own decision or the outcome of their own
action.

## Gravity audit

Every prepared Beat records its **Link of Relevance**. Ask:

1. What established player investment does this touch?
2. Why is that investment active now?
3. What does ignoring this situation plausibly allow to happen?
4. Would the Beat remain interesting if the players approached it in an unexpected way?

Strong:

> **Link of Relevance:** [[Mara Vale]] swore to recover her brother alive;
> the Crown has now ordered his execution.

Weak:

> **Link of Relevance:** The party is nearby.

Physical proximity is circumstance. Gravity is investment.

## Revision workflow

When revising an existing orchestration, diagnose before adding content.
Check in this order:

1. **Canon** — does the composition still match the current vault?
2. **Gravity** — does each Beat matter to a player character?
3. **Agency** — does any transition assume a player decision or outcome?
4. **State** — can each Beat actually arise from its predecessor?
5. **Rhythm** — does the active path preserve dramatic alternation?
6. **Escalation** — does each Beat make the situation more consequential?
7. **Climax** — is the decisive Beat earned by prior play?
8. **Resolution** — does aftermath remain conditional on actual results?
9. **DRY** — is information duplicated from atomic Beat or entity pages?
10. **Runtime** — can the human DM understand the structure at a glance?

Repair the earliest failing layer first. Later problems often disappear
when the upstream state is corrected.

## Failure patterns

### Plot railroad

**Symptom:** the chart reads as a sequence of things the PCs will do.
**Repair:** convert assumptions into actor pressures, entry states, and
conditional transitions.

### Quantum beat

**Symptom:** the same encounter appears wherever the players travel
because it has already been prepared.
**Repair:** give the Beat a real location, actor, cause, and activation
condition. Let it be missed.

### Branch explosion

**Symptom:** preparation attempts to enumerate attack, negotiate, sneak,
flee, deceive, investigate, and every other imaginable method.
**Repair:** branch only on materially different resulting states.

### Decorative choice

**Symptom:** several branches exist but all secretly produce the same
mandated result.
**Repair:** make meaningful consequences differ or collapse the false
branches into one situation.

### Gravity-free hook

**Symptom:** players must become curious about something unrelated to
their established interests.
**Repair:** connect the situation to existing player gravity.

### Predetermined Climax

**Symptom:** the Climax describes who wins, what the PCs decide, or what
revelation they must accept.
**Repair:** prepare opposition, stakes, leverage, and decision pressure;
let play answer the question.

### Predetermined Resolution

**Symptom:** an ending is written before the Climax occurs.
**Repair:** prepare consequence possibilities and instantiate the
Resolution from actual play afterward.

### Beat padding

**Symptom:** extra Developments or Cliffhangers exist only to preserve
length or alternation.
**Repair:** remove the filler and reconnect the nearest meaningful states.

### Escalation by inflation

**Symptom:** every later problem simply contains more enemies, larger
explosions, or higher numbers.
**Repair:** escalate consequence, intimacy, cost, exposure, or difficult
tradeoffs.

### Lore rehearsal

**Symptom:** Developments repeat information already known because the
planned scene still exists.
**Repair:** begin from the current knowledge state and reveal something
that changes play.

### Prep preservation

**Symptom:** opposition receives coincidences, reinforcements, immunity,
or information primarily so unused prepared material can still happen.
**Repair:** honor the changed world state and retire invalidated prep.

## Validation gate

Before declaring an orchestration complete, verify every item.

### Canon

- [ ] Current state comes from authoritative compiled vault material.
- [ ] New inventions are identifiable as prep rather than established history.
- [ ] No prepared Beat is treated as evidence that an event occurred.

### Gravity

- [ ] Every prepared Beat has a concrete Link of Relevance.
- [ ] Links point to established player investments.
- [ ] Major opposition pressures something the PCs already value.

### Composition

- [ ] The dramatic question permits multiple answers.
- [ ] Every Beat has a reachable entry state.
- [ ] Every transition follows from state rather than assumed player method.
- [ ] Branches correspond to materially different consequences.
- [ ] Shared consequences reconverge where appropriate.

### Rhythm

- [ ] New adventure structures begin with a Hook.
- [ ] Development and Cliffhanger alternate on every active path.
- [ ] Hook energy informs the first subsequent Beat.
- [ ] The final pre-Climax Beat contrasts with the Climax where practical.
- [ ] Climax leads directly to Resolution.

### Escalation

- [ ] Every Beat materially changes the playable state.
- [ ] Later pressure builds from earlier consequences.
- [ ] Repeated Beat functions have been removed or differentiated.
- [ ] Later Cliffhangers generally carry greater consequence than earlier ones.

### Agency

- [ ] No unresolved Beat requires a predetermined PC decision.
- [ ] No unresolved Beat requires predetermined PC emotion or belief.
- [ ] Success can permanently alter or bypass later prep.
- [ ] Failure produces a changed playable state.
- [ ] Unused Beats can be discarded safely.

### Climax

- [ ] The dramatic question is decisively contestable.
- [ ] Relevant player investment is active.
- [ ] Opposition is present or reachable.
- [ ] Players possess enough understanding to choose meaningfully.
- [ ] Prior play has created meaningful leverage.
- [ ] Stakes are legible.
- [ ] Multiple outcomes remain possible.
- [ ] Relevant forces have naturally converged.

### Resolution

- [ ] Resolution remains dependent on the Climax's actual result.
- [ ] Consequences update the world rather than merely narrating closure.
- [ ] Future hooks emerge from surviving state rather than undoing the ending.

### Vault

- [ ] Atomic Beat content has one source of truth.
- [ ] Composition uses wikilinks or appropriate embeds rather than duplicated prose.
- [ ] Current repository templates and Obsidian syntax are respected.
- [ ] The page is concise enough for an expert human DM to scan during play.

The orchestration is complete only when every applicable item passes.

## Diagnosing a stalled or flat journey

Reference consulted only once a quest, arc, or campaign journey has
already stalled — not read up front. Full shape catalog:
`.claude/skills/draft-story/references/story-structures.md`.

Use when a quest, arc, or campaign has sat with no forward beats for a
while — a stall usually means the pattern, not the party, is the problem.

- **"Nothing's happening."** No Ticking Clock is live. Fix: give the
  opposing faction/NPC a next step, surfaced as a rumor.
- **"It feels flat, not escalating."** Stuck at Rung 1 of the Escalation
  Ladder (`.claude/skills/draft-story/references/story-structures-campaign.md` § The
  Escalation Ladder). Fix: name what player action (or inaction) raises
  the stakes one rung.
- **"Every session/beat feels the same."** No variation in opening or
  register. Fix: vary the in medias res opening
  (`.claude/skills/draft-story/references/story-structures-classic.md` § In medias res), or
  introduce a Convergence
  (`.claude/skills/draft-story/references/story-structures-campaign.md` § Convergence Arc)
  for novelty.
- **"Players seem disengaged."** Threads aren't connected to player
  gravity wells. Fix: audit active threads against PC backstories — at
  least one active thread per PC needs a direct personal stake.
- **"It feels like a series of unrelated events."** No Slow Burns or
  Convergence Arcs providing connective tissue
  (`.claude/skills/draft-story/references/story-structures-campaign.md` § The Slow Burn, §
  Convergence Arc). Fix: retroactively connect 2–3 past events with a
  Slow Burn reveal.
- **"The 'main plot' is being ignored."** Convert it into a faction
  timeline (Parallel Threads,
  `.claude/skills/draft-story/references/story-structures-campaign.md` § Parallel Threads)
  that advances whether players engage or not — sandbox players resist a
  predetermined path, not urgency itself.

Quest-scale symptoms specific to `quest_status: active` pages —
`link_of_relevance` too thin, or a quest with no real pull — are the quest
guide's own diagnostic: `vault/refs/vault/quest/references/structure.md` §
Diagnosing a stalled quest.
