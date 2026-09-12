# Quickstart: Sample Content Guidance

Prove the feature by reading and writing **sample** pages only. Do not open `legacy/` to “fix” them.

## Prerequisites

- Branch `006-aruhe-page-standards`
- Spec [spec.md](./spec.md), contract [contracts/sample-page.md](./contracts/sample-page.md)
- `wiki/AGENTS.md` Layout states run-jobs (not “match template headings”)
- Skills listed in [plan.md](./plan.md) point at those jobs

## 1. Shared jobs (P1)

Pick one complete `_raw/` page per kind (place, consumable, hazard, creature, person). For each:

- Speak the look aloud. Fail if a secret, DC, or unearned name is in that block.
- Confirm the kind’s run questions are answerable without another page for the same numbers.
- Confirm no empty heading.

Expected: all five pass. Timebox: start play in under 45 seconds per page (SC-001).

## 2. Thin vs dense (P1, P5)

Compare two sample pages of the same kind at different density (e.g. a short fruit vs a long place; Thunk vs Hinewai as people). Fail if the thin page looks like a different document type or is “incomplete” only because unused sections are absent.

## 3. Owner uniqueness (P2–P4)

On a sample place that names fruit, flora, or a creature, follow the link. Fail if the place restates the owner’s effect, save, or sheet in full.

## 4. New pages from jobs, not clones (SC-004)

Author four **new** thin samples (do not photocopy a named `_raw/` outline):

- Place: look, situation, one way onward, one consequential move, presence-or-absence
- Consumable: look, classification, one effect
- Creature: look, sheet stub, habitat, opening, one shut-down
- Person: who/want, look, first minutes, one tie; no Combat heading

File as Work (`proposed`). Expected: a second reader can run first contact; no empty sections.

## 5. Legacy untouched (SC-006)

Confirm this change set does not rewrite `legacy/` or restyle historical pages solely to match sample jobs. Wrapup notes on a legacy page keep that page’s shape.

## 6. Agent path

Load `wiki/AGENTS.md` only. Confirm Layout done-when is jobs + omit-empty, not heading-order match. Confirm a skill that used to name `_raw/` as layout source now calls those files illustrative.

Pass: steps 1–6 hold. Fail any step → guidance is not the default yet.
