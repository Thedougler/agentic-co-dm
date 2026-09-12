#!/usr/bin/env node
// inbox:archive -f <path> [--force]
// Archives one inbox/ file into raw/<YYYY-MM>/, refusing when identical
// content is already archived somewhere under raw/ (dedupe check derived
// directly from raw/'s current contents — no ledger, see lib.mjs). If the
// file has a markitdown-generated .md companion (see inbox:to-md /
// inbox:sweep), the companion is archived alongside it in the same batch —
// same raw/<YYYY-MM>/ destination dir.
//
// The wiki page(s) built from this file are never recorded here — that
// mapping is derived on demand from each vault/ page's own `source:`
// frontmatter (raw/CLAUDE.md's ingestion contract), so this command only
// ever reports it, never stores it.
import { parseArgs } from 'node:util';
import { existsSync } from 'node:fs';
import {
  resolveInboxPath,
  hashFile,
  moveIntoArchive,
  companionMarkdownPath,
  findArchivedByHash,
  findWikiPagesForArchivedPath,
} from './lib.mjs';

const { values } = parseArgs({
  options: {
    f: { type: 'string' },
    force: { type: 'boolean', default: false },
  },
});

if (!values.f) {
  console.error('Usage: npm run inbox:archive -- -f <path> [--force]');
  process.exit(1);
}

let absPath;
try {
  absPath = resolveInboxPath(values.f);
} catch (err) {
  console.error(err instanceof Error ? err.message : String(err));
  process.exit(1);
}

const hash = hashFile(absPath);
const existing = findArchivedByHash(hash);

if (existing.length > 0 && !values.force) {
  const hit = existing[0];
  const citingPages = findWikiPagesForArchivedPath(hit);
  console.error(
    `Refusing to archive: identical content already archived at ${hit}` +
      (citingPages.length > 0
        ? ` (wiki: ${citingPages.join(', ')})`
        : ' (no vault/ page cites it yet)') +
      '. Pass --force to archive it again anyway.'
  );
  process.exit(1);
}

const companionAbs = companionMarkdownPath(absPath);

const archivedPath = moveIntoArchive(absPath, hash);
let companionArchivedPath = null;
if (companionAbs !== null && existsSync(companionAbs)) {
  companionArchivedPath = moveIntoArchive(companionAbs, hashFile(companionAbs));
}

console.log(`Archived ${values.f} -> ${archivedPath}`);
if (companionArchivedPath) console.log(`Archived companion -> ${companionArchivedPath}`);

const citingPages = findWikiPagesForArchivedPath(archivedPath);
if (citingPages.length > 0) {
  console.log(`Wiki: ${citingPages.join(', ')}`);
} else {
  console.log('Wiki: none yet — no vault/ page cites this raw/ path in its source: frontmatter.');
}
