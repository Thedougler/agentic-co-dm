---
status: draft
---
# Task: Close the agent-guidance gap in this repo's existing Vale setup

This repo already runs Vale in production against wiki prose — reuse that
infrastructure (`.vale.ini` + `.vale-hard.ini` + `docs/vale-styles/`, wired
through `npm run lint`/`utils/scripts/lint-dispatch.mjs` and the
ratchet/worklist tracker), don't stand up a second linting system next to it.
But agent-guidance prose is a different genre from wiki prose, and the
existing custom style (`CampaignOS`) is heavily tuned for the wiki's genre:
maritime-campaign overrides (`ShipOveruse`, `FigurativeLands`), narrative
rules that only make sense for in-world pages (`ProcessLeak`,
`StaleWorkMarkers`, `DedupNarration`, `VaScriptDeliveryPhrases`, and more),
each with its own hand-tuned per-path exemption list in both config files.
Don't fight that tuning to make agent guidance activate cleanly against it —
give agent guidance its own dedicated style instead (§ Deliverable 3), so it
never inherits a wiki-genre rule it would just need to turn back off.
`docs/vale-styles/ai-tells/*.yml` (generic AI-tell detection, not
wiki-specific) already implements most of "hedging" and "AI filler/tells"
(e.g. `HedgingPhrases.yml`, `FillerPhrases.yml`, `SelfReference.yml`,
`Metacommentary.yml`, `FormalRegister.yml`, `SycophancyMarkers.yml`) and is
safe to keep in the new style's `BasedOnStyles` — read that directory before
writing a single new rule, so the work here adds only what's genuinely
missing: (a) scanner coverage for the agent-guidance paths this setup
doesn't scan today, (b) a new dedicated style for what `ai-tells` doesn't
already catch.

Implement a system that lints and helps correct our agent guidance so it matches Anthropic's current prompt/context-engineering best practices (Claude 4.x / 5-generation and Claude Code). Look up Anthropic's current guidance (WebFetch/official docs) before encoding rules — do not rely on training memory or the starter list below alone; treat that list as a floor, not the spec.

## Scope — what to lint, and why it isn't linted yet

Treat all of the following as **agent instruction prose** (not general product docs):

1. Root `CLAUDE.md` and every nested `CLAUDE.md`
2. `.claude/rules/**` and `.claude/commands/**`
3. `docs/guardrails/**`
4. `content/runbooks/craft/**` and `content/runbooks/**`

`.claude/skills/**` and `.claude/agents/**` are already scanned (they're in
both `utils/scripts/lib/prose-scope.mjs`'s `INCLUDE_ROOTS` and
`lint-dispatch.mjs`'s `routeType()`, and `.vale.ini` has
`[**/.claude/skills/**/*.md]` / `[**/.claude/agents/*.md]` sections) — leave
them as reference shape, don't re-touch them. `content/runbooks/craft/**` and
`content/runbooks/**` are also already scanned (under the `content` root) and
already have `.vale.ini` sections (`[content/runbooks/craft/exemplars/**/*.md]`,
`[content/runbooks/**/*.md]`, and the broad `[content/**/*.md]` fallback for
the rest of `content/runbooks/craft/`) — verify current tuning still holds, but no new
wiring is required there.

The real gap is items 1-3: `routeType()` in `lint-dispatch.mjs` returns `null`
for `CLAUDE.md`, `docs/guardrails/**`, `.claude/rules/**`, and
`.claude/commands/**` today, and none of them are in `prose-scope.mjs`'s
`INCLUDE_ROOTS` either — these files get zero Vale coverage, zero ratchet
tracking, and don't show up in `npm run lint:worklist` no matter what they
contain. Closing that gap (not building a new linter) is the actual task.

Skip pure code, lockfiles, and generated artifacts.

## Objective best practices to encode

Derive rules from Anthropic's guidance, not from taste. Before writing a new
rule for any bullet below, check whether `docs/vale-styles/ai-tells/*.yml`
already covers it — most of "hedging" and "AI filler/tells" already do (§
above); `CampaignOS` isn't relevant here since the new style won't include
it (§ Deliverable 2). Only the bullets with no existing match are new work.

**Clarity & structure**

- Clear, direct, imperative instructions
- Prefer short directives over long explanations
- Prefer positive framing where possible; use hard negatives (`Never` / `Do not`) only for non-negotiable constraints
- Prefer sequential numbered/bulleted steps when order matters
- Prefer XML-style sectioning only when a file mixes instructions, context, examples, and inputs

**Context engineering (Claude Code era)**

- Keep always-on files (especially root and nested `CLAUDE.md`) short and high-signal
- Prefer progressive disclosure: point to skills/runbooks instead of inlining everything
- Do not restate the obvious (things Claude can infer from the repo/filesystem)
- Avoid overlapping or conflicting rules across CLAUDE.md, skills, hooks, and shared guardrails
- Prefer “use judgement / match surrounding conventions” over long absolute rule lists when appropriate
- Put tool-usage detail in tool/skill descriptions, not duplicated in every CLAUDE.md

**Language to ban or flag**

- Hedging: try to, consider, if possible, ideally, when appropriate, it is recommended, etc.
- AI filler / tells: In today’s…, It’s important to note, leverage, utilize, delve, robust, seamless, unlock, game-changer, etc.
- Soft role fluff: “You are a highly skilled / world-class / expert with extensive knowledge…”
- Vague process language that does not prescribe a concrete action

**Terminology**

- Standardize: CLAUDE.md, AGENTS.md (if present), skill, subagent, hook, output style, context engineering
- Prefer project-standard names for guardrails, craft, and runbooks paths when referenced in prose

**Length / density**

- Flag very long sentences and very long always-on instruction files
- Prefer one concrete rule per bullet

## Deliverables

Implement, do not only propose:

### 1. Wire the four gap paths into the scanner

Both files must move together (`lint-dispatch.mjs`'s own header comment says
so — `routeType()` and `prose-scope.mjs` classify the same paths and must
never drift):

- `utils/scripts/lib/prose-scope.mjs`: add `CLAUDE.md` (root + nested — glob,
  not a literal), `docs/guardrails`, `.claude/rules`, `.claude/commands` to
  `INCLUDE_ROOTS` (or to `isExcluded`'s counterpart if a root-level glob
  isn't how that list works — read the function before editing it).
- `utils/scripts/lint-dispatch.mjs`: extend `routeType()` so these four paths
  return a real bucket instead of `null`. Decide `'skills'` vs `'wiki'` by
  reading what `lintSkills`/`lintWiki` actually run (`lint-skills.mjs` vs the
  wiki path) — these are fixed-format instruction docs like
  `.claude/skills/**` and `.claude/agents/**`, not narrative prose, so
  `'skills'` is the likely correct bucket; confirm, don't assume.

### 2. Two config files, not one — `.vale.ini` AND `.vale-hard.ini`

This repo runs Vale through two separate configs that must both be updated
and kept in sync (`.vale-hard.ini`'s own comments already document one past
drift between them, and this session hit it again — see below): `.vale.ini`
is the advisory pass (`npm run lint`, the full style stack), `.vale-hard.ini`
is the blocking pass the PostToolUse Edit hook (`vault_lint_fix.sh`) runs
per-edited-file, at `MinAlertLevel = error`.

Gotcha, verified empirically this session: for a given key (`BasedOnStyles`
included), Vale merges every section whose glob matches the file, in file
order, and the last matching section to set that key wins — it's a
per-key override, not a per-section union (`content/spells/**/*.md`'s
`BasedOnStyles = Vale, CampaignOS` already relies on this to drop
`proselint`/`write-good`/`ai-tells`/`Readability` from the broader
`[content/**/*.md]` section). A path with no matching section that ever sets
`BasedOnStyles` gets none at all. `.vale-hard.ini`'s pre-existing
`[**/CLAUDE.md]` section hit exactly that: it disabled two `CampaignOS`
rules but no matching section (for root/nested CLAUDE.md specifically) ever
set `BasedOnStyles`, so CampaignOS was never on to begin with — fixed this
session as a standalone bug fix, unrelated to the new style below. Applies
directly to this deliverable: every new gap-path section must set its own
`BasedOnStyles` (don't assume a broader section covers it), and setting
`BasedOnStyles =` (empty) in a narrower, later section is exactly how to
opt a path OUT of a broader section's styles entirely (this session used it
to disable the wiki stack for `prompts/**/*.md`, so the new
`AgentGuidance` style can own that path when it's ready).

Add sections for the four gap paths to both `.vale.ini` and
`.vale-hard.ini`: `[CLAUDE.md]` + `[**/CLAUDE.md]`, `[docs/guardrails/**/*.md]`, `[.claude/rules/**/*.md]`, `[.claude/commands/**/*.md]`.
`BasedOnStyles = Vale, proselint, write-good, Readability, ai-tells,
AgentGuidance` (§ Deliverable 3 for the new style's name) — deliberately
**not** `CampaignOS`, so these paths never inherit a wiki-genre rule in the
first place and never need that style's exemption dance. Expect a handful of
genuine self-reference false positives regardless (a rules file quoting a
banned phrase as its own example, the same shape as the existing
`.claude/skills/dnd5e-scene-narration/SKILL.md` entries in both configs) —
carve those out per-file as they surface, don't weaken the rule.

### 3. A new, dedicated Vale style: `AgentGuidance`

Create `docs/vale-styles/AgentGuidance/` (name is a placeholder — confirm or
rename), a sibling to `CampaignOS`/`Readability`/`ai-tells`, not a subfolder
of any of them. Same file shape as every existing custom rule:
`existence`/`substitution`/`occurrence`, actionable message ending in the
fix, `link:` field — copy `docs/vale-styles/CampaignOS/StalePattern.yml`'s
shape as a template. Candidates, after confirming `ai-tells` has no existing
match (§ intro):

- Imperative/directness (flag passive, hedged instructions where a direct
  imperative would do)
- XML-style sectioning used, or omitted, against Anthropic's own guidance
  for when it helps vs. adds noise
- Progressive disclosure (an always-on file — root/nested `CLAUDE.md`,
  `.claude/rules/**` — inlining a procedure that belongs in a skill or
  runbook)
- Terminology drift (inconsistent naming for skill/subagent/hook/output
  style/context engineering)

`ConflictMarkers` (ALWAYS/NEVER spam, contradicting rules across files) is
cross-file and needs counting/structural logic Vale's per-line matching
can't do — if still wanted, follow `utils/scripts/lint-rules/README.md` §
Adding a rule (the W-numbered JS lint-rules system already does this class
of check for `docs/guardrails/_FORMAT.md`'s own F3/F4 caps) instead of
forcing it into a Vale existence rule.

### 4. Reuse the existing lint workflow — do not build a new one

Once step 1 wires the paths in, `npm run lint -- <path> --include-vale`,
`npm run lint:worklist`, and `npm run lint:ratchet*` already cover
lint/interpret/fix/re-lint for these paths — that's the whole point of
routing through the shared dispatcher instead of a bespoke script. Author a
new `.claude/skills/` skill only if a genuinely distinct workflow is needed
beyond running those commands; if so, follow the `writing-for-agents` skill's
conventions and check whether the existing `content-fixer` agent or
`enforce-with-linters` skill already covers "summarize findings by file,
apply fix, re-check" before writing new logic.

### 5. Self-correction policy — point at existing sources, don't duplicate

`.claude/rules/docs.md` already states this repo's guidance-authoring
standard (state current behavior only, no historical narration, no
meta-commentary, DRY — a fact lives in one file and everywhere else links to
it, terse). `docs/guardrails/_FORMAT.md` already binds every
`docs/guardrails/*.md` and `CLAUDE.md` edit (F1-F15: one line per rule,
imperative or trigger-clause opening, every prohibition carries its
replacement, length/CAPS budgets, single source of truth). New guidance for
fixing Vale findings in agent-instruction prose extends those two files —
add to them, don't write a third doc that restates or drifts from what they
already say.

### 6. Seed the ratchet baseline

Once the new paths are wired in and scanning, run `npm run lint:ratchet:seed`
(or `:sync`) so the existing baseline/ratchet mechanism — already tracking
findings across the wiki-lint scope, per the session-start "Ratchet: N over
baseline" report — starts covering these paths too, instead of building a
separate baseline report. Fix clear, safe violations the seed surfaces; file
genuinely ambiguous ones for a human per `PROJECT.md` PJ15's "2 failed fixes
-> stop and ask" rule.

## Constraints

- npm is this repo's package manager — every command is an `npm run` script (§ Deliverable 4), never `make`/`just`/a standalone shell script.
- Vale is already installed and already the repo's prose linter — extend it (new style + new `.vale.ini`/`.vale-hard.ini` sections), never add a second linter or reimplement a check `ai-tells`/`proselint`/`write-good` already does.
- Don't fold new rules into `CampaignOS` — that style is wiki-genre-tuned (§ intro); a wrong fold means re-litigating its exemption list for every agent-guidance path.
- Apply new rules to a handful of high-confidence findings first, not a repo-wide rewrite in one pass — `npm run lint:ratchet:seed` (§ Deliverable 6) establishes the baseline; drain it incrementally afterward.
- Don't invent policy — only enforce clarity/structure rules Anthropic's own guidance states (§ intro's WebFetch instruction).
- A finding that would delete substantive policy text, not just reword it -> stop and ask, don't guess intent.

## Success criteria

- `npm run lint -- CLAUDE.md docs/guardrails/ .claude/rules/ .claude/commands/ --include-vale` runs clean (or only pre-existing ratchet debt remains) — proof the scanner wiring (§ Deliverable 1) and the two configs (§ Deliverable 2) both work.
- `npm run lint:worklist` lists findings for these four paths where it listed none before.
- The new `AgentGuidance` style's rule count matches the "genuinely missing" list from § Objective best practices — no rule duplicates something `ai-tells`/`proselint`/`write-good` already catches.
- Root and nested `CLAUDE.md` files carry fewer hedges/AI-tells/conflicts after the fix pass than the seeded baseline recorded.
- Detailed procedures that were inline in an always-on file move to a skill or `content/runbooks/` entry, cited by path — never duplicated in both places.

## Method

1. Read `docs/vale-styles/ai-tells/*.yml` and `docs/vale-styles/CampaignOS/*.yml` in full; list which "Objective best practices" bullets already have a matching rule and which don't.
2. Look up Anthropic's current prompt/context-engineering guidance (WebFetch/official docs) and reconcile it against the "Objective best practices" list — add, drop, or sharpen bullets before writing any rule.
3. Extend `prose-scope.mjs`'s `INCLUDE_ROOTS` and `lint-dispatch.mjs`'s `routeType()` for the four gap paths (§ Deliverable 1); confirm with `node lint-dispatch.mjs --route <rel>` on a sample file from each path.
4. Create `docs/vale-styles/AgentGuidance/` with the rules the audit in step 1 found missing (§ Deliverable 3).
5. Add matching sections to `.vale.ini` and `.vale-hard.ini` for the four gap paths (§ Deliverable 2); run `vale` directly against a sample file from each to confirm the section actually applies (don't trust an unverified glob — this session's `[**/CLAUDE.md]` bug shipped silently for exactly that reason).
6. Run `npm run lint:ratchet:seed`, then fix the high-confidence findings it surfaces (§ Deliverable 6).
7. Point `.claude/rules/docs.md` / `docs/guardrails/_FORMAT.md` readers at the new check where relevant (§ Deliverable 5) — don't write a new standalone doc.
8. Report: what the scanner wiring changed, the new style's rule list, the seeded baseline count, and remaining findings left for a human.
