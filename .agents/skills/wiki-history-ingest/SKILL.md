---
name: wiki-history-ingest
description: >
  Unified wiki-history-ingest entrypoint for conversation/session sources. Use this when the user says
  "/wiki-history-ingest claude", "/wiki-history-ingest copilot", "/wiki-history-ingest codex",
  "/wiki-history-ingest pi", or asks to ingest agent history without naming the underlying skill.
  This router dispatches to the specialized history skill.
---

# Unified History Ingest Router

This is a thin router for **history sources only**. It does not replace `wiki-ingest` for documents.
## Capability Boundary

**Input** — One explicit history target or an inferable source path, the user's original ingest objective, and only the bounded routing context needed to choose a destination owner. The router may inspect the command/path and relevant config, but does not load destination sessions, a full manifest, or unrelated vault artifacts.

**Work** — `wiki-history-ingest` owns source classification and direct dispatch only. It preserves the destination skill's specialized ingest, approval, canon, and tracking procedure; it does not duplicate or partially execute that work.

**Done** — A route closes only with an explicit destination dispatch, or with the single documented clarification for an ambiguous source. It must not claim pages, manifest/index/log/hot updates, validation, or QMD completion until the destination owner returns that evidence. A missing or invalid route ends with a specific blocker.

**Capability Handoff** — Pass the selected history owner, source path/target, and parent objective to the specialized history skill. The destination owner returns selected evidence, page/tracking results, scoped validation, and any one-time QMD retrieval result; then this router returns that bounded result to the caller without re-running or re-finalizing it.


## Subcommands

If the user invokes `/wiki-history-ingest <target>` (or equivalent text command), dispatch directly:

| Subcommand | Route To |
|---|---|
| `claude` | `claude-history-ingest` |
| `copilot` | `copilot-history-ingest` |
| `codex` | `codex-history-ingest` |
| `hermes` | `hermes-history-ingest` |
| `openclaw` | `openclaw-history-ingest` |
| `pi` | `pi-history-ingest` |
| `auto` | infer from context using rules below |

## Routing Rules

1. If the user explicitly says `claude`, `copilot`, `codex`, `hermes`, `openclaw`, or `pi`, route directly.
2. If the user provides a path/source:
   - `~/.claude` or Claude memory/session JSONL artifacts -> `claude-history-ingest`
   - `~/.copilot`, `session-store.db`, VS Code copilot-chat transcripts -> `copilot-history-ingest`
   - `~/.codex` or rollout/session index artifacts -> `codex-history-ingest`
   - `~/.hermes` or Hermes memories/session artifacts -> `hermes-history-ingest`
   - `~/.openclaw` or OpenClaw MEMORY.md/session JSONL artifacts -> `openclaw-history-ingest`
   - `~/.pi/agent/sessions` or Pi session JSONL artifacts -> `pi-history-ingest`
3. If ambiguous, ask one short clarification:
   - "Should I ingest `claude`, `copilot`, `codex`, `hermes`, `openclaw`, or `pi` history?"

## Execution Contract

- After routing, execute the destination skill's workflow exactly.
- Do not duplicate destination logic in this file.
- Leave manifest/index/log update semantics to the destination skill.

## UX Convention

- Use `wiki-ingest` for **documents/content sources**
- Use `wiki-history-ingest` for **agent history sources**

Examples:

- `/wiki-history-ingest claude`
- `/wiki-history-ingest copilot`
- `/wiki-history-ingest codex`
- `/wiki-history-ingest hermes`
- `/wiki-history-ingest openclaw`
- `/wiki-history-ingest pi`
- `$wiki-history-ingest claude` (agents that use `$skill` invocation)
- `$wiki-history-ingest copilot`
