// Seen Back service worker. It keeps the app usable where there is no signal.
// The page itself is fetched fresh whenever there is a network, so a new build arrives by itself.
// Under models/, vendor/ and data/ there are two kinds of address:
//   with ?v=<version>   the file never changes under that address, so the kept copy is used first and the network only once;
//                       a new version is a new address, and so can never be hidden by an old kept copy;
//   without             (a slot's manifest.json) the network first, and the kept copy only where there is no network.
// The page itself also puts the recognizer's large files into the same store (KEEP) under the same addresses,
// so that they are kept even on a first visit, before this worker has taken charge of the page.
// Nothing kept here differs by what a request's headers say, so kept copies are looked up with ignoreVary: a host that sends
// "Vary: Accept-Encoding" (GitHub Pages does) must not make a kept copy unfindable for a request whose headers differ.
// The full database's parts come from another origin and are fetched and kept by the page alone; this worker never sees them.
const VERSION = '26';
const ORT_V = '1.30.0';                                            // the same number as ORT.v in src/cam.rec.js
const SHELL = 'shell-' + VERSION;
const KEEP = 'keep-v1';
const SHELL_FILES = ['./', 'index.html', 'manifest.webmanifest', 'icons/icon-192.png', 'icons/icon-512.png',
  'fonts/instrument-serif-latin-400-normal.woff2', 'fonts/instrument-serif-latin-400-italic.woff2',
  'fonts/dm-sans-latin-wght-normal.woff2', 'fonts/dm-sans-latin-wght-italic.woff2'];
// The small scripts the recognizer's worker is made of. The large files are fetched by the page, with a count of what has arrived.
const REC_FILES = ['vendor/rec-worker.js?v=' + VERSION, 'vendor/ort/ort.wasm.min.js?v=' + ORT_V, 'vendor/ort/ort-wasm-simd-threaded.mjs?v=' + ORT_V];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(SHELL).then((c) => c.addAll(SHELL_FILES))
      .then(() => caches.open(KEEP))
      .then((c) => Promise.all(REC_FILES.map((u) => c.match(u).then((hit) => hit || c.add(u)).catch(() => {}))))   // a missing recognizer must not stop the app from installing
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('shell-') && k !== SHELL).map((k) => caches.delete(k))))
      .then(() => caches.open(KEEP))
      .then((c) => c.keys().then((reqs) => Promise.all(reqs.map((req) => {          // scripts of an older build or an older runtime are let go
        const u = new URL(req.url), v = u.searchParams.get('v');
        const stale = (/\/vendor\/rec-worker\.js$/.test(u.pathname) && v !== VERSION) || (/\/vendor\/ort\//.test(u.pathname) && v !== ORT_V);
        return stale ? c.delete(req) : null;
      }))))
      .catch(() => {})
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;                 // anything from elsewhere goes straight to the network
  if (/\/(models|vendor|data|fonts)\//.test(url.pathname)) {
    const fixed = url.searchParams.has('v') || /\/fonts\//.test(url.pathname);
    event.respondWith(caches.open(KEEP).then((c) => {
      const fromNet = () => fetch(req).then((res) => {
        if (res.status === 200) event.waitUntil(c.put(req, res.clone()).catch(() => {}));   // kept even if the page goes away mid-download
        return res;
      });
      const keptCopy = () => c.match(req, { ignoreVary: true }).then((hit) => hit || caches.match(req, { ignoreVary: true }));   // the typeface may be in the shell's store
      if (fixed) return keptCopy().then((hit) => hit || fromNet());
      // a server or a proxy in the way answering 5xx is no better than no network: the kept copy, where there is one
      return fromNet().then((res) => res.status >= 500 ? keptCopy().then((hit) => hit || res) : res, () => keptCopy().then((hit) => hit || Response.error()));
    }, () => fetch(req)));                                         // the store will not open: the network as it is, and the page looks for kept copies by itself
    return;
  }
  const kept = () => caches.match(req, { ignoreSearch: true, ignoreVary: true }).then((hit) => hit || caches.match('index.html', { ignoreVary: true }));
  event.respondWith(                                               // the page: the network first, the kept copy when there is none
    fetch(req).then((res) => {
      if (res.ok) { const copy = res.clone(); caches.open(SHELL).then((c) => c.put(req, copy)); }
      if (res.status >= 500) return kept().then((hit) => hit || res);   // a 5xx (WebKit hands a proxy's 502 over as an answer) is treated as no network
      return res;
    }).catch(kept)
  );
});
