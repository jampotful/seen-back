// Image vectors through onnxruntime-web's WASM build (the runtime the page uses), one photo at a time, single thread,
// with the per-photo time of session.run recorded.
// Usage: node tools/lab/wasm_embed.mjs <node_modules prefix> <model.onnx> <pixels dir> <out.f32> <out latency.json> [threads]
// <pixels dir> holds u8.bin (uint8 [N,3,S,S], RGB, already resized and cropped as Pillow does), ids.json and norm.json.
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';

const [prefix, modelPath, pixDir, outF32, outLat, threadsArg] = process.argv.slice(2);
const require = createRequire(path.join(path.resolve(prefix), 'package.json'));
const ort = require('onnxruntime-web');
const runtime = JSON.parse(fs.readFileSync(path.join(path.resolve(prefix), 'node_modules', 'onnxruntime-web', 'package.json'), 'utf8')).version;
const threads = parseInt(threadsArg || '1', 10);
ort.env.wasm.numThreads = threads;

const norm = JSON.parse(fs.readFileSync(path.join(pixDir, 'norm.json'), 'utf8'));
const ids = JSON.parse(fs.readFileSync(path.join(pixDir, 'ids.json'), 'utf8'));
const S = norm.size, plane = S * S, per = 3 * plane;
const fd = fs.openSync(path.join(pixDir, 'u8.bin'), 'r');
const u8 = Buffer.alloc(per);
const x = new Float32Array(per);
const mean = norm.mean, std = norm.std;

const sess = await ort.InferenceSession.create(new Uint8Array(fs.readFileSync(modelPath)), { executionProviders: ['wasm'], graphOptimizationLevel: 'all' });
const out = fs.openSync(outF32, 'w');
const ms = [];
let width = 0;
// warm-up on the first photo (not recorded)
function load(i) {
  fs.readSync(fd, u8, 0, per, i * per);
  for (let c = 0; c < 3; c++) {
    const m = mean[c], s = std[c], o = c * plane;
    for (let k = 0; k < plane; k++) x[o + k] = (u8[o + k] / 255 - m) / s;
  }
  return new ort.Tensor('float32', x, [1, 3, S, S]);
}
if (ids.length) { for (let w = 0; w < 3; w++) await sess.run({ pixel_values: load(0) }); }
for (let i = 0; i < ids.length; i++) {
  const t = load(i);
  const t0 = performance.now();
  const r = await sess.run({ pixel_values: t });
  ms.push(performance.now() - t0);
  const e = r.image_embeds.data;
  width = e.length;
  fs.writeSync(out, Buffer.from(e.buffer, e.byteOffset, e.byteLength));
  if (i % 500 === 0) console.log(`wasm ${i}/${ids.length} ${ms[ms.length - 1].toFixed(1)} ms`);
}
fs.closeSync(out);
fs.writeFileSync(outLat, JSON.stringify({ runtime, threads, node: process.version, width, count: ids.length, ms }) + '\n');
console.log(`wasm done: ${ids.length} photos, mean ${(ms.reduce((a, b) => a + b, 0) / Math.max(ms.length, 1)).toFixed(1)} ms`);
