# Contract: Session-prep ingest preserve

The interface is ingest or promote of approved session-prep into the wiki.

## Preserve

1. Sources that are session-prep beats or spines are filed, not distilled. Body markdown treatments stay: heading spine, column pairs, tables, `[!narration]`, highlighted narration cells, wikilinks, image embeds, filenames.
2. Destination is the session folder `journal/sessions/<campaign-slug>/<session-number>/`.
3. After ingest, the DM runs from that wiki page. They do not need `_raw/` to recover layout or rulings.
4. Re-ingest with no body change does not rewrite the cockpit into a different template.

## Mixed batch

5. Ordinary knowledge sources in the same batch still compile to wiki pages.
6. Session-prep pages in that batch still follow 1–4. They must not land in `concepts/` or `entities/`.

## Companion notes

7. A companion note for that night files into the same session folder. It is not scored as a beat card.

## Gates

8. Unaccepted Work does not publish a wiki page, except named ingest of approved sources.
9. `_raw/Session-11-*.md` remain evidence files; ingest files copies into the session folder rather than restyling the evidence set.
10. Older session-prep outside the Session 11 production set is not rewritten solely to match this format.

## Out of contract

Transcript wrapup rewriting what happened at the table. Distill path for non-session-prep sources.
