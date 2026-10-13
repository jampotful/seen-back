// Times image encoders in headless Chromium through the page's own onnxruntime-web build (vendor/ort), in a worker as
// the page runs its encoder, with one thread and with four (tools/world/speed.html, tools/world/speed-worker.js). The
// repository root is served with the headers that make a page cross-origin isolated, which onnxruntime-web needs for
// more than one thread; the page as published runs one thread (vendor/rec-worker.js).
// Usage: node tools/world/speed.mjs <playwright prefix> <models dir> <out.json> [photos=30] [threads=1,4] [rounds=2]
// The models dir holds <model id>.onnx files; every file is timed at every thread count, the files and thread counts
// taking turns, round after round. Writes out.json and, beside it, SPEED.md.
import { createRequire } from 'node:module';
import http from 'node:http';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const [pwPrefix, modelsDir, outJson, nArg, thrArg, roundsArg] = process.argv.slice(2);
const n = parseInt(nArg || '30', 10), threads = (thrArg || '1,4').split(',').map(Number), rounds = parseInt(roundsArg || '2', 10);
const require = createRequire(path.join(path.resolve(pwPrefix), 'package.json'));
const { chromium } = require('playwright');
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..');
const mdir = path.resolve(modelsDir);
const models = fs.readdirSync(mdir).filter((f) => f.endsWith('.onnx')).sort();
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.wasm': 'application/wasm', '.onnx': 'application/octet-stream', '.json': 'application/json' };
const server = http.createServer((req, res) => {
  const u = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  const f = u.startsWith('/models/') ? path.join(mdir, path.basename(u)) : path.join(root, path.normalize(u));
  fs.stat(f, (err, st) => {
    if (err || !st.isFile()) { res.writeHead(404); res.end(); return; }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream', 'Content-Length': st.size, 'Cache-Control': 'no-store',
      'Cross-Origin-Opener-Policy': 'same-origin', 'Cross-Origin-Embedder-Policy': 'require-corp', 'Cross-Origin-Resource-Policy': 'same-origin' });
    fs.createReadStream(f).pipe(res);
  });
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const port = server.address().port;
const q = (a, p) => { const s = [...a].sort((x, y) => x - y); return s.length ? s[Math.min(s.length - 1, Math.floor(p * (s.length - 1) + 0.5))] : null; };
const r2 = (x) => (x === null || x === undefined ? null : Math.round(x * 10) / 10);
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();
const logs = [];
page.on('console', (m) => logs.push(m.type() + ': ' + m.text().slice(0, 300)));
page.on('pageerror', (e) => logs.push('pageerror: ' + String(e).slice(0, 300)));
await page.goto(`http://127.0.0.1:${port}/tools/world/speed.html`);
const ortV = (/var ORT = \{ v: '([^']+)'/.exec(fs.readFileSync(path.join(root, 'src', 'cam.rec.js'), 'utf8')) || [])[1];
const rec = { what: 'session.run wall time per photo, batch 1, 224 x 224, onnxruntime-web ' + ortV + ' (vendor/ort, the WASM build the page loads)',
  browser: 'Chromium ' + browser.version() + ', headless', page: await page.evaluate(() => window.isolated()),
  machine: { cpus: os.cpus().length, cpu: (os.cpus()[0] || {}).model, memory_gb: Math.round(os.totalmem() / 1073741824 * 10) / 10, platform: os.platform() + ' ' + os.release() },
  photos_per_measurement: n, warm_up_runs: 2, rounds, files: {}, runs: [] };
for (const m of models) rec.files[m] = { bytes: fs.statSync(path.join(mdir, m)).size };
for (let r = 0; r < rounds; r++) {
  for (const m of models) {
    for (const t of threads) {
      const out = await page.evaluate((a) => window.speed(a[0], a[1], a[2]), [`/models/${m}`, t, n]);
      const row = { round: r + 1, model: m.replace(/\.onnx$/, ''), threads_asked: t };
      if (out.op === 'done') {
        Object.assign(row, { threads: out.threads, isolated: out.isolated, input: out.input, width: out.width, session_ms: r2(out.ms.session),
          median_ms: r2(q(out.ms.runs, 0.5)), p90_ms: r2(q(out.ms.runs, 0.9)), min_ms: r2(Math.min(...out.ms.runs)), mean_ms: r2(out.ms.runs.reduce((a, b) => a + b, 0) / out.ms.runs.length),
          warm_ms: out.ms.warm.map(r2), runs_ms: out.ms.runs.map(r2) });
      } else row.fail = out.message;
      rec.runs.push(row);
      console.log(JSON.stringify(Object.fromEntries(Object.entries(row).filter(([k]) => k !== 'runs_ms'))));
    }
  }
}
await browser.close();
server.close();
// every model at every thread count: the median of all its timed runs, over the rounds
rec.summary = [];
for (const m of models) {
  for (const t of threads) {
    const rows = rec.runs.filter((x) => x.model === m.replace(/\.onnx$/, '') && x.threads_asked === t && !x.fail);
    const all = rows.flatMap((x) => x.runs_ms);
    rec.summary.push({ model: m.replace(/\.onnx$/, ''), threads: t, measurements: rows.length, photos: all.length, median_ms: r2(q(all, 0.5)), p90_ms: r2(q(all, 0.9)),
      round_medians_ms: rows.map((x) => x.median_ms), session_ms: rows.map((x) => x.session_ms) });
  }
}
rec.console = logs.slice(0, 40);
fs.writeFileSync(outJson, JSON.stringify(rec, null, 1) + '\n');
const L = ['# Encoder speed in headless Chromium', '', `Made by \`tools/world/speed.mjs\`: ${rec.what}; ${rec.browser}; ${rec.machine.cpus} cores (${rec.machine.cpu}), ${rec.machine.memory_gb} GB; the page cross-origin isolated: ${rec.page.isolated}. ` +
  `${n} timed photos a measurement after 2 to warm up, ${rounds} rounds taking turns. The input is a fixed made-up picture: the encoders do the same work whatever the picture shows.`, '',
  '| Model file | bytes | threads | median ms a photo | 90th percentile | medians of the rounds | session made in ms |', '|---|---:|---:|---:|---:|---|---|'];
for (const s of rec.summary) L.push(`| ${s.model} | ${rec.files[s.model + '.onnx'].bytes.toLocaleString('en-US')} | ${s.threads} | ${s.median_ms} | ${s.p90_ms} | ${s.round_medians_ms.join(', ')} | ${s.session_ms.join(', ')} |`);
const base = rec.summary.filter((s) => /tinyclip/.test(s.model));
if (base.length) {
  L.push('', 'Against TinyCLIP 39M/16 at the same thread count:');
  for (const s of rec.summary) {
    const b = base.find((x) => x.threads === s.threads);
    if (b && b !== s && b.median_ms && s.median_ms) L.push(`- ${s.model}, ${s.threads} thread(s): ${(s.median_ms / b.median_ms).toFixed(2)} times as long (${s.median_ms} ms against ${b.median_ms} ms).`);
  }
}
fs.writeFileSync(path.join(path.dirname(outJson), 'SPEED.md'), L.join('\n') + '\n');
console.log(L.join('\n'));
