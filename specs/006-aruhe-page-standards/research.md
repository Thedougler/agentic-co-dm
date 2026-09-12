# Research: Sample Content Guidance

## Decision: `wiki/AGENTS.md` Layout is the one source of truth

**Rationale**: Co-DM already must load `$OBSIDIAN_VAULT_PATH/AGENTS.md` before every wiki write. Putting run-jobs there (not a new skill, not a second “standards” page) is the smallest change that every writer hits. `writing-for-agents`: one source of truth.

**Alternatives considered**: New `sample-design` skill (extra trigger surface). New `wiki/templates/README.md` (easy to skip). Spec `003` contracts as the NPC-only freeze (conflicts with FR-001).

## Decision: Samples illustrate; templates scaffold; jobs pass

**Rationale**: Spec forbids frozen heading lists and named clone targets. Current Layout “Done when: the filed note matches the template headings in that order” is the defect. Templates stay as copy-start with omit-if-empty. `_raw/` stays as quality evidence. Pass/fail is: spoken look + run questions for the kind, no empty sections, numbers on one owner.

**Alternatives considered**: Delete templates (agents need a copy-start). Keep “match Old Gardens / Hinewai order” (user rejected gold standards). Require `col` or forbid `col` on creatures (density choice, not a type).

## Decision: Point existing skills at jobs; do not add a skill

**Rationale**: `copy-writer`, `place-design`, `npc-design`, `homebrew-monsters-5e`, `dnd-5e-magic-item-design`, `wiki-ingest`, and `obsidian-markdown` already author these kinds. They currently name `_raw/` files as layout source and heading order as done-when. Replace those sentences with a pointer to AGENTS.md jobs plus “illustrative, not clone.” `003` band names (landmark/skirmish/patron/contact) remain useful density examples, not required classes.

**Alternatives considered**: Rewrite every skill’s body shape in duplicate (drifts). Leave skills as clone lists and only change AGENTS.md (skills would override).

## Decision: No scanner; no legacy touch; no `_raw/` rewrite

**Rationale**: A lint that scores heading order would punish legacy and re-freeze gold outlines (FR-001, SC-006). `_raw/` samples already demonstrate the jobs; rewriting them to a new outline is clone-thinking. Wrapup of a legacy page must not convert it.

**Alternatives considered**: Wiki-lint rule on `wiki/entities/` (hits non-samples). “Promote `_raw/` into entities as the standard” (out of scope; accept-gate still binds).

## Decision: Keep the closed campaign type set; map early sample labels on file

**Rationale**: `wiki/AGENTS.md` already forbids inventing `type` values. Sample frontmatter `location` / `monster` / `lore` maps to `place` / `creature` / `item` when a page is filed. Consumable and flora hazard share `item`; they differ by run questions, not a new type.

**Alternatives considered**: Add `type: hazard` or `type: monster` (violates closed set). Force all items onto one run-question list (consumable vs hazard are different jobs).

## Decision: Quickstart is the behavioral test

**Rationale**: Constitution IV — observe the page the DM opens. Author thin samples (or score existing `_raw/` as illustrations) for jobs, empty headings, spoken-look leaks, owner uniqueness. No fixture suite.

**Alternatives considered**: pytest over markdown AST (implementation-coupled). Visual Obsidian screenshots (not agent-shaped as the primary gate).
