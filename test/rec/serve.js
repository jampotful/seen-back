// A small static server for the recognizer checks: the repository root, with switches to slow a file down,
// lose it, damage it, or swap one file for another, and a list of what was asked for.
//   node test/rec/serve.js [port]        then   GET /__ctl?reset=1 | down=1 | drop=<regexp> | slow=<regexp>&bps=<bytes a second> | lose=<regexp> | damage=<regexp> | cut=<regexp> | swap=<path>&with=<path> | log=1
const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..', '..'), port = +(process.argv[2] || process.env.PORT || 8782);
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8', '.json': 'application/json', '.wasm': 'application/wasm',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.webm': 'video/webm', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json', '.css': 'text/css' };
let rule = {}, log = [];
const re = (s) => (s ? new RegExp(s) : null);
http.createServer((req, res) => {
  const u = new URL(req.url, 'http://x');
  if (u.pathname === '/__ctl') {
    const q = u.searchParams;
    if (q.has('reset')) { rule = {}; log = []; }
    if (q.has('down')) rule.down = true;                             // as if the network were gone: every request is dropped
    if (q.has('slow')) { rule.slow = re(q.get('slow')); rule.bps = +(q.get('bps') || 2e6); }
    if (q.has('lose')) rule.lose = re(q.get('lose'));
    if (q.has('drop')) rule.drop = re(q.get('drop'));                // the connection is cut for these, as when there is no network
    if (q.has('damage')) rule.damage = re(q.get('damage'));
    if (q.has('cut')) rule.cut = re(q.get('cut'));
    if (q.has('swap')) { rule.swap = q.get('swap'); rule.with = q.get('with'); }
    res.writeHead(200, { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' }); res.end(JSON.stringify(q.has('log') ? log : { ok: true })); return;
  }
  let rel = decodeURIComponent(u.pathname).replace(/^\/+/, '') || 'index.html';
  log.push(rel + u.search);
  if (rule.down || (rule.drop && rule.drop.test(u.pathname))) { req.socket.destroy(); return; }
  if (rule.swap && rel === rule.swap) rel = rule.with;
  const file = path.join(root, rel);
  if (file.indexOf(root) !== 0 || (rule.lose && rule.lose.test(u.pathname)) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { res.writeHead(404, { 'Content-Type': 'text/plain' }); res.end('not found'); return; }
  let body = fs.readFileSync(file);
  if (rule.damage && rule.damage.test(u.pathname)) { body = Buffer.from(body); for (let i = 1000; i < body.length; i += 997) body[i] ^= 0x5a; }
  if (rule.cut && rule.cut.test(u.pathname)) body = body.subarray(0, body.length >> 1);
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream', 'Content-Length': body.length, 'Cache-Control': 'no-cache' });
  if (rule.slow && rule.slow.test(u.pathname)) {
    const step = Math.max(1024, Math.round(rule.bps / 20)); let o = 0;
    const t = setInterval(() => { if (o >= body.length || res.destroyed) { clearInterval(t); res.end(); return; } res.write(body.subarray(o, o + step)); o += step; }, 50);
  } else res.end(body);
}).listen(port, '127.0.0.1', () => console.log('serving ' + root + ' on http://127.0.0.1:' + port));
