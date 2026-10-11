// Runs the page's own worker (vendor/rec-worker.js) unchanged, after wrapping WebAssembly.Memory so that every message
// the worker sends carries the size of the runtime's WASM heap (bytes; it only grows).
var __mems = [];
(function () {
  var Orig = WebAssembly.Memory;
  WebAssembly.Memory = new Proxy(Orig, { construct: function (t, a) { var m = new t(a[0]); __mems.push(m); return m; } });
  var oi = WebAssembly.instantiate;
  WebAssembly.instantiate = function () {
    return oi.apply(this, arguments).then(function (r) {
      try { var ex = (r.instance || r).exports, k; for (k in ex) if (ex[k] instanceof Orig && __mems.indexOf(ex[k]) < 0) __mems.push(ex[k]); } catch (e) {}
      return r;
    });
  };
  var post = self.postMessage.bind(self);
  self.postMessage = function (msg, tr) {
    try { if (msg && typeof msg === 'object') msg.heap = __mems.reduce(function (s, m) { return Math.max(s, m.buffer.byteLength); }, 0); } catch (e) {}
    return tr ? post(msg, tr) : post(msg);
  };
})();
importScripts('/vendor/rec-worker.js');
