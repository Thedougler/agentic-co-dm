#!/usr/bin/env node
// inbox:to-md -f <path>
// Converts a non-markdown, non-text file under inbox/ (DOCX, XLSX, images,
// HTML, etc.) to a sibling .md file via markitdown-ts, so the file can be
// ingested with the same llm-wiki-ingest methodology as any other inbox/
// document. Never touches the original — only ever adds a new file next to
// it. A PDF never gets a companion this way — see isPdfPath in lib.mjs;
// load the `anthropic-skills:pdf` skill and extract directly instead.
import { parseArgs } from 'node:util';
import path from 'node:path';
import { resolveInboxPath, companionMarkdownPath, convertToMarkdownCompanion, isPdfPath } from './lib.mjs';

const { values } = parseArgs({ options: { f: { type: 'string' } } });

if (!values.f) {
  console.error('Usage: npm run inbox:to-md -- -f <path>');
  process.exit(1);
}

let absPath;
try {
  absPath = resolveInboxPath(values.f);
} catch (err) {
  console.error(err instanceof Error ? err.message : String(err));
  process.exit(1);
}

if (isPdfPath(absPath)) {
  console.log(
    `${values.f} is a PDF — no companion generated (markitdown-ts drops fillable-form ` +
      'field values). Load the anthropic-skills:pdf skill and extract directly.'
  );
  process.exit(0);
}

if (!companionMarkdownPath(absPath)) {
  console.log(`${values.f} is already markdown/text — nothing to convert.`);
  process.exit(0);
}

try {
  const destAbs = await convertToMarkdownCompanion(absPath);
  console.log(`Wrote ${path.relative(path.dirname(absPath), destAbs)}`);
} catch (err) {
  console.error(err instanceof Error ? err.message : String(err));
  process.exit(1);
}
