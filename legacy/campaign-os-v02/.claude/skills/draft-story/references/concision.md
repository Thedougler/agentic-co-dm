# Concision — Strunk's line-edit rules

The same six core rules `writing-clearly-and-concisely` applies to this
repo's own process prose (`.claude/skills/writing-clearly-and-concisely/elements-of-style.md`),
applied here to narrative campaign prose instead — fantasy examples, not
process examples. Apply after the eight de-slop passes; they overlap
deliberately — active voice and positive form are also the cure for
copula avoidance and hedging.

## Use the active voice

Active is more direct and vigorous. Replace perfunctory "there is" /
"could be heard" framings with an acting subject:

| Weak | Strong |
|---|---|
| There were dead leaves lying on the courtyard stones. | Dead leaves covered the courtyard stones. |
| The sound of chanting could be heard from the crypt. | Chanting rose from the crypt. |
| The gate was forced open by the ogre. | The ogre forced the gate. |

Passive stays when the acted-upon thing is the topic ("The reliquary was
stolen sometime before dawn" — in a paragraph about the reliquary). Never
hang one passive on another.

## Put statements in positive form

Say what is, not what is not. "Not" is for denial and antithesis, never
evasion:

| Hedged | Definite |
|---|---|
| The captain is not very forthcoming. | The captain stonewalls. |
| He did not remember the password. | He forgot the password. |
| The ward is not without its gaps. | The ward has two gaps: the well and the north drain. |

## Use definite, specific, concrete language

The surest way to hold attention. Prefer the specific to the general,
the concrete to the abstract:

| Vague | Concrete |
|---|---|
| A period of bad weather set in. | It rained every day for a week. |
| He showed satisfaction as he took his reward. | He grinned as he pocketed the coin. |

This is the mechanism behind "lush" player-facing prose too: richness is
concrete sensory detail, not adjective density.

## Omit needless words

Every word tells. This does not mean all sentences short — it means no
dead weight:

| Cut | To |
|---|---|
| the question as to whether | whether |
| he is a man who | he |
| in a hasty manner | hastily |
| owing to the fact that | because |
| in spite of the fact that | although |
| the fact that she had arrived | her arrival |
| His story is a strange one. | His story is strange. |
| Trafalgar, which was Nelson's last battle | Trafalgar, Nelson's last battle |

A single idea dribbled across several sentences usually combines into
one; Strunk cuts a 51-word Macbeth summary to 26 with nothing lost.

## Place the emphatic words at the end

The end of the sentence is the position of prominence — put the new or
striking element there:

| Buried | Landed |
|---|---|
| This steel is used for razors, because of its hardness. | Because of its hardness, this steel is used for razors. |
| A winding stream flowed through the valley. | Through the valley flowed a winding stream. |

The same principle scales up: the emphatic sentence ends the paragraph;
the emphatic paragraph ends the piece. For read-aloud boxes, the last
line is the one the table sits with — make it the hook.

## Keep related words together

Word position shows relationship. Subject and main verb stay close;
modifiers sit next to what they modify; the relative pronoun follows its
antecedent:

| Tangled | Clear |
|---|---|
| Veyra, in the fifth year of her exile, forged the pact. | In the fifth year of her exile, Veyra forged the pact. |
| He only found two runes. | He found only two runes. |

## Supporting rules, briefly

- **One paragraph per topic; lead with the topic sentence.**
- **Parallel form for parallel ideas.** "In spring, summer, or winter" —
  repeat the article/preposition before each term or only the first.
- **Avoid a run of loose and-then sentences.** A paragraph of "X, and Y"
  clauses is sing-song; recast some as simple or periodic sentences.
- **One tense per summary.** Recaps pick past (or present) and hold it;
  antecedent action takes the perfect.

## Misused-words highlights

The Section V entries most likely to matter in campaign prose:

- **However** — meaning "nevertheless", not first in its clause.
- **Less / fewer** — less sand, fewer goblins.
- **Like / as** — *like* governs nouns ("fought like a lion"); before
  clauses use *as* ("as the captain ordered").
- **Interesting** — never announce that a thing is interesting; make it
  so. (The emotional-flatline rule in ai-tells.md is this, generalized.)
- **Certainly / so (intensifier) / very** — indiscriminate intensifiers;
  cut or replace with a stronger word.
- **Data** — plural.
- **Different than** → different from.
- **Effect / affect** — result / to influence.
- **Fact** — only for the verifiable; "the greatest general of the age"
  is a judgment, not a fact.
- **Literal, literally** — never as support for exaggeration.
- **One of the most...** — threadbare opener; start somewhere sharper.
- **Possess** — plain "have" or "own".
- **Claim (verb)** — means *lay claim to*; not a substitute for say,
  declare, maintain.

## Off-thread subagent copyedit

When the main context is tight, don't load this file plus the full draft
into the working conversation. Dispatch a subagent instead:

1. `Agent` (general-purpose), prompt: the draft's absolute path, this
   file's absolute path (`.claude/skills/draft-story/references/concision.md`),
   the register (player-facing or DM-facing), and the instruction to
   line-edit for concision only — style-only, no fact/name/wikilink
   changes, return the edited text plus a one-line-per-change list.
2. The main thread reviews the returned edits and applies them; the
   subagent burns the reading cost, the main context keeps only the diff.
