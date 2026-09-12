# Research: Sequential Ingest Quality

## Decision: Sequential loop in `wiki-ingest`; delete parallel dispatch

**Rationale**: Named failure is overlapping files. Step 0 today fans `batch_count > 1` to parallel subagents; a later line says “one at a time.” Those conflict. The later line is the product. `cache-check` still skips unchanged. Folder size does not authorize overlap. No queue service.

**Alternatives considered**: Keep parallel batches of 15 (still overlaps files). Sequential groups of 15 (still overlaps inside a group). New orchestrator skill (split catch-all).

## Decision: Campaign kinds in AGENTS.md are the quality bar

**Rationale**: Spec ends the bootstrap period where ingested source layouts were exemplary. 006 already made jobs the pass/fail, not heading clone. `_raw/` illustrates jobs; it is not a clone target. Incoming files are evidence. Filed pages answer the kind’s jobs. Point at Layout; do not copy the job table into `wiki-ingest`.

**Alternatives considered**: Treat campaign-of-record dumps as gold format (the period that just ended). Freeze Old Gardens headings (violates 006 FR-001 and Constitution VII).

## Decision: Preserve stays for campaign-shaped session-prep and place; foreign sources map in

**Rationale**: 007/008 required treatments (session-prep body, place `[!narration]`) are internal kind jobs, not “the source is sacred.” If the source already matches the kind, file it with those treatments. If the source is foreign, map facts into the kind; do not photocopy the foreign outline. Do not reverse 008 narration.

**Alternatives considered**: Photocopy every incoming layout (violates FR-005). Distill places into concept pages (violates 008). Preserve all templates types now (scope).

## Decision: Per-file record is existing log + manifest, plus a batch report

**Rationale**: Completing a file already means `cache-update` and a `log.md` line. After a multi-file run, the Co-DM reports each file in order: complete/failed, pages, failure reason. No new file format. Failed file: close with reason, do not hash as success, then start the next.

**Alternatives considered**: New `_meta/ingest-runs.json` (extra store). Stop the whole batch on first failure (spec says remaining files still run). Parallel retry of the failed file (overlaps).

## Decision: History ingest follows the same rule; no extra rewrite this change

**Rationale**: Spec applies to every multi-file ingest path. This repo’s history-ingest skills do not currently fan files in parallel. State the rule in `wiki-ingest` (the catch-all). Do not retouch every history skill unless a later failure shows overlap.

**Alternatives considered**: Audit and rewrite all `*-history-ingest` skills in this change (no current parallel dispatch; token cost with no named failure in those files).

## Decision: Quickstart is the behavioral test; no heading linter

**Rationale**: Constitution IV — observe order and the page the DM opens. An AST linter on outlines would freeze headings and hit legacy.

**Alternatives considered**: pytest over markdown AST. A “no parallel” string test on SKILL.md (pins wording, not behavior).
