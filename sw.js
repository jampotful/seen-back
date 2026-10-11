// Seen Back service worker. It keeps the app usable where there is no signal.
// The page itself is fetched fresh whenever there is a network, so a new build arrives by itself;
// models and other large unchanging files are kept after their first download.
const VERSION = '5';
const SHELL = 'shell-' + VERSION;
const KEEP = 'keep-v1';
const SHELL_FILES = ['./', 'index.html', 'manifest.webmanifest', 'icons/icon-192.png', 'icons/icon-512.png',
  'fonts/instrument-serif-latin-400-normal.woff2', 'fonts/instrument-serif-latin-400-italic.woff2'];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(SHELL).then((c) => c.addAll(SHELL_FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('shell-') && k !== SHELL).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;                 // anything from elsewhere goes straight to the network
  if (/\/(models|vendor|data|fonts)\//.test(url.pathname)) {       // large and unchanging: the kept copy first
    event.respondWith(
      caches.open(KEEP).then((c) => c.match(req).then((hit) => hit || fetch(req).then((res) => {
        if (res.ok) c.put(req, res.clone());
        return res;
      })))
    );
    return;
  }
  event.respondWith(                                               // the page: the network first, the kept copy when there is none
    fetch(req).then((res) => {
      if (res.ok) { const copy = res.clone(); caches.open(SHELL).then((c) => c.put(req, copy)); }
      return res;
    }).catch(() => caches.match(req, { ignoreSearch: true }).then((hit) => hit || caches.match('index.html')))
  );
});
