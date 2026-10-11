#!/usr/bin/env python3
"""Parity of the reference with the page, to 1e-6, on random and adversarial scores.

    python3 -I tools/fusion/parity.py make cases.json            # cases for the stand-in slot (test/rec/models/standin)
    node test/rec/fuse_page.js cases.json page.json               # the page's own answers (needs test/rec/serve.js running on 8782)
    python3 -I tools/fusion/parity.py check cases.json page.json  # exits 1 on any difference

The page reads its settings from the slot's manifest, so huge and tiny temperatures are made by scaling the scores themselves.
"""
import json, pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fuse import fuse, load_slot

slot = load_slot(pathlib.Path(__file__).resolve().parents[2] / "test" / "rec" / "models" / "standin")
m, t = slot["manifest"], slot["table"]
nk, ns = len(m["kinds"]["labels"]), len(t)

if sys.argv[1] == "make":
    rs = np.random.RandomState(20261011)
    cases = []
    for i in range(300):
        scale = [1, 1, 1, 0.001, 0.05, 30][i % 6]                 # tiny and huge temperatures
        cases.append({"kd": (rs.uniform(-0.2, 1, nk) * scale).tolist(), "sd": (rs.uniform(-0.2, 1, ns) * scale).tolist(), "month": int(rs.randint(0, 12))})
    for month in range(12):                                         # everything equal; everything zero
        cases.append({"kd": [0.5] * nk, "sd": [0.5] * ns, "month": month})
        cases.append({"kd": [0.0] * nk, "sd": [0.0] * ns, "month": month})
    for k in range(nk):                                             # each kind sure of itself against a species list sure of something else, and ties between two kinds
        for j in (0, 5, 6, ns - 1):
            kd = [0.0] * nk; kd[k] = 1.0; sd = [0.0] * ns; sd[j] = 1.0
            cases.append({"kd": kd, "sd": sd, "month": (k + j) % 12})
        kd = [0.0] * nk; kd[k] = kd[(k + 1) % nk] = 0.7
        cases.append({"kd": kd, "sd": [0.3] * ns, "month": k % 12})
    pathlib.Path(sys.argv[2]).write_text(json.dumps(cases))
    print(len(cases), "cases")
else:
    cases = json.loads(pathlib.Path(sys.argv[2]).read_text()); page = json.loads(pathlib.Path(sys.argv[3]).read_text())
    worst, bad = 0.0, []
    for i, (c, g) in enumerate(zip(cases, page)):
        r = fuse(m, t, c["month"], c["kd"], c["sd"])
        why = []
        if r["kind"] != g["kind"]: why.append("kind %s / %s" % (r["kind"], g["kind"]))
        if [k["key"] for k in r["kinds"]] != [k["key"] for k in g["kinds"]]: why.append("order of kinds")
        if [s["sci"] for s in r["species"]] != [s["sci"] for s in g["species"]]: why.append("top five")
        if (r["named"] or {}).get("sci") != (g["named"] or {}).get("sci"): why.append("named")
        if [s["sci"] for s in r["offers"]] != [s["sci"] for s in g["offers"]]: why.append("offers")
        d = max([abs(a["p"] - b["p"]) for a, b in zip(r["kinds"], g["kinds"])] + [abs(a["head"] - b["head"]) for a, b in zip(r["kinds"], g["kinds"])] + [abs(a["p"] - b["p"]) for a, b in zip(r["species"], g["species"])])
        worst = max(worst, d)
        if d > 1e-6: why.append("numbers differ by %.3g" % d)
        if why: bad.append((i, why))
    print(len(cases), "cases, largest difference in any probability %.3g," % worst, len(bad), "cases differ")
    for i, why in bad[:12]: print("  case", i, why)
    raise SystemExit(1 if bad else 0)
