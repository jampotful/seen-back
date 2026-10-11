// The larger model through the page's own worker (vendor/rec-worker.js) in headless Chromium, with the renderer's
// resident memory read from ps every 150 ms and kept as a peak for each phase; the worker reports the WASM heap's size
// with every message (ci/lab/mem/wrap-worker.js).
// Usage: node tools/lab/mem_page.mjs <playwright prefix> <port> <model path on the server> <photos> <out.json> <out.f32>
// The server is test/rec/serve.js at the repository root; the pixels are at /pix/u8.bin (tools/lab/mem_prep.py pixels).
import { createRequire } from 'node:module';
import { execFile } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const [pwPrefix, port, modelPath, nArg, outJson, outF32] = process.argv.slice(2);
const require = createRequire(path.join(path.resolve(pwPrefix), 'package.json'));
const { chromium } = require('playwright');
const MB = (kb) => Math.round(kb / 1024 * 10) / 10;
let phase = 'launch';
const peaks = {}, order = [];
function sample() {
  // the browser's processes are this script's descendants (Playwright starts the browser as a child)
  return new Promise((res) => execFile('ps', ['-eo', 'pid=,ppid=,rss=,args='], { maxBuffer: 16 << 20 }, (err, out) => {
    if (err) return res();
    const procs = [];
    for (const line of out.split('\n')) {
      const m = line.trim().match(/^(\d+)\s+(\d+)\s+(\d+)\s+(.*)$/);
      if (m) procs.push({ pid: +m[1], ppid: +m[2], rss: +m[3], args: m[4] });
    }
    const mine = new Set([process.pid]);
    for (let grew = true; grew;) { grew = false; for (const p of procs) if (!mine.has(p.pid) && mine.has(p.ppid)) { mine.add(p.pid); grew = true; } }
    let rMax = 0, rSum = 0, all = 0;
    for (const p of procs) {
      if (!mine.has(p.pid) || p.pid === process.pid) continue;
      all += p.rss;
      if (/--type=renderer/.test(p.args)) { rSum += p.rss; rMax = Math.max(rMax, p.rss); }
    }
    const q = peaks[phase] || (order.push(phase), peaks[phase] = { renderer_max_mb: 0, renderer_sum_mb: 0, browser_all_mb: 0 });
    q.renderer_max_mb = Math.max(q.renderer_max_mb, MB(rMax)); q.renderer_sum_mb = Math.max(q.renderer_sum_mb, MB(rSum)); q.browser_all_mb = Math.max(q.browser_all_mb, MB(all));
    res();
  }));
}
const timer = setInterval(sample, 150);
const rec = { what: 'vendor/rec-worker.js in headless Chromium, one thread, model handed over as the page hands it', phases: peaks, order };
const browser = await chromium.launch({ headless: true });
rec.browser = browser.version();
const page = await browser.newPage();
const logs = [];
page.on('console', (m) => logs.push(m.type() + ': ' + m.text().slice(0, 300)));
page.on('pageerror', (e) => logs.push('pageerror: ' + String(e).slice(0, 300)));
await page.goto(`http://127.0.0.1:${port}/ci/lab/mem/page.html`);
phase = 'page open'; await new Promise((r) => setTimeout(r, 1500)); await sample();
phase = 'model fetched into the page';
rec.fetch = await page.evaluate((p) => window.memFetch(p), modelPath);
await sample();
phase = 'session created (worker init, warm-up)';
rec.init = await page.evaluate((w) => window.memStart(w), parseInt(process.env.WIDTH || '768', 10));
await sample();
console.log('init: ' + JSON.stringify(rec.init));
const n = parseInt(nArg, 10), vecs = new Float32Array(n * 768);
rec.photos = [];
if (rec.init.op === 'ready') {
  for (let i = 0; i < n; i++) {
    phase = i === 0 ? 'photo 1' : i === 9 ? 'photo 10' : 'other photos';
    const r = await page.evaluate((k) => window.memRun(k), i);
    await sample();
    if (r.emb) vecs.set(r.emb.slice(0, 768), i * 768);  // (the larger model's width)
    rec.photos.push({ ms: r.ms, worker_ms: r.worker_ms, heap_mb: Math.round(r.heap / 1048576 * 10) / 10, fail: r.fail });
    if (r.fail) break;
  }
  fs.writeFileSync(outF32, Buffer.from(vecs.buffer));
}
phase = 'after';
await sample();
clearInterval(timer);
rec.heap_mb = rec.photos.length ? rec.photos[rec.photos.length - 1].heap_mb : Math.round((rec.init.heap || 0) / 1048576 * 10) / 10;
rec.console = logs.slice(0, 40);
fs.writeFileSync(outJson, JSON.stringify(rec, null, 1) + '\n');
console.log(JSON.stringify({ peaks, heap_mb: rec.heap_mb, photo_ms: rec.photos.map((p) => p.ms) }));
await browser.close();
