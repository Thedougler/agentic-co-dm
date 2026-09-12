# Research: OMP Spec Kit Integration

## Native integration already present

**Decision**: Do not re-run `specify init`. Verify `integration: omp` and fill missing baseline files only.

**Rationale**: `.specify/init-options.json` and `.specify/integration.json` already record `omp`. `.omp/commands/` already has generated `speckit.*` commands (including `speckit.converge` and `speckit.agent-context.update`). FR-022 forbids wiping Spec Kit state.

**Alternatives considered**: Fresh `specify init . --integration omp` — destructive and unnecessary. Generic adapter — forbidden by FR-001.

## Live context file

**Decision**: Set `.specify/extensions/agent-context/agent-context-config.yml` `context_file: .omp/AGENTS.md`. Unmanaged preamble of that file is `@../AGENTS.md`. Spec Kit writes only between `<!-- SPECKIT START -->` / `<!-- SPECKIT END -->`.

**Rationale**: OMP native `.omp/AGENTS.md` outranks root `AGENTS.md` at the same directory. Root `AGENTS.md` is load-bearing wiki/skill routing. Import preserves it without duplicating meaning. Agent-context is already installed; default for `omp` would otherwise write root `AGENTS.md`.

**Alternatives considered**: Let the omp default target root `AGENTS.md` — misses FR-005 highest-priority file. Copy wiki routing into `.omp/AGENTS.md` — duplicates FR-008. Delete root `AGENTS.md` — breaks non-OMP readers and constitution “runtime guidance is AGENTS.md.”

## Sticky rules vs live context

**Decision**: `.omp/RULES.md` holds only the five safety constraints (verify; generated files; no push/deploy unless asked; map to tasks; completion needs evidence). Feature-current text stays in the Spec Kit-managed block.

**Rationale**: OMP compaction keeps RULES; agent-context overwrites the managed AGENTS section. Mixing them would either compact away the feature or let the updater clobber rules.

**Alternatives considered**: All standing instruction in AGENTS.md — rules die on compaction. All in RULES.md — feature pointers go stale or bloat every turn.

## Project OMP config

**Decision**: Add `.omp/config.yml` with `modelRoleStorage: project` and the spec baseline: `task.batch: true`, `maxConcurrency: 4`, `maxRecursionDepth: 1`, `isolation.enabled: true`, `advisor.enabled: false`, `memory.backend: off`, `autolearn.enabled: false`, compaction on, `tools.approvalMode: write`, LSP on. Role aliases: `@plan`/`@review` = strong reasoning high; `@task` = fast coding medium; `@smol` = cheap low; `@default` = balanced medium. Seed concrete model IDs from the maintainer’s current user config so the project runs; change IDs only in this file.

**Rationale**: User config has no `review` role and `task` at low effort. Project file is the one place FR-014 requires. Caps and recursion are the public seam for SC-004.

**Alternatives considered**: Rely on user `~/.omp/agent/config.yml` — not repo-owned, missing `review`, wider concurrency defaults. Per-agent model strings — violates FR-014.

## Specialists

**Decision**: Three project agents only: `spec-auditor`, `implementer`, `verifier`. All `spawns: []`. Auditor and verifier: read-only tools, `blocking: true`, `thinking-level: high`. Implementer: edit/write/bash/lsp. Isolation requested at delegation time, not frontmatter. No agents named after Spec Kit phases.

**Rationale**: FR-004/013. Isolation is per-task in OMP, not agent YAML.

**Alternatives considered**: Generic `task` agent for everything — FR-013. Phase-named agents (`specify-agent`) — FR-004. `spawns` to nested workers — FR-012.

## Orchestration

**Decision**: One new command `.omp/commands/feature-fast.md`. It sequences unmodified `/speckit.*` commands, then OMP `task` batches of `implementer`, then `/speckit.converge`, then `verifier`. Do not edit generated `speckit.*`. Do not introduce a Spec Kit workflow YAML that re-owns implementation waves. Primary path: direct OMP CLI session.

**Rationale**: FR-018/019/020. Spec Kit already owns the macro lifecycle; OMP batch owns one wave.

**Alternatives considered**: Patch `speckit.implement.md` — upgrade-hostile. Spec Kit workflow + OMP Swarm both driving the same DAG — FR-019. RPC/ACP as default — FR-020; current OMP RPC resets `task.*`.

## Memory, advisor, MCP, duplicate clients

**Decision**: Advisor off. Memory backend off. Autolearn off. Do not add `.omp/mcp.json` in this feature. Do not add CLAUDE.md / Copilot twins.

**Rationale**: FR-007/015/021/008. Foundry MCP already exists at user/session scope; this baseline does not need a project MCP file.

**Alternatives considered**: Global advisor as continuous review — taxes every turn (FR-015). Autolearn skills as project memory — competes with spec (FR-007).

## Verification seam

**Decision**: One agent-shaped script `scripts/check-omp-baseline.sh`: args none, stdout short status, exit 0/1. Observes files and keys from the contracts. No test framework. Quickstart is the human/agent run guide.

**Rationale**: Constitution IV/VI. Public seam is the baseline files, not OMP internals.

**Alternatives considered**: No script (quickstart-only) — not agent-shaped. Pytest suite over YAML — bulk suite, couples to incidental keys.

## Domain language

**Decision**: Do not add harness-ops terms to `CONTEXT.md`.

**Rationale**: CONTEXT.md is campaign glossary. Its **Redesign** entry forbids operational grain as domain language. This feature is repository operating procedure, not a second bounded context.

**Alternatives considered**: Glossary entries for “thin orchestrator” etc. — pollutes campaign language. `CONTEXT-MAP.md` — unjustified second context.
