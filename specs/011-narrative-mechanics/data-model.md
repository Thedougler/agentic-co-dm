# Data Model: Expert-Grounded D&D Content Guidance

Entities are jobs and outcomes. No database.

## Guidance job

One act of creating or changing D&D content guidance.

| Field | Rule |
|---|---|
| Kind | skill \| standing instruction \| pointed-at procedure that creates D&D wiki content |
| Problem | The content problem the guidance must solve |
| Research | Required. Named published designers and documented craft first. High-quality homebrew only if those are silent. None found → invent and flag. |
| Integration | Expert-solved **outcomes** folded into this one document. Techniques may be cited. |
| Incomplete | Vacuum-invented while experts exist; quote dump; second competing procedure; named person's process required as the only method; proprietary book paste |

Ordinary wiki content jobs are not this entity. They follow existing guidance.

## Combat Work job

First instance. One act of authoring or customizing combat mechanics.

| Field | Rule |
|---|---|
| Reader | DM (Work). Players never open the wiki. |
| Narrative beat | lore \| origin \| stakes \| plot \| character. A second person can name it. |
| Place | Named lair/site/battlefield, or none. If named → at least one mechanical pressure. |
| Opposition | Stock unchanged (exempt from custom features) \| customized \| substantial homebrew |
| Override | Explicit DM request for stock/featureless fight, or none |

Incomplete: number-only custom features; flavor-only scenery on a named place; difficulty-only homebrew with no named beat.

## Expert-solved outcome

What a second person can point at in the guidance or in the Work.

| Field | Rule |
|---|---|
| Statement | Testable. Not a method. |
| Source | Named designer / documented craft, or high-quality homebrew if those were silent, or invention flagged |
| Does not own | The only valid creative process; proprietary book text |

Combat instance outcomes:

| Outcome | Applies when |
|---|---|
| Custom feature communicates lore, origin, or stakes | Feature was added or rewritten |
| Named place has mechanical pressure that changes strategy | Encounter has a named place |
| Substantial homebrew names the plot or character beat it manifests | Mechanical rewrite changes how the creature acts |

## Relationships

- Guidance job → research → integrated outcomes on that same document
- Next ordinary content job → follows that guidance (no fresh research)
- Combat Work job → combat instance outcomes (first application of the loop to combat craft)
- Stock opposition / explicit override → skip custom-feature outcomes
- Craft math, facts, procedure → not this model
- Writing/visual authorities (010) → still apply; this model does not reassign them
