# Feature Specification: Agent-Shaped Wiki CLI

**Feature Branch**: `027-wiki-agent-cli`

**Created**: 2026-09-19

**Status**: Draft

**Input**: User description: "Make the agent lint/query/health surface thin, efficient, composable, predictable, and discoverable. One `wiki` command: lint, query, and health. Defaults that lint one file or the whole wiki. Bulk operations, cache of unchanged files so identical inputs do not re-run prose checkers, easy path scoping, agent-shaped structured output by default (no nested finding blobs agents must reduce by hand), full dump still available, `--pretty` for humans. Health covers lint plus wiki size, tokens, and existing maintenance stats. Runnable from anywhere using the configured vault."

## Clarifications

### Session 2026-09-19 (grill)

- Primary job is the **result contract**, then shorter invocation. Lint does **not** fuzzy-match or invent owners.
- One command with subcommands `lint`, `query`, and `health` (not three unrelated names).
- Vault comes from existing configuration (environment, nearest `.env`, global wiki config). Working directory does not matter. Path arguments are vault-relative. Unknown path fails closed. No fuzzy path matching.
- Default stdout is **agent-shaped**: one compact structured object, stable keys, no terminal detection. `--json` is accepted and ignored. `--pretty` is explicit human text.
- Lint runs **all** checkers including prose/Vale. Unchanged files reuse prior checker results. Adding, deleting, or renaming a page still refreshes corpus facts (links, missing owners) from cached per-file extracts plus the current file set.
- Default lint body is a **worklist** (status, counts, unique targets per rule, backlog, next page, cache stats, files checked, scope). Nested per-rule finding arrays are not default. One file argument includes that file’s findings with 1-based line numbers. `--full` restores the complete dump.
- Query defaults: retrieval enabled in agent environments, collection `wiki`, ten hits, compact fields title / path / retrieval id.
- Health **promotes** the existing Layer A maintenance report: live lint (same cache) plus page count, bytes, tokens, waste, staging leftovers, remorph plan counts, and policy, **plus compact trend aggregates** from existing sitting, efficiency, skill, and error trackers, plus ordered `focus` and a single `next` action. The old report invocation remains an alias of that one snapshot.
- Creative lint subcommands (`file`, `task`, `corpus`, `changed`, `rule`, `queue`, `template`, consolidate) stay on the existing lint script this sitting.
- Out of this feature: human-default output, TTY format forks, migrating the creative hydra, a second health counter, identity-resolution intelligence inside lint, inventing new vault folder trees.

### Session 2026-09-19

- Q: Should `wiki health` in this feature also surface trending session, context, and skill stats from the existing trackers (`sittings.jsonl`, efficiency traces, error ledger), or stay the current vault-fitness snapshot only? → A: Same snapshot as today (lint + pages/bytes/tokens + Layer A) plus compact trends from existing sitting/efficiency/skill/error trackers (compose; no second counter; no raw-trace dump).
- Q: Over what window should those compact health trends be computed? → A: All currently retained tracker records (existing efficiency retention; sittings and error ledger as stored; no new health-only window).
- Q: How should `wiki health` give agents concise, objective next actions (including file and folder structure fixes for context use) without turning into an essay? → A: Bounded structured `focus` items on the default object (and `--pretty`); layout fixes only from existing remorph/layout plans; no invented trees; no free-prose advice block.
- Q: Must `wiki health` be easy enough that small agents (Luna/Haiku class) can proactively, autonomously, and objectively improve the wiki? → A: Yes. Ordered `focus`, single `next` action, existing names only; instructions tell agents to run health and do `next` without extra interpretation or a DM wait.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Agent lints a path and gets a worklist (Priority: P1)

An agent needs to lint one owner page or a whole directory (for example `entities/npc`) without remembering vault roots, scope dialects, or extra flags. It receives one structured object it can load directly: counts, already-unique targets per rule, a backlog ordered for repair, the next page to touch, and cache stats. It does not write a follow-up script to flatten nested findings or unique missing-owner strings. When the argument is a single file, each finding includes a 1-based line.

**Why this priority**: This is the failure that burns sessions today. Shorter flags without this contract still dump an unusable blob.

**Independent Test**: Lint a directory of owner pages and a single page. Directory result has no findings arrays and includes unique targets plus `next_page`. Single-file result includes findings with line numbers. Unknown path exits with a structured error and does not scan the wiki.

**Acceptance Scenarios**:

1. **Given** a configured vault, **When** an agent runs `wiki lint entities/npc`, **Then** the command lints that prefix using all checkers and prints one compact worklist object (counts, unique targets, backlog, next page, cache, files checked, scope).
2. **Given** the same vault, **When** an agent runs `wiki lint entities/npc/some-page.md`, **Then** the object includes that page’s findings with 1-based `line` on each record (`rule`, `file`, `line`, `severity`, `message`).
3. **Given** a bulk run, **When** the agent omits `--full`, **Then** nested per-rule finding lists and per-file finding maps are absent.
4. **Given** `--full`, **When** lint completes with findings, **Then** the complete finding dump is present in addition to the worklist fields.
5. **Given** path `entities/npcs` when only `entities/npc` exists, **When** lint runs, **Then** it exits 2 with `status=error` and does not invent a nearby directory.

---

### User Story 2 - Unchanged pages skip repeated checker work (Priority: P1)

A second lint of the same wiki (or health, which lints live) must not re-run expensive per-file checkers on files whose content and checker configuration are unchanged. Corpus facts still reflect add/delete/rename.

**Why this priority**: Health is live full lint. Without this, every health or whole-wiki lint re-runs prose checkers on every page.

**Independent Test**: Lint twice with no file or checker-config changes; second run reports cache hits and does not re-invoke prose checkers for those files. Change one page; only that page and corpus aggregation miss the cache.

**Acceptance Scenarios**:

1. **Given** a completed lint, **When** the same paths are linted again with identical file contents and checker configuration, **Then** those files’ checker results are reused and `cache` reports hits / vale skipped.
2. **Given** a cached wiki, **When** one page’s content changes, **Then** that page is rechecked and corpus facts (links, missing owners) reflect the current file set.
3. **Given** `--no-vale` or `--no-template`, **When** lint runs, **Then** those checkers are skipped for this invocation without disabling the others.

---

### User Story 3 - Agent queries the wiki with one phrase (Priority: P2)

An agent asks `wiki query 'The Flat Water'` and gets compact hits (title, path, retrieval id) without unsetting environment variables, naming a collection, or setting a hit cap. Overrides exist for collection and hit count.

**Why this priority**: Retrieval is already possible but the invocation is easy to get wrong in agent environments, and the result is not a worklist.

**Independent Test**: Run a known-title query with no extra flags; hits include the three fields. Override hit count and confirm the cap.

**Acceptance Scenarios**:

1. **Given** a configured wiki collection, **When** an agent runs `wiki query 'The Flat Water'`, **Then** retrieval runs (including inside environments that would otherwise block it), uses collection `wiki`, returns at most ten hits, each with `title`, `path`, and retrieval id.
2. **Given** `--collection` or a hit-count override, **When** query runs, **Then** those values replace the defaults.
3. **Given** default output, **When** query succeeds, **Then** the result is one compact object (`status` plus hits), not scraped prose.

---

### User Story 4 - One health snapshot for wiki fitness (Priority: P2)

The DM or an agent runs `wiki health` and sees whether the wiki is fit **and how it is trending**, then takes one next action without decoding an essay: live lint totals (same cache as lint), page count, bytes, tokens, existing Layer A maintenance stats, compact trend aggregates from existing sitting/efficiency/skill/error trackers, ordered `focus` items (path or prefix, reason, source), and `next` (the first focus item, or null). Layout/file-structure items come only from existing remorph/layout plans. Small agents can act on `next` unaided.

**Why this priority**: Named as a new command; vault and sitting stats already exist and must surface here so even small agents can improve the wiki without a DM wait.

**Independent Test**: `wiki health` returns one object with inventory + lint + Layer A fields + compact trend aggregates + ordered `focus` + `next`. The previous maintenance-report invocation still works as an alias of the same snapshot. A small independent agent names `next.path` from the object alone.

**Acceptance Scenarios**:

1. **Given** a configured vault, **When** `wiki health` runs, **Then** it performs live lint (all checkers, same cache) and returns page count, bytes, tokens, lint counts, cache stats, Layer A maintenance stats, compact sitting/efficiency/skill/error trend aggregates, ordered `focus`, and `next` in one object.
2. **Given** the historical maintenance-report invocation, **When** it runs, **Then** it produces the same snapshot (alias), not a second set of numbers.
3. **Given** default output, **When** health completes, **Then** it does not print per-step essays, a full findings dump, raw sitting/trace records, or a free-prose advice block.
4. **Given** an existing remorph or layout plan and a lint backlog, **When** health completes, **Then** `focus` includes bounded items with path or prefix, reason, and source (`lint`, `remorph`, `layout`, or `tracker`), and does not invent folder trees that are not in those plans.
5. **Given** a non-empty `focus`, **When** a small agent (Luna/Haiku class) reads only the health object, **Then** it can name `next.path` and the matching `reason` without extra flags or a DM prompt.

---

### User Story 5 - Human pretty output on request (Priority: P3)

A human at a terminal passes `--pretty` and reads text: lint scoreboard and `file:line  RULE  message` when findings are in scope; query as one hit per line; health as a short scoreboard plus `next` and the `focus` list. Omitting `--pretty` never switches to text, even on an interactive terminal.

**Why this priority**: Operators need to read output; agents must not get text by accident.

**Independent Test**: Same lint with and without `--pretty` on an interactive terminal: default is compact structured output; `--pretty` is text.

**Acceptance Scenarios**:

1. **Given** an interactive terminal, **When** `wiki lint` runs without `--pretty`, **Then** stdout is one compact structured object.
2. **Given** `--pretty`, **When** lint/query/health run, **Then** stdout is human text as specified (scoreboard / one hit per line / health scoreboard plus the `focus` list). `--pretty --full` is the human findings list.
3. **Given** `--pretty` and a usage error, **When** the command fails, **Then** the error is one line on stderr and exit 2. Without `--pretty`, the error is a structured `status=error` object on stdout and exit 2.

---

### Edge Cases

- Zero path arguments: lint and health cover the whole configured vault.
- Several path arguments: union of those vault-relative files and prefixes.
- Path outside the vault or a missing file/prefix: exit 2, structured error, no scan.
- `--json` with or without other flags: same as default compact structured output (no-op).
- `--pretty` and `--full` together: human listing of findings, not indented structured text pretending to be human.
- Checker configuration (prose styles, structural rules) changes: prior per-file cache entries for those checkers are invalid.
- Retrieval backend missing or failing: query returns structured error, exit 2; it does not invent hits.
- Creative lint subcommands invoked via the new `wiki` command: out of scope this sitting; existing script remains the surface.
- `entities/npcs` vs `entities/npc`: not corrected; fail closed.
- Empty or missing sitting/efficiency/error trackers: health still succeeds; trend aggregates are empty/zero, not an error and not invented history.
- No remorph/layout plan: health omits invented structure items; other `focus` sources may still appear.
- Path arguments scope live lint, inventory, and `focus`; sitting/efficiency/error trend aggregates stay whole-tracker (those logs are not path-scoped).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The product MUST expose one `wiki` command with subcommands `lint`, `query`, and `health`.
- **FR-002**: The command MUST resolve the vault from existing configuration (environment variable, nearest `.env`, global wiki config) without requiring the working directory to be the vault or repository root.
- **FR-003**: Path arguments MUST be treated as vault-relative files or prefixes. Zero paths mean the whole vault. Unknown or out-of-vault paths MUST exit 2 without fuzzy matching.
- **FR-004**: Default stdout for every subcommand MUST be agent-shaped: exactly one compact structured object, stable keys, `status` present. No terminal detection. `--json` MUST be accepted and MUST NOT change default output.
- **FR-005**: Machine failures MUST print `{"status":"error","error":"<message>"}` (or equivalent compact object with those keys) on stdout and exit 2. They MUST NOT be prose-only.
- **FR-006**: Exit codes MUST be 0 = clean/success, 1 = findings present (lint/health when the wiki is not clean), 2 = bad invocation or precondition.
- **FR-007**: `wiki lint` MUST run every checker including prose/Vale and template conformance. `--hard` is the default finding class; `--all` includes soft. `--no-vale` and `--no-template` MUST remain overrides.
- **FR-008**: Lint MUST cache per-file checker results keyed by file content plus checker configuration. Identical inputs MUST reuse results. Add/delete/rename MUST refresh corpus facts from cached extracts plus the current file set.
- **FR-009**: Default lint objects MUST include `status`, `counts`, `hard_fail`, `unique` (already-deduped targets per rule), `backlog` (page, finding count, size), `next_page`, `cache` (hits, misses, vale skipped), `files_checked`, and `scope`. They MUST NOT include nested findings arrays or per-file finding maps unless FR-010 or FR-011 applies.
- **FR-010**: When the lint argument is exactly one existing file, default output MUST include a flat `findings` list of records with `rule`, `file`, `line` (1-based), `severity`, and `message`.
- **FR-011**: `--full` MUST add the complete finding dump while keeping worklist fields.
- **FR-012**: Lint MUST NOT guess, alias-match, or invent owners for missing-link targets.
- **FR-013**: `wiki query <phrase>` MUST run retrieval even when the process environment would otherwise block it, default collection `wiki`, default cap 10 hits, compact hit fields `title`, `path`, and retrieval id. Collection and hit cap MUST be overridable.
- **FR-014**: `wiki health` MUST produce one snapshot: live lint (FR-007, FR-008) plus page count, bytes, tokens, the existing Layer A maintenance stats (waste, staging leftovers, remorph plan counts, policy), compact trend aggregates composed from the existing sitting log (`sittings.jsonl`), efficiency traces, skill-usage fields on those records, and the error ledger, an ordered `focus` array (FR-019), and `next` (the first `focus` item or null). Trend aggregates MUST cover all currently retained tracker records (existing efficiency retention; sittings and error ledger as stored) and MUST NOT introduce a health-only time window. It MUST NOT emit a full findings dump, per-step essays, or raw tracker records by default. It MUST NOT invent a second health counter.
- **FR-015**: The existing Layer A maintenance-report invocation MUST remain an alias of `wiki health` (same snapshot, not a second counter).
- **FR-016**: `--pretty` MUST select human text: lint scoreboard (and `file:line  RULE  message` when findings are included); query one hit per line (`path  title  id`); health scoreboard plus `next` and the same `focus` list. `--pretty` plus `--full` is the human findings list. `--pretty` MUST NOT be implied by an interactive terminal.
- **FR-017**: Creative lint operations (`file`, `task`, `corpus`, `changed`, `rule`, `queue`, `template`, consolidate) MUST remain on the existing lint script for this feature. `wiki lint` is structural lint plus the worklist contract.
- **FR-018**: Agent instructions that tell agents how to lint, query, or health-check the wiki MUST be updated to this command, to the default worklist, and to: run `wiki health`, then act on `next` (then remaining `focus`) without terminal detection, extra interpretation, or waiting for the DM. This MUST be usable by small agents (Luna/Haiku class).
- **FR-019**: Default `wiki health` MUST include a bounded ordered `focus` array and `next`. Each `focus` item MUST have `path` (file or prefix), `reason` (one objective line using an existing rule, remorph/layout plan, or tracker name — no new jargon), and `source` (`lint` | `remorph` | `layout` | `tracker`). `next` MUST be `focus[0]` or null if `focus` is empty. Layout and file/folder-structure suggestions MUST come from existing remorph/layout plans. `focus` MUST NOT invent new vault trees, MUST NOT be free prose, and MUST be present (possibly empty) on the default object.

### Key Entities

- **Worklist**: Default lint object an agent acts on — counts, unique targets, backlog, next page, cache, scope — without a findings dump.
- **Finding record**: Flat diagnostic: rule, file, 1-based line, severity, message.
- **Checker cache**: Reuse of per-file checker results when file bytes and checker configuration are unchanged.
- **Health snapshot**: One inventory + lint + Layer A maintenance + compact operational-trend object, including ordered `focus` and `next`.
- **Focus item**: Bounded next action: vault-relative path or prefix, objective reason, source (`lint`, `remorph`, `layout`, `tracker`). `next` is the first item or null.
- **Query hit**: Title, vault-relative path, retrieval id.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: An agent lints a directory of owner pages with one invocation and uses the result without a follow-up script to unique targets or flatten nested findings.
- **SC-002**: Default bulk lint of a ~100-page prefix stays under 8 KB of stdout (worklist only). `--full` on the same prefix may be larger.
- **SC-003**: A second whole-wiki lint with no content or checker-config changes reports cache hits for previously checked pages and does not re-run prose checkers on those pages.
- **SC-004**: `wiki query` of a known in-wiki title, with no extra flags, returns at least one hit containing title, path, and retrieval id.
- **SC-005**: `wiki health` returns page count, byte size, token total, lint hard-total, compact sitting/efficiency/skill/error trend aggregates over all currently retained tracker records, ordered `focus`, and `next` in one invocation; the historical maintenance-report invocation returns the same snapshot.
- **SC-006**: On an interactive terminal, omitting `--pretty` still yields compact structured output; passing `--pretty` yields text a human can read without a decoder.
- **SC-007**: An unknown vault-relative path fails in under one second with a structured error and does not enumerate the wiki.
- **SC-008**: Independent agent given only this spec’s command examples lints one file and names the next backlog page from the worklist without being told to parse nested finding maps.
- **SC-009**: A small independent agent (Luna/Haiku class) given only this spec’s health object names `next.path` and its `reason` and would perform that action without extra interpretation, extra commands, or a DM wait.

## Assumptions

- Existing vault configuration and vault-resolution behavior are reused, not redesigned.
- Existing structural lint, template conformance, prose/Vale, identity scan, Layer A maintenance report, sitting log, efficiency-trace reports, error ledger, and retrieval backend are composed, not replaced. This feature changes the **command surface and default result contract**.
- Creative lint remains on the current lint script until a later feature.
- `--hard` default and `--all` for soft findings match current lint behavior.
- Retrieval hit cap uses the backend’s native count flag; the user-facing default is 10.
- Constitution VI asks for errors on stderr. This feature’s **default** machine errors are structured objects on stdout so agents have one stream to load (already the shared wiki-ops convention). `--pretty` errors go to stderr. That split is intentional.
- Agent-instruction updates (lint/query/health skills and standing wiki command examples) ship in the same change so agents do not keep copying the old invocation. Health instructions tell agents to run `wiki health` and do `next`.
- No new identity-resolution or owner-guessing behavior.
- Cache location and invalidation on checker-config change are planning details; behavior is FR-008.
- Trend window is existing tracker retention, not a new health policy. Empty trackers yield empty aggregates.
- Sitting/efficiency/error trends are whole-tracker even when path args scope lint/inventory/`focus`.
