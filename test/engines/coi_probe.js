// The threads experiment's probe, added to index.html by test/engines/coi_serve.js when the address has probe=1. It runs inside the
// real page: waits until the service worker controls the page (reloading at most three times), then reads crossOriginIsolated, waits
// for the recognizer, puts the photos through it `rounds` times, tries what isolation might break, and posts everything to
// /report/<name> on the page's own server. Address parts: name, threads, want=coi, photos=a,b,c, rounds, x=<the other origin>, cam=1.
(function () {
  var q = new URLSearchParams(location.search), name = q.get('name') || 'probe', R = { name: name, href: location.href, ua: navigator.userAgent, steps: [] };
  window.__probe = R;
  function post(final) { R.done = !!final; return fetch('/report/' + name, { method: 'POST', body: JSON.stringify(R) }).catch(function () {}); }
  function wait(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function within(ms, p) { return Promise.race([p, wait(ms).then(function () { return { timeout: ms }; })]); }
  async function run() {
    if (document.readyState !== 'complete') await new Promise(function (r) { addEventListener('load', r); });
    var key = 'probe-reloads-' + name, n = +(sessionStorage.getItem(key) || 0);
    var sw = navigator.serviceWorker;
    if (sw && n < 3 && (!sw.controller || (q.get('want') === 'coi' && !self.crossOriginIsolated))) {
      sessionStorage.setItem(key, n + 1); R.steps.push('reload ' + (n + 1) + ': controlled ' + !!sw.controller + ', isolated ' + !!self.crossOriginIsolated); post(false);
      await within(20000, sw.ready); await wait(1000); location.reload(); return 'reloading';
    }
    R.reloads = n; R.controlled = !!(sw && sw.controller); R.coi = !!self.crossOriginIsolated; R.sab = typeof SharedArrayBuffer; R.cores = navigator.hardwareConcurrency;
    var rec = window.__seenBack && window.__seenBack.rec; if (!rec) throw new Error('no recognizer on this page');
    var t = performance.now(), ok = await rec.ready().then(function () { return 'ready'; }, function (e) { return 'failed: ' + (e && e.code) + ' ' + (e && (e.sentence || e.detail || e.message)); });
    R.ready = ok; R.readyMs = Math.round(performance.now() - t); R.about = rec.about(); post(false);
    if (ok === 'ready') {
      var list = (q.get('photos') || '').split(',').filter(Boolean), rounds = +(q.get('rounds') || 3), pics = [];
      for (var i = 0; i < list.length; i++) {
        var blob = await (await fetch(list[i])).blob(), file = new File([blob], list[i].split('/').pop(), { type: blob.type });
        var bmp = await createImageBitmap(file), c = document.createElement('canvas'); c.width = bmp.width; c.height = bmp.height; c.getContext('2d').drawImage(bmp, 0, 0); pics.push([c, file]);
      }
      R.photos = [];
      for (var r = 0; r < rounds; r++) for (var j = 0; j < pics.length; j++) {
        var t1 = performance.now(), x = await rec.recognize(pics[j][0], pics[j][1]);
        R.photos.push({ round: r, name: pics[j][1].name, kind: x.kind, p: +x.kinds[0].p.toFixed(3), sp: x.species[0] ? x.species[0].sci : null, ms: x.ms, wall: Math.round(performance.now() - t1) });
      }
      R.about2 = rec.about();
    }
    post(false);
    // what isolation might break
    var B = R.breaks = {}, X = q.get('x');
    if (X) {
      B.corsFetch = await within(10000, fetch(X + '/test/rec/photos/heron.png', { mode: 'cors' }).then(function (r) { return r.arrayBuffer().then(function (a) { return 'ok ' + r.status + ' ' + a.byteLength; }); }, function (e) { return 'failed: ' + e; }));
      B.noCorsFetch = await within(10000, fetch(X + '/test/rec/photos/heron.png', { mode: 'no-cors' }).then(function (r) { return 'ok ' + r.type; }, function (e) { return 'failed: ' + e; }));
      B.img = await within(10000, new Promise(function (res) { var im = new Image(); im.onload = function () { res('loaded ' + im.naturalWidth); }; im.onerror = function () { res('error'); }; im.src = X + '/test/rec/photos/heron.png?img'; }));
    }
    B.rawGithub = await within(15000, fetch('https://raw.githubusercontent.com/jampotful/seen-back/main/manifest.webmanifest', { mode: 'cors' }).then(function (r) { return r.text().then(function (s) { return 'ok ' + r.status + ' ' + s.length + ' acao=' + r.headers.get('access-control-allow-origin'); }); }, function (e) { return 'failed: ' + e; }));
    B.worker = await within(10000, new Promise(function (res) { try { var w = new Worker(URL.createObjectURL(new Blob(['postMessage(self.crossOriginIsolated)'], { type: 'text/javascript' }))); w.onmessage = function (e) { res('ok, isolated inside: ' + e.data); w.terminate(); }; w.onerror = function (e) { res('error ' + (e && e.message)); }; } catch (e) { res('threw ' + e); } }));
    B.webgl = (function () { try { var g = document.createElement('canvas').getContext('webgl2') || document.createElement('canvas').getContext('webgl'); return g ? 'ok' : 'none'; } catch (e) { return 'threw ' + e; } })();
    if (q.get('cam') === '1' && navigator.mediaDevices) {
      B.camera = await within(8000, navigator.mediaDevices.getUserMedia({ video: true }).then(function (s) { var tr = s.getVideoTracks()[0], l = tr ? tr.label : ''; s.getTracks().forEach(function (k) { k.stop(); }); return 'ok ' + l; }, function (e) { return 'refused: ' + e.name; }));
    } else B.camera = 'not tried';
    B.opener = typeof window.opener;
  }
  run().then(function (v) { if (v !== 'reloading') post(true); }, function (e) { R.error = String((e && (e.sentence || e.message)) || e); post(true); });
})();
