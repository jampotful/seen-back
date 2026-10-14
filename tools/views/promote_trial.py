#!/usr/bin/env python3
"""Put a compiled draft behind ?try=<view> on an offered view (burst 9, compiler2).

    python3 -I tools/views/promote_trial.py DRAFT_DIR key [key ...]

DRAFT_DIR holds <key>.<model>.json from tools/views/compile.py (a folder of pub/views-draft). An offered view is reached with
?try=<key> through its spec's "trial" block (src/cam.a.js), so the draft goes there and the offered view stays as it is:
- the draft's params, zones, gaze and blocks go into the trial, except where the trial already holds a key, which a person
  checked by hand (most are pigment matrices) and which is kept;
- the draft's matrices are added under names the spec does not use yet;
- the trial's rows become the draft's rows, followed by the hand-made trial rows whose titles the draft does not repeat, so
  nothing is lost before the one-voice pass;
- "compiled" in the trial says which draft it came from.
The spec checker runs on every file written, and a refused file is put back as it was.
"""
import copy, glob, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BLOCKS = ["zones", "gaze", "spectrum", "clock", "pace", "motion", "slow", "tilt", "magnet", "remap", "overlay", "sound", "haptic"]


def rename(x, old, new):
    """Matrix references (M, dark, q) equal to old become new, anywhere in x."""
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ("M", "dark", "q", "value") and v == old:
                x[k] = new
            else:
                rename(v, old, new)
    elif isinstance(x, list):
        for v in x:
            rename(v, old, new)


def promote(spec, draft, label):
    draft = copy.deepcopy(draft)
    old = copy.deepcopy(spec.get("trial") or {})
    taken = set(spec.get("matrices") or {}) | set(old.get("matrices") or {})
    for k in list((draft.get("matrices") or {}).keys()):
        if k in taken:
            nk = k + "_COMPILED"
            draft["matrices"][nk] = draft["matrices"].pop(k)
            rename({b: draft.get(b) for b in ["params"] + BLOCKS}, k, nk)
    t = copy.deepcopy(old)
    params = t.setdefault("params", {})
    for k, v in (draft.get("params") or {}).items():
        if k not in params:
            params[k] = v
    mats = t.setdefault("matrices", {})
    for k, v in (draft.get("matrices") or {}).items():
        mats[k] = v
    if not mats:
        t.pop("matrices")
    for b in BLOCKS:
        if draft.get(b) and b not in t:
            t[b] = draft[b]
    rows = [r for r in draft.get("rows") or []]
    seen = {str(r[1]).strip().lower() for r in rows if isinstance(r, list) and len(r) > 1}
    rows += [r for r in old.get("rows") or [] if str(r[1]).strip().lower() not in seen]
    t["rows"] = rows
    t["compiled"] = label
    out = dict(spec)
    out["trial"] = t
    return out


def main(argv):
    d, keys = argv[0], argv[1:]
    bad = 0
    for k in keys:
        drafts = sorted(glob.glob(os.path.join(d, "%s.*.json" % k)))
        drafts = [p for p in drafts if not p.endswith((".refused.json", ".reply.json"))]
        if not drafts:
            print("%s: no draft in %s" % (k, d)); bad += 1; continue
        vp = os.path.join(ROOT, "views", k + ".json")
        before = open(vp, encoding="utf-8").read()
        spec = json.loads(before)
        if not spec.get("offered"):
            print("%s: not an offered view; its own file is reached by ?try= already, so nothing was changed" % k); bad += 1; continue
        draft = json.load(open(drafts[0], encoding="utf-8"))
        label = "%s/%s" % (os.path.basename(os.path.normpath(d)), os.path.basename(drafts[0]))
        open(vp, "w", encoding="utf-8").write(json.dumps(promote(spec, draft, label), ensure_ascii=False, indent=1) + "\n")
        r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "tools", "views", "check_spec.py"), vp], capture_output=True, text=True)
        if r.returncode:
            open(vp, "w", encoding="utf-8").write(before)
            print("%s: refused by the checker, left as it was\n%s" % (k, r.stdout)); bad += 1
        else:
            print("%s: trial holds %s" % (k, label))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
