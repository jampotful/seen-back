#!/usr/bin/env python3
"""Tables for the webkitmem trial: python3 -I ci/engines/bigwmsum.py <out dir> (reads <out>/mem2.jsonl and <out>/<variant>/big-<browser>.json).
For each variant and browser: the largest web-content process's resident size and physical footprint (Linux: anonymous + shared resident)
at their highest in each phase, its own recorded peak (macOS: the lifetime maximum of the footprint; Linux: VmHWM), the threads, and the
marks of each step of the larger model's load with the footprint and the runtime heap at that moment. Sizes in MiB."""
import glob, json, os, sys
out = sys.argv[1]
S = []
for line in open(os.path.join(out, "mem2.jsonl")):
    try:
        x = json.loads(line)
        if "p" in x: S.append(x)
    except Exception: pass
WEB = ("WebContent", "WebKitWebProcess")
def web(rows): return [r for r in rows if any(w in r[1] for w in WEB)]
def window(a, b): return [s for s in S if a and b and a <= s["t"] <= b]
def peak(a, b):
    xs = window(a, b); best = {"rss": 0, "foot": 0, "own": 0, "thr": 0, "pid": 0}
    for s in xs:
        for r in web(s["p"]):
            pid, name, rss, foot, own, thr = r
            if foot > best["foot"]: best.update(foot=foot, pid=pid)
            best["rss"] = max(best["rss"], rss); best["own"] = max(best["own"], own); best["thr"] = max(best["thr"], thr)
    return best
def at(t, pid=None):                       # the largest web-content process's footprint at the first sample after t
    for s in S:
        if s["t"] >= t:
            w = web(s["p"]); w = [r for r in w if pid is None or r[0] == pid] or w
            return max((r[3] for r in w), default=0)
    return 0
mb = lambda k: "%5d" % (k // 1024)
print("variant  browser   phase         rss-peak  footprint-peak  own-peak(lifetime)  threads")
for d in sorted(glob.glob(os.path.join(out, "*", "big-*.json"))):
    v = os.path.basename(os.path.dirname(d)); r = json.load(open(d)); G = r.get("get") or {}; A = r.get("again") or {}; M = r.get("marks") or {}
    b = r.get("browser")
    for ph, a, z in [("first visit", M.get("open"), M.get("getDone")), ("download", G.get("epochYes"), G.get("epochDown")),
                     ("to ready", G.get("epochDown"), G.get("epochReady")), ("photos", G.get("epochPhotos"), G.get("epochPhotosEnd")),
                     ("reload", M.get("reload"), M.get("againDone"))]:
        p = peak(a, z)
        print("%-8s %-9s %-13s %s MiB  %s MiB        %s MiB          %s" % (v, b, ph, mb(p["rss"]), mb(p["foot"]), mb(p["own"]), p["thr"]))
    ph = [p.get("large") for p in (G.get("photos") or [])]
    print("   answers:", json.dumps([(p or {}).get("named") for p in ph] + [((A.get("photo") or {}).get("large") or {}).get("named")])[:400],
          "| error:", r.get("error"), "| getFail:", G.get("getFail"), "| ready ms:", (G.get("download") or {}).get("readyMs"))
    for tag, R in [("get", G), ("again", A)]:
        wm = R.get("wm") or []
        if not wm: continue
        t0 = wm[0][0]
        print("   marks (%s): " % tag + "; ".join("%s +%.1fs foot %s heap %s" % (w[1], (w[0] - t0) / 1000, mb(at(w[0])).strip(),
              (str(int(w[2].split()[0]) // 1048576) if w[1].startswith("w-") and w[2] and w[2].split()[0].isdigit() else w[2])) for w in wm))
snaps = os.path.join(out, "mem2-snap.jsonl")
if os.path.exists(snaps):
    print("\nbreakdowns of the largest process at its highs (mem2-snap.jsonl):")
    for line in open(snaps):
        x = json.loads(line); s = x["snap"]
        if isinstance(s, list): s = "; ".join("%s %s %dM of %dM %s" % (m["perm"], m["path"][-30:], m["rss"] // 1024, m["size"] // 1024, "anon %dM" % (m["anon"] // 1024)) for m in s[:12])
        print(" ", x["t"], x["name"], "rss", x["rss"] // 1024, "foot", x["foot"] // 1024, "|", s[:1800].replace("\n", " / "))
