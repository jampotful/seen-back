// Used only by the native shells' checks (ci/native): fetch the larger model through the page's own recognizer object, as the
// consent sheet's "Get it" does (download, verify, keep, start the encoder), then name four photos with it. Progress and results go to
// window.__bigProbe, which the shell reads every three seconds. The shell injects this file when started with the extra "probe".
(function () {
  var R = window.__bigProbe = { started: new Date().toISOString(), steps: [], photos: [] };
  function now() { return Math.round(performance.now()); }
  function est() {
    return navigator.storage && navigator.storage.estimate ? navigator.storage.estimate().then(function (e) { return { usage: e.usage, quota: e.quota }; }, function () { return null; }) : Promise.resolve(null);
  }
  function img(src) { return new Promise(function (res, rej) { var i = new Image(); i.onload = function () { res(i); }; i.onerror = function () { rej(new Error('image ' + src)); }; i.src = src; }); }
  function canvasOf(i) { var c = document.createElement('canvas'); c.width = i.naturalWidth; c.height = i.naturalHeight; c.getContext('2d').drawImage(i, 0, 0); return c; }
  var B = window.__seenBack && window.__seenBack.big;
  if (!B) { R.error = 'no window.__seenBack.big'; R.done = true; return; }
  var t0 = now();
  B.progress(function () { R.line = B.line(); R.has = B.has(); R.size = B.size(); R.atMs = now() - t0; });
  est().then(function (e) { R.before = e; R.steps.push('get at ' + (now() - t0)); return B.get(); })
    .then(function () { R.gotMs = now() - t0; R.has = B.has(); R.size = B.size(); R.steps.push('kept and started at ' + R.gotMs); return est(); })
    .then(function (e) { R.after = e; var t1 = now(); return B.ready().then(function () { R.readyMs = now() - t1; R.about = B.about(); }); })
    .then(function () {
      var names = ['heron.png', 'portrait.jpg', 'garden.jpg', 'wall.png'], k = 0;
      function next() {
        if (k >= names.length) return Promise.resolve();
        var n = names[k++], t = now();
        return img('test/rec/photos/' + n).then(function (i) { return B.recognize(canvasOf(i), null); })
          .then(function (r) { R.photos.push({ name: n, ms: now() - t, answer: JSON.stringify(r).slice(0, 500) }); },
                function (e) { R.photos.push({ name: n, ms: now() - t, error: String(e && (e.code ? e.code + ': ' + e.message : e.message) || e) }); })
          .then(next);
      }
      return next();
    })
    .then(function () { R.about2 = B.about(); },
          function (e) { R.error = String(e && (e.code ? e.code + ': ' + (e.message || '') : (e.stack || e.message)) || e); R.about = B.about(); })
    .then(function () { R.done = true; R.ms = now() - t0; });
})();
