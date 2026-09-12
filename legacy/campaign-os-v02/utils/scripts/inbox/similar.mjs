#!/usr/bin/env node
// inbox:similar -f <path>
// Surfaces existing wiki content similar to a candidate inbox/ (or already
// archived) file, via qmd's semantic search — a pre-write duplicate-content
// check before ingesting.
import { parseArgs } from 'node:util';
import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { resolveInboxOrArchivePath, stripFrontmatter, REPO_ROOT } from './lib.mjs';

const EXCERPT_LENGTH = 500;
const QMD_BIN = path.join(REPO_ROOT, 'node_modules', '.bin', 'qmd');

const { values } = parseArgs({ options: { f: { type: 'string' } } });

if (!values.f) {
  console.error('Usage: npm run inbox:similar -- -f <path>');
  process.exit(1);
}

let absPath;
try {
  absPath = resolveInboxOrArchivePath(values.f);
} catch (err) {
  console.error(err instanceof Error ? err.message : String(err));
  process.exit(1);
}

const content = readFileSync(absPath, 'utf8');
const body = stripFrontmatter(content).trim();
// qmd's plain expand-query form must be a single line (a multi-line document
// requires per-line lex:/vec:/hyde: prefixes) — flatten whitespace.
const excerpt = body.slice(0, EXCERPT_LENGTH).replace(/\s+/g, ' ').trim();

if (!excerpt) {
  console.log('File is empty after stripping frontmatter — nothing to search on.');
  process.exit(0);
}

// The "wiki" collection unions vault/ (see qmd_session_update.sh
// and the "wiki" row in .claude/skills/llm-wiki-query/SKILL.md's collections table) —
// use it for a combined search across all four.
const result = spawnSync(QMD_BIN, ['query', excerpt, '-c', 'wiki', '--json'], { encoding: 'utf8' });

if (result.error) {
  console.error(`Failed to run qmd: ${result.error.message}`);
  process.exit(1);
}
if (result.status !== 0) {
  console.error(`qmd exited with status ${result.status}:`);
  console.error(result.stderr || result.stdout);
  process.exit(1);
}

let hits;
try {
  hits = JSON.parse(result.stdout);
} catch (err) {
  const message = err instanceof Error ? err.message : String(err);
  console.error(`Could not parse qmd output as JSON: ${message}`);
  console.error(result.stdout);
  process.exit(1);
}

if (!Array.isArray(hits) || hits.length === 0) {
  console.log('No similar wiki content found.');
  process.exit(0);
}

for (const hit of hits) {
  const file = (hit.file || '').replace(/^qmd:\/\//, '');
  console.log(`[${hit.score}] ${file}`);
  if (hit.snippet) console.log(hit.snippet);
  console.log('');
}
