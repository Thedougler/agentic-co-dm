@AGENTS.md

# Claude Companion

Claude Code-specific guidance for this repository. Load `AGENTS.md` first for project context; use this file only for native Claude Code behavior, verified Claude Code gaps, and Claude Code UI affordances. Shared agent behavior stays in the constitution, specs, skills, and docs named by the project context.

## Behavioral Test Subject

For agent-facing surface changes and every skill eval run, use Luna 6 through the Codex CLI as the independent behavioral test subject: `codex exec -m gpt-6-luna -s workspace-write -C <repo> --json -o <run>/final.txt "<prompt>" > <run>/events.jsonl`, each run in its own background shell (one shell per subject, never one shell looping several) so each completion can be graded and acted on as it lands; dispatch every eval subject at once (eight or more is fine). The JSONL events record shell commands and file writes but not image views, so ask the subject for an ordered process log and check that its art claims match the pixels. Luna needs Codex CLI 0.156 or newer (`codex update`). When any run reports a Codex usage limit, stop every Luna run and dispatch no more until the limit resets. Luna is only the test subject: this Claude session grades every output itself, and no Luna run grades Luna output. Give it cold context (the changed instruction excerpt, the task or slice, scope, and success criteria — not the producing conversation) and no write permission in the prompt. Reconcile its output as behavioral evidence before declaring completion.
