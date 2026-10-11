// Run exported image encoders in onnxruntime-web's WASM backend (the build the page uses), single-threaded,
// and compare with onnxruntime CPU and with the original model.
// Usage: node tools/lab/wasm_check.mjs <node_modules prefix> <onnx dir> <wasm dir> <out json>
// <wasm dir> holds input.f32 + shape.json (pixel_values), torch_ref.f32 and ort_<variant>.f32 written by lab.py export.
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';

const [prefix, onnxDir, wasmDir, outJson] = process.argv.slice(2);
const require = createRequire(path.join(path.resolve(prefix), 'package.json'));
const ort = require('onnxruntime-web');
const ortVersion = JSON.parse(fs.readFileSync(path.join(path.resolve(prefix), 'node_modules', 'onnxruntime-web', 'package.json'), 'utf8')).version;
ort.env.wasm.numThreads = 1;

const shape = JSON.parse(fs.readFileSync(path.join(wasmDir, 'shape.json'), 'utf8'));
const readF32 = (f) => { const b = fs.readFileSync(f); return new Float32Array(b.buffer, b.byteOffset, b.byteLength / 4); };
const input = readF32(path.join(wasmDir, 'input.f32'));
const [n, c, h, w] = shape;
const per = c * h * w;

function cosRows(a, b, rows) {
  const d = a.length / rows; const out = [];
  for (let r = 0; r < rows; r++) {
    let ab = 0, aa = 0, bb = 0;
    for (let k = 0; k < d; k++) { const x = a[r * d + k], y = b[r * d + k]; ab += x * y; aa += x * x; bb += y * y; }
    out.push(ab / Math.sqrt(aa * bb));
  }
  return out;
}
const stats = (xs) => ({ mean: xs.reduce((s, x) => s + x, 0) / xs.length, min: Math.min(...xs) });

const result = { onnxruntime_web: ortVersion, backend: 'wasm', threads: 1, node: process.version, photos: n, files: {} };
const torchRef = fs.existsSync(path.join(wasmDir, 'torch_ref.f32')) ? readF32(path.join(wasmDir, 'torch_ref.f32')) : null;
for (const variant of ['int8', 'fp16', 'fp32']) {
  const f = path.join(onnxDir, `vision.${variant}.onnx`);
  if (!fs.existsSync(f)) continue;
  const info = {};
  try {
    const t0 = Date.now();
    const sess = await ort.InferenceSession.create(new Uint8Array(fs.readFileSync(f)), { executionProviders: ['wasm'], graphOptimizationLevel: 'all' });
    info.load_ms = Date.now() - t0;
    const outs = [];
    for (let i = 0; i < n; i++) {
      const x = new ort.Tensor('float32', input.slice(i * per, (i + 1) * per), [1, c, h, w]);
      const r = await sess.run({ pixel_values: x });
      outs.push(r.image_embeds.data);
    }
    const d = outs[0].length;
    const got = new Float32Array(n * d);
    outs.forEach((o, i) => got.set(o, i * d));
    const cpuF = path.join(wasmDir, `ort_${variant}.f32`);
    if (fs.existsSync(cpuF)) info.cosine_vs_ort_cpu = stats(cosRows(got, readF32(cpuF), n));
    if (torchRef) info.cosine_vs_torch = stats(cosRows(got, torchRef, n));
    const x1 = new ort.Tensor('float32', input.slice(0, per), [1, c, h, w]);
    for (let k = 0; k < 3; k++) await sess.run({ pixel_values: x1 });
    const ts = [];
    for (let k = 0; k < 10; k++) { const t = performance.now(); await sess.run({ pixel_values: x1 }); ts.push(performance.now() - t); }
    info.latency_ms_1thread = { mean: ts.reduce((s, x) => s + x, 0) / ts.length, min: Math.min(...ts), runs: 10, warmup: 3, batch: 1 };
    info.runs = true;
    await sess.release();
  } catch (e) {
    info.runs = false;
    info.error = String(e && e.message ? e.message : e).slice(0, 2000);
  }
  result.files[variant] = info;
  console.log(variant, JSON.stringify(info));
}
fs.writeFileSync(outJson, JSON.stringify(result, null, 1) + '\n');
