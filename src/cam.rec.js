
  // ---------- recognition in the page itself: the pocket recognizer, and the full database the person may fetch once
  // Outside Claude's viewer the page names the photo by itself: an image encoder run by ONNX Runtime Web in a worker
  // (vendor/rec-worker.js), and label vectors worked out beforehand. The files are described by models/<slot>/manifest.json
  // (docs/CONTRACTS.md). Nothing here is fetched before the opening screen is up, and nothing about a photo leaves the device.
  // Kept copies: every file is asked for with ?v=<version> and kept under that address, so a new version is a new address.
  // The runtime's version is its release number; a slot's version is a fingerprint of its manifest, which is always asked of the network first.
  // From build 9 the encoder is the exception where the manifest gives its checksum: it is asked for with ?v=sha256-<checksum>, so that
  // new heads or new settings (a new manifest) do not cost a second download of an encoder whose bytes have not changed.
  // There are two slots. The pocket one (models/pocket) is fetched by the page itself once the opening screen is up. The larger one
  // (models/naturalist) is some hundreds of megabytes, in parts that may live on another origin: nothing of it is fetched until the
  // person has said so, its parts are kept one by one so that a download carries on where it stopped, and its worker is started only
  // when a photo needs it and let go after a minute with nothing to do.
  var ORT = { v: '1.30.0', dir: 'vendor/ort/', js: 'ort.wasm.min.js', mjs: 'ort-wasm-simd-threaded.mjs', wasm: 'ort-wasm-simd-threaded.wasm', wasmBytes: 14239897, ep: 'wasm' };
  var KIND_ORDER = ['cat', 'dog', 'squirrel', 'deer', 'rabbit', 'hawk', 'wader', 'bird', 'alligator', 'reptile', 'frog', 'bee', 'insect', 'plant', 'other', 'person',
    'fungus', 'slime', 'spider', 'jumper', 'fish', 'shark', 'snail', 'sealife', 'crab', 'salamander', 'worm', 'scorpion', 'tick', 'mammal', 'primate', 'whale', 'bat', 'flyingfox', 'cephalopod'];   // the order of KINDS in tools/fusion/fuse.py; the groups with no view yet (GROUPS) follow
  function known(k) { return !!(EYES[k] || GROUPS[k]); }   // a kind with a view, or a group the page names and cannot yet view the world as
  var onThisMachine = /^(localhost|127\.0\.0\.1)$/.test(location.hostname);
  function plain(x) { return String(x || '').toLowerCase().replace(/[^a-z' -]+/g, ' ').replace(/\s+/g, ' ').trim(); }
  function slips(a, b, lim) {                          // how many slips of the keys turn one word into the other: a letter wrong, missing, added, or two swapped
    var n = a.length, m = b.length, i, j, p2 = null, p = [], c, low;
    for (j = 0; j <= m; j++) p[j] = j;
    for (i = 1; i <= n; i++) {
      c = [i]; low = i;
      for (j = 1; j <= m; j++) {
        c[j] = Math.min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (a.charCodeAt(i - 1) === b.charCodeAt(j - 1) ? 0 : 1));
        if (p2 && i > 1 && j > 1 && a.charCodeAt(i - 1) === b.charCodeAt(j - 2) && a.charCodeAt(i - 2) === b.charCodeAt(j - 1)) c[j] = Math.min(c[j], p2[j - 2] + 1);
        if (c[j] < low) low = c[j];
      }
      if (low > lim) return lim + 1;
      p2 = p; p = c;
    }
    return p[m];
  }
  function recognizer(o) {                             // o.slot: where the manifest is, or 'off'; o.big: the full database
    var big = !!o.big, slot = o.slot;
    var manifestUrl = /\.json$/.test(slot) ? slot : slot.replace(/\/$/, '') + '/manifest.json';
    var cannot = inViewer ? 'off' : slot === 'off' || /\.\.|^\/|\/\//.test(slot) ? 'off'
      : (typeof Worker !== 'function' || typeof WebAssembly !== 'object' || typeof fetch !== 'function' || typeof Float32Array !== 'function') ? 'browser'
      : (big && !window.caches) ? 'browser' : '';      // the full database has to be kept, and this browser keeps nothing
    var SAY = {
      off: 'IDing is turned off.',
      absent: 'This app can’t ID photos yet.',
      missing: 'Some of this app’s files are missing. Close the app and open it again.',
      network: 'This app’s download is incomplete. Check your connection, then close the app and open it again.',
      damaged: 'This app’s download is damaged. Close the app and open it again.',
      unfit: 'This app’s files are out of date. Close the app and open it again to update.',
      browser: 'This browser is too old to ID photos. Try a current Chrome, Safari, or other browser.',
      died: 'This app’s IDing has crashed. Check that your device has enough memory.',
      slow: 'The IDing timed out. Try again.',
      photo: 'That photo couldn’t be read. Try again.'
    };
    if (big) {
      SAY.off = 'The full database is switched off.'; SAY.absent = 'This app has no full database yet.'; SAY.missing = 'The full database\u2019s files are missing.';
      SAY.network = 'The full database’s download was interrupted.'; SAY.damaged = 'The full database\u2019s download is damaged.'; SAY.unfit = 'The full database does not fit this build of the app. Download the latest version of the app.';
      SAY.browser = 'This browser cannot run the full database.'; SAY.died = 'The full database crashed. Check that your device has enough memory.'; SAY.slow = 'The full database timed out. Try again.'; SAY.photo = 'The full database failed on that photo. Try a different photo. Try a different photo.';
      SAY.room = 'There is not enough storage on this device for the full database.';
      SAY.keep = 'The full database could not be kept on this device.';
      SAY.stopped = 'The download has been stopped.';
    }
    var KEEP = 'keep-v1', EPS = 1e-9;
    var state = cannot ? 'failed' : 'idle', why = cannot, M = null, ver = '', base = '', cur = null, worlds = [], worker = null, loadP = null, loadMs = 0, info = { backend: '', threads: 0 };
    var got = 0, total = 0, pending = {}, nextId = 1, last = null, lastFail = '', onProgress = null, watchMs = big ? 120000 : 45000, netWaitMs = 6000, api;
    // the full database only: what of it is kept, the download under way, and the rest it takes after a minute with nothing to do
    var have = '', gone = false, keptBytes = 0, partGot = 0, getP = null, getCtl = null, getFail = '', surveyP = null, idleMs = 60000, idleTimer = 0, queue = Promise.resolve(), asked = 0;

    function err(code, detail) { var e = new Error(SAY[code] || code); e.code = code; e.sentence = SAY[code] || SAY.died; e.detail = String(detail || ''); return e; }
    function abs(u, b) { try { return new URL(u, b || location.href).href; } catch (e) { return u; } }
    function withV(u, v) { return u + (u.indexOf('?') < 0 ? '?' : '&') + 'v=' + encodeURIComponent(v); }
    function fingerprint(text) {                       // two rounds of FNV-1a: enough to tell one manifest from the next
      var a = 0x811c9dc5, b = 0x01000193 ^ text.length, i, c;
      for (i = 0; i < text.length; i++) { c = text.charCodeAt(i); a = Math.imul(a ^ c, 0x01000193); b = Math.imul(b ^ (c + i), 0x85ebca6b); }
      return ('0000000' + (a >>> 0).toString(16)).slice(-8) + ('0000000' + (b >>> 0).toString(16)).slice(-8);
    }
    function keepOpen() { try { return window.caches ? caches.open(KEEP).catch(function () { return null; }) : Promise.resolve(null); } catch (e) { return Promise.resolve(null); } }
    // A kept copy, looked for in every way there is. Nothing here differs by what a request's headers say, so a copy kept with a Vary header
    // (GitHub Pages sends "Vary: Accept-Encoding") is matched whatever the asking request carries; and where this page's own store
    // will not open or will not answer, every store of this site is asked, the service worker's among them.
    function kept(cache, url) {
      function one(c) { try { return c.match(url, { ignoreVary: true }).then(function (hit) { return hit || null; }, function () { return null; }); } catch (e) { return Promise.resolve(null); } }
      return (cache ? one(cache) : Promise.resolve(null)).then(function (hit) { return hit || (window.caches ? one(caches) : null); });
    }
    function unkeep(url) {                             // out of every store of this site
      if (!window.caches) return Promise.resolve();
      return caches.keys().then(function (names) {
        return Promise.all(names.map(function (n) { return caches.open(n).then(function (c) { return c.delete(url, { ignoreVary: true }); }); }));
      }).catch(function () {});
    }
    function notify() { if (onProgress) onProgress(); }
    function tick(n) { got += n; notify(); }
    function readAll(res, expect, count) {             // the whole body, counted as it arrives
      if (!res.body || !res.body.getReader) return res.arrayBuffer().then(function (b) { count(b.byteLength); return b; });
      var reader = res.body.getReader(), buf = expect ? new Uint8Array(expect) : null, chunks = [], n = 0;
      function pump() {
        return reader.read().then(function (r) {
          if (r.done) return;
          var c = r.value;
          if (buf && n + c.length <= buf.length) buf.set(c, n); else { if (buf) { chunks.push(buf.slice(0, n)); buf = null; } chunks.push(c); }
          n += c.length; count(c.length); return pump();
        });
      }
      return pump().then(function () {
        if (buf) return n === buf.length ? buf.buffer : buf.slice(0, n).buffer;
        var out = new Uint8Array(n), o = 0; chunks.forEach(function (c) { out.set(c, o); o += c.length; }); return out.buffer;
      });
    }
    // One file: the kept copy if there is one, otherwise the network, counted toward the progress line.
    function file(cache, url, expect, check, fresh) {
      function again() { return unkeep(url).then(function () { return file(cache, url, expect, check, true); }); }
      return (fresh ? Promise.resolve(null) : kept(cache, url)).then(function (res) {
        if (res) return res.arrayBuffer().then(function (b) {
          if (expect && b.byteLength !== expect) return again();        // a kept copy cut short is thrown away
          return b;
        }, again);                                                     // and so is one that cannot be read
        total += expect || 0; notify();
        return fetch(url).then(function (r) {
          if (!r.ok) throw err(r.status === 404 ? 'missing' : 'network', url + ' ' + r.status);
          if (!expect) { var len = +r.headers.get('content-length') || 0; total += len; }
          return readAll(r, expect, tick).catch(function (e) { throw e && e.code ? e : err('network', url); }).then(function (b) {
            if (expect && b.byteLength !== expect) throw err('damaged', url + ' is ' + b.byteLength + ' bytes, not ' + expect);
            return (check ? check(b) : Promise.resolve()).then(function () {
              if (!cache) return b;
              // kept by the page itself, unless the service worker has kept the same bytes under the same address already
              return kept(cache, url).then(function (there) {
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
    function okPart(u) {                               // a part may live on another origin, over https; a check on this machine may use its own ports
      return typeof u === 'string' && !!u && (/^https:\/\/[^\/]+\//.test(u) || (!/^[a-z][a-z0-9+.-]*:/i.test(u) && !/^\/\//.test(u)) || (onThisMachine && /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?\//.test(u)));
    }
    function partsOf(V) { return Array.isArray(V.parts) ? V.parts : [{ url: V.url, bytes: V.bytes, sha256: V.sha256 }]; }
    function readManifest(text) {
      var m; try { m = JSON.parse(text); } catch (e) { throw err('damaged', 'manifest is not JSON'); }
      var v = m && m.vision, f = m && m.fusion, k = m && m.kinds, sp = m && m.species;
      if (!v || !f || !num(m.width) || !num(v.size) || !Array.isArray(v.mean) || !Array.isArray(v.std) || !(v.url || Array.isArray(v.parts))) throw err('unfit', 'manifest lacks a field');
      // a slot may come without a kinds head: then the kind is taken from the species answer, and the species are not optional
      if (k ? !(Array.isArray(k.labels) && k.url && num(f.t_kind)) : !sp) throw err('unfit', 'manifest lacks a field');
      if (k && k.labels.some(function (l) { return l !== 'none' && !known(l); })) throw err('unfit', 'a kind this page does not know');
      if (sp && !(sp.url && sp.table && num(sp.count) && num(f.t_species) && num(f.alpha_prior) && (!k || num(f.w_kind)) && num(f.name_at) && num(f.offer_at))) throw err('unfit', 'species without their settings');
      // a trained head carries a bias for each row; a manifest may choose how the two heads are combined. Anything this build does not know is refused, not guessed at.
      if (k && k.bias !== undefined && k.bias !== null && !(Array.isArray(k.bias) && k.bias.length === k.labels.length && k.bias.every(num))) throw err('unfit', 'kinds.bias does not match the labels');
      if (f.rule !== undefined && f.rule !== 'product' && f.rule !== 'mix') throw err('unfit', 'a combination rule this page does not know');
      if (f.guard !== undefined && !(num(f.guard) && f.guard > 0)) throw err('unfit', 'fusion.guard is not a positive number');
      if (f.kind_at !== undefined && f.kind_at !== null && !num(f.kind_at)) throw err('unfit', 'fusion.kind_at is not a number');
      // a model in parts: every part with its length, the lengths adding up to the whole
      if (v.parts !== undefined) {
        var sum = 0;
        if (!Array.isArray(v.parts) || !v.parts.length || !num(v.bytes) || !v.parts.every(function (p) { sum += p && p.bytes; return p && okPart(p.url) && num(p.bytes) && p.bytes > 0 && (p.sha256 === undefined || typeof p.sha256 === 'string'); }) || sum !== v.bytes) throw err('unfit', 'the parts do not add up to the whole');
      }
      if (big ? !(num(v.bytes) && v.bytes > 0 && partsOf(v).every(function (p) { return okPart(p.url); })) : v.parts !== undefined) throw err('unfit', big ? 'the full database without its length' : 'a model in parts in the pocket slot');
      return m;
    }
    function readTable(buf, count) {                   // rows: [scientific, English, kind, twelve monthly weights], or the same as objects
      var t, rows; try { t = JSON.parse(new TextDecoder('utf-8').decode(buf)); } catch (e) { throw err('damaged', 'species table is not JSON'); }
      rows = Array.isArray(t) ? t : t && t.species;
      if (!Array.isArray(rows) || rows.length !== count) throw err('unfit', 'species table has ' + (rows ? rows.length : 0) + ' rows, not ' + count);
      return rows.map(function (r) {
        var a = Array.isArray(r) ? r : [r.sci, r.en, r.kind || r.eyes, r.m], kind = known(a[2]) ? a[2] : 'other', m = Array.isArray(a[3]) && a[3].length === 12 ? a[3] : null;
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
      var has = {}, uniq = [], rowAt = [];
      if (rows) rows.forEach(function (r) { has[r.kind] = 1; });
      if (sb && (!rows || sb.length !== rows.length)) throw err('unfit', 'species biases do not match the table');
      if (!m.kinds && !rows) throw err('unfit', 'neither kinds nor species');
      // rows of the kinds head that share a label are one kind, in the place of the label's first row (a group head keeps the row
      // of a group it cannot yet name well and labels it `other`); their probabilities are added in fuseWith, as in tools/fusion/fuse.py
      if (m.kinds) m.kinds.labels.forEach(function (l) { var j = uniq.indexOf(l); if (j < 0) { j = uniq.length; uniq.push(l); } rowAt.push(j); });
      // without a kinds head the labels are the kinds the table has, in the one fixed order
      return { f: m.fusion, head: !!m.kinds, labels: m.kinds ? uniq : KIND_ORDER.filter(function (k) { return has[k]; }), rowAt: m.kinds ? rowAt : null, table: rows, has: has,
        kb: m.kinds && m.kinds.bias ? Float64Array.from(m.kinds.bias) : null, sb: sb || null, prior: {} };
    }
    function encV(V) { return V && !V.parts && typeof V.sha256 === 'string' && /^[0-9a-f]{64}$/i.test(V.sha256) ? 'sha256-' + V.sha256.toLowerCase() : ''; }   // the encoder's own version, where its checksum is given
    function prune(cache, v) {                         // older versions of this slot and of the runtime are let go; the encoder in use stays under its checksum
      if (!cache) return;
      var ev = M ? encV(M.vision) : '';
      cache.keys().then(function (keys) {
        keys.forEach(function (req) {
          var u; try { u = new URL(req.url); } catch (e) { return; }
          var q = /[?&]v=([^&]+)/.exec(u.search), here = u.href.split('?')[0];
          if (!q) return;
          if (here.indexOf(base) === 0 && here.slice(base.length).indexOf('/') < 0 && decodeURIComponent(q[1]) !== v && !(ev && decodeURIComponent(q[1]) === ev && here === abs(M.vision.url, base))) cache.delete(req);
          if (here.indexOf(abs(ORT.dir)) === 0 && decodeURIComponent(q[1]) !== ORT.v) cache.delete(req);
        });
      }).catch(function () {});
    }
    function stop(code, detail) {                      // the worker is gone or cannot be trusted: everything waiting hears of it
      var w = worker, p = pending; worker = null; pending = {};
      if (w) { w.onmessage = w.onerror = null; try { w.terminate(); } catch (e) {} }
      state = 'failed'; why = code; lastFail = code + (detail ? ': ' + detail : ''); loadP = null;
      Object.keys(p).forEach(function (id) { clearTimeout(p[id].timer); p[id].rej(err(code, detail)); });
    }
    function startWorker(init, transfer, sessionCode) {
      return new Promise(function (res, rej) {
        var w, hello = false, settled = false, timer;
        function no(code, detail) { if (settled) { stop(code, detail); return; } settled = true; clearTimeout(timer); stop(code, detail); rej(err(code, detail)); }
        try { w = new Worker('vendor/rec-worker.js?v=' + BUILD); } catch (e) { rej(err('browser', e && e.message)); return; }
        worker = w;
        timer = setTimeout(function () { no('slow', 'starting'); }, Math.max(watchMs, 60000) * (big ? 2 : 1));
        w.onerror = function (e) { if (e && e.preventDefault) e.preventDefault(); no(hello ? (big && !settled ? 'browser' : 'died') : 'network', e && e.message); };
        w.onmessage = function (ev) {
          var m = ev.data || {}, p;
          if (m.op === 'hello') { hello = true; return; }
          if (m.op === 'ready') { settled = true; clearTimeout(timer); info = { backend: m.backend, threads: m.threads, ms: m.ms }; res(); return; }
          if (m.op === 'fail' && !m.id) { no(m.stage === 'runtime' ? 'network' : m.stage === 'browser' ? 'browser' : m.stage === 'unfit' ? 'unfit' : m.stage === 'session' ? sessionCode : 'died', m.stage + ' ' + m.name + ' ' + m.message); return; }
          p = pending[m.id]; if (!p) return;
          delete pending[m.id]; clearTimeout(p.timer);
          if (m.op === 'done') p.res(m); else p.rej(err('photo', m.message));
        };
        w.postMessage(init, transfer);
      });
    }
    // The manifest: the network first, so that a new model is noticed; the kept copy where there is no network, where the server is
    // having a bad moment, where the answer breaks off, or where none comes in six seconds. The kept copy is the last resort, so it is
    // looked for more than once before the load is given up, and what was missing is written into the reason.
    function keptText(cache, url, detail) {
      var tries = 0;
      function look() {
        return (cache ? Promise.resolve(cache) : keepOpen()).then(function (c) { return kept(c, url); }).then(function (hit) { return hit ? hit.text() : null; }, function () { return null; }).then(function (text) {
          if (text) return text;
          if (++tries < 3) return new Promise(function (res) { setTimeout(res, 150 * tries); }).then(look);
          throw err('network', detail + (window.caches ? '; no kept copy found' : '; this browser keeps no copies'));
        });
      }
      return look();
    }
    function manifestText(cache) {
      var url = abs(manifestUrl), ctl = typeof AbortController === 'function' ? new AbortController() : null, late = false;
      var timer = ctl ? setTimeout(function () { kept(cache, url).then(function (hit) { if (hit) { late = true; try { ctl.abort(); } catch (e) {} } }); }, netWaitMs) : 0;
      return fetch(manifestUrl, { cache: 'no-cache', signal: ctl ? ctl.signal : undefined }).then(function (r) {
        clearTimeout(timer);
        if (r.status === 404) throw err('absent', manifestUrl);            // taken away on purpose, or never there
        if (!r.ok) return keptText(cache, url, manifestUrl + ' ' + r.status);           // a server having a bad moment
        return r.text().then(function (text) {
          if (cache) cache.put(url, new Response(text, { headers: { 'Content-Type': 'application/json' } })).catch(function () {});
          return text;
        }, function () { return keptText(cache, url, manifestUrl + ' broke off'); });
      }, function () { clearTimeout(timer); return keptText(cache, url, manifestUrl + (late ? ' did not answer in time' : '')); });
    }
    function adopt(text) { M = readManifest(text); ver = fingerprint(text); base = abs(manifestUrl).replace(/[^\/]*$/, ''); cur = null; }
    function u(rel) { return withV(abs(rel, base), ver); }

    // ---------- a model in parts (the full database)
    // A part is kept under an address of this slot made from its checksum, so the same bytes are never fetched twice, wherever they came from.
    function partKey(p) { return base + 'part/' + (p.sha256 ? String(p.sha256).toLowerCase() : fingerprint(String(p.url))) + '?bytes=' + p.bytes; }
    function wholeKey(V) { return base + 'whole/' + String(V.sha256 || '').toLowerCase(); }
    function unkeepParts() {
      var V = M.vision; have = 'absent'; keptBytes = 0;
      return Promise.all(partsOf(V).map(function (p) { return unkeep(partKey(p)); }).concat([unkeep(wholeKey(V))]));
    }
    function staleParts(cache) {                       // parts of a model this slot no longer names
      if (!cache || !M) return;
      var now = {}; partsOf(M.vision).forEach(function (p) { now[partKey(p).split('?')[0]] = 1; }); now[wholeKey(M.vision)] = 1;
      cache.keys().then(function (keys) {
        keys.forEach(function (req) { var here = req.url.split('?')[0]; if ((here.indexOf(base + 'part/') === 0 || here.indexOf(base + 'whole/') === 0) && !now[here]) cache.delete(req); });
      }).catch(function () {});
    }
    function readInto(res, buf, at, n) {               // a kept part, straight into its place in the whole
      function wrong(len) { return err('damaged', 'a kept part is ' + len + ' bytes, not ' + n); }
      if (!res.body || !res.body.getReader) return res.arrayBuffer().then(function (b) { if (b.byteLength !== n) throw wrong(b.byteLength); buf.set(new Uint8Array(b), at); });
      var reader = res.body.getReader(), done = 0;
      function pump() {
        return reader.read().then(function (r) {
          if (r.done) { if (done !== n) throw wrong(done); return; }
          if (done + r.value.length > n) throw wrong(done + r.value.length);
          buf.set(r.value, at + done); done += r.value.length; return pump();
        });
      }
      return pump();
    }
    function joined(cache, V) {                        // the parts as they are kept, put together; the whole is verified the first time
      var buf, off = 0, i = 0, P = partsOf(V);
      try { buf = new Uint8Array(V.bytes); } catch (e) { return Promise.reject(err('browser', 'no room in memory for ' + V.bytes + ' bytes')); }
      function next() {
        if (i >= P.length) return Promise.resolve();
        var p = P[i++], at = off; off += p.bytes;
        return kept(cache, partKey(p)).then(function (res) {
          if (!res) { have = ''; throw err('missing', 'a part is no longer kept on this device'); }
          return readInto(res, buf, at, p.bytes).catch(function (e) { have = ''; return unkeep(partKey(p)).then(function () { throw e && e.code ? e : err('damaged', 'a kept part could not be read'); }); });
        }).then(next);
      }
      return next().then(function () {
        if (!V.sha256) return;
        return kept(cache, wholeKey(V)).then(function (ok) {
          if (ok) return;
          return sha256(V.sha256)(buf.buffer).then(function () { if (cache) return cache.put(wholeKey(V), new Response('verified')).catch(function () {}); },
            function (e) { return unkeepParts().then(function () { throw e; }); });      // every part passed and the whole does not: nothing of it can be trusted
        });
      }).then(function () { return buf.buffer; });
    }
    function room(need) {                              // is there room to keep it? Where the browser will not say, the download finds out
      try {
        if (navigator.storage && navigator.storage.estimate) return navigator.storage.estimate().then(function (e) {
          if (e && num(e.quota) && num(e.usage) && e.quota - e.usage < need) throw err('room', 'room for ' + Math.max(0, e.quota - e.usage) + ' bytes, and ' + need + ' are needed');
        }, function () {});
      } catch (e) {}
      return Promise.resolve();
    }
    // What of the full database is on this device: 'none' (there is no such model, or it cannot be used here), 'absent', 'partial', 'getting', 'kept'.
    // The manifest is asked for the first time this is called, and never before.
    function survey(fresh) {
      if (cannot || gone) return Promise.resolve('none');
      if (!fresh && getP) return Promise.resolve('getting');
      if (!fresh && have) return Promise.resolve(have);
      if (!surveyP) surveyP = keepOpen().then(function (cache) {
        return (M ? Promise.resolve() : manifestText(cache).then(adopt)).then(function () {
          var P = partsOf(M.vision);
          return Promise.all(P.map(function (p) { return kept(cache, partKey(p)); })).then(function (hits) {
            var n = 0; keptBytes = 0; hits.forEach(function (h, i) { if (h) { keptBytes += P[i].bytes; n++; } });
            have = n === P.length ? 'kept' : n ? 'partial' : 'absent';
            if (have !== 'kept') staleParts(cache);
            return have;
          });
        });
      }).then(function (h) { surveyP = null; return h; }, function (e) {
        surveyP = null;
        if (e && e.code === 'absent') gone = true; else lastFail = ((e && e.code) || 'died') + (e && e.detail ? ': ' + e.detail : '');
        return 'none';
      });
      return surveyP.then(function (h) { return h !== 'none' && getP ? 'getting' : h; });
    }
    // Fetch what is missing, one part after another, each verified and kept before the next is asked for; then start the encoder once, which
    // verifies the whole and shows that it runs on this device. Stopped by halt(); a later call carries on from the parts already kept.
    function get() {
      if (cannot) return Promise.reject(err(cannot));
      if (getP) return getP;
      var ctl = typeof AbortController === 'function' ? new AbortController() : null, store = null;
      function halted() { return !!(ctl && ctl.signal.aborted); }
      getCtl = ctl; getFail = ''; partGot = 0;
      var p = survey(true).then(function (h) {
        if (h === 'none') throw err(gone ? 'absent' : 'network', manifestUrl);
        return keepOpen();
      }).then(function (cache) {
        if (!cache) throw err('keep', 'this browser gave no store to keep it in');
        store = cache;
        var P = partsOf(M.vision), i = 0;
        function next() {
          if (i >= P.length) return Promise.resolve();
          var part = P[i++], key = partKey(part);
          return kept(cache, key).then(function (hit) {
            if (hit) return;                           // already here: not fetched again
            if (halted()) throw err('stopped');
            partGot = 0; notify();
            return fetch(abs(part.url, base), { mode: 'cors', credentials: 'omit', cache: 'no-store', referrerPolicy: 'no-referrer', signal: ctl ? ctl.signal : undefined }).then(function (r) {
              if (!r.ok) throw err(r.status === 404 ? 'missing' : 'network', part.url + ' ' + r.status);
              return readAll(r, part.bytes, function (n) { partGot += n; notify(); });
            }).then(function (b) {
              if (b.byteLength !== part.bytes) throw err('damaged', part.url + ' is ' + b.byteLength + ' bytes, not ' + part.bytes);
              return sha256(part.sha256)(b).then(function () {
                return cache.put(key, new Response(b, { headers: { 'Content-Type': 'application/octet-stream', 'Content-Length': String(b.byteLength) } })).catch(function (e) {
                  throw err(e && e.name === 'QuotaExceededError' ? 'room' : 'keep', e && e.message);
                });
              });
            }).then(function () { keptBytes += part.bytes; partGot = 0; notify(); }, function (e) {
              partGot = 0;
              throw halted() ? err('stopped') : e && e.code ? e : err('network', part.url + ' ' + ((e && e.message) || ''));
            });
          }).then(next);
        }
        return room(Math.max(0, M.vision.bytes - keptBytes)).then(next);
      }).then(function () {
        have = 'kept'; staleParts(store); notify();
        return ready();
      }).then(function () { getP = null; getCtl = null; diag('large-kept', M.id + ' ' + M.vision.bytes); notify(); }, function (e) {
        getP = null; getCtl = null;
        if (!e || !e.code) e = err('died', e && e.message);
        if (have !== 'kept') have = keptBytes ? 'partial' : 'absent';
        getFail = e.code + (e.detail ? ': ' + e.detail : ''); diag('large-get', getFail.slice(0, 160)); notify();
        throw e;
      });
      getP = p; p.catch(function () {});
      return p;
    }
    function halt() { if (getCtl) try { getCtl.abort(); } catch (e) {} }
    function rest() {                                  // nothing has needed the full database for a minute: its worker, and the memory it holds, are let go
      clearTimeout(idleTimer); idleTimer = 0;
      if (!worker || state !== 'ready' || Object.keys(pending).length) return;
      var w = worker; worker = null; w.onmessage = w.onerror = null; try { w.terminate(); } catch (e) {}
      state = 'idle'; loadP = null; diag('large-rest', '');
    }
    function tire() { if (!big) return; clearTimeout(idleTimer); idleTimer = setTimeout(rest, idleMs); }
    function forget() {                                // off this device: the parts, the rows and the table, and the worker
      halt();
      return (getP ? getP.catch(function () {}) : Promise.resolve()).then(function () {
        var w = worker, p = pending; worker = null; pending = {}; clearTimeout(idleTimer);
        if (w) { w.onmessage = w.onerror = null; try { w.terminate(); } catch (e) {} }
        Object.keys(p).forEach(function (id) { clearTimeout(p[id].timer); p[id].rej(err('died', 'deleted')); });
        state = cannot ? 'failed' : 'idle'; why = cannot; loadP = null;
        return keepOpen();
      }).then(function (cache) {
        if (!cache || !base) return;
        return cache.keys().then(function (keys) { return Promise.all(keys.map(function (req) { return req.url.split('?')[0].indexOf(base) === 0 ? cache.delete(req) : null; })); });
      }).catch(function () {}).then(function () { have = M ? 'absent' : ''; keptBytes = 0; partGot = 0; getFail = ''; diag('large-deleted', ''); notify(); });
    }

    function load() {
      var t0 = performance.now(), cacheRef = null, fromKeep = { model: false };
      state = 'loading'; why = ''; got = 0; total = 0;
      return keepOpen().then(function (cache) {
        cacheRef = cache;
        if (big && M) return null;                     // the full database's worker is started again and again; its manifest is read once
        return manifestText(cache).then(adopt);
      }).then(function () {
        var V = M.vision, nK = M.kinds ? M.kinds.labels.length : 0, nS = M.species ? M.species.count : 0, c = cacheRef;
        var inParts = big || !!V.parts, modelUrl = inParts ? '' : encV(V) ? withV(abs(V.url, base), encV(V)) : u(V.url);
        return (inParts ? Promise.resolve(true) : kept(c, modelUrl)).then(function (hit) {
          fromKeep.model = !!hit;
          return Promise.all([
            file(c, withV(abs(ORT.dir + ORT.wasm), ORT.v), ORT.wasmBytes),
            inParts ? joined(c, V) : file(c, modelUrl, num(V.bytes) ? V.bytes : 0, sha256(V.sha256)),
            M.kinds ? file(c, u(M.kinds.url), nK * M.width * 2) : null,
            M.species ? file(c, u(M.species.url), nS * M.width * 2) : null,
            M.species ? file(c, u(M.species.table), 0) : null,
            M.species && M.species.bias_url ? file(c, u(M.species.bias_url), nS * 4) : null
          ]);
        }).then(function (b) {
          cur = slotOf(M, M.species ? readTable(b[4], nS) : null, b[5] ? floats(b[5], nS) : null);
          total = got;                                 // the downloads are over; what remains is starting the encoder
          notify();
          var init = { op: 'init', ep: ORT.ep, ort: { js: withV(abs(ORT.dir + ORT.js), ORT.v), mjs: withV(abs(ORT.dir + ORT.mjs), ORT.v), wasm: withV(abs(ORT.dir + ORT.wasm), ORT.v) },
            wasmBinary: b[0], model: b[1], vision: { input: V.input || 'pixel_values', output: V.output || 'image_embeds', size: V.size, mean: V.mean, std: V.std, resize: V.resize, crop: V.crop || 'center' },
            width: M.width, kinds: b[2], nKinds: nK, species: b[3], nSpecies: nS };
          // a model in parts has passed its checksums by now: if the encoder will not take it, the fault is not in the bytes, and they are kept
          return startWorker(init, [b[0], b[1]].concat(b[2] ? [b[2]] : [], b[3] ? [b[3]] : []), inParts && V.sha256 ? 'browser' : 'damaged').catch(function (e) {
            // a kept model that will not start is thrown away, so the next try fetches it afresh
            if (e.code === 'damaged' && c) return (inParts ? unkeepParts() : unkeep(modelUrl)).then(function () { throw e; });
            throw e;
          });
        });
      }).then(function () {
        state = 'ready'; loadMs = performance.now() - t0; if (!big) prune(cacheRef, ver);
        tire();
        diag(big ? 'large-ready' : 'pocket-ready', M.id + ' ' + Math.round(loadMs) + 'ms ' + (fromKeep.model ? 'kept' : 'fetched'));
      }, function (e) {
        if (!e || !e.code) e = err('died', e && e.message);
        if (state !== 'failed' || !why) { state = 'failed'; why = e.code; lastFail = e.code + (e.detail ? ': ' + e.detail : ''); }
        loadP = null;
        diag(big ? 'large-failed' : 'pocket-failed', lastFail.slice(0, 160));
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
    //   A slot without a kinds head (the full database): kd is not used, and a kind's score is its share of the species answer.
    function fuseWith(c, kd, sd, month) {
      var f = c.f, labels = c.labels, table = c.table, n = labels.length, z, i, p = null, q = {}, s = null, order = [], comb, kinds = [], species = [];
      if (c.head) {
        var nr = c.rowAt.length, pr;
        z = new Float64Array(nr);
        for (i = 0; i < nr; i++) z[i] = f.t_kind * kd[i] + (c.kb ? c.kb[i] : 0);
        pr = softmax(z);
        if (nr === n) p = pr;
        else { p = new Float64Array(n); for (i = 0; i < nr; i++) p[c.rowAt[i]] += pr[i]; }   // rows that share a label are one kind
      }
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
      if (!c.head) {
        if (!s) throw err('unfit', 'a slot without a kinds head was given no species scores');
        comb = new Float64Array(n);
        for (i = 0; i < n; i++) comb[i] = q[labels[i]] || 0;
      } else if (f.rule === 'mix') {
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
      for (i = 0; i < n; i++) kinds.push({ key: labels[i], p: comb[i], head: p ? p[i] : null, list: speaks(i) ? (q[labels[i]] || 0) : null });
      kinds.sort(function (a, b) { return b.p - a.p; });
      // Not sure is an answer. Under fusion.kind_at no kind is asserted and no species named: the three likeliest kinds of living thing are
      // offered instead (the species offers are worked out as ever). Without fusion.kind_at every answer is asserted, as before build 8.
      var kind = kinds[0].key, named = null, offers = [], sure = !(num(f.kind_at) && kinds[0].p < f.kind_at), kindOffers = [];
      if (!sure) kindOffers = kinds.filter(function (k) { return k.key !== 'none'; }).slice(0, 3).map(function (k) { return k.key; });
      if (species.length && kind !== 'none' && kind !== 'person') {
        if (sure && species[0].p >= f.name_at && species[0].kind === kind) named = species[0];
        else {
          // the three likeliest are kept as offers. They are taken from the kind that won, so that a flower is not offered a turtle;
          // a manifest that sets fusion.offer_any_kind takes the three likeliest of any kind.
          var three = (f.offer_any_kind ? order : order.filter(function (j) { return table[j].kind === kind; })).slice(0, 3).map(function (j) { return { sci: table[j].sci, en: table[j].en, p: s[j], kind: table[j].kind }; });
          if (three.reduce(function (a, r) { return a + r.p; }, 0) >= f.offer_at) offers = three;
        }
      }
      return { kind: kind, kindP: kinds[0].p, sure: sure, kinds: kinds, kindOffers: kindOffers, species: species, named: named, offers: offers };
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
      var tAsk = performance.now(), wasReady = state === 'ready', shot = pixels(canvas, file), mine = ++asked;   // read now: the canvas may show something else by the time the encoder is ready
      shot.catch(function () {});
      function run() {
        if (big && mine !== asked) return Promise.reject(err('photo', 'a newer photo is waiting'));   // only the photo in hand is worth the seconds
        clearTimeout(idleTimer);
        return ready().then(function () { return shot.catch(function (e) { throw err('photo', e && e.message); }); }).then(function (px) {
          var tRun = performance.now();
          return new Promise(function (res, rej) {
            var id = nextId++;
            pending[id] = { res: res, rej: rej, timer: setTimeout(function () { if (pending[id]) stop('slow', 'no answer in ' + watchMs + ' ms'); }, watchMs) };
            worker.postMessage({ op: 'run', id: id, rgba: px.buf, w: px.w, h: px.h, wantPre: !!api.wantPre }, [px.buf]);
          }).then(function (m) {
            // far from the species list's place: a slot with a kinds head leaves the list out; one without still takes the kind from it, with no month's weight
            var t = performance.now(), month = new Date().getMonth(), away = pocket.local === false, local = !away && !!cur.table;
            var r = fuseWith(cur, m.kinds, local || !cur.head ? m.species : null, local ? month : null);
            r.month = month; r.local = local;                // local: the species list of this slot's region was consulted for a name
            r.kindAt = num(cur.f.kind_at) ? cur.f.kind_at : null;
            r.ms = { load: wasReady ? 0 : Math.round(tRun - tAsk), pre: Math.round(m.ms.pre), run: Math.round(m.ms.run), post: Math.round((m.ms.post + performance.now() - t) * 10) / 10 };
            r.backend = info.backend; r.model = M.id; r.at = Date.now(); r.from = px.w + 'x' + px.h;
            last = r; if (api.wantPre) { api.lastEmb = m.emb; api.lastPre = m.pre; api.lastDots = { kinds: m.kinds, species: m.species }; }
            return r;
          });
        });
      }
      if (!big) return run();
      var p = queue.then(run, run); queue = p.catch(function () {}).then(tire); return p;     // one photo at a time through the full database
    }
    function mb(n) { return Math.max(0, Math.round(n / 1e6)); }
    function line() {
      if (big) return !(getP && M) ? 'Looking more closely\u2026' : have === 'kept' ? 'Checking the full database\u2026' : 'Downloading the full database\u2026 ' + mb(keptBytes + partGot) + ' of ' + Math.max(1, mb(M.vision.bytes)) + ' MB';
      if (state === 'loading' && total > got) return 'Downloading\u2026 ' + mb(got) + ' of ' + Math.max(1, mb(total)) + ' MB';
      return 'Looking\u2026';
    }
    function warm() {                                  // once the opening screen is up and the page has nothing else to do
      if (big || cannot || (navigator.connection && navigator.connection.saveData)) return;
      function go() { if (state === 'idle') ready().catch(function () {}); }
      function soon() { if (window.requestIdleCallback) requestIdleCallback(go, { timeout: 4000 }); else setTimeout(go, 1200); }
      if (document.readyState === 'complete') soon(); else window.addEventListener('load', soon);
    }
    api = {
      usable: function () { return !cannot; }, whyNot: function () { return SAY[cannot] || ''; },
      recognize: recognize, line: line, warm: warm, ready: ready, fuse: function (kd, sd, month) { return fuseWith(cur, kd, sd, month); },
      fetching: function () { return state === 'loading' && total > got; },      // the first download is under way
      place: function () { return (M && M.species && typeof M.species.place === 'string' && clip(M.species.place, 60)) || 'Gainesville, Florida'; },   // where the species list is from
      listed: function () { return !!(cur && cur.table); },
      // A typed name looked up in the species list: the species it names exactly, the species whose names hold every word of it, and the
      // species whose names are a slip of the keys away. The most recorded come first. Empty where there is no list.
      find: function (q) {
        var t = cur && cur.table, s = plain(q), out = { exact: null, has: [], near: [] }, ws, lim, best = -1;
        if (!t || s.length < 3) return out;
        ws = s.split(' '); lim = s.length <= 5 ? 1 : 2;
        t.forEach(function (r) {
          var en = plain(r.en), sci = plain(r.sci), w = 0, i;
          if (r.m) for (i = 0; i < 12; i++) w += r.m[i];
          if (en === s || sci === s) { if (w > best) { best = w; out.exact = r; } return; }
          if (ws.every(function (x) { return (' ' + en + ' ').indexOf(' ' + x) >= 0 || (' ' + sci + ' ').indexOf(' ' + x) >= 0; })) { out.has.push([w, r]); return; }
          if ((en && Math.abs(en.length - s.length) <= lim && slips(s, en, lim) <= lim) || (sci && Math.abs(sci.length - s.length) <= lim && slips(s, sci, lim) <= lim)) out.near.push([w, r]);
        });
        function top(a) { return a.sort(function (x, y) { return y[0] - x[0]; }).slice(0, 3).map(function (x) { return x[1]; }); }
        out.has = top(out.has); out.near = top(out.near); return out;
      },
      progress: function (fn) { onProgress = fn; },
      // the full database: what of it is here, fetching it, stopping, deleting; its size and, where the manifest gives one, a measured time for a photo
      survey: survey, get: get, halt: halt, forget: forget, say: function (code) { return SAY[code] || SAY.died; },
      has: function () { return getP ? 'getting' : have; },
      broken: function () { return state === 'failed' && (why === 'browser' || why === 'unfit'); },   // it has shown that it cannot run here: not tried again for every photo
      size: function () { return M ? { bytes: M.vision.bytes || 0, kept: keptBytes + partGot, mb: Math.max(1, mb(M.vision.bytes || 0)), keptMb: mb(keptBytes + partGot), seconds: M.seconds_a_photo || null } : null; },
      offers: [], kindOffers: [], file: null, local: true, wantPre: false, lastEmb: null, lastPre: null, lastDots: null,
      about: function () { return { state: state, why: why, fail: lastFail, model: M ? M.id : '', rule: M ? (M.fusion.rule || 'product') : '', trained: !!(cur && (cur.kb || cur.sb)), backend: info.backend, threads: info.threads, loadMs: Math.round(loadMs), start: info.ms || null, last: last, got: got, total: total, slot: manifestUrl, fitted: M && M.fitted_on && typeof M.fitted_on === 'object' ? M.fitted_on : null,
        have: getP ? 'getting' : have, keptBytes: keptBytes + partGot, bytes: M && M.vision.bytes || 0, getFail: getFail }; },
      test: { kill: function (how) { if (worker) worker.postMessage({ op: 'die', how: how }); }, watch: function (ms) { watchMs = ms; }, forget: function () { stop('died', 'forgotten by a check'); state = 'idle'; why = ''; },
        idle: function (ms) { idleMs = ms; tire(); }, netWait: function (ms) { netWaitMs = ms; }, running: function () { return !!worker; },
        // the scoring with settings given by a check, through the same readers as a real slot (tools/fusion/parity.py)
        world: function (m, rows, sb) { worlds.push(slotOf(readManifest(JSON.stringify(m)), rows ? readTable(new TextEncoder().encode(JSON.stringify({ species: rows })).buffer, rows.length) : null, sb ? Float64Array.from(sb) : null)); return worlds.length - 1; },
        fuseIn: function (w, kd, sd, month) { return fuseWith(worlds[w], kd, sd, month); } }
    };
    return api;
  }
  var pocket = recognizer({ slot: (/[?&]rec=([A-Za-z0-9_.\/-]+)/.exec(location.search || '') || [0, 'models/pocket'])[1] });
  // The full database's slot. A check on this machine may name another slot, or switch it off; a link to the public page may not.
  var large = recognizer({ big: true, slot: ((onThisMachine ? /[?&]big=([A-Za-z0-9_.\/-]+)/.exec(location.search || '') : null) || [0, 'models/naturalist'])[1] });

  // ---------- the species service (the naturalist): the full database on a server, asked only with the person's say-so
  // Where it lives is told by a small file at the site's root, service.json, fetched only when it is first needed:
  //   {"api": "gradio", "call": "https://<space>.hf.space/gradio_api/call/identify", "region": "us-fl-alachua", "model": "bioclip2-l14",
  //    "health": "<an address that answers {"ready": true}>" (optional), "kind_at": 0.9, "name_at": 0.5, "top": 5, "wake_s": 90, "answer_s": 60}
  // No such file: the feature does not exist, and nothing on the page mentions it. Nothing is sent before the person has said yes.
  // The call is Gradio's two steps: POST <call> {"data": [photo as base64 JPEG, month 1-12, region or "", top]} -> {"event_id"};
  // GET <call>/<event_id> is a stream of events, and the one named "complete" carries [answer].
  var naturalist = (function () {
    var KEY = 'seenback.service.v1', mem = '', cfg = null, cfgP = null, known = false;
    var local = /^(localhost|127\.0\.0\.1)$/.test(location.hostname);
    var asked = local ? /[?&]svc=(off|[A-Za-z0-9_.\/-]+\.json)/.exec(location.search || '') : null;   // a check on this machine may name another file; a link to the public page may not
    var T = { wake: 90000, answer: 60000, post: 20000, poll: 3000 };
    function num(x) { return typeof x === 'number' && isFinite(x); }
    function okUrl(u) { return typeof u === 'string' && (/^https:\/\/[^\/]+\//.test(u) || (local && /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?\//.test(u))); }
    function readConfig(j) {
      if (!j || typeof j !== 'object' || j.api !== 'gradio' || !okUrl(j.call) || (j.health !== undefined && !okUrl(j.health))) return null;   // an arrangement this build does not know is as good as none
      var host = ''; try { host = new URL(j.call).host; } catch (e) { return null; }
      if (num(j.wake_s)) T.wake = j.wake_s * 1000;
      if (num(j.answer_s)) T.answer = j.answer_s * 1000;
      return { call: j.call.replace(/\/+$/, ''), health: j.health || '', region: typeof j.region === 'string' ? j.region : '', model: clip(j.model, 60), host: host,
        where: /(^|\.)hf\.space$|(^|\.)huggingface\.co$/.test(host) ? 'hosted by Hugging Face' : 'at ' + host,
        kindAt: num(j.kind_at) ? j.kind_at : null, nameAt: num(j.name_at) ? j.name_at : 0, top: num(j.top) ? Math.max(1, Math.min(10, Math.round(j.top))) : 5 };
    }
    function config() {                                // resolves with the service's particulars, or null where there is none
      if (inViewer || (asked && asked[1] === 'off')) return Promise.resolve(null);
      if (known) return Promise.resolve(cfg);
      if (!cfgP) cfgP = fetch(asked ? asked[1] : 'service.json', { cache: 'no-cache', credentials: 'omit' }).then(function (r) {
        if (r.status === 404) { known = true; return null; }               // no such file: there is no service
        if (!r.ok) throw new Error('service.json ' + r.status);
        return r.json().then(function (j) { cfg = readConfig(j); known = true; return cfg; });
      }).catch(function () { cfgP = null; return null; });                  // no network just now, or not JSON: look again another time
      return cfgP;
    }
    function choice() { try { var v = localStorage.getItem(KEY); return v === 'yes' || v === 'no' ? v : ''; } catch (e) { return mem; } }
    function setChoice(v) { mem = v === 'yes' || v === 'no' ? v : ''; try { if (mem) localStorage.setItem(KEY, mem); else localStorage.removeItem(KEY); } catch (e) {} }
    function fail(code, detail) { var e = new Error(code); e.code = code; e.detail = String(detail || '').slice(0, 120); return e; }
    // What leaves the device: the photo with its longest side at most 512, as a JPEG under 1 MB. Nothing else about the photo or the person.
    function jpeg(canvas) {
      var k = Math.min(1, 512 / Math.max(canvas.width, canvas.height)), c = makeCanvas(canvas.width * k, canvas.height * k), x = c.getContext('2d'), q = [.85, .7, .5, .3], i, url = '';
      x.imageSmoothingQuality = 'high'; x.drawImage(canvas, 0, 0, c.width, c.height);
      for (i = 0; i < q.length; i++) { url = c.toDataURL('image/jpeg', q[i]); if (url.length * .75 < 1e6) break; }
      c.width = c.height = 1;
      if (url.indexOf('data:image/jpeg;base64,') !== 0 || url.length * .75 >= 1e6) throw fail('photo', 'not a small JPEG');
      return url.slice(23);
    }
    function clean(out) {                              // the answer, with nothing taken on trust
      if (typeof out === 'string') { try { out = JSON.parse(out); } catch (e) { out = null; } }
      if (!out || typeof out !== 'object' || !Array.isArray(out.species)) throw fail(out && (out.error || out.refused) ? 'refused' : 'garbled', out && (out.error || out.refused));
      var species = out.species.slice(0, 10).map(function (s) {
        return s && typeof s === 'object' && num(s.p) ? { sci: clip(s.sci, 80), en: clip(s.en, 60), kind: known(s.eyes) ? s.eyes : 'other', p: Math.max(0, Math.min(1, s.p)) } : null;
      }).filter(function (s) { return s && (s.sci || s.en); });
      var kinds = (Array.isArray(out.kinds) ? out.kinds : []).map(function (k) { return k && typeof k === 'object' && num(k.p) && (known(k.key) || k.key === 'none') ? { key: k.key, p: Math.max(0, Math.min(1, k.p)) } : null; }).filter(Boolean);
      species.sort(function (a, b) { return b.p - a.p; }); kinds.sort(function (a, b) { return b.p - a.p; });
      return { species: species, kinds: kinds, region: typeof out.region === 'string' ? out.region : '', model: clip(out.model, 60), ms: num(out.ms) ? out.ms : 0 };
    }
    function opts(signal, more) {                      // no cookies, no address of the page it came from
      var o = { mode: 'cors', credentials: 'omit', cache: 'no-store', referrerPolicy: 'no-referrer', signal: signal }, k;
      for (k in more) o[k] = more[k];
      return o;
    }
    function listen(url, signal) {                     // the stream of events for one question, until the one that completes it
      return fetch(url, opts(signal, { headers: { Accept: 'text/event-stream' } })).then(function (r) {
        if (!r.ok) throw fail('failed', 'GET ' + r.status);
        var dec = new TextDecoder('utf-8'), buf = '', found = null;
        function take(final) {
          var parts = buf.split(/\r?\n\r?\n/), i, ev, data;
          buf = final ? '' : parts.pop();
          for (i = 0; i < parts.length && !found; i++) {
            ev = (/^event:\s*(.*)$/m.exec(parts[i]) || [])[1]; data = parts[i].split(/\r?\n/).filter(function (l) { return /^data:/.test(l); }).map(function (l) { return l.replace(/^data:\s?/, ''); }).join('\n');
            if (ev === 'complete') found = { data: data }; else if (ev === 'error') found = { error: data };
          }
          return found;
        }
        function finish() {
          if (!found) throw fail('garbled', 'the stream ended with no answer');
          if (found.error !== undefined) throw fail('failed', found.error);
          var j; try { j = JSON.parse(found.data); } catch (e) { throw fail('garbled', 'the answer is not JSON'); }
          return clean(Array.isArray(j) ? j[0] : j);
        }
        if (!r.body || !r.body.getReader) return r.text().then(function (t) { buf = t; take(true); return finish(); });
        var reader = r.body.getReader();
        function pump() {
          return reader.read().then(function (x) {
            if (x.value) buf += dec.decode(x.value, { stream: true });
            if (take(x.done)) { try { reader.cancel(); } catch (e) {} return finish(); }
            if (x.done) return finish();
            return pump();
          });
        }
        return pump();
      });
    }
    // One question. say('asking' | 'waking') tells the page what to show. Returns { promise, cancel }.
    function ask(canvas, o, say) {
      var ctl = typeof AbortController === 'function' ? new AbortController() : null, signal = ctl ? ctl.signal : undefined, t0 = performance.now(), tries = 0, over = false, net = false, timers = [];
      function left() { return T.wake - (performance.now() - t0); }
      function wait(ms) { return new Promise(function (res) { timers.push(setTimeout(res, ms)); }); }
      function within(p, ms, code) {                   // p, or a failure once ms have passed
        return new Promise(function (res, rej) { var t = setTimeout(function () { rej(fail(code)); }, ms); timers.push(t); p.then(function (v) { clearTimeout(t); res(v); }, function (e) { clearTimeout(t); rej(e); }); });
      }
      // "Waking up" is said only where it is the likely truth: the service did not answer, and this site itself can still be reached.
      // (A request the service worker leaves alone, so that a kept copy cannot answer for a network that is gone.)
      function reachable() {
        if (net) return Promise.resolve(true);
        return within(fetch(location.href.split('#')[0], { method: 'HEAD', cache: 'no-store', credentials: 'omit' }).then(function (r) { net = r.ok; return net; }), 8000, 'offline').catch(function () { return false; });
      }
      function sayWaking() { return reachable().then(function (yes) { if (over) throw fail('cancelled'); if (!yes) throw fail('offline', 'this site cannot be reached either'); say('waking'); }); }
      function awake() {                               // where the service names an address that says whether it is ready, that is asked first
        if (!cfg.health) return Promise.resolve();
        return within(fetch(cfg.health, opts(signal)).then(function (r) { return r.ok ? r.json() : null; }), T.post, 'asleep').catch(function () { return null; }).then(function (h) {
          if (over) throw fail('cancelled');
          if (h && h.ready !== false && h.ok !== false) return;
          if (left() <= 0) throw fail('asleep', 'not ready in time');
          return (h ? Promise.resolve(say('waking')) : sayWaking()).then(function () { return wait(Math.min(T.poll, Math.max(200, left()))); }).then(awake);
        });
      }
      function post(body) {
        tries++; if (tries === 1) say('asking');
        return within(fetch(cfg.call, opts(signal, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: body })).then(function (r) {
          if (!r.ok) throw fail(r.status === 429 ? 'busy' : (r.status >= 500 || r.status === 404) ? 'asleep' : 'refused', 'POST ' + r.status);
          return r.json().catch(function () { throw fail('garbled', 'no event id'); });
        }, function (e) { throw e && e.code ? e : fail(over ? 'cancelled' : 'asleep', e && e.message); }), T.post, 'asleep').then(function (j) {
          var id = j && j.event_id;
          if (typeof id !== 'string' || !/^[A-Za-z0-9_.-]{1,120}$/.test(id)) throw fail('garbled', 'no event id');
          say('asking');
          return within(listen(cfg.call + '/' + id, signal), T.answer, 'slow');
        }, function (e) {
          // no answer at the door: a server that sleeps when nobody calls takes a while to wake. Try again, less and less often, for as long as the wait allows.
          if (e.code !== 'asleep' || over || left() <= 0) throw e;
          return sayWaking().then(function () { return wait(Math.min(T.poll * Math.min(tries, 5), Math.max(200, left()))); }).then(function () { if (over) throw fail('cancelled'); return awake(); }).then(function () { return post(body); });
        });
      }
      var promise = config().then(function (c) {
        if (!c) throw fail('absent');
        if (navigator.onLine === false) throw fail('offline');
        var body = JSON.stringify({ data: [jpeg(canvas), o.month, o.local ? c.region : '', c.top] });
        return awake().then(function () { return post(body); });
      });
      function end() { over = true; timers.forEach(clearTimeout); }
      promise.then(end, function () { end(); if (ctl) try { ctl.abort(); } catch (e) {} });
      return { promise: promise, cancel: function () { end(); if (ctl) try { ctl.abort(); } catch (e) {} } };
    }
    return { config: config, choice: choice, setChoice: setChoice, ask: ask, cfg: function () { return cfg; },
      test: { times: function (t) { for (var k in t) T[k] = t[k]; return T; }, read: function (j) { return readConfig(j); } } };
  })();
