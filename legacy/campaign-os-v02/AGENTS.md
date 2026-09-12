<!-- guardrails-kit: v1.15-project -->
<!-- BEGIN KIT CORE v1.0 -->
<!-- Editing this file? Read docs/guardrails/_FORMAT.md first. Never paraphrase kit text. -->
These rules compensate for known model failure modes. They are procedures, not advice — follow them literally.

## Routing — the moment X happens, your next tool call is Read on the doc

| The moment you... | Read |
|---|---|
| notice the user proposing, asking to brainstorm, or steering toward a story idea, plot direction, or NPC/faction/quest concept, with no target vault/ page identified yet — or floating a "what if" reinterpretation of pages that already exist, with no direction chosen yet | docs/guardrails/IDEA.md |
| realize — at start or mid-task — the task needs >2 file edits or edits in >1 top-level directory, or are about to Edit a 3rd file with no TASK block posted | docs/guardrails/PLAN.md |
| are about to create or modify a file under vault/** or _templates/** — by Edit, Write, or a shell command that writes files — for the first time since session start or the last compaction | docs/guardrails/WIKI.md |
| are about to create or modify a code/config file (.mjs, .js, .ts, .tsx, .py, .sh, .json, .jsonc, .yml, .yaml, .css, .scss, .toml — never .md) — by Edit, Write, or a shell command that writes files — for the first time since session start or the last compaction | docs/guardrails/CODE.md |
| see a test you expected to pass fail, a build/test/run command exit non-zero, a traceback, run output that contradicts your prediction, or a user-reported bug you have not reproduced this session | docs/guardrails/DEBUG.md |
| are about to write "done", "fixed", "works", "passing", "complete", "resolved", or "ready", or to run git commit / gh pr create | docs/guardrails/VERIFY.md |
| start any task needing 2+ tool calls (a session's first request, or a dispatched brief's first act), or are about to Read a 3rd file over 300 lines, or a search returned >50 hits | docs/guardrails/EFFICIENCY.md |
| no other routing row matches | docs/guardrails/PLAN.md |

Before your first tool call OR written response each turn: check every row above against what you're about to do — a row can match plain text you're about to write, not only a tool call, and this check runs every turn, not just once per session. Row matched: write `TRIGGER: <event> -> <doc>`; your next tool call is Read on that doc, in the same message, with no acting tool call beside it (other triggered Reads may batch with it). 2+ rows match at once? Write one TRIGGER line per row and Read each matched doc, in table order, before any other tool call. Already Read the doc since the last compaction? Write `TRIGGER: <event> -> <doc> (cached: <its checklist IDs, from memory>)` and obey those items — cannot list the IDs without looking? It is not cached: Read the doc. A TRIGGER line whose next tool call is not that Read is itself a violation.

## Iron rules

- Before your first Edit of a file: Read the enclosing function/class plus the import block — a Grep snippet is not a Read; under 250 lines, Read it all (guessed edits patch the wrong code).
- Modify existing files with Edit, never Write — sole exception: the rewrite procedure in docs/guardrails/CODE.md; if Edit fails twice, re-Read the region and retry Edit (memory rewrites delete real code).
- After changing any signature, symbol name, return shape, config key, route, CLI flag, env var, or enum member: run REFERENCE SWEEP per docs/guardrails/CODE.md (missed callers break silently).
- Before calling an unfamiliar or third-party API with 2+ arguments: paste its real signature per docs/guardrails/CODE.md C5 (plausible is not real).
- Claim done/fixed/works/passing/complete/resolved/ready only beside fresh command output in the same turn; otherwise report `EDITED-UNVERIFIED: <file>` (unrun code is unknown code).
- Never write "should work", "should fix", "likely resolves", or "ought to now" — only the two legal forms in docs/guardrails/VERIFY.md: `Verified: <command> -> <result line>` / `UNVERIFIED — to confirm, run: <command>` (hedges hide skipped runs).
- Treat the user's stated bug location or cause as a hypothesis; trace evidence to file:line before editing there (wrong premise wastes the fix).
- Change only lines the task requires; log other findings as `NOTED (not done): <thing> <file:line>` (drive-by edits are unreviewed bugs).
- Never truthiness-check a value that can be 0, "", or false — compare to null/undefined/None explicitly; JS defaults use ?? (zero is data).
- About to write "probably / presumably / likely / I assume / should be" about this repo's code: run the Grep or Read that answers it instead (a guess costs 10x the lookup).
- Batch independent tool calls into one message; between calls write at most one line, findings and decisions only — details: docs/guardrails/EFFICIENCY.md E5/E6 (narration buries findings).

<!-- END KIT CORE -->

## Project — Campaign OS rules

<!-- Project-specific commands, ports, paths, and constraints go below this line. Cap: 40 lines. -->
campaign-os loads when working ON this system itself (skills/rules/hooks/linters), not automatically — see the process-engineering bullet below. campaign-os and llm-wiki are repo skills, read at `.claude/skills/<name>/SKILL.md`; flag-the-gap is user-level (`~/.claude/skills/flag-the-gap/`) and is reached with the Skill tool — a repo-relative Read or grep for it returns nothing.

1. Repo is the sole source of truth. NEVER state a campaign fact from memory — `npm run search:content -- query "<topic>"` (qmd hybrid search) and paste the hit first; a known exact heading/string in a file you're about to Read anyway still uses Grep (L1).
2. Numbers: pending diff > 40 lines → review in chunks of 20; 2 failed fixes of the same lint → stop and ask the human (L5).

- Starting any task in this repo (a session's first request or a dispatched brief's first act) → read `index.md` (wiki orientation) and `hot.md` (recent changes) before acting — these are capped at 100 and 50 lines respectively
- About to write prose a DM or player reads (read-aloud, recap, handout, lore, NPC page prose, story, run-guide) → chain-load `writing-player-prose` first
- About to write text an agent reads (skill body, CLAUDE.md section, runbook, agent spec, docs/guardrails file) → chain-load `writing-for-agents` first
- About to prep a session, write a beat, draft a story, design an encounter, or create/edit content under `vault/campaigns/` → read `vault/campaigns/shattered-sea/campaign-overview.md` (campaign identity and tone), `vault/campaigns/shattered-sea/threads.md` (active narrative pressure), `vault/campaigns/shattered-sea/player-gravity.md` (what players bite on), and `vault/campaigns/shattered-sea/party-items.md` (what the party has) first
- Never read `vault/campaigns/shattered-sea/spoilers.md` unless the DM explicitly asks to include spoilers, secrets, foreshadowing, or hints in the content being written — reading it without that direction contaminates output with facts the party does not know
- About to finish creating or editing a `vault/**` file → update `hot.md` with one line: `- YYYY-MM-DD type | short note` (keeps hot.md self-maintaining)
- User says "prep the session", "get me the prep", "prep for <day>", or you are about to write an episode overview, run-guide, `beat-*.md`, or a Situation's Beat Chart for an unplayed session → chain-load `composing-beats` (the default prep method, ADR-0060; a beat is the only atomic playable unit, ADR-0061). The session's story at `vault/episodes/NNN/session-NN-*.md` must already exist; none there → chain-load draft-story and write it first, never derive prep from a sketch, notes, or "the thinking is already done", however close the deadline (W47 fails the lint anyway)
- About to write a single Hook/Development/Cliffhanger/Climax/Resolution beat, or opening pressure for a dramatic unit → chain-load that type's beat skill (`writing-hook-beats`, `writing-development-beats`, `writing-cliffhanger-beats`, `writing-climax-beats`, `writing-resolution-beats`); a cold open / pre-Hook prelude from a borrowed NPC POV → `writing-cold-opens`; composing or resequencing more than one beat → `composing-beats`
- About to design a trap, puzzle, hazard, or trial the party can beat by play → chain-load `writing-traps-trials`
- User corrects a word choice, sentence, rhythm, or prose habit in the agent's writing — for ANY content, in ANY task, not only a dedicated editing pass → capture the correction into vault/refs/stories/prose-aesthetic.md (a never-do goes in vault/refs/stories/banned-patterns.md) same turn, never deferred
- DM names a favourite book, author, or film, hands over a sample of their own writing, or asks to set or extend the voice of generated content → chain-load writing-style, which researches each named work and appends the moves to vault/refs/stories/influences.md and the profile (the row above catches a correction mid-draft; this one catches the deliberate pass)
- About to finish an edit to a vault/**.md or code/config file → run `npm run lint -- <path>` yourself. Output is an instruction list (ADR-0064): `FILE REWRITTEN by autofix` → Read the file again before further edits; a finding with a FIX line → obey it same turn, satisfying the rule's intent — rewording to dodge the pattern is a violation; a genuine false positive → fix the rule's term list, not the instance; cannot fix after 2 attempts → quote it and stop (L5); never disposition it as pre-existing/NOTED. A FIX line needs more than one imperative → `npm run lint:explain -- <RULE>`. Every prose check reaches the file through this one command (vault/refs/runbook-commands.md § Lint).
- `npm run lint:bench` prints `PERF OVER BUDGET`, or you are about to write "lint is slow", "the sweep takes", "skip the lint for now", or run a lint command a 2nd time because the 1st was too broad → tune the named producer at the path the PERF block prints, re-run `npm run lint:bench`, and paste the delta — never route around the linter, drop a producer, or leave the slowdown for the next session (every session re-pays it)
- An existing page or file conflicting with current `vault/_templates/` or lint is wrong — fix it or `/drain` it, never replicate its shape into new work (precedent isn't evidence; templates + linters are)
- Found any fixable issue in a file already in your context — bug, canon conflict, QC fail, lint debt, doc/spec violation (e.g. a word-count cap), stale reference — fix it this turn or dispatch a background Agent (explicit non-fable model, smallest/quickest model that can do the fix — Haiku by default, step up only if the fix needs subagents of its own, no push), even if pre-existing or outside the task's original scope (overrides the kit iron rule's NOTED default for anything actionable now). The dispatch option is main thread/orchestrator only — a dispatched subagent (leaf worker) never calls the Agent tool: it fixes what fits its own task inline and lists the rest in its completion report for the orchestrator to dispatch. NEVER park it as a marker/suggestion/task-chip, and canon/story problems NEVER become GitHub issues (vault/refs/issue-tracker.md). `NOTED (not done)` stays valid only for a finding genuinely outside this session's reach — a file you never opened, or one only a DM can judge.
- About to write or relay "no X exists", "no X anywhere in the vault", "canon does not document X", or a subagent's CONFLICT/MISSING block → run the search yourself before it reaches the DM (`npm run search:content -- query "X"` AND `grep -rni "X" vault/`, vault/campaigns/shattered-sea/pcs/ included — a PC's own sheet and combat profile are canon and subagents routinely miss them), then paste the hit or the literal zero-result line. Never relay an absence you did not personally search for, and never write the verdict in the same message as the plan to check it — no "I'll grep, and confirmed: no bows exist". The search output goes on the page first, the verdict after it, or you have verified nothing. Search comes back empty → the next bullet's duh test runs before the DM hears anything (L1)
- About to write "needs your ruling", "your call", "should I", "which files should I target", an AskUserQuestion, or an add-it-to-canon vs change-the-story fork → STOP and apply the duh test first: would a real culture/place/person in this world obviously already have this (a spear-and-poison culture also has bows, a port has rope, a city has beggars)? Yes → it is a gap in the wiki, not a gap in the world: write the one-line canon addition yourself this turn and report that you did, no fork offered. The DM's answer to a duh-test question is "duh", and asking it costs him a round-trip he is paying for. Escalate ONLY what a player would notice or a plot would turn on
- Write only what the template or task asks — no anticipatory notes, no beyond-scope "helpful" additions (extra content is the next session's context poison; W38 + Vale CampaignOS.NonData/StaleWorkMarkers enforce)
- About to improve `vault/_templates/`, a `.claude/skills/` skill, or any other campaign-os element → search craft docs first (`npm run search:craft -- query "<topic>"`) — no element of campaign-os is sacred; that material holds real GM-expert D&D methodology (5e SRD, Sly Flourish's LGMRD/Monster Builder) to improve against, not just campaign facts. Every search and lint command, and which question each answers: vault/refs/runbook-commands.md
- DM makes a table-level ruling, a new mechanic/concept needs its name picked, or 2+ names are in circulation for one thing → chain-load campaign-domain-modeling
- DM asks for a whole-wiki health/cleanup pass, or a bulk import/pull just landed → read vault/refs/runbook-maintain.md
- About to build or extend a `.claude/skills/` skill, hook, linter, or other process-engineering feature → chain-load campaign-os, then read CONTEXT.md + docs/adr/ first for existing domain decisions (the process domain, distinct from campaign-domain-modeling's DM-ruling domain above)
- Never use the WebFetch tool to fetch a URL → run `trafilatura -u '<url>'` instead (strips boilerplate to clean text; installed at /opt/homebrew/bin/trafilatura)

Subtree-scoped rules (vault/ — including its vault/campaigns/shattered-sea/pcs/ and vault/episodes/ subtrees, utils/, docs/, .claude/, inbox/, raw/) live in that dir's own CLAUDE.md — loaded automatically once Claude reads a file there, not restated here.

<!-- BEGIN KIT FOOTER v1.0 -->

## Agent skills

### Issue tracker

Issues live as local markdown files under `.scratch/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default label vocabulary (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix). See `docs/agents/triage-labels.md`.

### Domain docs

Multi-context layout — `CONTEXT-MAP.md` at the repo root indexes each context's `CONTEXT.md`. See `docs/agents/domain.md`.

## Hard stops

- NEVER make a failing test or check pass by weakening it — no skips, deleted tests, loosened asserts, raised tolerances, widened catch blocks, `as any` / `# type: ignore`, lint-disables -> instead: quote the failure, propose the change, wait for approval (a silenced check certifies the regression).
- Commit and push automatically by default — the main thread/orchestrator pushes after each wave-close or milestone commit; parallel subagents still never push (concurrent pushes race), the orchestrator pushes for them.
- NEVER kill processes by image name (`taskkill /IM node.exe`, `pkill node`) -> instead: find the PID via the port (`lsof -ti :PORT` | `netstat -ano | findstr :PORT`) then kill that PID (image-name kills take down your own harness).
- NEVER delete tracked files/branches or run `git reset --hard` / `git checkout -- <file>` without pasting what will be lost -> instead: paste the exact target list and wait for the user's approval in this conversation (deletion is unrecoverable). Exception: an untracked file this session's own work created by mistake (a stray scaffold, an abandoned template stub) may be `rm`'d directly, no approval needed (`git status` confirms untracked -> housekeeping, not history loss).

Docs read before compaction no longer count as read: `(cached)` is invalid until you Read the doc again.
<!-- END KIT FOOTER -->
