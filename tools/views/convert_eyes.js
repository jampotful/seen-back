// Converts the views written in src/cam.a.js (EYES and TRY, build 23) into one spec per view in views/<key>.json, following
// docs/ENGINE-DESIGN.md section 3. Run once, from the repository root: node tools/views/convert_eyes.js [path to an older cam.a.js]
// Every number that changes the picture becomes a parameter object. Its grade is '?' (not yet graded, converted from build 23) and its
// source is empty, since the code gave grades only to rows; the research threads grade each parameter when they next touch the view.
'use strict';
const fs = require('fs'), vm = require('vm'), path = require('path');
const root = path.resolve(__dirname, '..', '..');
const file = process.argv[2];
const lines = fs.readFileSync(file, 'utf8').split('\n');
const a = lines.findIndex(l => /^\s*var I3 = /.test(l)), b = lines.findIndex(l => /^\s*var TRY_KEYS = /.test(l));
const ctx = { location: { search: '' } };
vm.createContext(ctx);
vm.runInContext(lines.slice(a, b).join('\n') + '\n;this.EYES = EYES; this.TRY = TRY; this.ORDER = ORDER;' +
  'this.NAMED = { I3: I3, PROTAN: PROTAN, DEUTAN: DEUTAN, BEE: BEE, SIDE_GREEN: SIDE_GREEN, UV_GREEN: UV_GREEN, UV_GREEN_RED: UV_GREEN_RED };', ctx);
const { EYES, TRY, ORDER, NAMED } = ctx;
const NOTES = { PROTAN: 'Vienot, Brettel and Mollon 1999, entered from memory', DEUTAN: 'Vienot, Brettel and Mollon 1999, entered from memory',
  BEE: 'their green drawn as red, their blue as green; ultraviolet goes to blue', SIDE_GREEN: 'the side eyes’ one green class as a dim green; the tint is invented',
  UV_GREEN: 'green as green and ultraviolet as blue, red their mean; receptor fits in research/methods', UV_GREEN_RED: 'the red-filtered class as red, green as green, ultraviolet as blue; receptor fits in research/methods' };
const SWITCH = new Set(['id', 'shape', 'gaze', 'pupil', 'salience']);   // plain values: switches with no claim behind them
const isNum = v => typeof v === 'number' || (Array.isArray(v) && v.length && v.every(x => typeof x === 'number'));
const P = v => ({ value: v, grade: '?', invented: null, src: [] });

function convert(key, m, offered) {
  const mats = {};
  function matrix(v, hint) {
    for (const n in NAMED) if (NAMED[n] === v || JSON.stringify(NAMED[n]) === JSON.stringify(v)) { mats[n] = mats[n] || { rows: [v.slice(0, 3), v.slice(3, 6), v.slice(6, 9)], grade: '?', invented: null, src: [], note: NOTES[n] || '' }; return n; }
    const n = key + '_' + hint; mats[n] = { rows: [v.slice(0, 3), v.slice(3, 6), v.slice(6, 9)], grade: '?', invented: null, src: [] }; return n;
  }
  function wrap(v, k, hint) {
    if (k === 'M') return matrix(v, hint || 'M');
    if (SWITCH.has(k) && !Array.isArray(v) && typeof v !== 'object') return v;
    if (isNum(v)) return P(Array.isArray(v) ? v.slice() : v);
    if (Array.isArray(v)) return v.map((x, i) => wrap(x, k, (hint || k) + i));
    if (v && typeof v === 'object') { const o = {}; for (const j in v) o[j] = wrap(v[j], j, (hint ? hint + '_' : '') + (v.id || j)); return o; }
    return v;
  }
  const spec = { key, version: 1, offered, chip: m.chip, who: m.who, cue: m.cue, params: {} };
  const skip = new Set(['chip', 'who', 'cue', 'rows', 'zones', 'gaze', 'byGenus', 'senses']);
  for (const k in m) if (!skip.has(k)) spec.params[k] = wrap(m[k], k, 'M');
  if (m.zones) spec.zones = m.zones.map((z, i) => { const o = {}; for (const k in z) o[k] = wrap(z[k], k, 'zone_' + (z.id || i)); return o; });
  if (m.gaze) spec.gaze = wrap(m.gaze, 'gaze_block');
  if (m.senses) spec.inputs = { senses: m.senses };
  if (m.byGenus) { spec.by = { genus: {} }; for (const g in m.byGenus) spec.by.genus[g] = wrap(m.byGenus[g], 'by', g); }
  spec.matrices = mats;
  spec.rows = m.rows.map(r => r.slice());
  return spec;
}
const { fmt } = require('./fmt.js');
const out = path.join(root, 'views'); fs.mkdirSync(out, { recursive: true });
const keys = [];
for (const k in EYES) { fs.writeFileSync(path.join(out, k + '.json'), fmt(convert(k, EYES[k], true)) + '\n'); keys.push(k); }
for (const k in TRY) { fs.writeFileSync(path.join(out, k + '.json'), fmt(convert(k, TRY[k], false)) + '\n'); keys.push(k); }
console.log('wrote', keys.length, 'specs:', keys.join(' '));
