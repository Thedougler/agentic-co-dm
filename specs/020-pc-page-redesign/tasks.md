---

description: "Task list for the PC Page Redesign feature"
---

# Tasks: PC Page Redesign

**Input**: Design documents from `/specs/020-pc-page-redesign/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/pc-page.md`, and `quickstart.md`

**Tests**: No per-story TDD suite. The public seam is `specs/020-pc-page-redesign/fixtures/check.py` plus the scoped lint/manual checks in Polish. Independent acceptance scenarios live in `spec.md`.

**Organization**: Tasks are grouped by user story so each increment has a clear owner, dependency, and independent acceptance check.

**Existing files**: First-pass skill, template, five owners, CSS snippet, pointers, and fixture exist and still encode two column pairs and optional `Spells`. Implement MUST remorph those files against this list. Do not recreate from scratch. Do not add a PDF parser, database, Foundry client, `pc-design` skill, extra `type`, decorative PC theme, or visual clone of D&D Beyond chrome.

**Writer**: Design-impact remaining work is `wiki/templates/pc.md` and `.agents/skills/player-characters/SKILL.md`. `/speckit.implement` dispatches the designated writer per `docs/agents/skill-design-dispatch.md` with a scoped prompt (outcome, files, bounds, job) and `.agents/skills/writing-for-agents`. Session agent writes the fixture remorph, CSS snippet, `wiki/AGENTS.md`, pointer edits, and the five owner reconforms. Session agent MUST NOT write the skill or template while a designated writer is usable.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no incomplete dependencies)
- **[Story]**: Which user story this task belongs to (US1–US4)
- Include exact file paths in descriptions

## Path Conventions

- Skill: `.agents/skills/player-characters/SKILL.md`
- Template: `wiki/templates/pc.md`
- Live owners: `wiki/entities/pc/{jean-claude-tabarnack,perrin-black-jaw,catarina-davirelli,crissdalynn-khinriss,delmar-fisk}.md`
- Governing wiki: `wiki/AGENTS.md`
- Pointers: `.agents/skills/npc-design/SKILL.md`, `.agents/skills/pc-interview/SKILL.md`, `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`, `.agents/skills/obsidian-markdown/SKILL.md`, `.agents/skills/obsidian-markdown/references/COLUMNS.md`, `.agents/skills/session-beats/SKILL.md`, `.agents/skills/run-guide/SKILL.md`
- Contract: `specs/020-pc-page-redesign/contracts/pc-page.md`
- Fixture: `specs/020-pc-page-redesign/fixtures/check.py`
- CSS: `wiki/.obsidian/snippets/ttrpg-styles.css`, `wiki/.obsidian/snippets/wide-note-surface.css`, `wiki/.obsidian/snippets/pc-sheet.css`
- Archive evidence: `wiki/_archive/` (immutable; not a second live PC page)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Keep the existing argument-free feature checker; no new dependency or database.

- [X] T001 Keep the argument-free feature checker entrypoint in `specs/020-pc-page-redesign/fixtures/check.py`, using Python 3 with text/JSON-compatible output and a done-vs-failed exit code; do not expand `tools/check_wiki_pages.py` as PC proof

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Make the current page contract executable before template, skill, owner-page, or workflow remorphs.

**⚠️ CRITICAL**: No user story work begins until this phase is complete. The checker MUST fail the current two-column Ability Scores+Skills pair, optional `Spells`, and any live `[verify]`.

- [X] T002 Remorph observable PC contract assertions in `specs/020-pc-page-redesign/fixtures/check.py` for `wiki/templates/pc.md` and the five owners under `wiki/entities/pc/`: required frontmatter including `type` ("Exactly `pc`."), `cssclasses` ("Must include `pc-sheet` so PC-only CSS tweaks apply. Not a campaign fact."), `player` ("Player handle only; never real-player PII.") when live, `summary` ("One concise DM-readable sentence. Not a prescribed play pattern."); one H1; player-safe `> [!narration] Narration`; required H2 spine `Identity`, `Combat Stats`, `Ability Scores`, `Skills`, `Actions`, `Spells`, `Inventory`, `Features` then optional `Connections` / `Stated Goals` / `Session Log` / `Art`; `Spells` present on every page including non-casters and M…

**Checkpoint**: `specs/020-pc-page-redesign/fixtures/check.py` fails clearly on the current two-column sheet, optional `Spells`, and any live `[verify]`, and can pass the remorphed five-page set.

---

## Phase 3: User Story 1 - Reference any PC from one page (Priority: P1) 🎯 MVP

**Goal**: One predictable, player-safe, D&D Beyond-ordered PC scaffold the DM can scan: featured portrait beside Identity when art exists, Combat Stats full-width, then three columns (Ability Scores | Skills | Actions/Spells/Inventory/Features stacked), with required `Spells`.

**Independent Test**: Copy-start a scratch page from `wiki/templates/pc.md` and, without another page, locate player, class/level, AC, current/max HP, initiative, Actions, Spells, and Connections in D&D Beyond order in under 60 seconds. Confirm three `col-md` children after Combat Stats, required `## Spells`, and no `Voice` / `At a Glance` / `Sheet` / `Combat Profile` / `Abilities` / DM thesis / `[verify]`.

### Implementation for User Story 1

- [ ] T003 [US1] Dispatch the designated writer per `docs/agents/skill-design-dispatch.md` to remorph `wiki/templates/pc.md` against `specs/020-pc-page-redesign/contracts/pc-page.md`; instruct the writer to follow `.agents/skills/writing-for-agents`; session agent does not write that file. Outcome: copy-start scaffold with required frontmatter `title` ("Display name; may contain spaces/apostrophes."), `category` (`entities`), `tags` ("Existing campaign/type tags; preserve them."), `sources` ("All evidence supporting the page, including archived satellites and ingest sources; preserve lineage."), `created` / `updated`, `type` ("Exactly `pc`."), `lifecycle`, `reveal`, `campaign` / `visibility`, `summary` ("One concise DM-readable sentence. Not a prescribed play pattern."), `player` ("Player handle only; never real-player PII."), `class_levels` ("Human-readable single- or multiclass levels.") when known, `level` / `ac` / `hp_max` / `init_mod` / `pp` ("Scalar identity/reference values. Unknown values are omitted, not invented.") when known, `speed` ("Walk and conditional movement as a string.") when known, `status` ("Existing character status; do not infer a change.") when known, `cssclasses` ("Must include `pc-sheet` so PC-only CSS tweaks apply. Not a campaign fact."), optional `aliases` / `foundry_id` / `provenance` / `base_confidence` / `tier` / `lifecycle_changed` ("Preserve when present; omit when absent."); after `[!narration]`, featured portrait + `## Identity` pair when art exists; `## Combat Stats` full-width; then one parent `col` with three `col-md` children Ability Scores | Skills | Actions/Spells/Inventory/Features stacked; `## Spells` always present (state none when no casting; omit empty subsections); campaign extras `Connections`, conditional `Stated Goals`, `Session Log`, leftover `Art`; omit empty optional campaign sections; no Identity+Combat Stats pair; no two-child Ability+Skills-only sheet row; no `[verify]`, user questions, or superseded numbers; no decorative chrome
  Deferred: Claude Code usage limit until 2026-09-14 20:10 America/Vancouver. Codex fallback because remaining work is blocked and retry is more than one hour away.
- [X] T004 [P] [US1] Using `.agents/skills/obsidian-layout-adjustment/SKILL.md`, remorph PC-page scan tweaks in `wiki/.obsidian/snippets/pc-sheet.css` scoped to `.pc-sheet` (featured-portrait size, three-column sheet widths, heading density); keep vault-wide defaults in `wiki/.obsidian/snippets/ttrpg-styles.css` and `wiki/.obsidian/snippets/wide-note-surface.css`; MUST NOT add a distinct decorative theme, cards, site colors, or D&D Beyond chrome; MUST NOT use markdown `flexGrow` unless CSS cannot set column widths

**Checkpoint**: A new PC copied from `wiki/templates/pc.md` is one three-column D&D Beyond-ordered reference surface with required `Spells`. The fixture still fails live owners until User Story 3.

---

## Phase 4: User Story 2 - Record predictable PC pages (Priority: P2)

**Goal**: Agents record player-created characters from supplied source through one PC-owning skill. They do not invent a PC, generate stats, prescribe actions, print `[verify]`, or route through npc-design.

**Independent Test**: Give an agent `.agents/skills/player-characters/SKILL.md`, `wiki/templates/pc.md`, `wiki/AGENTS.md`, `specs/020-pc-page-redesign/contracts/pc-page.md`, and a representative supplied source (PDF, prose, or Foundry actor). Confirm it transcribes a complete `type: pc` page with stable headings including required `Spells`, valid frontmatter, correct wikilinks, no satellite dump, no invented stats, and no prescribed actions; with no source, or a request to invent/generate/prescribe, it refuses and does not mint a page.

### Implementation for User Story 2

- [ ] T005 [US2] Dispatch the designated writer per `docs/agents/skill-design-dispatch.md` to remorph `.agents/skills/player-characters/SKILL.md`; instruct the writer to follow `.agents/skills/writing-for-agents`; session agent does not write that file. Outcome: `player-characters` is the sole skill owner for `type: pc`; name is `player-characters` not `pc-design`; point at `specs/020-pc-page-redesign/contracts/pc-page.md` instead of cloning it; state idle → record ("source supplied for a player-created character") → refresh-goals ("post-session transcript for a player who was in that session") → refuse ("no source, or a request to invent/generate/prescribe, or inventing goals"); MAY file `wiki/entities/pc/<kebab-slug>.md` by transcribing supplied source only; MUST accept PDF character sheets, prose descriptions, Foundry VTT via existing MCP (`get-character`, `list-characters`, `get-character-entity`, related character tools), and other DM-supplied files; newest supplied source overwrites a conflicting wiki number in place (body home and matching frontmatter mirror); structure-only conformance is not a newer source; one source that internally disagrees: omit the contested number from the live page and file a GitHub issue; do not write `[verify]` or a user question; unreadable source: transcribe what can be read, omit unread numbers, do not abort a usable partial page; required `Spells` (state none when no casting); three-column sheet; featured portrait + Identity when pictures exist; leftover pictures only in `## Art`; Stated Goals lists only transcript-supported player statements (IC or OOC), session summary is backup only, omit when none, refresh after sessions that included that player, drop a goal only if the player said it is done or abandoned; MUST NOT invent a PC, generate stats, or write the player's actions
- [ ] T006 [P] [US2] Update the PC layout row in `wiki/AGENTS.md`: live owner `wiki/entities/pc/` with `type: pc`; copy `wiki/templates/pc.md`; jobs are the D&D Beyond spine (featured portrait + Identity when art exists, Combat Stats full-width, three-column sheet Ability Scores | Skills | Actions/Spells/Inventory/Features stacked, required Spells, Connections, conditional Stated Goals, Session Log, leftover Art); `cssclasses` must include `pc-sheet`; no Voice / At a Glance / Sheet / Combat Profile / Abilities / required DM thesis / live `[verify]`; player controls the PC; omit empty optional campaign sections; flatten satellites; structure-only conformance does not change `lifecycle` ("Existing value; structure-only conformance does not change it.") / `reveal` ("Existing value; structure-only conformance does not change it.") / `visibility` / campaign facts; wiki-kind route "Write, edit, or create a named PC page" → `player-characters`
- [ ] T007 [P] [US2] Update `.agents/skills/npc-design/SKILL.md` so player-character builds remain a hard stop that routes to `player-characters`; npc-design MUST NOT create, rewrite, or prescribe `type: pc` pages; remove any leftover optional-Spells or two-column PC path

**Checkpoint**: The skill, template, npc-design exclusion, and governing wiki instructions tell an agent how to record a PC from source, when to overwrite, when to omit, and when to refuse.

---

## Phase 5: User Story 3 - Conform the current party without losing canon (Priority: P3)

**Goal**: Bring the five live PC owners onto the remorphed contract (three-column sheet, required `Spells`, no live `[verify]`) while preserving campaign facts, source lineage, links, aliases, art, lifecycle, reveal, visibility, campaign, and player handles.

**Independent Test**: Compare each conformed owner with its pre-change page and applicable `wiki/_archive/` satellites. Confirm the shared spine including required `Spells`, every previously supported fact is inline or an owner link (contested single-source numbers omitted and tracked as a GitHub issue, not `[verify]`), no competing live satellite dump, and no changed campaign state.

### Implementation for User Story 3

- [ ] T008 [P] [US3] Remorph `wiki/entities/pc/jean-claude-tabarnack.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md`: set `cssclasses` ("Must include `pc-sheet` so PC-only CSS tweaks apply. Not a campaign fact."); pair one featured portrait with Identity when pictures exist; leftover pictures only in `## Art`; three-column sheet after Combat Stats; keep `## Spells` with this character's casting; add `## Stated Goals` only for transcript-supported player statements (in or out of character) citing session; omit Stated Goals and Art when empty; flatten applicable archive facts into canonical homes; preserve `tags` ("Existing campaign/type tags; preserve them."), `sources` lineage ("All evidence supporting the page, including archived satellites and ingest sources; preserve lineage."), `lifecycle` ("Existing value; structure-only conformance does not change it."), `reveal` ("Existing value; structure-only conformance does not change it."), `campaign` / `visibility`, aliases ("Preserve when present; omit when absent."), art, player handle ("Player handle only; never real-player PII."), and `status` ("Existing character status; do not infer a change."); do not overwrite numbers (structure-only is not a newer source); omit internally contested numbers from the live page and file a GitHub issue; do not print `[verify]`; omit empty optional sections; keep multiclass/resource pools distinct; preserve existing `[!secret]` callouts outside narration
- [ ] T009 [P] [US3] Remorph `wiki/entities/pc/perrin-black-jaw.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same `cssclasses`, three-column sheet, required `Spells`, portrait/Art, Stated Goals, preservation, omission, and no-`[verify]` rules as T008
- [ ] T010 [P] [US3] Remorph `wiki/entities/pc/catarina-davirelli.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same rules as T008; keep caster pools in `Spells` without duplicating Combat Stats numbers
- [ ] T011 [P] [US3] Remorph `wiki/entities/pc/crissdalynn-khinriss.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same rules as T008
- [ ] T012 [P] [US3] Remorph `wiki/entities/pc/delmar-fisk.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same rules as T008; `## Spells` MUST remain and MUST state that the character has no spells rather than omitting the heading

**Checkpoint**: All five live owners share the remorphed contract, retain canon, include required `Spells`, contain no live `[verify]`, and contain no second live PC facet representation.

---

## Phase 6: User Story 4 - Maintain the standard across PC workflows (Priority: P4)

**Goal**: Interview, ingest, reconciliation, Markdown, and session-planning guidance point at one PC contract and `player-characters`. They do not reintroduce satellite dumps, two-column sheets, optional `Spells`, live `[verify]`, or NPC treatment of PCs.

**Independent Test**: Trace `.agents/skills/player-characters/SKILL.md`, `.agents/skills/pc-interview/SKILL.md`, `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`, `.agents/skills/obsidian-markdown/SKILL.md`, `.agents/skills/obsidian-markdown/references/COLUMNS.md`, `.agents/skills/npc-design/SKILL.md`, `.agents/skills/session-beats/SKILL.md`, `.agents/skills/run-guide/SKILL.md`, and `wiki/AGENTS.md`. Confirm one template, one skill owner, no npc-design PC path, required `Spells`, three-column sheet, and the same frontmatter/section/omission rules.

### Implementation for User Story 4

- [ ] T013 [P] [US4] Update `.agents/skills/obsidian-markdown/references/COLUMNS.md` PC owner-page section: header pair is featured portrait + Identity when art exists; Combat Stats full-width; sheet row is three nested `col-md` children (Ability Scores | Skills | Actions/Spells/Inventory/Features stacked); longer parent fence; headings/tables as linear fallback; narration outside fences; prohibition on `[!col]` for these PC rows; full-width Connections / Stated Goals / Session Log / Art; do not pair Identity with Combat Stats; do not keep Actions/Spells/Inventory/Features full-width; column widths are CSS (`pc-sheet.css`), not markdown `flexGrow` unless CSS cannot
- [ ] T014 [P] [US4] Update `.agents/skills/pc-interview/SKILL.md` to map stated answers into D&D Beyond sections on `wiki/templates/pc.md` at `wiki/entities/pc/`; route page writes through `player-characters`; treat the interview transcript as evidence, not a live facet; leave unknown mechanics unknown; never invent combat math, player choices, or `[verify]` prompts
- [ ] T015 [P] [US4] Update `.agents/skills/wiki-ingest/SKILL.md` so `type: pc` ingest points at `player-characters` and `wiki/templates/pc.md`, files `wiki/entities/pc/<kebab-slug>.md`, flattens archived satellites, preserves `sources` lineage, overwrites conflicting numbers when the ingest is a newer supplied source, omits internally contested numbers instead of printing `[verify]`, and does not duplicate `specs/020-pc-page-redesign/contracts/pc-page.md`
- [ ] T016 [P] [US4] Update `.agents/skills/reconciling-session-evidence/SKILL.md` so durable PC changes and post-session Stated Goals refresh for PCs who were in that session route through `player-characters`; do not invent goals; do not refresh a PC who was not in the session; preserve `lifecycle` / `reveal` / `visibility`; avoid satellite dumps, invented conflict resolutions, and live `[verify]`
- [ ] T017 [P] [US4] Update `.agents/skills/obsidian-markdown/SKILL.md` so the campaign `type` enum includes `pc`; keep wikilink and escaped-pipe (`\|`) table-cell rules, complete-sentence DM prose, player-safe narration, inline-code DC/dice, real newlines, and omission rules; point at `COLUMNS.md` for the three-column PC sheet without weakening the session/run rule that narration stays outside fences
- [ ] T018 [P] [US4] Update `.agents/skills/session-beats/SKILL.md` so session planning that includes a player MUST read that PC's `## Stated Goals` when present and MUST NOT write the PC owner page
- [ ] T019 [P] [US4] Update `.agents/skills/run-guide/SKILL.md` so a run guide that includes a player MUST read that PC's `## Stated Goals` when present and MUST NOT write the PC owner page

**Checkpoint**: PC interview, ingest, reconciliation, Markdown, and planning workflows converge on the remorphed template and skill and do not reintroduce obsolete two-column or optional-Spells paths.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Prove the quickstart: fixture, lint, routing, Reading view, preservation, representative recording, refuse-to-generate, Stated Goals, and CSS.

- [ ] T020 Run `.venv/bin/python specs/020-pc-page-redesign/fixtures/check.py` against `wiki/templates/pc.md`, `wiki/entities/pc/`, and applicable `wiki/_archive/` satellites; require exit `0`
- [ ] T021 [P] Run `./scripts/lint-wiki-write --path wiki/entities/pc` against all five conformed owners; require exit `0`
- [ ] T022 [P] Run `./scripts/lint-obsidian-markdown --strict --path wiki/entities/pc` against all five conformed owners; require exit `0`
- [ ] T023 Run `./scripts/wiki-lint --json` and confirm no HARD findings for PC paths, frontmatter, links, filenames, or duplicate H1/facet structure; do not use `tools/check_wiki_pages.py` as PC proof
- [ ] T024 Confirm `wiki/.obsidian/snippets/pc-sheet.css` exists and is scoped to `.pc-sheet`, vault snippets `wiki/.obsidian/snippets/ttrpg-styles.css` and `wiki/.obsidian/snippets/wide-note-surface.css` remain, and each live PC has `cssclasses` containing `pc-sheet`
- [ ] T025 Perform an Obsidian Reading-view review of `wiki/entities/pc/jean-claude-tabarnack.md`, `wiki/entities/pc/perrin-black-jaw.md`, `wiki/entities/pc/catarina-davirelli.md`, `wiki/entities/pc/crissdalynn-khinriss.md`, and `wiki/entities/pc/delmar-fisk.md`: full-width player-safe narration; featured portrait beside Identity when art exists; Combat Stats full-width; three columns Ability Scores | Skills | Actions/Spells/Inventory/Features stacked; every page has `## Spells` (Delmar Fisk states none); vault CSS plus PC scan tweaks without a decorative theme; Stated Goals only when transcript-supported; leftover Art only at the bottom; no Voice / At a Glance / Sheet / Combat Profile / Abilities / empty optional heading / second H1 / required DM thesis / `[verify]` / live satellite dump; headings and tables remain understandable with columns unavailable
- [ ] T026 Perform the timed DM-reference review (under 60 seconds per page for player, class/level, AC, current/max HP, initiative, signature options, a named connection, a decision-relevant pressure, and any Stated Goals) and the structure-only preservation comparison of `wiki/entities/pc/` against pre-change copies and `wiki/_archive/{abilities,character-sheets,combat-profile,galleries,inventory,session-logs,spells,stats,va-scripts}/`
- [ ] T027 Using only `player-characters`, `wiki/templates/pc.md`, `specs/020-pc-page-redesign/contracts/pc-page.md`, and representative supplied source, produce temporary scratch outputs for a caster with multiple casting pools, a non-caster whose `## Spells` heading states none, and a multiclass PC with distinct class/resource pools; each must use the same frontmatter and heading contract including `Spells`, omit empty campaign extras, leave unknowns uninvented, keep narration safe, and pass scoped lint before scratch files are removed. Confirm the negatives in `.agents/skills/player-characters/SKILL.md`: no source / invent PC / generate stats / write actions / invent goals → refuse and do not mint a page; summary-only goal is not filed; a session that did not include the player does not refresh that PC's Stated Goals

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in priority order (P1 → P2 → P3 → P4)
  - US3 depends on the remorphed US1 template
  - US2 skill dispatch depends on the US1 template so the skill can point at it
  - US4 pointer edits can start after US2 skill/wiki-kind row exist
- **Polish (Phase 7)**: Depends on all desired user stories being complete; T020 before treating the remorphed contract as complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) — No dependencies on other stories
- **User Story 2 (P2)**: Can start after US1 template (T003) so the skill points at the remorphed scaffold
- **User Story 3 (P3)**: Can start after US1 template (T003); five owner files are independent of one another
- **User Story 4 (P4)**: Can start after US2 skill/wiki-kind row (T005–T006); workflow files are independent of US3

### Within Each User Story

- Tests (fixture) MUST fail the current two-column / optional-Spells shape before remorph
- User Story 1: designated-writer template, then CSS snippet on a different file
- User Story 2: designated-writer skill, then `wiki/AGENTS.md` and npc-design
- User Story 3: preserve metadata; then three-column sheet, required `Spells`, no `[verify]`
- User Story 4: point each workflow at the contract; do not copy the contract into every skill
- Story complete before moving to next priority unless parallel staffing allows

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- T003 and T004 after T002 (template vs CSS snippet)
- T006 and T007 after T005 (wiki-kind row vs npc-design)
- T008–T012 after T003 (five owner files)
- T013–T019 after T005–T006 (seven guidance files)
- T021 and T022 after source edits; T020 before claiming the remorphed contract complete

---

## Parallel Example: User Story 1

```text
Task: "Dispatch designated writer to remorph wiki/templates/pc.md"
Task: "Remorph wiki/.obsidian/snippets/pc-sheet.css for three-column widths"
```

## Parallel Example: User Story 3

```text
Task: "Remorph wiki/entities/pc/jean-claude-tabarnack.md"
Task: "Remorph wiki/entities/pc/perrin-black-jaw.md"
Task: "Remorph wiki/entities/pc/catarina-davirelli.md"
Task: "Remorph wiki/entities/pc/crissdalynn-khinriss.md"
Task: "Remorph wiki/entities/pc/delmar-fisk.md"
```

## Parallel Example: User Story 4

```text
Task: "Update .agents/skills/obsidian-markdown/references/COLUMNS.md"
Task: "Update .agents/skills/pc-interview/SKILL.md"
Task: "Update .agents/skills/wiki-ingest/SKILL.md"
Task: "Update .agents/skills/reconciling-session-evidence/SKILL.md"
Task: "Update .agents/skills/obsidian-markdown/SKILL.md"
Task: "Update .agents/skills/session-beats/SKILL.md"
Task: "Update .agents/skills/run-guide/SKILL.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL — blocks all stories)
3. Complete Phase 3: User Story 1 (template + CSS)
4. **STOP and VALIDATE**: Copy-start from `wiki/templates/pc.md` independently
5. Demo the three-column scaffold if ready

### Incremental Delivery

1. Complete Setup + Foundational → Fixture fails the old two-column / optional-Spells shape
2. Add User Story 1 → Test independently → Demo (MVP!)
3. Add User Story 2 → Test independently → Demo record/refuse
4. Add User Story 3 → Test independently → Demo five live owners
5. Add User Story 4 → Test independently → Demo workflow pointers
6. Polish → Run `quickstart.md`
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Designated writer: User Story 1 template, then User Story 2 skill
   - Session agent: CSS snippet, wiki-kind row, npc-design, five owners, pointer files
3. Stories complete and integrate independently except US3 needing the US1 template

---

## Notes

- [P] tasks = different files, no incomplete dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify the fixture fails the current two-column / optional-Spells shape before remorphing pages
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same-file conflicts, recreating first-pass files from scratch, reintroducing `[verify]` on live pages
