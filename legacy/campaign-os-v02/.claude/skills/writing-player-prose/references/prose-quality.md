# Prose Quality

## Clear writing (Orwell)

Write to express thought clearly, not to conceal it. The relationship
between language and thought is bidirectional: unclear language produces
unclear thinking, which produces worse language.

Applies to **every word meant to be read** — read-aloud boxes, DM-facing
notes, player-facing handouts, recaps, NPC dialogue, lore entries, skill
bodies, runbook prose, commit messages. The only exception: mechanical
stat blocks and frontmatter fields, which are data, not prose.

Source: Orwell, *Politics and the English Language* (1946).

### Six rules

In order of priority:

1. **No clichéd imagery.** Never use a metaphor, simile, or figure of
   speech you commonly see in print.
2. **Prefer short words.** Never use a long word where a short one will do.
3. **Eliminate ruthlessly.** If it is possible to cut a word out, always
   cut it out.
4. **Active voice.** Never use the passive where you can use the active.
5. **Plain language.** Never use a foreign phrase, scientific word, or
   jargon if an everyday English equivalent exists.
6. **Break rules when necessary.** Break any of these rules sooner than
   write anything outright barbarous.

### Writing faults to eliminate

#### Dying metaphors

Worn-out phrases that no longer evoke imagery: "toe the line,"
"Achilles' heel," "swan song." These are mental shortcuts that prevent
fresh thinking. Replace with a direct statement or a fresh image.

#### Verbal false limbs

Phrases that pad sentences without adding meaning:

| Verbose | Terse |
|---|---|
| exhibit a tendency to | often [verb] |
| render inoperative | break |
| with respect to | about |
| the fact that | that (or recast) |
| in view of | because |
| serve the purpose of | [verb directly] |

#### Pretentious diction

Latinate or scientific vocabulary used to appear sophisticated when a
plain word exists:

| Pretentious | Plain |
|---|---|
| ameliorate | improve |
| expedite | speed |
| utilize | use |
| endeavour | try |
| eliminate | end / remove |
| facilitate | help |
| commence | begin |

#### Meaningless words

Vague terms that express approval or disapproval without concrete content.
If a word could be removed and the sentence still says something specific,
it is meaningless. Replace with the concrete claim it was obscuring.

### Writing process

Before writing each sentence:

1. What am I trying to say?
2. What words will express it most precisely?
3. What image or idiom will make it clearer?
4. Is this image fresh enough to have an effect?
5. Could I put it more shortly?
6. Have I said anything avoidably ugly?

Select words by meaning, not pattern. Choose words for what you need to
express, not because they commonly appear in similar contexts. Let the
meaning determine the word; never the reverse.

### Concrete over abstract

Move toward the concrete. Compare:

> *The race is not to the swift* — concrete, vivid, direct.

> *Success in competitive activities exhibits no tendency to be
> commensurate with innate capacity* — abstract, Latinate, lifeless.

The concrete version uses everyday words with clear imagery. The abstract
version uses Latinisms that obscure meaning. Make abstractions into scenes,
bodies, actions, things.

### Purpose

Writing is an instrument for expressing thought, not concealing it.
Simplified, precise English forces honest thinking. When language becomes
vague, unclear reasoning hides behind it. Make meaning impossible to
misunderstand.

## Prose inflation filter

LLMs naturally overproduce fantasy prose. Actively remove phrases whose
primary function is sounding literary rather than communicating something
useful. Replace abstraction with specific evidence.

The full catalog of AI-tell phrases, with per-word fixes and Vale rule
wiring: `vault/refs/stories/ai-tells.md`. That file is the single source
of truth — do not maintain a separate list here.

## Adjective test

For every adjective, ask whether it:

- changes the image,
- changes player understanding,
- establishes relevant tone,
- distinguishes the object.

If not, delete it.

Instead of:

> a massive, imposing, ancient stone door

Try:

> a stone door tall enough for a giant.

Concrete scale carries more information.

## Metaphor test

Use metaphors when they compress an unfamiliar image into a familiar one.

Good:

> The tower leans over the harbor like a fisherman listening for a splash.

Questionable:

> Moonlight cascades across the silver tapestry of waves like the tears of forgotten gods.

The second consumes attention without improving play unless that exact lyrical tone is required.

## Cliché test

If a phrase could appear unchanged in hundreds of unrelated fantasy adventures, replace it with a detail specific to this world, character, or moment.

Generic:

> The marketplace bustles with activity.

Specific:

> Fishmongers shout prices over a priest publicly excommunicating a swordfish.

Specificity creates world.

## Information density test

Each spoken unit should ideally perform multiple functions.

Strong detail:

> The guards wear ceremonial armor over muddy boots.

This can communicate:

- status,
- haste,
- current conditions,
- possible recent movement,
- institutional contrast.

Prefer details that carry several useful signals without requiring explanation.

## Concrete before abstract

Prefer observable manifestations.

Instead of:

> The city is decadent.

Use:

> A sedan chair waits outside the soup kitchen while two servants argue about which perfume to spray inside it.

Instead of:

> The fortress is poorly maintained.

Use:

> Someone has painted fresh heraldry across a gate whose hinges are being held together with rope.

Concrete manifestations do more than abstract adjectives because they simultaneously establish:

- world state,
- tone,
- social conditions,
- possible implications.
