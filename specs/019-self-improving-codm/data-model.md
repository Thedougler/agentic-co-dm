# Data Model: Self-Improving Co-DM

No database. Durable objects are Markdown (and one helper-owned sitting log).

## Table Aim

Who these players are and the current campaign intent.

- **players**: Named people at the table (at least one; tests use three).
- **intent**: What this campaign is trying to be for them now.
- **status**: `missing` → `recorded` (after DM accept on the campaign hub) → `updated`.

Validation: Co-DM MUST NOT treat Work as aimed while `missing`. Work that could swap onto another table without edits is not aimed.

## Sitting

One prep or wrapup window.

- **kind**: `prep` | `wrapup`
- **jobs**: Named jobs finished
- **paths_read**: Files loaded
- **skills_loaded**: Skills loaded
- **helpers_used**: Helper command ids
- **waste_named**: Standing load that did not change the outcome
- **errors_filled**: Error entry ids appended this sitting
- **token_cost**: Derived from paths/skills/output for same-kind compare — not a tokenizer
- **status**: `open` → `recorded`

Validation: every finished prep/wrapup sitting is `recorded`. DM is not a field.

## Error Entry

One runtime failure on `errors.md`.

- **id**: Stable id
- **cause**: What failed
- **sitting**: Sitting that filled it
- **status**: `open` → `drained`
- **cause_fixed**: Boolean; drain requires true

Transitions: `open` only from a runtime failure before sitting close. `drained` only when the cause is actually fixed (wiki fact write after accept, helper, layout, or other landed fix). Drain-without-fix is invalid. Bulk-clear is invalid.

## Helper

Agent-shaped command for a repeating job.

- **id**: Invocable name
- **job**: Repeating job it replaces in context
- **shape**: Arguments in, text or JSON out, exit done vs failed
- **status**: `active` | `stale` | `removed`

Validation: no helper for a one-off. No wrap of an existing command. Stale + still loaded = wasted context → update or remove.

## Reflection

Chat Work after wrapup (and after prep when asked).

- **observation**: At least one concrete note about these players
- **next_change**: Optional one next change
- **status**: `offered` → `accepted` | `edited` | `rejected`

Validation: reject leaves wiki facts and campaign-facing practice unchanged. Accept that needs a fact change becomes a Canon proposal. Accept that needs campaign-facing practice becomes an Improvement proposal. Token/layout/ledger are not this object.

## Layout Move

Regroup of agent-facing files or wiki pages.

- **from** / **to**: Locations
- **scope**: `agent-facing` | `wiki`
- **facts_changed**: Must be false for wiki moves
- **links_resolve**: Must be true after the move
- **trigger**: `growth` (mixed dump / unrelated load). Not `tidiness`

Validation: one-off skip. Worse lookup is not an improvement. Wiki fact change is not a layout move.

## State

```text
sitting open
  → if table aim missing: ask (do not treat Work as aimed)
  → do jobs (gaps do not stall; name the gap)
  → on failure: append error entry
  → on wrapup (or prep if asked): offer reflection
  → record sitting (token cost)
  → if repeating job and no command: create/maintain helper
  → if mixed growth: layout move (keep links; no fact rewrite)
sitting recorded

wiki fact write accepted
  → drain matching open error entries whose cause that write fixed
```
