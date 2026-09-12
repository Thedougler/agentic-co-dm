# Contract: Ownership layout

After repair, these paths have these jobs.

## Canonical

| Path | Role |
|---|---|
| `AGENTS.md` | Operating map. May contain SPECKIT live-context markers. |
| `.specify/memory/constitution.md` | Principles. |
| `specs/*/spec.md` | Feature requirements. |
| `docs/agents/harness-dispatch.md` | Orchestrator procedure. |

## Shims (import only)

| Path | Must contain | Must not contain |
|---|---|---|
| `.claude/CLAUDE.md` | `@../AGENTS.md` | Wiki routing, constitution, specs |
| `.omp/AGENTS.md` | `@../AGENTS.md` | SPECKIT block, wiki routing copy |

## Forbidden after repair

- Root `CLAUDE.md`
- Hand-copied `**/commands/speckit.*` not in the current manifest
- Unique project rules inside generated `speckit-*` / `speckit.*` adapters
- Bot-local Spec Kit packs (`.grok-bot/speckit/` or equivalent)

## Harness runtime (genuine deltas only)

| Path | Allowed |
|---|---|
| `.omp/config.yml` | Model roles, caps, isolation, `disabledExtensions` for Claude project context |
| `.omp/RULES.md` | OMP sticky safety constraints |
| `.claude/settings.json` | Claude runtime only, if needed |
| User `~/.grok/config.toml` | `[compat.claude]` isolation (documented, not repo-enforced) |

## Generated (disposable)

Spec Kit owns these. Humans do not edit them to add policy.

- `.agents/skills/speckit-*/`
- `.grok/skills/speckit-*/`
- `.omp/commands/speckit.*`
- `.claude/skills/speckit-*/`
