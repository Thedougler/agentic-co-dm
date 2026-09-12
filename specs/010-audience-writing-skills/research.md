# Research: Audience Writing and Visual Skills

## Decision: `AGENTS.md` holds the one stack table

**Rationale**: This routing must fire on wiki writes, chat Work, agent-consumed docs, and picture jobs. `wiki/AGENTS.md` loads only on vault writes. `docs/agents/work.md` loads only before prep/wrapup output. `AGENTS.md` is always-loaded standing context. Six rows plus “they stack” is load-bearing (Constitution IX). `writing-for-agents`: one source of truth.

**Alternatives considered**: New `docs/agents/writing.md` (extra hop; easy to skip). New router skill (Constitution VII; router skills are for user-invoked skills, and these six are already model-invoked). Put the table only in `wiki/AGENTS.md` (misses non-wiki jobs). Duplicate the table in `.omp/AGENTS.md` (it already imports `AGENTS.md`).

## Decision: Skill descriptions are the per-branch triggers

**Rationale**: A skill `description` is the always-loaded pointer for that branch. Today `copy-writer` claims every wiki write and `[!narration]`; `writing-for-agents` only names skills and `AGENTS.md` / `CLAUDE.md`. Those pointers miss DM chat and agent-consumed specs, and they steal theatre of the mind. Rewrite descriptions so each branch is one trigger. Leave a description unchanged when it already matches.

**Alternatives considered**: Rewrite skill bodies to restate the table (duplication; suffocates). Rely on descriptions alone with no AGENTS.md table (composition — they stack — has no home).

## Decision: Point work.md and wiki/AGENTS.md; delete restated load lines

**Rationale**: `docs/agents/work.md` and `wiki/AGENTS.md` currently hardcode copy-writer plus obsidian-markdown on every vault write. That is a cache of two rows and omits theatre of the mind, writing-for-agents, and the visual pair. Craft skills already say “Follow `docs/agents/work.md`” and then restate the same load trio (~26 copies). Delete the restatement. Vault-specific outcomes stay: complete-sentence prose, spoken text as theatre of the mind.

**Alternatives considered**: Leave the 26 copies (sediment; drifts). Expand every copy into the full six-row table (token spike; Constitution IX fail).

## Decision: No seventh skill; no linter; no legacy touch

**Rationale**: The six authorities already exist. A classifier lint over `wiki/` would score legacy pages (FR-014, SC-007) and freeze implementation. Named failure is wrong voice on *new* jobs, prevented by the table plus triggers.

**Alternatives considered**: `audience-router` skill (extra trigger surface). Markdown lint for “which skill was loaded” (not observable; couples to internals). Rewrite `_raw/` or `legacy/` as proof (out of scope).

## Decision: Visual pair stays two jobs that stack

**Rationale**: Spec FR-016/FR-017. `visual-references` gathers look and does not place. `visual-aids` produces or places and does not replace the gather step when a known owner is depicted. Descriptions already say this. Do not merge them. Do not assign map rendering or spoken narration to visual-aids (FR-021).

**Alternatives considered**: One “art” skill (hides the gather/place split the spec names). Teach visual-aids to gather (duplicates visual-references).

## Decision: Quickstart is the behavioral test

**Rationale**: Constitution IV — observe classification of jobs, not whether a skill file contains a string. Contract lists ≥16 jobs. Two reviewers should name the same authorities (SC-001). Mixed wiki page and known-owner depiction prove stacking (SC-006, SC-008).

**Alternatives considered**: pytest over SKILL.md YAML (implementation-coupled). Require a live image-generation call in quickstart (not needed to prove routing).
