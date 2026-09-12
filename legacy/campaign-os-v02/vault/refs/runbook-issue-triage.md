---
type: runbook
status: canon
publish: false
aliases: []
created: "2026-07-23"
updated: "2026-07-23"
tags: [craft]
summary: "A dogfood loop's product-critic report becomes a labeled, triage-ready GitHub issue queue. eval-triager files it, triage-labels.md labels it, /triage works it."
phase: any
uid: bad25a25-f94b-468f-8186-f8ae73c7fb09
---

# Issue-triage runbook (any GitHub issue pipeline)

Run whenever a product-critic report needs turning into tracked work, or a GitHub issue needs moving through the triage state machine. Orchestrates `eval-triager`, `vault/refs/issue-tracker.md`'s `gh` conventions, `vault/refs/triage-labels.md`'s label vocabulary, and the `/triage` skill. It never restates any of their procedures.

## Scope

`vault/refs/issue-tracker.md`'s Scope section sets the boundary. Cited, not restated.

## The sequence

1. A product-critic report lands in a dogfood loop's `<loop>/reports/` dir (e.g. `docs/dogfood/<loop>/reports/`). The caller names the loop, report path, and its `<loop>/EVAL-PLAN.md` path.
2. Dispatch `eval-triager` once per report — a personal, cross-project agent at `~/.claude/agents/eval-triager.md`, not in `vault/refs/runbook-agents.md`'s instantiated set. Give it the loop, report path, and `<loop>/EVAL-PLAN.md` path; its own spec owns what it does with them.
3. Every filed issue carries `needs-triage` plus the surface label eval-triager derives from the loop, per `vault/refs/triage-labels.md`'s vocabulary and `vault/refs/issue-tracker.md`'s `gh` conventions — cited, not restated.
4. The `/triage` skill (`~/.claude/skills/triage/SKILL.md`, or the human directly) works the queue through its own state machine, feeding `ready-for-agent` issues to `/implement`.

Done = issue(s) filed and labeled per `vault/refs/triage-labels.md`, `<loop>/EVAL-PLAN.md` updated when the run was `eval-triager`'s, commit `chore(dogfood): <loop> eval-plan` only if `<loop>/EVAL-PLAN.md` changed (filing/labeling GitHub issues is not a repo commit).
