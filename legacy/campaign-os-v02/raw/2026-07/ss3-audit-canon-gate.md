# Audit: canon-gate enforcement (MIGRATION-LEDGER Round 3, line 80)

Ledger line under investigation: "audit :: canon-gate enforcement question — R1 link
pass (ad049e2) edited canon pages with no unchecked ledger line naming them;
PreToolUse should have blocked. Verify whether subagent Edit-tool calls actually
trip the hook or whether Bash-path edits bypassed it; report, patch if real."

## 1. Ordering evidence (confirmed)

```text
17adf25 2026-07-13 22:27:48 -0700 chore(migration): check off 11 ledger lines, regen _meta (orchestrator-owned)
ad049e2 2026-07-13 22:38:21 -0700 ingest(link-pass): restore deferred wikilinks between landed pages
```

`17adf25` flips the campaign-overview ledger line from unchecked to checked, ~11
minutes *before* `ad049e2` edits `world/lore/campaign-overview.md`:

```diff
-- [ ] lore :: lore/campaign-overview.md → restructure → world/lore/ — status: canon
+- [x] lore :: lore/campaign-overview.md → DONE d794cc8 — world/lore/campaign-overview.md, canon ...
```

`ad049e2` itself touches only ingest-queue files and the three wiki pages
(`campaign-overview.md`, `estratto.md`, `vethka.md`) — it does **not** touch
`MIGRATION-LEDGER.md`. So at the moment `ad049e2` ran, no unchecked ledger line
named `world/lore/campaign-overview.md`. For `world/ships/vethka.md`: the only
ledger line mentioning "vethka" at that time was `- [ ] vehicle ::
entities/vehicles/vethka.md → GAP BY DESIGN ...` — unchecked, but its path
string is the legacy path `entities/vehicles/vethka.md`, not
`world/ships/vethka.md`, so it would not have satisfied `canon_gate.py`'s `rel
in line` substring check even had the agent looked. **Confirmed: `ad049e2`
edited two canon pages with zero valid ledger authorization at the time.**

The line that *does* authorize both paths — `- [ ] link-pass R3 :: restore
deferred wikilinks ... world/lore/campaign-overview.md ... world/ships/vethka.md
... this unchecked line IS the canon_gate authorization for those paths` (now
line 79) — was added by `6295152` ("round-3 ledger section"), committed
`2026-07-13 23:26:21`, **48 minutes after** `ad049e2`. It's a retroactive
paper trail, not a contemporaneous authorization; it does not excuse the
original bypass.

## 2. Live enforcement test — Edit-tool path

**Deviation from the ticket's literal instructions, noted up front:** the
ticket named `world/items/preserved-eel.md` as the probe target, on the
premise it is "currently named ONLY in a checked ledger line." That premise is
now false — `preserved-eel.md` is also named in the unchecked line 79
(link-pass R3, added by `6295152`, see above), so `canon_gate.py` currently
*authorizes* edits to it (verified: `python3 scripts/canon_gate.py
"world/items/preserved-eel.md"` → exit 0, no block). Testing enforcement
against an already-authorized file can't distinguish "blocked" from "allowed
because valid." I substituted `world/items/delmars-cloak-of-the-manta-ray.md`
— confirmed `status: canon`, and confirmed by direct string check that no
unchecked ledger line's text contains its exact path (`- [ ]  item-uncommon ::
entities/items/uncommon/delmars-cloak-of-the-manta-ray.md → world/items/ —
...` names the *legacy* path, not `world/items/delmars-cloak-of-the-manta-ray.md`,
so the substring test fails — matches the same pattern that let `ad049e2`
through on vethka).

**Result: BYPASS CONFIRMED for this subagent's Edit-tool calls.**

- I ran the Edit tool to append `<!-- canon-gate-audit probe -->` to
  `world/items/delmars-cloak-of-the-manta-ray.md`. The call **succeeded** —
  no CANON-GATE message, no block, exit path indistinguishable from an
  unrestricted edit.
- Immediately after, I ran the exact same script the hook is wired to,
  against the exact same path, outside the tool-call machinery:

  ```console
  $ python3 scripts/canon_gate.py "world/items/delmars-cloak-of-the-manta-ray.md"
  CANON-GATE [world/items/delmars-cloak-of-the-manta-ray.md]: this page is status: canon.
    Either: add a ledger line in sessions/NN/state-changes.md and run CANONIZE;
    or execute an unchecked docs/campaign/MIGRATION-LEDGER.md line naming this path
    (migration-mode exception, REVIEWED-BY-HUMAN gated);
    or append a CONTRADICTION block (appends are allowed);
    or open canon-review (sets CANON_REVIEW=1).
    Draft your intended edit to /tmp/blocked-edit.md so nothing is lost.
  $ echo $?
  2
  ```

  So the script's *logic* is correct and would have blocked this exact edit —
  the hook simply never intercepted my Edit tool call to enforce it.

**Complication (self-caused, disclosed):** while my probe edit was live on
disk, a concurrent in-flight ingest process (a separate orchestrator/session
actively working the Round-3 ledger — visibly churning `world/_meta/index.md`,
creating `world/rules/carpenters-shop.md`, `world/locations/elemental-plane-of-water.md`,
`sessions/02-conflict-is-a-surety/`, etc. throughout this audit) staged and
committed `world/items/delmars-cloak-of-the-manta-ray.md` as part of its own
legitimate commit `8714561` ("ingest(ss3-item-delmars-cloak): ...") before I
reverted my probe line — sweeping `<!-- canon-gate-audit probe -->` into that
commit. I did not create or touch that commit; I fixed the resulting
contamination with a new, separate commit (`86ca979`,
"fix(canon-gate-audit): remove audit probe line accidentally committed into
delmars-cloak") that removes exactly the one line I added, restoring the file
to byte-identical content otherwise. `git diff -- world/items/delmars-cloak-of-the-manta-ray.md`
is now clean against HEAD. This is disclosed under the "don't narrate/touch
other sessions' work" rule as an exception: it was contamination *I* caused,
not pre-existing foreign work, so cleaning it up was mine to do.

## 3. Bash-path test

```console
$ echo "<!-- probe -->" >> world/items/preserved-eel.md
$ git diff -- world/items/preserved-eel.md
+<!-- probe -->
```

Went through with no interception, as expected — `.claude/settings.json`'s
PreToolUse matcher is `"Write|Edit"` (tool name), and `Bash` is a distinct
tool name, so this hook was never wired to see Bash-issued file writes at all.
Reverted immediately via Edit (removed exactly the added line); `git diff --
world/items/preserved-eel.md` is clean. Note: because `preserved-eel.md` is
currently authorized via ledger line 79 anyway, this particular run doesn't
prove the Bash hole would let through something *invalid* — but the matcher
text alone (`Write|Edit`, no `Bash`) is sufficient proof the hole exists
independent of any specific file's authorization state; `canon_gate.py` is
never invoked for a `Bash` tool call regardless of the target path or its
ledger status.

## 4. Diagnosis

`canon_gate.py` itself has no defect:

- Empty arg: `python3 scripts/canon_gate.py ""` → exit 0, no crash (the
  `" ".join(...).split()` produces an empty list; the for-loop is a no-op).
- Multi-file space-joined arg (how `$CLAUDE_FILE_PATHS` would arrive for a
  batch): `python3 scripts/canon_gate.py "world/items/delmars-cloak-of-the-manta-ray.md world/items/preserved-eel.md"`
  → correctly blocks on the unauthorized file (exit 2) while the authorized
  one alongside it doesn't suppress the block.
- Single-file arg: exit 2, correct block message, as shown above.

So `ad049e2`'s bypass was not a `canon_gate.py` argument-parsing or logic bug.
Given (a) this audit reproduced an identical bypass empirically — a Task-tool
subagent's Edit call on a genuinely-unauthorized canon page went through
uncontested, while the same script invoked directly on the same path blocks
correctly — and (b) `ad049e2`'s own commit message/shape ("ingest(link-pass):
restore deferred wikilinks between landed pages", a `world/`-modifying
ingest-phase action reconciling multiple pages in one commit) matches this
repo's pipeline pattern of dispatching ingest-phase work to spawned
subagents rather than running it in the top-level session — the most
parsimonious explanation is: **`ad049e2` was produced by a spawned subagent,
and this harness's PreToolUse hook does not intercept that subagent's own
Edit-tool calls**, exactly as reproduced in section 2. I checked Claude Code's
official hook documentation before asserting this (via the claude-code-guide
agent): the docs state PreToolUse *should* fire for subagent tool calls and
include an `agent_id` field for that purpose — so either this environment has
a gap relative to documented behavior, or there is a narrower condition (e.g.
which subagent-spawn mechanism, or how `.claude/settings.json` is loaded for
a Task-spawned context) that the docs don't spell out. I was not able to
pin down *why* the hook didn't fire from inside this same audit — only that,
empirically and repeatably in this run, it didn't.

I did not find any alternative explanation that fits the evidence better:
`$CLAUDE_FILE_PATHS` quoting/splitting is not the culprit (tested above), and
`ad049e2` never touched the ledger file, so it can't be that the agent
legitimately raced a ledger check-off against its own edit.

## 5. Patch

No patch to `scripts/canon_gate.py` (or its mirror at
`.claude/skills/campaign-os/scripts/canon_gate.py`) — no real defect was
found in the script's own logic; both copies remain `cmp`-identical and
unmodified by this audit. The actual gap (subagent Edit calls not tripping
the hook) lives in the hook-invocation layer, not in this repo's script, and
I could not find a script-side change that would close it — the script has no
control over whether it gets invoked in the first place.

## 6. Recommendation for the Bash hole (human decision, not mine to fix)

`.claude/settings.json`'s PreToolUse matcher is `"Write|Edit"`. Any file write
issued via `Bash` (`echo >>`, `sed -i`, `python -c "open(...).write(...)"`,
etc.) never reaches `canon_gate.py` at all — confirmed empirically in section
3. Broadening the matcher to include `Bash` is possible but would fire on
*every* Bash call (build commands, git, tests, ...), not just file-writing
ones, and `canon_gate.py` has no way to introspect an arbitrary shell command
for which paths it's about to write — a much harder problem than the current
`$CLAUDE_FILE_PATHS`-driven check. This is a real, standing gap but it's a
hook-design trade-off for a human to weigh (broaden the matcher and accept
false-positive friction on every Bash call, vs. leave the hole and rely on
agents/CLAUDE.md discipline not to route wiki edits through Bash), not
something `canon_gate.py` can close by itself.

## Same finding, restated for the subagent-Edit gap

This is the higher-severity gap of the two: unlike the Bash hole (which is
visible in the matcher config and easy to reason about), the subagent-Edit
bypass looks, from the settings.json and script alone, like it *should* work
— the matcher says `Edit`, the tool called was `Edit`, and the script blocks
correctly when invoked directly. It only fails silently, in a way neither the
ledger nor the agent transcript would flag without an explicit live test like
this one. Recommend treating this as the same class of "human decision /
platform behavior" as the Bash hole — flagging it upstream (Claude Code
feedback channel) rather than attempting a repo-side workaround, since the
repo has no lever over whether the harness invokes its own configured hooks
for a given tool-call context.

## FRICTION LIST

1. **Ticket's probe-file premise went stale between when it was written and
   when I ran it.** `world/items/preserved-eel.md` was named in the ticket as
   authorized-only-by-a-checked-line; by the time I ran the audit, the R3
   ledger section (added `6295152`, ~itself part of this same audit thread)
   had already added the unchecked line-79 authorization naming it. A ticket
   referencing "currently" ledger state is fragile when the ledger is a live,
   fast-moving document in the same repo the ticket describes — worth ticket
   authors re-grepping the *current* ledger at hand-off time rather than
   embedding a state snapshot as fact.
2. **This repo had a concurrent, unrelated agent process actively committing
   to `world/` and the ledger while this audit ran** (visible via `git
   status`/`git log` churn mid-task: new canon pages landing, `world/_meta/index.md`
   rewrites, a whole `sessions/02-conflict-is-a-surety/` tree appearing).
   Running a live-fire enforcement test (editing real files) in a repo with
   an active concurrent writer is inherently risky — my probe line got swept
   into a stranger's legitimate commit before I could revert it (section 2).
   For any future live-hook test like this, safer practice would be to
   either coordinate a quiet window first, or test against a throwaway file
   created solely for the probe (with its own `status: canon` frontmatter)
   rather than a real in-flight ledger target — that would have avoided
   colliding with concurrent work entirely while still exercising identical
   `canon_gate.py` logic.
3. **The subagent-Edit bypass is a platform/harness question this repo can't
   answer from inside itself.** I confirmed the docs claim hooks fire for
   subagent tool calls (with `agent_id`), which contradicts what I observed;
   I could not, from within this sandboxed audit, determine whether that's a
   genuine Claude Code defect, an environment-specific config gap, or a
   narrower condition the docs don't cover. Recommend the human file this
   with Claude Code directly (`/feedback` or the Anthropic issue tracker)
   with the reproduction in section 2, since no repo-side fix is available.
