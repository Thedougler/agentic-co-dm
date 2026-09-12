# Quickstart: DRY Multi-Harness Spec Kit

Validate repair. Do not force-init. Do not switch git branches unless asked.

## Prerequisites

- Repo root
- `specify` CLI 1.0.6+
- `python3`
- Optional: `grok`, `omp` CLIs for runtime inspection

## 0. Preserve

```bash
git status --short
```

Classify unique intent before deleting any instruction file. Root `CLAUDE.md` is currently identical to `AGENTS.md`; unique intent is none.

## 1. Spec Kit adapters (shipped Python, not custom scripts)

```bash
specify integration install codex --script py
specify integration install grok --script py
specify integration install claude --script py
specify integration upgrade omp --script py
specify integration use grok
specify integration use claude
specify integration use codex
specify integration use omp
specify integration status --json
```

Expect `status=ok`, default `omp`, installed set includes `codex`, `grok`, `omp`, `claude`.

If status reports modified managed files: stop, migrate unique text, then continue. Do not `--force` by default.

## 2. Shims and isolation

- Root `AGENTS.md` is the map (add Sources of Truth / Workflow pointers; keep wiki routing).
- `.claude/CLAUDE.md` imports `@../AGENTS.md`. Root `CLAUDE.md` gone.
- `.omp/AGENTS.md` is `@../AGENTS.md` only.
- `agent-context` `context_file: AGENTS.md`.
- `.omp/config.yml` disables `context-file:project:CLAUDE.md` without dropping existing keys.

User-level Grok (cannot be repo-enforced):

```toml
# ~/.grok/config.toml
[compat.claude]
agents = false
skills = false
rules = false
```

## 3. Dispatcher

`docs/agents/harness-dispatch.md` matches [contracts/harness-dispatch.md](./contracts/harness-dispatch.md).

## 4. Checks

```bash
scripts/check-speckit-dry.sh
scripts/check-omp-baseline.sh
```

Both exit 0.

CI: `.github/workflows/speckit-dry.yml` runs status JSON + `check-speckit-dry.sh`.

## 5. Runtime inspection (when the CLI exists)

| Harness | Check |
|---|---|
| Spec Kit | status JSON healthy |
| Codex | `AGENTS.md` + `.agents/skills/speckit-*` |
| Grok | `grok inspect --json` loads root `AGENTS.md`; native `.grok/skills/speckit-*` wins |
| OMP | project context is `AGENTS.md` via import; Claude project file does not shadow |
| Claude | `.claude/CLAUDE.md` import only |

Missing CLI: skip that row; do not invent a pass.

## Failure

- `specify init --force` used while manifests are healthy
- Project-authored files added under Spec Kit script dirs to replace `--script py`
- Generated adapters edited to hold policy
