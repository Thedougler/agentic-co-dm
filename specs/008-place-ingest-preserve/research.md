# Research: Place Ingest Preserve

## Decision: Extend the existing preserve GUARD; do not add a skill

**Rationale**: `wiki-ingest` already has **Session-prep preserve** (007): copy body unchanged, do not distill. The named failure for places is the same distill path (Step 2–5 rewrite, llm-wiki template, dropped `[!narration]`). One GUARD that also matches `type: place` is the smallest change. A second ingest skill would split the catch-all and drift.

**Alternatives considered**: New `place-ingest` skill (extra trigger). Distill then “restore narration” (lossy). Leave places in `_raw/` forever (DM still hunts).

## Decision: File places to `wiki/entities/`; keep filename and body

**Rationale**: Campaign places already use `category: entities` and `type: place`. Preserve copies land next to other owner pages. Do not scatter into `concepts/`. Do not use the session folder. `_raw/` evidence (Old Gardens and peers) stays in `_raw/`; ingest files a copy, same as Session 11 evidence.

**Alternatives considered**: `wiki/places/` (second tree). Overwrite `_raw/` on promote (loses evidence). Map `location` → distill as concept (violates FR-001).

## Decision: Required narration is the open `[!narration]` Narration block

**Rationale**: `wiki/templates/place.md` and Aruhe place samples put spoken look in `> [!narration] Narration` under Overview. Spec FR-002: ingest must not delete, empty, or convert that block into ordinary prose. Empty stub on a thin place still stays (source had the heading). Player-safety (no secrets/DCs/unearned names) is already AGENTS.md / obsidian-markdown; ingest does not “fix” spoken look by stripping the callout.

**Alternatives considered**: Allow spoken look as unlabeled paragraphs (fails US1). Re-title to `[!narration] Initial Narration` to match beats (wrong surface; places use Narration).

## Decision: Jobs stay in AGENTS.md; ingest does not freeze Old Gardens headings

**Rationale**: 006 already made place run questions the pass/fail, not heading-order clone. This feature stops mutation; it does not re-freeze a named file. `wiki-ingest` points at AGENTS.md Layout + “keep source markdown treatments including `[!narration]`.” Omit empty stays.

**Alternatives considered**: Require exact Old Gardens heading list on every ingested place (violates 006 FR-001 and Constitution VII).

## Decision: Items, creatures, people, session-prep out of scope

**Rationale**: User named places. Session-prep already has preserve. Extending to every campaign type in the same change invites untested mutation. Add kinds later if the same failure shows up.

**Alternatives considered**: Preserve all `wiki/templates/` types now (scope creep).

## Decision: Quickstart is the behavioral test; no heading linter

**Rationale**: Constitution IV — observe the page the DM opens. An AST linter on heading order would freeze outlines and hit legacy (FR-010).

**Alternatives considered**: pytest over markdown AST. wiki-lint rule on `wiki/entities/` (hits non-samples).
