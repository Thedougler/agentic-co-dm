# Work

Co-DM output is **Work** addressed to the DM. Players see nothing until the DM accepts and presents. Load this file before prep or wrapup output **and** before any FR-003 wait. FR-002 operations MUST NOT enter Propose. Classify per `AGENTS.md` **Autonomy classification**; do not copy that table. Do not duplicate the glossary in `CONTEXT.md`.

## Propose

Input: DM request in prep or wrapup, plus wiki pages.

Output: inspectable text in the conversation. **Do not create or change a campaign wiki page yet** (FR-019). Creative pages still require Work accept before `_staging/` or live write. FR-002 writes MAY land in `_staging/` without chat propose (`WIKI_STAGED_WRITES` does not change class).

Done when:

- Addressed to the DM.
- Canon claims cite `[[wiki pages]]`.
- Invention is flagged and grounded in wiki pages and/or D&D 5e rules.
- Does not contradict an existing page, or names the conflict for the DM.
- The DM can accept, edit, or reject before any wiki write.

Never present invention as a wiki fact. Never mint a fake wiki citation.

## Decide

The DM accepts (optionally after edit) or rejects.

- A direct imperative to write, update, apply, repair, merge, or file a named existing wiki page is acceptance for that named destination. File it directly. An explicit repair or merge instruction satisfies the gate unless the requested change invents canon.
- A request for ideas, drafting, review, or suggested changes without authorization to write is not acceptance. Propose in chat first.
- Accept → then file a wiki page (`lifecycle: accepted`, or `proposed` if the DM asked to park it). Eligible for the table, and for canon if the DM says so.
- Reject → no wiki page. Not presentable. Not canon.

Chat-only proposals that were never approved leave no page. Accepted pages are the inspectable record (FR-013).

## Named ingest

A named ingest is DM approval for those sources, plus thin complete-sentence stubs for people, places, and things named in them (including as links). Do not create pages for names the sources do not contain. Invented names not in the source are a separate proposal. Named ingest does not wait for a second chat accept.

## Canon

Only accepted Work may change wiki facts. `session-recap` proposes the narrative recap in chat first, then files only `Session-<NN>-Recap.md` after accept — owner-page canon is Campaign Editor / reconcile / ingest.

## Windows

- **Prep:** author Work as chat proposals unless the DM gives a direct imperative filing request for a named existing wiki page. Stage Foundry from accepted Work only.
- **Session:** no Co-DM.
- **Wrapup:** propose outcomes in chat. Still no live table agent.

## File

Classify the write against the stack table in `AGENTS.md`. Unknown reader → `DM`. Vault is `false` until the text is filed as a wiki vault note.

## Table aim

Home: campaign hub wiki page, grouped under layout kind Campaign State. Fields: `players` (at least one; tests use three) and `intent`. Status: `missing` → `recorded` (after DM accept on the campaign hub) → `updated`.

After DM accept, file `players` + `intent` on the existing campaign hub. Do not invent a new wiki kind or `type`.

Co-DM MUST NOT treat Work as aimed while `missing`. Work that could swap onto another table without edits is not aimed. DM Intelligence MUST NOT hold a second copy of the aim. When the DM updates players or intent, later Work uses the updated aim.

Done when: missing aim was asked; recorded aim is on the hub; generic-table Work is not treated as aimed.

## Gaps

A missing wiki fact or missing Co-DM practice MUST NOT prevent playable Work in that sitting. When Work is offered despite a gap, name the gap.

A campaign-facing practice fix is a proposal the DM accepts, edits, or rejects. How the Co-DM works is unchanged until accept. A rejected fix is not applied.

Done when: the DM has playable Work in that sitting and the gap is named; campaign-facing practice is unchanged unless accepted.

## Reflection

After a session sitting (not inside `session-recap` itself — that skill is narrative recap only), offer a reflection when appropriate. After prep, offer a reflection only if the DM asks. Do not run reflection or improvement during a session.

An accepted reflection that needs a campaign fact change becomes a canon proposal and still waits for accept. An accepted campaign-facing practice change becomes an improvement proposal and still waits for accept. Later sittings of that kind of job follow the accepted change.

Done when: a post-session sitting offered inspectable reflection Work when appropriate; wiki facts and campaign-facing practice change only after accept. Narrative recap filing stays in `session-recap` and does not own reflection.
