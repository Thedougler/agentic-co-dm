# Ingest record

## 01-primary.md
status: complete
related:
- identity: _raw/01-related.md
  origin: staging
  role: supporting-context
  status: read

## 02-primary.md
status: complete
related:
- identity: _raw/02-sibling.md
  origin: staging
  role: supporting-context
  status: read
- identity: legacy/02-old-variant.md
  origin: legacy
  role: supporting-context
  status: read

## 03-primary.md
status: complete
related:
- identity: legacy/03-old-lighthouse.md
  origin: legacy
  role: supporting-context
  status: read
recency-conflict: newest 03-primary.md says lighthouse is black; older variant says white; kept black; white is a proposal

## 04-primary.md
status: complete
misses:
- identity: missing-ally.md
  reason: not found in staging or legacy

## 05-primary.md
status: complete
related-search: nothing

## 06-a.md
status: complete
related:
- identity: 06-b.md
  origin: staging
  role: supporting-context
  status: read
destinations: entities/first.md
note: 06-b was not an open ingest unit; no destinations attributed to 06-b

## 06-b.md
status: complete
after: 06-a.md
destinations: entities/second.md
