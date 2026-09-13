# Data Model: Self-Improving Co-DM

No database. Durable objects are Markdown (and one helper-owned sitting log).

## Table Aim

Who these players are and the current campaign intent.

- **players**: Named people at the table (at least one; tests use three).
- **intent**: What this campaign is trying to be for them now.
- **status**: `missing` → `recorded` (after DM accept on the campaign hub) → `updated`.
- **home**: Campaign hub wiki page, grouped under layout kind Campaign State.

Validation: Co-DM MUST NOT treat Work as aimed while `missing`. Work that could swap onto another table without edits is not aimed. DM Intelligence MUST NOT hold a second copy of the aim.

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

## Layout Kind

Grouping name for agent lookup. Not a campaign `type`. Not a frontmatter field.

- **name**: One of Encounters, Rules, Campaign State, DM Intelligence, System, Source Material
- **surface**: `wiki` (Encounters, Rules, Campaign State, DM Intelligence) | `agent-facing` (System, Source Material)
- **template**: Wiki kinds only — `wiki/templates/encounter.md` (`session-prep`), `rules.md` (`lore`), `campaign-state.md` (`lore`), `dm-intelligence.md` (`work`)

Validation: MUST NOT duplicate an existing `type` (Characters, Places, Factions, Deities, Items, Vehicles, Creatures, Situations, Narrative Islands, Sessions, Lore). System and Source Material MUST NOT be treated as wiki canon and MUST NOT get wiki templates. Source Material is `wiki/_raw/` staging. System is skills/`AGENTS.md`/`docs/agents`. Campaign State includes the campaign hub. DM Intelligence is not the aim. New pages from a wiki template use that template's pinned `type`.

## Wiki Template

Copy-start scaffold for one wiki layout kind.

- **layout_kind**: Encounters | Rules | Campaign State | DM Intelligence
- **path**: `wiki/templates/<file>.md`
- **type**: Existing campaign `type` only (`session-prep` | `lore` | `work`)
- **jobs**: Named in the `wiki/AGENTS.md` layout table. Pass is those jobs, not heading-order match.

Validation: MUST NOT add a campaign `type`. Existing pages of that layout kind are rewritten onto the template when facts stay the same. A rewrite that would change facts waits on accept. Table aim stays on the hub.


## Layout Move

Regroup of agent-facing files or wiki pages.

- **from** / **to**: Locations
- **scope**: `agent-facing` | `wiki`
- **layout_kind**: One Layout Kind name
- **facts_changed**: Must be false for wiki moves
- **type_changed**: Must be false
- **links_resolve**: Must be true after the move
- **trigger**: `growth` (mixed dump / unrelated load). Not `tidiness`

Validation: one-off skip. Worse lookup is not an improvement. Wiki fact change is not a layout move. Changing campaign `type` is not a layout move. Filing System or Source Material as canon is not a layout move. Copying table aim onto DM Intelligence is not a layout move.

## State

```text
sitting open
  → if table aim missing: ask (do not treat Work as aimed)
  → do jobs (gaps do not stall; name the gap)
  → on failure: append error entry
  → on wrapup (or prep if asked): offer reflection
  → record sitting (token cost)
  → if repeating job and no command: create/maintain helper
  → if mixed growth: layout move by layout kind (keep links; no fact rewrite; no type rewrite; System/Source Material stay non-canon)
sitting recorded

wiki fact write accepted
  → drain matching open error entries whose cause that write fixed

wiki template lands
  → rewrite existing pages of that layout kind onto the template when facts_changed is false
  → if facts would change: wait on accept
```
