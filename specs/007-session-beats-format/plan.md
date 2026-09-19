# Implementation Plan: Session Beat Format

**Branch**: `007-session-beats-format` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/007-session-beats-format/spec.md`

## Summary

Session 11 production beats are the cockpit and spine the Co-DM must compose, and ingest must file without flattening. `run-guide` already owns the beat-card catalog — make Session 11 the quality evidence and required job order, omit empty. `session-beats` keeps composition/pacing and the filed spine shape. `wiki-ingest` gains a preserve-and-file branch for session-prep (not distill). Filed home is `wiki/journal/sessions/<campaign-slug>/<session-number>/`. No new skill. No `_raw/` rewrite. No older-session restyle.

## Technical Context

**Language/Version**: Markdown skills, wiki templates, owner conventions. Host agent executes skills. No new compiled language.

**Primary Dependencies**: `run-guide`; `session-beats`; `wiki-ingest`; `wiki/AGENTS.md`; `obsidian-markdown`; `copy-writer`; `wiki/templates/session.md` (log, unchanged role).

**Storage**: Wiki pages under `wiki/journal/sessions/`. Staging `_raw/`. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Side-by-side Reading-view vs Session 11; ingest preserve; folder home. Skill evals at those seams. No bulk lint over older sessions.

**Target Platform**: Local DM workstation. Prose wiki the DM opens in Reading view.

**Project Type**: Wiki guidance + agent skill pack.

**Performance Goals**: SC-001 start a live beat in under 45 seconds. SC-007 open the session folder and reach spine + beats in under 15 seconds.

**Constraints**: FR-007 preserve markdown shape on ingest. FR-013 / SC-006 older session-prep out of scope. FR-006 omit empty. Constitution VII — do not add a second creative procedure beyond the spec’s jobs. Constitution IX — do not copy the cockpit catalog into a third standing doc.

**Scale/Scope**: One session folder pattern. One preserve ingest branch. Pointers in existing skills. One beat-card template scaffold. Session 11 evidence stays in `_raw/`. No `src/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — wiki, Work, Co-DM, session, session-prep, theatre of the mind. No knowledge bank. No GM. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec stories P1–P2 plus folder home. Independently testable. |
| IV. Tests specify behavior | Pass — quickstart observes cockpit jobs, ingest shape, folder home, spoken-look safety. |
| V. Single context | Pass — no second bounded context. |
| VI. Software is agent-shaped | Pass — skills + AGENTS.md; agent files pages; no GUI wrapper. |
| VII. Do not suffocate agents | Pass — constrain cockpit jobs, order, markdown treatments, folder, ingest preserve. Do not freeze Session 11 plot or a single prose voice. |
| VIII. Safe automation unattended | Pass — no new agent chore for formatters; after-write stays as today. |
| IX. Token efficiency | Pass — cockpit catalog stays in `run-guide`; AGENTS.md and session-beats point, they do not duplicate the column table. |

**Post-design re-check**: still pass. Contract is the page and folder the DM opens. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/007-session-beats-format/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── beat-card.md
│   ├── session-spine.md
│   └── ingest-preserve.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
wiki/AGENTS.md
wiki/templates/session-prep.md          # new omit-if-empty beat scaffold
wiki/journal/sessions/<campaign>/<N>/   # filed session home (created on ingest/accept)
wiki/_raw/Session-11-*.md               # evidence; do not rewrite
.agents/skills/run-guide/SKILL.md
.agents/skills/session-beats/SKILL.md
.agents/skills/session-beats/references/session-skeleton.md
.agents/skills/wiki-ingest/SKILL.md
.agents/skills/obsidian-markdown/references/properties.md
.agents/skills/session-wrapup/SKILL.md  # path pointer only
.agents/skills/copy-writer/SKILL.md     # pointer only if it still treats beats as freeform
```

**Structure Decision**: Keep skills + wiki. Do not add a session-format skill. Do not add `wiki/<slug>/sessions/` beside journal — spec home is `journal/sessions/<campaign-slug>/<session-number>/`. `wiki/templates/session.md` remains the post-play log. Beat cockpit lives in `run-guide`; filed spine jobs live in `session-beats`.

## Complexity Tracking

> None. No constitution violations.
