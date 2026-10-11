#!/usr/bin/env python3
"""Gather an engines job's results into <out>/summary.json. Usage: python3 -I ci/engines/summarize.py <out> <shard>"""
import glob, json, os, re, sys

out, shard = sys.argv[1], sys.argv[2]
S = {"shard": shard, "runs": [], "check4": {}, "iphone": None}


def brief(rec):
    T = rec.get("selftest") or {}
    E = T.get("env") or {}
    M = (T.get("motion") or {}).get("runs") or {}

    def pick(size):
        xs = [v for k, v in M.items() if k.startswith(size + " ")]
        ms = [x["ms"] for x in xs if x.get("ms") is not None]
        wo = [x["worst"] for x in xs if x.get("worst") is not None]
        return {"ms_mean": round(sum(ms) / len(ms), 1) if ms else None, "ms_worst": max(wo) if wo else None,
                "sizes": sorted(set(x.get("size") for x in xs))} if xs else None

    return {"browser": rec.get("browser"), "viewport": rec.get("viewport"), "platform": rec.get("platform"), "version": rec.get("version"),
            "launchError": (rec.get("launchError") or "")[:300] or None, "error": rec.get("error"),
            "done": T.get("done"), "ok": T.get("ok"), "checks": T.get("checks"), "fails": T.get("fails"),
            "webgl2": E.get("webgl2"), "floatOK": E.get("floatOK"), "renderer": E.get("unmaskedRenderer") or E.get("renderer"),
            "engineError": E.get("engineError"), "maxTexture": E.get("maxTexture"), "serif": E.get("serif"),
            "side0": (T.get("motion") or {}).get("side0"), "frame_default": pick("default"), "frame_540": pick("540"),
            "video": (T.get("motion") or {}).get("video"), "ms": T.get("ms"),
            "pageErrors": rec.get("pageErrors"), "console": (rec.get("console") or [])[:8], "failedRequests": (rec.get("failedRequests") or [])[:8],
            "installability": rec.get("installability"), "serviceWorker": rec.get("serviceWorker"), "liveFlow": rec.get("liveFlow"),
            "openState": rec.get("openState"), "notes": rec.get("notes"), "shots": rec.get("shots"), "rec": recBrief(T.get("rec"))}


def recBrief(R):
    if not R:
        return None
    ph = R.get("photos") or []
    return {"ready": not R.get("error"), "readyMs": R.get("readyMs"), "error": R.get("error"), "backend": (R.get("about") or {}).get("backend"), "model": (R.get("about") or {}).get("model"),
            "meanRunMs": R.get("meanRunMs"), "photos": len(ph), "errors": [p["name"] + ": " + str(p["error"]) for p in ph if p.get("error")],
            "matchPython": "%d of %d" % (sum(1 for p in ph if p.get("match")), sum(1 for p in ph if "match" in p)), "differ": [[p["name"], p.get("head3"), p.get("python3")] for p in ph if p.get("match") is False],
            "preSamePNG": "%d of %d" % (sum(1 for p in ph if p.get("preSame") and p["name"].endswith(".png")), sum(1 for p in ph if "preSame" in p and p["name"].endswith(".png"))),
            "cosineMin": min([p["cosine"] for p in ph if "cosine" in p and not p["name"].startswith("info-")] or [None]) if any("cosine" in p for p in ph) else None,
            "perPhoto": [[p["name"], (p.get("ms") or {}).get("pre"), (p.get("ms") or {}).get("run"), p.get("from")] for p in ph]}


for f in sorted(glob.glob(os.path.join(out, "shots", "*.json"))):
    if f.endswith("selftest-summary.json"):
        continue
    try:
        S["runs"].append(brief(json.load(open(f))))
    except Exception as e:
        S["runs"].append({"file": os.path.basename(f), "unreadable": str(e)})

for f in sorted(glob.glob(os.path.join(out, "check4-*.json"))):
    m = re.search(r"check4-(\w+)\.json$", f).group(1)
    txt = open(f).read()
    err = open(f.replace(".json", ".err.txt")).read() if os.path.exists(f.replace(".json", ".err.txt")) else ""
    r = {"ran": False, "pass": False}
    try:
        j = json.loads(txt)
        r["ran"] = True
        errs = []

        def walk(o, p=""):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k == "errors" and isinstance(v, list):
                        errs.extend(p + ": " + str(x) for x in v)
                    else:
                        walk(v, p + "." + k)
        walk(j)
        r["page_errors"] = errs[:10]
        if m == "lex":
            r["wrong"] = j.get("lex", {}).get("wrong")
            r["pass"] = not r["wrong"] and not errs
        else:
            r["pass"] = not errs
    except Exception:
        r["stderr_tail"] = err[-400:]
    S["check4"][m] = r

S["check_rec"] = {}
for f in sorted(glob.glob(os.path.join(out, "rec", "*.json"))):
    name = os.path.basename(f)[:-5]
    txt = open(f).read().strip().splitlines()
    try:
        j = json.loads("\n".join(txt[:-1])) if len(txt) > 1 else {}
    except Exception:
        j = {}
    S["check_rec"][name] = {"line": txt[-1] if txt else "(nothing printed)", "failed": {k: v for k, v in j.items() if isinstance(v, dict) and not v.get("ok")}}
    if os.path.exists(f.replace(".json", ".err.txt")):
        e = open(f.replace(".json", ".err.txt")).read()
        if e.strip():
            S["check_rec"][name]["stderr_tail"] = e[-600:]
ip = os.path.join(out, "reports", "iphone.json")
if os.path.exists(ip):
    try:
        S["iphone"] = brief({"browser": "safari-ios-simulator", "viewport": "phone", "platform": "macos", "selftest": json.load(open(ip))})
    except Exception as e:
        S["iphone"] = {"unreadable": str(e)}
S["iphone_posts"] = sorted(os.path.basename(p) for p in glob.glob(os.path.join(out, "reports", "iphone*.json")))
json.dump(S, open(os.path.join(out, "summary.json"), "w"), indent=1)
for r in S["runs"]:
    print(r.get("browser"), r.get("viewport"), "done", r.get("done"), "ok", r.get("ok"), "fails", len(r.get("fails") or []), "webgl2", r.get("webgl2"), "float", r.get("floatOK"), r.get("renderer"))
print("check4", {k: v.get("pass") for k, v in S["check4"].items()})
print("iphone", (S["iphone"] or {}).get("done"), (S["iphone"] or {}).get("ok"), S["iphone_posts"])
