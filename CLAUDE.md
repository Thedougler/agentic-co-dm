@AGENTS.md

# Claude Companion

Claude Code-specific guidance for this repository. Load `AGENTS.md` first for project context; use this file only for native Claude Code behavior, verified Claude Code gaps, and Claude Code UI affordances. Shared agent behavior stays in the constitution, specs, skills, and docs named by the project context.

## Behavioral Test Subject

For agent-facing surface changes, use a Haiku subagent as the independent behavioral test subject. Give it cold context (the changed instruction excerpt, the task or slice, scope, and success criteria — not the producing conversation) and no write permission in the prompt. Reconcile its output as behavioral evidence before declaring completion.
