# Contract: Ingest-linked art

Named ingest imports only art the source already names, from the campaign of record.

## Search

Precondition: DM named and approved the source (FR-019).

Collect basenames from `![[file]]`, `![[file|caption]]`, and wikilinks whose target has a media extension.

For each basename, search `Documents/ai-co-dm` for a file whose name equals that basename exactly.

Done when: every linked basename was searched.

Invalid: fuzzy match; directory scrape; generating art.

## Import

- Found and dest absent → copy to `wiki/attachments/<basename>`.
- Found and dest exists → do not overwrite; tell the DM.
- Not found → no file; include the basename in the miss list.

Done when: dest files that were copied resolve the filed page's embeds, and the DM has the miss/skip list.

Invalid: placeholder images; silent overwrite; rewriting embeds to campaign-of-record paths.
