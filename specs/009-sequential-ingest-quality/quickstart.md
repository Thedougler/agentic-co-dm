# Quickstart: Sequential Ingest Quality

Prove multi-file ingest is sequential and filed pages match campaign kinds. Do not restyle `legacy/` or rewrite `_raw/` evidence bodies.

## Prerequisites

- Branch `009-sequential-ingest-quality`
- Spec [spec.md](./spec.md), contract [contracts/sequential-ingest.md](./contracts/sequential-ingest.md)
- `wiki-ingest` has no parallel file dispatch
- Kind jobs remain in `wiki/AGENTS.md` Layout

## 1. One file finishes first (P1, SC-001)

Three approved sources (or a dry-run of the skill text if filing is not approved). Watch ingest.

Fail if file 2 pages or tracking appear while file 1 is still open. Fail if Step 0 still dispatches parallel subagents for large folders.

## 2. Batched page matches solo ingest (P1, SC-002)

Compare one subject ingested alone vs as the third file in a sequential batch. Fail if the batched page is a different kind, missing spoken look, or missing that kind’s jobs.

## 3. Foreign source maps to the kind (P1, SC-003)

One source whose outline is not the campaign kind (for example a concept-style dump that names a place). After ingest, the wiki page answers place jobs (or the correct kind). Fail if the foreign outline is the page shape. Fail if a campaign-shaped place loses `[!narration]`.

## 4. Failed file then continue (P2, SC-005)

Three files; middle file unreadable. Report lists 1 complete, 2 failed with a reason, 3 complete. Fail if file 3 pages appear before file 2 is closed. Fail if the DM cannot read order, states, and page attribution from the report in under one minute.

## 5. Guidance retarget (SC-004)

Open `.agents/skills/wiki-ingest/SKILL.md` and `wiki/AGENTS.md`. Fail if ingest still tells the Co-DM to copy an incoming file’s layout as exemplary format. Fail if Layout jobs were duplicated into `wiki-ingest` instead of pointed at. Fail if `_raw/` is described as a clone target.

## 6. Legacy untouched

This change set does not rewrite `legacy/` or restyle historical pages solely to match campaign kinds.

Pass: steps 1–6 hold. Fail any step → ingest still overlaps files or treats source format as the bar.
