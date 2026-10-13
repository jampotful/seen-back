#!/usr/bin/env python3
"""Checks views/*.json against docs/ENGINE-DESIGN.md section 3. Usage: python3 tools/views/check_spec.py [file ...]
Refuses: a row graded m whose every linked parameter is graded i; a parameter graded m or g with no src; a value outside its range;
an invented parameter that no row graded i or g names; a row of the wrong shape; a parameter name the engine has no field for;
a matrix that is not 3 by 3 or a matrix name that does not exist. A row links to a parameter by listing "param:<name>" among its
sources, or by listing a source string that the parameter also lists."""
import json, sys, glob, os
FIELDS = {"fov", "cpd", "fovea", "fall", "topoA", "topoS", "pupil", "dof", "M", "uvBlue", "sheen", "gain", "sat", "noGreen", "gate", "field", "persist", "hold", "thrust", "rate"}
GRADES = {"m", "g", "i"}; ROWG = {"m", "g", "i", "x"}
def is_param(d): return isinstance(d, dict) and "grade" in d
def check_param(name, d, where, errs):
    if d.get("grade") not in GRADES: errs.append("%s: grade of %s must be m, g or i" % (where, name))
    if not isinstance(d.get("invented"), bool): errs.append("%s: %s needs a true or false 'invented'" % (where, name))
    if d.get("grade") in ("m", "g") and not d.get("src"): errs.append("%s: %s is graded %s and has no src" % (where, name, d.get("grade")))
    v, r = d.get("value"), d.get("range")
    if r is not None and isinstance(v, (int, float)) and not (r[0] <= v <= r[1]): errs.append("%s: %s = %s is outside its range %s" % (where, name, v, r))
    if r is not None and r[0] > r[1]: errs.append("%s: range of %s is reversed" % (where, name))
def check(path):
    errs = []; spec = json.load(open(path)); k = spec.get("key", "?")
    for f in ("key", "version", "chip", "who", "modules", "params", "rows", "cue"):
        if f not in spec: errs.append("missing %s" % f)
    if errs: return errs
    if os.path.splitext(os.path.basename(path))[0] != k: errs.append("file name and key differ")
    P = spec["params"]; mats = spec.get("matrices", {})
    for n, d in P.items():
        if n not in FIELDS: errs.append("params: %s is not a field today's engine has" % n); continue
        if not is_param(d): errs.append("params: %s must be a parameter object" % n); continue
        check_param(n, d, "params", errs)
        if n == "M" and d.get("value") not in mats: errs.append("params: M names a matrix that does not exist: %s" % d.get("value"))
    for mn, m in mats.items():
        rows = m.get("rows")
        if not (isinstance(rows, list) and len(rows) == 3 and all(isinstance(r, list) and len(r) == 3 for r in rows)): errs.append("matrix %s is not 3 by 3" % mn)
        if m.get("grade") in ("m", "g") and not m.get("src"): errs.append("matrix %s is graded %s and has no src" % (mn, m.get("grade")))
    for sect, label in (("by", None), ("variants", None)):
        for grp, ents in spec.get(sect, {}).items():
            items = ents.items() if sect == "by" else [(grp, ents)]
            for nm, e in items:
                for n, d in e.get("params", {}).items():
                    if n not in FIELDS: errs.append("%s %s: %s is not a field today's engine has" % (sect, nm, n))
                    elif is_param(d): check_param(n, d, "%s %s" % (sect, nm), errs)
    rows = spec["rows"]; links = {n: [] for n in P}
    for i, r in enumerate(rows):
        if not (isinstance(r, list) and len(r) == 4 and r[0] in ROWG and isinstance(r[1], str) and isinstance(r[2], str) and isinstance(r[3], list)):
            errs.append("row %d has the wrong shape" % i); continue
        if r[0] in ("m", "g") and not [s for s in r[3] if not s.startswith("param:")]: errs.append("row %d (%s) is graded %s and names no source" % (i, r[1], r[0]))
        for n, d in P.items():
            if not is_param(d): continue
            if ("param:" + n) in r[3] or (set(r[3]) & set(d.get("src", []))): links[n].append(r[0])
        for s in r[3]:
            if s.startswith("param:") and s[6:] not in P: errs.append("row %d (%s) links to %s, which is not a parameter" % (i, r[1], s[6:]))
        if "—" in r[2] or "–" in r[2]: errs.append("row %d (%s) has a dash" % (i, r[1]))
    for i, r in enumerate(rows):
        if isinstance(r, list) and len(r) == 4 and r[0] == "m":
            lk = [n for n, d in P.items() if is_param(d) and (("param:" + n) in r[3] or (set(r[3]) & set(d.get("src", []))))]
            if lk and all(P[n]["grade"] == "i" for n in lk): errs.append("row %d (%s) is graded m and every parameter it describes (%s) is graded i" % (i, r[1], ", ".join(lk)))
    for n, d in P.items():
        if is_param(d) and d.get("invented") and not any(g in ("i", "g") for g in links[n]): errs.append("params: %s is invented and no row graded i or g says so" % n)
    return errs
if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob("views/*.json")); bad = 0
    for f in files:
        e = check(f); print(("FAIL " if e else "ok   ") + f)
        for x in e: print("     " + x)
        bad += bool(e)
    sys.exit(1 if bad else 0)
