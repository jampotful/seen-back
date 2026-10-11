// The threads experiment's server: one directory per port, so that each port is its own origin with its own service worker.
//   node test/engines/coi_serve.js <report dir> 8791=/tmp/coi/none 8792=/tmp/coi/rc 8793=/tmp/coi/cl 8794=/tmp/coi/none:cors
// It sends no isolation headers of its own (the point is to see what the service worker alone can do); ':cors' marks a port that
// stands in for raw.githubusercontent.com (Access-Control-Allow-Origin: *, no Cross-Origin-Resource-Policy).
// A request for index.html with probe=1 in its address gets test/engines/coi_probe.js added before </body>.
// POST /report/<name> writes the body to <report dir>/<name>.json. GET /__bad?on=1|0 makes the port answer 502 to everything, or stop.
const http = require('http'), fs = require('fs'), path = require('path');
const [, , RDIR, ...specs] = process.argv;
fs.mkdirSync(RDIR, { recursive: true });
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'application/javascript', '.mjs': 'text/javascript', '.wasm': 'application/wasm', '.json': 'application/json',
  '.onnx': 'application/octet-stream', '.bin': 'application/octet-stream', '.png': 'image/png', '.jpg': 'image/jpeg', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json', '.css': 'text/css', '.md': 'text/plain' };
const bad = {};   // GET /__bad?on=1: every later answer on that port is a 502 until /__bad?on=0
for (const spec of specs) {
  const [port, rest] = spec.split('='), [root, flag] = rest.split(':'), cors = flag === 'cors';
  http.createServer((req, res) => {
    const u = new URL(req.url, 'http://x');
    if (req.method === 'POST' && u.pathname.startsWith('/report/')) {
      let b = ''; req.on('data', (d) => b += d); req.on('end', () => {
        const name = u.pathname.slice(8).replace(/[^\w.-]/g, '_') || 'report';
        fs.writeFileSync(path.join(RDIR, name + '.json'), b); res.writeHead(204, { 'Access-Control-Allow-Origin': '*' }); res.end();
      });
      return;
    }
    if (u.pathname === '/__bad') { bad[port] = u.searchParams.get('on') === '1'; res.writeHead(200, { 'Access-Control-Allow-Origin': '*' }); res.end(String(bad[port])); return; }
    if (bad[port]) { res.writeHead(502, { 'Content-Type': 'text/html' }); res.end('<h1>502 Bad Gateway</h1>'); return; }   // as a proxy or a CDN having a bad moment
    if (req.method === 'OPTIONS') { res.writeHead(204, { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST', 'Access-Control-Allow-Headers': '*' }); res.end(); return; }
    let p = decodeURIComponent(u.pathname); if (p.endsWith('/')) p += 'index.html';
    const file = path.join(root, path.normalize(p).replace(/^(\.\.[\/\\])+/, ''));
    if (!file.startsWith(root) || !fs.existsSync(file) || !fs.statSync(file).isFile()) { res.writeHead(404); res.end('not found'); return; }
    const h = { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream', 'Cache-Control': 'no-store' };
    if (cors) h['Access-Control-Allow-Origin'] = '*';
    let body = fs.readFileSync(file);
    if (/index\.html$/.test(file) && u.searchParams.get('probe') === '1') body = Buffer.from(body.toString('utf8').replace('</body>', '<script src="test/engines/coi_probe.js?v=1"></script>\n</body>'));
    h['Content-Length'] = body.length;
    res.writeHead(200, h); res.end(req.method === 'HEAD' ? undefined : body);
  }).listen(+port, '127.0.0.1', () => console.log('serving', root, 'on', port, cors ? '(cors)' : ''));
}
