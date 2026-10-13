// Confirms that the specs in views/ give exactly the views an older src/cam.a.js wrote out by hand (EYES and TRY), field by field.
// Usage: node tools/views/same_views.js <older cam.a.js>   (for example from `git show e207805:src/cam.a.js > /tmp/old.js`)
'use strict';
const fs = require('fs'), vm = require('vm'), path = require('path');
const root = path.resolve(__dirname, '..', '..');
function load(file, specs) {
  const L = fs.readFileSync(file, 'utf8').split('\n');
  const a = L.findIndex(l => /^\s*var I3 = /.test(l)), b = L.findIndex(l => /^\s*var TRY_KEYS = /.test(l));
  const ctx = { location: { search: '' } }; vm.createContext(ctx);
  vm.runInContext(L.slice(a, b).join('\n').replace('/*@SPECS@*/{}', JSON.stringify(specs || {})) + '\n;this.EYES = EYES; this.TRY = TRY;', ctx);
  return Object.assign({}, ctx.EYES, ctx.TRY);
}
const sorted = x => Array.isArray(x) ? x.map(sorted) : x && typeof x === 'object' ? Object.keys(x).sort().reduce((o, k) => (x[k] === undefined || k === 'draw' ? o : (o[k] = sorted(x[k]), o)), {}) : x;
const specs = {};
for (const f of fs.readdirSync(path.join(root, 'views'))) if (f.endsWith('.json') && f !== 'index.json') specs[f.slice(0, -5)] = JSON.parse(fs.readFileSync(path.join(root, 'views', f), 'utf8'));
const old = load(process.argv[2]), now = load(path.join(root, 'src', 'cam.a.js'), specs);
let bad = 0;
for (const k in old) {
  const A = JSON.stringify(sorted(old[k])), B = JSON.stringify(sorted(now[k] || null));
  if (A !== B) { bad++; console.log('DIFFERS', k); let i = 0; while (A[i] === B[i]) i++; console.log('  old', A.slice(Math.max(0, i - 60), i + 60)); console.log('  new', B.slice(Math.max(0, i - 60), i + 60)); }
}
console.log(bad ? bad + ' views differ' : 'all ' + Object.keys(old).length + ' views are the same');
process.exit(bad ? 1 : 0);
