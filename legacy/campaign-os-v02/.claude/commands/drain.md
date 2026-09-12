---
description: Drain lint findings to zero via generated worklist + dispatch waves, then promote drained rules
argument-hint: "[optional: a rule code like W33 to drain just that rule]"
---

Drain the lint backlog. The worklist is regenerated from live lint every run — never read a committed ticket or ledger for this (docs/adr/0006).

1. Run `npm run lint:drain` (append ` -- --rule $ARGUMENTS` if a rule was given) — the queue comes from the last sweep's cache, every producer included, so Vale's findings (docs/adr/0018) reach a triager instead of a void. Empty queue → run `npm run lint:debt -- accept --force`, commit any promoted rule files, done.
2. Dispatch per `vault/refs/runbook-dispatch-wave.md`, straight from the worklist output — max 5 concurrent agents total, explicit non-fable model on every dispatch. Every dispatched agent inherits this: the rule's intent binds, not its regex — rewording flagged text so the pattern stops matching while the flagged behaviour stays is a violation, not a fix; a genuine false positive → fix the rule's term list (`npm run lint -- --rules`), not the instance.
   - one agent per **file group** (use the `content-fixer` agent for pure template-shape drift, `general-purpose` otherwise);
   - one agent per **duplication cluster** (W33/W36/W57): the agent picks the owning page, keeps the content there, and replaces every copy with `![[owner#Heading]]` (verbatim block) or a `[[wikilink]]` (restated fact) — copies are deleted, never left alongside the pointer. Same-entity doubt → route to `canon-review`, don't guess.
3. After each wave, both mandatory before trusting it (`vault/refs/runbook-dispatch-wave.md` step 4 — neither alone closes a wave): dispatch `wave-verifier` over the touched paths, AND independently re-run the check with `node utils/scripts/rerun-check.mjs lint <touched-path...>`, pasted output. Never trust a subagent's self-report.
4. `npm run lint:debt -- accept --force`.
5. Commit: `chore(lint): drain <rules> — baseline -<N>` (include promoted rule files), then push.
6. Findings remain? Loop from step 1. A finding only a human can rule on (canon conflict) → file it via `canon-review` and say so; everything else drains now, this session — never deferred as "established".

Shared-tree concurrency: a batch lint result goes stale the moment another agent lands an edit — an agent re-lints each file immediately before editing it (`npm run lint -- <file>`), and a finding whose text greps to nothing was fixed by a sibling, not a linter bug — skip it, never chase it.
