
  // ---------- recognition in the page itself (the pocket recognizer)
  // Outside Claude's viewer the page names the photo by itself: an image encoder run by ONNX Runtime Web in a worker
  // (vendor/rec-worker.js), and label vectors worked out beforehand. The files are described by models/<slot>/manifest.json
  // (docs/CONTRACTS.md). Nothing here is fetched before the opening screen is up, and nothing about a photo leaves the device.
  // Kept copies: every file is asked for with ?v=<version> and kept under that address, so a new version is a new address.
  // The runtime's version is its release number; a slot's version is a fingerprint of its manifest, which is always asked of the network first.
  var ORT = { v: '1.30.0', dir: 'vendor/ort/', js: 'ort.wasm.min.js', mjs: 'ort-wasm-simd-threaded.mjs', wasm: 'ort-wasm-simd-threaded.wasm', wasmBytes: 14239897, ep: 'wasm' };
  var pocket = (function () {
    var asked = /[?&]rec=([A-Za-z0-9_.\/-]+)/.exec(location.search || ''), slot = asked ? asked[1] : 'models/pocket';
    var manifestUrl = /\.json$/.test(slot) ? slot : slot.replace(/\/$/, '') + '/manifest.json';
    var cannot = inViewer ? 'off' : slot === 'off' || /\.\.|^\/|\/\//.test(slot) ? 'off'
      : (typeof Worker !== 'function' || typeof WebAssembly !== 'object' || typeof fetch !== 'function' || typeof Float32Array !== 'function') ? 'browser' : '';
    var SAY = {
      off: 'This page’s recognizer is switched off.',
      absent: 'This page has no recognizer yet.',
      missing: 'The recognizer’s files are missing.',
      network: 'The recognizer could not be downloaded.',
      damaged: 'The recognizer’s file arrived damaged.',
      unfit: 'The recognizer’s files do not fit this build of the page.',
      browser: 'This browser cannot run the recognizer.',
      died: 'The recognizer stopped working.',
      slow: 'The recognizer took too long.',
      photo: 'The recognizer failed on that photo.'
    };
    var KEEP = 'keep-v1', EPS = 1e-9;
    var state = cannot ? 'failed' : 'idle', why = cannot, M = null, cur = null, worlds = [], worker = null, loadP = null, loadMs = 0, info = { backend: '', threads: 0 };
    var got = 0, total = 0, pending = {}, nextId = 1, last = null, lastFail = '', onProgress = null, watchMs = 45000;

    function err(code, detail) { var e = new Error(SAY[code] || code); e.code = code; e.sentence = SAY[code] || SAY.died; e.detail = String(detail || ''); return e; }
    function abs(u, base) { try { return new URL(u, base || location.href).href; } catch (e) { return u; } }
    function withV(u, v) { return u + (u.indexOf('?') < 0 ? '?' : '&') + 'v=' + encodeURIComponent(v); }
    function fingerprint(text) {                       // two rounds of FNV-1a: enough to tell one manifest from the next
      var a = 0x811c9dc5, b = 0x01000193 ^ text.length, i, c;
      for (i = 0; i < text.length; i++) { c = text.charCodeAt(i); a = Math.imul(a ^ c, 0x01000193); b = Math.imul(b ^ (c + i), 0x85ebca6b); }
      return ('0000000' + (a >>> 0).toString(16)).slice(-8) + ('0000000' + (b >>> 0).toString(16)).slice(-8);
    }
    function keepOpen() { try { return window.caches ? caches.open(KEEP).catch(function () { return null; }) : Promise.resolve(null); } catch (e) { return Promise.resolve(null); } }
    function tick(n) { got += n; if (onProgress) onProgress(); }
    function readAll(res, expect) {                    // the whole body, counted as it arrives
      if (!res.body || !res.body.getReader) return res.arrayBuffer().then(function (b) { tick(b.byteLength); return b; });
      var reader = res.body.getReader(), buf = expect ? new Uint8Array(expect) : null, chunks = [], n = 0;
      function pump() {
        return reader.read().then(function (r) {
          if (r.done) return;
          var c = r.value;
          if (buf && n + c.length <= buf.length) buf.set(c, n); else { if (buf) { chunks.push(buf.slice(0, n)); buf = null; } chunks.push(c); }
          n += c.length; tick(c.length); return pump();
        });
      }
      return pump().then(function () {
        if (buf) return n === buf.length ? buf.buffer : buf.slice(0, n).buffer;
        var out = new Uint8Array(n), o = 0; chunks.forEach(function (c) { out.set(c, o); o += c.length; }); return out.buffer;
      });
    }
    // One file: the kept copy if there is one, otherwise the network, counted toward the progress line.
    function file(cache, url, expect, check) {
      var hit = cache ? cache.match(url).catch(function () { return null; }) : Promise.resolve(null);
      return hit.then(function (res) {
        if (res) return res.arrayBuffer().then(function (b) {
          if (expect && b.byteLength !== expect) { return cache.delete(url).then(function () { return file(cache, url, expect, check); }); }   // a kept copy cut short is thrown away
          return b;
        });
        total += expect || 0; if (onProgress) onProgress();
        return fetch(url).then(function (r) {
          if (!r.ok) throw err(r.status === 404 ? 'missing' : 'network', url + ' ' + r.status);
          if (!expect) { var len = +r.headers.get('content-length') || 0; total += len; }
          return readAll(r, expect).catch(function (e) { throw e && e.code ? e : err('network', url); }).then(function (b) {
            if (expect && b.byteLength !== expect) throw err('damaged', url + ' is ' + b.byteLength + ' bytes, not ' + expect);
            return (check ? check(b) : Promise.resolve()).then(function () {
              if (!cache) return b;
              // kept by the page itself, unless the service worker has kept the same bytes under the same address already
              return cache.match(url).catch(function () { return null; }).then(function (there) {
                if (there) return b;
                var copy = new Response(b, { headers: { 'Content-Type': r.headers.get('content-type') || 'application/octet-stream', 'Content-Length': String(b.byteLength) } });
                return cache.put(url, copy).catch(function () {}).then(function () { return b; });   // a full disk is no reason to fail
              });
            });
          });
        }, function (e) { throw e && e.code ? e : err('network', url); });
      });
    }
    function sha256(want) {
      return function (b) {
        if (!want || !(window.crypto && crypto.subtle && crypto.subtle.digest)) return Promise.resolve();
        return crypto.subtle.digest('SHA-256', b).then(function (d) {
          var h = Array.prototype.map.call(new Uint8Array(d), function (x) { return ('0' + x.toString(16)).slice(-2); }).join('');
          if (h !== String(want).toLowerCase()) throw err('damaged', 'sha256 is ' + h);
        });
      };
    }
    function num(x) { return typeof x === 'number' && isFinite(x); }
    function readManifest(text) {
      var m; try { m = JSON.parse(text); } catch (e) { throw err('damaged', 'manifest is not JSON'); }
      var v = m && m.vision, f = m && m.fusion, k = m && m.kinds;
      if (!v || !f || !k || !Array.isArray(k.labels) || !num(m.width) || !num(v.size) || !Array.isArray(v.mean) || !Array.isArray(v.std) || !v.url || !k.url || !num(f.t_kind)) throw err('unfit', 'manifest lacks a field');
      if (k.labels.some(function (l) { return l !== 'none' && !EYES[l]; })) throw err('unfit', 'a kind this page does not know');
      if (m.species && !(m.species.url && m.species.table && num(m.species.count) && num(f.t_species) && num(f.alpha_prior) && num(f.w_kind) && num(f.name_at) && num(f.offer_at))) throw err('unfit', 'species without their settings');
      // a trained head carries a bias for each row; a manifest may choose how the two heads are combined. Anything this build does not know is refused, not guessed at.
      if (k.bias !== undefined && k.bias !== null && !(Array.isArray(k.bias) && k.bias.length === k.labels.length && k.bias.every(num))) throw err('unfit', 'kinds.bias does not match the labels');
      if (f.rule !== undefined && f.rule !== 'product' && f.rule !== 'mix') throw err('unfit', 'a combination rule this page does not know');
      if (f.guard !== undefined && !(num(f.guard) && f.guard > 0)) throw err('unfit', 'fusion.guard is not a positive number');
      return m;
    }
    function readTable(buf, count) {                   // rows: [scientific, English, kind, twelve monthly weights], or the same as objects
      var t, rows; try { t = JSON.parse(new TextDecoder('utf-8').decode(buf)); } catch (e) { throw err('damaged', 'species table is not JSON'); }
      rows = Array.isArray(t) ? t : t && t.species;
      if (!Array.isArray(rows) || rows.length !== count) throw err('unfit', 'species table has ' + (rows ? rows.length : 0) + ' rows, not ' + count);
      return rows.map(function (r) {
        var a = Array.isArray(r) ? r : [r.sci, r.en, r.kind || r.eyes, r.m], kind = EYES[a[2]] ? a[2] : 'other', m = Array.isArray(a[3]) && a[3].length === 12 ? a[3] : null;
        return { sci: clip(a[0], 80), en: clip(a[1], 60), kind: kind, m: m };
      });
    }
    function floats(buf, count) {                      // a trained head's biases for the species: little-endian float32, one for each row
      if (!buf || buf.byteLength !== count * 4) throw err('damaged', 'species biases of the wrong length');
      var dv = new DataView(buf), out = new Float64Array(count), i;
      for (i = 0; i < count; i++) out[i] = dv.getFloat32(i * 4, true);
      return out;
    }
    function slotOf(m, rows, sb) {                     // everything the scoring needs: the settings, the labels, the species table, the biases
      var has = {};
      if (rows) rows.forEach(function (r) { has[r.kind] = 1; });
      if (sb && (!rows || sb.length !== rows.length)) throw err('unfit', 'species biases do not match the table');
      return { f: m.fusion, labels: m.kinds.labels, table: rows, has: has, kb: m.kinds.bias ? Float64Array.from(m.kinds.bias) : null, sb: sb || null, prior: {} };
    }
    function prune(cache, base, v) {                   // older versions of this slot and of the runtime are let go
      if (!cache) return;
      cache.keys().then(function (keys) {
        keys.forEach(function (req) {
          var u; try { u = new URL(req.url); } catch (e) { return; }
          var ver = /[?&]v=([^&]+)/.exec(u.search), here = u.href.split('?')[0];
          if (!ver) return;
          if (here.indexOf(base) === 0 && here.slice(base.length).indexOf('/') < 0 && decodeURIComponent(ver[1]) !== v) cache.delete(req);
          if (here.indexOf(abs(ORT.dir)) === 0 && decodeURIComponent(ver[1]) !== ORT.v) cache.delete(req);
        });
      }).catch(function () {});
    }
    function stop(code, detail) {                      // the worker is gone or cannot be trusted: everything waiting hears of it
      var w = worker, p = pending; worker = null; pending = {};
      if (w) { w.onmessage = w.onerror = null; try { w.terminate(); } catch (e) {} }
      state = 'failed'; why = code; lastFail = code + (detail ? ': ' + detail : ''); loadP = null;
      Object.keys(p).forEach(function (id) { clearTimeout(p[id].timer); p[id].rej(err(code, detail)); });
    }
    function startWorker(init, transfer) {
      return new Promise(function (res, rej) {
        var w, hello = false, settled = false, timer;
        function no(code, detail) { if (settled) { stop(code, detail); return; } settled = true; clearTimeout(timer); stop(code, detail); rej(err(code, detail)); }
        try { w = new Worker('vendor/rec-worker.js?v=' + BUILD); } catch (e) { rej(err('browser', e && e.message)); return; }
        worker = w;
        timer = setTimeout(function () { no('slow', 'starting'); }, Math.max(watchMs, 60000));
        w.onerror = function (e) { if (e && e.preventDefault) e.preventDefault(); no(hello ? 'died' : 'network', e && e.message); };
        w.onmessage = function (ev) {
          var m = ev.data || {}, p;
          if (m.op === 'hello') { hello = true; return; }
          if (m.op === 'ready') { settled = true; clearTimeout(timer); info = { backend: m.backend, threads: m.threads, ms: m.ms }; res(); return; }
          if (m.op === 'fail' && !m.id) { no(m.stage === 'runtime' ? 'network' : m.stage === 'browser' ? 'browser' : m.stage === 'unfit' ? 'unfit' : m.stage === 'session' ? 'damaged' : 'died', m.stage + ' ' + m.name + ' ' + m.message); return; }
          p = pending[m.id]; if (!p) return;
          delete pending[m.id]; clearTimeout(p.timer);
          if (m.op === 'done') p.res(m); else p.rej(err('photo', m.message));
        };
        w.postMessage(init, transfer);
      });
    }
    function load() {
      var t0 = performance.now(), cacheRef = null, v = '', base = abs(manifestUrl).replace(/[^\/]*$/, ''), fromKeep = { model: false };
      state = 'loading'; why = ''; got = 0; total = 0;
      return keepOpen().then(function (cache) {
        cacheRef = cache;
        // the manifest: the network first, so that a new model is noticed; the kept copy where there is no network
        function keptOne(detail) {
          return (cache ? cache.match(abs(manifestUrl)).catch(function () { return null; }) : Promise.resolve(null)).then(function (hit) { if (!hit) throw err('network', detail); return hit.text(); });
        }
        return fetch(manifestUrl, { cache: 'no-cache' }).then(function (r) {
          if (r.status === 404) throw err('absent', manifestUrl);            // taken away on purpose, or never there
          if (!r.ok) return keptOne(manifestUrl + ' ' + r.status);           // a server having a bad moment
          return r.text().then(function (text) { if (cache) cache.put(abs(manifestUrl), new Response(text, { headers: { 'Content-Type': 'application/json' } })).catch(function () {}); return text; });
        }, function () { return keptOne(manifestUrl); });
      }).then(function (text) {
        M = readManifest(text); v = fingerprint(text); cur = null;
        var V = M.vision, nK = M.kinds.labels.length, nS = M.species ? M.species.count : 0, c = cacheRef;
        function u(rel) { return withV(abs(rel, base), v); }
        var modelUrl = u(V.url);
        return (c ? c.match(modelUrl).catch(function () { return null; }) : Promise.resolve(null)).then(function (hit) {
          fromKeep.model = !!hit;
          return Promise.all([
            file(c, withV(abs(ORT.dir + ORT.wasm), ORT.v), ORT.wasmBytes),
            file(c, modelUrl, num(V.bytes) ? V.bytes : 0, sha256(V.sha256)),
            file(c, u(M.kinds.url), nK * M.width * 2),
            M.species ? file(c, u(M.species.url), nS * M.width * 2) : null,
            M.species ? file(c, u(M.species.table), 0) : null,
            M.species && M.species.bias_url ? file(c, u(M.species.bias_url), nS * 4) : null
          ]);
        }).then(function (b) {
          cur = slotOf(M, M.species ? readTable(b[4], nS) : null, b[5] ? floats(b[5], nS) : null);
          total = got;                                 // the downloads are over; what remains is starting the encoder
          if (onProgress) onProgress();
          var init = { op: 'init', ep: ORT.ep, ort: { js: withV(abs(ORT.dir + ORT.js), ORT.v), mjs: withV(abs(ORT.dir + ORT.mjs), ORT.v), wasm: withV(abs(ORT.dir + ORT.wasm), ORT.v) },
            wasmBinary: b[0], model: b[1], vision: { input: V.input || 'pixel_values', output: V.output || 'image_embeds', size: V.size, mean: V.mean, std: V.std, resize: V.resize, crop: V.crop || 'center' },
            width: M.width, kinds: b[2], nKinds: nK, species: b[3], nSpecies: nS };
          return startWorker(init, [b[0], b[1], b[2]].concat(b[3] ? [b[3]] : [])).catch(function (e) {
            // a kept model that will not start is thrown away, so the next try fetches it afresh
            if (e.code === 'damaged' && c) return c.delete(modelUrl).catch(function () {}).then(function () { throw e; });
            throw e;
          });
        });
      }).then(function () {
        state = 'ready'; loadMs = performance.now() - t0; prune(cacheRef, base, v);
        diag('pocket-ready', M.id + ' ' + Math.round(loadMs) + 'ms ' + (fromKeep.model ? 'kept' : 'fetched'));
      }, function (e) {
        if (!e || !e.code) e = err('died', e && e.message);
        if (state !== 'failed' || !why) { state = 'failed'; why = e.code; lastFail = e.code + (e.detail ? ': ' + e.detail : ''); }
        loadP = null;
        diag('pocket-failed', lastFail.slice(0, 160));
        throw e;
      });
    }
    function ready() {
      if (cannot) return Promise.reject(err(cannot));
      if (state === 'ready' && worker) return Promise.resolve();
      if (!loadP) { loadP = load(); loadP.catch(function () {}); }
      return loadP;
    }

    // ---------- from the encoder's numbers to a name
    function softmax(z) {
      var n = z.length, out = new Float64Array(n), m = -Infinity, s = 0, i;
      for (i = 0; i < n; i++) if (z[i] > m) m = z[i];
      for (i = 0; i < n; i++) { out[i] = Math.exp(z[i] - m); s += out[i]; }
      for (i = 0; i < n; i++) out[i] /= s;
      return out;
    }
    function priorFor(c, month) {                      // log of each species' share of this month's records, with a floor so that an unrecorded month is unlikely and not impossible
      var key = (typeof month === 'number' && month === Math.floor(month) && month >= 0 && month < 12) ? month : 'none';   // no month known: no prior
      if (c.prior[key]) return c.prior[key];
      var t = c.table, n = t.length, out = new Float64Array(n), sum = 0, i, floor = num(c.f.prior_floor) ? c.f.prior_floor : 1e-6;
      if (key !== 'none') {
        for (i = 0; i < n; i++) sum += t[i].m ? Math.max(0, +t[i].m[key] || 0) : 0;
        if (sum > 0) for (i = 0; i < n; i++) out[i] = Math.log(Math.max(t[i].m ? Math.max(0, +t[i].m[key] || 0) / sum : 0, floor));
      }
      c.prior[key] = out; return out;
    }
    // From the two heads' scores to a kind of eye, a name and offers. tools/fusion/fuse.py is the same arithmetic in numpy, line for line,
    // and tools/fusion/parity.py holds the two to the same answers; a change here is a change there.
    //   kd, sd: row . e for each kind row and each species row, e being the unit image vector. The rows are used as they are: a trained
    //   head's rows are weights, not unit vectors, and it adds a bias to each score.
    function fuseWith(c, kd, sd, month) {
      var f = c.f, labels = c.labels, table = c.table, n = labels.length, z = new Float64Array(n), i, p, q = {}, s = null, order = [], comb, kinds = [], species = [];
      for (i = 0; i < n; i++) z[i] = f.t_kind * kd[i] + (c.kb ? c.kb[i] : 0);
      p = softmax(z);
      if (table && sd) {
        var pr = f.alpha_prior ? priorFor(c, month) : null, zs = new Float64Array(table.length);
        for (i = 0; i < zs.length; i++) zs[i] = f.t_species * sd[i] + (c.sb ? c.sb[i] : 0) + (pr ? f.alpha_prior * pr[i] : 0);
        s = softmax(zs);
        for (i = 0; i < s.length; i++) { q[table[i].kind] = (q[table[i].kind] || 0) + s[i]; order.push(i); }
        order.sort(function (a, b) { return s[b] - s[a]; });
        species = order.slice(0, 5).map(function (j) { return { sci: table[j].sci, en: table[j].en, p: s[j], kind: table[j].kind }; });
      }
      // a kind the species list can speak for is scored by both heads; one it has no rows for (nothing alive, a person) by the kinds alone
      function speaks(i) { return !!(s && c.has[labels[i]]); }
      if (f.rule === 'mix') {
        // mixing: the species head re-divides the share the kinds head gave to the kinds it can speak for, and moves at most 1 - w_kind of it
        var A = 0, tot = 0; comb = new Float64Array(n);
        for (i = 0; i < n; i++) if (speaks(i)) A += p[i];
        for (i = 0; i < n; i++) { comb[i] = speaks(i) ? f.w_kind * p[i] + (1 - f.w_kind) * A * (q[labels[i]] || 0) : p[i]; tot += comb[i]; }
        if (tot > 0) for (i = 0; i < n; i++) comb[i] /= tot; else comb = p;
      } else {
        // the product (the rule of build 6): a weighted sum of logarithms, with a guard under each so that a zero is unlikely and not impossible
        var g = num(f.guard) ? f.guard : EPS, score = new Float64Array(n);
        for (i = 0; i < n; i++) score[i] = speaks(i) ? f.w_kind * Math.log(Math.max(p[i], g)) + (1 - f.w_kind) * Math.log(Math.max(q[labels[i]] || 0, g)) : Math.log(Math.max(p[i], g));
        comb = softmax(score);
      }
      for (i = 0; i < n; i++) kinds.push({ key: labels[i], p: comb[i], head: p[i], list: speaks(i) ? (q[labels[i]] || 0) : null });
      kinds.sort(function (a, b) { return b.p - a.p; });
      var kind = kinds[0].key, named = null, offers = [];
      if (species.length && kind !== 'none' && kind !== 'person') {
        if (species[0].p >= f.name_at && species[0].kind === kind) named = species[0];
        else {
          // the three likeliest are kept as offers. They are taken from the kind that won, so that a flower is not offered a turtle;
          // a manifest that sets fusion.offer_any_kind takes the three likeliest of any kind.
          var three = (f.offer_any_kind ? order : order.filter(function (j) { return table[j].kind === kind; })).slice(0, 3).map(function (j) { return { sci: table[j].sci, en: table[j].en, p: s[j], kind: table[j].kind }; });
          if (three.reduce(function (a, r) { return a + r.p; }, 0) >= f.offer_at) offers = three;
        }
      }
      return { kind: kind, kindP: kinds[0].p, kinds: kinds, species: species, named: named, offers: offers };
    }
    // The photo's pixels for the encoder. The canvas the page shows was brought down to 1280 by the browser's own scaling, which differs
    // from one browser to the next; so a photo chosen as a file is read again at its full size where a canvas can hold it (16 million
    // pixels is the smallest limit among phones), and the one resize that follows is Pillow's. A camera frame is used as it is.
    function pixels(canvas, file) {
      function shown() { var d = canvas.getContext('2d').getImageData(0, 0, canvas.width, canvas.height); return { buf: d.data.buffer, w: d.width, h: d.height, full: false }; }
      if (!file || typeof createImageBitmap !== 'function') return Promise.resolve().then(shown);
      return createImageBitmap(file).then(function (bmp) {
        var w = bmp.width, h = bmp.height, c, x, d;
        if (Math.max(w, h) <= Math.max(canvas.width, canvas.height) || w * h > 16e6) { if (bmp.close) bmp.close(); return shown(); }
        c = document.createElement('canvas'); c.width = w; c.height = h; x = c.getContext('2d', { willReadFrequently: true });
        x.drawImage(bmp, 0, 0); if (bmp.close) bmp.close();
        d = x.getImageData(0, 0, w, h); c.width = c.height = 1;
        return { buf: d.data.buffer, w: w, h: h, full: true };
      }).catch(shown);
    }
    function recognize(canvas, file) {
      var tAsk = performance.now(), wasReady = state === 'ready', shot = pixels(canvas, file);   // read now: the canvas may show something else by the time the encoder is ready
      shot.catch(function () {});
      return ready().then(function () { return shot.catch(function (e) { throw err('photo', e && e.message); }); }).then(function (px) {
        var tRun = performance.now();
        return new Promise(function (res, rej) {
          var id = nextId++;
          pending[id] = { res: res, rej: rej, timer: setTimeout(function () { if (pending[id]) stop('slow', 'no answer in ' + watchMs + ' ms'); }, watchMs) };
          worker.postMessage({ op: 'run', id: id, rgba: px.buf, w: px.w, h: px.h, wantPre: !!pocket.wantPre }, [px.buf]);
        }).then(function (m) {
          var t = performance.now(), month = new Date().getMonth(), local = pocket.local !== false && !!cur.table, r = fuseWith(cur, m.kinds, local ? m.species : null, month);
          r.month = month; r.local = local;                // local: the species list of this slot's region was consulted
          r.ms = { load: wasReady ? 0 : Math.round(tRun - tAsk), pre: Math.round(m.ms.pre), run: Math.round(m.ms.run), post: Math.round((m.ms.post + performance.now() - t) * 10) / 10 };
          r.backend = info.backend; r.model = M.id; r.at = Date.now(); r.from = px.w + 'x' + px.h;
          last = r; if (pocket.wantPre) { pocket.lastEmb = m.emb; pocket.lastPre = m.pre; pocket.lastDots = { kinds: m.kinds, species: m.species }; }
          return r;
        });
      });
    }
    function mb(n) { return Math.max(0, Math.round(n / 1e6)); }
    function line() {
      if (state === 'loading' && total > got) return 'Getting the recognizer: ' + mb(got) + ' of ' + Math.max(1, mb(total)) + ' MB.';
      return 'Looking at what it is.';
    }
    function warm() {                                  // once the opening screen is up and the page has nothing else to do
      if (cannot || (navigator.connection && navigator.connection.saveData)) return;
      function go() { if (state === 'idle') ready().catch(function () {}); }
      function soon() { if (window.requestIdleCallback) requestIdleCallback(go, { timeout: 4000 }); else setTimeout(go, 1200); }
      if (document.readyState === 'complete') soon(); else window.addEventListener('load', soon);
    }
    return {
      usable: function () { return !cannot; }, whyNot: function () { return SAY[cannot] || ''; },
      recognize: recognize, line: line, warm: warm, ready: ready, fuse: function (kd, sd, month) { return fuseWith(cur, kd, sd, month); },
      fetching: function () { return state === 'loading' && total > got; },      // the first download is under way
      region: function () { return cur && cur.table ? String((M.species && M.species.place) || '') : ''; },
      progress: function (fn) { onProgress = fn; },
      offers: [], file: null, local: true, wantPre: false, lastEmb: null, lastPre: null, lastDots: null,
      about: function () { return { state: state, why: why, fail: lastFail, model: M ? M.id : '', rule: M ? (M.fusion.rule || 'product') : '', trained: !!(cur && (cur.kb || cur.sb)), backend: info.backend, threads: info.threads, loadMs: Math.round(loadMs), start: info.ms || null, last: last, got: got, total: total, slot: manifestUrl }; },
      test: { kill: function (how) { if (worker) worker.postMessage({ op: 'die', how: how }); }, watch: function (ms) { watchMs = ms; }, forget: function () { stop('died', 'forgotten by a check'); state = 'idle'; why = ''; },
        // the scoring with settings given by a check, through the same readers as a real slot (tools/fusion/parity.py)
        world: function (m, rows, sb) { worlds.push(slotOf(readManifest(JSON.stringify(m)), rows ? readTable(new TextEncoder().encode(JSON.stringify({ species: rows })).buffer, rows.length) : null, sb ? Float64Array.from(sb) : null)); return worlds.length - 1; },
        fuseIn: function (w, kd, sd, month) { return fuseWith(worlds[w], kd, sd, month); } }
    };
  })();
