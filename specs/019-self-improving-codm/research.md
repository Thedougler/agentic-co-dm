# Research: Self-Improving Co-DM

## Decision: No new skill

**Rationale**: The loop is standing behavior plus one wrapup offer. A new skill would be standing load and a 016 design-impact create. IX: extra tokens for the same outcome.

**Alternatives considered**: A `self-improve` skill agents load every sitting. Rejected — it is wasted context when wrapup and `AGENTS.md` already run.

## Decision: Session-wrapup owns the required reflection; AGENTS.md owns the rest

**Rationale**: FR-008 is wrapup-window Work. `session-wrapup` already owns that window. Adding a required chat reflection changes that skill’s workflow → design-impact (016). Table aim ask, gap-no-stall, token record, helpers, ledger, layout are standing and belong in `AGENTS.md` / `work.md` (session agent).

**Alternatives considered**: Put reflection only in `AGENTS.md`. Rejected — wrapup agents that load the skill and skip `AGENTS.md` extras would drop FR-008. Put all of 019 into wrapup. Rejected — prep sittings need aim/token/helpers too.

## Decision: Token cost is what was loaded and finished, not a tokenizer

**Rationale**: Hosts do not share one token API. Spec defines token cost as how much the Co-DM must read and write. Record sitting kind, jobs done, paths read, skills loaded, helpers used, waste named, errors filled. Same-kind comparison: fewer unrelated paths/skills for the same jobs.

**Alternatives considered**: Depend on harness token counters. Rejected — not portable. Estimate tokens with a library. Rejected — extra dependency for no extra outcome.

## Decision: `errors.md` at repo root; one helper operates it

**Rationale**: Owner named `errors.md`. It is agent-owned, not canon, so not a wiki page. Fill/drain repeats → FR-026 helper. Command: append, drain (only with cause fixed), list. Args in, JSON or Markdown out, non-zero if drain-without-fix.

**Alternatives considered**: Vault page. Rejected — it would look like canon and hit the accept-gate. Chat-only errors. Rejected — not durable across sittings. Hand-edit only. Rejected — the job repeats.

## Decision: Sitting records ride the same helper

**Rationale**: Recording a sitting also repeats. One CLI with `sitting` and `error` subcommands avoids a second wrapper. Persist next to `errors.md` (append-only Markdown or JSONL the helper owns).

**Alternatives considered**: A second script. Rejected — XIV and IX. Vault `log.md`. Rejected — mixes wiki activity with agent ops.

## Decision: Table aim is a wiki fact on the campaign hub

**Rationale**: Who the players are and current intent is campaign fact. DM records it; Co-DM asks if missing (FR-003). File on the existing campaign hub after accept. Do not invent a new wiki kind.

**Alternatives considered**: Repo-side config. Rejected — the DM’s second brain is the wiki. Chat-only aim. Rejected — not inspectable next sitting.

## Decision: Wiki layout is not a canon write; wiki facts still are

**Rationale**: Owner: self-org includes llm-wiki. Spec: regrouping without changing facts is layout; agents own it; links must still resolve. FR-015 carve-out. Silent fact edits via “move” stay invalid.

**Alternatives considered**: Every wiki path change needs accept (earlier draft). Rejected by owner. Ingest-engine rewrite of destinations. Rejected — existing kind folders already exist; 019 is the growth pass when mixes appear, not a new compiler.

## Decision: Helpers only when the job repeats and no command exists

**Rationale**: FR-026–FR-031. XIV: run the existing command. VII: no speculative scripts. Stale helpers are wasted context (FR-027).

**Alternatives considered**: Generate a helper per sitting. Rejected — one-off. Wrap `qmd` / git. Rejected — XIV.

## Decision: 012 does not gate this feature’s wrapup add

**Rationale**: The wrapup change is a chat reflection offer, not a change to how D&D wiki log bands are written. 012 applies when D&D content-producing guidance changes. If implement later rewrites session-log shape, 012 binds then.

**Alternatives considered**: Blind-eval every reflection. Rejected — reflections are DM Work, not wiki content samples.

## Decision: Tests observe files and chat Work, not skill prose

**Rationale**: IV. Fixture: ledger append/drain, sitting fields, mixed-dump layout (repo + wiki kinds) → one-job load, reflection present as chat Work, fact write still gated.

**Alternatives considered**: Grep `AGENTS.md` for slogans. Rejected.
