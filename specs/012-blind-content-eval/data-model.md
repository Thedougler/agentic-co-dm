# Data Model: Blind Cold Evaluation of D&D Content

Entities are jobs and judgments. No database.

## Guidance change

An edit to a skill, standing instruction, or procedure that produces D&D wiki content.

| Field | Rule |
|---|---|
| Produces D&D content | `true` → this eval is required. `false` → not this feature. |
| Sample | Work produced from the changed guidance. Required before done. |
| Done | Incomplete until two independent cold evals pass. |

## Sample content

The judged object.

| Field | Rule |
|---|---|
| Kind | The campaign `type` / kind it claims (place, creature, person, beat, …) |
| Bands | DM-facing, player-facing, mechanical — each present or absent |
| Not | The skill file, the author's notes, the diff |

## Eval job

One cold judgment of one sample.

| Field | Rule |
|---|---|
| Evaluator | Did not produce the sample. Does not see authoring session, skill diff, or author notes. |
| Axes | Every applicable axis from the table below. Inapplicable axes omitted, not failed. |
| Verdict | `pass` \| `fail` per axis, then overall. Fail any applicable axis → overall fail. |

## Axes

| Axis | Applies when | Pass | Fail |
|---|---|---|---|
| Form | Sample claims a kind | Layout, format, shape, mechanics match that kind | Wrong kind-shape |
| Appropriate use | Form treatments are present | Treatments mean the jobs they mean | Decorative or swapped use |
| DM copy | DM-facing bands exist | Complete-sentence table reference | Telegram, slash-stacks, agent-speak, novel-padding |
| Spoken look | Player-facing narration exists | Theatre of the mind: drawable, speakable, leak-free | Secrets, DCs, unearned names, process notes, telegram, padding |

## Evaluation set

| Field | Rule |
|---|---|
| Count | At least two independent eval jobs on the same sample |
| Agreement | Incomplete while they disagree on overall pass/fail |
| Contamination | Any eval that saw the authoring session is void |

## Relationships

- Guidance change → one sample → two eval jobs → done iff both pass
- Eval job → loads copy-writer / theatre-of-the-mind / vault form; does not own those rubrics
- Automatic file-shape check → not an eval job; cannot pass the guidance change
- Ordinary wiki write / non-D&D guidance → no eval job required
- DM accept-gate → still required for canon; eval does not publish
