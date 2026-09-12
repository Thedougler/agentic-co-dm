# Mechanical vs judgment — what this skill may edit directly

Everything in the left column is a shape-only correction — no new fact
invented, no prose touched, reversible by re-running the check. Fix these
directly, the same way any skill fixes its own single-page WIKI-LINT finding:

| Mechanical (fix directly) | Judgment (report, never fix silently) |
|---|---|
| Frontmatter key ordering, boolean coercion, stripping null/junk keys (W1) | A missing required value with no path-inferred default (W1) |
| A status/publish value that's an unambiguous typo of a valid enum member (W2) | Any value where the intended enum member isn't obvious (W2) |
| A tag matching a listed alias in `docs/tags.md` → its canonical form (W13) | A tag not in the canonical list or its aliases — that's a taxonomy decision (W13) -> `tag-taxonomy` resolves it |
| — | Page has no tags at all — a closest-fit proposal is needed (W27) -> `tag-taxonomy` resolves it |
| — | Everything else: broken links (W3 — the CLI *detects* these via `OFM001`, but the fix, a template-instantiate or an alias correction, is still a judgment call), prep-linkage (W4), missing/misordered headings (W5), stale pending pages (W8), page splits (W12), summaries (W14) — all invent or restructure content, never silent |

A canon-page finding still needs real judgment before touching the page —
mechanical or not, "this is trivial" is an assumption worth checking against
the page's actual history before editing in place.

Design principle this table exists to hold the line on
(`npm run lint -- --rules`): never delete or restructure content merely to
silence a linter. A finding and the content are in genuine tension → that's
a NOTED, not a rewrite.
