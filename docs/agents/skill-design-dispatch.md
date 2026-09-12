# Skill Design Dispatch

Follow after the `AGENTS.md` gate classifies an in-scope instruction edit. Classification lives there.

## Non-design

Class `not`: complete the edit in this session. Do not park.

Mixed request: split. Session agent completes non-design in this session. Design-impact follows Dispatch, Unavailability, or Usage-limit wait.

Done: non-design edits are on disk in this session; no `Parked skill design:` issue for them.

## Dispatch

Class `design-impact` and no owner overrule:

1. Write a scoped prompt:
   - **Outcome** — what must be true when done
   - **Files** — in-scope targets
   - **Bounds** — what must not change
   - **Job** — one design job, not an unbounded rewrite
2. Leave those target instruction files unmodified.
3. Commit non-design work first. Record `HEAD` as dispatch start.
4. Invoke the designated writer with the scoped prompt: `claude -p --model claude-opus-4-6 --effort high`. Flags from `claude --help`. Do not use the `opus` alias or default Opus. Tell the writer to follow writing-for-agents. Do not prescribe skill-design method, voice, or structure.
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
2. Do not create parked dispatch.
3. Record retry time: reset time from the report when present; if none, 5 hours from the stop; if a retry still reports a usage limit with no reset time, 24 hours from that attempt.
4. Do not re-attempt before this time. A new session retries after it. Other in-session jobs are not marked incomplete for this reason.
5. Session agent does not write the design-impact change.

Done: targets match dispatch-start content; retry time recorded; no `Parked skill design:` issue.

## Verify

After a successful designated-writer run:

1. Report whether touched files were in-scope and whether the prompt outcome was met.
2. Stop. Do not rewrite those files for the same change.

Owner overrule (explicit skip in `AGENTS.md`) is the only license for the session agent to write design-impact.

Done: scope and outcome reported; dispatched files unchanged by the session agent for this change.
