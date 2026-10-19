/* The recognizer's runtime alone (test/engines/ffbench.html): the model's bytes, the session, and the same input run several times.
   Reports each step's time and the first values of the answer, so that two settings can be compared for speed and for identical output. */
'use strict';
importScripts('../../vendor/ort/ort.wasm.min.js');
function now() { return performance.now(); }
self.onmessage = function (ev) {
  var o = ev.data, R = { model: o.model, opt: o.opt, threads: o.threads, wb: o.wb, t: { runs: [] } }, T = R.t, t0 = now(), v, s;
  function step(x) { self.postMessage({ step: x }); }
  function get(u) { return fetch(u).then(function (r) { if (!r.ok) throw new Error(u + ': ' + r.status); return r.arrayBuffer(); }); }
  var ort = self.ort;
  ort.env.logLevel = 'error'; ort.env.wasm.numThreads = o.threads || 1; ort.env.wasm.proxy = false;
  ort.env.wasm.wasmPaths = { mjs: o.base + 'vendor/ort/ort-wasm-simd-threaded.mjs', wasm: o.base + 'vendor/ort/ort-wasm-simd-threaded.wasm' };
  fetch(o.base + 'models/' + (o.model === 'big' ? 'naturalist' : 'pocket') + '/manifest.json').then(function (r) { return r.json(); }).then(function (man) {
    v = man.vision;
    var wbP = o.wb ? get(o.base + 'vendor/ort/ort-wasm-simd-threaded.wasm').then(function (b) { ort.env.wasm.wasmBinary = b; }) : Promise.resolve();
    if (o.model !== 'big') return wbP.then(function () { return get(o.base + 'models/pocket/' + v.url); }).then(function (b) { return { bytes: new Uint8Array(b) }; });
    var w = new Uint8Array(v.bytes), at = 0;
    return wbP.then(function () { return get(v.graph.url); }).then(function (g) {
      return v.parts.reduce(function (p, part) { return p.then(function () { return get(part.url).then(function (b) { w.set(new Uint8Array(b), at); at += b.byteLength; }); }); }, Promise.resolve())
        .then(function () { return { bytes: new Uint8Array(g), ext: [{ path: v.weights_name, data: w }] }; });
    });
  }).then(function (m) {
    T.fetch = Math.round(now() - t0); step('fetched in ' + T.fetch + ' ms');
    var opts = { executionProviders: ['wasm'], graphOptimizationLevel: o.opt }, t1 = now();
    if (m.ext) opts.externalData = m.ext;
    return ort.InferenceSession.create(m.bytes, opts).then(function (x) { s = x; T.session = Math.round(now() - t1); step('session in ' + T.session + ' ms'); });
  }).then(function () {
    var S = v.size, n = 3 * S * S, x = new Float32Array(n), i, r = 0;
    for (i = 0; i < n; i++) x[i] = Math.sin(i * 0.01) * 1.5;
    function one() {
      if (r >= o.reps) return Promise.resolve();
      var feeds = {}, t2 = now(); feeds[v.input] = new ort.Tensor('float32', x, [1, 3, S, S]);
      return s.run(feeds).then(function (out) {
        var d = (out[v.output] || out[s.outputNames[0]]).data, dt = Math.round(now() - t2), j, sum = 0;
        T.runs.push(dt); step('run ' + r + ' in ' + dt + ' ms');
        if (r === 0) { R.head = Array.prototype.slice.call(d, 0, 6).map(function (z) { return +z.toFixed(6); }); for (j = 0; j < d.length; j++) sum += d[j] * (j % 7 + 1); R.sum = +sum.toFixed(5); }
        r++; return one();
      });
    }
    return one();
  }).then(function () { self.postMessage({ result: R }); }, function (e) { self.postMessage({ error: String((e && e.message) || e).slice(0, 500), result: R }); });
};
