// Run inside the live page (https://jampotful.github.io/seen-back/) by test/engines/big.js, through Playwright or WebDriver alike.
// window.__bigRun('get', opts) gets the larger model through the page's own offer and consent sheet, waits until it is ready,
// and puts photos through it; window.__bigRun('again', opts) is for a later visit: is it still kept, is anything fetched again,
// and does it answer a photo. Everything is written into window.__big, which the caller reads until done is true.
// opts: { offerPhotos: [{name, type, b64}], photos: [{name, type, b64, truth}], limitMs }
(function () {
  if (window.__bigRun) return;
  var W = window;
  function now() { return Math.round(performance.now()); }
  function sleep(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function $(id) { return document.getElementById(id); }
  function vis(id) { var e = $(id); return !!e && !e.hidden && e.offsetParent !== null; }
  function txt(id) { var e = $(id); return e ? e.textContent : null; }
  async function until(fn, ms, every) { var t0 = Date.now(); for (;;) { var v = null; try { v = fn(); } catch (e) { v = null; } if (v) return v; if (Date.now() - t0 > ms) return null; await sleep(every || 200); } }
  function noCamera() {
    if (!navigator.mediaDevices) return; var no = function () { return Promise.reject(new DOMException('Permission denied', 'NotAllowedError')); };
    try { navigator.mediaDevices.getUserMedia = no; } catch (e) {}
    [navigator.mediaDevices, W.MediaDevices && MediaDevices.prototype].forEach(function (o) { if (o) try { Object.defineProperty(o, 'getUserMedia', { value: no, configurable: true, writable: true }); } catch (e) {} });
  }
  async function est() { try { var e = await navigator.storage.estimate(); return { usage: e.usage, quota: e.quota, details: e.usageDetails || null }; } catch (e) { return { error: String(e) }; } }
  async function persisted() { try { return navigator.storage && navigator.storage.persisted ? await navigator.storage.persisted() : 'no persisted()'; } catch (e) { return 'error ' + e; } }
  async function cachesNow() {
    var o = {};
    if (W.__bigNoCaches) return { skipped: 'NOCACHES: WebKit reads a kept body into the page on every match' };
    try {
      var ks = await caches.keys();
      for (var i = 0; i < ks.length; i++) {
        var c = await caches.open(ks[i]), q = await c.keys(), bytes = 0, big = [];
        for (var j = 0; j < q.length; j++) {
          var res = await c.match(q[j]), len = res ? +(res.headers.get('Content-Length') || 0) : 0; bytes += len;
          if (/naturalist/.test(q[j].url)) big.push(q[j].url.replace(location.origin, '').replace(/[0-9a-f]{64}/, function (h) { return h.slice(0, 12); }) + ' ' + (res && res.headers.get('Content-Length') ? len : 'no length'));
        }
        o[ks[i]] = { entries: q.length, bytesByHeader: bytes, naturalist: big };
      }
    } catch (e) { o.error = String(e); }
    return o;
  }
  function res() {
    try {
      return performance.getEntriesByType('resource').filter(function (e) { return /githubusercontent\.com|models\/naturalist/.test(e.name); }).map(function (e) {
        return { name: e.name.replace(/^https:\/\/[^/]+\//, '').replace(/[0-9a-f]{40}/, 'COMMIT'), start: Math.round(e.startTime), ms: Math.round(e.duration), transfer: e.transferSize, encoded: e.encodedBodySize, decoded: e.decodedBodySize, proto: e.nextHopProtocol, status: e.responseStatus, init: e.initiatorType };
      });
    } catch (e) { return [{ error: String(e) }]; }
  }
  function bigNow() { var B = W.__seenBack, a = B.big.about(); return { have: a.have, kept: a.keptBytes, bytes: a.bytes, state: a.state, why: a.why, fail: a.fail, getFail: a.getFail, choice: B.bigChoice(), model: a.model, backend: a.backend, threads: a.threads, loadMs: a.loadMs, start: a.start }; }
  function bigLast() { var l = W.__seenBack.big.about().last; return l ? { kind: l.kind, kindP: l.kindP != null ? +(+l.kindP).toFixed(3) : null, sure: l.sure, named: l.named ? (l.named.en || '') + ' | ' + l.named.sci : '', top3: (l.species || []).slice(0, 3).map(function (x) { return [x.sci, x.en || '', +(+x.p).toFixed(3)]; }), ms: l.ms } : null; }
  function smallLast() { var l = W.__seenBack.rec.about().last; return l ? { kind: l.kind, kindP: l.kindP != null ? +(+l.kindP).toFixed(3) : null, named: l.named ? (l.named.en || '') + ' | ' + l.named.sci : '', top: l.species && l.species[0] ? [l.species[0].sci, +(+l.species[0].p).toFixed(3)] : null, ms: l.ms } : null; }
  function st() { var b = W.__seenBack; return { screen: b.S.screen, eyes: b.S.eyes, named: b.S.named ? b.S.named.common + ' | ' + b.S.named.scientific + ' | ' + b.S.named.by : null, claim: vis('claim'), svc: b.S.svc ? b.S.svc.state : null, line: vis('svcView') ? txt('svcView') : vis('svcHud') ? txt('svcHud') : '' }; }
  function fileOf(p) { var bin = atob(p.b64), u = new Uint8Array(bin.length); for (var i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i); return new File([u], p.name, { type: p.type }); }
  function diagOf(re) { try { return W.__seenBack.diag().filter(function (d) { return re.test(d.what); }).slice(-20).map(function (d) { return Math.round(d.at) + ' ' + d.what + ' ' + String(d.code).slice(0, 200); }); } catch (e) { return [String(e)]; } }
  async function toAsk() {
    if (vis('askAnimal')) return true;
    if (st().claim && $('claimBack')) { $('claimBack').click(); await sleep(250); }
    if (st().screen === 'askView' && $('backAskView')) { $('backAskView').click(); await sleep(250); }
    if (st().screen === 'naming') { history.back(); await sleep(400); }
    if (st().screen === 'intro') { noCamera(); $('btnBegin').click(); }
    return !!(await until(function () { return vis('askAnimal'); }, 10000));
  }
  async function choose(p) {
    var B = W.__seenBack, ph0 = B.S.animalPhoto, inp = $('inAnimalPick'), dt = new DataTransfer(); dt.items.add(fileOf(p)); inp.files = dt.files; inp.dispatchEvent(new Event('change', { bubbles: true }));
    return !!(await until(function () { return B.S.animalPhoto && B.S.animalPhoto !== ph0 && (B.S.eyes || vis('claim')); }, 90000, 100));
  }
  async function onePhoto(p, limitMs) {      // a photo chosen; the small model's answer; then the larger model's, if it looks at it
    var B = W.__seenBack, ok = await toAsk(), prev = B.big.about().last, t0 = now();
    var chosen = ok && await choose(p), tSmall = now(), sm = smallLast(), s1 = st(), got = null;
    if (chosen && s1.eyes && s1.eyes !== 'person') got = await until(function () { var l = B.big.about().last; return l && l !== prev ? l : null; }, limitMs || 240000, 100);
    var t1 = now(); await sleep(400);
    return { name: p.name, truth: p.truth || '', toAsk: ok, chosen: chosen, small: sm, smallMs: tSmall - t0, large: got ? bigLast() : null, wallMs: got ? t1 - t0 : null, afterSmallMs: got ? t1 - tSmall : null, st: st(), big: bigNow(), fail: got ? '' : diagOf(/^large-none|^large-get/).slice(-2) };
  }
  async function pageUp(R) {
    if (!(await until(function () { return W.__seenBack && W.__seenBack.rec && W.__seenBack.big; }, 60000))) throw new Error('the page did not start in 60 s: ' + document.title + ' | ' + (document.body ? document.body.innerText.slice(0, 200) : ''));
    var B = W.__seenBack, t0 = now();
    R.pocketReady = await Promise.race([B.rec.ready().then(function () { return 'ready'; }, function (e) { return 'failed ' + (e && e.code); }), sleep(150000).then(function () { return 'still waiting after 150 s'; })]);
    R.pocketReadyMs = now() - t0; R.pocketAt = now();
    R.controlled = !!(navigator.serviceWorker && navigator.serviceWorker.controller); R.online = navigator.onLine;
    R.build = B.about ? B.about().split('\n')[0] : ''; R.ua = navigator.userAgent;
    R.jsHeap = performance.memory ? { used: performance.memory.usedJSHeapSize, limit: performance.memory.jsHeapSizeLimit } : null;
    return B;
  }
  async function phaseGet(o, R) {
    try { performance.setResourceTimingBufferSize(2000); } catch (e) {}
    var B = await pageUp(R);
    R.before = { estimate: await est(), persisted: await persisted(), caches: await cachesNow(), big: bigNow() };
    noCamera(); R.steps.push(now() + ' begin'); R.begun = await toAsk();
    var offered = false; R.offerTried = [];
    for (var i = 0; i < o.offerPhotos.length && !offered; i++) {
      var p = o.offerPhotos[i]; await toAsk(); var c = await choose(p);
      offered = !!(await until(function () { return vis('svcView') && B.S.svc && B.S.svc.state === 'get'; }, 12000));
      R.offerTried.push({ name: p.name, chosen: c, st: st(), small: smallLast() });
    }
    if (offered) { R.path = 'the offer under the photo'; R.offerLine = txt('svcView'); $('svcView').click(); }
    else {                                     // the About block's own button
      R.path = 'the About block';
      if (st().screen === 'askView' && $('backAskView')) { $('backAskView').click(); await sleep(300); }
      if ($('recAskAnimal')) $('recAskAnimal').click(); await until(function () { return vis('record'); }, 5000);
      if (!$('about').open) { $('about').querySelector('summary').click(); } await sleep(500);
      if (vis('bigGet')) $('bigGet').click(); else R.path += ' (no Get button visible)';
    }
    var sheet = await until(function () { return vis('big'); }, 10000);
    R.sheet = sheet ? { title: txt('bigTitle'), sub: txt('bigSub'), net: txt('bigNet'), yes: txt('bigYes') } : null;
    R.tYes = now(); R.epochYes = Date.now();
    if (sheet) $('bigYes').click(); else { R.error = 'the consent sheet did not open'; return; }
    R.steps.push(now() + ' yes');
    var samples = [], lastKept = -1, lastLine = '', tDown = 0, tReady = 0; R.lines = [];
    for (;;) {
      var b = bigNow(), t = now(), line = st().line;
      if (b.kept !== lastKept) { samples.push([t - R.tYes, b.kept]); lastKept = b.kept; }
      if (line && line !== lastLine) { if (R.lines.length < 40 || !/^Getting the larger model/.test(line)) R.lines.push((t - R.tYes) + ' ' + line); lastLine = line; }
      if (!tDown && b.bytes && b.kept >= b.bytes) { tDown = t; R.epochDown = Date.now(); }
      if (b.have === 'kept' && b.state === 'ready') { tReady = t; R.epochReady = Date.now(); break; }
      if (b.have !== 'getting' && b.getFail) { R.getFail = b.getFail; break; }
      if (t - R.tYes > (o.limitMs || 900000)) { R.getFail = 'still getting after ' + (o.limitMs || 900000) + ' ms'; break; }
      await sleep(250);
    }
    var step = Math.max(1, Math.ceil(samples.length / 60));
    R.download = { downloadMs: tDown ? tDown - R.tYes : null, readyMs: tReady ? tReady - R.tYes : null, afterDownloadMs: tDown && tReady ? tReady - tDown : null,
      samples: samples.filter(function (x, k) { return k % step === 0 || k === samples.length - 1; }), big: bigNow(), diag: diagOf(/^large/) };
    R.resources = res();
    R.after = { estimate: await est(), persisted: await persisted(), caches: await cachesNow() };
    R.steps.push(now() + ' ready ' + !!tReady); R.wm = (W.__wm || []).slice();
    if (!tReady) return;
    // the photo in hand is looked at as soon as the model is ready
    var g0 = /offer/.test(R.path) && B.S.eyes ? await until(function () { var l = B.big.about().last; return l ? l : null; }, 120000, 100) : null;
    R.photo0 = { at: now() - tReady, large: g0 ? bigLast() : null, st: st() }; R.epochPhotos = Date.now();
    R.photos = [];
    for (var k = 0; k < o.photos.length; k++) { R.photos.push(await onePhoto(o.photos[k], 240000)); R.steps.push(now() + ' photo ' + o.photos[k].name); }
    R.epochPhotosEnd = Date.now(); R.end = { big: bigNow(), estimate: await est(), diag: diagOf(/^large/) };
    R.wm = (W.__wm || []).slice();                // webkitmem trial: the marks of each step of the larger model's load
  }
  async function phaseAgain(o, R) {
    try { performance.setResourceTimingBufferSize(2000); } catch (e) {}
    var B = await pageUp(R);
    R.choice = B.bigChoice(); R.big0 = bigNow();
    var t0 = now(); R.survey = await Promise.race([B.big.survey(), sleep(60000).then(function () { return 'no answer in 60 s'; })]); R.surveyMs = now() - t0;
    R.big1 = bigNow(); R.estimate = await est(); R.persisted = await persisted(); R.caches = await cachesNow();
    noCamera(); R.begun = await toAsk(); R.epochPhoto = Date.now();
    R.photo = await onePhoto(o.photos[0], 300000);
    R.epochPhotoEnd = Date.now();
    R.resources = res(); R.diag = diagOf(/^large/); R.wm = (W.__wm || []).slice();
  }
  W.__bigRun = function (phase, o) {
    W.__bigNoCaches = !!(o && o.noCaches);
    var R = W.__big = { phase: phase, started: now(), done: false, steps: [] };
    (phase === 'get' ? phaseGet : phaseAgain)(o || {}, R).catch(function (e) { R.error = String(e && e.stack || e).slice(0, 600); }).then(function () { R.done = true; R.finished = now(); });
    return 'started';
  };
})();
