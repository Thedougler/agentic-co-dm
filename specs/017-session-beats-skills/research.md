# Research: Session Beat Skills

## Decision: Keep `session-beats` as the composition skill

**Rationale**: Its description already fires on planning a session, one-shot, adventure arc, or expedition evening (spec US1). Renaming to `composing-beats` would duplicate the Campaign OS skill name and force every caller to move for no behavior change.

**Alternatives considered**: New `composing-beats` beside `session-beats` (two composition skills). Rename `session-beats` (churn). User-invoked router (type skills could not load each other; SKILL-MECHANICS).

## Decision: Five new type skills named after the type

**Rationale**: Spec FR-004 — Hook, Development, Cliffhanger, Climax, Resolution. Names `hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats` use the type as the leading word. They do not collide with Campaign OS `writing-*-beats` if those directories are still discoverable.

**Alternatives considered**: One skill per RTG card (~50 skills; FR-004 forbids; Constitution IX). Reuse `writing-hook-beats` etc. (second system, different domain). Fold cards into `session-beats/references/` only (blob remains).

## Decision: Do not port Campaign OS composing/writing-*-beats

**Rationale**: `.claude/skills/composing-beats` and `writing-*-beats` teach Situation/Gravity/Irrigation, not the RTG Beat Chart already adapted in `session-beats`. Spec out of scope: a second pacing system. `writing-beats` under `.agents/skills/` is an article-journey skill (`disable-model-invocation`); leave it.

**Alternatives considered**: Copy those skills into `.agents/skills/` (imports a competing procedure). Merge their card lists into RTG cards (duplicate SoT).

## Decision: All six skills are model-invoked

**Rationale**: The agent must reach composition when planning a session, and a type skill when writing/editing/filling that type. Skills must load each other at named seams. User-invoked skills cannot be fired by other skills (SKILL-MECHANICS). Six always-loaded descriptions is the cost of independent reach; worth it versus one blob.

**Alternatives considered**: Only `session-beats` model-invoked (type skills unreachable at seams). Seventh router skill (Constitution VII/IX; extra trigger).

## Decision: Cards live with their type; chart lives with composition

**Rationale**: FR-006 / SC-007. `beat-types.md` is the blob. Split cards into per-type disclosed reference. Composition keeps agency, polarity, budget, threads, recompute. Type skill keeps purpose, completion test, cards, how to fill this beat. Pointers, not copies.

**Alternatives considered**: Keep `beat-types.md` as shared reference both load (agents still open the full catalog). Duplicate card summaries in composition (SoT split).

## Decision: Named seams are the only cross-load

**Rationale**: Spec FR-008. Composition filling a typed slot; typed-beat job that needs chart position/polarity/threads/transition; Play a Cliffhanger as Hook; Play a Development as Hook; handoff that must name the next type. Any other second catalog is a defect.

**Alternatives considered**: Always load composition with every type skill (blob). Type skills inline the full chart (FR-006 fail).

## Decision: `AGENTS.md` holds one routing table

**Rationale**: Same pattern as 010 writing authorities. Sessions that never open `session-beats` still need to pick the right skill. `.omp/AGENTS.md` imports `AGENTS.md` — do not copy the table. Description of each type skill carries its write/edit/fill branches.

**Alternatives considered**: Routing only in skill descriptions (misses sessions that do not match). Duplicate table in `.omp/AGENTS.md` (Constitution IX). New `docs/agents/session-beats.md` procedure file (extra hop).

## Decision: Claude Code only for novel or major skill work

**Rationale**: FR-025 / constitution XI. New type skills, `spell-design`, and a `session-beats` or `vehicle-design` redesign are Claude Code jobs (`claude-opus-4-6 --effort medium`, minimal prompt). Session agent lands `AGENTS.md`, wiki templates, `wiki/AGENTS.md` Layout, pointer retargets, and Spec Kit pattern tweaks. Conserve Claude Code.

This re-plan: filling the session-plan draft (instead of the Session 11-00 spine) is a `session-beats` redesign → designated writer. Type-skill "copy this template / fill these jobs" pointers and the `run-guide` "do not rewrite into Session 11" line are small established-file edits → session agent.

**Alternatives considered**: Dispatch every standing-load edit (wastes quota). Session agent drafts new skills (016 fail for novel design). `opus` alias / `--effort high` (superseded).

## Decision: Quickstart observes routing, not file internals

**Rationale**: Constitution IV. Classify the contract jobs. A planning job produces a valid chart from the session-plan draft without type-card catalogs. A typed-beat job does not open the other four catalogs unless a named seam fires. After the split, no skill contains both the full chart and all five catalogs. Do not require rewriting Session 11 to prove it.

**Alternatives considered**: pytest over SKILL.md strings (implementation-coupled). Require a live session to be composed as the only proof (slow; still needed later at implement).

## Decision: Vehicle and spell are wiki kinds with templates

**Rationale**: Clarifications 2026-09-12. Scaffolds go to `wiki/templates/vehicle.md` and `wiki/templates/spell.md`. `wiki/AGENTS.md` adds `type: vehicle` and `type: spell` and Layout jobs. Pass is those jobs. `vehicle-design` fills the 5e sheet, components, crew, handling, and combat. `spell-design` is primary for write/edit/create of a spell page.

**Alternatives considered**: Keep vehicle notes as play-dials with a blank sheet (pages are not runnable). Fold spells into `dnd-5e-magic-item-design` (wrong kind). Layout jobs with no `spell-design` (no skill fires).

## Decision: Skills teach the work to do now

**Rationale**: Clarification: write positive jobs and done-when. Vehicle design is in scope now. Text that frames a missing craft as something that will never exist is the named failure.

**Alternatives considered**: Keep “leave HP/speed blank” as a standing ban (contradicts the template). Extra exception lists instead of jobs.

## Decision: Usage limit defers only the Claude job; Codex is a gated fallback; session-agent last-resort follows constitution XI

**Rationale**: FR-026 / SC-016 / constitution 1.11.0. Restore Claude targets, record retry time on the feature `tasks.md`, complete remaining tasks that do not depend on that job. Completing other work MUST carry those deferred tasks forward. If every remaining open task is blocked, no other work can be done, and the retry time on the blocked task is more than one hour away, the session agent MAY invoke the Codex CLI at ChatGPT 5.5 medium with the same tightly scoped prompt. Re-check those gates before each remaining blocked skill job; prefer Claude Code if it is usable again.

Named conflict: FR-026 says the session agent MUST NOT write the design-impact change itself. Constitution XI (Last Amended 2026-09-12) allows session-agent write when both Claude Code and Codex are usage-limited. Constitution wins for operating constraints. `docs/agents/skill-design-dispatch.md` already records that last-resort path.

**Alternatives considered**: Halt the whole implement (leaves independent wiki/AGENTS.md work undone). Session agent writes the novel skill on first usage-limit (016 fail). Park usage limits as GitHub issues (owner rejected; Spec Kit `tasks.md` is the tracker). Always switch to Codex on first usage-limit (skips Claude when it returns inside the hour). Ignore constitution XI last-resort (operating-constraint miss).

## Decision: Claude Code skill updates use a minimal prompt and Opus 4.6 medium

**Rationale**: FR-025. When Claude Code runs, default model is `claude-opus-4-6` at `--effort medium`. Prompt names deliverables and a completion test.

**Alternatives considered**: `--effort high` (superseded). `opus` alias (default Opus). Long pasted spec/plan in the writer prompt (IX).

## Decision: Add faction, lore, quest, city, and region wiki kinds

**Rationale**: Clarifications 2026-09-12. Same pattern as vehicle/spell: template + Layout jobs + one primary skill. Pass is jobs, not heading-order match. Omit unused sections. Scaffolds are installed at `wiki/templates/{faction,lore,quest,city,region}.md`.

**Alternatives considered**: Keep stretching site `place.md` and session-prep for cities, regions, and quests (pages are not runnable). One mega-template for all geography (Constitution VII fail).

## Decision: New skills for faction, lore, city, and region; keep existing owners for quest and place hub

**Rationale**: Spec FR-030/031, FR-037, FR-043, FR-049, FR-053. `faction-design` replaces `faction-prep` (removed, not a stub). `lore-design` is new. `city-design` and `region-design` are new. `place-design` is the hub for all places and defers to those specialized skills; it still writes site places from `wiki/templates/place.md`. `narrative-islands` stays primary for `type: quest` and fills `wiki/templates/quest.md`. No `quest-design`.

**Alternatives considered**: Keep `faction-prep` beside `faction-design` (split owner). Put cities on `place-design` because settlements resemble cities (owner rejected; hub must defer). New `quest-design` (owner rejected; islands already owns quests).

## Decision: Fewer situation types — quest only

**Rationale**: FR-045. Durable sandbox situations are `type: quest`. `type: front` and `type: encounter` are retired. Encounter-prep and traps-trials still own fight/site math. Night-only pressure stays a session-plan section. Region pages do not invent pressure; if a pressure is already stated, they link that note (FR-051).

**Alternatives considered**: Keep front/encounter as extra types (owner wants fewer types). Apply the quest template to fronts and encounters (wrong name). Require every region to invent a front (owner rejected).

## Decision: Later-update owners stay split by kind

**Rationale**: Faction: `faction-design` writes Current Turn with no roll; `world-tick` rolls and appends the faction-turn log; agenda clock lives on the faction page; `hot.md` may point, not duplicate (FR-032/033). Lore: not `canon` until players interact or witness; until then the DM may change it freely and Canon Log is omitted; wrapup/reconcile append the log (FR-039). Quest: `narrative-islands` owns later updates including rolls and the Quest log; `world-tick` does not advance quest portents (FR-044). City change log and local clocks stay on the city page under `city-design`; a pursuable city situation is a linked quest, same as region pressure. Region change log stays on the region page under `region-design`.

**Alternatives considered**: `world-tick` owns every clock (drifts from page). `lore-design` marks lore canon at accept (owner: not until table).

## Decision: Ingest remap `lore`→`item` is removed

**Rationale**: FR-038. `type: lore` is a real kind. World-truth notes use it. Actual items stay `item`. Existing mislabeled flora stay `item` and are not rewritten solely to prove the template.

**Alternatives considered**: Keep `lore`→`item` for old files only (new lore notes get filed as items). Rename the kind to avoid the collision (owner wants `lore`).

## Decision: Claude Code for the new kind skills and the islands/quest redesign

**Rationale**: FR-025. Novel: `faction-design`, `lore-design`, `city-design`, `region-design`. Redesign: `narrative-islands` to fill the quest template and stop minting front/encounter. Session agent: templates, `wiki/AGENTS.md` Layout and type enum, `AGENTS.md` routing rows, `faction-prep` deletion and caller retarget, `place-design` hub defer pointers, `world-tick` faction-turn log, wrapup/reconcile Canon Log pointers.

**Alternatives considered**: Session agent writes novel skills (016 fail). Dispatch `place-design` pointer-only defer to Claude Code (unnecessary).

## Decision: Typed draft templates are the live pages; session-plan draft is the chart

**Rationale**: Clarifications 2026-09-13 / FR-013 / FR-054 / US5. The page the DM runs is the filled typed draft, not a later Session 11 cockpit rewrite. Composition fills the session-plan draft (compass, beat map, floating beats, pressure, PC touchpoints, links to typed beats). Beat Chart rules still bind. Session 11 remains scan-quality evidence. FR-015: `run-guide` MUST NOT rewrite a typed beat into a Session 11 cockpit.

Install the six supplied drafts at `wiki/templates/{hook,development,cliffhanger,climax,resolution,session-plan}.md`. Keep draft jobs. Add `col` / `col-md` where a pair of scan jobs share a dashboard. Keep DM-facing callouts on the typed drafts for scan. `[!narration]` remains the only player-spoken surface. Strip HTML design-basis comments and citation crumbs on install (skills teach methods; they do not paste the source). Drop the session-plan draft comment that treats alternation as optional — FR-010 still requires alternating middle beats; FR-011 still allows skip/reorder/end early after play.

Stop using `wiki/templates/session-prep.md` as copy-start for new beats or plans (it is the old Session 11 cockpit scaffold). Filing path and `Session-<n>-<BB>-<Label>.md` names stay (wiki/AGENTS.md). Do not adopt the draft's `{{title}} - B01 - Strong Start` filename scheme.

`session-skeleton.md` must not teach Session 11-00 as the filed page. Point composition at `wiki/templates/session-plan.md`.

**Alternatives considered**: Keep Session 11 cockpit as the live page (owner rejected; two layouts is the blob). Keep Session 11-00 spine jobs on composition (owner rejected; fill the session-plan draft). Seventh campaign `type` per beat (owner rejected; keep `type: session-prep`). Leave `session-prep.md` as the copy-start (agents would still mint cockpits).

## Decision: Session-prep identity is `type` + `kind`; drop useless draft keys

**Rationale**: FR-055. New live beats and session plans are `type: session-prep`. `kind` is `hook` | `development` | `cliffhanger` | `climax` | `resolution` | `session-plan`. MUST NOT add `type: beat`, `type: session-beat`, or `type: session-plan`. Draft `beat:` / `beat_type:` rewrite to `kind`. `category` is `journal`.

Shared keys: `title`, `category`, `tags`, `sources`, `created`, `updated`, `type`, `kind`, `lifecycle`, `reveal`, `campaign`, `session`, `visibility`, `summary`. Page jobs, card, polarity, handoff, location, budget, and previous/next live in the body. Drop draft extras that duplicate those jobs or `kind`: `intensity`, `pacing`, `card`/`hook_kind`/`development_type`/`climax_kind`, minute/order/sequence/duration fields, location, previous/next aliases, `participants`, extra `status`, session-plan `date`/`planned_length`/`previous_session`/`next_session`. Do not copy a kind's extras onto the other pages.

Page identity and jobs live in [session-prep-pages.md](./contracts/session-prep-pages.md), not folded into beat-skill-routing.

**Alternatives considered**: Keep every draft key on every page (owner: all files do not need all those keys). Keep `intensity` (owner: useless as frontmatter). Keep `pacing`/`card` as Hook-only extras (body already has key and card). Add `type: session-plan` (owner rejected). Harmonize `beat:` beside `kind` (two names for one field).
