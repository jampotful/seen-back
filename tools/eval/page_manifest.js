// Does the page's own manifest reader accept a slot's manifest? Runs readManifest from src/cam.rec.js in Node, with the
// kinds the page knows read from src/cam.a.js. Usage: node tools/eval/page_manifest.js src/cam.rec.js src/cam.a.js <manifest.json>
// Run build 8's own manifest reader (src/cam.rec.js, readManifest) on a manifest file.
const fs = require('fs');
const src = fs.readFileSync(process.argv[2], 'utf8');
const a = src.indexOf('    function num(x)'), b = src.indexOf('    function readTable(');
const eyesSrc = fs.readFileSync(process.argv[3], 'utf8');
const ea = eyesSrc.indexOf('var EYES = {');
let depth = 0, i = ea + 'var EYES = '.length, end = -1;
for (; i < eyesSrc.length; i++) { if (eyesSrc[i] === '{') depth++; else if (eyesSrc[i] === '}') { depth--; if (depth === 0) { end = i + 1; break; } } }
const EYES = {}; for (const mm of eyesSrc.slice(ea, end).matchAll(/^\s{4}([a-z]+): \{/gm)) EYES[mm[1]] = true; console.log('kinds the page knows:', Object.keys(EYES).join(','));
const body = src.slice(a, b);
const f = new Function('EYES', 'big', 'onThisMachine', 'err', body + '\nreturn readManifest;');
const err = (c, d) => { const e = new Error(c + ': ' + d); e.code = c; return e; };
const readManifest = f(EYES, false, false, err);
const m = readManifest(fs.readFileSync(process.argv[4], 'utf8'));
console.log('accepted by build 8 readManifest:', process.argv[4], '| keys:', Object.keys(m).join(','), '| fusion:', JSON.stringify(m.fusion));
