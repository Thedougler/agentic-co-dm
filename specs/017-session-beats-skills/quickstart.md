# Quickstart: Session Beat Skills

Prove the beat split by classifying jobs and checking isolation. Prove wiki kinds with one page each. Prove new session-prep pages use typed/session-plan drafts. Session 11 bodies stay as they are.

## Prerequisites

- Branch `017-session-beats-skills`
- Spec [spec.md](./spec.md), contracts [beat-skill-routing.md](./contracts/beat-skill-routing.md), [session-prep-pages.md](./contracts/session-prep-pages.md), and [wiki-kind-pages.md](./contracts/wiki-kind-pages.md)
- `session-beats` is composition only (no five type-card catalogs in that skill)
- Type skills `hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats` exist
- `spell-design`, `faction-design`, `lore-design`, `city-design`, `region-design` exist
- `vehicle-design` fills the vehicle sheet
- `narrative-islands` fills `wiki/templates/quest.md`; no `quest-design`
- `place-design` defers city and region jobs
- `faction-prep` is gone
- Wiki templates exist for vehicle, spell, faction, lore, quest, city, region
- Wiki templates exist for hook, development, cliffhanger, climax, resolution, session-plan
- `wiki/templates/session-prep.md` is not copy-start for new beats or plans
- `wiki/AGENTS.md` lists the kinds and Layout jobs, including session-prep `kind`
- `AGENTS.md` contains the beat routing table
- `.omp/AGENTS.md` does not copy that table
- `.agents/skills/writing-beats` unchanged
- Session 11 `_raw/` / wiki beat bodies unchanged

## 1. Classify the contract jobs (P1, SC-001)

Cover jobs 1–15 in the contract. A second reviewer names the primary skill without seeing the first list.

Expected: 100% agreement. Fail if planning a session is classified as a type skill. Fail if writing a Hook is classified as `session-beats`.

## 2. Chart without type catalogs (P1, SC-002, SC-033, SC-034)

Give a session-planning job and withhold the five type-card catalogs. Author produces a Beat Chart session plan from `wiki/templates/session-plan.md`: compass, beat map, floating beats, pressure, PC touchpoints, links to typed beat pages. `type: session-prep`, `kind: session-plan`. One Hook, alternating middle, Climax then Resolution, polarity, budget, threads.

Fail if the author must open a type-card catalog to draw the chart. Fail if two same-type middle beats sit consecutively. Fail if the page uses Session 11-00 heading order (length, prize, opposition, numbered skeleton as the run jobs). Fail if it duplicates Scene ends when, Zones, or Be ready for. Fail if `type` is `session-plan`, `beat`, or `session-beat`.

## 3. Typed beat without other catalogs (P1, SC-003, SC-007)

Give a job to write a Development (or another type) with no named seam. Withhold the other four type-card catalogs.

Expected: a Development by the completion test. Fail if another type's cards were required. Fail if the result is a Cliffhanger.

## 4. Named seams only (P2, SC-009)

Walk jobs 16–20. Extra skills load only as the contract names.

Fail if Play a Cliffhanger as Hook becomes a second Hook. Fail if a no-seam typed-beat job opens another catalog.

## 5. Chart rules still bind (P2, SC-004, SC-005, SC-010)

Audit a newly composed chart against contract chart rules 1–8.

Fail if polarity is wrong. Fail if a beat has only one viable response. Fail if the next slot is forced after the party breaks the chart.

## 6. Owners and leftovers (P1, SC-006, SC-007, SC-008, SC-034)

- New live beat starts from that type's draft template, presents that type's draft jobs, and is scannable as current wiki templates (columns where a dashboard pair shares the scan). Not Session 11 heading order.
- New live beat is `type: session-prep` with matching `kind`. Fail if `type` is `beat` or `session-beat`.
- `run-guide` did not rewrite the typed beat into a Session 11 cockpit.
- Session plan still does not duplicate Scene ends when / Zones / Be ready for.
- No skill contains both the full Beat Chart and all five type-card catalogs.
- `beat-types.md` is gone from `session-beats` or is not the standing load for composition.
- Zero Session 11 beat/spine bodies rewritten solely for this feature.
- `writing-beats` (article skill) untouched.
- Work was proposed in chat before any wiki write.

Pass: steps 1–6 hold. Fail any step → the blob is not split yet.

## 7. Vehicle and spell pages (P2, SC-011–SC-014)

Give a job to create a named ship. Primary skill is `vehicle-design`. Page starts from `wiki/templates/vehicle.md` and includes narration, sheet, and hull/component figures a DM can run.

Give a job to create a spell. Primary skill is `spell-design`. Page starts from `wiki/templates/spell.md` and includes narration, classification, and a runnable 2024 effect.

Fail if the vehicle page has no sheet. Fail if the spell job is classified as `session-beats` or `dnd-5e-magic-item-design`.

## 8. Faction, lore, quest (P2, SC-017–SC-028)

Faction: `faction-design` is primary. Page from `wiki/templates/faction.md` has the named jobs. Current Turn has no roll. Fail if `faction-prep` still loads.

Lore: `lore-design` is primary. Page from `wiki/templates/lore.md` answers one question and has At a Glance, Current Truth, At the Table. Fail if ingest remaps `lore` to `item`. Fail if an unwitnessed lore page is `canon`.

Quest: `narrative-islands` is primary. Page from `wiki/templates/quest.md` has summary, Situation, walk-away stakes, World in motion, two independent leads. Fail if a `quest-design` skill exists. Fail if a new durable situation is `type: front` or `type: encounter`.

## 9. City and region (P2, SC-029–SC-032)

City: start at `place-design` for a city; it defers to `city-design`. Page is `type: place` `kind: city` from `wiki/templates/city.md` with Arrival, pressure, districts, gazetteer, table rules, one if-nobody-intervenes situation.

Region: start at `place-design` for a region; it defers to `region-design`. Page is `type: region` from `wiki/templates/region.md` with look, current state, choosable routes, active powers, change log. Fail if the region invents a pressure that was not already stated. Fail if `type: front` is revived.

## 10. Claude Code dispatch (SC-015, SC-016)

Claude Code runs only for a new skill or a major skill redesign. Those dispatches use `claude-opus-4-6 --effort medium`. The prompt names deliverables and a completion test. `AGENTS.md` and template installs are session-agent work. After a usage-limit stop, independent tasks still completed and deferred jobs stay on `tasks.md` with a retry time. Codex CLI at ChatGPT 5.5 medium is allowed only when every remaining open task is blocked, no other work can be done, and that retry time is more than one hour away. Re-check those gates before each remaining blocked skill job. Session-agent last-resort write only when both Claude Code and Codex are usage-limited.

Fail if those dispatches use the `opus` alias, default Opus, or `--effort high`. Fail if an `AGENTS.md`-only edit was sent to Claude Code. Fail if Codex ran while other independent work remained, or while the retry time was within one hour, or without re-checking Claude Code first on a later job.

Pass: steps 1–10 hold.
