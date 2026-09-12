# Quickstart: Session Beat Format

Prove the feature on Session 11 evidence plus one new beat. Do not restyle older `wiki/journal/Session 0N - Recap.md` files.

## Prerequisites

- Branch `007-session-beats-format`
- Spec [spec.md](./spec.md)
- Contracts in [contracts/](./contracts/)
- `run-guide` states Session 11 job order with omit-empty
- `wiki-ingest` has the preserve-and-file branch
- Session home path is `wiki/journal/sessions/<campaign-slug>/<session-number>/`

## 1. Cockpit vs Session 11 (P1)

Open `_raw/Session-11-01-Angry-Birds.md` and `_raw/Session-11-02-Landing-Sign.md`. Confirm both have the cockpit jobs in order, columns/tables/narration intact, no empty headings, spoken blocks free of secrets/DCs/unearned names.

Author **one new** live beat (do not photocopy a Session 11 title). File as Work. A second DM starts the slice from that page in under 45 seconds and judges it the same kind of card as Session 11 (SC-001, SC-002).

## 2. Spine is not a cockpit (P2)

Open `_raw/Session-11-00-Birds-of-a-Feather.md`. Name length, prize, opposition, dramatic spine, and beat 1’s link. Fail if the spine contains Zones or Be ready for. Follow the Hook link and run from that card.

## 3. Ingest preserve (P1)

Ingest or promote the Session 11 spine plus at least one beat card (and, if present in the batch, one ordinary knowledge source).

Expected:

- Pages land in `wiki/journal/sessions/shattered-sea/11/` with Session 11 filenames
- Reading view still shows columns, tables, `[!narration]`, embeds
- Knowledge source (if any) compiled as a wiki page, not stuffed into the session folder as a beat
- Beat is not a `concepts/` page (SC-003, SC-005)

Re-run ingest with no body change. Fail if the cockpit is rewritten.

## 4. Folder home (P1)

From `wiki/journal/sessions/shattered-sea/11/` open spine then beats in filename order in under 15 seconds without `_raw/` (SC-007). Confirm owner links leave the folder. Confirm no creature/place owner pages were copied in.

## 5. Spoken safety (SC-004)

Read aloud Initial Narration and How the Scene Resolves on three Session 11 beats and the new beat. Fail on a secret, DC, or unearned name in those surfaces.

## 6. Older sessions untouched (SC-006)

This change set does not rewrite pre-Session-11 session-prep or recaps solely to match the cockpit.

## 7. Agent path

Load `wiki/AGENTS.md`. Confirm `session-prep` is in the type set and the session folder path is stated. Confirm `run-guide` points at Session 11 as evidence, not as a clone title. Confirm `wiki-ingest` says preserve session-prep.

Pass: steps 1–7 hold. Fail any step → format is not in force yet.
