# Climax Beat Reference

Consult this file when building the active situation, designing pressure and escalation, writing the DM-facing body, or running the validation gate.

The procedure belongs in `../SKILL.md`. This file owns the detailed Climax model so the main workflow stays short and predictable.

## Climax invariant

A Climax is the decisive Beat of its containing dramatic unit.

Its job is to answer the situation's central dramatic question through play. Only a Resolution follows it. The Climax is where the sandbox's accumulated causality becomes most visible — prior choices, established investments, active opposition, and live consequences converge on one situation the party can decisively affect.

For sandbox play, preserve the same function while changing the control model:

> **Earned convergence; open outcome.**

The GM prepares the irrigation: pressure, actors, objectives, terrain, leverage, consequences, and things already in motion. The players remain the water: their route through that pressure and the resulting outcome belong to them.

---

## Leading concepts

Use these terms consistently while reasoning about the Beat.

**Gravity** — what the characters already care about strongly enough that pressure attached to it naturally earns engagement.

**Convergence** — independent threads from prior play becoming simultaneously relevant to one decisive situation.

**Pressure** — what changes or worsens while the characters act.

**Leverage** — anything the characters can exploit because they learned, earned, protected, sacrificed for, allied with, or caused it earlier.

**Threshold** — the state change after which the situation cannot simply return to what it was before.

**Fallout** — the facts produced by the Climax that the following Resolution interprets.

---

## The pressure engine

Design the situation as something already happening.

### Opposition objective

What the principal opposing force is trying to accomplish.

### Immediate action

What they are doing when the characters arrive or become able to intervene.

### No-intervention trajectory

What happens if the characters do nothing. This is the baseline simulation of the situation, not a prediction of play.

### Pressure

What gets worse, closes, completes, escapes, collapses, transforms, arrives, or becomes harder while events continue.

Pressure may be represented by an existing campaign clock when one already exists. Reuse it rather than creating a duplicate.

### Threshold

The state after which the old situation is gone.

Examples:

- the coronation is publicly recognized;
- the gate becomes self-sustaining;
- the fleet leaves firing range;
- the evidence is destroyed;
- the hostage is transferred;
- the ritual reaches its irreversible phase;
- the army commits to one side;
- the buried entity wakes.

The Threshold changes the situation. It does not automatically end play.

**Design test:** the GM can answer "What happens if the party waits?" without inventing a new plot beat.

---

## Handle design

Prepare **handles**, not routes.

A handle is a part of the situation players can push on:

- an actor who can be influenced;
- an objective that can be attacked, stolen, protected, exposed, moved, sabotaged, or surrendered;
- terrain that can be exploited;
- a relationship that can be invoked;
- a weakness that can be targeted;
- information that can change allegiance or priorities;
- a resource that can be spent;
- a clock that can be accelerated, delayed, redirected, or made irrelevant;
- an objective whose importance can be reinterpreted.

Provide enough independent handles that success does not depend on discovering a single intended solution.

At least **two independent handles** must be viable before play starts. They must not merely be two implementations of the same required route.

Leave the topology open: if players invent a credible third approach, adjudicate it from the established actors, world rules, and situation rather than forcing it back onto a prepared route.

Do not write an option menu for the players. The handles exist for the DM to understand the situation.

**Design test:** removing any one prepared handle would still leave the situation meaningfully playable.

---

## Escalation triggers

Each trigger has:

**When** — an observable change in the fiction.
**Then** — what the world does in response.
**Because** — the actor, mechanism, or established fact that causes it.

Trigger classes:

- an objective is seized;
- an actor is wounded or exposed;
- a secret becomes public;
- a clock crosses a threshold;
- reinforcements are signaled;
- an alliance visibly breaks;
- the environment is damaged;
- a protected resource is threatened;
- an antagonist realizes their original plan cannot succeed.

Triggers may never require the players to make a particular choice.

Prefer reactions that change the geometry of the problem:

- priorities shift;
- actors realign;
- safe areas become dangerous;
- a secondary objective becomes urgent;
- a bargain becomes possible;
- a resource becomes available;
- an escape route closes;
- truth changes who is willing to fight.

**Design test:** every prepared escalation can be triggered or avoided by changes in the fiction rather than by a predetermined scene order.

---

## Earned-play payoff

Review the Climax from each participating PC's perspective.

Ask:

- What can this character recognize as resulting from earlier play?
- What can they affect because of something they previously did?
- What established relationship can change the situation?
- What personal investment is now under pressure?
- What part of the current problem belongs specifically to choices this party made?

The Climax need not distribute equal spotlight by word count or initiative turns. It must make the campaign's accumulated choices legible.

Prefer **causal spotlight** over decorative spotlight:

Decorative:
> The paladin's old mentor happens to be standing in the room.

Causal:
> The paladin spared the mentor after their earlier betrayal; the mentor now commands the only troops positioned to stop the evacuation.

---

## Outcome dimensions

Do not write the ending. Identify the independent facts the Climax can change.

Typical dimensions:

- primary objective achieved / lost / transformed;
- antagonist alive / dead / captured / escaped / allied / displaced;
- threatened people or assets preserved / damaged / lost;
- secret contained / exposed / misunderstood;
- faction allegiance changed / preserved / fractured;
- resource retained / spent / destroyed;
- personal promise fulfilled / compromised / broken;
- Threshold prevented / reached / redirected;
- cost accepted or avoided.

Only include dimensions actually relevant to this situation.

For each dimension, record the **causal consequences** of plausible states. Do not assign those states to predetermined endings.

This forms a consequence lattice from which the Resolution can later be compiled after the table establishes what actually happened.

A failed objective must remain a valid campaign state. If failure would make continuation impossible, redesign the consequence rather than secretly guaranteeing success.

---

## DM-facing body contract

Use the repository's existing frontmatter template. The following contract governs the body when the template leaves discretion.

```markdown
# <Climax Title>

## Climax Question
<One unresolved question this situation will decide.>

## Situation Now
<2–5 sentences describing what is already happening when the Climax becomes live.>

## Link of Relevance
- [[PC]] — <established investment> → <how the Climax presses on it>
- [[PC]] — <established investment> → <how the Climax presses on it>

## Stakes
- **If unopposed:** <trajectory>
- **Threshold:** <irreversible state change>
- **At risk:** <specific people, relationships, objectives, truths, or resources>

## Actors in Motion
- [[Actor]] — **Wants:** <goal>. **Doing:** <current action>. **Changes if:** <relevant condition>.
- [[Actor]] — **Wants:** <goal>. **Doing:** <current action>. **Changes if:** <relevant condition>.

## Earned Leverage
- <Earlier choice/setup> → <what it makes possible now>
- <Earlier choice/setup> → <what it makes possible now>

## Decision Handles
- **<Handle>:** <what can be affected and why>
- **<Handle>:** <what can be affected and why>

## Escalation Triggers
- **When:** <state change>
  **Then:** <reaction or new pressure>
  **Because:** <established cause>

- **When:** <state change>
  **Then:** <reaction or new pressure>
  **Because:** <established cause>

## Environment
<Only tactically, socially, magically, politically, or narratively actionable features. Link to the location page for maintained lore.>

## Consequence Lattice
- **<Outcome dimension>:**
  - <state> → <direct consequence>
  - <state> → <direct consequence>
- **<Outcome dimension>:**
  - <state> → <direct consequence>
  - <state> → <direct consequence>

## Resolution Handoff
<Record only what the eventual Resolution will need to inspect after play: which facts must be determined from the session outcome. Do not decide them here.>
```

### Runtime compression

The DM-facing note is an execution surface, not a design essay.

Prioritize:

1. what is happening;
2. why the party cares;
3. what earned setup is now exploitable;
4. what changes with time;
5. what the world supports if the players surprise the prep.

Keep extensive biography, faction history, location description, mechanics, and reusable lore on their owning pages and reach them with `[[wikilinks]]` or precise embeds.

The beat page owns only what is unique to **this occurrence of this situation**.

---

## Validation gate

Run every applicable gate before completion.

### Climax gate

- The Beat decides or transforms one central situation.
- Only a Resolution is expected after this Beat within its Beat Chart.
- The situation contains a genuine Threshold.
- The outcome is not already determined.

### Gravity gate

- Every personal stake comes from established character material.
- The page contains explicit Links of Relevance.
- Character investment affects decisions or consequences rather than appearing as decoration.

### Agency gate

- Players are free to choose their route.
- At least two independent handles exist.
- No escalation requires a prescribed player action.
- An unexpected credible plan can be adjudicated from the situation as written.
- Failure, retreat, compromise, alliance, or an unforeseen victory can become legitimate campaign states when fiction supports them.

### Earned-play gate

- Every relevant prior setup found during preparation has been accounted for.
- Earlier player choices can materially alter the Climax.
- Advantages were earned or established rather than appearing solely to guarantee the intended result.
- Liabilities caused by prior choices remain live when still relevant.

### Pressure gate

- Every consequential actor has a present objective.
- The situation changes if the players wait.
- Escalation follows fictional state changes.
- The world does not freeze while waiting for a planned scene.

### Resolution gate

- The Climax records fallout dimensions rather than writing the Resolution.
- Multiple coherent post-Climax states are possible.
- The Resolution can later be derived from what actually occurred at the table.

### Vault gate

- Canon was read from current source-of-truth pages.
- Existing templates and repository schema were followed.
- Entity references use correct wikilinks.
- Maintained information remains DRY.
- Frontmatter follows repository conventions.
- No unsupported canon was inferred from memory.

**Complete only when every applicable gate passes.**

---

## Failure modes

### Predetermined finale → decisive situation

Replace:

> The party defeats the villain and saves the city.

With:

> The villain is activating the sea wall while evacuation ships are still inside the harbor. The wall protects the city from the coming wave but traps every ship behind it.

Now the GM knows the situation. The players determine the ending.

### Mandatory route → independent handles

Replace a single required solution with multiple parts of the situation that can be affected independently.

### Frozen boss room → actors in motion

Begin with actors already pursuing objectives. The antagonist does not wait for a speech. The situation continues to exist between player decisions.

### HP objective → mission objective

Creature defeat may be one means of achieving the objective. It should not automatically be the objective unless killing or defeating that creature is genuinely what resolves the situation.

### Decorative callback → causal payoff

A returning NPC, object, location, phrase, or backstory element should alter what can happen, what someone wants, what someone knows, what the party can attempt, or what the consequences mean. Recognition alone is not payoff.

### Cutscene revelation → actionable evidence

Place enough information in the established world that players can discover, connect, protect, challenge, expose, or misinterpret it through play. The GM owns the truth. The players own the process by which their characters reach it.

### Rescue from nowhere → established causality

When outside intervention occurs, derive it from something already in motion: an alliance the party earned, a message they sent, an enemy they spared, a faction pursuing its own goal, an established environmental process, a consequence deliberately triggered earlier. Unexpected to the characters can still be causally earned. Unexpected to the campaign state is deus ex machina.

---

## Reference basis

This framework combines two compatible models.

### Beat function

*Scripting the Game* treats the Climax as the decisive Beat — the crisis point of the dramatic unit where the central question becomes answerable. It permits battle-driven Climaxes and revelation-driven Climaxes. It expects escalation to arise from the situation's own logic rather than from predetermined scene ordering.

### Player gravity and agency

The Brennan Lee Mulligan player-gravity framing treats players as pursuing routes that make sense to their characters while the GM shapes the surrounding terrain. Preparation becomes reliable when conflicts attach to things the characters already care about. The sandbox translation:

> **Earn the convergence. Pressure the gravity. Leave the outcome open.**
