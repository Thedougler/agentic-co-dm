#!/usr/bin/env node
// inbox:check — lists every file under inbox/ that hasn't been archived yet
// (by content hash), and flags any whose content was already archived under
// a different name/location. Both checks are derived from disk on every
// run — raw/'s own contents for the hash match, vault/'s `source:`
// frontmatter for the citing wiki page(s) — never a ledger (raw/CLAUDE.md).
import path from 'node:path';
import { hashFile, listInboxFiles, findArchivedByHash, findWikiPagesForArchivedPath, REPO_ROOT } from './lib.mjs';

const files = listInboxFiles();

if (files.length === 0) {
  console.log('inbox is empty — nothing to check.');
  process.exit(0);
}

const fresh = [];
const duplicates = [];

for (const abs of files) {
  const rel = path.relative(path.join(REPO_ROOT, 'inbox'), abs);
  const hash = hashFile(abs);
  const hits = findArchivedByHash(hash);
  if (hits.length === 0) {
    fresh.push(rel);
  } else {
    const archivedPath = hits[0];
    duplicates.push({ rel, archivedPath, wikiPaths: findWikiPagesForArchivedPath(archivedPath) });
  }
}

if (fresh.length > 0) {
  console.log('NEW (needs ingesting):');
  for (const rel of fresh) console.log(`  - ${rel}`);
}

if (duplicates.length > 0) {
  if (fresh.length > 0) console.log('');
  console.log('DUPLICATE (already archived):');
  for (const dup of duplicates) {
    const wiki = dup.wikiPaths.length > 0 ? dup.wikiPaths.join(', ') : '(no vault/ page cites it yet)';
    console.log(`  - ${dup.rel} -> ${dup.archivedPath} (wiki: ${wiki})`);
  }
}
