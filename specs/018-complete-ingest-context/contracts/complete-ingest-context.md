# Contract: Complete ingest context

The interface is wiki ingest of one named primary (and, in a batch, each named primary in sequence). Co-DM is the writer. Players never open the pages.

This contract adds a completeness pass inside the open primary. It does not replace [sequential ingest](../../009-sequential-ingest-quality/contracts/sequential-ingest.md), [ingestion quality](../../015-wiki-ingest-polish/contracts/ingest-quality.md), or [retrieval precedence](../../004-qmd-search-default/contracts/retrieval-precedence.md).

## Completeness unit

1. The named primary is the completeness unit. Related files are corroboration for that primary, not a parallel ingest.
2. A primary is not `complete` until related discovery has run and each candidate is `read`, `missed`, or `unreadable`.
3. A request for speed does not skip related search.
4. A missing, unreadable, or unreachable related source is recorded and does not stall the primary.

## Discovery bound

5. Candidates come from the primary’s content (links, embeds, explicit names) and from the primary’s own subject.
6. Do not treat the rest of the vault as in-scope merely because it exists.
7. Each related identity is considered at most once per primary. Do not loop on mutual links.

## Where to search

8. Search the staging area (`_raw/`) for those candidates and read each relevant hit.
9. Search the legacy collections for the same subject and for clearly related subjects, and read relevant hits as supporting context. Use the existing search index (`qmd`). Fetch full sources before relying on a fact; do not answer from snippets.
10. A staging hit does not skip the legacy search. A legacy hit does not skip the staging search.
11. Ingest-time corroboration does not use query-time short-circuit (`wiki` silence before legacy). Compiled `wiki` is still the page to update and current canon on conflict.

## Recency

12. Among the primary and its related sources, newest files are the latest decisions.
13. Older versions and variants remain supporting context. Uncontradicted older detail stays available to the compiled page.
14. An older file must not silently override a newer decision. Surface that conflict as a proposal or explicit unresolved item.
15. Recency defaults to which file is newer. If the content itself dates a decision more clearly, that dating wins for that decision.

## Sequential and canon gates

16. Related reads must not open a later named input file, and must not create or change wiki pages attributed to a later named file, while the current primary is `open`.
17. If a related file is itself a later named input, ingest it as a primary only on its sequential turn.
18. Legacy hits remain campaign-of-record context. Do not file them as compiled wiki pages without DM accept.
19. When compiled wiki and a legacy hit disagree, wiki remains current canon. Mention the legacy wording only as extra context or a proposal.
20. Unaccepted Work does not publish, except named ingest of approved sources.

## Report

21. After the primary closes, report: the primary; each related file read; origin (`staging` or `legacy`); each miss; each recency conflict that was surfaced.
22. If related search returned nothing, say so. Do not omit the search.

## Out of contract

Changing query-time lookup order. Ingesting the entire legacy vault. A new media pipeline. Foundry staging. Player-facing sheets. Restyling pages that are not in the ingest.
