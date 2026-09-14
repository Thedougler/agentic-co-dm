# Skill Design Dispatch

Follow after the `AGENTS.md` gate classifies an in-scope instruction edit. Classification lives there.

## Non-design

Class `not`: complete the edit in this session. Do not park. Includes
smaller edits to established files and Spec Kit pattern tweaks. Borderline
is `not`. Using a skill to write wiki or session content is `not`.

MUST NOT invoke Claude Code opus except to make a skill, write agent
instructions, or write a wiki template. Campaign wiki pages, session-prep,
TotM, recap, constitution, specs, code, tests, and filling a page from a
template stay with the session agent.

Mixed request: split. Session agent completes non-design in this session.
Design-impact follows Dispatch, Unavailability, or Usage-limit wait.

Done: non-design edits are on disk in this session; no `Parked skill design:`
issue for them.

## Dispatch

Class `design-impact` and no owner overrule — novel skill, skill redesign,
major skill-file change, new subagent, new or rewritten agent-instruction
file, or new or rewritten wiki template only. Conserve Claude Code; skip
dispatch when the session agent can land a small established-file edit.

1. Write a scoped prompt. Keep it minimal, focused, and direct. Name deliverables and completion criteria. No extra standing context.
   - **Outcome** — what must be true when done
   - **Files** — in-scope targets
   - **Bounds** — what must not change
   - **Job** — one design job, not an unbounded rewrite
2. Leave those target instruction files unmodified.
3. Commit non-design work first. Record `HEAD` as dispatch start.
4. Preflight the writer environment before dispatch. For every target path, verify actual create, write, and delete capability at that path, not metadata permissions: existing target — copy bytes aside, write the same bytes back, delete the target, restore it, and compare content to dispatch-start; absent target — create it, write a marker, delete it, and confirm it is absent. If any target fails in the current workspace, do not invoke the writer there. Use a fresh writable isolated worktree when available, restore it to dispatch-start, and run the same preflight before starting. If no preflighted writable target set exists, follow Unavailability or Usage-limit handling.
5. Invoke the designated writer with the scoped prompt: `claude -p --model claude-opus-4-6 --effort medium`. Flags from `claude --help`. Do not use the `opus` alias or default Opus. Tell the writer to follow writing-for-agents and to return a commit or patch. Do not prescribe skill-design method, voice, or structure.
6. Accept only complete delegated work: target-only scope, prompt outcome met, and a writer commit or patch that can be merged from the writer environment. The parent does not hand-edit the delegated change. Permission failure, missing commit/patch, out-of-scope edits, or unmet outcome is a partial writer result: restore all target paths to dispatch-start and follow Unavailability or Usage-limit handling.
7. Designated writer is the sole writer of a change that lands.

Done: writer change accepted, or Unavailability or Usage-limit wait started.

## Unavailability

Writer cannot start, stops, refuses, or errors for a reason other than a usage limit:

1. Restore the prompt’s target paths to the dispatch-start revision (`git checkout <dispatch-start> -- <paths>`).
2. Restore all writer worktrees or patches for those targets to dispatch-start; keep no partial delegated edits.
3. Search existing `Parked skill design:` issues before creating another for the same job.
4. Park with `gh issue create`:
   - Title: `Parked skill design: <outcome>`
   - Label: `ready-for-agent`
   - Body: the scoped prompt
5. Session agent does not write the design-impact change.

States: `open` → `resumed` → `done`.

Done: targets match dispatch-start content; issue exists with the scoped prompt.

## Usage-limit wait

Writer reports a usage limit:

1. Restore the prompt’s target paths to the dispatch-start revision (`git checkout <dispatch-start> -- <paths>`).
2. Restore all writer worktrees or patches for those targets to dispatch-start; keep no partial delegated edits.
3. Do not create a GitHub issue.
4. Record the job and retry time on the feature's `tasks.md`. Retry time is the reset time from the report when present; if none, 5 hours from the stop; if a retry still reports a usage limit with no reset time, 24 hours from that attempt.
5. Do not re-attempt before this time. A new session retries after it. Defer only the Claude-dependent task. Complete remaining tasks that do not depend on it; do not mark those jobs incomplete. Completing other or new work MUST carry those deferred tasks forward still incomplete.
6. Leave the design-impact files at dispatch-start until a designated writer or the last-resort write below lands them.

When every remaining open task is blocked by that usage limit, no other work can be done, and the retry time on the blocked task is more than one hour away, invoke the Codex CLI at ChatGPT 5.5 medium with the same scoped prompt. Re-check those gates before each remaining blocked skill job. Prefer Claude Code if it is usable again, then Codex if Claude Code is still usage-limited.

If that Codex invocation is itself unavailable due to a usage limit, and Claude Code remains unavailable due to a usage limit, write the design-impact change in this session. Follow writing-for-agents. Keep the scoped prompt’s files, bounds, and outcome.

Done: wait path — targets match dispatch-start content; job stays incomplete on `tasks.md` with retry time; independent work completed; deferred tasks carried forward; no GitHub issue. Last-resort path — change is on disk; prompt outcome met; job no longer deferred for that usage-limit wait.

## Verify

After a successful designated-writer run or last-resort session write:

1. For a designated-writer run, verify the merged commit or patch touched only prompt target paths and met the prompt outcome. Partial delegated work is not success; restore targets to dispatch-start and follow Unavailability or Usage-limit handling.
2. Report whether touched files were in-scope and whether the prompt outcome was met.
3. Stop. Do not rewrite those files for the same change.

Owner overrule (explicit skip in `AGENTS.md`) or the usage-limit last-resort write licenses the session agent to write design-impact.

Done: scope and outcome reported; dispatched files unchanged by the session agent for this change unless overrule or last-resort write applied.
