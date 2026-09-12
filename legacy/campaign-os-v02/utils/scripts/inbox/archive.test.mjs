// Colocated CLI-level tests for scripts/inbox/archive.mjs. Runs the real
// script as a subprocess against an isolated temp sandbox (INBOX_REPO_ROOT),
// never the real repo's inbox/ or raw/.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ARCHIVE_CLI = fileURLToPath(new URL('./archive.mjs', import.meta.url));
const CHECK_CLI = fileURLToPath(new URL('./check.mjs', import.meta.url));

function sandbox() {
  const root = mkdtempSync(path.join(tmpdir(), 'inbox-archive-test-'));
  mkdirSync(path.join(root, 'inbox'), { recursive: true });
  return root;
}

/**
 * @param {string} cli
 * @param {string[]} args
 * @param {string} root
 */
function run(cli, args, root) {
  return execFileSync('node', [cli, ...args], {
    encoding: 'utf8',
    env: { ...process.env, INBOX_REPO_ROOT: root },
  });
}

function currentYearMonth() {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
}

test('archives a file and moves it into raw/<YYYY-MM>/', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'note.md'), '# A note\n');

  const out = run(ARCHIVE_CLI, ['-f', 'note.md'], root);
  assert.match(out, /Archived note\.md ->/);
  assert.match(out, /Wiki: none yet/);

  const expected = path.join(root, 'raw', currentYearMonth(), 'note.md');
  assert.ok(existsSync(expected));
  assert.ok(!existsSync(path.join(root, 'inbox', 'note.md')));
});

test('archiving reports the vault/ page(s) whose source: frontmatter already cites the archived path — derived, not passed in', () => {
  const root = sandbox();
  const yyyyMm = currentYearMonth();
  writeFileSync(path.join(root, 'inbox', 'note.md'), '# A note\n');
  const npcDir = path.join(root, 'vault', 'npcs');
  mkdirSync(npcDir, { recursive: true });
  writeFileSync(
    path.join(npcDir, 'foo.md'),
    `---\ntype: npc\nsource: "raw/${yyyyMm}/note.md"\n---\n\n# Foo\n`
  );

  const out = run(ARCHIVE_CLI, ['-f', 'note.md'], root);
  assert.match(out, /Archived note\.md ->/);
  assert.match(out, new RegExp(`Wiki: vault[\\\\/]npcs[\\\\/]foo\\.md`));
});

test('a second inbox:check shows the archived content as DUPLICATE if re-dropped', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'note.md'), 'identical content\n');
  run(ARCHIVE_CLI, ['-f', 'note.md'], root);

  writeFileSync(path.join(root, 'inbox', 're-dropped.md'), 'identical content\n');
  const out = run(CHECK_CLI, [], root);
  assert.match(out, /DUPLICATE \(already archived\):/);
  assert.match(out, /re-dropped\.md ->/);
});

test('refuses to re-archive identical content without --force', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'note.md'), 'identical content\n');
  run(ARCHIVE_CLI, ['-f', 'note.md'], root);

  writeFileSync(path.join(root, 'inbox', 're-dropped.md'), 'identical content\n');
  assert.throws(
    () => run(ARCHIVE_CLI, ['-f', 're-dropped.md'], root),
    /** @param {any} err */ (err) => err.status === 1
  );
});

test('--force allows re-archiving identical content anyway', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'note.md'), 'identical content\n');
  run(ARCHIVE_CLI, ['-f', 'note.md'], root);

  writeFileSync(path.join(root, 'inbox', 're-dropped.md'), 'identical content\n');
  const out = run(ARCHIVE_CLI, ['-f', 're-dropped.md', '--force'], root);
  assert.match(out, /Archived re-dropped\.md ->/);
});

test('prunes an empty inbox subdirectory after moving its only file', () => {
  const root = sandbox();
  mkdirSync(path.join(root, 'inbox', 'sub'), { recursive: true });
  writeFileSync(path.join(root, 'inbox', 'sub', 'note.md'), '# A note\n');

  run(ARCHIVE_CLI, ['-f', 'sub/note.md'], root);
  assert.ok(!existsSync(path.join(root, 'inbox', 'sub')));
});

test('errors clearly on a missing file', () => {
  const root = sandbox();
  assert.throws(
    () => run(ARCHIVE_CLI, ['-f', 'nope.md'], root),
    /** @param {any} err */ (err) => err.status === 1
  );
});

test('archives a file and its markdown companion together, in one batch', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'source.pdf'), 'not really a pdf\n');
  writeFileSync(path.join(root, 'inbox', 'source.md'), 'converted content\n');

  const out = run(ARCHIVE_CLI, ['-f', 'source.pdf'], root);
  assert.match(out, /Archived source\.pdf ->/);
  assert.match(out, /Archived companion ->/);

  const yyyyMm = currentYearMonth();
  assert.ok(existsSync(path.join(root, 'raw', yyyyMm, 'source.pdf')));
  assert.ok(existsSync(path.join(root, 'raw', yyyyMm, 'source.md')));
  assert.ok(!existsSync(path.join(root, 'inbox', 'source.pdf')));
  assert.ok(!existsSync(path.join(root, 'inbox', 'source.md')));
});

test('archives a file with no companion exactly as before (no companion line, no crash)', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'lonely.pdf'), 'not really a pdf\n');

  const out = run(ARCHIVE_CLI, ['-f', 'lonely.pdf'], root);
  assert.match(out, /Archived lonely\.pdf ->/);
  assert.doesNotMatch(out, /Archived companion/);
});
