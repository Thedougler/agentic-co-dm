# Data Model: Skill Graph Architecture

This feature adds no runtime database or universal state schema. These are design concepts expressed in existing Markdown guidance, skill evals, and observable repository behavior.

## Capability

An existing skill or deterministic wiki operation that owns bounded work.

| Field | Meaning | Validation |
|---|---|---|
| name | Existing skill or operation name | Resolves to an existing owner; no generic fallback owner |
| input | Intent, target, evidence, and constraints accepted by the owner | Specific enough to select the owner directly |
| work | Owner-specific procedure | Preserves specialized craft and safeguards |
| done | Observable completion guard | Not satisfied by prose existence alone |
| handoff | Condition and receiving owner when ownership changes | Child scope is bounded and control returns to the parent |
| read/write mode | Canonical mutation permission | Read mode does not mutate canonical wiki state |

## Capability Route

A direct selection or handoff between existing owners.

| Field | Meaning | Validation |
|---|---|---|
| trigger | User intent, artifact kind, prerequisite, or finding class | Uses existing routing vocabulary |
| source owner | Parent or current capability | Retains the original objective when delegating |
| destination owner | Existing receiving capability | Owns the delegated artifact or operation |
| return condition | Receiving capability's completion evidence | Required before the parent resumes |

State transitions:

```text
classified -> active owner -> [dependency owner -> dependency done -> parent resumes]* -> validated -> complete
```

Invalid transitions: completion before required dependencies; parent abandonment after child completion; mutation from a read-only route; parallel writes to the same canonical surface.

## Parent Operation

The capability accountable for the user's original objective.

Fields: original objective, active owner, unresolved dependencies, completed dependencies, final completion guard.

Rules:
- Delegation transfers only the bounded child artifact or operation.
- The parent resumes after every child completion.
- The parent closes only after the original objective and all required output contracts pass.

## Capability Dependency

A real prerequisite artifact or state.

Fields: dependent owner, prerequisite owner/state, reason, write surface, completion evidence.

Rules:
- Prerequisites execute before dependents.
- Independent dependencies with disjoint canonical write surfaces may execute concurrently.
- Shared canonical write surfaces have one active writer and execute serially.
- Context convenience is not a dependency.

## Context Projection

Minimum sufficient canon and operational evidence for one capability.

Fields: owner instructions, target artifacts, relevant canon, applicable template/contract, validation evidence, deliberate omissions.

Rules:
- Prior capability context is not inherited automatically.
- Retrieval deepens only while the evidence condition is unmet.
- Unrelated artifact groups remain omitted.

## Completion Guard

An observable condition that permits a route to continue or close.

Kinds:
- owner artifact satisfies its output contract;
- required dependency exists and validates;
- read evidence is sufficient and cited;
- scoped lint/validation is green;
- an unresolved owner-level blocker is reported with evidence.

## Observation Surface

Existing compact query, lint, or health evidence.

| Surface | Owner | Consumer behavior |
|---|---|---|
| query | `scripts/wiki query` and wiki CLI contract | Use hits; deepen retrieval only when insufficient |
| lint | `scripts/wiki lint` / `lint fix` and wiki CLI contract | Follow complete findings and `next`; rerun affected scope |
| health | `scripts/wiki health` and wiki CLI contract | Follow `context.act`, `next`, and ordered `focus` without reranking |

## Output Contract

The combination of owner conventions, template/contract, and validation rules defining a valid artifact.

Relationships:
- Root routing selects the owner.
- The owner skill defines craft and local completion.
- Template/contract defines artifact shape where applicable.
- Validation rules check the written artifact.
- Synchronization is required only among counterparts governing the same changed behavior.

## Canonical workflow compositions

### Read

Input -> direct read owner -> focused retrieval -> evidence sufficient -> cited answer -> done.

Canonical pages, manifests, indexes, and logs remain unchanged. Derived CLI cache/timing writes remain governed by the wiki CLI contract.

### Write

Input -> direct artifact owner -> retrieve canon -> resolve dependencies -> mutate owner artifact -> scoped validation feedback -> done.

### Ingest

Source -> ingest owner -> destination/owner resolution -> owner write -> manifest/index/log/hot tracking -> scoped validation -> QMD refresh -> done.

### Maintenance

Health/lint observation -> existing ordered action -> deterministic fixer or artifact owner -> rerun affected scope -> clean or specific blocker -> done.

## In-scope owner inventory

The implementation inventory is derived from the existing `AGENTS.md` Wiki, Wiki kind, Co-DM lifecycle/world-building, and presentation routing tables plus their receiving skills. It is not a second owner registry. At minimum it covers:

- Read: `wiki-query`, `wiki-context-pack`, `wiki-narrate`, `memory-bridge`, `session-search`.
- Write/ingest: `wiki-ingest`, `wiki-update`, `wiki-capture`, `wiki-agent`, `wiki-history-ingest`, `cross-linker`, `tag-taxonomy`, `wiki-dedup`, `wiki-import`, `wiki-research`, `wiki-synthesize`, `wiki-dashboard`, `graph-colorize`.
- Maintenance/observation: `wiki-lint`, `wiki-status`, `daily-update`, `wiki-rebuild`, `wiki-stage-commit`, `wiki-export`, `wiki-switch`.
- Campaign artifact owners and composers used by cross-capability routes: `session-beats`, five typed beat skills, `run-guide`, `theatre-of-the-mind`, `place-design`, `city-design`, `region-design`, `faction-design`, `lore-design`, `narrative-islands`, `vehicle-design`, `spell-design`, `npc-design`, `encounter-prep`, `dungeon-design`, `traps-trials`, `travel-events`, `homebrew-monsters-5e`, `dnd-5e-magic-item-design`, and `foundry-stage`.

Implementation must reconcile this inventory against the live root routing tables before editing; additions or removals follow the root authority rather than this descriptive snapshot.
