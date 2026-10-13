// A worker that times an image encoder the way the page's worker (vendor/rec-worker.js) runs one: the page's
// onnxruntime-web build (vendor/ort), the WASM backend, graphOptimizationLevel 'all', one picture at a time.
// Unlike the page it may use more than one thread, which needs a cross-origin isolated page (tools/world/speed.mjs
// serves one). Messages: in {model: url, threads, n, size}; out {op: 'done', ...} or {op: 'fail', message}.
/* global importScripts, ort */
self.onmessage = function (ev) {
  var m = ev.data || {}, now = function () { return performance.now(); }, t0 = now();
  try {
    importScripts('/vendor/ort/ort.wasm.min.js');
  } catch (e) { self.postMessage({ op: 'fail', message: 'runtime: ' + e }); return; }
  ort.env.logLevel = 'error';
  ort.env.wasm.numThreads = m.threads;
  ort.env.wasm.proxy = false;
  ort.env.wasm.wasmPaths = { mjs: '/vendor/ort/ort-wasm-simd-threaded.mjs', wasm: '/vendor/ort/ort-wasm-simd-threaded.wasm' };
  var size = m.size || 224, n = m.n || 20, times = [], session = null, t1, t2, feeds = {}, data = new Float32Array(3 * size * size), seed = 20261013;
  for (var i = 0; i < data.length; i++) { seed = (seed * 1103515245 + 12345) % 2147483648; data[i] = (seed / 2147483648) * 4 - 2; }   // normalized pixel values, fixed
  fetch(m.model).then(function (r) { if (!r.ok) throw new Error('model ' + r.status); return r.arrayBuffer(); }).then(function (buf) {
    t1 = now();
    return ort.InferenceSession.create(new Uint8Array(buf), { executionProviders: ['wasm'], graphOptimizationLevel: 'all' });
  }).then(function (s) {
    session = s; t2 = now();
    feeds[s.inputNames[0]] = new ort.Tensor('float32', data, [1, 3, size, size]);
    var k = 0, warm = [];
    function one() {
      var a = now();
      return session.run(feeds).then(function (out) {
        var ms = now() - a;
        if (k < 2) warm.push(ms); else times.push(ms);
        k++;
        if (k < n + 2) return one();
        var o = out[session.outputNames[0]];
        return { width: o && o.dims ? o.dims[o.dims.length - 1] : null };
      });
    }
    return one().then(function (info) {
      self.postMessage({ op: 'done', threads: ort.env.wasm.numThreads, isolated: self.crossOriginIsolated === true, cores: navigator.hardwareConcurrency,
        input: session.inputNames[0], output: session.outputNames[0], width: info.width, ms: { load: t1 - t0, session: t2 - t1, warm: warm, runs: times } });
    });
  }).catch(function (e) { self.postMessage({ op: 'fail', message: String((e && e.message) || e) }); });
};
