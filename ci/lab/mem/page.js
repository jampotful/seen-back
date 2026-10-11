// The harness page for tools/lab/mem_page.mjs: starts vendor/rec-worker.js (through wrap-worker.js) as the page starts
// the larger model (the runtime's .wasm and the model's bytes handed over as transferred buffers, one thread), then
// sends photos as 224 x 224 RGBA pictures, so the worker's own resize is the identity and its pixels are the Node runs'.
(function () {
  var V = { input: 'pixel_values', output: 'image_embeds', size: 224, mean: [0.48145466, 0.4578275, 0.40821073], std: [0.26862954, 0.26130258, 0.27577711], resize: 'shortest-bicubic-antialias', crop: 'center-round' };
  var w = null, waiters = [], pix = null;
  function next(op) { return new Promise(function (res) { waiters.push({ op: op, res: res }); }); }
  function abs(p) { return new URL(p, location.href).href; }
  var got = null, fetchMs = 0;
  // the model's bytes as one buffer in the page, as the page holds them once it has joined the kept parts
  window.memFetch = function (modelPath, weightsPath) {
    var t0 = performance.now();
    return Promise.all([
      fetch(abs('/vendor/ort/ort-wasm-simd-threaded.wasm')).then(function (r) { return r.arrayBuffer(); }),
      fetch(abs(modelPath)).then(function (r) { return r.arrayBuffer(); }),
      fetch(abs('/pix/u8.bin')).then(function (r) { return r.arrayBuffer(); }),
      weightsPath ? fetch(abs(weightsPath)).then(function (r) { return r.arrayBuffer(); }) : null
    ]).then(function (b) { got = b; pix = new Uint8Array(b[2]); fetchMs = Math.round(performance.now() - t0); return { fetch_ms: fetchMs, model_bytes: b[1].byteLength, weights_bytes: b[3] ? b[3].byteLength : 0 }; });
  };
  window.memStart = function (width) {
    var b = got; got = null; width = width || 768;
    return Promise.resolve().then(function () {
      w = new Worker(abs('/ci/lab/mem/wrap-worker.js'));
      w.onmessage = function (ev) {
        var m = ev.data || {}, i;
        for (i = 0; i < waiters.length; i++) if (waiters[i].op === m.op || m.op === 'fail') { var x = waiters.splice(i, 1)[0]; x.res(m); return; }
      };
      w.onerror = function (e) { var x = waiters.shift(); if (x) x.res({ op: 'fail', message: String(e.message || e) }); };
      return next('hello').then(function () {
        var t1 = performance.now();
        var init = { op: 'init', ep: 'wasm', ort: { js: abs('/vendor/ort/ort.wasm.min.js'), mjs: abs('/vendor/ort/ort-wasm-simd-threaded.mjs'), wasm: abs('/vendor/ort/ort-wasm-simd-threaded.wasm') },
          wasmBinary: b[0], model: b[1], vision: V, width: width, kinds: null, nKinds: 0, species: new ArrayBuffer(width * 2), nSpecies: 1 }, tr = [b[0], b[1]];
        if (b[3]) { init.weights = b[3]; init.weightsName = 'vision.weights.bin'; tr.push(b[3]); }   // read only by a worker with ci/lab/patches/worker-memory.patch
        w.postMessage(init, tr);
        return next('ready').then(function (m) {
          return { op: m.op, fail: m.op === 'fail' ? (m.stage + ': ' + m.message) : '', fetch_ms: fetchMs, ready_ms: Math.round(performance.now() - t1),
            worker_ms: m.ms || null, heap: m.heap || 0, threads: m.threads, backend: m.backend };
        });
      });
    });
  };
  window.memRun = function (i) {
    var S = 224, n = S * S, rgba = new Uint8Array(n * 4), o = i * 3 * n, k;
    for (k = 0; k < n; k++) { rgba[k * 4] = pix[o + k]; rgba[k * 4 + 1] = pix[o + n + k]; rgba[k * 4 + 2] = pix[o + 2 * n + k]; rgba[k * 4 + 3] = 255; }
    var t0 = performance.now();
    w.postMessage({ op: 'run', id: 'p' + i, rgba: rgba.buffer, w: S, h: S }, [rgba.buffer]);
    return next('done').then(function (m) {
      return { op: m.op, fail: m.op === 'fail' ? (m.stage + ': ' + m.message) : '', ms: Math.round(performance.now() - t0), worker_ms: m.ms || null, heap: m.heap || 0, emb: m.emb ? Array.from(m.emb) : null };
    });
  };
})();
