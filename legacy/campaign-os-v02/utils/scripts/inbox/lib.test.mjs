// Colocated tests for scripts/inbox/lib.mjs. Every filesystem-touching
// assertion runs against an isolated temp sandbox (INBOX_REPO_ROOT), never
// the real repo's inbox/ or raw/.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';

process.env.INBOX_REPO_ROOT = mkdtempSync(path.join(tmpdir(), 'inbox-lib-test-'));

const lib = await import('./lib.mjs');

mkdirSync(lib.INBOX_DIR, { recursive: true });

test('stripFrontmatter removes a leading --- block', () => {
  const content = '---\ntitle: Foo\n---\n# Body\n\nHello.\n';
  assert.equal(lib.stripFrontmatter(content), '# Body\n\nHello.\n');
});

test('stripFrontmatter returns content unchanged when there is no frontmatter', () => {
  const content = '# Body\n\nHello.\n';
  assert.equal(lib.stripFrontmatter(content), content);
});

test('currentYearMonth returns a YYYY-MM string', () => {
  assert.match(lib.currentYearMonth(), /^\d{4}-\d{2}$/);
});

test('hashFile is deterministic for identical content', () => {
  const a = path.join(lib.INBOX_DIR, 'a.md');
  const b = path.join(lib.INBOX_DIR, 'b.md');
  writeFileSync(a, 'same content\n');
  writeFileSync(b, 'same content\n');
  assert.equal(lib.hashFile(a), lib.hashFile(b));
});

test('listInboxFiles finds nested files and skips OS noise', () => {
  const sub = path.join(lib.INBOX_DIR, 'nested');
  mkdirSync(sub, { recursive: true });
  writeFileSync(path.join(sub, 'note.md'), 'hi\n');
  writeFileSync(path.join(lib.INBOX_DIR, '.DS_Store'), '');
  const files = lib.listInboxFiles();
  assert.ok(files.some((f) => f.endsWith(path.join('nested', 'note.md'))));
  assert.ok(!files.some((f) => f.endsWith('.DS_Store')));
});

test('resolveInboxPath accepts both a bare name and an inbox/-prefixed path', () => {
  const abs = path.join(lib.INBOX_DIR, 'resolve-me.md');
  writeFileSync(abs, 'content\n');
  assert.equal(lib.resolveInboxPath('resolve-me.md'), abs);
  assert.equal(lib.resolveInboxPath('inbox/resolve-me.md'), abs);
});

test('resolveInboxPath throws a clear error for a missing file', () => {
  assert.throws(() => lib.resolveInboxPath('does-not-exist.md'), /No such file under inbox\//);
});

test('findArchivedByHash finds nothing when raw/ has no matching file', () => {
  const hash = 'deadbeef'.repeat(8);
  assert.equal(lib.findArchivedByHash(hash).length, 0);
});

test('findArchivedByHash derives a hit straight from raw/\'s contents, no ledger', () => {
  const dir = path.join(lib.ARCHIVE_DIR, '2026-07');
  mkdirSync(dir, { recursive: true });
  const abs = path.join(dir, 'example.md');
  writeFileSync(abs, 'archived content\n');
  const hash = lib.hashFile(abs);

  const hits = lib.findArchivedByHash(hash);
  assert.equal(hits.length, 1);
  assert.equal(hits[0], path.join('raw', '2026-07', 'example.md'));
});

test('findWikiPagesForArchivedPath finds nothing when no vault/ page cites the path', () => {
  mkdirSync(lib.VAULT_DIR, { recursive: true });
  assert.deepEqual(lib.findWikiPagesForArchivedPath('raw/2026-07/uncited.md'), []);
});

test('findWikiPagesForArchivedPath derives citing pages from source: frontmatter, no ledger', () => {
  const npcDir = path.join(lib.VAULT_DIR, 'npcs');
  mkdirSync(npcDir, { recursive: true });
  writeFileSync(
    path.join(npcDir, 'cited.md'),
    '---\ntype: npc\nsource: "raw/2026-07/cited-source.md"\n---\n\n# Cited\n'
  );

  const hits = lib.findWikiPagesForArchivedPath('raw/2026-07/cited-source.md');
  assert.deepEqual(hits, [path.join('vault', 'npcs', 'cited.md')]);
});

test('moveIntoArchive moves the file, dedupes name collisions, and prunes empty dirs', () => {
  const sub = path.join(lib.INBOX_DIR, 'sub');
  mkdirSync(sub, { recursive: true });
  const src = path.join(sub, 'move-me.md');
  writeFileSync(src, 'move me\n');
  const hash = lib.hashFile(src);

  const rel = lib.moveIntoArchive(src, hash);
  assert.equal(rel, path.join('raw', lib.currentYearMonth(), 'move-me.md'));
  assert.ok(existsSync(path.join(lib.REPO_ROOT, rel)));
  assert.ok(!existsSync(src), 'source file no longer under inbox/');
  assert.ok(!existsSync(sub), 'now-empty parent directory was pruned');

  // A second file with the same basename gets a hash-suffixed name instead
  // of overwriting the first.
  mkdirSync(sub, { recursive: true });
  const src2 = path.join(sub, 'move-me.md');
  writeFileSync(src2, 'different content\n');
  const hash2 = lib.hashFile(src2);
  const rel2 = lib.moveIntoArchive(src2, hash2);
  assert.notEqual(rel2, rel);
  assert.ok(rel2.includes(hash2.slice(0, 8)));
});

test('pruneEmptyDirsUpTo stops at stopDir and never removes it', () => {
  const nested = path.join(lib.INBOX_DIR, 'x', 'y', 'z');
  mkdirSync(nested, { recursive: true });
  lib.pruneEmptyDirsUpTo(nested, lib.INBOX_DIR);
  assert.ok(existsSync(lib.INBOX_DIR));
  assert.ok(!existsSync(path.join(lib.INBOX_DIR, 'x')));
});
