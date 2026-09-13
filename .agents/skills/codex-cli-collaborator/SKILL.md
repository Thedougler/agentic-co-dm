---
name: codex-cli-collaborator
description: Guide agents in invoking Codex CLI as a focused collaborator from the shell. Use when an agent needs to ask Codex for implementation help, code review, debugging, research over a local repository, independent verification, or a second-pass critique via `codex exec`, `codex review`, or an interactive `codex` session.
---

# Codex CLI Collaborator

## Overview

Use Codex CLI as a bounded collaborator, not as an unmanaged background worker. Give it a narrow job, the exact workspace, constraints, success criteria, and a required report format.

## Choose the Mode

- **Focused one-shot**: use `codex exec` for implementation, investigation, or validation that should finish and print a result.
- **Review only**: use `codex review` for an independent code review. Do not ask it to edit files.
- **Interactive pairing**: use `codex --no-alt-screen` only when a human or orchestrating agent will actively steer the session.
- **Do not spawn Codex** for trivial greps, formatting, or tasks the current agent can complete directly.

## Command Patterns

Prefer non-interactive commands for agent-to-agent collaboration:

```bash
codex exec --cd /path/to/repo --ask-for-approval on-request '<prompt>'
codex review --cd /path/to/repo '<review prompt>'
codex --cd /path/to/repo --no-alt-screen '<interactive starter prompt>'
```

Add options only when needed:

- `--model <model>` to pin a model.
- `--sandbox read-only` for review or research.
- `--sandbox workspace-write` for edits inside the repo.
- `--add-dir <dir>` only for an explicitly needed extra writable path.
- `--search` only when live web access is part of the task.

## Prompt Handoff

Include:

1. **Role**: "You are a collaborator, not the lead."
2. **Goal**: one concrete outcome.
3. **Workspace**: repo path and relevant files.
4. **Bounds**: files not to edit, no commits, no branch changes, no dependency installs unless approved.
5. **Context**: copied constraints that are not discoverable from files.
6. **Success criteria**: exact tests, checks, or evidence expected.
7. **Output format**: concise summary, files touched, commands run, failures, and next recommendation.

Template:

```text
You are a Codex CLI collaborator. Do not commit or change branches.
Goal: <one outcome>.
Workspace: <repo path>.
Read first: <files or docs>.
Bounds: <what not to touch>.
Allowed edits: <paths or "none">.
Validation: <specific commands or "report why not run">.
Report: findings, files changed, checks run, unresolved risks.
```

## Collaboration Rules

- Keep one lead agent responsible for final judgment.
- Pass only task-local context; avoid leaking the intended answer when asking for independent review.
- Use read-only mode for verification lanes.
- Use separate worktrees or non-overlapping file scopes for parallel write-capable agents.
- Inspect `git status --short` before and after. Treat unexpected changes as a stop condition.
- Never let a nested Codex perform destructive actions, credential changes, deployment, or broad rewrites without explicit approval.

## Output Capture

For auditable runs, capture output:

```bash
codex exec --cd /path/to/repo '<prompt>' | tee /tmp/codex-collab.log
```

If the collaborator edits files, the lead must review the diff and run or justify validation before reporting success.

## Failure Handling

- If `codex` is not logged in, report that the user must run `codex login`.
- If sandboxing blocks a required action, rerun only after the human approves the narrower needed permission.
- If the collaborator returns low-confidence advice, use it as input; do not present it as verified.
- If the collaborator changes out-of-scope files, stop and restore or ask the user how to proceed.
