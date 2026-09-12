# Implementation Plan: Copy Foundry Config

**Branch**: `002-copy-foundry-config` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/002-copy-foundry-config/spec.md`

## Summary

Reuse the campaign of record's live development table from this repo, and on named ingest copy only the art those sources already link. Copy `mcp.json` from `Documents/ai-co-dm`. Recreate the `foundry-data` symlink to the same Foundry Data directory. Extend `wiki-ingest` to exact-basename search that vault for `![[...]]` / media wikilinks, copy hits into `wiki/attachments/`, report misses, never invent, never silent-overwrite. `foundry-stage` keep the accepted-Work gate.

No application server. No `src/`.

## Technical Context

**Language/Version**: Markdown skills + local JSON/symlink. Host agent executes skills. No new compiled language.

**Primary Dependencies**: Existing Foundry VTT MCP (`foundry-mcp` in campaign-of-record `mcp.json`); `wiki-ingest`; `foundry-stage`; campaign of record at `Documents/ai-co-dm` (`CONTEXT.md`).

**Storage**: Local `mcp.json`; `foundry-data/` symlink; `wiki/attachments/` for imported art. Not a database.

**Testing**: Quickstart in [quickstart.md](./quickstart.md). Observe: table reachability, one staged accepted page, resolved embeds, missing-art report. No bulk suite.

**Target Platform**: Local macOS DM workstation. One development table already running.

**Project Type**: Agent skill pack + local machine config + wiki attachments.

**Performance Goals**: SC-001 one sitting. SC-005 open imported embeds in under 2 minutes.

**Constraints**: FR-004 secrets untracked. FR-005 accept-gate unchanged. FR-006–009 named-source art only, exact filename match. Constitution VI agent-shaped. Campaign of record stays at ai-co-dm until cutover (ADR 0002).

**Scale/Scope**: One table. One campaign of record path. Art only for files the ingested source already names.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — wiki, Work, Co-DM, prep, campaign of record (`ai-co-dm`). |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec exists with independently testable stories. |
| IV. Tests specify behavior | Pass — checks observe table reachability, staged wording, resolved embeds, missing-art reports. |
| V. Single context | Pass — no second bounded context. Path is `CONTEXT.md` `ai-co-dm`. |
| VI. Tools are agent-shaped | Pass — copy existing MCP config; ingest step in `wiki-ingest`; no GUI wrapper. |

**Post-design re-check**: still pass. Contracts are markdown gates. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/002-copy-foundry-config/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── foundry-connection.md
│   └── ingest-art.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
mcp.json                   # local copy of campaign-of-record Foundry MCP (gitignored)
foundry-data/              # symlink → Foundry Data (gitignored)
wiki/attachments/          # imported linked art
.agents/skills/wiki-ingest/SKILL.md
.agents/skills/foundry-stage/SKILL.md
.gitignore
CONTEXT.md                 # campaign of record path (do not duplicate)
```

**Structure Decision**: Keep skills + wiki. Do not add `src/` or a second Foundry world. Machine config stays local and ignored. Art lands in `wiki/attachments/` so Obsidian resolves `![[basename]]`.

## Complexity Tracking

> None. No constitution violations.
