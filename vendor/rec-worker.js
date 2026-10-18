/* Seen Back: the recognizer's worker. A classic worker (no modules), so the picture on the page keeps moving
   while a photo is prepared and passed through the image encoder.

   The page sends:   {op:'init', ort:{js,mjs,wasm}, wasmBinary, ep, model, weights?, weightsName?, vision:{input,output,size,mean,std,resize,crop}, width, kinds, nKinds, species, nSpecies,
                      speciesType, speciesScale}
                     (kinds may be absent where there are species: a slot without a kinds head; speciesType 'int8' gives the rows at one byte
                     a number, row after row, with speciesScale one little-endian float32 a row, the row's value being scale * byte; where the
                     model's weights are a file of their own, model is the graph and weights that file's bytes, under the name the graph gives it)
                     (store {keep, parts:[{key, bytes}], verify, sha256, ext} in place of model or weights: the encoder's parts as the page keeps
                     them in Cache Storage, read here; a single file goes straight into the runtime's heap, and weights of their own (ext) into
                     one buffer that is let go once the session is made; verify asks for the whole's checksum on the way)
                     (rows {keep, parts, verify, sha256} in place of species: the species rows' parts, read here from Cache Storage)
                     {op:'run', id, rgba, w, h, wantPre}          rgba: the photo's pixels, 4 bytes each, rows from the top
   and it answers:   {op:'hello'}  {op:'ready', ms, backend, threads}  {op:'done', id, kinds, species, emb, ms, pre?}  {op:'fail', id?, stage, name, message}
                     (stage 'store': the parts could not be read here, and the page sends their bytes instead; stage 'damaged': a whole's
                     checksum is not the manifest's)

   The resize follows Pillow's Image.resize(size, Image.BICUBIC) step for step (8-bit, two passes, its fixed-point
   weights and its rounding), because the label vectors were made from photos prepared by Pillow. */
'use strict';
var session = null, V = null, width = 0, K = null, nK = 0, SP = null, SP8 = null, SC = null, nS = 0, backend = '', trip = '';
// The runtime's own module object, noted when the runtime first sets its view of the heap on it (an assignment no other code here
// makes), so that a model can be read into the heap before the session is made. See intoHeap.
var ORTMOD = null;
try {
  Object.defineProperty(Object.prototype, 'HEAPU8', { configurable: true, set: function (v) {
    Object.defineProperty(this, 'HEAPU8', { value: v, writable: true, configurable: true, enumerable: true }); ORTMOD = this;
  } });
} catch (e) {}


function now() { return (self.performance && performance.now) ? performance.now() : Date.now(); }
function fail(stage, e, id) { self.postMessage({ op: 'fail', id: id, stage: stage, name: String((e && e.name) || ''), message: String((e && e.message) || e || '').slice(0, 300) }); }

// ---------- half-precision vectors
function halves(buf) {
  var n = buf.byteLength >> 1, out = new Float32Array(n), dv = new DataView(buf), P = new Float64Array(32), i, h, e, f;
  for (i = 0; i < 32; i++) P[i] = Math.pow(2, i - 15);
  for (i = 0; i < n; i++) {
    h = dv.getUint16(i * 2, true); e = (h >> 10) & 31; f = h & 1023;
    out[i] = (h & 32768 ? -1 : 1) * (e === 0 ? f * 5.960464477539063e-8 : e === 31 ? (f ? NaN : Infinity) : (1 + f / 1024) * P[e]);
  }
  return out;
}

// ---------- Pillow's bicubic, as in its Resample.c
function cubic(x) {
  var a = -0.5;
  if (x < 0) x = -x;
  if (x < 1) return ((a + 2) * x - (a + 3)) * x * x + 1;
  if (x < 2) return (((x - 5) * x + 8) * x - 4) * a;
  return 0;
}
function weights(inSize, outSize) {
  var scale = inSize / outSize, fscale = scale < 1 ? 1 : scale, support = 2 * fscale, ksize = Math.ceil(support) * 2 + 1;
  var bounds = new Int32Array(outSize * 2), kk = new Int32Array(outSize * ksize), k = new Float64Array(ksize), ss = 1 / fscale, xx, x, center, ww, xmin, xmax, w;
  for (xx = 0; xx < outSize; xx++) {
    center = (xx + 0.5) * scale; ww = 0;
    xmin = Math.trunc(center - support + 0.5); if (xmin < 0) xmin = 0;
    xmax = Math.trunc(center + support + 0.5); if (xmax > inSize) xmax = inSize;
    xmax -= xmin;
    for (x = 0; x < xmax; x++) { w = cubic((x + xmin - center + 0.5) * ss); k[x] = w; ww += w; }
    for (x = 0; x < xmax; x++) {
      w = ww !== 0 ? k[x] / ww : k[x];
      kk[xx * ksize + x] = w < 0 ? Math.trunc(-0.5 + w * 4194304) : Math.trunc(0.5 + w * 4194304);     // 22 bits, rounded away from zero
    }
    bounds[xx * 2] = xmin; bounds[xx * 2 + 1] = xmax;
  }
  return { ksize: ksize, bounds: bounds, kk: kk };
}
// src: w x h pixels, `step` bytes each (the first three are used). Returns ow x oh pixels, 3 bytes each.
function resize(src, w, h, step, ow, oh) {
  var H = weights(w, ow), Vv = weights(h, oh), y0 = Vv.bounds[0], y1 = Vv.bounds[oh * 2 - 2] + Vv.bounds[oh * 2 - 1], rows = y1 - y0;
  var mid = new Uint8Array(ow * rows * 3), out = new Uint8Array(ow * oh * 3), xx, yy, x, y, s0, s1, s2, k, p, o, lo, n, base, v;
  for (yy = 0; yy < rows; yy++) {                              // across, and only the rows the second pass will read
    base = (yy + y0) * w * step;
    for (xx = 0; xx < ow; xx++) {
      lo = H.bounds[xx * 2]; n = H.bounds[xx * 2 + 1]; k = xx * H.ksize; s0 = s1 = s2 = 2097152; p = base + lo * step;
      for (x = 0; x < n; x++, p += step) { v = H.kk[k + x]; s0 += src[p] * v; s1 += src[p + 1] * v; s2 += src[p + 2] * v; }
      o = (yy * ow + xx) * 3;
      v = s0 >> 22; mid[o] = v < 0 ? 0 : v > 255 ? 255 : v;
      v = s1 >> 22; mid[o + 1] = v < 0 ? 0 : v > 255 ? 255 : v;
      v = s2 >> 22; mid[o + 2] = v < 0 ? 0 : v > 255 ? 255 : v;
    }
  }
  for (yy = 0; yy < oh; yy++) {                                // then down
    lo = Vv.bounds[yy * 2] - y0; n = Vv.bounds[yy * 2 + 1]; k = yy * Vv.ksize;
    for (xx = 0; xx < ow; xx++) {
      s0 = s1 = s2 = 2097152; p = (lo * ow + xx) * 3;
      for (y = 0; y < n; y++, p += ow * 3) { v = Vv.kk[k + y]; s0 += mid[p] * v; s1 += mid[p + 1] * v; s2 += mid[p + 2] * v; }
      o = (yy * ow + xx) * 3;
      v = s0 >> 22; out[o] = v < 0 ? 0 : v > 255 ? 255 : v;
      v = s1 >> 22; out[o + 1] = v < 0 ? 0 : v > 255 ? 255 : v;
      v = s2 >> 22; out[o + 2] = v < 0 ? 0 : v > 255 ? 255 : v;
    }
  }
  return out;
}
// The short side to `size` (the long side cut down to a whole number, as int() does), then the middle square.
// crop 'center' takes the left and top edge at floor(spare / 2); 'center-round' rounds halves to the even number, as torchvision does.
function prepare(rgba, w, h, spec) {
  var S = spec.size, ow, oh, big, left, top, u8, x, y, c, i;
  if (w <= h) { ow = S; oh = Math.floor(S * h / w); } else { ow = Math.floor(S * w / h); oh = S; }
  big = (ow === w && oh === h) ? null : resize(rgba, w, h, 4, ow, oh);
  function edge(spare) { if (spec.crop !== 'center-round') return Math.floor(spare / 2); var r = Math.round(spare / 2); return (spare % 2 && r % 2) ? r - 1 : r; }
  left = edge(ow - S); top = edge(oh - S);
  u8 = new Uint8Array(S * S * 3);
  for (y = 0; y < S; y++) for (x = 0; x < S; x++) {
    i = (y * S + x) * 3;
    if (big) { c = ((y + top) * ow + x + left) * 3; u8[i] = big[c]; u8[i + 1] = big[c + 1]; u8[i + 2] = big[c + 2]; }
    else { c = ((y + top) * w + x + left) * 4; u8[i] = rgba[c]; u8[i + 1] = rgba[c + 1]; u8[i + 2] = rgba[c + 2]; }
  }
  return u8;
}
function toTensor(u8, spec) {
  var S = spec.size, n = S * S, t = new Float32Array(3 * n), c, i, m, s;
  for (c = 0; c < 3; c++) { m = spec.mean[c]; s = spec.std[c]; for (i = 0; i < n; i++) t[c * n + i] = (u8[i * 3 + c] / 255 - m) / s; }
  return t;
}
function dots(M, n, e) {
  var out = new Float32Array(n), i, j, s, o;
  for (i = 0; i < n; i++) { s = 0; o = i * width; for (j = 0; j < width; j++) s += M[o + j] * e[j]; out[i] = s; }
  return out;
}
function dots8(Q, scale, n, e) {                     // rows at one byte a number: the full database for the whole world, hundreds of thousands of rows
  var out = new Float32Array(n), i, j, s, o;
  for (i = 0; i < n; i++) { s = 0; o = i * width; for (j = 0; j < width; j++) s += Q[o + j] * e[j]; out[i] = s * scale[i]; }
  return out;
}

// ---------- the larger model, from the page's store into the runtime's heap
// Where the model's 310 MB pass through JavaScript, WebKit holds them in memory more than once besides the heap: the page's joined copy
// (moved to this worker) outlives the session until the collector comes round, and so does each kept part the page reads
// (docs/ENGINES.md, 18 October 2026). Here each part goes from Cache Storage straight into a block of the runtime's heap, one chunk at a
// time, and the session is made from that block: the runtime takes a model that already lies in its heap without copying it, and frees
// the block once the session is made. The runtime is started first with a model of 67 bytes (one Identity node), so that its heap exists.
var TINY = 'CAgSADo3ChAKAXgSAXkiCElkZW50aXR5EgFnWg8KAXgSCgoICAESBAoCCAFiDwoBeRIKCggIARIECgIIAUIECgAQDQ==';
function storeErr(e) { var x = new Error(String((e && e.message) || e || 'the model could not be read into the heap')); x.store = true; return x; }
function let_go(v) {                                 // a chunk copied into the heap is let go at once, not when the collector comes round
  try { if (v && v.buffer instanceof ArrayBuffer && v.byteOffset === 0 && v.byteLength === v.buffer.byteLength && v.buffer.transfer) v.buffer.transfer(0); } catch (e) {}
}
// SHA-256 (FIPS 180-4) over chunks: the whole's checksum, the first time, of a group whose bytes are never in one buffer here that
// WebCrypto would take (a block of the runtime's heap is shared memory, which digest() refuses)
var SHA_K = new Int32Array([0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
  0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d,
  0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
  0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a,
  0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]);
function sha256s() {
  var H = new Int32Array([0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]);
  var W = new Int32Array(64), tail = new Uint8Array(64), nt = 0, len = 0;
  function block(b, o) {
    var i, x, y, t1, t2, a = H[0], c1 = H[1], c2 = H[2], d = H[3], e = H[4], f = H[5], g = H[6], h = H[7];
    for (i = 0; i < 16; i++, o += 4) W[i] = (b[o] << 24) | (b[o + 1] << 16) | (b[o + 2] << 8) | b[o + 3];
    for (i = 16; i < 64; i++) {
      x = W[i - 15]; y = W[i - 2];
      W[i] = (((x >>> 7) | (x << 25)) ^ ((x >>> 18) | (x << 14)) ^ (x >>> 3)) + W[i - 7] + (((y >>> 17) | (y << 15)) ^ ((y >>> 19) | (y << 13)) ^ (y >>> 10)) + W[i - 16] | 0;
    }
    for (i = 0; i < 64; i++) {
      t1 = h + (((e >>> 6) | (e << 26)) ^ ((e >>> 11) | (e << 21)) ^ ((e >>> 25) | (e << 7))) + ((e & f) ^ (~e & g)) + SHA_K[i] + W[i] | 0;
      t2 = (((a >>> 2) | (a << 30)) ^ ((a >>> 13) | (a << 19)) ^ ((a >>> 22) | (a << 10))) + ((a & c1) ^ (a & c2) ^ (c1 & c2)) | 0;
      h = g; g = f; f = e; e = d + t1 | 0; d = c2; c2 = c1; c1 = a; a = t1 + t2 | 0;
    }
    H[0] += a; H[1] += c1; H[2] += c2; H[3] += d; H[4] += e; H[5] += f; H[6] += g; H[7] += h;
  }
  function update(b) {
    var i = 0, n = b.length;
    len += n;
    if (nt) { while (nt < 64 && i < n) tail[nt++] = b[i++]; if (nt < 64) return; block(tail, 0); nt = 0; }
    for (; i + 64 <= n; i += 64) block(b, i);
    while (i < n) tail[nt++] = b[i++];
  }
  function hex() {
    var hi = Math.floor(len / 536870912), lo = (len * 8) >>> 0, pad = new Uint8Array((nt < 56 ? 64 : 128) - nt), L = pad.length, i, out = '';
    pad[0] = 0x80;
    pad[L - 8] = hi >>> 24; pad[L - 7] = hi >>> 16; pad[L - 6] = hi >>> 8; pad[L - 5] = hi; pad[L - 4] = lo >>> 24; pad[L - 3] = lo >>> 16; pad[L - 2] = lo >>> 8; pad[L - 1] = lo;
    update(pad);
    for (i = 0; i < 8; i++) out += ('0000000' + (H[i] >>> 0).toString(16)).slice(-8);
    return out;
  }
  return { update: update, hex: hex };
}
// Each part of a group kept by the page, in order: put(bytes, offset) receives every chunk, at its offset in the whole. The first time
// (st.verify) the whole's checksum is worked out on the way and compared with the manifest's, as the page did with the joined whole.
function damagedErr(h) { var x = new Error('sha256 is ' + h); x.damaged = true; return x; }
function readParts(st, put) {
  if (typeof caches === 'undefined') return Promise.reject(storeErr('this worker has no store'));
  var sum = st.verify && st.sha256 ? sha256s() : null;
  return caches.open(st.keep).then(function (c) {
    var k = 0, at = 0;
    function next() {
      if (k >= st.parts.length) return Promise.resolve();
      var p = st.parts[k++], start = at; at += p.bytes;
      return c.match(p.key, { ignoreVary: true }).then(function (res) {
        if (!res) throw storeErr('a part is no longer kept');
        var reader = res.body.getReader(), done = 0;
        function pump() {
          return reader.read().then(function (r) {
            if (r.done) { if (done !== p.bytes) throw storeErr('a kept part is ' + done + ' bytes, not ' + p.bytes); return; }
            if (done + r.value.length > p.bytes) throw storeErr('a kept part is longer than ' + p.bytes + ' bytes');
            if (sum) sum.update(r.value);
            put(r.value, start + done); done += r.value.length; let_go(r.value); return pump();
          });
        }
        return pump();
      }).then(next);
    }
    return next();
  }).then(function () {
    var h = sum ? sum.hex() : '';
    if (sum && h !== String(st.sha256).toLowerCase()) throw damagedErr(h);
  }, function (e) { throw e && (e.store || e.damaged) ? e : storeErr(e); });
}
function total(st) { var n = 0; st.parts.forEach(function (p) { n += p.bytes; }); return n; }
// the species rows, or the encoder's weights where they are a file of their own: into one buffer of this worker, so that the page never holds them
function rowsFromStore(st) {
  var buf;
  try { buf = new Uint8Array(total(st)); } catch (e) { return Promise.reject(storeErr('no room for the species rows')); }
  return readParts(st, function (b, at) { buf.set(b, at); }).then(function () { return buf.buffer; });
}
function intoHeap(st, opts) {
  var tiny = atob(TINY), u = new Uint8Array(tiny.length), i, n = total(st), ptr = 0, M;
  for (i = 0; i < tiny.length; i++) u[i] = tiny.charCodeAt(i);
  return self.ort.InferenceSession.create(u, opts).then(function (s0) { return s0.release(); }).then(function () {
    M = ORTMOD;
    if (!M || typeof M._malloc !== 'function' || typeof M._free !== 'function' || !M.HEAPU8) throw storeErr('the runtime\'s heap is out of reach');
    ptr = M._malloc(n) >>> 0;
    if (!ptr) throw storeErr('no room in the heap for ' + n + ' bytes');
    return readParts(st, function (b, at) { M.HEAPU8.set(b, ptr + at); });
  }).then(function () {
    var view = new Uint8Array(M.HEAPU8.buffer, ptr, n);
    ptr = 0;                                           // from here the runtime owns the block, and frees it once the session is made
    return view;
  }, function (e) { if (ptr) try { M._free(ptr); } catch (x) {} throw e && (e.store || e.damaged) ? e : storeErr(e); });
}

// ---------- the encoder
function init(m) {
  var t0 = now();
  try { importScripts(m.ort.js); } catch (e) { fail(e && e.name === 'SyntaxError' ? 'browser' : 'runtime', e); return; }
  if (!m.rows) { start(m, t0); return; }
  rowsFromStore(m.rows).then(function (b) { m.species = b; m.rows = null; start(m, t0); }, function (e) { fail(e && e.damaged ? 'damaged' : 'store', e); });
}
function start(m, t0) {
  var t1, t2;
  try {
    V = m.vision; width = m.width; backend = m.ep || 'wasm';
    if (V.resize !== 'shortest-bicubic-antialias' || (V.crop !== 'center' && V.crop !== 'center-round')) throw new Error('unknown resize or crop rule');
    // a slot may come without a kinds head (the larger model: its kind is taken from the species answer)
    K = m.kinds ? halves(m.kinds) : null; nK = m.kinds ? m.nKinds : 0; nS = m.species ? m.nSpecies : 0;
    if (m.species && m.speciesType === 'int8') { SP8 = new Int8Array(m.species); SC = new Float32Array(m.speciesScale || new ArrayBuffer(0)); SP = null; }
    else { SP = m.species ? halves(m.species) : null; SP8 = SC = null; }
    if ((K && K.length !== nK * width) || (SP && SP.length !== nS * width) || (SP8 && (SP8.length !== nS * width || SC.length !== nS)) || (!K && !SP && !SP8)) throw new Error('label vectors of the wrong length');
  } catch (e) { fail('unfit', e); return; }
  t1 = now();
  var ort = self.ort;
  ort.env.logLevel = 'error';
  ort.env.wasm.numThreads = 1;                       // more than one needs a cross-origin isolated page, which a plain static host does not give
  ort.env.wasm.proxy = false;
  ort.env.wasm.wasmPaths = { mjs: m.ort.mjs, wasm: m.ort.wasm };
  if (m.wasmBinary) ort.env.wasm.wasmBinary = m.wasmBinary;
  var opts = { executionProviders: [backend], graphOptimizationLevel: 'all' }, st = m.store;
  // a model whose weights come in an external data file (m.weights, under the name its graph gives the file): the runtime
  // copies them into its heap once, where a single file is first copied in whole and then read into a second copy
  // (with st.ext the weights are read here from the store, and let go with transfer(0) once the session is made)
  (st && st.ext ? rowsFromStore(st).then(function (b) { m.weights = b; return new Uint8Array(m.model); })
    : st ? intoHeap(st, opts) : Promise.resolve(new Uint8Array(m.model))).then(function (bytes) {
    if (m.weights) opts.externalData = [{ path: m.weightsName || 'vision.weights.bin', data: new Uint8Array(m.weights) }];
    return ort.InferenceSession.create(bytes, opts);
  }).then(function (s) {
    var w = m.weights;
    session = s; t2 = now(); m.model = null; m.weights = null; opts.externalData = null;   // the session has its own copy by now: a large model's bytes are let go
    if (w && st && st.ext) let_go(new Uint8Array(w));  // at once, where this worker read them: WebKit would keep them until its collector came round
    if (s.inputNames.indexOf(V.input) < 0) throw new Error('the model has no input named ' + V.input);
    // one pass over an empty picture, so the first real photo does not pay for warming up
    return run1(new Float32Array(3 * V.size * V.size)).then(function () {
      self.postMessage({ op: 'ready', backend: backend, threads: ort.env.wasm.numThreads, ms: { vectors: t1 - t0, session: t2 - t1, warm: now() - t2 } });
    });
  }).catch(function (e) {
    // the runtime failing to start is not the model's fault: its loader could not be fetched, or this browser cannot run it
    var text = String((e && e.message) || e || ''), had = !!session;
    session = null;
    if (e && (e.store || e.damaged)) { fail(e.damaged ? 'damaged' : 'store', e); return; }
    fail(had ? 'session' : /dynamically imported module|Importing a module script failed|importScripts|NetworkError/i.test(text) ? 'runtime' : /no available backend|WebAssembly|wasm/i.test(text) && !/ERROR_CODE/.test(text) ? 'browser' : 'session', e);
  });
}
function run1(t) {
  var feeds = {}; feeds[V.input] = new self.ort.Tensor('float32', t, [1, 3, V.size, V.size]);
  return session.run(feeds).then(function (out) {
    var o = out[V.output] || out[session.outputNames[0]], d = o.data, e = new Float32Array(width), i, s = 0;
    if (!d || d.length < width) throw new Error('the model gave ' + (d ? d.length : 0) + ' values, not ' + width);
    for (i = 0; i < width; i++) s += d[i] * d[i];
    s = Math.sqrt(s) || 1;
    for (i = 0; i < width; i++) e[i] = d[i] / s;
    return e;
  });
}
function run(m) {
  if (!session) { fail('run', new Error('not ready'), m.id); return; }
  var t0 = now(), u8, t, t1;
  try { u8 = prepare(new Uint8Array(m.rgba), m.w, m.h, V); t = toTensor(u8, V); } catch (e) { fail('run', e, m.id); return; }
  t1 = now();
  run1(t).then(function (e) {
    var t2 = now(), kd = K ? dots(K, nK, e) : null, sd = SP ? dots(SP, nS, e) : SP8 ? dots8(SP8, SC, nS, e) : null, t3 = now();
    var msg = { op: 'done', id: m.id, kinds: kd, species: sd, emb: e, ms: { pre: t1 - t0, run: t2 - t1, post: t3 - t2 } };
    if (m.wantPre) msg.pre = u8;
    self.postMessage(msg);
  }).catch(function (e) { fail('run', e, m.id); });
}

self.onmessage = function (ev) {
  var m = ev.data || {};
  if (m.op === 'init') init(m);
  else if (m.op === 'run') {
    if (trip === 'hang') { trip = ''; return; }                                    // only the checks set this: the next photo gets no answer,
    if (trip === 'throw') { trip = ''; throw new Error('stopped by a check'); }    // or the worker fails with it in hand
    run(m);
  }
  else if (m.op === 'die') trip = m.how === 'hang' ? 'hang' : 'throw';
};
self.postMessage({ op: 'hello' });
