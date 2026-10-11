#!/usr/bin/env python3
"""Serve a directory over HTTP and keep what pages POST to /report.

Usage: python3 -I ci/engines/serve.py <port> <root> <report dir>
GET serves files under <root>. POST /report or /report/<name> writes the body to <report dir>/<name>.json
(the latest) and to <report dir>/<name>-<n>.json (each one in turn), so a page that dies mid-run still leaves
what it sent last.
"""
import http.server, os, re, sys, threading

port, root, rdir = int(sys.argv[1]), os.path.abspath(sys.argv[2]), os.path.abspath(sys.argv[3])
os.makedirs(rdir, exist_ok=True)
count = {}
lock = threading.Lock()


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=root, **k)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_head(self):
        # byte ranges, which Safari asks for before it plays a video
        rng = self.headers.get("Range")
        path = self.translate_path(self.path)
        m = re.match(r"^bytes=(\d*)-(\d*)$", rng or "")
        if not m or not os.path.isfile(path):
            return super().send_head()
        size = os.path.getsize(path)
        a = int(m.group(1)) if m.group(1) else max(0, size - int(m.group(2) or 0))
        b = int(m.group(2)) if m.group(1) and m.group(2) else size - 1
        b = min(b, size - 1)
        if a > b or a >= size:
            self.send_response(416)
            self.send_header("Content-Range", "bytes */%d" % size)
            self.end_headers()
            return None
        f = open(path, "rb")
        f.seek(a)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", "bytes %d-%d/%d" % (a, b, size))
        self.send_header("Content-Length", str(b - a + 1))
        self.send_header("Accept-Ranges", "bytes")
        self.end_headers()
        import io
        data = f.read(b - a + 1)
        f.close()
        return io.BytesIO(data)

    def do_POST(self):
        m = re.match(r"^/report(?:/([\w.\-]{1,80}))?/?$", self.path.split("?")[0])
        if not m:
            self.send_error(404)
            return
        name = m.group(1) or "report"
        n = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(min(n, 8_000_000))
        with lock:
            count[name] = count.get(name, 0) + 1
            for fn in (name + ".json", "%s-%02d.json" % (name, count[name])):
                with open(os.path.join(rdir, fn), "wb") as f:
                    f.write(body)
        self.send_response(204)
        self.end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.log_date_time_string(), fmt % args))


http.server.ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
