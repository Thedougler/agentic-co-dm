# The instruction levers — how they fit together

Eight levers, differing on **context cost** (when tokens are paid for the
guidance to be present) and **activation precision** (how exactly it targets
the moment of need). Pick the narrowest lever that still holds:

| Lever | Context cost | Fires | Best for | Author/edit via |
|---|---|---|---|---|
| Root `CLAUDE.md` + `docs/guardrails/` (the kit) | every session, unconditionally, for the whole session | once, at load | the handful of rules that must never be missed, repo-wide — keep lean, this is the one lever you always pay for | `guardrails-kit` |
| Directory-scoped rules (`.claude/rules/*.md` with `paths:` glob, nested `CLAUDE.md`) | nothing until a matching file is Read/Edited, then just that file | the moment Claude touches a file under the glob | guidance specific to one subtree (`vault/`, `vault/campaigns/`) that would be noise everywhere else | `codify-it` |
| Model-invoked skills — cross-cutting (`campaign-os`, `recap-writer`, `canon-review`, …, root `.claude/skills/`) | a small constant fee every turn — the `description`, always in the skill listing | whenever the model itself decides the description matches | open-ended procedures the model should reach for unprompted, regardless of which content type is in play | `writing-for-agents` |
| Model-invoked skills — content-scoped (`.claude/skills/<name>/`, `.claude/skills/<name>/`) | same as above, plus directory placement narrows precision further | description match; living under the subtree also wins name-collision ties for work there (`.claude/rules/skills.md` § Directory scoping) | a skill that purely authors or analyzes one page type end to end within a single subtree — never a skill that also writes outside it (those stay cross-cutting) | `writing-for-agents`; placement rule: `.claude/rules/skills.md` |
| User-invoked skills (`disable-model-invocation: true` — e.g. `edit-article`, `campaign-writers-room`, `campaign-handoff`) | nothing until the human types the name | only on explicit `/skill-name` | workflows the human should choose on purpose — destructive, structural, or too easy for the model to mis-trigger | `writing-for-agents` |
| Hooks (`.claude/settings.json`; events: SessionStart/PreToolUse/PostToolUse/Stop/PreCompact) | nothing until the lifecycle moment; then only its own stdout, once | one exact lifecycle event, every time, deterministically | a must-happen gate — blocking a bad edit, injecting fresh state at session start. A careless one is pure context bloat — get it right. What's wired: the repo's own `.claude/settings.json` | `author-a-hook` |
| Lint-based enforcement (a script, wired via PreToolUse/PostToolUse or on demand) | nothing, ever, standing; a few lines only on violation | the instant the violated pattern is machine-detectable | anything a script can check — the best lever whenever the guardrail is machine-checkable, full stop | `enforce-with-linters` |
| Subagents (`.claude/agents/*.md`) | a fresh, separate context window per spawn — zero pollution of the caller's | dispatched explicitly by a skill or the orchestrator | tool restriction (an agent that literally *cannot* `Write`) or context isolation (a 2,000-line transcript chunk) | `writing-for-agents` |

About to author or edit a guardrail on any of these levers → chain-load the
named skill in the same row (next tool call: Read on its SKILL.md, no acting
tool call beside it) rather than hand-rolling the change from memory. Any
other gap — which lever a new guardrail belongs on, "which skill do I use for
X" — → chain-load `flag-the-gap`.
