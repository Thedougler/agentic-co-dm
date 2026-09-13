# Data Model: Complete Ingest Context

The feature extends how one open ingest interprets existing files. It does not introduce a database schema.

## Primary Source

The named input file currently `open` for ingest. Completeness unit.

- **path**: Canonical source path the DM named.
- **content**: Untrusted evidence (ideas, links, embeds, names, subject).
- **status**: `open` → `complete` or `failed` (009 transitions still apply).
- **related set**: Related sources discovered for this open primary.

Validation: a primary is not `complete` until related discovery has run, each candidate is `read`, `missed`, or `unreadable`, recency has been applied, and 015 destinations exist for extracted ideas. Failure of the primary still requires a reason. Related misses do not by themselves fail the primary.

## Related Source

A linked, related, or corroborating file for the open primary.

- **identity**: Path or collection hit (staging path, or collection + document id).
- **origin**: `staging` or `legacy`.
- **relation**: Named by link/embed, named explicitly in prose, or same/clearly-related subject.
- **recency**: File time, unless content dates the decision more clearly.
- **role**: `latest-decision` and/or `supporting-context`.
- **status**: `unread` → `read` | `missed` | `unreadable`.

Validation: candidates come only from the primary’s content and subject. Each identity is considered at most once per primary. A related source is not an `open` ingest unit unless it is also a later named primary.

## Recency Rank

Ordering of the primary plus its related *sources* for decision vs support.

- **newest decision source**: The newest relevant file for a given fact, unless content dates that decision more clearly.
- **older variants**: Remaining files on that subject.

Validation: an older source must not silently replace a newer decision. Uncontradicted older detail remains available as supporting context.

## Supporting Context

Uncontradicted detail that exists in an older variant and is absent from the newest decision source.

- **fact**: The extra description, history, name, or detail.
- **from**: Older related source.
- **used**: Included on the compiled page, or recorded unused with a reason.

## Conflict Outcome

When sources disagree, or a source disagrees with compiled wiki canon.

- **newer vs older source**: Keep the newer decision; surface the older contradiction as a proposal or unresolved item.
- **source vs compiled wiki**: Wiki remains current canon; legacy/source contradiction is extra context and a proposal if it would change that page. Named ingest of an approved primary still follows 015 for compiling that primary.

Validation: no silent overwrite of a newer decision; no silent overwrite of compiled wiki canon; no filing a legacy hit as a wiki page without DM accept.

## Ingest Record

Existing per-file report, extended.

- **primary**: Path and `complete` | `failed`.
- **related reads**: Identity, origin (`staging` | `legacy`), role.
- **misses**: Named related identity that was not found or not readable, with reason.
- **recency conflicts**: Files involved and the proposal/unresolved item.
- **destinations**: Unchanged from 015 (pages created/updated, staged, unresolved, proposals).

Transition: record is written when the primary closes. A “no related hits” search is still recorded, not omitted.

## State

```text
named primary open
  → discover related candidates (content + subject)
  → for each candidate: read | missed | unreadable (once)
  → rank recency; classify latest-decision vs supporting-context
  → extract/compile (015) with that evidence
  → close primary complete | failed
  → next named primary (009)
```

Related reads during `open` must not create or change wiki pages attributed to a later named file, and must not mark a later named file `open`.
