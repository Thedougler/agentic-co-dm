@AGENTS.md

# Claude Companion

Claude Code-specific guidance for this repository. Load `AGENTS.md` first for project context; use this file only for native Claude Code behavior, verified Claude Code gaps, and Claude Code UI affordances. Shared agent behavior stays in the constitution, specs, skills, and docs named by the project context.

## Behavioral Test Subject

For agent-facing surface changes and every skill eval run, use Luna 6 through the Codex CLI as the independent behavioral test subject. Run each eval with `./scripts/luna-eval <skill-dir> <eval-id> <skill-name>-workspace/iteration-<N>` (it owns the command, reads the prompt from the skill's `evals/evals.json`, and writes `output.md` and `process.md` per run), one call per eval in its own background shell so each completion can be graded as it lands; dispatch every eval subject at once (eight or more is fine), and after the first full pass re-run only the evals that did not pass, stopping once all pass. The JSONL events record shell commands and file writes but not image views, so check the subject's process log and that its art claims match the pixels. Luna needs Codex CLI 0.156 or newer (`codex update`). When a run reports a Codex usage limit, the script stops every Luna run and leaves a `CODEX_LIMIT` marker that blocks dispatch until the limit resets and you delete it. Luna is only the test subject: this Claude session grades every output itself, and no Luna run grades Luna output; for narration, `scripts/check-narration.py` surfaces mechanical leads to judge. Give it cold context (the changed instruction excerpt, the task or slice, scope, and success criteria — not the producing conversation) and no write permission in the prompt. Reconcile its output as behavioral evidence before declaring completion.
