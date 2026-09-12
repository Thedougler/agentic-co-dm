# omp subagent frontmatter — full field reference

Read when writing or editing `.omp/agents/*.md` and the summary table in SKILL.md is not enough.

## Fields

All fields use YAML. Keys accept camelCase or kebab-case.

### name (required)

Exact, case-sensitive identifier. Used to select the agent by name in requests and in `spawns` lists. Prefer lowercase kebab-case.

### description (required)

Short explanation of when this agent should be used. Concrete verbs, subject matter, and boundaries. This is a selection hint — omp shows it when deciding whether to delegate.

"Review database migrations for unsafe locks and rollback gaps" is useful.
"A helpful database expert" is not.

### tools

CSV string or YAML list of allowed tool names. Omit to inherit the parent session's full tool set.

Common tool names: `read`, `grep`, `glob`, `lsp`, `edit`, `write`, `bash`, `web_search`, `browser`, `github`, `task`.

Start with the smallest set that can complete the job.

### model

One model selector, a CSV string, or a YAML list tried in order. May be:
- A concrete selector: `openai/gpt-5-mini`, `anthropic/claude-sonnet-5`
- A role alias: `"@review"`, `"@smol"`

Role aliases are mapped in `~/.omp/agent/config.yml` under `modelRoles:` or via the `/models` Roles view. Using aliases keeps agent definitions stable across environments.

### thinking-level

Controls extended thinking depth. Values: `inherit`, `off`, `auto`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`. Actual support is model-dependent. The older `thinking` key is also accepted.

### spawns

Agent names this agent may delegate to, as a CSV string or list. `*` allows any discovered agent. Omit for none (no delegation).

Granting the `task` tool without setting `spawns` implies `*` — set `spawns` explicitly when granting `task`.

### autoload-skills

Skill names to load before the first assignment, as CSV or list. Unknown names are silently ignored.

### read-summarize

Boolean. Set `false` when the agent needs verbatim code from reads rather than structural summaries. Default is enabled (true).

### output

JSON Schema for a structured result. Omit when a normal prose report is appropriate.

### blocking

Boolean. Set `true` when callers should wait for this agent synchronously even if asynchronous delegation is enabled. Usually omit.

### prewalk

`true` hands off to the model in the `smol` role at the first edit or write. A model selector or role alias chooses another target. Use when a stronger model should inspect or plan before a cheaper model implements.

### advisor

`true` uses the configured advisor model role. A model selector or role alias chooses a specific advisor. Subagents otherwise run without an advisor.
