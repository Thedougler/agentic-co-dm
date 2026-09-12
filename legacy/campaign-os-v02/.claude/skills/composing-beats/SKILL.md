---
name: composing-beats
description: >-
  The default session-prep and play-content method in a Campaign OS repo
  (vault/ present): orchestrate Hook, Development, Cliffhanger, Climax, and
  Resolution beats into playable sandbox structures. Use when prepping a
  session, turning a situation, quest, or adventure into a Beat Chart or
  beat field, resequencing beats after player action, deciding whether play
  has earned a Climax, or auditing a composition for agency, gravity,
  rhythm, and continuity. Delegates single-beat craft to the
  writing-*-beats skills.
---

# Composing Beats

Compose **pressure, not plot**. The DM is the runtime.

The vault contains the situation, actors, player investments, prepared
pressures, and consequences from which play emerges. The composition
describes **what dramatic functions are available and how they can follow
one another** — never the route the players will take. Treat the Beat
Chart as dramatic grammar (Hook → Development ↔ Cliffhanger → Climax →
Resolution) and the sandbox as **irrigation**: player gravity → relevant
obstacles → player choice → changed world state → next appropriate beat.

The output is **prepared dramatic possibility**. The table determines
actuality.

## Contract

A successful composition:

1. begins from the campaign's current compiled state and the dramatic question presently worth playing;
2. anchors every prepared beat to established player gravity via a Link of Relevance;
3. composes atomic beat pages rather than duplicating their contents;
4. preserves dramatic rhythm and escalation along every prepared path without scripting player decisions;
5. exposes only branches justified by materially different world states, and lets unused beats disappear safely;
6. enters the Climax only when earned, leaves the Resolution dependent on the Climax's actual result, and produces a Beat Chart the DM can scan during play.

## Beat craft delegation

Delegate atomic beat creation, revision, and review to the specialized
skill — invoke it rather than reproducing its instructions:

- `writing-hook-beats` — involvement and opening pressure.
- `writing-development-beats` — information, relationships, leverage, revelations, changed understanding.
- `writing-cliffhanger-beats` — immediate danger, physical conflict, pursuit, hazards, demanded action.
- `writing-climax-beats` — decisive play that answers the central dramatic question.
- `writing-resolution-beats` — consequences and the new settled state created by the Climax.

Traps, trials, puzzles, and hazards inside a beat: `writing-traps-trials`.
Spoken or shown prose: `writing-player-prose`. Encounter math:
`encounter-prep`.

This skill owns **composition between beats**. Beats are `type: beat`
pages instantiated from `vault/_templates/_episodes/_beat_<type>.md` —
episode-scoped beats in `vault/episodes/NNN/`, situation-scoped beats in
`vault/campaigns/shattered-sea/beats/`.

Also out of scope: an entity's own page (NPC, location, faction, quest,
item, encounter, creature) — its own prep skill, never inlined here.
Generating scene art or rendering a battlemap — `visual-aids` /
`battlemap-render`. Flipping `status:` past `pending` or touching
`publish:` — `world-update` / `canon-review` / PUBLISH, never this skill.

## Canon and gravity

The compiled wiki is the authoritative campaign state — follow the
repository's retrieval and canon-governance skills before relying on
remembered campaign information. Prepared material describes possibility;
played material becomes authoritative only through the normal
session-ingest pipeline. After a session, re-orchestrate from the updated
compiled vault, never from what the chart predicted.

Consult `vault/campaigns/shattered-sea/player-gravity.md` and
`vault/refs/blm-player-gravity.md` whenever preparing or selecting beats.
Every prepared beat records its **Link of Relevance**: the established
goal, fear, relationship, history, obligation, or desire that makes it
worth engaging.

Follow the repository's templates and Obsidian contracts for frontmatter,
wikilinks, embeds, tags, callouts, and page schemas; prefer wikilinks or
embeds to duplicated entity information.

## Reference index

| File | Read when |
|------|-----------|
| `references/composition.md` | Running any workflow step in detail; the core model (Beat, State, Gravity, Irrigation, Rhythm, Escalation); choosing Spine vs Field; re-orchestrating after play; disciplining branches |
| `references/climax-gate.md` | Evaluating Climax readiness; handing a played Climax to `writing-resolution-beats` |
| `references/audits.md` | Auditing agency, gravity, or an existing composition; diagnosing a failure pattern; running the final validation gate |
| `references/runtime-surface.md` | Writing the Beat Chart onto the Situation page; session shapes and table mechanics; the after-play procedure |
| `references/rhythm-and-pacing.md` | Estimating beats per session; pacing the active path |

## Workflow

Detail for every step: `references/composition.md`.

### 1. Compile the current playable state

Retrieve the smallest authoritative vault set: involved PCs and their
gravity, the situation, active actors, unresolved threats, prior
consequential actions, existing prepared beats, the dramatic question if
defined. **Complete when** every fact the composition needs is either
supported by current vault material or explicitly identified as new prep.

### 2. State the dramatic question

One question whose answer would materially change the situation.
**Complete when** it names a real conflict, permits at least two
materially different answers, player action can influence which becomes
true, and answering it would justify a Climax.

### 3. Map player gravity

Identify only the established investments bearing on this situation —
never manufacture backstory to make prep convenient. **Complete when**
every beat intended for advance preparation can carry a concrete Link of
Relevance.

### 4. Determine the current Beat position

New adventure needing a Hook, mid-structure, or Climax-ready? A new
session does not automatically imply a new Hook. **Complete when** exactly
one next structural function (or the Climax gate) is identified.

### 5. Choose Spine or Field

Spine when player direction makes the near future predictable; Field when
several materially different states remain live. **Complete when** every
retained branch corresponds to a materially distinct playable state and
none exists solely to predict a player method.

### 6. Compose atomic Beats

Assemble a context packet per beat, delegate to its `writing-*-beats`
skill, instantiate from the beat-type template, wikilink from the
composition. **Complete when** every required beat exists as a valid
atomic unit with one source of truth.

### 7. Connect Beats by state

Every transition is justified by an achievable world state — shared
invariants reconverge branches; assumed player decisions do not connect
anything. **Complete when** every edge passes that test.

### 8. Audit rhythm

Verify the beat grammar on every prepared path. **Complete when** every
plausible path has coherent alternation and no beat pads a quota.

### 9. Audit escalation and repetition

Every beat changes the playable state; later beats are more consequential,
not merely larger. **Complete when** no two adjacent beats perform the
same dramatic job.

### 10. Gate, write, validate

Evaluate the Climax gate when decisive play looks near
(`references/climax-gate.md`). Write the Beat Chart onto the Situation
page (`references/runtime-surface.md`). Run the audits and the validation
gate (`references/audits.md`). Run `npm run lint -- <paths>` and fix
findings. **Complete when** every applicable gate item passes and lint is
clean.

## Governing principle

> **Prepare the terrain. Follow the gravity. Let the players choose the
> river.**

The Beat Chart gives that river dramatic rhythm. The sandbox decides where
it actually flows.
