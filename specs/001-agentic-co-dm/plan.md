# Implementation Plan: Agentic Co-DM

**Branch**: `001-agentic-co-dm` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-agentic-co-dm/spec.md`

## Summary

Prep-and-wrap Co-DM for one D&D 5e table. The product the DM opens is the Obsidian wiki at `wiki/`. The Co-DM is the D&D 5e skill pack in `.agents/skills/`, rewritten to writing-for-agents and to this spec. Invention is required as a proposal, grounded in wiki pages and 5e rules. The Co-DM does not create or change a campaign wiki page until the DM approves (FR-019). Named ingest covers those sources plus thin stubs for names in them. Never silent canon, never a fake wiki fact, never an invented person the source did not name. Wiki pages are complete-sentence human prose. Place, item, hazard, and creature notes follow `wiki/templates/` copied from early-dev `_raw/` samples; creature notes are linear. Foundry is the play surface for accepted Work only. The live campaign stays in `Documents/ai-co-dm` until cutover.

No application server. No `src/` tree. Agent-shaped skills, markdown pages, and existing Foundry MCP tools.

## Technical Context

**Language/Version**: Markdown (skills + wiki pages). Host agent (Oh My Pi / Claude / Codex) executes skills. No new compiled language.

**Primary Dependencies**: Obsidian; llm-wiki skill pack (`wiki-ingest`, `wiki-query`, `llm-wiki`); D&D 5e craft pack in `.agents/skills/`; Foundry VTT MCP (`foundry-stage` and siblings); `writing-for-agents`; `copy-writer` + `obsidian-markdown` on every wiki write.

**Storage**: `wiki/` Obsidian vault (markdown + YAML frontmatter). `.manifest.json` for ingest provenance. Work and canon are pages, not a database.

**Testing**: Existing `evals/evals.json` on craft skills. Behavioral checks on wiki pages and Foundry artifacts (constitution IV). Quickstart loop in [quickstart.md](./quickstart.md). No bulk suite of imagined internals.

**Target Platform**: Local macOS DM workstation. One human DM. Players never operate the wiki or the agent.

**Project Type**: Agent skill pack + prose wiki + Foundry staging.

**Performance Goals**: SC-001 locate a fact in under 2 minutes without the agent. SC-009 three new wiki pages readable as ordinary prose.

**Constraints**: Co-DM runs only in prep and wrapup (ADR 0001). v1 is D&D 5e, one campaign, one table. Wiki is human prose (FR-018). No campaign wiki write until DM approval; named ingest + named-in-source stubs only (FR-019). Early-dev `_raw/` samples keep their layout on ingest; templates and skills align to those samples; creature notes are linear. Canon edits require DM-accepted proposals (ADR 0003). Agent-shaped tools only (constitution VI). This repo is a candidate redesign (ADR 0002).

**Scale/Scope**: One table. Full copied D&D 5e toolkit in v1 (~30 craft skills). Campaign of record remains ai-co-dm until cutover.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — plan uses `CONTEXT.md` terms (wiki, Work, Co-DM, prep, wrapup). ADR 0003 still says "bank"; rename in the same change that touches it. |
| II. Issues are the work surface | Pass — this plan does not treat PRs as a request surface. Implementation work lands as GitHub issues after `/speckit.tasks`. |
| III. Spec before code | Pass — spec exists with testable stories. |
| IV. Tests specify behavior | Pass — checks observe wiki pages, citations, accept/reject, Foundry artifacts. No internals. |
| V. Single context | Pass — one `CONTEXT.md`, ADRs in `docs/adr/`. No second bounded context. |
| VI. Tools are agent-shaped | Pass — skills and CLIs; no human-only wrapper. Wiki is the DM surface, not a GUI we build. |

**Post-design re-check**: still pass. Contracts are markdown schemas and skill gates, not a new service. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/001-agentic-co-dm/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── wiki-pages.md
│   ├── work.md
│   └── foundry.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
CONTEXT.md
docs/adr/
docs/agents/
wiki/                      # candidate wiki
  .manifest.json
  index.md
  log.md
  hot.md
  _raw/                    # early-dev layout samples
  _archive/
  templates/
    place.md
    item.md
    hazard.md
    creature.md            # linear; no col
    npc.md
    session.md
    work.md
.agents/skills/            # craft toolkit + llm-wiki + writing-for-agents
  copy-writer/
  obsidian-markdown/
  theatre-of-the-mind/
  foundry-stage/
  foundry-battlemap/
  foundry-token/
  session-wrapup/
  npc-design/
  place-design/
  homebrew-monsters-5e/
  dnd-5e-magic-item-design/
  … (full D&D 5e pack)
```

**Structure Decision**: Keep the repo as skills + wiki + glossary. Do not add `src/`, a web app, or a second vault. `wiki/templates/` is the page shape; early-dev `_raw/` samples are the layout source. Foundry MCP stays external; `foundry-stage` is the gate.

## Complexity Tracking

> None. No constitution violations.
