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
- Default whole-wiki and bulk lint output is a compact overview: aggregate counts, affected-page/finding totals, cache/scope metadata, and an actionable `next` recommendation. `next.path` is the smallest dirty file by byte size, with path as the tie-breaker. Detailed per-file findings are available only with `--full`; `--full` is the intentional escape hatch for the next page.
- Query defaults: retrieval enabled in agent environments, collection `wiki`, ten hits, compact fields title / path / retrieval id.
- Health **promotes** the existing Layer A maintenance report: live lint (same cache) plus page count, bytes, tokens, waste, staging leftovers, remorph plan counts, and policy, **plus compact trend aggregates** from existing sitting, efficiency, skill, and error trackers, plus ordered `focus` and a single `next` action. The old report invocation remains an alias of that one snapshot.
- Creative lint evaluator implementations remain behind the single `wiki lint` command this sitting. Their findings are part of the default result; evaluator-specific subcommands are implementation details, not agent instructions or alternate lint paths.
- Out of this feature: human-default output, TTY format forks, identity-resolution intelligence inside lint, inventing new vault folder trees, skill-eval pass/fail or missing-skill inventories (stay on skill-creator), npm/package.json wrappers (`wiki` is the command), and repair-plan authoring.

### Session 2026-09-19

- Q: Should `wiki health` in this feature also surface trending session, context, and skill stats from the existing trackers (`sittings.jsonl`, efficiency traces, error ledger), or stay the current vault-fitness snapshot only? → A: Same snapshot as today (lint + pages/bytes/tokens + Layer A) plus compact trends from existing sitting/efficiency/skill/error trackers (compose; no second counter; no raw-trace dump).
- Q: Over what window should those compact health trends be computed? → A: All currently retained tracker records (existing efficiency retention; sittings and error ledger as stored; no new health-only window).
- Q: How should `wiki health` give agents concise, objective next actions (including file and folder structure fixes for context use) without turning into an essay? → A: Bounded structured `focus` items on the default object (and `--pretty`); layout fixes only from existing remorph/layout plans; no invented trees; no free-prose advice block.
- Q: Must `wiki health` be easy enough that small agents (Luna/Haiku class) can proactively, autonomously, and objectively improve the wiki? → A: Yes. Ordered `focus`, single `next` action, existing names only; instructions tell agents to run health and do `next` without extra interpretation or a DM wait.
- Q: When an agent runs wiki lint on more than one path, what should the default output be? → A: Always dump every finding, grouped by file (complete Vale-included breakdown per file with 1-based line numbers; no worklist-only default).
- Q: How should wiki lint, query, and health record runtime so agents can see the slowest wiki operations in wiki health? → A: Time each wiki command on the existing efficiency tracker; health ranks slowest commands (one compact record per run: command, duration, cache hits/misses, exit; no raw traces; no second ledger).
- Q: Should wiki health this sitting also show skills that are missing or failing their evals, or stay on wiki/command fitness only? → A: Token-heaviest sittings only; skill evals out of this feature (health ranks slowest wiki commands and existing efficiency/token trends; skill pass/fail stays on skill-creator).
### Session 2026-09-20 (remediation)

- The single agent-facing `wiki` command also exposes approved typed mutations
  and repair-plan application. It resolves the configured vault internally and
  keeps every path vault-relative; bulk-operation scripts remain implementation
  details. Repair-plan authoring remains out of scope.
- A lint invocation with more than one explicit path always includes complete
  flat findings grouped by file; one-path and whole-wiki invocations retain the
  compact default and use `--full` for details.
- Q: Which findings may `wiki lint fix` change automatically? → A: Only explicitly registered fixers that are deterministic and idempotent; findings without such a fixer remain for manual repair.
- Q: After applying eligible fixes, should `wiki lint fix` rerun lint on the affected scope? → A: Yes; apply fixes, rerun lint on the affected scope, and return applied fixes plus remaining findings.
- Q: How should agent instructions expose `wiki lint fix`? → A: Run `wiki lint fix <next.path>` before `wiki lint <next.path> --full` so safe repairs happen before manual review.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Agent gets a compact lint worklist (Priority: P1)

An agent needs to lint one owner page, several named pages, or the whole wiki without loading every finding into context. It receives one structured overview with counts, affected-page/finding totals, cache metadata, and one actionable `next` recommendation. `next.path` is the smallest dirty file by byte size, then path. The agent can rerun that file with `--full` to read line-level findings.

**Independent Test**: Lint a directory, the whole wiki, and two named pages. Each default result stays compact, exposes aggregate issue counts, and selects the smallest dirty file. `--full` exposes complete findings for the selected scope. Unknown path exits with a structured error and does not scan the wiki.

**Acceptance Scenarios**:

1. **Given** a configured vault, **when** an agent runs `wiki lint`, the command lints the whole wiki using all checkers and returns one compact object with aggregate counts, affected-page/finding totals, cache/scope metadata, and `next`.
2. **Given** dirty files of different sizes, **when** lint completes, **then** `next.path` is the smallest dirty file; equal sizes use vault-relative path order.
3. **Given** a scoped lint of multiple files, **when** lint completes, **then** it returns the same compact overview plus complete flat findings grouped by file.
4. **Given** `--full` for a one-path lint, **when** lint completes, **then** output adds complete Vale-included findings grouped by file, with 1-based lines and flat finding records.
5. **Given** path `entities/npcs` when only `entities/npc` exists, **when** lint runs, **then** it exits 2 with `status=error` and does not invent a nearby directory.

---

### User Story 2 - Unchanged pages skip repeated checker work (Priority: P1)

A second lint of the same wiki (or health, which lints live) must not re-run expensive per-file checkers on files whose content and checker configuration are unchanged. Corpus facts still reflect add/delete/rename.

**Why this priority**: Health is live full lint. Without this, every health or whole-wiki lint re-runs prose checkers on every page.

**Independent Test**: Lint twice with no file or checker-config changes; second run reports cache hits and does not re-invoke prose checkers for those files. Change one page; only that page and corpus aggregation miss the cache.

**Acceptance Scenarios**:

1. **Given** a completed lint, **When** the same paths are linted again with identical file contents and checker configuration, **Then** those files’ checker results are reused and `cache` reports hits / vale skipped.
2. **Given** a cached wiki, **When** one page’s content changes, **Then** that page is rechecked and corpus facts (links, missing owners) reflect the current file set.
3. **Given any checker configuration, **When** lint runs, **Then** all configured checkers run and all findings are returned by default; there is no default hard-only filter and no checker-suppression flag on the agent-facing command.

### User Story 3 - Agent applies safe lint fixes (Priority: P1)

An agent needs to clear obvious lint defects in one owner page, several named
pages, or the whole wiki before handling judgment-based findings manually. It
runs `wiki lint fix` with the same vault-relative path semantics as lint. The
command applies only explicitly registered deterministic, idempotent fixers;
every other finding remains available for manual repair.

**Independent Test**: Run the fix command against one file, several files, and
the whole wiki. Safe fixes are applied, unsupported findings remain, and a
second identical run makes no further changes.

**Acceptance Scenarios**:

1. **Given** a finding with an explicitly registered deterministic, idempotent
   fixer, **when** an agent runs `wiki lint fix`, **then** the fixer updates the
   affected file.
2. **Given** a finding without such a fixer, **when** an agent runs
   `wiki lint fix`, **then** the finding remains and the command does not alter
   that content.
3. **Given** one or more vault-relative files or prefixes, **when** an agent
   runs `wiki lint fix <paths>`, **then** only the selected scope is changed;
   zero paths select the whole configured vault.
4. **Given** a completed fix run, **when** the same scope is fixed again with
   unchanged content and rules, **then** the second run is idempotent.

---


### User Story 4 - Agent queries the wiki with one phrase (Priority: P2)

An agent asks `wiki query 'The Flat Water'` and gets compact hits (title, path, retrieval id) without unsetting environment variables, naming a collection, or setting a hit cap. Overrides exist for collection and hit count.

**Why this priority**: Retrieval is already possible but the invocation is easy to get wrong in agent environments, and the result is not a worklist.

**Independent Test**: Run a known-title query with no extra flags; hits include the three fields. Override hit count and confirm the cap.

**Acceptance Scenarios**:

1. **Given** a configured wiki collection, **When** an agent runs `wiki query 'The Flat Water'`, **Then** retrieval runs (including inside environments that would otherwise block it), uses collection `wiki`, returns at most ten hits, each with `title`, `path`, and retrieval id.
2. **Given** `--collection` or a hit-count override, **When** query runs, **Then** those values replace the defaults.
3. **Given** default output, **When** query succeeds, **Then** the result is one compact object (`status` plus hits), not scraped prose.

---

### User Story 5 - One health snapshot for wiki fitness (Priority: P2)

The DM or an agent runs `wiki health` and sees whether the wiki is fit **and how it is trending**, then takes one next action without decoding an essay: live lint totals (same cache as lint), page count, bytes, tokens, existing Layer A maintenance stats, compact trend aggregates from existing sitting/efficiency/skill/error trackers, ordered `focus` items (path or prefix, reason, source), and `next` (the first focus item, or null). Layout/file-structure items come only from existing remorph/layout plans. Small agents can act on `next` unaided.

**Why this priority**: Named as a new command; vault and sitting stats already exist and must surface here so even small agents can improve the wiki without a DM wait.

**Independent Test**: `wiki health` returns one object with inventory + lint + Layer A fields + compact trend aggregates (including slowest wiki-command ranks and token-heaviest sittings from existing trackers) + ordered `focus` + `next`. The previous maintenance-report invocation still works as an alias of the same snapshot. A small independent agent names `next.path` from the object alone.

**Acceptance Scenarios**:

1. **Given** a configured vault, **When** `wiki health` runs, **Then** it performs live lint (all checkers, same cache) and returns page count, bytes, tokens, lint counts, cache stats, Layer A maintenance stats, compact sitting/efficiency/skill/error trend aggregates including slowest wiki-command ranks and token-heaviest sittings, ordered `focus`, and `next` in one object.
2. **Given** the historical maintenance-report invocation, **When** it runs, **Then** it produces the same snapshot (alias), not a second set of numbers.
3. **Given** default output, **When** health completes, **Then** it does not print per-step essays, a full findings dump, raw sitting/trace records, or a free-prose advice block.
4. **Given** an existing remorph or layout plan and a lint backlog, **When** health completes, **Then** `focus` includes bounded items with path or prefix, reason, and source (`lint`, `remorph`, `layout`, or `tracker`), and does not invent folder trees that are not in those plans.
5. **Given** a non-empty `focus`, **When** a small agent (Luna/Haiku class) reads only the health object, **Then** it can name `next.path` and the matching `reason` without extra flags or a DM prompt.
6. **Given** prior `wiki lint` / `wiki query` / `wiki health` runs recorded on the existing efficiency tracker, **When** `wiki health` runs, **Then** the snapshot names the slowest wiki commands from those records and does not dump raw traces or open a second ledger.
7. **Given** retained efficiency/sitting records with token totals, **When** `wiki health` runs, **Then** the snapshot ranks the token-heaviest sittings from those records and does not include skill-eval pass/fail or missing-skill inventories.
8. **Given** repo first-turn files and installed skills, **When** `wiki health` runs, **Then** `context.first_turn.files` is tiktoken cost per always-loaded file, `context.skills` is SKILL.md cost descending, `context.efficiency` names the first-turn delta vs the last health command record, and `context.act` is imperative steps the agent can follow without extra commands. Skill-eval pass/fail stays out.


---

### User Story 6 - Human pretty output on request (Priority: P3)

A human at a terminal passes `--pretty` and reads text: lint scoreboard and `file:line  RULE  message` grouped by file; query as one hit per line; health as a short scoreboard plus `next` and the `focus` list. Omitting `--pretty` never switches to text, even on an interactive terminal.

**Why this priority**: Operators need to read output; agents must not get text by accident.

**Independent Test**: Same lint with and without `--pretty` on an interactive terminal: default is compact structured output; `--pretty` is text.

**Acceptance Scenarios**:

1. **Given** an interactive terminal, **When** `wiki lint` runs without `--pretty`, **Then** stdout is one compact structured object.
2. **Given** `--pretty`, **When** lint/query/health run, **Then** stdout is human text as specified (lint scoreboard plus findings grouped by file / one hit per line / health scoreboard plus the `focus` list). `--pretty --full` is the same human findings list.
3. **Given** `--pretty` and a usage error, **When** the command fails, **Then** the error is one line on stderr and exit 2. Without `--pretty`, the error is a structured `status=error` object on stdout and exit 2.

---

### Edge Cases

- Zero path arguments: lint, lint fix, and health cover the whole configured vault.
- Several path arguments: union of those vault-relative files and prefixes; lint findings and fix results are still grouped by file.
- Path outside the vault or a missing file/prefix: exit 2, structured error, no scan.
- `--pretty` and `--full` together: human listing of all findings grouped by file, not indented structured text pretending to be human.
- Checker configuration (prose styles, structural rules, templates) changes: prior per-file cache entries for the affected checkers are invalid.
- Retrieval backend missing or failing: query returns structured error, exit 2; it does not invent hits.
- Creative lint subcommands invoked via the new `wiki` command: out of scope this sitting; existing script remains the surface.
- `entities/npcs` vs `entities/npc`: not corrected; fail closed.
- Empty or missing sitting/efficiency/error trackers: health still succeeds; trend aggregates are empty/zero, not an error and not invented history.
- No remorph/layout plan: health omits invented structure items; other `focus` sources may still appear.
- Path arguments scope live lint, inventory, and `focus`; sitting/efficiency/error trend aggregates stay whole-tracker (those logs are not path-scoped).
- A fix run with no eligible deterministic fixer leaves the affected finding and content unchanged; an eligible fixer that cannot apply safely is reported without a best-effort edit.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The product MUST expose one `wiki` command with subcommands `lint`, `query`, and `health`.
- **FR-002**: The command MUST resolve the vault from existing configuration (environment variable, nearest `.env`, global wiki config) without requiring the working directory to be the vault or repository root.
- **FR-003**: Path arguments MUST be treated as vault-relative files or prefixes. Zero paths mean the whole vault. Unknown or out-of-vault paths MUST exit 2 without fuzzy matching.
- **FR-004**: Default stdout for every subcommand MUST be agent-shaped: exactly one compact structured object, stable keys, `status` present, plus compact `timing` (`command`, duration, cache hits/misses when applicable). No terminal detection. `--json` MUST be accepted and MUST NOT change default output.
- **FR-005**: Machine failures MUST print `{"status":"error","error":"<message>"}` (or equivalent compact object with those keys) on stdout and exit 2. They MUST NOT be prose-only.
- **FR-006**: Exit codes MUST be 0 = clean/success, 1 = findings present (lint/health when the wiki is not clean), 2 = bad invocation or precondition.
- **FR-007**: `wiki lint` MUST run every configured checker including structural, template-conformance, creative, and prose/Vale checks. Its default finding set is all severities and all checker types. The agent-facing command exposes no hard-only or checker-suppression override.
- **FR-008**: Lint MUST cache per-file checker results keyed by the unique file plus the rules state applied to it (cache schema version, file content sha256, the hash of that file's resolved template when one exists, and a digest of Vale styles/config, structural lint sources, template contracts, and checker flags). Identical inputs MUST reuse results. A cache-version, rules-state, page-content, or resolved-template change MUST invalidate that entry and re-lint. Add/delete/rename MUST refresh corpus facts from cached extracts plus the current file set.
- **FR-009**: Default lint objects MUST include `status`, `counts`, `hard_fail`, `finding_total`, `affected_pages`, `next_page`, `next` (an actionable recommendation containing `path`, `findings`, `bytes`, and `action` or null), `cache` (hits, misses, Vale skipped), `files_checked`, `scope`, `ledger` (open count and ids from `errors.md`), and `timing`. The default object MUST NOT include the full `files`, `unique`, or `backlog` dumps.
- **FR-010**: Default `wiki lint` output MUST summarize every finding through aggregate rule counts and total/affected-page counts. `--full` MUST include every finding for the scoped files, including every Vale finding and every severity, grouped by file. Each full file group has the file path and flat records with `rule`, `file`, `line` (1-based), `severity`, and `message`. Nested per-rule finding maps MUST NOT be used.
- **FR-011**: `--full` MUST be accepted on lint and MUST add the detailed per-file finding dump to the compact default overview. Without `--full`, lint output MUST remain bounded by summary fields and one `next` recommendation regardless of file count.
- **FR-012**: Lint MUST NOT guess, alias-match, or invent owners for missing-link targets.
- **FR-013**: `wiki query <phrase>` MUST run retrieval even when the process environment would otherwise block it, default collection `wiki`, default cap 10 hits, compact hit fields `title`, `path`, and retrieval id. Collection and hit cap MUST be overridable.
- **FR-014**: `wiki health` MUST produce one snapshot: live lint (FR-007, FR-008) plus page count, bytes, tokens, the existing Layer A maintenance stats (waste, staging leftovers, remorph plan counts, policy), compact trend aggregates composed from the existing sitting log (`sittings.jsonl`), efficiency traces, skill-usage fields on those records, and the error ledger, an ordered `focus` array (FR-019), `next` (the first `focus` item or null), and `context` (FR-022). Trend aggregates MUST cover all currently retained tracker records.
- **FR-015**: The existing Layer A maintenance-report invocation MUST remain an alias of `wiki health` (same snapshot, not a second counter).
- **FR-016**: `--pretty` MUST select human text: lint scoreboard plus `file:line  RULE  message` grouped by file; query one hit per line (`path  title  id`); health scoreboard plus `next` and the same `focus` list. `--pretty` plus `--full` is the same human findings list. `--pretty` MUST NOT be implied by an interactive terminal.
- **FR-017**: Creative lint evaluator operations remain backend implementation details. Their findings MUST flow through the single default `wiki lint` result; agents MUST NOT need an evaluator-specific command to see them.
- **FR-018**: Agent instructions that tell agents how to lint, query, or health-check the wiki MUST be updated to this command, to the compact default lint overview, and to: run `wiki health`, then act on `context.act` (first-turn and skill load) then `next` (then remaining `focus`) without terminal detection, extra interpretation, or waiting for the DM. For a lint work item, agents MUST run `wiki lint fix <next.path>` before opening `wiki lint <next.path> --full`; they MUST use `--full` to inspect findings that remain. This MUST be usable by small agents (Luna/Haiku class).
- **FR-019**: Default `wiki health` MUST include a bounded ordered `focus` array and `next`. Each `focus` item MUST have `path` (file or prefix), `reason` (one objective line using an existing rule, remorph/layout plan, or tracker name — no new jargon), and `source` (`lint` | `remorph` | `layout` | `tracker`). `next` MUST be `focus[0]` or null if `focus` is empty. Layout and file/folder-structure suggestions MUST come from existing remorph/layout plans. `focus` MUST NOT invent new vault trees, MUST NOT be free prose, and MUST be present (possibly empty) on the default object.
- **FR-020**: Every `wiki lint`, `wiki query`, and `wiki health` invocation MUST append one compact timing record to the existing efficiency tracker (`command`, duration, cache hits/misses when applicable, exit code) and MUST include that same compact `timing` on its stdout object. Health MUST rank slowest wiki commands from those records. This MUST NOT create a second benchmark ledger or dump raw traces.
- **FR-021**: Default `wiki health` MUST include compact token-heaviest sitting ranks composed from existing sitting/efficiency records. It MUST NOT include skill-eval pass/fail or missing-skill inventories.

- **FR-022**: Default `wiki health` MUST include `context`: tiktoken `first_turn` file breakdown (`.omp/AGENTS.md`, repo `AGENTS.md`, vault `AGENTS.md`, vault `hot.md`), skill `SKILL.md` costs descending by tokens with `coverage` `with`|`without` eval criteria (`evals`/`criteria` counts, `eval_coverage` totals), `efficiency` first-turn delta vs the previous health command record (`up`/`down`/`flat`/`new`), and `act` — imperative completion-bounded steps. Tokens use `tools/token_count.py`. MUST NOT include skill-eval pass/fail or file bodies.
- **FR-023**: `wiki health` MUST flag llm-wiki issues on the critical files `index.md`, `hot.md`, `log.md`, and `AGENTS.md` (oversized, bloated, duplication, redundancy, cohesion / overlapping jobs) in `context.core` and `context.act`. Those files MUST keep distinct jobs: index lists pages, log is the activity log, hot is a 500-word snapshot, AGENTS.md is owner conventions.
- **FR-024**: `wiki lint` and `wiki health` MUST NOT report `status: clean` (or exit 0) while `errors.md` still contains open operational failures. Page-lint-only clean is not an all-issues health result.
- **FR-025**: Live lint used by `wiki health` MUST run all pending files in one checker invocation (same cache as lint). It MUST NOT fan out one full-vault checker process per small file batch.
- **FR-026**: While `wiki lint` or `wiki health` is running, the command MUST write a progress line to stderr at least every 10 seconds so a watching agent can tell the process is alive. Those lines MUST NOT mix into the stdout result object. A run that finishes before 10 seconds MAY emit no heartbeat. `wiki query` is out of this requirement.
- **FR-027**: The product MUST expose `wiki lint fix [paths...]` as the repair action under the agent-facing lint command. It MUST accept zero, one, or multiple vault-relative files or prefixes using the same scope rules as `wiki lint`.
- **FR-028**: `wiki lint fix` MUST apply only explicitly registered fixers that are deterministic and idempotent. Findings without an eligible fixer MUST remain unchanged and available for manual repair.
- **FR-029**: `wiki lint fix` MUST apply eligible fixes, rerun lint on the affected scope, and use the agent-shaped output contract: one compact structured result with stable keys, `status`, applied fixes, remaining findings, scoped change information, and `timing`; `--pretty` MAY render an explicit human summary without changing the machine result contract.


### Key Entities

- **Worklist**: Bounded default lint overview — aggregate counts, finding/page totals, cache/scope metadata, and `next` for the smallest dirty file — with `--full` as the detailed per-file finding dump.
- **Finding record**: Flat diagnostic: rule, file, 1-based line, severity, message.
- **Checker cache**: Reuse of per-file checker results when file bytes and checker configuration are unchanged.
- **Health snapshot**: One inventory + lint + Layer A maintenance + compact operational-trend object (including slowest wiki-command ranks and token-heaviest sittings), including ordered `focus`, `next`, and `context` (first-turn file cost, ranked skill cost, efficiency delta, `act`).
- **Focus item**: Bounded next action: vault-relative path or prefix, objective reason, source (`lint`, `remorph`, `layout`, `tracker`). `next` is the first item or null.
- **Query hit**: Title, vault-relative path, retrieval id.
- **Command timing record**: One efficiency-tracker row per wiki subcommand run: command name, duration, cache hits/misses when applicable, exit code.
- **Fix result**: Agent-shaped repair outcome containing the selected scope, changed files and fix counts, skipped or remaining findings, and command timing.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: An agent lints a directory or the whole wiki with one invocation and receives bounded aggregate issue counts plus an actionable `next.path`; it does not need to flatten or summarize a per-file finding dump.
- **SC-002**: Default lint of two named files, a prefix, or the whole wiki returns one compact overview with complete issue counts and selects the smallest dirty file. `--full` returns the complete Vale-included findings for that scope with 1-based line numbers.
- **SC-003**: A second whole-wiki lint with no content or checker-config changes reports cache hits for previously checked pages and does not re-run prose checkers on those pages.
- **SC-004**: `wiki query` of a known in-wiki title, with no extra flags, returns at least one hit containing title, path, and retrieval id.
- **SC-005**: `wiki health` returns page count, byte size, token total, lint hard-total, compact sitting/efficiency/skill/error trend aggregates over all currently retained tracker records including slowest wiki-command ranks and token-heaviest sittings, ordered `focus`, `next`, and `context` (first-turn files, ranked skills, first-turn efficiency delta, `act`) in one invocation; the historical maintenance-report invocation returns the same snapshot.
- **SC-006**: On an interactive terminal, omitting `--pretty` still yields compact structured output; passing `--pretty` yields text a human can read without a decoder.
- **SC-007**: An unknown vault-relative path fails in under one second with a structured error and does not enumerate the wiki.
- **SC-008**: Independent agent given only this spec’s command examples lints the whole wiki, names aggregate issue counts, and names `next.path` and its action without being told to parse per-file findings. It can then run `wiki lint <next.path> --full` for line-level repair.
- **SC-009**: A small independent agent (Luna/Haiku class) given only this spec’s health object names `next.path` and its `reason` and would perform that action without extra interpretation, extra commands, or a DM wait.
- **SC-010**: After at least two `wiki lint` or `wiki query` runs, `wiki health` names the slower command from the existing efficiency tracker without a raw-trace dump.
- **SC-011**: Given retained sitting/efficiency records with token totals, `wiki health` names the token-heaviest sitting and does not list skill-eval pass/fail.
- **SC-012**: Given installed skills and first-turn files, `wiki health` names the heaviest first-turn file and the heaviest skill by tiktoken, reports each ranked skill with/without eval criteria, and emits `context.act` the agent can follow; it does not list skill-eval pass/fail.
- **SC-013**: A `wiki lint` or `wiki health` run that lasts at least 10 seconds emits at least one stderr progress line by the 10-second mark, and another by each subsequent 10-second mark until it exits. Stdout remains one result object.
- **SC-014**: `wiki lint fix` accepts one file, multiple files or prefixes, and no path; it applies only registered deterministic, idempotent fixers within scope and leaves unsupported findings unchanged.
- **SC-015**: Repeating `wiki lint fix` with unchanged content and rules produces no additional changes, proving idempotence.
- **SC-016**: Default `wiki lint fix` output is one compact structured object that identifies changed files, applied/skipped fixes, and post-fix remaining findings, scope, status, and timing; an agent can distinguish completed repairs from manual work without parsing prose.
- **SC-017**: Agent instructions and command examples name `wiki lint fix <next.path>` as the first repair step and `wiki lint <next.path> --full` as the follow-up for findings that remain, making the safe-repair path discoverable without additional interpretation.

## Assumptions

- Existing vault configuration and vault-resolution behavior are reused, not redesigned.
- Existing structural lint, template conformance, prose/Vale, identity scan, Layer A maintenance report, sitting log, efficiency-trace reports, error ledger, and retrieval backend are composed, not replaced. This feature changes the **command surface and default result contract**.
- All configured checkers, including structural, template-conformance, creative, and Vale checks, run through the agent-facing `wiki lint` command. Its default result aggregates every finding regardless of severity; detailed records require `--full`. Agents do not need checker-suppression flags.
- `--full` adds the detailed dump; it is not a suppression or omission carve-out. The agent-facing lint command has no `--all`, `--no-vale`, or `--no-template` flags.
- Retrieval hit cap uses the backend’s native count flag; the user-facing default is 10.
- Constitution VI asks for errors on stderr. This feature’s **default** machine errors are structured objects on stdout so agents have one stream to load (already the shared wiki-ops convention). `--pretty` errors go to stderr. That split is intentional.
- Agent-instruction updates (lint/query/health skills and standing wiki command examples) ship in the same change so agents do not keep copying the old invocation. Health instructions tell agents to run `wiki health` and do `next`.
- No new identity-resolution or owner-guessing behavior.
- Cache location and invalidation on checker-config change are planning details; behavior is FR-008.
- Trend window is existing tracker retention, not a new health policy. Empty trackers yield empty aggregates.
- Sitting/efficiency/error trends are whole-tracker even when path args scope lint/inventory/`focus`.
- Wiki command timings reuse the existing efficiency tracker (FR-020); they are not a second health counter.
- Skill-eval pass/fail and missing-skill inventories are out of this feature; they stay on skill-creator.
- Safe automatic repair is limited to checkers with an explicit fixer contract; this feature does not infer fixability from a finding message or attempt heuristic prose rewriting.
- Agent-facing guidance MUST present `wiki lint fix <next.path>` before `wiki lint <next.path> --full`; it MUST describe the latter as the manual follow-up for remaining findings.
