---
name: publish-site
description: >-
  Build and deploy the Quartz player site, in a Campaign OS repo (vault/, utils/site/
  present) — pipeline's final publish step. Fires on "publish"/"publish the site"/"run
  PUBLISH"/"publish session NN", a `recap(sNN)` commit ready to catch the site up, or proposing
  which pages go player-visible. The only skill allowed to flip `publish: true`.
---

# Publish Site

Phase 6 of the session pipeline — `vault/refs/runbook-publish.md` is the runbook
and the full contract (layered defense, the secrets blacklist, proposal shape,
acceptance). Publishing is
default-deny (L3): nothing reaches players unless a page opts in AND the
strip pass removes DM-only content AND the leak check passes on the built
HTML. This skill drives both layers but owns none of the guardrail
logic itself — that lives in `utils/site/quartz.config.ts` (layer 1) and
`utils/scripts/build_site.sh` (layer 2). If this skill and the runbook ever
disagree on a point, stop and say REVIEW-for-human; don't pick one.

## Gate (check before touching anything)

```
git log --oneline | grep "recap(sNN)"
```

Paste it. No `recap(sNN)` commit → stop, tell the user RECAP is the
missing upstream phase, offer to run it (a site built from stale canon is
the pipeline-rot failure mode L2 exists to prevent). The human can override
explicitly ("publish anyway") — if they do, note `GATE-OVERRIDDEN by user`
in your response.

## Standard queries (build the candidate list)

```
grep -rl "touched: sNN" vault/ 2>/dev/null
ls vault/episodes/NNN/sNN-recap.md vault/episodes/NNN/sNN-highlights.md 2>/dev/null
grep -L "publish: true" $(grep -rl "touched: sNN" vault/ 2>/dev/null) 2>/dev/null
```

First two find everything this session's ingest touched; the third
narrows to what isn't already published. Every page in this candidate list
gets a line in the proposal below — flip or hold, never silently omitted.

## Owned paths

`publish: true` / `publish: false` frontmatter flips on pages under
`vault/` (including its `vault/campaigns/shattered-sea/pcs/` and `vault/episodes/`
subtrees) — and only there, and only after human
approval per page. `utils/site/public/` — write-only via `build_site.sh`, never
hand-edited (`vault/refs/runbook-wiki.md` § Who writes what: "hand edits, ever"
is its Never column).

## Workflow

### 1. Write the publish proposal

For each page from the standard queries, one line: flip (with a one-line
reason — "party spent the whole session here") or hold (with a one-line
reason — "reveal goes in Player-Known but HOLD until the party confirms
sharing"). Shape, per `vault/refs/runbook-publish.md` § The publish proposal:

```markdown
# Publish proposal — sNN
Flip publish: true
- vault/episodes/NNN/sNN-recap.md — session recap
- vault/campaigns/shattered-sea/locations/gullscrag.md — party spent the whole session here
Leave unpublished (met but sensitive):
- vault/campaigns/shattered-sea/npcs/otar-the-foul.md — reveal in Player-Known, HOLD pending confirm
```

Always propose `vault/episodes/NNN/sNN-recap.md` and `vault/episodes/NNN/sNN-highlights.md` for the flip
list if they exist and aren't already published — they're built
player-facing by design (`vault/refs/runbook-recap.md`). Never add a page
this skill invented; every line traces to the standard queries above.

### 2. Get explicit human approval

Present the proposal. The human edits or confirms it — in chat or in the
proposal file. **Approval is per page, never blanket.** "looks good" against
a list you just showed them counts; approving in advance of seeing the list
does not. Do not proceed to step 3 without it.

### 3. Flip exactly the approved flags

Edit only the pages the human approved for the flip list, changing
`publish: false` → `publish: true` (never touch pages on the hold list).
Paste the diff (`git diff -- <paths>`) as evidence — the flip is real only
if it's shown, not narrated.

### 4. Build and leak-check

```
utils/scripts/build_site.sh
```

This chains both layers: strips `## DM Only` sections and `%%...%%`
comments onto a staging copy (vault files untouched — verify with
`git status` after, should show no diff outside frontmatter), builds Quartz
from the staging copy. Paste the
full `PUBLISH-CHECK:` block(s) verbatim — `PASS (N pages, M secrets
checked)` or one or more `FAIL` blocks.

**Inference-leak audit.** If
`.claude/agents/site-auditor.md` is present, spawn the `site-auditor`
subagent over `utils/site/public/` with the secrets-blacklist entries
(`vault/refs/runbook-agents.md`) — it catches what the string check can't: a fact a
clever player could *infer* from a built page (a `retired` NPC page, an
Session Log entry for a secret meeting). It returns `CLEAR` or
`INFERENCE-LEAK:` blocks. A leak is a REVIEW for the human (hold the page,
rephrase the source) — never a unilateral unpublish (L3). Absent →
`NOTED: site-auditor not present in this repo — ran string-level leak_check only`.

### 5. On FAIL

Each `FAIL` block names the leaking page and the exact marker or secret
string and its `FIX` line. Fix the *source* page (remove the DM Only
leak, close the `%%…%%` comment, or rephrase the secret) — never tune down
the secrets blacklist (`vault/refs/runbook-publish.md` § The layered defense)
to make a failure disappear;
that defeats the layer it exists to be. Re-run step 4. **Two failed
fix attempts on the same finding → stop, ask the human** (iron rule 7,
numbers not judgment) rather than trying a third variation alone. Holding
the page unpublished (move it back to the hold list, revert its flip) is
always an acceptable resolution if the human prefers that to a content fix.

### 6. Commit and deploy

1. Commit `publish(sNN): <slug>` — stage the flipped pages plus
   `utils/site/public/` if it's tracked in this repo (check `git status`; some
   repos gitignore build output and rely on CI to build it — follow what
   the repo already does, don't newly track or newly ignore it without
   asking).
2. Deploy is default GitHub Pages via a CI Action that re-runs
   `build_site.sh` (so a leak that somehow got committed still can't reach
   the live site) — this skill's job ends at the commit/push that triggers
   it. Pushing to the deploy remote and any account/DNS/hosting setup is
   outside this skill's owned paths; ask the human before pushing if the
   repo's remote isn't already the deploy target they expect.

## Degrade by asking

Ambiguous flip/hold call the standard queries didn't resolve, a page with no
clear reason either way, or uncertainty about whether the repo tracks
`utils/site/public/` in git — ask the specific question, never guess a default.

## Markers

`PUBLISH-CHECK: PASS (...)` or `PUBLISH-CHECK: FAIL` blocks, pasted from
real `build_site.sh` output in the same turn — never
reconstructed from memory of a previous run.
