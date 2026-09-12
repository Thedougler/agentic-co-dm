import { readFileSync } from 'node:fs';

const ABSTRACT = /\b(grief|doctrine|silence|patience|memory|debt|truth|weight|dark|nothing|everything|time|cost)\.?$/i;

function lastSentence(text) {
  const s = text.replace(/\s+/g, ' ').trim().split(/(?<=[.!?]["']?)\s+/);
  return s[s.length - 1] ?? '';
}
function classify(sent) {
  const words = sent.replace(/[^\w\s']/g, '').trim().split(/\s+/).filter(Boolean);
  if (/"$|"\s*$/.test(sent) || sent.startsWith('"')) return 'dialogue';
  if (words.length <= 8 || ABSTRACT.test(sent.trim())) return 'epigram';
  return 'concrete';
}
export function analyze(md, exemplarStats = null) {
  const body = md.replace(/^---\n[\s\S]*?\n---\n/, '');
  const parts = body.split(/^##+ /m).slice(1);
  const sections = parts.map(p => {
    const [head, ...rest] = p.split('\n');
    const prose = rest.join(' ').replace(/\[\[|\]\]|[*_>#]/g, '');
    const last = lastSentence(prose);
    return { heading: head.trim(), ending_class: classify(last), last_sentence: last };
  }).filter(s => s.last_sentence);
  const ending_counts = {};
  let max_run = 0, run = 0, prev = null;
  for (const s of sections) {
    ending_counts[s.ending_class] = (ending_counts[s.ending_class] ?? 0) + 1;
    run = s.ending_class === prev ? run + 1 : 1;
    max_run = Math.max(max_run, run); prev = s.ending_class;
  }
  const sents = body.replace(/\[\[|\]\]/g, '').split(/(?<=[.!?])\s+/).map(s => s.split(/\s+/).length).filter(n => n > 1);
  const mean = sents.reduce((a, b) => a + b, 0) / (sents.length || 1);
  const stdev = Math.sqrt(sents.reduce((a, b) => a + (b - mean) ** 2, 0) / (sents.length || 1));
  const flags = [];
  const n = sections.length;
  for (const [cls, c] of Object.entries(ending_counts))
    // n >= 4, not 3: with only three sections and three ending classes, a >40%
    // share is near-unavoidable and says nothing about the writing. Three-section
    // monotony is still caught, by the max_run rule below.
    if (n >= 4 && c / n > 0.4) flags.push(`ending shape '${cls}' closes ${c}/${n} sections (>40%)`);
  if (max_run >= 3) flags.push(`${max_run} consecutive sections share an ending shape`);
  let exemplar_delta_pct = null;
  if (exemplarStats) {
    exemplar_delta_pct = Math.round(Math.abs(mean - exemplarStats.mean) / exemplarStats.mean * 100);
    if (exemplar_delta_pct > 30) flags.push(`sentence-length mean drifts ${exemplar_delta_pct}% from exemplar corpus`);
  }
  return { sections, ending_counts, max_run, sentence_stats: { mean: +mean.toFixed(1), stdev: +stdev.toFixed(1) }, exemplar_delta_pct, flags };
}
// CLI
if (import.meta.url === `file://${process.argv[1]}`) {
  const [file, flag, profilePath] = process.argv.slice(2);
  let ex = null;
  if (flag === '--profile' && profilePath)
    ex = JSON.parse(readFileSync(profilePath, 'utf8'));
  const r = analyze(readFileSync(file, 'utf8'), ex);
  console.log(JSON.stringify(r, null, 2));
  process.exit(r.flags.length ? 1 : 0);
}
