#!/usr/bin/env python3
"""The spec checker (docs/ENGINE-DESIGN.md, section 3). Usage: python3 -I tools/views/check_spec.py [--quiet] [views/<key>.json ...]

With no files it checks every views/*.json. It refuses a spec (and exits with 1) where:
  - a parameter's grade is not m, g, i or ? (? means not yet graded: the views converted from build 23 carry it until graded);
  - a parameter graded m has no source;
  - a value lies outside the parameter's range;
  - invented is not true or false on a graded parameter;
  - a row's grade is not m, g, i or x, or a row is not [grade, title, text] with optional [sources] and [parameters it describes];
  - a row graded m names parameters (its fifth element) and every one of them is graded i;
  - an invented parameter has no row graded i or g that says so: the row names it in its fifth element, or, where no row of
    the spec names parameters, the spec has at least one row graded i or g;
  - a matrix or an @reference names nothing.
The build (build.py) runs it and stops on a refusal.
"""
import json, pathlib, sys

root = pathlib.Path(__file__).resolve().parents[2]
GRADES = {"m", "g", "i", "?"}


def walk(x, path, out):
    """Every parameter object under x, with its dotted path."""
    if isinstance(x, dict):
        if "grade" in x and ("value" in x or "curve" in x):
            out.append((path, x))
            return
        for k, v in x.items():
            walk(v, path + "." + k if path else k, out)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            walk(v, "%s[%d]" % (path, i), out)


def refs(x, out):
    if isinstance(x, str) and x.startswith("@"):
        out.append(x[1:])
    elif isinstance(x, dict):
        for k, v in x.items():
            if k == "M" and isinstance(v, str):
                out.append(("M", v))
            else:
                refs(v, out)
    elif isinstance(x, list):
        for v in x:
            refs(v, out)


def inside(v, rng):
    lo, hi = rng
    vals = v if isinstance(v, list) else [v]
    return all(not isinstance(n, (int, float)) or lo <= n <= hi for n in vals)


def check(path):
    errs, notes = [], []
    try:
        s = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return ["not JSON: %s" % e], notes
    if s.get("key") != path.stem:
        errs.append("key %r is not the file's name" % s.get("key"))
    if isinstance(s.get("trial"), dict):          # changes tried on an offered view (?try=<key>): the merged spec must pass as well
        e2, n2 = check_obj(merged(s, s["trial"]))
        errs += ["trial: " + e for e in e2]
    e1, n1 = check_obj(s)
    return errs + e1, n1


def merged(a, b):
    o = dict(a)
    o.pop("trial", None)
    for k, v in b.items():
        o[k] = merged(a[k], v) if isinstance(a.get(k), dict) and isinstance(v, dict) and "grade" not in v else v
    return o


def check_obj(s):
    errs, notes = [], []
    for f in ("who", "rows", "params"):
        if f not in s:
            errs.append("no %s" % f)
    blocks = {k: s.get(k) for k in ("params", "zones", "gaze", "by", "inputs", "spectrum", "clock", "pace", "motion", "slow", "tilt", "magnet", "remap", "overlay", "sound", "haptic")}
    params = []
    walk(blocks, "", params)
    for m in (s.get("matrices") or {}).values():
        if "rows" not in m and "from_pigments" not in m:
            errs.append("a matrix has neither rows nor from_pigments")
    walk({"matrices": s.get("matrices") or {}}, "", params)
    for name, mat in (s.get("matrices") or {}).items():
        if "grade" in mat:
            params.append(("matrices." + name, dict(mat, value=mat.get("rows"))))
    ungraded = 0
    for p, o in params:
        g = o.get("grade")
        if g not in GRADES:
            errs.append("%s: grade %r" % (p, g))
        if g == "?":
            ungraded += 1
            continue
        if g == "m" and not o.get("src"):
            errs.append("%s: graded m with no source" % p)
        if not isinstance(o.get("invented"), bool):
            errs.append("%s: invented is neither true nor false" % p)
        if o.get("range") and "value" in o and not inside(o["value"], o["range"]):
            errs.append("%s: %r outside %r" % (p, o["value"], o["range"]))
    rows = s.get("rows") or []
    named_rows = [r for r in rows if len(r) >= 5]
    grade_of = {p.split(".")[-1]: o.get("grade") for p, o in params}
    grade_of.update({p: o.get("grade") for p, o in params})
    for r in rows:
        if not isinstance(r, list) or len(r) < 3 or r[0] not in ("m", "g", "i", "x") or not all(isinstance(t, str) for t in r[1:3]):
            errs.append("row %r is malformed" % (r[:2] if isinstance(r, list) else r))
            continue
        if len(r) >= 4 and not isinstance(r[3], list):
            errs.append("row %r: sources are not a list" % r[1])
        if len(r) >= 5 and r[0] == "m" and r[4] and all(grade_of.get(n) == "i" for n in r[4]):
            errs.append("row %r says m and every parameter it describes is graded i" % r[1])
    for p, o in params:
        if o.get("invented") is True:
            short = p.split(".")[-1]
            if named_rows:
                if not any(r[0] in ("i", "g") and (p in r[4] or short in r[4]) for r in named_rows):
                    errs.append("%s: invented, and no row graded i or g names it" % p)
            elif not any(r[0] in ("i", "g") for r in rows if isinstance(r, list) and r):
                errs.append("%s: invented, and the spec has no row graded i or g" % p)
    rs = []
    refs(blocks, rs)
    mats = set((s.get("matrices") or {}).keys())
    for g in ((s.get("by") or {}).get("genus") or {}).values():
        mats |= set((g.get("matrices") or {}).keys())
    for r in rs:
        if isinstance(r, tuple):
            if r[1] not in mats:
                errs.append("matrix %r is not in matrices" % r[1])
        elif r not in (s.get("params") or {}):
            errs.append("@%s names no parameter" % r)
    if ungraded:
        notes.append("%d parameters not yet graded (?)" % ungraded)
    return errs, notes


def main(argv):
    quiet = "--quiet" in argv
    files = [pathlib.Path(a) for a in argv if not a.startswith("--")] or sorted(p for p in (root / "views").glob("*.json") if p.stem != "index")
    bad = 0
    for f in files:
        errs, notes = check(f)
        if errs:
            bad += 1
            print("REFUSED %s" % f.name)
            for e in errs:
                print("  " + e)
        elif not quiet:
            print("ok %s%s" % (f.name, ("  (" + "; ".join(notes) + ")") if notes else ""))
    if not quiet or bad:
        print("%d of %d specs refused" % (bad, len(files)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
