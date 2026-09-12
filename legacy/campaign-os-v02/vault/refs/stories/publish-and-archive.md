---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "The /publish-prep and /archive-story commands: creating promo/publication scaffolding and moving a finished story into the archive."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: c3aaf349-0c71-4b67-afeb-0db49cf8b761
---

# Stories Playbook: /publish-prep and /archive-story

## `/publish-prep`

Reads _Index.md to confirm title and current status, then creates in the story folder, populating what _Index.md provides and leaving the rest as empty placeholders (never inventing details):

- _Promo/Blurb.md: pre-filled with the premise from _Index.md as a draft starting point for editorial refinement.
- _Promo/Tags.md: pre-filled with genre and any themes noted in _Index.md.
- _Promo/Campaign.md: empty, for marketing campaign notes, ARC list, launch plan, etc.
- _Publication.md (story root): from the Publication template, title pre-filled; storefront links, ISBN/ASIN, and cover path left as empty placeholders.

Presents a summary of what the command created and what the author needs to fill in manually.

## `/archive-story`

Reads _Index.md to confirm the story title and current status, then asks: "Archive as Completed or Abandoned?" and waits for the answer.

Once confirmed, proposes and waits for approval before applying:

1. Update _Index.md frontmatter: set `status` to `complete` or `abandoned`.
2. Move the story folder to ../_Archive/Completed/ or ../_Archive/Abandoned/.

Presents the exact destination path for confirmation. After approval, applies both changes and confirms completion. If archiving as Completed and no _Publication.md exists yet, suggests running `/publish-prep` before or after archiving to capture publication details.

See also: [[audit-story]], [[vault-architecture]].
