# Quickstart: Session Beat Skills

Prove the beat split by classifying jobs and checking isolation. Prove vehicle and spell kinds with one page each. Session 11 bodies stay as they are.

## Prerequisites

- Branch `017-session-beats-skills`
- Spec [spec.md](./spec.md), contracts [beat-skill-routing.md](./contracts/beat-skill-routing.md) and [wiki-kind-pages.md](./contracts/wiki-kind-pages.md)
- `session-beats` is composition only (no five type-card catalogs in that skill)
- Type skills `hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats` exist
- `spell-design` exists; `vehicle-design` fills the vehicle sheet
- `wiki/templates/vehicle.md` and `wiki/templates/spell.md` exist
- `wiki/AGENTS.md` lists `type: vehicle` and `type: spell` and Layout jobs
- `AGENTS.md` contains the beat routing table
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

## 7. Vehicle and spell pages (P2, SC-011–SC-014)

Give a job to create a named ship. Primary skill is `vehicle-design`. Page starts from `wiki/templates/vehicle.md` and includes narration, sheet, and hull/component figures a DM can run.

Give a job to create a spell. Primary skill is `spell-design`. Page starts from `wiki/templates/spell.md` and includes narration, classification, and a runnable 2024 effect.

Fail if the vehicle page has no sheet. Fail if the spell job is classified as `session-beats` or `dnd-5e-magic-item-design`.

## 8. Claude Code dispatch (SC-015, SC-016)

Claude Code runs only for a new skill or a major skill redesign. Those dispatches use `claude-opus-4-6 --effort medium`. The prompt names deliverables and a completion test. `AGENTS.md` and template installs are session-agent work.

Fail if those dispatches use the `opus` alias, default Opus, or `--effort high`. Fail if an `AGENTS.md`-only edit was sent to Claude Code. After a usage-limit stop, independent tasks still completed.

Pass: steps 1–8 hold.
