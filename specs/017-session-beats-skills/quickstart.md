# Quickstart: Session Beat Skills

Prove the split by classifying jobs and checking isolation. Do not rewrite Session 11 to prove it.

## Prerequisites

- Branch `017-session-beats-skills`
- Spec [spec.md](./spec.md), contract [contracts/beat-skill-routing.md](./contracts/beat-skill-routing.md)
- `session-beats` is composition only (no five type-card catalogs in that skill)
- Type skills `hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats` exist
- `AGENTS.md` contains the routing table
- `.omp/AGENTS.md` does not copy that table
- `.agents/skills/writing-beats` unchanged
- Session 11 `_raw/` / wiki beat bodies unchanged

## 1. Classify the contract jobs (P1, SC-001)

Cover jobs 1–15 in the contract. A second reviewer names the primary skill without seeing the first list.

Expected: 100% agreement. Fail if planning a session is classified as a type skill. Fail if writing a Hook is classified as `session-beats`.

## 2. Chart without type catalogs (P1, SC-002)

Give a session-planning job and withhold the five type-card catalogs. Author produces a Beat Chart spine: one Hook, alternating middle, Climax then Resolution, polarity, budget, threads.

Fail if the author must open a type-card catalog to draw the chart. Fail if two same-type middle beats sit consecutively.

## 3. Typed beat without other catalogs (P1, SC-003, SC-007)

Give a job to write a Development (or another type) with no named seam. Withhold the other four type-card catalogs.

Expected: a Development by the completion test. Fail if another type's cards were required. Fail if the result is a Cliffhanger.

## 4. Named seams only (P2, SC-009)

Walk jobs 16–20. Extra skills load only as the contract names.

Fail if Play a Cliffhanger as Hook becomes a second Hook. Fail if a no-seam typed-beat job opens another catalog.

## 5. Chart rules still bind (P2, SC-004, SC-005, SC-010)

Audit a newly composed chart against contract chart rules 1–8.

Fail if polarity is wrong. Fail if a beat has only one viable response. Fail if the next slot is forced after the party breaks the chart.

## 6. Owners and leftovers (P3, SC-006, SC-007, SC-008)

- New live beat still reads as a Session 11 cockpit card (`run-guide`).
- Spine still does not duplicate Scene ends when / Zones / Be ready for.
- No skill contains both the full Beat Chart and all five type-card catalogs.
- `beat-types.md` is gone from `session-beats` or is not the standing load for composition.
- Zero Session 11 beat/spine bodies rewritten solely for this feature.
- `writing-beats` (article skill) untouched.

Pass: steps 1–6 hold. Fail any step → the blob is not split yet.
