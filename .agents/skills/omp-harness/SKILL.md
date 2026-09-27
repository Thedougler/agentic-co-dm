---
name: omp-harness
description: >
  Write or edit omp context files, skills, and subagent definitions. Use when
  creating AGENTS.md, .omp/AGENTS.md, RULES.md, SYSTEM.md, APPEND_SYSTEM.md,
  .omp/skills/*/SKILL.md, or .omp/agents/*.md — or when adapting existing
  instructions for the omp harness. Use when the user mentions omp, oh-my-pi,
  or wants to port agent config from another harness (Claude Code, Codex,
  Gemini, OpenCode) into omp's format.
---

# omp harness

Write context files, skills, and subagent definitions for [omp](https://omp.sh) (oh-my-pi). Three surfaces, one Markdown language.

Also load `writing-for-agents` — its levers (context pointers, information hierarchy, leading words, completion criteria, pruning) apply to every omp document. This skill covers omp-specific packaging and mechanics.

## 1 · Context files

Context files are standing instructions loaded automatically. omp walks upward from the working directory to the repository root, composing files at each level. Most-local wins.

### File types

| File | Project location | User location | Purpose |
|---|---|---|---|
| `AGENTS.md` | `<repo>/AGENTS.md` | `~/.omp/agent/AGENTS.md` | Standing project instructions. Composes across directory levels. |
| `.omp/AGENTS.md` | `<repo>/.omp/AGENTS.md` | same as above | omp-native alternative. Shadows bare `AGENTS.md` at the same level. |
| `RULES.md` | `<repo>/.omp/RULES.md` | `~/.omp/agent/RULES.md` | Sticky always-apply rules. Both user and project can apply. |
| `APPEND_SYSTEM.md` | `<launch-dir>/.omp/APPEND_SYSTEM.md` | `~/.omp/agent/APPEND_SYSTEM.md` | Appends to omp's built-in system prompt. Launch-dir only. |
| `SYSTEM.md` | `<launch-dir>/.omp/SYSTEM.md` | `~/.omp/agent/SYSTEM.md` | Replaces omp's built-in system prompt body. Rarely needed. |

**Provider priority** (at same scope, first wins): native `.omp` → `claude` → `agents`/`codex` → `gemini` → `opencode` → `github` → bare `agents-md`. `.omp/AGENTS.md` shadows `AGENTS.md` at the same level — do not create both.

### Imports

`@path` tokens include another file inline:

```markdown
# Project instructions
@docs/agent/testing.md
@docs/agent/style.md
```

- Relative paths resolve from the importing file, not the working directory.
- `~/...` resolves from home. Absolute paths accepted.
- Must begin a line or follow whitespace (email addresses and `git@` are left alone).
- Imports inside code fences are left as examples.
- Nested imports followed for at most five hops. Cycles stopped.

### Writing context files

Choose `AGENTS.md` for instructions that guide most work in a directory tree. Choose `RULES.md` for constraints that always apply regardless of task. Choose `APPEND_SYSTEM.md` only for behavioral overrides to omp's own system prompt.

For monorepos: shared policies at the root, package-specific commands in nested `AGENTS.md` files. Do not duplicate root content into packages.

After editing, start a new session or `/new`. Verify with `/extensions` → Context Files tab.

## 2 · Skills

A skill is a reusable playbook loaded on demand when the task matches its description.

### Location

| Scope | Path |
|---|---|
| Project | `.omp/skills/<name>/SKILL.md` |
| User | `~/.omp/agent/skills/<name>/SKILL.md` |
| Compatible | `.agents/skills/`, `.claude/skills/`, `.codex/skills/` (also discovered) |

Discovery is one level deep: `skills/postgres/SKILL.md` is found; `skills/databases/postgres/SKILL.md` is not.

### Frontmatter

```yaml
---
description: >   # Required. Concrete task verbs + objects + boundary.
  Use when adding or reviewing Vitest tests in src/importer;
  covers fixtures, snapshots, and integration setup.
name: importer-tests  # Optional. Overrides directory name.
hide: false            # Optional. Omits from auto-matching; /skill:<name> still works.
---
```

`description` is the trigger. Name the actions (writing, reviewing, debugging, migrating), the objects (Postgres migrations, snapshot tests), and the boundary (a directory, file type, subsystem). omp uses description to decide whether to load the skill — write it so every relevant prompt matches and irrelevant ones do not.

### Body

Direct, operational instructions. State when the workflow applies, the required sequence, safety boundaries, and what success looks like. Keep the body under ~500 lines; push long reference to `references/` beside `SKILL.md`.

```
skill-name/
├── SKILL.md
├── references/    # loaded on demand via pointer in SKILL.md
│   └── registry-checks.md
├── scripts/       # deterministic helpers the playbook calls
│   └── verify-artifacts.sh
└── assets/        # templates, icons, fonts used in output
```

Supporting files do not execute automatically — the playbook explains when and how.

### Invocation

Users invoke skills three ways:
1. **Natural match** — omp loads when description matches the request.
2. **Explicit** — `/skill:release-check Review the 2.1 tag.`
3. **Inline** — `Review migrations/042.sql with /skill:postgres and propose a safer rollout.`

After creating or editing, `/reload-plugins` or new session.

## 3 · Subagent definitions

A subagent is a named specialist in one Markdown file. omp delegates work to it by name.

### Location

| Scope | Path |
|---|---|
| Project | `<project>/.omp/agents/<name>.md` |
| User | `~/.omp/agent/agents/<name>.md` |

Nearest project `.omp/agents/` directory wins. Lowercase kebab-case names. `.claude/agents/`, `.codex/agents/` are **not** scanned — omp has its own frontmatter contract.

### Frontmatter

```yaml
---
name: api-reviewer           # Required. Exact, case-sensitive.
description: >               # Required. When to use this agent.
  Review API changes for compatibility, missing tests,
  and contract drift.
tools: [read, grep, glob]    # Optional. Omit → inherits parent's full set.
model: "@review"             # Optional. Concrete selector or role alias.
thinking-level: high          # Optional. off/auto/minimal/low/medium/high/xhigh/max.
spawns: []                    # Optional. Agent names this agent may delegate to.
autoload-skills: [postgres]  # Optional. Skills loaded before first assignment.
read-summarize: true          # Optional. false → verbatim reads, no summaries.
blocking: false               # Optional. true → caller waits synchronously.
prewalk: false                # Optional. true → stronger model plans before cheaper implements.
advisor: false                # Optional. true → use advisor model role.
---
```

### Body

The reusable role instructions. State what the agent owns, what it must not do, the checks or workflow, expected evidence in its answer, and whether it may edit files.

Put changing work in the request, not the definition. Do not copy general project instructions — normal project context still applies.

### Tool grants

Start with the smallest set:

| Job | Tools |
|---|---|
| Investigation | `read, grep, glob` |
| + semantic nav | add `lsp` |
| + file changes | add `edit` or `write` |
| + shell commands | add `bash` |
| + external access | add `web_search`, `browser`, `github` |
| + further delegation | add `task`, set `spawns` |

### Isolation

Isolation is requested per delegation, not in frontmatter:

> Use the migration-fixer subagent in an isolated worktree to fix the failing migration test.

Isolation separates filesystem changes; it does not sandbox network or credentials — keep tool grants narrow.

## Cross-harness porting

When adapting from another harness:

| Source | omp equivalent |
|---|---|
| `.claude/CLAUDE.md` | `.omp/AGENTS.md` (or root `AGENTS.md`) |
| `.claude/skills/*/SKILL.md` | `.omp/skills/*/SKILL.md` (same format, same frontmatter) |
| `.claude/agents/*.md` | `.omp/agents/*.md` (different frontmatter — see §3) |
| `.codex/agents/*.toml` | `.omp/agents/*.md` (rewrite TOML → YAML frontmatter + Markdown body) |
| `.github/copilot-instructions.md` | `AGENTS.md` or `.omp/AGENTS.md` |

Claude Code agent frontmatter (`type`, `model_id`) does not map 1:1 to omp's (`tools`, `model`, `thinking-level`, `spawns`). Rewrite, do not copy.

## Verification

After writing any omp file:

1. Start omp from the intended directory (or `/new`).
2. `/extensions` → inspect Context Files, Skills, or `/agents` hub.
3. Confirm the expected path is active, not shadowed.
4. For skills: `/reload-plugins` if editing in-session.
