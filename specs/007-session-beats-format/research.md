# Research: Session Beat Format

## Decision: `run-guide` owns the beat cockpit; Session 11 is evidence

**Rationale**: `run-guide` already documents the Session 11 column catalog (Scene ends when / At a Glance, Now, action cards, Initial Narration, procedure, zones, Be ready for, clock, How the Scene Resolves, roster, backup, battlemap). Duplicating that table into `wiki/AGENTS.md` or `session-beats` fails Constitution IX. Change `run-guide` from “catalog, fill only what you need” to “Session 11 job order is required; omit a section only when that job is absent.” Point at `_raw/Session-11-01-Angry-Birds.md` (and peers) as quality evidence, not clone targets.

**Alternatives considered**: New `session-format` skill (extra trigger). Freeze Angry Birds headings as the only valid outline (violates FR-001 photocopy ban and VII). Leave run-guide lean-optional (new beats would drift).

## Decision: `session-beats` owns composition and the filed spine

**Rationale**: Pacing, polarity, threads, and recompute already live there. The Session 11 spine (`Session-11-00-Birds-of-a-Feather.md`) is a different page kind: length, prize, opposition, dramatic spine, numbered skeleton, per-beat purpose / table sees / truth / pressure / if they break / landing. Add those filed-spine jobs to `session-beats` (short, pointer to the evidence file). Keep `session-skeleton.md` as the *planning* form; the filed spine is what the DM opens. Do not turn the spine into a tenth cockpit (FR-009).

**Alternatives considered**: Put spine jobs on `run-guide` (wrong skill; run-guide is one beat). Replace skeleton with the filed spine (loses candidate pools). Merge spine into beat 1 (Session 11 split them for a reason).

## Decision: Preserve-and-file ingest, not a new ingest skill

**Rationale**: Named failure is `wiki-ingest` distilling session-prep into concept pages. One branch in `wiki-ingest`: if the source is `type: session-prep` (beat or spine) or a Session-N filename in that shape, copy body markdown treatments unchanged into `wiki/journal/sessions/<campaign>/<N>/`, keep the filename, do not compile. Ordinary sources stay on the distill path (FR-008). Companion notes with `type: encounter` that belong to that session file into the same folder without cockpit scoring.

**Alternatives considered**: New `session-ingest` skill (second ingest surface). Always distill then “restore layout” (lossy). Leave beats in `_raw/` forever (SC-007 fails).

## Decision: Folder home is `journal/sessions/<campaign-slug>/<session-number>/`

**Rationale**: Spec FR-015. `journal/` is the wiki’s time-bound tree. Campaign then number keeps two campaigns from sharing `11/`. Session 11 files to `wiki/journal/sessions/shattered-sea/11/`. `session-wrapup` currently says `wiki/<slug>/sessions/` in its description — retarget that pointer to the same home so a later log MAY join the folder (spec edge case). Do not mint `wiki/shattered-sea/` as a second root.

**Alternatives considered**: `wiki/<slug>/sessions/` (conflicts with llm-wiki category folders). Flat `wiki/journal/` (today’s recap dump; DM hunts). Keep `_raw/` as the only home (staging, not the product).

## Decision: Filenames stay Session 11 pattern; `_raw/` evidence is not rewritten

**Rationale**: `Session-<N>-00-<Spine-Title>`, `Session-<N>-<BB>-<Label>` with two-digit beat numbers. Companion notes must not consume a live beat number. `_raw/Session-11-*.md` stay as format evidence (006 pattern: do not restyle gold files). Ingest files copies into the session folder; DM runs from journal, not `_raw/`. Older session-prep and `wiki/journal/Session 0N - Recap.md` are untouched (FR-013).

**Alternatives considered**: Rename to unprefixed `01-angry-birds.md` (breaks identity with skeleton). Move `_raw/` files on ingest and lose the evidence set. Bulk-convert recaps into the new tree (out of scope).

## Decision: Add `session-prep` to the wiki AGENTS closed type set

**Rationale**: Session 11 and `run-guide` already use `type: session-prep`. `wiki/AGENTS.md` currently omits it (`session` / `recap` / `work` only). `obsidian-markdown` PROPERTIES still lists `session-prep`. Align AGENTS to the type already in production rather than mapping session-prep → session (that type is the post-play log).

**Alternatives considered**: Map session-prep to `type: session` (collides with wrapup logs). Invent `type: beat` (closed-set violation).

## Decision: One omit-if-empty beat template; no second format skill

**Rationale**: `wiki/templates/session-prep.md` is a copy-start of the cockpit spine with omit-empty, matching 006. `wiki/templates/session.md` stays the log. No spine template file if `session-beats` plus the Session 11-00 evidence is enough to file a spine. `copy-writer` / `obsidian-markdown` already cover live session surfaces — pointer tweaks only.

**Alternatives considered**: Two templates (beat + spine) up front (spine is one page per session; evidence file is enough). No template (agents still need a copy-start for the cockpit).

## Decision: Quickstart plus existing skill evals; no heading linter

**Rationale**: Constitution IV — observe the page and folder the DM opens. A markdown-AST linter would freeze outlines and punish older sessions (FR-013, VII). Add eval cases on ingest-preserve and cockpit job order where those skills already have evals.

**Alternatives considered**: pytest over `.md` AST. wiki-lint rule on `wiki/journal/` (hits recaps).
