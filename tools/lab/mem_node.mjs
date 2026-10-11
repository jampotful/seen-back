// How much memory BioCLIP 2's device file needs in onnxruntime-web's WASM build, in Node, for one way of creating the
// session (a "route"). One route per process, so that every number starts from a fresh process.
// Usage: node --expose-gc tools/lab/mem_node.mjs <node_modules prefix> <route.json> <pixels dir> <out dir>
// route.json: {"name", "model": path, "external": path or null, "external_name": name the graph refers to,
//              "options": session options for InferenceSession.create, "drop_js": true to let go of the file's bytes
//              (and run the garbage collector) once the session exists, "photos": n, "threads": 1}
// Memory is read from /proc/self/status: VmRSS (resident now) and VmHWM (the highest resident size since the last
// reset; writing 5 to /proc/self/clear_refs resets it). The WASM heap is the byteLength of the runtime's
// WebAssembly.Memory (it only grows), caught by wrapping the constructor and WebAssembly.instantiate before the runtime
// loads. Writes <out dir>/<name>.json and <name>.f32 (the photos' vectors, float32, as the runtime returned them).
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';

const [prefix, routePath, pixDir, outDir] = process.argv.slice(2);
const route = JSON.parse(fs.readFileSync(routePath, 'utf8'));
fs.mkdirSync(outDir, { recursive: true });

// ---- catch the runtime's WebAssembly.Memory
const mems = [];
let growCalls = 0;
const OrigMemory = WebAssembly.Memory;
WebAssembly.Memory = new Proxy(OrigMemory, {
  construct(target, args) {
    const m = new target(...args);
    mems.push({ m, how: 'constructed', desc: JSON.parse(JSON.stringify(args[0] || {})) });
    return m;
  },
});
const origGrow = OrigMemory.prototype.grow;
OrigMemory.prototype.grow = function (n) { growCalls++; return origGrow.call(this, n); };
function catchExports(res) {
  const inst = res && (res.instance || res);
  try {
    for (const [k, v] of Object.entries(inst.exports || {})) if (v instanceof OrigMemory && !mems.some((x) => x.m === v)) mems.push({ m: v, how: 'exported:' + k });
  } catch (e) { /* not an instance */ }
  return res;
}
const origInst = WebAssembly.instantiate;
WebAssembly.instantiate = function (...a) { return origInst.apply(this, a).then(catchExports); };
if (WebAssembly.instantiateStreaming) {
  const origStream = WebAssembly.instantiateStreaming;
  WebAssembly.instantiateStreaming = function (...a) { return origStream.apply(this, a).then(catchExports); };
}
const heap = () => mems.reduce((s, x) => Math.max(s, x.m.buffer.byteLength), 0);

// ---- resident memory
function status() {
  const t = fs.readFileSync('/proc/self/status', 'utf8');
  const get = (k) => { const m = t.match(new RegExp('^' + k + ':\\s+(\\d+) kB', 'm')); return m ? +m[1] * 1024 : null; };
  return { rss: get('VmRSS'), hwm: get('VmHWM') };
}
let resetOk = true;
function resetPeak() { try { fs.writeFileSync('/proc/self/clear_refs', '5'); } catch (e) { resetOk = false; } }
const MB = (b) => (b == null ? null : Math.round(b / 1048576 * 10) / 10);   // MiB, as every "_mb" field here

const require = createRequire(path.join(path.resolve(prefix), 'package.json'));
const ort = require('onnxruntime-web');
const runtime = JSON.parse(fs.readFileSync(path.join(path.resolve(prefix), 'node_modules', 'onnxruntime-web', 'package.json'), 'utf8')).version;
ort.env.wasm.numThreads = route.threads || 1;
ort.env.logLevel = 'error';

const norm = JSON.parse(fs.readFileSync(path.join(pixDir, 'norm.json'), 'utf8'));
const ids = JSON.parse(fs.readFileSync(path.join(pixDir, 'ids.json'), 'utf8')).slice(0, route.photos || 24);
const S = norm.size, plane = S * S, per = 3 * plane;
const allPix = fs.readFileSync(path.join(pixDir, 'u8.bin'));
function tensorOf(i) {
  const x = new Float32Array(per);
  if (i >= 0) {
    for (let c = 0; c < 3; c++) {
      const m = norm.mean[c], s = norm.std[c], o = c * plane, b = i * per + o;
      for (let k = 0; k < plane; k++) x[o + k] = (allPix[b + k] / 255 - m) / s;
    }
  }
  return new ort.Tensor('float32', x, [1, 3, S, S]);
}

const rec = { route: route.name, runtime, node: process.version, threads: ort.env.wasm.numThreads, options: route.options || {}, drop_js: !!route.drop_js, steps: [] };
const step = (name, extra) => { const s = status(); const o = Object.assign({ step: name, rss_mb: MB(s.rss), peak_mb: MB(s.hwm), heap_mb: MB(heap()) }, extra || {}); rec.steps.push(o); console.log(JSON.stringify(o)); return o; };

step('start');
// the runtime itself (its WASM module) is loaded by the first session; load it now with nothing in it, so that the
// numbers below are about the model: an empty session is not possible, so we only note the start
let t = performance.now();
let bytes = fs.readFileSync(route.model);                       // a Buffer is a Uint8Array: no second copy
let ext = route.external ? fs.readFileSync(route.external) : null;
rec.model_bytes = bytes.byteLength; rec.external_bytes = ext ? ext.byteLength : 0;
step('file read', { ms: Math.round(performance.now() - t) });

const opts = Object.assign({ executionProviders: ['wasm'], graphOptimizationLevel: 'all' }, JSON.parse(JSON.stringify(route.options || {})));
if (ext) opts.externalData = [{ path: route.external_name || path.basename(route.external), data: ext }];
resetPeak();
t = performance.now();
let sess;
try {
  sess = await ort.InferenceSession.create(bytes, opts);
} catch (e) {
  rec.error = String(e && e.message || e).slice(0, 600);
  step('session failed', { ms: Math.round(performance.now() - t) });
  rec.memories = mems.map((x) => ({ how: x.how, desc: x.desc || null, bytes: x.m.buffer.byteLength }));
  fs.writeFileSync(path.join(outDir, route.name + '.json'), JSON.stringify(rec, null, 1) + '\n');
  console.log('session failed: ' + rec.error);
  process.exit(2);
}
rec.ready_ms = Math.round(performance.now() - t);
step('session created', { ms: rec.ready_ms });
if (route.drop_js) {
  bytes = null; ext = null; delete opts.externalData;
  if (global.gc) { global.gc(); global.gc(); }
  step('file bytes let go');
}
// the page's own warm-up: one pass over an empty picture
resetPeak();
t = performance.now();
await sess.run({ pixel_values: tensorOf(-1) });
step('warm-up (empty picture)', { ms: Math.round(performance.now() - t) });
rec.ready_with_warm_ms = rec.ready_ms + rec.steps[rec.steps.length - 1].ms;
const out = new Float32Array(ids.length * 768);
rec.photo_ms = [];
for (let i = 0; i < ids.length; i++) {
  resetPeak();
  t = performance.now();
  const r = await sess.run({ pixel_values: tensorOf(i) });
  const ms = performance.now() - t;
  rec.photo_ms.push(Math.round(ms));
  const e = (r.image_embeds || r[sess.outputNames[0]]).data;
  out.set(e.subarray(0, 768), i * 768);
  if (i === 0 || i === 9 || i === ids.length - 1) step('photo ' + (i + 1), { ms: Math.round(ms) });
}
fs.writeFileSync(path.join(outDir, route.name + '.f32'), Buffer.from(out.buffer));
rec.ids = ids;
rec.peak_reset_works = resetOk;
rec.heap_final_mb = MB(heap());
rec.grow_calls = growCalls;
rec.memories = mems.map((x) => ({ how: x.how, desc: x.desc || null, mb: MB(x.m.buffer.byteLength) }));
const pm = rec.photo_ms.slice(1);
rec.photo_ms_mean_2_on = pm.length ? Math.round(pm.reduce((a, b) => a + b, 0) / pm.length) : null;
fs.writeFileSync(path.join(outDir, route.name + '.json'), JSON.stringify(rec, null, 1) + '\n');
console.log(`route ${route.name}: ready ${rec.ready_ms} ms, heap ${rec.heap_final_mb} MB, photo mean ${rec.photo_ms_mean_2_on} ms`);
