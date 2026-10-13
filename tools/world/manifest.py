#!/usr/bin/env python3
"""models/naturalist/manifest.json for the full database of the whole world (docs/tracks/worlddb.md, step 5).

Keeps the encoder and the kinds head of the present manifest, and replaces the county's species rows with the world's,
read by the page from a pinned commit of pub/naturalist-world (rows.i8.partNN, scale.f32, table.json, place.bin,
zones.json; their lengths and checksums from that branch's parts.json and place.json). The prior's weight and the
naming and offering levels come from the world test (tools/world/worldtest.py, worldtest.json, the condition given).

Usage: python3 -I tools/world/manifest.py --slot models/naturalist --pub DIR --commit SHA --test worldtest.json
         --condition zone+3@ship1 [--repo jampotful/seen-back]
"""
import argparse
import json
import os


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--slot", required=True)
    ap.add_argument("--pub", required=True, help="a checkout of pub/naturalist-world at --commit")
    ap.add_argument("--commit", required=True)
    ap.add_argument("--test", required=True)
    ap.add_argument("--condition", required=True)
    ap.add_argument("--repo", default="jampotful/seen-back")
    a = ap.parse_args()
    base = "https://raw.githubusercontent.com/%s/%s/" % (a.repo, a.commit)
    old = json.load(open(os.path.join(a.slot, "manifest.json")))
    parts = json.load(open(os.path.join(a.pub, "parts.json")))
    pl = json.load(open(os.path.join(a.pub, "place.json")))
    wt = json.load(open(a.test))
    cond = wt["by_condition"][a.condition]
    st = cond["settings_on_all"]

    def far(name, info):
        return {"url": base + name, "bytes": info["bytes"], "sha256": info["sha256"]}
    m = {"id": "bioclip2-l14-world", "licence": old["licence"], "source": old["source"], "vision": old["vision"], "width": parts["width"], "kinds": old["kinds"]}
    m["species"] = {"count": parts["count"], "dtype": "int8",
                    "parts": [far(p["url"], p) for p in parts["rows"]["parts"]], "bytes": parts["rows"]["bytes"], "sha256": parts["rows"]["sha256"],
                    "scale": far("scale.f32", parts["scale"]), "table": far("table.json", parts["table"]),
                    "names_from": "GBIF backbone (scientific names, tools/world/names.py); iNaturalist taxonomy (English names)",
                    "rows_from": "one sentence a species, 'a photo of <name>.', BioCLIP 2's text half (tools/coverage/text.py), one byte a number (tools/world/pack.py)"}
    m["place"] = dict(far("place.bin", pl["place.bin"]), zones=far("zones.json", pl["zones.json"]), radius_km=wt["radius_km"], eps=wt["eps"], res=pl["res"])
    f = dict(old["fusion"])
    f["alpha_prior"] = st["alpha"]
    if st["name_at"] is not None:
        f["name_at"] = st["name_at"]
    if st["offer_at"] is not None:
        f["offer_at"] = st["offer_at"]
    m["fusion"] = f
    m["fusion_note"] = ("The kinds head, t_kind, w_kind, the rule and kind_at are the county slot's (tools/eval/study2.py, tools/eval/shipped.py). "
                        "alpha_prior, name_at and offer_at were chosen on the world test's %d photos under the prior of the time zone and three creatures "
                        "met (tools/world/worldtest.py, condition %s): alpha the best for the right species first, name_at the lowest level from which at "
                        "least 97 names in 100 were right, offer_at the lowest from which the three likeliest held the right species nine times in ten "
                        "for the photos left without a name, over every kind. The figures the page may claim, with each continent's setting chosen on the "
                        "other six, are in docs/tracks/worlddb.md." % (wt["photos"], a.condition))
    m["evaluation"] = {"world_test": {"photos": wt["photos"], "condition": a.condition, "top1": cond["all"]["top1"], "named": cond["all"]["named"],
                                      "names_right": cond["all"]["names_right"], "settings_on_all": st,
                                      "by_condition_top1": {k: v["all"]["top1"] for k, v in wt["by_condition"].items()}},
                       "previous_slot": {"id": old["id"], "species": old["species"].get("count")}}
    m["needs"] = sorted(set((old.get("needs") or []) + ["species.dtype int8, species.parts, place (the build of the page that reads the full database for the world)"]))
    if old.get("seconds_a_photo"):
        m["seconds_a_photo"] = old["seconds_a_photo"]
        m["seconds_note"] = (old.get("seconds_note", "") + " The world rows add the scoring of every one of their rows to each photo, which no phone has timed.").strip()
    json.dump(m, open(os.path.join(a.slot, "manifest.json"), "w"), indent=1)
    total = m["vision"]["bytes"] + m["species"]["bytes"] + m["species"]["scale"]["bytes"] + m["species"]["table"]["bytes"] + m["place"]["bytes"] + m["place"]["zones"]["bytes"]
    print(json.dumps({"bytes_to_download": total, "alpha_prior": f["alpha_prior"], "name_at": f["name_at"], "offer_at": f["offer_at"]}))


if __name__ == "__main__":
    main()
