#!/usr/bin/env node
// inbox:sweep — walks every file under inbox/ and creates a sibling .md
// companion for each one that doesn't already have one (skipping files that
// are already markdown/text, and skipping PDFs entirely — see isPdfPath in
// lib.mjs; a PDF is read via the `anthropic-skills:pdf` skill instead, never
// this companion). Never touches an existing companion or the original.
// Designed to run unattended from the SessionStart hook: continues past a
// single file's conversion failure rather than aborting the sweep.
import path from 'node:path';
import {
  listInboxFiles,
  companionMarkdownPath,
  convertToMarkdownCompanion,
  isPdfPath,
  INBOX_DIR,
  loadFailureCache,
  saveFailureCache,
  isKnownFailure,
  recordFailure,
  clearFailure,
} from './lib.mjs';
import { existsSync } from 'node:fs';

const converted = [];
const failed = [];
const skipped = [];
const cache = loadFailureCache();
let cacheDirty = false;

for (const absPath of listInboxFiles()) {
  if (isPdfPath(absPath)) continue;
  const destAbs = companionMarkdownPath(absPath);
  if (!destAbs || existsSync(destAbs)) continue;

  // A file whose conversion already failed for this exact content is
  // skipped without importing markitdown-ts at all — see
  // lib.mjs's FAILURE_CACHE_PATH comment for why this matters for
  // SessionStart latency.
  if (isKnownFailure(absPath, cache)) {
    skipped.push(path.relative(INBOX_DIR, absPath));
    continue;
  }

  try {
    await convertToMarkdownCompanion(absPath);
    converted.push(path.relative(INBOX_DIR, destAbs));
    if (clearFailure(absPath, cache)) cacheDirty = true;
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    failed.push({ rel: path.relative(INBOX_DIR, absPath), message });
    recordFailure(absPath, message, cache);
    cacheDirty = true;
  }
}

if (cacheDirty) saveFailureCache(cache);

if (converted.length > 0) {
  console.log('Converted to markdown (inbox/):');
  for (const rel of converted) console.log(`  - ${rel}`);
}

if (failed.length > 0) {
  if (converted.length > 0) console.log('');
  console.log('Failed to convert (inbox/):');
  for (const { rel, message } of failed) console.log(`  - ${rel}: ${message}`);
}

if (skipped.length > 0) {
  if (converted.length > 0 || failed.length > 0) console.log('');
  console.log(
    `Skipped ${skipped.length} known-unconvertible file(s) (unchanged since last failure) — ` +
      `run npm run inbox:to-md -- -f <path> to force a retry: ${skipped.join(', ')}`
  );
}
