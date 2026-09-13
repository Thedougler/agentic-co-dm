# Skill Design Dispatch

Follow after the `AGENTS.md` gate classifies an in-scope instruction edit. Classification lives there.

## Non-design

Class `not`: complete the edit in this session. Do not park. Includes smaller edits to established files, Spec Kit pattern tweaks, and `AGENTS.md`.

Mixed request: split. Session agent completes non-design in this session. Design-impact follows Dispatch, Unavailability, or Usage-limit wait.

Done: non-design edits are on disk in this session; no `Parked skill design:` issue for them.

## Dispatch

Class `design-impact` and no owner overrule — novel skill, skill redesign, or major skill-file change only. Conserve Claude Code; skip dispatch when the session agent can land a small established-file edit.

1. Write a scoped prompt. Keep it minimal, focused, and direct. Name deliverables and completion criteria. No extra standing context.
   - **Outcome** — what must be true when done
   - **Files** — in-scope targets
   - **Bounds** — what must not change
   - **Job** — one design job, not an unbounded rewrite
2. Leave those target instruction files unmodified.
3. Commit non-design work first. Record `HEAD` as dispatch start.
4. Invoke the designated writer with the scoped prompt: `claude -p --model claude-opus-4-6 --effort medium`. Flags from `claude --help`. Do not use the `opus` alias or default Opus. Tell the writer to follow writing-for-agents. Do not prescribe skill-design method, voice, or structure.
5. Designated writer is the sole writer of a change that lands.

Done: writer finished, or Unavailability or Usage-limit wait started.

## Unavailability

Writer cannot start, stops, refuses, or errors for a reason other than a usage limit:

1. Restore the prompt’s target paths to the dispatch-start revision (`git checkout <dispatch-start> -- <paths>`).
2. Search existing `Parked skill design:` issues before creating another for the same job.
3. Park with `gh issue create`:
   - Title: `Parked skill design: <outcome>`
   - Label: `ready-for-agent`
   - Body: the scoped prompt
4. Session agent does not write the design-impact change.

States: `open` → `resumed` → `done`.

Done: targets match dispatch-start content; issue exists with the scoped prompt.

## Usage-limit wait

Writer reports a usage limit:

1. Restore the prompt’s target paths to the dispatch-start revision (`git checkout <dispatch-start> -- <paths>`).
2. Do not create a GitHub issue.
3. Record the job and retry time on the feature's `tasks.md`. Retry time is the reset time from the report when present; if none, 5 hours from the stop; if a retry still reports a usage limit with no reset time, 24 hours from that attempt.
4. Do not re-attempt before this time. A new session retries after it. Defer only the Claude-dependent task. Complete remaining tasks that do not depend on it; do not mark those jobs incomplete. Completing other or new work MUST carry those deferred tasks forward still incomplete.
5. Leave the design-impact files at dispatch-start until a designated writer or the last-resort write below lands them.

When every remaining open task is blocked by that usage limit, no other work can be done, and the retry time on the blocked task is more than one hour away, invoke the Codex CLI at ChatGPT 5.5 medium with the same scoped prompt. Re-check those gates before each remaining blocked skill job. Prefer Claude Code if it is usable again, then Codex if Claude Code is still usage-limited.

If that Codex invocation is itself unavailable due to a usage limit, and Claude Code remains unavailable due to a usage limit, write the design-impact change in this session. Follow writing-for-agents. Keep the scoped prompt’s files, bounds, and outcome.

Done: wait path — targets match dispatch-start content; job stays incomplete on `tasks.md` with retry time; independent work completed; deferred tasks carried forward; no GitHub issue. Last-resort path — change is on disk; prompt outcome met; job no longer deferred for that usage-limit wait.

## Verify

After a successful designated-writer run or last-resort session write:

1. Report whether touched files were in-scope and whether the prompt outcome was met.
2. Stop. Do not rewrite those files for the same change.

Owner overrule (explicit skip in `AGENTS.md`) or the usage-limit last-resort write licenses the session agent to write design-impact.

Done: scope and outcome reported; dispatched files unchanged by the session agent for this change unless overrule or last-resort write applied.
