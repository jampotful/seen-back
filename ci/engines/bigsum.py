#!/usr/bin/env python3
"""Tables from test/engines/big.js: python3 -I ci/engines/bigsum.py <out dir> (reads big-*.json and mem.jsonl)."""
import glob, json, os, sys
out = sys.argv[1]
mem = []
if os.path.exists(os.path.join(out, "mem.jsonl")):
    for line in open(os.path.join(out, "mem.jsonl")):
        try:
            x = json.loads(line)
            if "total" in x: mem.append(x)
        except Exception: pass
def peak(a, b):
    xs = [m for m in mem if a and b and a <= m["t"] <= b]
    if not xs: return "no samples"
    t = max(xs, key=lambda m: m["total"]); s = max(xs, key=lambda m: m["top"][0][0] if m["top"] else 0)
    return "all browser processes %d MB; largest one %d MB (%s)" % (t["total"] // 1024, s["top"][0][0] // 1024 if s["top"] else 0, s["top"][0][2] if s["top"] else "")
def mb(x): return "%.1f MB" % (x / 1e6) if isinstance(x, (int, float)) else str(x)
for f in sorted(glob.glob(os.path.join(out, "big-*.json"))):
    r = json.load(open(f)); G = r.get("get") or {}; A = r.get("again") or {}; D = G.get("download") or {}; M = r.get("marks") or {}
    print("\n=== %s %s" % (r.get("browser"), r.get("version")))
    print("error:", r.get("error"), "| get poll:", r.get("getPoll"), "| again poll:", r.get("againPoll"), "| crashed:", r.get("crashed"))
    print("page:", G.get("build"), "| pocket", G.get("pocketReady"), G.get("pocketReadyMs"), "ms | controlled", G.get("controlled"), "| path:", G.get("path"), "| offer line:", G.get("offerLine"))
    print("sheet:", json.dumps(G.get("sheet"))[:400])
    b = (G.get("before") or {}); a = (G.get("after") or {})
    print("estimate before:", json.dumps(b.get("estimate"))[:200], "| persisted", b.get("persisted"))
    print("estimate after: ", json.dumps(a.get("estimate"))[:200], "| persisted", a.get("persisted"))
    for k, v in (a.get("caches") or {}).items(): print("  cache", k, json.dumps(v)[:600])
    print("download: %s ms; ready %s ms after Get it (%s ms after the last byte); fail: %s" % (D.get("downloadMs"), D.get("readyMs"), D.get("afterDownloadMs"), G.get("getFail")))
    print("  big:", json.dumps(D.get("big"))[:400]); print("  lines:", json.dumps(G.get("lines"))[:600]); print("  diag:", json.dumps(D.get("diag"))[:900])
    print("  resources:", json.dumps(G.get("resources"))[:900])
    for n in (r.get("net") or [])[:12]: print("  net:", json.dumps(n)[:420])
    print("photo in hand:", json.dumps(G.get("photo0"))[:500])
    for p in G.get("photos") or []: print("  photo %s | truth %s | small %s | large %s | wall %s ms, after the small one %s ms | fail %s" % (p.get("name"), (p.get("truth") or "")[:60], json.dumps(p.get("small"))[:160], json.dumps(p.get("large"))[:420], p.get("wallMs"), p.get("afterSmallMs"), p.get("fail")))
    print("memory: download %s | to ready %s | photos %s" % (peak(G.get("epochYes"), G.get("epochDown")), peak(G.get("epochDown") or G.get("epochYes"), G.get("epochReady")), peak(G.get("epochPhotos"), G.get("epochPhotosEnd"))))
    print("memory: whole first visit %s | reload %s" % (peak(M.get("open"), M.get("getDone")), peak(M.get("reload"), M.get("againDone"))))
    print("again: choice %s, survey %s in %s ms, big %s" % (A.get("choice"), A.get("survey"), A.get("surveyMs"), json.dumps(A.get("big1"))[:300]))
    print("  photo:", json.dumps(A.get("photo"))[:700]); print("  resources:", json.dumps(A.get("resources"))[:400], "| fetched again (Playwright):", json.dumps(r.get("againNet"))[:400])
    print("  estimate:", json.dumps(A.get("estimate"))[:200], "| diag", json.dumps(A.get("diag"))[:500])
    if r.get("home"): print("home:", json.dumps(r["home"])[:3000])
    print("notes:", json.dumps(r.get("notes"))[:1500])
