# Research: Expert-Grounded D&D Content Guidance

## Decision: `writing-for-agents` owns the research-then-integrate loop

**Rationale**: The loop fires only when creating or changing agent-consumed D&D content guidance — skills, standing instructions, pointed-at procedures. That is already `writing-for-agents`' job (Reader `agent`). A new skill would be a seventh trigger surface (Constitution VII). A second table in `AGENTS.md` would mix this with the 010 writing/visual stack and spend always-loaded tokens on a branch that is not every turn (Constitution IX). Put one description branch plus a short in-file section on `writing-for-agents`. Host web search is already the research tool.

**Alternatives considered**: New `expert-research` skill (extra trigger; router-skill smell). Row on the 010 `AGENTS.md` table (wrong classifier; always-loaded). Duplicate the loop into every D&D craft skill (sediment; 010 already deleted that pattern). New `docs/agents/narrative.md` (extra hop; easy to skip).

## Decision: Integrate outcomes, cite techniques

**Rationale**: Clarification Q2 and Constitution VII. The named failure is vacuum-invented guidance and math detached from story. The test is a second person pointing at the expert-solved outcome. Requiring a named person's process as the only method is itself a fail (FR-002, FR-019). Techniques may be cited as sources.

**Alternatives considered**: Paste Mercer (or any expert) process into combat skills (suffocates; collides with VII). Quote-dump a research appendix beside the skill (second competing procedure; FR-002 fail).

## Decision: Source bar lives in that same section

**Rationale**: Clarification Q3. Named published designers and documented craft first. High-quality homebrew only if those are silent. Never paste proprietary book text (already a hard rule on monster craft). If nothing is found, invent and flag per Work rules — do not pretend a giant spoke. Do not add a source allowlist file (environment + judgment; Constitution IX).

**Alternatives considered**: Any web page (junk in standing guidance). Famous names only (blocks problems they never wrote about). A checked-in bibliography (stale cache of a lookup).

## Decision: Combat instance is outcome lines on existing craft, not a new owner

**Rationale**: FR-015 craft owners stay. `homebrew-monsters-5e` already owns monster math and already asks for a fiction signature and a reason to exist — add the testable outcomes (custom feature tells lore/origin/stakes; substantial homebrew names a plot beat; number-only is incomplete). `encounter-prep` already owns encounters — add named-place mechanical pressure and stock/override exemptions. Later content kinds reuse the `writing-for-agents` loop when those skills are next edited; they do not need an instance in this feature.

**Alternatives considered**: Rewrite every D&D craft skill now (scope spike; US1 already covers the next edit). New combat-narrative skill (steals craft). Put combat outcomes in `AGENTS.md` (always-loaded; wrong layer).

## Decision: Ordinary wiki writes do not research

**Rationale**: FR-003 / SC-002. Research is for guidance changes. Content jobs follow the guidance. Requiring web research on every NPC page would burn tokens and stall prep (Constitution VIII/IX). `docs/agents/work.md` and `wiki/AGENTS.md` stay as 010 left them.

**Alternatives considered**: Research on every wiki write (explicitly out of spec). Point work.md at the research loop (teaches the wrong job).

## Decision: Quickstart is the behavioral test

**Rationale**: Constitution IV. Observe classification of guidance jobs and combat Work jobs. Do not pytest YAML. Do not rewrite `legacy/`. Do not require a live image call or a live web call in the quickstart — a reviewer checks that the pointers and outcomes exist and that sample jobs classify.

**Alternatives considered**: Require a live web-search transcript in CI (flaky; couples to internals). Scanner over wiki pages (FR-016 / SC-008 fail).
