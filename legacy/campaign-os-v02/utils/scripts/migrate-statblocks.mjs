#!/usr/bin/env node
// One-time migration: consolidate every ```statblock fence into vault/statblocks/.
//
// - vault/srd/monsters/*.md (a fence, minimal wrapper page) -> moved
//   wholesale into vault/statblocks/<slug>.md, frontmatter `type: guide` becomes
//   `type: statblock`, `statblock: inline` + matching `name:` added.
// - vault/campaigns/shattered-sea/monsters/*.md and vault/campaigns/shattered-sea/npcs/*.md (a fence embedded in a fuller
//   page) -> the fence is extracted into a new vault/statblocks/<slug>-statblock.md
//   page; the origin page keeps everything else and gets `![[vault/statblocks/<slug>-statblock]]`
//   in the fence's place.
//
// Default is a dry run — prints the plan, writes nothing. Pass --apply to write.
import { readFileSync, writeFileSync, unlinkSync, mkdirSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const APPLY = process.argv.includes('--apply');
const TODAY = new Date().toISOString().slice(0, 10);
const ROOT = process.cwd();
const SRD_DIR = 'vault/srd/monsters';
const CREATURES_DIR = 'vault/creatures';
const NPCS_DIR = 'vault/campaigns/shattered-sea/npcs';
const OUT_DIR = 'vault/statblocks';

function listMd(dir) {
  return readdirSync(join(ROOT, dir))
    .filter((f) => f.endsWith('.md'))
    .map((f) => join(dir, f));
}

function readFile(relPath) {
  return readFileSync(join(ROOT, relPath), 'utf8');
}

function splitFrontmatter(raw) {
  const m = /^---\n([\s\S]*?)\n---\n?/.exec(raw);
  if (!m) return { fm: null, body: raw };
  return { fm: m[1], body: raw.slice(m[0].length) };
}

function fenceRegex() {
  return /```statblock\n[\s\S]*?\n```/;
}

function extractName(fenceText) {
  const m = /^\s*name:\s*"?([^"\n]+?)"?\s*$/m.exec(fenceText);
  return m ? m[1].trim() : null;
}

function fmGet(fm, key) {
  const m = new RegExp(`^${key}:\\s*(.*)$`, 'm').exec(fm);
  return m ? m[1].trim() : null;
}

// --- Plan SRD monster moves (whole-page relocation) ---
const srdFiles = listMd(SRD_DIR);
const srdPlan = [];
const srdSkipped = [];
for (const relPath of srdFiles) {
  const raw = readFile(relPath);
  const fence = fenceRegex().exec(raw);
  if (!fence) {
    srdSkipped.push(relPath);
    continue;
  }
  const { fm, body } = splitFrontmatter(raw);
  const name = extractName(fence[0]);
  if (!fm || !name) {
    srdSkipped.push(relPath);
    continue;
  }
  let newFm = fm.replace(/^type:\s*guide\s*$/m, 'type: statblock');
  if (!/^statblock:/m.test(newFm)) newFm += `\nstatblock: inline`;
  if (!/^name:/m.test(newFm)) newFm += `\nname: "${name}"`;
  const slug = relPath.split('/').pop().replace(/\.md$/, '');
  srdPlan.push({
    from: relPath,
    to: `${OUT_DIR}/${slug}.md`,
    content: `---\n${newFm}\n---\n${body}`,
  });
}

// --- Plan creature/npc fence extractions ---
function planExtractions(dir) {
  const plan = [];
  const skipped = [];
  for (const relPath of listMd(dir)) {
    const raw = readFile(relPath);
    const fence = fenceRegex().exec(raw);
    if (!fence) {
      skipped.push(relPath);
      continue;
    }
    const { fm } = splitFrontmatter(raw);
    const name = extractName(fence[0]);
    if (!fm || !name) {
      skipped.push(relPath);
      continue;
    }
    const slug = relPath.split('/').pop().replace(/\.md$/, '') + '-statblock';
    const newFm = [
      'type: statblock',
      `status: ${fmGet(fm, 'status') ?? 'draft'}`,
      `publish: ${fmGet(fm, 'publish') ?? 'false'}`,
      'aliases: []',
      `created: ${fmGet(fm, 'created') ?? TODAY}`,
      `updated: ${fmGet(fm, 'updated') ?? TODAY}`,
      `tags: ${fmGet(fm, 'tags') ?? '[]'}`,
      `campaigns: ${fmGet(fm, 'campaigns') ?? '[Shattered Sea]'}`,
      'statblock: inline',
      `name: "${name}"`,
    ].join('\n');
    const newPage = `---\n${newFm}\n---\n\n# ${name}\n\n${fence[0]}\n`;
    const embed = `![[${OUT_DIR}/${slug}]]`;
    const patchedOrigin = raw.slice(0, fence.index) + embed + raw.slice(fence.index + fence[0].length);
    plan.push({
      newPage: { to: `${OUT_DIR}/${slug}.md`, content: newPage },
      origin: { path: relPath, content: patchedOrigin },
    });
  }
  return { plan, skipped };
}

const { plan: creaturePlan, skipped: creatureSkipped } = planExtractions(CREATURES_DIR);
const { plan: npcPlan, skipped: npcSkipped } = planExtractions(NPCS_DIR);

// --- Collision check across every new vault/statblocks/ basename ---
const allNewSlugs = [
  ...srdPlan.map((p) => p.to),
  ...creaturePlan.map((p) => p.newPage.to),
  ...npcPlan.map((p) => p.newPage.to),
];
const seen = new Map();
const collisions = [];
for (const p of allNewSlugs) {
  const base = p.split('/').pop();
  if (seen.has(base)) collisions.push([seen.get(base), p]);
  seen.set(base, p);
}

console.log(`SRD monsters: ${srdPlan.length} to move, ${srdSkipped.length} skipped (no fence): ${srdSkipped.join(', ') || 'none'}`);
console.log(`Creatures: ${creaturePlan.length} extracted, ${creatureSkipped.length} skipped (no fence): ${creatureSkipped.join(', ') || 'none'}`);
console.log(`NPCs: ${npcPlan.length} extracted, ${npcSkipped.length} skipped (no fence): ${npcSkipped.join(', ') || 'none'}`);
console.log(`New pages total: ${allNewSlugs.length}`);

if (collisions.length) {
  console.error('COLLISIONS — aborting, nothing written:');
  for (const [a, b] of collisions) console.error(`  ${a} <-> ${b}`);
  process.exit(1);
}

if (!APPLY) {
  console.log('\nDry run only — pass --apply to write changes.');
  console.log('Example SRD move:', srdPlan[0]?.from, '->', srdPlan[0]?.to);
  console.log('Example extraction:', creaturePlan[0]?.origin.path, '-> new page', creaturePlan[0]?.newPage.to);
  process.exit(0);
}

mkdirSync(join(ROOT, OUT_DIR), { recursive: true });

for (const p of srdPlan) {
  writeFileSync(join(ROOT, p.to), p.content, 'utf8');
  unlinkSync(join(ROOT, p.from));
}
for (const p of [...creaturePlan, ...npcPlan]) {
  writeFileSync(join(ROOT, p.newPage.to), p.newPage.content, 'utf8');
  writeFileSync(join(ROOT, p.origin.path), p.origin.content, 'utf8');
}

console.log(`\nApplied: ${srdPlan.length} moved, ${creaturePlan.length + npcPlan.length} extracted, ${allNewSlugs.length} new pages under ${OUT_DIR}/.`);
