#!/usr/bin/env python3
"""Assemble pocket v3 from the slot the rule chose: the files that replace the heads in models/pocket/, and the published branch's files.

  python3 -I tools/eval/pocket_v3.py <slot dir> --shipped docs/eval/shipped-<name>.json --decision docs/eval/decision-pocket-v3.json --ready <dir> --publish <dir>

<ready>   exactly the files that replace the heads in models/pocket/: manifest.json, kinds.f16.bin, species.f16.bin,
          species.bias.f32.bin, species.json and fitted_on.csv (the list of the photos the rows were fitted on, which the
          manifest's fitted_on block names). The image encoder is not touched: the manifest's vision block names the same file.
<publish> the same files and measured.json (what tools/eval/shipped.py measured), for the branch pub/heads-pocket-v3.
The manifest gains evaluation.measured (the numbers on the test photos, with the file they come from) and evaluation.decision.
"""
import argparse, json, os, shutil

ap = argparse.ArgumentParser()
ap.add_argument("slot")
ap.add_argument("--shipped", required=True)
ap.add_argument("--decision", required=True)
ap.add_argument("--ready", required=True)
ap.add_argument("--publish", required=True)
a = ap.parse_args()
FILES = ("manifest.json", "kinds.f16.bin", "species.f16.bin", "species.bias.f32.bin", "species.json", "fitted_on.csv")
sh = json.load(open(a.shipped, encoding="utf-8"))
dec = json.load(open(a.decision, encoding="utf-8"))
if not dec.get("ships"):
    raise SystemExit("the decision file says the candidate does not ship: " + dec.get("why", ""))
man = json.load(open(os.path.join(a.slot, "manifest.json"), encoding="utf-8"))
assert man["fusion"]["name_at"] == sh["numbers"]["name_at"] and man["fusion"].get("kind_at") == sh["numbers"]["kind_at"], "the slot's thresholds are not the ones measured"
n, k = sh["numbers"], sh["numbers"]["kind"]
r1 = lambda v: None if v is None or v[0] is None else [round(v[0], 4), round(v[1], 4), round(v[2], 4), v[3]]
man["evaluation"]["measured"] = {
    "from": "docs/eval/" + os.path.basename(a.shipped) + " (tools/eval/shipped.py through tools/fusion/fuse.py)",
    "test_photos": n["test_photos"], "kind_right": r1(n["kind_right"]), "kind_asserted": r1(k["test_wildlife"]["asserted"]), "kind_right_when_asserted": r1(k["test_wildlife"]["asserted_right"]),
    "species_top1": r1(n["species_top1"]), "named": r1(n["named"]), "named_right": r1(n["named_right"]),
    "extra_test_photos": k["test_extra"]["photos"], "extra_kind_right": r1(k["test_extra"]["kind_right"]),
    "named_on_people_and_rooms": dec["tests"]["iii_named_on_people_and_rooms"]["share"],
    "intervals": "95% bootstrap intervals over photos: [share, low, high, photos]"}
man["evaluation"]["decision"] = {"from": "docs/eval/" + os.path.basename(a.decision) + " (tools/eval/decide_v3.py)", "rule": dec["rule"], "why": dec["why"]}
for d in (a.ready, a.publish):
    os.makedirs(d, exist_ok=True)
    for f in FILES[1:]:
        shutil.copyfile(os.path.join(a.slot, f), os.path.join(d, f))
    with open(os.path.join(d, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(man, fh, indent=1)
        fh.write("\n")
shutil.copyfile(a.shipped, os.path.join(a.publish, "measured.json"))
for d in (a.ready, a.publish):
    print(d, sorted(os.listdir(d)), "%.1f MB" % (sum(os.path.getsize(os.path.join(d, f)) for f in os.listdir(d)) / 1e6))
