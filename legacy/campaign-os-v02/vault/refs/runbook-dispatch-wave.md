---
type: runbook
status: canon
publish: false
aliases: []
created: "2026-07-23"
updated: "2026-08-15"
tags: [craft]
summary: "Dispatch one agent per independent domain on an eight-point brief carrying pre-run lookups as answers, close each wave on wave-verifier, then integrate or targeted-fix-and-reverify."
phase: any
uid: f908bea1-9463-4d58-bc85-97f163698880
---

# Dispatch-wave runbook (any batch operation)

Drives any parallel-subagent batch operation in this repo: a MIGRATION-scale
content batch, campaign-writers-room's rival drafts, or transcript-ingest's
chunk extraction. Orchestrates dispatch and verification; it never restates
a spawned agent's own spec.

## When to use it

Dispatch a wave when the task splits into independent problem domains that
share no state. Each domain gets a self-contained brief and works in
isolation, producing its own output with no shared write dependencies in its
critical path. Repo precedent: campaign-writers-room dispatches one
`draft-writer` per stance in parallel (`.claude/skills/campaign-writers-room/SKILL.md`
Phase 3a step 1); transcript-ingest dispatches one `extractor` per ≤400-line
transcript chunk (`.claude/skills/transcript/SKILL.md`).

A batch whose units depend on each other is not automatically single-agent
work — most content batches are *partially* ordered, and § Staged waves
below handles them. Reserve the one-agent-full-context fallback for the
truly inseparable case: the same failure recurring across different places,
or every unit needing every other's output, where separate agents would
each reconstruct the same picture independently.

Treat "no shared state" as a working assumption. Even chunk-per-agent transcript
extraction can have soft shared-state hazards (sibling agents landing new pages
mid-run). See the parallel-dispatch caveat in `.claude/skills/transcript/references/entity-resolution.md`
for the re-check pattern that covers it.

## Decomposability check (precondition)

Before dispatching, confirm the task actually decomposes:

- Each domain's brief is self-contained. No domain in the same wave
  depends on another's output to start or finish — a dependency moves the
  dependent domain to a later wave (§ Staged waves), it does not force
  single-agent work.
- No two instances write the same file. Shared hub pages (`*-overview.md`,
  router/reference pages many domains touch) are owned by exactly one
  agent per wave or left to the orchestrator's integration step — never
  listed in two briefs.
- An agent is worth using at all only where tool restriction or context
  isolation applies (see `vault/refs/runbook-agents.md`'s opening). Otherwise a
  skill in the main loop is simpler and more debuggable, wave or no wave.

Any of these fails → stage the batch (§ Staged waves) if it is merely
partially ordered, or fall back to single-agent full-context investigation
or authoring only when it cannot be partially ordered at all.

## Staged waves (dependent batches)

Most content batches are partially ordered, not independent: the encounter
brief needs the NPC page's facts, the run-guide row needs the moment's
slug. Staging keeps the parallel dispatch while honoring the order.

- **The ordering rule:** a unit whose *brief needs facts from* another
  unit goes in a later wave than that unit. Units that merely wikilink
  each other share a wave — the stub rule
  (`vault/refs/vault/_common/handoffs.md`) covers the link, so a link
  alone is never a dependency.
- **Typical order** for a prep batch: entities (NPC, location, item,
  faction) → compositions that cite their facts (encounters, moments,
  forks, travel legs) → aggregators that index the compositions (run
  guide, DM screen).
- **Between waves, sequential:** wave N+1's briefs are written only after
  wave N closes (both close checks in step 4 below), because those briefs
  quote facts from wave N's verified pages — quoting an unverified page
  propagates its defects into every downstream brief.
- **Within a wave**, everything in § The sequence applies unchanged: one
  focused agent per domain, in parallel, max 5 concurrent.

A batch where every unit needs every other's output has no valid staging
→ single-agent full-context work.

## The sequence

0. Open the wave record at `.claude/waves/<wave-slug>.md`, first line
   `# Wave: <slug>: <one-line goal>`. Every step below appends one line to
   it. Conversation memory does not survive compaction; this record and
   `git log` do, and after a compaction they are authoritative.
   A record already naming this wave is resumable. Domains with a
   `domain <name>: complete` entry have finished, do not re-dispatch them.
1. Identify the domains and write one self-contained brief per domain:
   facts, paths, and output location; no shared file writes between
   instances. Derive the domain list, don't guess it: the routed rung's
   own artifact checklist (its skill or guide names the files), plus
   every entity the source material names that has no page yet — each
   one a domain per `draft-content`'s path table. Group the domains into
   waves per § Staged waves. Append `domains: <list>` (prefix each with
   its wave number when staged: `w1:npc-thera, w2:moment-2-ambush`).
2. Dispatch one focused agent per domain, in parallel (one message, N
   instances), each with an **explicit `model:`** (an omitted model
   inherits the session's context, silently defeating model-per-job choice).
   Never an agent spawning further agents (`vault/refs/runbook-agents.md` §
   Anti-patterns, "Agent chains > 2 deep"). Every domain brief MUST contain
   this eight-point contract verbatim (REFACTOR-PLAN.md P1.3 — transcript
   mining measured the cost of omitting each point):

   ```text
   1. Read any file before you Edit or Write it.
   2. Before your FIRST edit under vault/**, _templates/**: Read
      docs/guardrails/WIKI.md. Before your first edit to a
      code/config file (.mjs/.js/.sh/.json/...): Read docs/guardrails/CODE.md.
      A PreToolUse guard denies every edit until that Read appears in your
      own transcript — do the Read before queuing any Edit; each Edit
      batched ahead of it costs one denied call.
   3. The current path scheme, stated explicitly: wiki content lives under
      vault/ (PCs at vault/campaigns/shattered-sea/pcs/, agent-facing
      reference flat under vault/refs/, typed drafting guides under
      vault/refs/vault/<type>/); there is NO top-level sessions/, sys/,
      pcs/, or world/.
   4. You are a leaf worker: never call the Agent tool, never spawn
      subagents, do the work yourself. Any "delegate to a background
      Agent" line you meet in a guardrail doc (PROJECT.md PJ15, CODE.md
      C16a, EFFICIENCY.md E8) is for the orchestrator, not you -> fix
      what fits your task inline and list the rest in your completion
      report.
   5. The exact verification command you must run before reporting done,
      and the requirement to paste its real output.
   6. The exact file list you own — small explicit lists beat open-ended
      batches; a single-file lint-fix worker (the only Haiku use) gets
      exactly one file.
   7. Read docs/guardrails/EFFICIENCY.md before your first tool call —
      batching, named-check-only verification, and the report shape bind
      every worker.
   8. The lookups you already ran, pasted as answers — never as commands
      for the worker to re-run. Run each shared query ONCE yourself and
      paste its real output into every brief that needs it: the sibling
      sweep's hit list, the party's level and weakness lines, the target's
      current stock, the neighbour pages' values, the exact template path.
      A command handed to N workers is paid N times and returns a
      different answer to each as the wave writes underneath them. Name a
      command only where the worker must see state its OWN edits produced.
   ```

3. Collect each instance's output: the path it wrote plus its own short
   self-report, never the full content pasted back into the parent's
   context. Append `domain <name>: <paths> (<agent id>)`.
4. A wave closes ONLY on both of these — mandatory, not a judgment call:
   1. **`wave-verifier` PASS** over the wave's touched paths, not the
      agents that wrote them. Full spec, tools, and acceptance contract:
      `.claude/agents/wave-verifier.md`. Never
      make the verifier write-capable (`vault/refs/runbook-agents.md` §
      Anti-patterns, "Write-capable checkers"). Never tell it what not to
      flag. Saying "don't treat X as a defect" pre-judges the review;
      instead let it raise the finding and rule on it below.
   2. **The orchestrator's own re-run of the wave's measuring command**,
      pasted output — never trust a subagent's self-report (the exact
      REFACTOR-PLAN.md orchestrator-contract failure mode: session e8244a,
      a subagent claimed a clean report behind 112 unfixed lint errors).
      `node utils/scripts/rerun-check.mjs <check> <file...>` runs a named
      check (`lint`, `test`, or an explicit command) against exactly the
      wave's touched-path list and prints one verdict line — use it
      instead of re-deriving a judgment call each time.
   A wave-verifier PASS with no independent re-run, or a re-run with no
   wave-verifier dispatch, is an unclosed wave — neither alone is enough.
5. `PASS` (both checks green) → integrate/commit, append `domain <name>:
   complete`. Either check `FAIL` → enter the fix loop.

## Branch-isolation dispatch (walking a situation's live branches)

Walking a Situation's Live Branches rows into a branching chain of Beats
is a distinct dispatch pattern on top of § The sequence above — the loop,
the isolation clause, and termination rules live in
`vault/refs/runbook-dispatch-wave-branch-isolation.md`.

## The fix loop: two rounds, then rule

A round is one targeted fix dispatch plus one re-verify over exactly the
paths the verdict identified, never a full re-dispatch of the wave. Cap at two
rounds per domain, matching project law L5 for failed lint fixes. A loop
surviving two rounds reveals a structural problem with the wave brief itself,
requiring redesign rather than further attempts. Append `domain <name>: round <R>/2: <what changed>`
each time.

Never fix a finding yourself in the orchestrator -> dispatch the fix to a
targeted agent instead; a controller fix skips verification entirely and
wastes the context the wave protects.

At the cap, rule on every still-open finding, one entry each. Never drop
findings silently:

- The finding is wrong or contestable → `parked: <finding>: ruling: <why
  the page stands>`.
- Real, but nothing downstream depends on it → `parked: <finding>:
  ruling: real, deferred`.
- Real and blocking (another domain depends on it, or it exposes a flawed
  brief) → `BLOCKED: <reason>`, stop the wave, surface it to the DM with
  the finding and the brief text it collides with.

## Terminal states

A wave ends in exactly one, recorded in its final entry. An exhausted
budget is never reported as success:

`complete` · `clean no-op` (nothing needed changing) · `blocked` ·
`exhausted` (cap hit, findings parked with rulings) · `stagnated` (a round
produced no measurable progress. Stop the wave rather than inventing another attempt).

Done = every domain at `complete`, or at `exhausted` with every open finding
carrying a ruling. Then commit `<verb>(sNN): ...` per the project's phase
markers and commit verb conventions.
