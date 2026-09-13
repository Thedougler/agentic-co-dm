# Implementation Plan: Self-Improving Co-DM

**Branch**: `019-self-improving-codm` | **Date**: 2026-09-13 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/019-self-improving-codm/spec.md`

## Summary

Close the Co-DM improvement loop around 001: shared table aim, no stall on gaps, wrapup reflection with DM-gated campaign changes, and agent-owned efficiency (token cost, helpers, `errors.md` fill/drain, file/folder layout including llm-wiki).

No new skill. Standing rules in `AGENTS.md` and `docs/agents/work.md`. One wrapup skill add for the required reflection (design-impact). One agent-shaped helper for the repeating error-ledger job. Sitting cost is recorded as what was loaded and finished, not a tokenizer. Layout kinds are lookup grouping only: wiki Encounters, Rules, Campaign State, DM Intelligence; agent-facing System, Source Material. Existing campaign `type` stays. Table aim stays on the campaign hub, grouped under Campaign State.

## Technical Context

**Language/Version**: Markdown standing instructions and skills executed by the host agent; Python 3 for one small CLI helper

**Primary Dependencies**: existing Co-DM product (001), `session-wrapup`, `docs/agents/work.md`, `AGENTS.md`, wiki-ingest destinations, writing-for-agents (VI)

**Storage**: Repo-root `errors.md`; append-only sitting records; campaign hub wiki page for table aim (facts, DM accept; hub grouped under Campaign State); llm-wiki pages stay Markdown; Source Material stays staging (`wiki/_raw/`), not canon

**Testing**: One fixture check at the public seam: ledger append/drain invariants, sitting record fields, layout findability (mixed dump of wiki layout kinds + agent-facing System/Source Material → one-kind load), wrapup reflection is chat Work, aim not copied onto DM Intelligence. Do not snapshot instruction wording.

**Target Platform**: Local DM workstation and any agent host that loads repository skills

**Project Type**: Agent skill pack, standing instructions, and one helper CLI

**Performance Goals**: Same-kind sittings trend to lower token cost at the same quality. Lookup of one job or one layout kind does not load unrelated trees.

**Constraints**: Co-DM still prep/wrapup only. Wiki **facts** stay DM-gated. Layout, token cost, helpers, and the error ledger are agent-owned. Do not wrap an existing command. Do not reorganize one-off files for tidiness. Do not replace the campaign `type` enum. Do not add a layout kind that duplicates an existing `type`. Do not treat System or Source Material as wiki canon. 012/016 still bind when they apply.

**Scale/Scope**: One campaign, one table, D&D 5e. Standing rules + wrapup reflection step + error-ledger helper + sitting record + layout-kind grouping. No new app, database, skill, or `type` value.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — DM, Co-DM, Wiki, Work, Session, Prep, Wrapup, Canon proposal. Feature objects (table aim, token cost, helper, error ledger, layout kind) stay in this spec’s data model, not a silent glossary fork. Layout kind names are grouping labels, not CONTEXT.md terms. |
| II. Issues are the work surface | Pass — this plan is the feature workflow, not a new request surface. |
| III. Spec before code | Pass — spec has independently testable P1–P6 scenarios. |
| IV. Tests specify behavior | Pass — fixtures observe ledger, sitting records, layout findability, reflection-as-Work. Not instruction wording. |
| V. Single context | Pass — no second wiki or glossary file. |
| VI. Software is agent-shaped | Pass — helper is args in, text/JSON out, done vs failed. No GUI wrapper. |
| VII. Do not suffocate agents | Pass — outcomes and named failures only; no prescribed reflection voice or folder taxonomy. Layout kinds name the lookup groups; they do not mandate a folder tree. |
| VIII. Safe automation runs unattended | Pass — no new human chore; ledger helper is agent-invoked. |
| IX. Design trends toward token efficiency | Pass — this feature *is* IX. No new skill; point at 001/work.md instead of restating. |
| X. Agents act autonomously by default | Pass — agents own token cost, helpers, ledger, layout without waiting. |
| XI. Designated writer bounded concurrency | Pass — `session-wrapup` reflection step is design-impact; implement dispatches one writer. `AGENTS.md` / `work.md` are session-agent. This plan does not write the wrapup skill. |
| XII. Prompt other agents with objectives | Pass — implement uses a scoped prompt for the wrapup edit. |
| XIII. Wiki media filenames distinguish kind | Pass — layout self-org does not drop kind-in-filename or reintroduce spaces. |
| XIV. Use the simplest tool | Pass — one helper only where the job repeats and no command exists; otherwise Edit/Write. No wrapper around `qmd` or git. |

## Project Structure

### Documentation (this feature)

```text
specs/019-self-improving-codm/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/
    └── self-improving-codm.md
```

### Source Changes

```text
AGENTS.md
docs/agents/work.md
.agents/skills/session-wrapup/SKILL.md
errors.md
scripts/error-ledger.py
```

**Structure Decision**: Keep existing owners. Standing loop lives in `AGENTS.md` + `work.md`. Reflection is a required wrapup chat step, not a new skill. Error ledger is a repo-root Markdown file operated by one helper. Sitting records append beside it (same helper or a sibling command). Wiki layout self-org is a standing rule, not an ingest-engine rewrite. Layout kinds do not add frontmatter or a new `type`.

Implementation of the wrapup skill edit is **design-impact**. The session agent writes these Spec Kit artifacts, `AGENTS.md`, `work.md`, `errors.md`, and the helper. The wrapup skill is unmodified until `/speckit.implement` dispatches the designated writer.

## Complexity Tracking

None.

## Phase 0: Research

- Confirm no new skill.
- Confirm token cost without a tokenizer.
- Confirm `errors.md` path and drain-on-fix.
- Confirm wrapup owns the reflection offer.
- Confirm wiki layout vs wiki facts.
- Confirm layout kinds (non-redundant only; wiki vs agent-facing; hub under Campaign State).
- Confirm 016 dispatch only for wrapup.
## Phase 1: Design

- Model table aim, sitting, error entry, helper, layout move, layout kind, reflection.
- Document the agent-facing contract.
- Provide fixture scenarios for aim-ask, gap-no-stall, reflection gate, token/helper, ledger fill/drain, mixed-dump layout (wiki kinds + System/Source Material), layout is not canon.

**Post-design gate**: Constitution checks above still pass. No unresolved technical unknowns remain.
