#!/usr/bin/env python3
"""Point models/naturalist/manifest.json at the full database extended by tools/species/everyday_build.py.

The first parts of the rows and the zones stay where they are (the commit kept by pin/naturalist-world-9ae0806), so a
phone that holds the full database fetches again only the files that changed: the last part of the rows, the scale,
the table and the place file, from the commit of pub/naturalist-everyday given here (kept by its own pin/ branch).

Usage: python3 -I tools/species/everyday_manifest.py --parts stage-parts.json --commit SHA --results everyday.json
"""
import argparse
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MAN = os.path.join(HERE, "..", "..", "models", "naturalist", "manifest.json")
RAW = "https://raw.githubusercontent.com/jampotful/seen-back/%s/%s"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--parts", required=True)
    ap.add_argument("--commit", required=True)
    ap.add_argument("--results", required=True)
    a = ap.parse_args()
    p, r = json.load(open(a.parts)), json.load(open(a.results))
    m = json.load(open(MAN))
    sp = m["species"]
    last = sp["parts"][-1]
    assert os.path.basename(last["url"]) == p["last_part"]["name"]
    last.update({"url": RAW % (a.commit, p["last_part"]["name"]), "bytes": p["last_part"]["bytes"], "sha256": p["last_part"]["sha256"]})
    sp["count"], sp["bytes"], sp["sha256"] = p["count"], p["rows_bytes"], p["rows_sha256"]
    assert sum(x["bytes"] for x in sp["parts"]) == sp["bytes"]
    for k in ("scale", "table"):
        sp[k].update({"url": RAW % (a.commit, p[k]["name"]), "bytes": p[k]["bytes"], "sha256": p[k]["sha256"]})
    m["place"].update({"url": RAW % (a.commit, p["place"]["name"]), "bytes": p["place"]["bytes"], "sha256": p["place"]["sha256"]})
    sp["everyday"] = ("%d species people keep (tools/species/EVERYDAY.md): %d new rows at the end, made as the others were; the "
                      "table's home list gives each a share that holds in every cell (beta %g times its iNaturalist observations "
                      "marked captive or cultivated over all of iNaturalist's observations). Files that changed: pub/naturalist-everyday "
                      "at %s, kept by pin/naturalist-everyday-%s." % (r["species"], r["rows_new"], r["beta"], a.commit[:12], a.commit[:7]))
    t = r["test"]
    m.setdefault("evaluation", {})["everyday"] = {
        "photos": r["photos"], "beta": r["beta"], "made_by": "tools/species/everyday_build.py",
        "test_own_zone": {k: round(t["own"][k], 4) for k in ("kind_right", "species_right", "named", "named_right")},
        "test_alachua": {k: round(t["alachua"][k], 4) for k in ("kind_right", "species_right", "named", "named_right")},
        "world_test_drop_points": r.get("world_drop_points")}
    json.dump(m, open(MAN, "w"), indent=1)
    print("manifest: %d rows, last part %s, table %s, place %s" % (sp["count"], last["url"], sp["table"]["url"], m["place"]["url"]))


if __name__ == "__main__":
    main()
