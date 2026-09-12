---
name: optimize-wiki-context-size
description: optimize-wiki-context-size — pulls the campaign-os llm-wiki's non-content context cost (CLAUDE.md, docs/guardrails/*, .claude/skills/**, craft docs, templates) toward a content-majority ratio. Use when asked why a session burns tokens before reaching content, to reduce context cost, or shrink an oversized CLAUDE.md, skill, or doc.
---

# optimize-wiki-context-size

Fix-phase orchestration for the wiki's own overhead: reads the existing
`context-cost-snapshot.mjs` → `.claude/.context-cost.json` cache (never
re-measures), triages the worst non-content offenders, fixes them,
and proves each fix via `blind-proof`. `vault/**` content and this run's own
report are the protected bucket — last to be touched, never a target.

The ratio below uses real per-file Read tokens (the only real, billed data
`context-cost` exposes) as the proxy for "content vs. reasoning-about-content
share" — it can't attribute an agent's own output tokens back to a source
file, so treat it as the practical proxy, not an exact reasoning measure.

Each step ends on an `OC<n>:` line — the transcript proof it ran.

## OC0 — Orchestrate directly, or dispatch

Decide this before OC1, every invocation:

- **The user asked for this run directly, this turn** (named the skill, or
  asked in terms that map straight to "optimize context cost now") →
  **Orchestrate**: run OC1-OC6 yourself, inline, in this session — the rest
  of this file is written for you as the actor.
- **You reached for this skill on your own** — any trigger the user did not
  ask for this turn → **Dispatch**: don't run OC1-OC6 yourself. Dispatch the
  `context-optimizer` agent (`Agent` tool) and report back its own
  `OC1`/`OC6` lines instead. Running the procedure inline here is the exact
  cost `context-optimizer` exists to absorb — it holds this multi-step pass
  so the orchestrator's own context doesn't have to.

Never do both: a Dispatch that also starts OC1 inline duplicates the
subagent's own work; an Orchestrate run never additionally dispatches
`context-optimizer` for the same pass.

`OC0: <orchestrate | dispatch> — <one-line why>`

## OC1 — Rank

`npm run context-cost:snapshot && node utils/scripts/context-cost-decisions.mjs filter`.
This buckets every row by path prefix (`vault/**` = protected; everything
else = in scope), computes the ratio as `sum(tokens_total, vault/**) /
sum(tokens_total, all)` (the cache carries no `content_tokens`/
`non_content_tokens` fields to divide directly), and excludes any in-scope
path a prior run already decided is on cooldown or that another invocation
currently has claimed — `utils/scripts/context-cost-decisions.mjs`'s own
header comments own the ledger mechanics, don't re-derive them here. Take
its `top5`, then immediately lock them in before OC2 starts:
`node utils/scripts/context-cost-decisions.mjs claim <path1> <path2> ...` —
a second invocation running close behind sees these five as claimed in
`filter`'s next call and picks its own next five instead of redoing this
run's work.

`OC1: ratio <N>% content (target: majority >50%); top5: <path (tokens)>...;
skipped (cooldown/claimed): <count>`

Checking long-term/holistic health rather than one invocation's top-5 → `transcripts.py
context-cost --since 90 --buckets 6` for a real multi-point trend instead of the
cache's single recent/prior diff (recomputed fresh from transcript history, not
cached).

## OC2 — Triage each of the top 5

Walk the questions **in this order**, stop at the first that resolves the
file — never skip ahead to a later question because it's more familiar (the
RED baseline for this skill was a tester that jumped straight to question 2
and never validated the fix; that gap is why the order is enforced here).
OC1 already claimed these five in the ledger, so a concurrent invocation's
`filter` call skips them until the claim times out or OC6 resolves them:

1. **Necessity.** Does the agent already do this behaviour without the
   instruction (a no-op)? Grep `session-transcripts` for recent turns that
   needed this file's guidance and check whether they'd have acted the same
   way blind. Confirmed no-op → delete; deletion frees the entire cost.
2. **Progressive disclosure.** File genuinely needed → apply the
   technique menu: Split / Demote the lever / Script it / Lower a static
   cap / Drop a redundant example.
3. **Erroneous read.** `transcripts.py context-cost --timeline --session <sid>`
   for the exact real context-size cost of each read of this file, or
   `turns --grep <path>` for the sessions that actually Read it — was the
   agent sent here by a *different* stale pointer or mis-worded trigger
   elsewhere? `--with-friction` on the file's `context-cost` row shows
   whether its reads correlate with corrections/errors afterward (a
   correlational lead, not a verdict — read the actual turns via `show
   <session> --grep <path>` before trusting it). Fix the misleader, not this
   file.
4. **Conflict.** Grep the repo for the same rule or fact stated elsewhere.
   Duplicated → collapse to one judgement, delete the loser (this repo's
   own `vault/CLAUDE.md` rule 8 — one fact, one page — generalized past
   `vault/`).
5. **Genuinely unclear (last resort only).** Author new prose via
   `pattern-match`'s contract, then `grep -rn` the whole repo for every
   reference to the old guidance and update or delete each one — one
   surviving old-guidance reference means this step isn't done.

`OC2: <file> -> <verdict 1-5> because <evidence quoted>` — one line per
file.

## OC3 — Apply

Edit or delete directly; dispatch background subagents for a 3+ file batch
(this repo's existing dispatch convention). Sweep every cross-reference to
anything renamed or deleted — `grep -rn "<old path or name>"` — before
calling this step done.

`OC3: <files touched, refs swept>`

## OC4 — Validate (never skip)

Chain-load `~/.claude/skills/blind-proof/SKILL.md`
(chain-load X = your next tool call is Read on X's SKILL.md — the Read tool
itself, not a Skill invocation — no acting tool call beside it): single mode
per fix that stays in one file with an unchanged trigger, batch mode for a
fix spanning more than one file or a reworded trigger (OC2 verdict 5). No
fix from OC3 counts as done without a quoted `BP4: PASS`.

`OC4: <BP4 verdict per fix, or N/A with reason>`

## OC5 — Prove the drop

`npm run context-cost:snapshot`; diff `tokens_total` for every touched path
and the OC1 ratio. A "deleted" file whose cost didn't drop still has
something routing to it — reopen OC3.

`OC5: ratio <N>% -> <M>%; <path>: <before> -> <after> tokens`

## OC6 — Report

Resolve each of the five files' ledger entries with what OC2 concluded and
OC3 actually did: `node utils/scripts/context-cost-decisions.mjs resolve
<path> --verdict <1-necessity|2-progressive-disclosure|3-erroneous-read|4-conflict|5-unclear>
--action <deleted|edited|kept-necessary|misleader-fixed> --tokens <post-fix
tokens_total from OC5> --note "<short evidence quote>"`. A file OC2 verdict
1 confirmed necessary with no OC3 edit still gets `--action kept-necessary`
— that's what keeps it off the next invocation's top-5 instead of
re-litigating the same investigation.

`OC6: this run's before/after ratio; ledger updated: <paths>; next top-5 for
the next invocation` (fixing today's crop, and cooling down today's "kept"
verdicts, both promote new offenders — this is the "constant downward
pressure" mechanism: one bounded chunk per invocation, not a single sweep).

## Boundaries

- Never target a `vault/**` page's own length or prose — that's a DM canon
  call, not this skill's.
- Never claim a fix done on OC3's edit alone — OC4 and OC5 are required,
  not optional, for every fix this run makes.
- Never re-derive the split/demote mechanics beyond step 2's technique
  menu — that menu is the single source of truth.
- Never skip OC0, and never run OC1-OC6 inline in the same pass you also
  dispatch `context-optimizer` — one or the other, decided once, up front.
- A claim older than `CONTEXT_COST_CLAIM_TIMEOUT_MINUTES`
  (`wiki.toml` `[thresholds]`) is abandoned, never
  treated as still in-progress — a run that died mid-pass can't
  permanently block a file.
- A file re-spiking `CONTEXT_COST_RESPIKE_PCT`% past its last decision's
  token count breaks cooldown early — the ledger must never suppress a
  real regression.
