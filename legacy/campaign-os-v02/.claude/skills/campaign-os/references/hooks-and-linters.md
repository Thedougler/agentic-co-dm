# Hooks and linters — where each piece lives

Hooks are how this system prompts *itself*: deterministic scripts fire on
model actions and inject instructions back into context, so the guardrails
hold when nobody is watching. The check is code (no LLM in the hook path —
hooks must be fast and unfailing); the *output* is written for an LLM
reader. That split is the whole trick.

Extending this layer is the standing default: the moment a defect is
mechanically detectable, the next move is a lint rule, not a prose
guardrail — and migrations run rule-first (flag the old shape, then fix).

| You need | Read |
|---|---|
| What every W-rule checks, its severity, its FIX line | `uv run --directory utils/wiki-cli wiki lint --rules` |
| Which hooks are wired right now, on which events | `.claude/settings.json` |
| Vault-wide thresholds and word lists every rule reads | `wiki.toml` `[thresholds]` |
| A hook's stdin contract, or why an env-var escape hatch fails | `.claude/rules/scripts.md` |
| Wording a hook's `block()` or self-prompt message | the global `prompt-once` skill |
| Running the whole rule table standalone, at scale | the `llm-wiki-lint` skill |
