# Contract: Session beat card

The interface is the live beat page the DM opens in Reading view. Co-DM is the writer. Players never open it.

## Identity

1. `type: session-prep`. Campaign and session number match the session folder.
2. Filename `Session-<N>-<BB>-<Label>.md`. `<BB>` matches the spine skeleton.
3. Lives in `journal/sessions/<campaign-slug>/<session-number>/` after ingest or accept.

## Cockpit

4. Jobs appear in Session 11 order (see [data-model.md](../data-model.md)). Evidence: `_raw/Session-11-0*.md` beat cards. Do not photocopy a named Session 11 title as the only valid beat.
5. Empty jobs are omitted. Thin and dense beats are the same kind of card.
6. Only the first beat of a session may recap the previous session.
7. At a Glance: stakes, goal or exit, danger, silence, situation magnets.
8. Scene ends when: stop condition, ~30-minute budget, behind/ahead when needed.
9. How the Scene Resolves hands to a beat on this session’s skeleton.

## Markdown shape

10. Column pairs, ruling tables, open `[!narration]`, highlighted italic conditional speech, wikilinks, embeds, real line breaks.
11. Unconditional spoken text is theatre of the mind: no secrets, DCs, unearned names.
12. The only callout is `[!narration]`. Live session callouts stay open.
13. DM-facing lines are complete grammatical sentences. Checks/saves use at-table scan grammar.

## Owners

14. Owner numbers live on owner pages. The beat may carry default-mode action-card numbers for this slice. It must not become a second full owner page.

## Out of contract

Companion notes. Session spine (see [session-spine.md](./session-spine.md)). Older non-Session-11 session-prep. Foundry. Player sheets.
