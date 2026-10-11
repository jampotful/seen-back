// Seen Back self-test, build 14: fetched by the page only for ?selftest=1. Made by build.py from src/cam.selftest.js.
(function (I) {
  if (!I) return;
  var $ = I['$'], BUILD = I['BUILD'], EYES = I['EYES'], Engine = I['Engine'], HUMAN = I['HUMAN'], HUMAN_CPD = I['HUMAN_CPD'], ORDER = I['ORDER'], S = I['S'], calm = I['calm'], canvas = I['canvas'], clamp = I['clamp'], coarse = I['coarse'], decode = I['decode'], engine = I['engine'], fxNow = I['fxNow'], go = I['go'], hasCamera = I['hasCamera'], lerp = I['lerp'], makeCanvas = I['makeCanvas'], mix = I['mix'], paramsOf = I['paramsOf'], pocket = I['pocket'], setEyes = I['setEyes'], showStill = I['showStill'], vid = I['vid'];

  // ---------- self-test: open the page with ?selftest=1 and it checks its own picture engine
  // It takes over the page: a test card drawn through every eye and read back, moving pictures from a canvas and
  // from a video, the change of eyes held at three instants, and a contact sheet at the end. The result is shown
  // on screen, kept in window.__selftest, and sent as JSON to the same-origin path in &report=/path when given.
  // Only robust properties are judged; everything else is recorded as numbers.
  // It reads only page bindings that are set once at start-up (build.py lists them as SELFTEST_READS), so it can run either inside the
  // page's script or as selftest.js, fetched by the page only for ?selftest=1 and handed those bindings by a small hook.
  (function () {
    var qs = location.search || '';
    if (!/[?&]selftest=1(?:&|$)/.test(qs)) return;
    S.selftest = true;
    var rp = /[?&]report=([^&]*)/.exec(qs), reportPath = '';
    try { reportPath = rp ? decodeURIComponent(rp[1]) : ''; } catch (e) { reportPath = ''; }
    if (!/^\/(?!\/)[\w\-\/.]*$/.test(reportPath)) reportPath = '';
    var T = window.__selftest = { v: 1, build: BUILD, done: false, ok: null, fails: [], checks: 0, phase: 'start', env: {}, still: {}, motion: {}, pose: [], ms: {} };
    var tStart = performance.now(), STEADY = { ap: 1, shape: 0, mosaic: 0, soft: 0, expo: 1, focus: .5, mirror: false, camZoom: 1 };
    var EYELIST = ['person'].concat(ORDER), TWO_CONE = ['cat', 'dog', 'deer', 'rabbit', 'squirrel'], MOVERS = ['frog', 'wader', 'squirrel', 'plant'];
    var LIN = []; for (var i = 0; i < 256; i++) { var c = i / 255; LIN.push(c <= .04045 ? c / 12.92 : Math.pow((c + .055) / 1.055, 2.4)); }

    function el(tag, css, text, parent) { var e = document.createElement(tag); if (css) e.style.cssText = css; if (text !== undefined) e.textContent = text; if (parent) parent.appendChild(e); return e; }
    function frame() { return new Promise(function (res) { requestAnimationFrame(res); }); }
    function wait(ms) { return new Promise(function (res) { setTimeout(res, ms); }); }
    function r2(x) { return Math.round(x * 100) / 100; }
    function rgb(a) { return a.map(Math.round); }
    function check(name, ok, detail) { T.checks++; if (!ok) T.fails.push(name + (detail ? ': ' + detail : '')); return ok; }
    function phase(p, line) { T.phase = p; stLine.textContent = line || p; }
    function since() { return Math.round(performance.now() - tStart); }

    // ---- the page: everything of the app is hidden but its video element; the picture canvas moves into the report
    var style = el('style', '', '#app>:not(#vid){display:none!important}' +
      '#selftest{position:fixed;inset:0;z-index:50;overflow:auto;-webkit-overflow-scrolling:touch;background:#101010;color:#eee;font:14px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;' +
      'padding:calc(12px + env(safe-area-inset-top,0px)) 16px calc(28px + env(safe-area-inset-bottom,0px));box-sizing:border-box;-webkit-user-select:text;user-select:text}' +
      '#selftest h1{font:400 30px/1.05 var(--serif);margin:0 0 2px;letter-spacing:-.01em}' +
      '#selftest .ln{color:#bbb;margin:0 0 8px;min-height:1.4em}' +
      '#stStage{position:relative;background:#000;margin:0 0 10px;overflow:hidden}' +
      '#stStage.full{position:fixed;inset:0;z-index:60;margin:0;width:auto!important;height:auto!important}' +
      '#stCap{position:absolute;left:0;right:0;top:0;padding:calc(10px + env(safe-area-inset-top,0px)) 14px 10px;background:rgba(0,0,0,.72);color:#fff;font:600 17px/1.3 system-ui,-apple-system,sans-serif}' +
      '#stCap:empty{display:none}' +
      '#stSum{font-size:16px;margin:4px 0 8px}#stSum b.ok{color:#7ddc8a}#stSum b.no{color:#ff7b7b}' +
      '#stSum ul{margin:4px 0 0;padding-left:18px;color:#ffb3b3;font-size:13px}' +
      '#stBtns{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:0 0 12px}' +
      '#stBtns button{font:600 15px system-ui,-apple-system,sans-serif;min-height:44px;padding:0 18px;border-radius:999px;border:0;background:#f4f1ea;color:#111}' +
      '#stSheet{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin:0 0 14px}' +
      '@media (min-width:900px){#stSheet{grid-template-columns:repeat(8,minmax(0,1fr))}}' +
      '#stSheet figure{margin:0}#stSheet canvas{display:block;width:100%;height:auto;background:#000}' +
      '#stSheet figcaption{font-size:12px;line-height:1.2;padding:2px 0 0;color:#ddd;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
      '#stSheet figcaption.no{color:#ff7b7b}' +
      '#selftest table{border-collapse:collapse;font-size:12px;margin:0 0 12px}#selftest td,#selftest th{border-bottom:1px solid #333;padding:3px 8px 3px 0;text-align:left;vertical-align:top}' +
      '#selftest pre,#selftest textarea{font:11px/1.35 ui-monospace,Menlo,Consolas,monospace;color:#cfcfcf;white-space:pre-wrap;word-break:break-all}' +
      '#selftest textarea{width:100%;height:160px;background:#000;border:1px solid #333;box-sizing:border-box}', document.head);
    var root = el('div', '', undefined, document.body); root.id = 'selftest';
    el('h1', '', 'Regards self-test', root);
    var stLine = el('p', '', 'Starting.', root); stLine.className = 'ln';
    var stSum = el('div', '', '', root); stSum.id = 'stSum';
    var stBtns = el('div', '', undefined, root); stBtns.id = 'stBtns'; stBtns.hidden = true;
    var btnCopy = el('button', '', 'Copy report', stBtns), copied = el('span', 'color:#bbb', '', stBtns);
    var stage = el('div', '', undefined, root); stage.id = 'stStage';
    var cap = el('div', '', '', stage); cap.id = 'stCap';
    if (canvas) stage.insertBefore(canvas, cap);
    var sheet = el('div', '', undefined, root); sheet.id = 'stSheet';
    var details = el('div', '', undefined, root);
    var ta = el('textarea', '', '', root); ta.readOnly = true; ta.hidden = true;
    function fitStage() {
      if (stage.classList.contains('full') || !canvas) return;
      var a = canvas.width / Math.max(1, canvas.height), wMax = root.clientWidth - 32, hMax = Math.max(160, innerHeight * .55);
      var w = Math.min(wMax, hMax * a); stage.style.width = Math.round(w) + 'px'; stage.style.height = Math.round(w / a) + 'px';
    }
    function sizeCanvas(w, h) { canvas.width = Math.max(2, Math.round(w)); canvas.height = Math.max(2, Math.round(h)); fitStage(); }
    function fullSize() {          // the size the app itself would draw at, filling this screen (as engine.resize does)
      var dpr = Math.min(window.devicePixelRatio || 1, 2), w = innerWidth * dpr, h = innerHeight * dpr, k = Math.min(1, engine.side() / Math.max(w, h, 1));
      sizeCanvas(w * k, h * k);
    }

    // ---- reporting
    function post() {
      if (!reportPath || typeof fetch !== 'function') return Promise.resolve();
      T.ms.total = since();
      return fetch(reportPath, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(T) })
        .then(function (r) { T.posted = r.status; }, function (e) { T.postError = String(e).slice(0, 120); });
    }
    btnCopy.addEventListener('click', function () {
      var txt = JSON.stringify(T);
      function fallback() {
        ta.hidden = false; ta.value = txt; ta.focus(); ta.select();
        var ok = false; try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
        copied.textContent = ok ? 'Copied.' : 'Select the text in the box below and copy it.';
      }
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(function () { copied.textContent = 'Copied. Paste it into a message to us.'; }, fallback);
      else fallback();
    });

    // ---- the test card: colour patches, a grey ramp, a horizon, fine gratings, and four corner markers
    var PERIODS = [2, 4, 8, 16];
    function layout(W, H) {
      var L = { patches: [], ramp: [], grat: [], corners: [] }, names = ['red', 'green', 'blue', 'yellow', 'white'], cols = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ffffff'];
      names.forEach(function (n, i) { L.patches.push({ name: n, col: cols[i], x: Math.round((.10 + i * .17) * W), y: Math.round(.10 * H), w: Math.round(.14 * W), h: Math.round(.22 * H) }); });
      for (var j = 0; j < 6; j++) L.ramp.push({ v: j * 51, x: Math.round((.10 + j * .8 / 6) * W), y: Math.round(.36 * H), w: Math.round(.8 / 6 * W), h: Math.round(.10 * H) });
      L.horizon = { y: Math.round(.505 * H), h: Math.max(2, Math.round(.006 * H)) };
      ['v', 'h'].forEach(function (o, row) {
        PERIODS.forEach(function (p, k) { L.grat.push({ name: o + p, o: o, p: p, x: Math.round((.08 + k * .215) * W), y: Math.round((row ? .75 : .55) * H), w: Math.round(.195 * W), h: Math.round(.16 * H) }); });
      });
      var s = Math.round(.07 * H), m = Math.round(.02 * H);
      L.corners = [{ name: 'tl', col: '#ffffff', x: m, y: m }, { name: 'tr', col: '#ff0000', x: W - m - s, y: m }, { name: 'bl', col: '#00ff00', x: m, y: H - m - s }, { name: 'br', col: '#0000ff', x: W - m - s, y: H - m - s }];
      L.corners.forEach(function (c) { c.w = s; c.h = s; });
      return L;
    }
    function drawCard(W, H) {
      var c = makeCanvas(W, H), x = c.getContext('2d'), L = layout(W, H);
      x.fillStyle = '#5f5f5f'; x.fillRect(0, 0, W, H);
      L.patches.forEach(function (p) { x.fillStyle = p.col; x.fillRect(p.x, p.y, p.w, p.h); });
      L.ramp.forEach(function (p) { x.fillStyle = 'rgb(' + p.v + ',' + p.v + ',' + p.v + ')'; x.fillRect(p.x, p.y, p.w, p.h); });
      x.fillStyle = '#e8e8e8'; x.fillRect(0, L.horizon.y, W, L.horizon.h);
      L.grat.forEach(function (g) {
        x.fillStyle = '#000'; x.fillRect(g.x, g.y, g.w, g.h); x.fillStyle = '#fff';
        if (g.o === 'v') for (var a = 0; a < g.w; a += g.p) x.fillRect(g.x + a, g.y, g.p / 2, g.h);
        else for (var b = 0; b < g.h; b += g.p) x.fillRect(g.x, g.y + b, g.w, g.p / 2);
      });
      L.corners.forEach(function (p) { x.fillStyle = p.col; x.fillRect(p.x, p.y, p.w, p.h); });
      return { c: c, L: L };
    }

    // ---- where a point of the card lands on the screen: the view pass's own mapping, inverted (a still at full strength,
    // card and canvas the same size, so the person's eye maps every pixel to itself)
    function toScreen(P, W, H, sx, sy) {
      var A = W / H, qx = (sx / W - .5) * A, qy = sy / H - .5, qr = Math.hypot(qx, qy);
      if (qr < 1e-9) return [W / 2, H / 2];
      function out(r) { var rn = clamp(r / (.45 * Math.sqrt(A * A + 1)), 0, 1), mag = 1 / lerp(1 / P.fovea, 1, rn * rn); return r * (1 + P.barrel * r * r) / (P.zoom * mag); }
      var lo = 0, hi = 8;
      for (var i = 0; i < 48; i++) { var mid = (lo + hi) / 2; if (out(mid) < qr) lo = mid; else hi = mid; }
      var r = (lo + hi) / 2;
      return [(r * qx / qr / A + .5) * W, (r * qy / qr + .5) * H];
    }
    function screenBox(P, W, H, b, f) {
      var x0 = b.x + b.w * (.5 - f / 2), x1 = b.x + b.w * (.5 + f / 2), y0 = b.y + b.h * (.5 - f / 2), y1 = b.y + b.h * (.5 + f / 2);
      var pts = [toScreen(P, W, H, x0, y0), toScreen(P, W, H, x1, y0), toScreen(P, W, H, x0, y1), toScreen(P, W, H, x1, y1)];
      // keep only the inner part that every corner agrees on (the mapping bends straight edges a little)
      var X0 = Math.max(pts[0][0], pts[2][0]), X1 = Math.min(pts[1][0], pts[3][0]), Y0 = Math.max(pts[0][1], pts[1][1]), Y1 = Math.min(pts[2][1], pts[3][1]);
      var cx = (X0 + X1) / 2, cy = (Y0 + Y1) / 2;
      return { x0: clamp(Math.round(Math.min(X0, cx - .5)), 0, W - 1), x1: clamp(Math.round(Math.max(X1, cx + .5)), 1, W), y0: clamp(Math.round(Math.min(Y0, cy - .5)), 0, H - 1), y1: clamp(Math.round(Math.max(Y1, cy + .5)), 1, H) };
    }
    function stats(img, W, b) {
      var d = img.data, n = 0, s = [0, 0, 0], L = [];
      for (var y = b.y0; y < b.y1; y++) for (var x = b.x0; x < b.x1; x++) {
        var o = (y * W + x) * 4; s[0] += d[o]; s[1] += d[o + 1]; s[2] += d[o + 2]; n++;
        L.push(.2126 * LIN[d[o]] + .7152 * LIN[d[o + 1]] + .0722 * LIN[d[o + 2]]);
      }
      n = Math.max(1, n);
      var m = 0; L.forEach(function (v) { m += v; }); m /= Math.max(1, L.length);
      var vv = 0; L.forEach(function (v) { vv += (v - m) * (v - m); }); vv /= Math.max(1, L.length);
      return { rgb: [s[0] / n, s[1] / n, s[2] / n], lum: m, contrast: m > 1e-4 ? Math.sqrt(vv) / m : 0 };
    }
    function linDist(a, b) { var d = 0; for (var k = 0; k < 3; k++) { var e = LIN[Math.round(a[k])] - LIN[Math.round(b[k])]; d += e * e; } return Math.sqrt(d); }
    function lumOf(a) { return .2126 * LIN[Math.round(a[0])] + .7152 * LIN[Math.round(a[1])] + .0722 * LIN[Math.round(a[2])]; }
    function whole(img, W, H) {      // over the whole frame: spread of brightness, darkest share, largest gap between channels
      var d = img.data, n = 0, m = 0, m2 = 0, dark = 0, spread = 0, step = Math.max(1, Math.round(Math.min(W, H) / 120));
      for (var y = 0; y < H; y += step) for (var x = 0; x < W; x += step) {
        var o = (y * W + x) * 4, l = .299 * d[o] + .587 * d[o + 1] + .114 * d[o + 2];
        m += l; m2 += l * l; n++; if (l < 16) dark++;
        spread = Math.max(spread, Math.max(d[o], d[o + 1], d[o + 2]) - Math.min(d[o], d[o + 1], d[o + 2]));
      }
      m /= n; return { mean: m, std: Math.sqrt(Math.max(0, m2 / n - m * m)), dark: dark / n, spread: spread };
    }

    // ---- 1. the device
    async function envPhase() {
      phase('env', 'Reading what this browser offers.');
      var E = T.env, n = navigator;
      E.ua = n.userAgent; E.dpr = window.devicePixelRatio; E.viewport = innerWidth + 'x' + innerHeight; E.screen = screen.width + 'x' + screen.height;
      E.webgl2 = !!engine; E.side = engine ? engine.side() : null; E.coarse = coarse; E.calm = calm; E.camera = hasCamera;
      if (!engine) {
        try { E.webgl2Context = !!makeCanvas(4, 4).getContext('webgl2'); } catch (e) { E.webgl2Context = false; }
        try { Engine(makeCanvas(4, 4)); E.engineError = 'started on a second try'; } catch (e) { E.engineError = String(e && e.message || e).slice(0, 400); }
      }
      var gl = engine ? canvas.getContext('webgl2') : null;
      if (gl) {
        E.vendor = gl.getParameter(gl.VENDOR); E.renderer = gl.getParameter(gl.RENDERER); E.glVersion = gl.getParameter(gl.VERSION); E.glsl = gl.getParameter(gl.SHADING_LANGUAGE_VERSION);
        var dbg = null; try { dbg = gl.getExtension('WEBGL_debug_renderer_info'); } catch (e) { dbg = null; }
        if (dbg) { E.unmaskedVendor = gl.getParameter(dbg.UNMASKED_VENDOR_WEBGL); E.unmaskedRenderer = gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL); }
        E.floatOK = engine.floatOK; E.maxTexture = gl.getParameter(gl.MAX_TEXTURE_SIZE); E.maxLayers = gl.getParameter(gl.MAX_ARRAY_TEXTURE_LAYERS);
        E.maxSamplers = gl.getParameter(gl.MAX_TEXTURE_IMAGE_UNITS); E.colorSpace = gl.drawingBufferColorSpace || null;
        var ex = gl.getSupportedExtensions() || [];
        E.extCount = ex.length;
        E.ext = ['EXT_color_buffer_float', 'EXT_color_buffer_half_float', 'OES_texture_float_linear', 'EXT_float_blend', 'EXT_texture_filter_anisotropic', 'KHR_parallel_shader_compile', 'WEBGL_debug_renderer_info', 'EXT_disjoint_timer_query_webgl2', 'OVR_multiview2', 'WEBGL_compressed_texture_astc', 'WEBGL_compressed_texture_etc']
          .filter(function (k) { return ex.indexOf(k) >= 0; });
      }
      E.crossOriginIsolated = !!window.crossOriginIsolated; E.webgpu = !!n.gpu; E.offscreenCanvas = typeof OffscreenCanvas === 'function';
      E.captureStream = !!(HTMLCanvasElement.prototype.captureStream); E.rvfc = !!(window.HTMLVideoElement && 'requestVideoFrameCallback' in HTMLVideoElement.prototype);
      E.recorder = window.MediaRecorder && MediaRecorder.isTypeSupported ? ['video/mp4;codecs=avc1', 'video/mp4', 'video/webm;codecs=vp9', 'video/webm;codecs=vp8', 'video/webm', 'video/x-matroska;codecs=avc1']
        .filter(function (t) { try { return MediaRecorder.isTypeSupported(t); } catch (e) { return false; } }) : null;
      try { E.shareFiles = !!(n.canShare && n.canShare({ files: [new File([new Uint8Array([255, 216, 255])], 'x.jpg', { type: 'image/jpeg' })] })); } catch (e) { E.shareFiles = false; }
      E.serviceWorker = 'serviceWorker' in n; E.swControlled = !!(n.serviceWorker && n.serviceWorker.controller);
      E.cores = n.hardwareConcurrency || null; E.memoryGB = n.deviceMemory || null;
      E.canPlay = { mp4: vid.canPlayType('video/mp4; codecs="avc1.42E01E"'), webm: vid.canPlayType('video/webm; codecs="vp8"') };
      try { if (document.fonts && document.fonts.load) { await Promise.race([document.fonts.load('400 20px "Instrument Serif"'), wait(3000)]); E.serif = document.fonts.check('400 20px "Instrument Serif"'); } } catch (e) { E.serif = 'unknown'; }
      check('WebGL 2 engine starts', !!engine, E.engineError);
      post();
    }

    // ---- 1b. the recognizer, when the address names a slot (&rec=) and photos (&recphotos=a,b,c): each photo goes in as the page's
    // own photo does (a File, decoded to a canvas, then pocket.recognize), and with &recexpect=<expect.json> the answers are held
    // against what Python got for the same photos (test/rec/make_slot.py --photos)
    function param(name) { var m = new RegExp('[?&]' + name + '=([^&]*)').exec(qs); try { return m ? decodeURIComponent(m[1]) : ''; } catch (e) { return ''; } }
    function sameOrigin(u) { return /^(\/(?!\/)|[\w.\-]+(\/|$))/.test(u) && !/^[a-z][\w+.\-]*:/i.test(u); }
    async function recPhase() {
      var R = T.rec = { slot: param('rec'), photos: [] }, list = param('recphotos').split(',').filter(Boolean).filter(sameOrigin), ex = param('recexpect'), expect = null;
      phase('rec', 'The recognizer: starting it.');
      if (ex && sameOrigin(ex)) { try { expect = await (await fetch(ex, { cache: 'no-store' })).json(); R.expect = ex; } catch (e) { R.expectError = String(e).slice(0, 120); } }
      var t0 = performance.now();
      try { await pocket.ready(); R.readyMs = Math.round(performance.now() - t0); }
      catch (e) { R.readyMs = Math.round(performance.now() - t0); R.error = { code: e && e.code, sentence: e && e.sentence, detail: String(e && e.detail || e).slice(0, 200) }; }
      R.about = pocket.about(); delete R.about.last;
      check('rec: recognizer ready', !R.error, R.error ? R.error.sentence + ' (' + R.error.code + ': ' + R.error.detail + ')' : '');
      if (R.error) { post(); return; }
      pocket.wantPre = true;
      for (var i = 0; i < list.length; i++) {
        var url = list[i], name = url.split('/').pop().split('?')[0], P = { name: name };
        stLine.textContent = 'The recognizer: photo ' + (i + 1) + ' of ' + list.length + ' (' + name + ').';
        try {
          var blob = await (await fetch(url)).blob(), file = new File([blob], name, { type: blob.type || (/\.png$/i.test(name) ? 'image/png' : 'image/jpeg') });
          P.bytes = blob.size;
          var t1 = performance.now(), cv = await decode(file); P.decodeMs = Math.round(performance.now() - t1); P.shown = cv.width + 'x' + cv.height;
          var t2 = performance.now(), r = await pocket.recognize(cv, file); P.wallMs = Math.round(performance.now() - t2);
          P.from = r.from; P.ms = r.ms; P.kind = r.kind; P.kinds3 = r.kinds.slice(0, 3).map(function (k) { return [k.key, r2(k.p * 100) / 100]; });
          P.head3 = r.kinds.slice().sort(function (a, b) { return b.head - a.head; }).slice(0, 3).map(function (k) { return [k.key, Math.round(k.head * 1e4) / 1e4]; });
          if (r.species && r.species[0]) P.species1 = [r.species[0].sci, Math.round(r.species[0].p * 1e3) / 1e3];
          var py = expect && expect.kinds && expect.kinds[name], pe = expect && expect.photos && expect.photos[name];
          if (py) { P.python3 = py; P.match = P.head3[0][0] === py[0][0]; }
          if (pe && pe.embedding && pocket.lastEmb) {
            var e = pe.embedding, g = pocket.lastEmb, dot = 0, na = 0, nb = 0;
            for (var j = 0; j < e.length; j++) { dot += e[j] * g[j]; na += e[j] * e[j]; nb += g[j] * g[j]; }
            P.cosine = Math.round(dot / Math.sqrt(na * nb) * 1e6) / 1e6;
          }
          if (pe && pe.pre_sha256 && pocket.lastPre && window.crypto && crypto.subtle) {      // the 224 x 224 pixels the encoder got, against Pillow's
            var d = await crypto.subtle.digest('SHA-256', pocket.lastPre), hex = Array.prototype.map.call(new Uint8Array(d), function (x) { return ('0' + x.toString(16)).slice(-2); }).join('');
            P.preSame = hex === pe.pre_sha256;
          }
          check('rec ' + name + ': recognized', true);
          // Python's answer for an int8 model depends on the processor it ran on (its int8 kernels differ), so a photo whose two likeliest
          // kinds are within 0.05 of each other in Python's answer is recorded as a close call and not judged
          if (py) P.pyMargin = Math.round(((py[0] || [0, 0])[1] - (py[1] || [0, 0])[1]) * 1e4) / 1e4;
          if (py && !/^info-/.test(name) && P.pyMargin >= .05) check('rec ' + name + ': top kind matches Python', P.match, 'page ' + JSON.stringify(P.head3) + ', Python ' + JSON.stringify(py));
          // a PNG reaches both resizes as the same pixels, so the prepared picture must be Pillow's to the byte; an int8 encoder's
          // numbers differ between onnxruntime-web and native onnxruntime, and native onnxruntime's differ from one processor to the
          // next (cosines of 0.982 to 0.999 between build machines for the same photo), so the embedding is judged loosely
          if (P.preSame !== undefined && /\.png$/i.test(name) && !/^info-/.test(name)) check('rec ' + name + ': prepared pixels identical to Pillow\'s', P.preSame);
          if (P.cosine !== undefined && !/^info-/.test(name)) check('rec ' + name + ': embedding near Python\'s (cosine at least 0.98)', P.cosine >= .98, 'cosine ' + P.cosine);
        } catch (e) {
          P.error = { code: e && e.code, sentence: e && e.sentence, detail: String(e && (e.detail || e.message) || e).slice(0, 200) };
          check('rec ' + name + ': recognized', false, (P.error.sentence || '') + ' ' + P.error.detail);
        }
        R.photos.push(P);
        if (pocket.about().state !== 'ready' && i < list.length - 1) { try { await pocket.ready(); } catch (e) {} }
      }
      pocket.wantPre = false; pocket.lastPre = null;
      var runs = R.photos.filter(function (x) { return x.ms; });
      if (runs.length) R.meanRunMs = Math.round(runs.reduce(function (a, x) { return a + x.ms.pre + x.ms.run; }, 0) / runs.length);
      T.ms.rec = since();
      post();
    }

    // ---- 2. the test card through each of the sixteen eyes, read back
    async function stillPhase() {
      var side = engine.side(), W = Math.min(side, 480), H = Math.round(W * .75), card = drawCard(W, H), L = card.L;
      phase('still', 'Drawing a test card through each eye.');
      sizeCanvas(W, H); engine.setImage(card.c);
      var rc = makeCanvas(W, H), rx = rc.getContext('2d', { willReadFrequently: true });
      T.still.size = W + 'x' + H; T.still.eyes = {};
      await frame(); engine.draw(HUMAN, STEADY, performance.now(), 16); engine.state(); await frame();   // a first draw, so start-up costs are not counted
      for (var e = 0; e < EYELIST.length; e++) {
        var key = EYELIST[e], P = key === 'person' ? HUMAN : paramsOf(EYES[key]);
        stLine.textContent = 'Still pictures: ' + key + ' (' + (e + 1) + ' of ' + EYELIST.length + ').';
        var res = await new Promise(function (done) {
          requestAnimationFrame(function () {
            var t1 = performance.now();
            engine.draw(P, STEADY, performance.now(), 16);
            var err = engine.state().err;
            rx.drawImage(canvas, 0, 0);
            var img = rx.getImageData(0, 0, W, H);
            done({ err: err, img: img, ms: performance.now() - t1 });
          });
        });
        var img = res.img, R = { err: res.err, ms: Math.round(res.ms), patches: {}, ramp: [], grat: {}, corners: {} };
        L.patches.forEach(function (p) { R.patches[p.name] = rgb(stats(img, W, screenBox(P, W, H, p, .4)).rgb); });
        L.ramp.forEach(function (p) { R.ramp.push(Math.round(stats(img, W, screenBox(P, W, H, p, .4)).rgb[1])); });
        L.grat.forEach(function (g) { R.grat[g.name] = r2(stats(img, W, screenBox(P, W, H, g, .6)).contrast); });
        L.corners.forEach(function (c) { R.corners[c.name] = rgb(stats(img, W, screenBox(P, W, H, c, .5)).rgb); });
        var wh = whole(img, W, H); R.mean = Math.round(wh.mean); R.std = r2(wh.std); R.spread = wh.spread;
        T.still.eyes[key] = R;
        var tile = makeCanvas(160, 120); tile.getContext('2d').drawImage(rc, 0, 0, 160, 120);
        var fig = el('figure', '', undefined, sheet); fig.appendChild(tile); fig.dataset.key = key;
        el('figcaption', '', key === 'person' ? 'person (you)' : key, fig);
        await frame();
      }
      // judged: only what holds whatever the renderer
      var E = T.still.eyes, person = E.person;
      EYELIST.forEach(function (k) {
        var bad = !check('still ' + k + ': picture not blank', E[k].std > 1.5 && E[k].mean > 2, 'mean ' + E[k].mean + ', spread ' + E[k].std);
        bad = !check('still ' + k + ': no GL error', E[k].err === 0, 'error 0x' + (E[k].err || 0).toString(16)) || bad;
        if (bad) markTile(k);
      });
      var C = person.corners, upright = C.tl[0] > 170 && C.tl[1] > 170 && C.tl[2] > 170 && C.tr[0] > 150 && C.tr[1] < 100 && C.br[2] > 150 && C.br[0] < 100 && C.bl[1] > 150 && C.bl[0] < 100;
      check('still person: corner markers in place (picture neither flipped nor mirrored)', upright, JSON.stringify(C));
      var o = E.other, greyOK = o.spread <= 10;
      check('still other: comes out grey', greyOK, 'largest gap between channels ' + o.spread);
      var bR = lumOf(E.bee.patches.red), pR = lumOf(person.patches.red);
      check('still bee: red patch turns dark', bR < .5 * pR, 'red patch luminance ' + r2(bR) + ' against ' + r2(pR) + ' for a person');
      var dP = linDist(person.patches.red, person.patches.green);
      TWO_CONE.forEach(function (k) {
        var d = linDist(E[k].patches.red, E[k].patches.green);
        check('still ' + k + ': red and green pulled together', d < .8 * dP, 'distance ' + r2(d) + ' against ' + r2(dP) + ' for a person');
      });
      var fineP = (person.grat.v2 + person.grat.h2) / 2;
      ORDER.forEach(function (k) {
        if (!(EYES[k].cpd < HUMAN_CPD)) return;
        var f = (E[k].grat.v2 + E[k].grat.h2) / 2;
        check('still ' + k + ': finest grating keeps less contrast than for a person', f < .9 * fineP, 'contrast ' + r2(f) + ' against ' + r2(fineP));
      });
      T.ms.still = since();
      post();
    }
    function markTile(k) { var f = sheet.querySelector('figure[data-key="' + k + '"] figcaption'); if (f) f.className = 'no'; }

    // ---- 3. moving pictures, from a canvas and from a video
    var mcv = makeCanvas(1280, 720), mx = mcv.getContext('2d'), mbase = null, freshV = false, lastVT = -1, vidOK = false;
    function paintMotion(now) {
      var t = now / 1000;
      if (!mbase) mbase = drawCard(1280, 720).c;
      mx.drawImage(mbase, 0, 0);
      mx.fillStyle = '#ffffff'; mx.fillRect(((t * 420) % 1400) - 80, 300, 80, 80);
      mx.fillStyle = '#e33b2e'; mx.beginPath(); mx.arc(640 + 420 * Math.sin(t * 2.7), 520, 44, 0, 7); mx.fill();
    }
    function watchVideo() {
      if (!vid.requestVideoFrameCallback) return;
      (function again() { vid.requestVideoFrameCallback(function () { freshV = true; if (S.selftest) again(); }); })();
    }
    // the clip goes in as a blob address, as a clip the person picks does (startClip), and so needs no byte ranges from the server
    function loadClip(url) {
      return fetch(url).then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.blob(); }).then(function (b) {
        return new Promise(function (res, rej) {
        var done = false, to = setTimeout(function () { if (!done) { done = true; rej(new Error('no data within 8 s')); } }, 8000);
        vid.onloadeddata = function () { if (!done) { done = true; clearTimeout(to); res(); } };
        vid.onerror = function () { if (!done) { done = true; clearTimeout(to); rej(new Error('error ' + (vid.error && vid.error.code))); } };
        vid.loop = true; vid.muted = true; vid.playsInline = true; vid.setAttribute('playsinline', ''); vid.src = URL.createObjectURL(b);
        try { vid.load(); } catch (e) {}
        });
      }).then(function () { return vid.play(); });
    }
    async function startVideo() {
      var M = T.motion.video = { tried: [] }, order = vid.canPlayType('video/mp4; codecs="avc1.42E01E"') ? ['mp4', 'webm'] : ['webm', 'mp4'];
      for (var i = 0; i < order.length && !vidOK; i++) {
        try { await loadClip('test/assets/motion.' + order[i]); vidOK = true; M.used = order[i]; M.tried.push(order[i] + ': playing'); }
        catch (e) { M.tried.push(order[i] + ': ' + String(e && e.message || e).slice(0, 80)); }
      }
      check('video: a test clip plays', vidOK, M.tried.join('; '));
      if (vidOK) { M.size = vid.videoWidth + 'x' + vid.videoHeight; watchVideo(); }
    }
    // The clip has red in its top left corner and blue in its bottom right, in every frame. The check judges a picture made only of
    // the clip's own frames. One upload from a video element is not enough: before the element has a frame for WebGL, texImage2D can
    // leave the texture as it was (Chromium kept the still phase's test card: tl [192,192,192], br [38,38,192], read on a phone in
    // Ecosia and on a build machine, run engines/11) or make it black (WebKit on macOS, run engines/12). So it waits for the element's
    // first frame callback, then uploads every new frame until four have gone in (the ring has then taken two), and reads the picture
    // through the human eye, which has no time effects (no persistence, hold or slowed rate), so it shows the last frame uploaded.
    // The reading after the first upload is kept as `first`, as evidence of the race; it is not judged.
    function videoUpright() {
      function corners() {
        var vw = vid.videoWidth, vh = vid.videoHeight;
        engine.draw(HUMAN, STEADY, performance.now(), 16);
        var rc = makeCanvas(vw, vh), rx = rc.getContext('2d', { willReadFrequently: true }); rx.drawImage(canvas, 0, 0);
        var img = rx.getImageData(0, 0, vw, vh), s = Math.round(vh * .1);
        return { tl: rgb(stats(img, vw, { x0: 2, y0: 2, x1: s, y1: s }).rgb), br: rgb(stats(img, vw, { x0: vw - s, y0: vh - s, x1: vw - 2, y1: vh - 2 }).rgb) };
      }
      var firstFrame = vid.requestVideoFrameCallback ? new Promise(function (res) { var t = setTimeout(res, 1500); vid.requestVideoFrameCallback(function () { clearTimeout(t); res(); }); }) : wait(300);
      return firstFrame.then(function () { return new Promise(function (done) {
        var t0 = performance.now(), fresh = 0, first = null;
        sizeCanvas(vid.videoWidth, vid.videoHeight);
        (function step() {
          if (vid.readyState >= 2 && vid.videoWidth) {
            var isNew = vid.requestVideoFrameCallback ? freshV : vid.currentTime !== lastVT;
            if (isNew || fresh === 0) { freshV = false; lastVT = vid.currentTime; engine.setFrame(vid, vid.videoWidth, vid.videoHeight, performance.now()); fresh++; if (fresh === 1) first = corners(); }
          }
          if (fresh < 4 && performance.now() - t0 < 4000) { requestAnimationFrame(step); return; }
          var last = corners(), st = engine.state();
          done({ tl: last.tl, br: last.br, err: st.err, fresh: fresh, writes: st.writes, ms: Math.round(performance.now() - t0), first: first });
        })();
      }); });
    }
    // what the video element delivers over a while: frame callbacks, and changes of currentTime
    function videoProbe(ms) {
      return new Promise(function (done) {
        var cb = 0, ct = 0, last = vid.currentTime, t0 = performance.now(), on = true;
        if (vid.requestVideoFrameCallback) (function again() { vid.requestVideoFrameCallback(function () { cb++; if (on) again(); }); })();
        (function tick() {
          if (vid.currentTime !== last) { ct++; last = vid.currentTime; }
          if (performance.now() - t0 < ms) { requestAnimationFrame(tick); return; }
          on = false; done({ callbacks: cb, timeChanges: ct, paused: vid.paused, time: r2(vid.currentTime), ready: vid.readyState });
        })();
      });
    }
    async function videoProbes() {        // the page's own video element as the app styles it (2 px, transparent), then shown
      var P = T.motion.videoProbe = {};
      P.asStyled = await videoProbe(1500);
      var app = $('app'), keepApp = app.style.cssText, keepVid = vid.style.cssText;
      app.style.zIndex = '70'; app.style.background = 'transparent'; app.style.pointerEvents = 'none';
      vid.style.cssText = 'position:fixed;right:8px;bottom:8px;width:160px;height:90px;opacity:1';
      if (vid.paused) { try { await vid.play(); } catch (e) { P.replay = String(e).slice(0, 80); } }
      P.shown = await videoProbe(1500);
      app.style.cssText = keepApp; vid.style.cssText = keepVid;
      P.afterwards = await videoProbe(1000);
    }
    function run(eye, kind, ms) {
      return new Promise(function (done) {
        var P = paramsOf(EYES[eye]), t0 = null, last = 0, dts = [], cpu = [], n = 0, fresh = 0, w0 = null, wGot = 0, errAny = 0;
        function step(now) {
          if (t0 === null) t0 = now;
          var c0 = performance.now();
          if (kind === 'canvas') { paintMotion(now); engine.setFrame(mcv, mcv.width, mcv.height, now); fresh++; }
          else if (vid.readyState >= 2 && vid.videoWidth) {
            var isNew = vid.requestVideoFrameCallback ? freshV : vid.currentTime !== lastVT;
            if (isNew || fresh === 0) { freshV = false; lastVT = vid.currentTime; engine.setFrame(vid, vid.videoWidth, vid.videoHeight, now); fresh++; }
          }
          // state() reads the GL error flag, which waits for the graphics chip, so it is read only after the first frame
          // (where a change of size starts the ring again) and at the end; an error flag stays set until it is read
          if (fresh && w0 === null) { var s0 = engine.state(); w0 = s0.writes; errAny = s0.err; }
          engine.draw(P, STEADY, now, last ? Math.min(100, now - last) : 16);
          cpu.push(performance.now() - c0);
          if (last) dts.push(now - last);
          last = now; n++;
          if ((now - t0 < ms || n < 3 || fresh < 3) && now - t0 < 3000) { requestAnimationFrame(step); return; }   // the ring takes every second frame, so three new frames always write one
          var st = engine.state(), d = dts.slice(1), c = cpu.slice(1); wGot = w0 === null ? 0 : st.writes - w0;
          function mean(a) { if (!a.length) return null; var s = 0; a.forEach(function (v) { s += v; }); return Math.round(s / a.length * 10) / 10; }
          function worst(a) { return a.length ? Math.round(Math.max.apply(null, a) * 10) / 10 : null; }
          done({ frames: n, fresh: fresh, writes: wGot, err: errAny || st.err, paused: kind === 'video' ? vid.paused : undefined, ms: mean(d), worst: worst(d), cpu: mean(c), cpuWorst: worst(c), first: dts.length ? Math.round(dts[0]) : null, size: canvas.width + 'x' + canvas.height, ring: st.sw + 'x' + st.sh });
        }
        requestAnimationFrame(step);
      });
    }
    async function motionPhase() {
      phase('motion', 'Moving pictures.');
      var side0 = engine.side(), sizes = [['default', side0], ['540', 540]];
      T.motion.side0 = side0; T.motion.runs = {};
      await startVideo();
      if (vidOK) {
        var up = T.motion.videoUpright = await videoUpright();
        check('video: picture upright (red corner top left, blue bottom right)', up.tl[0] > 140 && up.tl[2] < 110 && up.br[2] > 140 && up.br[0] < 110, JSON.stringify(up));
      }
      if (vidOK) { stLine.textContent = 'Watching what the video element delivers.'; await videoProbes(); }
      for (var s = 0; s < sizes.length; s++) {
        engine.setSide(sizes[s][1]); fullSize();
        for (var e = 0; e < MOVERS.length; e++) {
          var kinds = vidOK ? ['canvas', 'video'] : ['canvas'];
          for (var k = 0; k < kinds.length; k++) {
            var name = sizes[s][0] + ' ' + MOVERS[e] + ' ' + kinds[k];
            stLine.textContent = 'Moving pictures: ' + MOVERS[e] + ' from a ' + kinds[k] + ', picture size ' + sizes[s][0] + ' (' + engine.side() + ').';
            var r = T.motion.runs[name] = await run(MOVERS[e], kinds[k], 600);
            check('motion ' + name + ': frames advance', r.writes > 0, r.writes + ' ring writes from ' + r.fresh + ' new frames');
            check('motion ' + name + ': no GL error', r.err === 0, 'error 0x' + (r.err || 0).toString(16));
          }
        }
      }
      engine.setSide(side0);
      try { vid.pause(); } catch (e) {}
      T.ms.motion = since();
      post();
    }

    // ---- 4. the change of eyes, held still with the page's own pose(t) hook and drawn by the page's own loop
    async function posePhase() {
      phase('pose', 'The change of eyes, held at three instants.');
      stage.classList.add('full'); stage.style.width = ''; stage.style.height = '';
      var dpr = Math.min(window.devicePixelRatio || 1, 2), w = innerWidth * dpr, h = innerHeight * dpr, k = Math.min(1, engine.side() / Math.max(w, h));
      var card = drawCard(Math.round(w * k), Math.round(h * k));
      showStill(card.c, true);
      var rc = makeCanvas(2, 2), rx = rc.getContext('2d', { willReadFrequently: true });
      S.selftest = false;                               // from here the app's own loop draws
      var plan = [['cat', 'slit pupil'], ['bee', 'mosaic']];
      for (var i = 0; i < plan.length; i++) {
        setEyes(plan[i][0], null); go('animal');
        for (var j = 0; j < 3; j++) {
          var t = [.2, .45, .8][j];
          window.__seenBack.pose(t);
          cap.textContent = 'Change of eyes: ' + plan[i][0] + ' (' + (calm ? 'reduced motion asked for, so no ' + plan[i][1] : plan[i][1]) + '), held at t = ' + t.toFixed(2);
          T.posing = plan[i][0] + '@' + t;
          var h0 = performance.now(), seen = 0, lastSeen = S.lastNow;
          while (performance.now() - h0 < 900 || (seen < 3 && performance.now() - h0 < 6000)) {   // on a slow renderer, hold until the page has drawn it a few times
            await frame(); if (S.lastNow !== lastSeen) { seen++; lastSeen = S.lastNow; }
          }
          var got = await new Promise(function (done) {
            requestAnimationFrame(function () {         // drawn and read back in one go, as the page's own snapshot does
              var now = performance.now(), fx = fxNow(now, 0);
              engine.draw(mix(HUMAN, S.eyes ? paramsOf(EYES[S.eyes]) : HUMAN, S.k), fx, now, 16);   // the eye setEyes chose, as the page's eyeP holds it
              var err = engine.state().err;
              rc.width = canvas.width; rc.height = canvas.height; rx.drawImage(canvas, 0, 0);
              var wh = whole(rx.getImageData(0, 0, rc.width, rc.height), rc.width, rc.height);
              done({ eye: plan[i][0], t: t, k: r2(S.k), ap: r2(fx.ap), mosaic: r2(fx.mosaic), err: err, dark: r2(wh.dark), mean: Math.round(wh.mean), size: canvas.width + 'x' + canvas.height });
            });
          });
          T.pose.push(got);
          check('pose ' + got.eye + ' at ' + t + ': no GL error', got.err === 0, 'error 0x' + (got.err || 0).toString(16));
          await wait(300);
        }
      }
      window.__seenBack.pose(null); S.selftest = true; T.posing = null; cap.textContent = '';
      stage.classList.remove('full'); stage.hidden = true;
      T.ms.pose = since();
    }

    // ---- 5. the report, ending on the contact sheet
    function finish() {
      T.done = true; T.ok = T.fails.length === 0; T.ms.total = since(); T.phase = 'done';
      stLine.textContent = 'Finished in ' + (T.ms.total / 1000).toFixed(1) + ' s. ' + (T.env.renderer ? 'Renderer: ' + (T.env.unmaskedRenderer || T.env.renderer) + '.' : '');
      stSum.innerHTML = '';
      var b = el('b', '', T.ok ? 'All ' + T.checks + ' checks passed.' : T.fails.length + ' of ' + T.checks + ' checks failed.', stSum); b.className = T.ok ? 'ok' : 'no';
      if (!T.ok) { var ul = el('ul', '', undefined, stSum); T.fails.slice(0, 12).forEach(function (f) { el('li', '', f, ul); }); if (T.fails.length > 12) el('li', '', 'and ' + (T.fails.length - 12) + ' more', ul); }
      stBtns.hidden = false;
      var E = T.env, rows = [['Browser', E.ua], ['Screen', E.viewport + ' at ' + E.dpr + 'x'], ['WebGL 2', E.webgl2 ? 'yes' : 'no ' + (E.engineError || '')],
        ['Renderer', (E.unmaskedRenderer || E.renderer || '') + ' / ' + (E.unmaskedVendor || E.vendor || '')], ['Float targets', String(E.floatOK)],
        ['Largest texture', E.maxTexture + ', ' + E.maxLayers + ' layers'], ['Typeface loaded', String(E.serif)], ['Video', JSON.stringify(E.canPlay) + (T.motion.video ? ' used ' + T.motion.video.used : '')],
        ['Recorder', (E.recorder || []).join(', ') || 'none'], ['Share files', String(E.shareFiles)]];
      var tb = el('table', '', undefined, details);
      rows.forEach(function (r) { var tr = el('tr', '', undefined, tb); el('th', '', r[0], tr); el('td', '', r[1], tr); });
      if (T.motion.runs) {
        var mt = el('table', '', undefined, details), hr = el('tr', '', undefined, mt);
        ['moving picture', 'ms per frame', 'worst', 'ring writes', 'size'].forEach(function (h) { el('th', '', h, hr); });
        Object.keys(T.motion.runs).forEach(function (k) { var r = T.motion.runs[k], tr = el('tr', '', undefined, mt); [k, r.ms, r.worst, r.writes, r.size].forEach(function (v) { el('td', '', String(v), tr); }); });
      }
      if (T.rec) {
        var rt = el('table', '', undefined, details), rh = el('tr', '', undefined, rt);
        el('caption', 'text-align:left;padding:0 0 4px', 'Recognizer ' + (T.rec.about ? (T.rec.about.model || '') + ', ' + (T.rec.about.backend || '') : '') + (T.rec.readyMs !== undefined ? ', ready in ' + T.rec.readyMs + ' ms' : '') + (T.rec.error ? ': ' + T.rec.error.sentence : ''), rt);
        ['photo', 'kinds (page)', 'Python', 'ms (prepare + run)'].forEach(function (h) { el('th', '', h, rh); });
        T.rec.photos.forEach(function (x) { var tr = el('tr', '', undefined, rt); [x.name, x.error ? x.error.sentence : (x.head3 || []).map(function (k) { return k[0] + ' ' + k[1]; }).join(', '), x.python3 ? x.python3[0][0] + (x.match ? ' (same)' : ' (differs)') : '', x.ms ? x.ms.pre + ' + ' + x.ms.run : ''].forEach(function (v) { el('td', '', String(v), tr); }); });
      }
      el('pre', '', JSON.stringify(T), details);
      ta.value = JSON.stringify(T);
      root.scrollTop = 0;
    }

    async function main() {
      await frame();
      await envPhase();
      if (param('rec')) { try { await recPhase(); } catch (e) { check('rec phase ran', false, String(e && e.stack || e).slice(0, 300)); } }
      if (engine) {
        try { await stillPhase(); } catch (e) { check('still phase ran', false, String(e && e.stack || e).slice(0, 300)); }
        try { await motionPhase(); } catch (e) { check('motion phase ran', false, String(e && e.stack || e).slice(0, 300)); }
        try { await posePhase(); } catch (e) { S.selftest = true; check('pose phase ran', false, String(e && e.stack || e).slice(0, 300)); }
      }
      finish();
      post();
    }
    main().catch(function (e) { check('self-test ran', false, String(e && e.stack || e).slice(0, 300)); finish(); post(); });
  })();
})(window.__seenBackSelftest);
