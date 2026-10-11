#!/usr/bin/env python3
"""Write docs/EVAL.md and the tables under docs/eval/ from the studies' JSON files.

  python3 -I tools/eval/report.py [--dir docs/eval] [--out docs/EVAL.md]

Every number in the report is read from a JSON file written by one of the scripts in tools/eval/
(study1.py, checks.py, study2.py, shipped.py); this script only lays them out and adds the sentences around them.
"""
import argparse, glob, json, os

ap = argparse.ArgumentParser()
ap.add_argument("--dir", default="docs/eval")
ap.add_argument("--out", default="docs/EVAL.md")
a = ap.parse_args()
D = a.dir


def load(name):
    p = os.path.join(D, name)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None


def pc(x, digits=1):
    return "–" if x is None else ("%." + str(digits) + "f%%") % (100 * x)


def pci(v):
    """A share with its interval, in percent."""
    if not v or v[0] is None:
        return "–"
    return "%.1f%% (%.1f to %.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])


def pts(v):
    """A difference in percentage points with its interval."""
    if not v or v[0] is None:
        return "–"
    return "%+.1f (%+.1f to %+.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])


def table(head, rows, align=None):
    align = align or ["---"] + ["---:"] * (len(head) - 1)
    out = ["| " + " | ".join(head) + " |", "|" + "|".join(align) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def write(name, text):
    p = os.path.join(D, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text.rstrip("\n") + "\n")
    print("wrote", p)


def extra_table(rows, first="Photos of"):
    """One row a true kind, from tools/eval/kinds.py table()."""
    return table([first, "Photos", "Kind right", "Kind asserted", "Right when asserted", "True kind among the three when not sure", "Said `person`", "Said `none`", "A species named", "Commonest wrong answer"],
                 [[g["kind"], g["n"], pci(g["right"]), pc(g["asserted"]), pc(g["asserted_right"]), pc(g["not_sure_true_kind_among_three"]), pc(g["said_person"]), pc(g["said_none"]), pc(g["named"]), g["commonest_wrong"] or "–"] for g in rows],
                 ["---"] + ["---:"] * 8 + ["---"])


def kind_decision_lines(kd):
    """The table of kinds heads and rules of one model in Study 2."""
    t = kd["tuned_on"]
    ex = t.get("extra")
    out = ["**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on %d wildlife tuning photos%s. The number tuned on is %s. Each row is one kinds head under one rule at its best setting on the tuning photos. "
           "`kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`." % (
               t["wildlife_photos"], (" and %d tuning photos of the extra set `%s` (`%s`). Another %d of its photos were there for fitting kind rows, and its %d test photos (`%s`) are only reported" % (
                   ex["photos"], ex["set"], ex["vectors"], ex["fitting_photos"], ex["test_photos"], ex["test_vectors"])) if ex else " alone, because this model's vectors of the extra set (people, pets, livestock, rooms) were not published when this ran", kd["tuned_number"]), ""]

    def row(label, c):
        tw, tx = c["test_wildlife"], c.get("test_extra")
        return [label, c["head"], c["rule"], "%g" % c["t_kind"], "%g" % c["w_kind"], pc(c["tuning_both"]), pc(c["tuning_wildlife"]), pc(c["tuning_extra"]), pci(tw["kind_right"]), pci(tx["kind_right"]) if tx else "–",
                ("%.2f" % c["kind_at"]) if c.get("kind_at") is not None else "none", pci(tw["asserted"]), pci(tw["asserted_right"]), pci(tx["asserted"]) if tx else "–", pci(tx["asserted_right"]) if tx else "–"]
    rows = [row("", c) for c in kd["candidates"]] + [row("**chosen**", kd["chosen"]), row("what the wildlife photos alone would choose", kd["chosen_on_wildlife_alone"])]
    out += [table(["", "Kinds head", "Rule", "t_kind", "w_kind", "Tuning number", "Wildlife tuning photos", "Extra tuning photos", "Kind right, wildlife test", "Kind right, extra test", "kind_at", "Asserted, wildlife test", "Right when asserted", "Asserted, extra test", "Right when asserted"],
                  rows, ["---", "---", "---"] + ["---:"] * 12), ""]
    if kd["chosen"].get("test_extra_by_kind"):
        out += ["The chosen setting on the extra set's test photos, by kind (no species is named in this computation):", "", extra_table(kd["chosen"]["test_extra_by_kind"]), ""]
    return out


GEN = "_This file is written by `tools/eval/report.py` from `%s`. Rerun the script to change it._"
NAMES = {"species_sci": "scientific name", "species_com": "English name", "species_taxon_com": "taxonomy and English name"}
ORDER = ["bioclip25-h14", "bioclip2-l14", "bioclip-b16", "tinyclip-39m-16", "tinyclip-8m-16", "tinyclip-61m-32", "tinyclip-40m-32", "mobileclip2-s0", "clip-b32", "siglip2-b16", "bioclip25-mobile-fastvit"]
# The coordinator's first look (tools: /home/claude/analysis/scripts/quick.py; numbers as written in the briefing notes).
FIRST_LOOK = [("bioclip2-l14", "species_sci", {"plain_top1": 0.904, "plain_top5": 0.968, "tuned_top1": 0.925, "tuned_top5": 0.975, "kind_from_top": 0.98}),
              ("bioclip25-h14", "species_sci", {"plain_top1": 0.929, "plain_top5": 0.973, "tuned_top1": 0.936, "tuned_top5": 0.977}),
              ("tinyclip-39m-16", "species_com", {"kind_phrases": 0.776, "plain_top1": 0.21, "tuned_top1": 0.35}),
              ("tinyclip-8m-16", "species_com", {"kind_phrases": 0.72, "plain_top1": 0.15, "tuned_top1": 0.27})]

S1 = load("study1.json")
CH = load("checks.json")
S2 = {os.path.basename(p)[7:-5]: json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(os.path.join(D, "study2-*.json")))}
S2L = {k: v for k, v in S2.items() if v.get("licence_rule", "all") != "all"}       # heads fitted under a licence rule: their own section
S2 = {k: v for k, v in S2.items() if k not in S2L}
SH = {os.path.basename(p)[8:-5]: json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(os.path.join(D, "shipped-*.json")))}
models = [m for m in ORDER if m in S1["models"]] + [m for m in S1["models"] if m not in ORDER]
P = S1["prior_only"]
meth = S1["method"]

# ---------------------------------------------------------------- tables under docs/eval/
rows = []
for m in models:
    r = S1["models"][m]
    for ls, v in r["labelsets"].items():
        t = v["tuned"]
        s = t["settings"]
        rows.append([m, NAMES[ls] + (" *" if ls == r.get("best_labelset_on_val") else ""), pci(v["plain"]["top1"]), pci(v["plain"]["top5"]), pci(t["top1"]), pci(t["top5"]), pts(t["top1_gain_over_plain"]),
                     pci(v["plain"]["kind_from_top"]), pci(t["kind_from_top"]), pci(t["kind_from_sum"]),
                     "n≥%d, λ=%g, c=%g, α/T=%g, T=%g" % (s["min_n"], s["lam"], s["c"], s["ratio"], s["t_species"])])
write("labelsets.md", "# Every model and every label set\n\n" + GEN % "docs/eval/study1.json" + "\n\n"
      "Test split, %d photos. Intervals are 95%% percentile intervals from %d bootstrap resamples over photos. A star marks the label set that did best on `val` with the prior. "
      "The last column gives the settings chosen on `val`: the smallest number of records a species needs to stay in the list, the two smoothing terms of the prior, the prior's weight divided by the temperature, and the temperature.\n\n" % (P["test_rows"], meth["resamples"])
      + table(["Model", "Species rows made from", "Top-1", "Top-5", "Top-1 with prior", "Top-5 with prior", "Gain from prior (points)", "Kind from top species", "Kind from top species, with prior", "Kind from summed species", "Settings"], rows))

rows = []
for m in models:
    r = S1["models"][m]
    b = r.get("best_labelset_on_val")
    for vn, v in r.get("variants", {}).items():
        if "error" in v:
            rows.append([m, vn, v["error"]] + [""] * 5)
            continue
        l = v["labelsets"].get(b, {})
        rows.append([m, vn.replace("alachua-2025.", ""), "%.4f" % v["cosine_to_original"]["mean"], "%.4f" % v["cosine_to_original"]["p01"],
                     pci(v.get("kind_phrases", {}).get("accuracy")), pts(v.get("kind_phrases", {}).get("difference_from_original")),
                     pci(l.get("tuned_top1")), pts(l.get("tuned_top1_difference_from_original"))])
write("variants.md", "# Quantized vectors against the original model's vectors\n\n" + GEN % "docs/eval/study1.json" + "\n\n"
      "The same %d test photos, the same settings as for the original vectors. `int8*` vectors were computed by onnxruntime on a build machine; `wasm-int8-per-channel` vectors were computed by the browser's WASM runtime, which is what a phone runs. "
      "Differences are paired over photos.\n\n" % P["test_rows"]
      + table(["Model", "Vectors", "Mean cosine to original", "1st percentile", "Kind from phrases", "Difference (points)", "Species top-1 with prior", "Difference (points)"], rows, ["---", "---"] + ["---:"] * 6))

for m in models:
    r = S1["models"][m]
    b = r.get("best_labelset_on_val")
    if not b:
        continue
    v = r["labelsets"][b]
    t = v["tuned"]
    L = ["# %s on the test split" % m, "", GEN % "docs/eval/study1.json", "",
         "Species rows made from the %s; settings chosen on `val`: %s. Top-1 %s without the prior and %s with it." % (NAMES[b], json.dumps(t["settings"]), pci(v["plain"]["top1"]), pci(t["top1"])), ""]
    for key, title, first in (("kind", "By kind of eye", "Kind"), ("class", "By class", "Kingdom / class"), ("records", "By how often the species was recorded before 2025", "Records before 2025"), ("month", "By calendar month", "Month")):
        L += ["## " + title, "", table([first, "Photos", "Top-1 with prior", "Top-5 with prior", "Top-1 without prior"], [[g["group"], g["n"], pci(g["top1"]), pci(g["top5"]), pc(g["top1_no_prior"])] for g in v["breakdown"][key]]), ""]
    c = r.get("kind_phrases", {}).get("confusion")
    if c:
        L += ["## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)", "",
              "Accuracy %s. Photos called `person`: %s; called `none`: %s (the test split holds neither)." % (pci(r["kind_phrases"]["accuracy"]), pc(r["kind_phrases"]["called_person"], 2), pc(r["kind_phrases"]["called_none"], 2)), "",
              table(["true \\ said"] + c["columns"], [[a_] + row for a_, row in zip(c["rows"], c["counts"])]), ""]
    c = v["kind_confusion_from_top"]
    L += ["## Kind of eye taken from the top species, with the prior", "", "Accuracy %s." % pci(t["kind_from_top"]), "", table(["true \\ said"] + c["columns"], [[a_] + row for a_, row in zip(c["rows"], c["counts"])]), ""]
    ms = v["mistakes_summary"]
    L += ["## Commonest mistakes", "",
          "Of %d wrong answers for species that are in the list, %d named another species of the same genus and %d another species of the same family. %d test photos show a species that is not in the list." % (ms["wrong_with_species_in_list"], ms["same_genus"], ms["same_family"], ms["species_not_in_list"]), "",
          table(["Photos", "The species", "What was said", "Observations"], [[x["photos"], "*%s* (%s)" % (x["true"], x["true_en"] or "no English name"), "*%s* (%s)" % (x["said"], x["said_en"] or "no English name"), " ".join("[%s](%s)" % (u.rsplit("/", 1)[1], u) for u in x["observations"])] for x in v["commonest_mistakes"]], ["---:", "---", "---", "---"]), ""]
    write("model-%s.md" % m, "\n".join(L))

if CH:
    write("checks.md", "# Checks for leakage and for mistakes in the inputs\n\n" + GEN % "docs/eval/checks.json" + "\n\n" + table(["Verdict", "Check", "What was found"], [[c["verdict"], c["check"], c["detail"]] for c in CH["checks"]], ["---", "---", "---"]))

# ---------------------------------------------------------------- docs/EVAL.md
b2 = S1["models"].get("bioclip2-l14")
T = []
T += ["# Evaluation: what the recognizers get right, and how we know", "",
      "_This file is written by `tools/eval/report.py` from the JSON files under `docs/eval/`, which the scripts in `tools/eval/` produce. Do not edit it by hand. The commands are at the end._", "",
      "## What was measured", "",
      "The question is how often a model names the right species, and the right kind of eye, for a photo of a living thing taken in Alachua County, Florida.", "",
      "- **The photos.** The evaluation set `alachua-2025` holds 6,000 research-grade iNaturalist photos dated 2025-01-01 to 2026-09-29, one photo an observation (`data/eval/alachua-2025/SUMMARY.md`). A hash of the record's id puts %d photos in `val` and %d in `test`. Every setting is chosen on `val`. Every number below comes from `test`." % (P["val_rows"], P["test_rows"]),
      "- **The list.** A model answers with one of the %d species recorded in the county through 2024 (`data/regions/us-fl-alachua/species.json`). The list also gives each species' records by calendar month, and its kind of eye." % P["species_in_list"]["1"],
      "- **Scoring against sentences.** Each species becomes a row made by the model's text half from sentences that hold its name. A photo's score for a species is the cosine between the photo's vector and that row. Three kinds of rows were tried: the scientific name, the English name, and the taxonomy followed by the English name in the form BioCLIP was trained on.",
      "- **The prior.** The place-and-season prior adds `alpha * log(share)` to a species' score, where `share` is the species' part of all records of that calendar month. A month's weight for a species is its records in that month, plus `lam` times a twelfth of its yearly records, plus `c`. This is the arithmetic of `tools/fusion/fuse.py`, with the smoothing written into the table's monthly weights.",
      "- **Intervals.** Each share is followed by a 95%% percentile interval from %d bootstrap resamples over photos (seed %d). The intervals describe the luck of which photos were drawn. They say nothing about photos of another kind." % (meth["resamples"], meth["seed"]),
      "- **People, pets, livestock and rooms.** The wildlife photos hold no people, no photos with nothing alive in them and almost no pets. The extra set `coco-kinds` (`data/extra/coco-kinds/SUMMARY.md`) holds 10,240 photos from COCO 2017 filed as `person`, `cat`, `dog`, `deer` (horses, cows and sheep) and `none` (rooms and objects). "
      "`tools/eval/kinds.py` cuts COCO's own training rows by a hash of the row id into a part for fitting kind rows (two thirds) and a part that joins the wildlife `val` photos whenever a setting of the kind decision is chosen (one third); COCO's own validation rows are the test rows and are only reported. "
      "A COCO photo has no date that means a season, so each is given a calendar month by a hash of its id. The number a kind decision is tuned on is the mean of the share right on the wildlife tuning photos and of the mean share right over the extra set's five kinds, because nobody knows what share of a phone's photos are of people or of rooms.", ""]

T += ["## The main table", "",
      "Test split, %d photos. For each model the species rows are the label set that did best on `val`. The kind of eye is given twice: from the model's own kind phrases (`labels/kinds.json`, seventeen rows that include `person` and `none`), and from the kind of the top species with the prior." % P["test_rows"], ""]
rows = []
for m in models:
    r = S1["models"][m]
    b = r.get("best_labelset_on_val")
    if not b:
        rows.append([m, "–", "–", "no text half: Study 2 only", "–", "–", "–", "–"])
        continue
    v = r["labelsets"][b]
    rows.append([m, pci(r["kind_phrases"]["accuracy"]), pci(v["tuned"]["kind_from_top"]), NAMES[b], pci(v["plain"]["top1"]), pci(v["plain"]["top5"]), pci(v["tuned"]["top1"]), pci(v["tuned"]["top5"])])
T += [table(["Model", "Kind from phrases", "Kind from top species", "Species rows from", "Top-1", "Top-5", "Top-1 with prior", "Top-5 with prior"], rows, ["---", "---:", "---:", "---", "---:", "---:", "---:", "---:"]), "",
      "All label sets, the gain from the prior with its interval, and the chosen settings are in [`docs/eval/labelsets.md`](eval/labelsets.md). One file a model, with the breakdowns, the confusion tables and the commonest mistakes, is at `docs/eval/model-<id>.md`.", ""]

T += ["## Baselines and the ceiling", "",
      "- A recognizer held to the list can be right on at most %s of test photos, because %d of %d show a species with no record in the county before 2025. Held to species with at least 3 records the ceiling is %s, and with at least 10 records it is %s." % (pc(P["ceiling"]["1"]), P["test_rows_species_not_in_list"], P["test_rows"], pc(P["ceiling"]["3"]), pc(P["ceiling"]["10"])),
      "- The prior alone, with no photo, names the species in %s of test photos and has it in its first five in %s. Always answering with the county's most recorded species is right in %s." % (pci(P["top1"]), pci(P["top5"]), pci(P["most_recorded_species_every_time"])),
      "- Always answering `plant`, the commonest kind, is right about the kind in %s." % pci(P["commonest_kind_every_time"]),
      "- With the species rows shuffled, top-1 falls to %s for BioCLIP 2, which is what chance gives. The scores therefore depend on which row belongs to which species." % (pc(b2["labelsets"]["species_sci"]["shuffled_rows_top1"], 2) if b2 else "–"), ""]

if b2:
    v = b2["labelsets"]["species_sci"]
    t = v["tuned"]
    rec = {g["group"]: g for g in v["breakdown"]["records"]}
    kinds = sorted([g for g in v["breakdown"]["kind"] if g["n"] >= 30], key=lambda g: g["top1"][0])
    na = v["names_agree_only"]
    T += ["## BioCLIP 2 in more detail", "",
          "BioCLIP 2 (ViT-L/14) scored against scientific names is right about the species in %s of test photos, and has the species in its first five in %s. With the prior these become %s and %s; the paired gain in top-1 is %s points. The same computation written twice by different hands (`tools/eval/firstcheck.py` and `tools/eval/study1.py`) gives the same top-1 and top-5 without the prior." % (
              pci(v["plain"]["top1"]), pci(v["plain"]["top5"]), pci(t["top1"]), pci(t["top5"]), pts(t["top1_gain_over_plain"])), "",
          ] + (["- **Photos that belong together.** Several photos of one species on one day often come from one outing, so they are less than independent. Resampling whole groups (one species on one day, %d groups) instead of single photos gives %s without the prior and %s with it, against the intervals above." % (
              v["clustered"]["plain_top1"][4], pci(v["clustered"]["plain_top1"]), pci(v["clustered"]["tuned_top1"]))] if v.get("clustered") else []) + [
          "- **Rare species lose under the prior.** For species with 1 or 2 records before 2025, top-1 is %s with the prior and %s without it (%d photos); for 3 to 9 records, %s and %s (%d photos). For species with 200 or more records it is %s and %s (%d photos). The prior buys its gain on common species and pays for it on rare ones." % (
              pc(rec["1 or 2 records"]["top1"][0]), pc(rec["1 or 2 records"]["top1_no_prior"]), rec["1 or 2 records"]["n"], pc(rec["3 to 9"]["top1"][0]), pc(rec["3 to 9"]["top1_no_prior"]), rec["3 to 9"]["n"],
              pc(rec["200 or more"]["top1"][0]), pc(rec["200 or more"]["top1_no_prior"]), rec["200 or more"]["n"]),
          "- **By kind of eye** (kinds with at least 30 test photos), top-1 with the prior runs from %s for `%s` to %s for `%s`." % (pc(kinds[0]["top1"][0]), kinds[0]["group"], pc(kinds[-1]["top1"][0]), kinds[-1]["group"]),
          "- **Its own kind phrases are weak.** Asked for the kind of eye through the kind phrases, BioCLIP 2 is right in %s. Taking the kind from its top species is right in %s. A biology model knows species names far better than everyday words such as \"a wading bird\"." % (pci(b2["kind_phrases"]["accuracy"]), pci(t["kind_from_top"])),
          "- **Names that differ between GBIF and iNaturalist.** %d test photos are of species whose GBIF name differs from the name iNaturalist uses. They were found from %s. Top-1 without the prior is %s on those photos and %s on the rest, so scoring against GBIF's names did not lower the result on these photos." % (
              na["rows_left_out"], b2["differing_names_rule"], pci(na["plain_top1_on_rows_left_out"]), pci(na["plain_top1"])),
          "- **Mistakes.** Of %d wrong answers for species in the list, %d named a species of the same genus and %d one of the same family. The table of commonest mistakes, with links to the observations, is in [`docs/eval/model-bioclip2-l14.md`](eval/model-bioclip2-l14.md)." % (
              v["mistakes_summary"]["wrong_with_species_in_list"], v["mistakes_summary"]["same_genus"], v["mistakes_summary"]["same_family"]), ""]
    b25 = S1["models"].get("bioclip25-h14")
    if b25:
        w = b25["labelsets"]["species_sci"]
        T += ["BioCLIP 2.5 (ViT-H/14) reaches %s without the prior and %s with it. Its model card does not give the date of its training data, so it cannot be shown that the test photos are new to it. That number is reported with this caveat and is kept out of any claim the app makes." % (pci(w["plain"]["top1"]), pci(w["tuned"]["top1"])), ""]

T += ["## The models small enough for a phone, scored against sentences", ""]
rows = []
for m in ("tinyclip-39m-16", "tinyclip-8m-16"):
    r = S1["models"].get(m)
    if not r:
        continue
    b = r["best_labelset_on_val"]
    v = r["labelsets"][b]
    w = r["variants"].get("alachua-2025.wasm-int8-per-channel")
    rows.append([m, "%.1f MB" % ((r["card"].get("ship_bytes") or 0) / 1e6), pci(r["kind_phrases"]["accuracy"]), pci(v["tuned"]["kind_from_sum"]), pci(v["plain"]["top1"]), pci(v["tuned"]["top1"]), pci(v["tuned"]["top5"]),
                 pci(w["labelsets"][b]["tuned_top1"]) if w else "–", pts(w["labelsets"][b]["tuned_top1_difference_from_original"]) if w else "–"])
T += [table(["Model", "File the phone downloads", "Kind from phrases", "Kind from summed species", "Top-1", "Top-1 with prior", "Top-5 with prior", "Top-1 with prior, WASM int8 vectors", "WASM against original (points)"], rows), "",
      "Scored against sentences, the small general models name the species in about a quarter to a third of test photos with the prior. That is too weak to show a species name on its own. Their kind of eye from phrases is right in about three photos in four. "
      "The vectors a phone computes (WASM, int8) cost about half a point of species top-1 against the original model's vectors; every quantized set is compared in [`docs/eval/variants.md`](eval/variants.md).", ""]
return_marker = len(T)

# Study 2: the detail goes to docs/eval/study2-<name>.md, a summary comes here.
def s2_title(name, s2):
    if s2.get("sentences_only"):
        return "Sentence rows with the prior, as the page would use them"
    if s2.get("standin"):
        return "Trained heads (Study 2): the machinery, proven on a stand-in"
    return "Heads trained on local photos (Study 2)"


def short_kind(n):
    return n.split(" (")[0] if n.startswith(("kind phrases", "trained on", "the page's combination")) else n.split(" of the head")[0]


for name in sorted(S2, key=lambda k: (bool(S2[k].get("standin")), not S2[k].get("sentences_only"))):
    s2 = S2[name]
    L = ["# %s" % s2_title(name, s2), "", GEN % ("docs/eval/study2-%s.json" % name), "", s2["what"], ""]
    for m, r in s2["models"].items():
        L += ["## %s" % m, "", "Fitted on %d photos of %d species (`%s`); settings chosen on %d tuning photos; tested on %d test photos (`%s`)." % (r["train_photos"], r["train_species"], r["train_vectors"], r["tuning_photos"], r["test_photos"], r["test_vectors"]), ""]
        L += [table(["Species head", "Top-1", "Top-5", "Top-1 with prior", "Top-5 with prior", "Kind from summed species", "Chosen on the tuning photos"],
                    [[h["name"], pci(h["plain"]["top1"]), pci(h["plain"]["top5"]), pci(h["prior"]["top1"]), pci(h["prior"]["top5"]), pci(h["prior"].get("kind_from_sum")), h["prior"].get("settings_text", "")] for h in r["species_heads"]],
                    ["---", "---:", "---:", "---:", "---:", "---:", "---"]), ""]
        if r.get("kind_heads"):
            L += [table(["Kind of eye from", "Right kind", "Called `person`", "Called `none`"], [[h["name"], pci(h["accuracy"]), pc(h.get("called_person"), 2), pc(h.get("called_none"), 2)] for h in r["kind_heads"]]), ""]
        if r.get("kind_decision"):
            L += kind_decision_lines(r["kind_decision"])
        if r["train_photos"] and r.get("by_train_photos"):
            L += ["Top-1 with the prior for each head, by how many fitting photos the species has:", "",
                  table(["Fitting photos of the species", "Test photos"] + r["by_train_photos"]["heads"], [[g["group"], g["n"]] + [pc(x) for x in g["top1"]] for g in r["by_train_photos"]["rows"]]), ""]
        c = r.get("confidence")
        if c:
            L += ["**Confidence.** %s" % c["text"], "", table(["Top probability", "Tuning photos", "Mean probability", "Share right"], [["%.1f to %.1f" % (x["from"], x["to"]), x["photos"], pc(x["mean_probability"]), pc(x["right"])] for x in c["reliability_on_tuning_photos"]]), ""]
        L += ["- " + note for note in r.get("notes", [])] + [""]
    write("study2-%s.md" % name, "\n".join(L))
    ms = list(s2["models"])
    T += ["## " + s2_title(name, s2), "", s2["what"], ""]
    heads = []
    for m in ms:
        for h in s2["models"][m]["species_heads"]:
            if h["name"] not in heads:
                heads.append(h["name"])
    get = lambda m, hn: next((h for h in s2["models"][m]["species_heads"] if h["name"] == hn), None)
    T += ["Species top-1 with the prior on the test photos%s:" % (" (the pocket models on the vectors a phone computes)" if any("wasm" in s2["models"][m]["test_vectors"] for m in ms) else ""), "",
          table(["Species head"] + ms, [[hn] + [pci(get(m, hn)["prior"]["top1"]) if get(m, hn) else "–" for m in ms] for hn in heads]), ""]
    kn = []
    for m in ms:
        for h in s2["models"][m]["kind_heads"]:
            if short_kind(h["name"]) not in kn:
                kn.append(short_kind(h["name"]))
    def kget(m, k):
        return next((h for h in s2["models"][m]["kind_heads"] if short_kind(h["name"]) == k), None)
    rows = [[k] + [pci(kget(m, k)["accuracy"]) if kget(m, k) else "–" for m in ms] for k in kn]
    T += ["Kind of eye right on the test photos:", "", table(["Kind of eye from"] + ms, rows), ""]
    kdm = [m for m in ms if s2["models"][m].get("kind_decision")]
    if kdm:
        rows = []
        for m in kdm:
            kd = s2["models"][m]["kind_decision"]
            for label, c in (("chosen", kd["chosen"]), ("what the wildlife photos alone would choose", kd["chosen_on_wildlife_alone"])):
                tw, tx = c["test_wildlife"], c.get("test_extra")
                by = {g["kind"]: g for g in c.get("test_extra_by_kind", [])}
                rows.append([m, label, "%s; rule `%s`, t_kind %g, w_kind %g" % (c["head"], c["rule"], c["t_kind"], c["w_kind"]), pci(tw["kind_right"]), pci(tx["kind_right"]) if tx else "–"] + [pc(by[k]["right"][0]) if k in by else "–" for k in ("person", "none", "cat", "dog", "deer")])
        T += ["The kind decision on the wildlife test photos and on the extra set's test photos (people, rooms with nothing alive, cats, dogs, grazing animals). The second row of each model shows what tuning on wildlife photos alone, as the first export did, would have chosen:", "",
              table(["Model", "", "Kinds head and settings", "Kind right, wildlife test", "Kind right, extra test", "`person`", "`none`", "`cat`", "`dog`", "`deer`"], rows, ["---", "---", "---"] + ["---:"] * 7), ""]
    for note in sorted({n_ for m in ms for n_ in s2["models"][m].get("notes", [])}):
        T += ["- " + note]
    T += ["", "Every head, its settings, the reliability tables and the breakdown by fitting photos are in [`docs/eval/study2-%s.md`](eval/study2-%s.md)." % (name, name), ""]

if SH:
    T += ["## What the page would show", "",
          "Each slot below was written by `tools/eval/export_heads.py` in the layout of `models/<slot>/` and then scored by `tools/eval/shipped.py`, which reads the slot's own files as the page does and sends every photo through `tools/fusion/fuse.py`. "
          "The two thresholds were set on the tuning photos so that a named species, and the three offered species, were right at least nine times in ten there. Slots whose name begins with `val-` hold stand-in heads. A name that ends in `-wasm-int8` or the like is the same slot scored on other vectors of the same photos (the larger model's int8 file as the browser runs it). The kinds head, its temperature, its weight and the rule (`mix` or `product`, both in the page since build 7) were chosen by Study 2 as described above.", ""]
    rows = []
    for name in sorted(SH, key=lambda k: (k.startswith("val-"), k)):
        n = SH[name]["numbers"]
        rows.append(["`%s`" % name, pci(n["kind_right"]), pci(n["species_top1"]), "%s at %s" % (pc(n["named"][0]), n["name_at"] if n["name_at"] is not None else "never"), pci(n["named_right"]),
                     "%s at %s" % (pc(n["offered"][0]), n["offer_at"] if n["offer_at"] is not None else "never"), pci(n["offered_holds_species"]), pc(n["kind_only"][0]), pci(n["kind_only_kind_right"])])
    T += [table(["Slot", "Kind right", "Top species right", "Species named (share, threshold)", "Named species right", "Three offered (share, threshold)", "Offer holds the species", "Kind only", "Kind right when kind only"], rows), ""]
    # the kind of eye with the answer "not sure"
    krows = []
    for name in sorted(SH, key=lambda k: (k.startswith("val-"), k)):
        k = SH[name]["numbers"].get("kind")
        if not k:
            continue
        tw, tx = k["test_wildlife"], k.get("test_extra")
        krows.append(["`%s`" % name, ("%.2f" % k["kind_at"]) if k["kind_at"] is not None else "none", "yes" if "extra" in k["tuned_on"] else "no", pci(tw["kind_right"]), pci(tw["asserted"]), pci(tw["asserted_right"]), pci(tw["not_sure_true_kind_among_three"]),
                      pci(tx["kind_right"]) if tx else "–", pci(tx["asserted"]) if tx else "–", pci(tx["asserted_right"]) if tx else "–", pci(tx["not_sure_true_kind_among_three"]) if tx else "–", pci(k.get("test_extra_named")) if tx else "–"])
    if krows:
        T += ["**Not sure is an answer.** Under `fusion.kind_at` the page asserts no kind, says that it is not sure and offers its three likeliest kinds. `tools/eval/shipped.py` sets the level through `fuse.py` as the lowest one from which an asserted kind was right at least 95 times in 100 on the wildlife tuning photos and, taken by itself, on the tuning third of the extra set. "
              "The table gives what then happens on the wildlife test photos and on the extra set's test photos. A slot whose third column says `no` was tuned before its model's vectors of the extra set were published: its level and its settings have never been asked about a person or an empty room.", "",
              table(["Slot", "kind_at", "Tuned with the extra set", "Kind right, wildlife test", "Kind asserted", "Right when asserted", "True kind among the three when not sure", "Kind right, extra test", "Kind asserted", "Right when asserted", "True kind among the three when not sure", "A species named on an extra photo"], krows), ""]
    L = ["# Exported slots, scored as the page would", "", GEN % "docs/eval/shipped-*.json", ""]
    for name in sorted(SH, key=lambda k: (k.startswith("val-"), k)):
        sh = SH[name]
        L += ["## `%s`" % name, "", sh["text"], "", table(["What the page would show", "Share of test photos", "Right"], [[x["what"], pc(x["share"]), x["right"]] for x in sh["outcomes"]], ["---", "---:", "---"]), ""]
        k = sh["numbers"].get("kind")
        if k:
            L += ["The kind of eye on the wildlife test photos, one row a true kind (kind_at %s):" % (("%.2f" % k["kind_at"]) if k["kind_at"] is not None else "none"), "", extra_table(k["table_wildlife"], "True kind"), ""]
            said_table = lambda rows: table(["Kind asserted", "Photos", "Right", "Commonest true kind when wrong"], [[g["said"], g["asserted"], pci(g["right"]), g["commonest_true_kind_when_wrong"] or "–"] for g in rows], ["---", "---:", "---:", "---"])
            if k.get("asserted_wildlife"):
                L += ["The same photos by the kind the page asserted:", "", said_table(k["asserted_wildlife"]), ""]
            if k.get("table_extra"):
                L += ["The kind of eye on the extra set's test photos (`%s`):" % k["test_extra_vectors"], "", extra_table(k["table_extra"]), ""]
            if k.get("asserted_extra"):
                L += ["The extra set's test photos by the kind the page asserted:", "", said_table(k["asserted_extra"]), ""]
            lv = []
            for l in k.get("levels", []):
                if l.get("kind_at") is None:
                    lv.append(["%d in 100" % round(100 * l["right_at_least"]), "no level reached it"] + ["–"] * 6)
                else:
                    tw, tx = l["test_wildlife"], l.get("test_extra")
                    lv.append(["%d in 100" % round(100 * l["right_at_least"]), "%.2f" % l["kind_at"], pci(tw["asserted"]), pci(tw["asserted_right"]), pci(tw["not_sure_true_kind_among_three"]), pci(tx["asserted"]) if tx else "–", pci(tx["asserted_right"]) if tx else "–", pci(tx["not_sure_true_kind_among_three"]) if tx else "–"])
            L += ["Other bars for an asserted kind, each level set on the tuning photos:", "", table(["Asserted kind right at least", "kind_at", "Asserted, wildlife test", "Right when asserted", "True kind among the three when not sure", "Asserted, extra test", "Right when asserted", "True kind among the three when not sure"], lv), ""]
    write("shipped.md", "\n".join(L))
    lrows = []
    for name in sorted(SH, key=lambda k: (k.startswith("val-"), k)):
        if name.startswith("val-"):
            continue
        for l in SH[name]["numbers"].get("levels", []):
            if l.get("name_at") is None:
                lrows.append(["`%s`" % name, "%d in 100" % round(100 * l["right_at_least"]), "no level reached it", "–", "–", "–", "–", "–", "–"])
            else:
                lrows.append(["`%s`" % name, "%d in 100" % round(100 * l["right_at_least"]), "%.2f" % l["name_at"], pci(l["named"]), pci(l["named_right"]),
                              ("%.2f" % l["offer_at"]) if l.get("offer_at") is not None else "never", pci(l.get("offered")), pci(l.get("offered_holds_species")), pci(l.get("kind_only"))])
    if lrows:
        T += ["A stricter bar for naming is available. The table gives, for a named species that has to be right at least 90, 95 or 98 times in 100 on `val`, the threshold that `val` gives and what then happens on the test photos. "
              "For each bar the offer threshold was set again on `val`, for the photos left without a name, so that the three offered species hold the right one nine times in ten. "
              "The slots scored with `--name-bar 0.92` add a row for 92 in 100. The shares in this table leave out the page's rule that no species is named while the kind is not sure (`fusion.kind_at`), which the table above applies, so for a slot with `kind_at` the share named can be lower there and the share right higher.", "",
              table(["Slot", "Named species right at least", "name_at", "Photos named", "Named species right", "offer_at", "Photos offered three", "Offer holds the species", "Kind only"], lrows), ""]
    T += ["The text for each slot, with what it needs from the page, is in [`docs/eval/shipped.md`](eval/shipped.md).", ""]

# ---- the larger model as a phone would run it
VAR = {os.path.basename(p_)[8:-5]: json.load(open(p_, encoding="utf-8")) for p_ in sorted(glob.glob(os.path.join(D, "variant-*.json")))}
if VAR:
    v0 = next(iter(VAR.values()))
    T += ["## The larger model on the device", "",
          "The species service has no free server to live on, so BioCLIP 2's image encoder is offered as a download and runs on the device. The laboratory made int8 files of it and ran each through onnxruntime-web's WASM build on %d test photos (every k-th test row). "
          "`tools/eval/variant.py` sent those vectors, and the original model's vectors of the same photos, through `fuse.py` with the slot `%s` and its thresholds (name_at %g, offer_at %g, the levels set on `val` for a named species right 98 times in 100). Every difference is paired over the same photos. "
          "No threshold was set again: the laboratory's vectors hold test photos only, and a threshold may be set on `val` alone." % (v0["test_photos"], v0["slot"], v0["fusion"]["name_at"], v0["fusion"]["offer_at"]), ""]
    rows = []
    for name, v in VAR.items():
        o, n, d = v["original"], v["variant"], v["paired_difference"]
        rows.append(["`%s`" % name, "%.4f (%.4f)" % (v["cosine_to_original"]["mean"], v["cosine_to_original"]["p01"]), pci(o["species_top1"]), pci(n["species_top1"]), pts(d["top1"]), pci(n["species_top5"]), pci(n["kind_right"]),
                     pci(o["named"]), pci(n["named"]), pci(n["named_right"]), pci(v["same_top_species"])])
    T += [table(["Vectors", "Cosine to the original (1st percentile)", "Top species right, original vectors", "Top species right, these vectors", "Paired difference (points)", "First five", "Kind right", "Species named, original", "Species named, these", "Named species right, these", "Same top species as the original"], rows), "",
          "With %d photos an interval is several points wide, so these figures can show a large loss and cannot show a small one. The sources of the vectors: %s." % (v0["test_photos"], "; ".join("`%s`: %s" % (k_, v_["vectors"]) for k_, v_ in VAR.items())), ""]

# ---- decisions: sentences around numbers that the studies wrote
real = next((v for k, v in S2.items() if not v.get("standin") and not v.get("sentences_only")), None)
CARDS = (CH or {}).get("cards", {})
m39, m8 = S1["models"].get("tinyclip-39m-16"), S1["models"].get("tinyclip-8m-16")
WV = "alachua-2025.wasm-int8-per-channel"
T += ["## Decisions", ""]
if m39 and m8 and WV in m39["variants"] and WV in m8["variants"]:
    def wasm(r):
        v = r["variants"][WV]
        return v["kind_phrases"]["accuracy"], v["labelsets"][r["best_labelset_on_val"]]["tuned_top1"]
    k39, s39 = wasm(m39)
    k8, s8 = wasm(m8)
    lat = lambda mid: ("about %d ms a photo" % round(CARDS[mid]["wasm_ms_per_photo"])) if CARDS.get(mid, {}).get("wasm_ms_per_photo") else "a time given in its card"
    txt = ("On the vectors a phone computes, and scored against sentences, TinyCLIP 39M/16 gets the kind of eye from phrases right for %s and the species with the prior for %s; TinyCLIP 8M/16 gets %s and %s. "
           "The first is a %.1f MB download and took %s in the laboratory's one-thread WASM run; the second is %.1f MB and took %s. " % (
               pci(k39), pci(s39), pci(k8), pci(s8), m39["card"]["ship_bytes"] / 1e6, lat("tinyclip-39m-16"), m8["card"]["ship_bytes"] / 1e6, lat("tinyclip-8m-16")))
    if real and "tinyclip-39m-16" in real["models"] and "tinyclip-8m-16" in real["models"]:
        def best(r):
            h = next(h for h in r["species_heads"] if h["name"] == r["chosen_species_head"]["name"])
            return h
        h39, h8 = best(real["models"]["tinyclip-39m-16"]), best(real["models"]["tinyclip-8m-16"])
        txt += ("With heads fitted on the training photos, the 39M model's best head (`%s`) names the species for %s of test photos with the prior and the 8M model's (`%s`) for %s. "
                "Which of the two ships is worked out in the next lines, by the kind of eye as the page would decide it." % (
                    h39["name"], pci(h39["prior"]["top1"]), h8["name"], pci(h8["prior"]["top1"])))
    else:
        txt += ("Heads fitted on the real training photos have not been measured, because the training vectors were not published when this report was written. They decide this choice: a trained head may close the gap between the two models or widen it. ")
        a39, a8 = SH.get("sentences-tinyclip-39m-16"), SH.get("sentences-tinyclip-8m-16")
        if a39 and a8:
            n39, n8 = a39["numbers"], a8["numbers"]
            txt += ("What can ship before then is each model's sentence rows with the prior. Scored as the page would, the 39M slot gets the kind of eye right for %s, names a species for %s of test photos and is right for %s of those names; the 8M slot gets %s, %s and %s. "
                    "Which of the two ships is worked out in the next lines." % (
                        pci(n39["kind_right"]), pc(n39["named"][0]), pci(n39["named_right"]), pci(n8["kind_right"]), pc(n8["named"][0]), pci(n8["named_right"])))
    T += ["- **The pocket model.** " + txt]
DEC = load("decision-pocket.json")
if DEC:
    d = DEC["deciding_difference"]
    T += ["- **The pocket model, by the rule set down beforehand** (`tools/eval/decide.py`). %s Compared: the slots `%s` and `%s`, scored through `fuse.py` on the same photos. %s By this rule the slot is `%s` (branch `%s`).%s" % (
        DEC["rule"], DEC["slots_compared"]["tinyclip-39m-16"], DEC["slots_compared"]["tinyclip-8m-16"], DEC["why"], DEC["slot"], DEC["branch"],
        (" This choice is provisional: it was made %s. `tools/eval/decide.py` makes it again from the trained slots when they exist." % " and ".join(
            ([("from sentence-made slots, before heads fitted on the training photos were measured")] if DEC["train"] != "alachua-pre2025" else []) +
            ([("on wildlife photos alone, before both models' vectors of the extra set were published")] if "extra" not in DEC["sets"] else []))) if DEC.get("provisional") else ""), "",
          table(["Photos", "Measure", "TinyCLIP 39M/16", "TinyCLIP 8M/16", "Paired difference (points)"], [[m_["photos"] + " test", m_["measure"], pc(m_["tinyclip-39m-16"]), pc(m_["tinyclip-8m-16"]), pts(m_["difference"])] for m_ in DEC["measures"]], ["---", "---", "---:", "---:", "---:"]), ""]
if b2:
    v = b2["labelsets"]["species_sci"]
    t = v["tuned"]
    st = t["settings"]
    b25 = S1["models"].get("bioclip25-h14")
    T += ["- **The server.** BioCLIP 2 (ViT-L/14) with rows made from scientific names, all %d species of the list, and the prior (alpha %g at temperature %g, smoothing lam %g and c %g): top-1 %s, top-5 %s, and the kind of eye from summed species probabilities right for %s. "
          "The kind of eye should come from the species list and the kind phrases should count for little, because this model's kind phrases alone are right for %s.%s" % (
              st["species_in_list"], st["alpha_prior"], st["t_species"], st["lam"], st["c"], pci(t["top1"]), pci(t["top5"]), pci(t["kind_from_sum"]), pci(b2["kind_phrases"]["accuracy"]),
              (" BioCLIP 2.5 measures %s with the prior%s.%s The date of BioCLIP 2.5's training data is undocumented, so it cannot be shown that the test photos are new to it, and no number for it can be defended in public. BioCLIP 2 is the one to run." % (
                  pci(b25["labelsets"]["species_sci"]["tuned"]["top1"]), (", a paired difference of %s points from BioCLIP 2 on the same photos" % pts(b25["against_bioclip2_l14"]["top1_with_prior_difference"])) if b25.get("against_bioclip2_l14") else "",
                  (" The laboratory's runs embedded %.1f photos a second with BioCLIP 2 and %.1f with BioCLIP 2.5 on build machines without a graphics card." % (CARDS["bioclip2-l14"]["torch_photos_per_second"], CARDS["bioclip25-h14"]["torch_photos_per_second"]))
                  if CARDS.get("bioclip2-l14", {}).get("torch_photos_per_second") and CARDS.get("bioclip25-h14", {}).get("torch_photos_per_second") else "")) if b25 else "")]
    srv = SH.get("sentences-bioclip2-l14")
    if srv:
        f_, n_, e_ = srv["manifest"]["fusion"], srv["numbers"], srv["manifest"]["evaluation"]
        T += ["- **The server's files.** The slot `sentences-bioclip2-l14` holds these rows and a table whose monthly weights carry the smoothing (lam %g, c %g), with alpha_prior %g, t_species %g, rule `%s`, t_kind %g and w_kind %g, all chosen on `val`. Scored as the page would, it gets the kind of eye right for %s of test photos and the species for %s. Its settings differ a little from the line above because Study 2 searches a finer grid of prior weights; the two results agree within their intervals." % (
            e_["prior_smoothing"]["lam"], e_["prior_smoothing"]["c"], f_["alpha_prior"], f_["t_species"], f_.get("rule", "product"), f_["t_kind"], f_["w_kind"], pci(n_["kind_right"]), pci(n_["species_top1"]))]
    lv = [l for l in (srv["numbers"].get("levels", []) if srv else []) if l.get("name_at") is not None and l["right_at_least"] == 0.98]
    if lv:
        l = lv[0]
        T += ["- **When the server should name a species.** The nine-in-ten rule lets BioCLIP 2 name a species for nearly every photo, since it is right more often than that overall. A stricter bar suits a name shown to a person: with name_at %.2f, set on `val` for 98 in 100, the slot `sentences-bioclip2-l14` names a species for %s of test photos and is right for %s of those names%s. The other bars are in the table under \"What the page would show\"." % (
            l["name_at"], pci(l["named"]), pci(l["named_right"]),
            ("; with offer_at %.2f it offers three species for %s and they hold the right one for %s, and %s get a kind of eye only" % (l["offer_at"], pci(l["offered"]), pci(l["offered_holds_species"]), pci(l["kind_only"]))) if l.get("offer_at") is not None else "")]
    T += ["- **What the app may say about the server.** A sentence the measurements support: \"On photos from Alachua County that iNaturalist's community had already identified, taken in 2025 and 2026, this recognizer named the species for about %d photos in 100.\" It may add that such photos are easier than a photo taken in passing. It may not compare itself with iNaturalist's model." % int(100 * t["top1"][1])]
live = SH.get("live-pocket")
if live:
    k_, n_, f_ = live["numbers"].get("kind") or {}, live["numbers"], live["manifest"]["fusion"]
    tw_, tx_ = k_.get("test_wildlife"), k_.get("test_extra")
    T += ["- **The slot that is live.** `live-pocket` in the tables is `models/pocket` as it stands on `main`: TinyCLIP 39M/16, sentence rows, and the interim settings chosen by hand (rule `%s`, t_kind %g, w_kind %g). Through `fuse.py` it gets the kind of eye right for %s of the wildlife test photos and names a species for %s, rightly for %s of those names. "
          "%s%s" % (f_.get("rule", "product"), f_["t_kind"], f_["w_kind"], pci(n_["kind_right"]), pc(n_["named"][0]), pci(n_["named_right"]),
                    ("For these settings `kind_at` comes out as %.2f: the page then asserts a kind for %s of the wildlife test photos and is right for %s of those, and where it is not sure the true kind is among its three likeliest for %s. " % (
                        k_["kind_at"], pci(tw_["asserted"]), pci(tw_["asserted_right"]), pci(tw_["not_sure_true_kind_among_three"]))) if k_.get("kind_at") is not None else "No level of `kind_at` reached 95 in 100 for these settings. ",
                    ("On the extra set's test photos (people, cats, dogs, grazing animals, rooms) it gets the kind right for %s, asserts for %s and is right for %s of those." % (pci(tx_["kind_right"]), pci(tx_["asserted"]), pci(tx_["asserted_right"]))) if tx_ else
                    "That level was set on wildlife photos alone, because the pocket models' vectors of the extra set were not published when this was written; it says nothing about people or rooms, for which the only evidence is the fifteen sample photos of `tools/eval/interim.py`.")]
if VAR:
    best = min(VAR.items(), key=lambda kv: -kv[1]["variant"]["species_top1"][0])
    T += ["- **The larger model on the device.** The head files are the slot `%s` with name_at %g and offer_at %g. On the laboratory's %d test photos the int8 vectors computed by the browser's WASM runtime change the top species for few photos (table above), and a named species stays right as often as with the original vectors, so the thresholds are kept. "
          "They could not be set again on int8 vectors, since no `val` photo has any. `tools/eval/naturalist.py` writes the files for `models/naturalist` and, given the laboratory's `parts.json`, lists the parts of the int8 file in the manifest's `vision` block; they are published as the branch `pub/heads-naturalist-bioclip2-l14`." % (
              best[1]["slot"], best[1]["fusion"]["name_at"], best[1]["fusion"]["offer_at"], best[1]["test_photos"])]
DECV = load("decision-pocket-val.json")
if DECV and DEC and DEC["train"] != "alachua-pre2025":
    dv = DECV["deciding_difference"]
    T += ["- **The same comparison on slots whose kind rows are fitted on photos.** The sentence slots above are the weakest form of either model on people and rooms. The stand-in slots `%s` and `%s` carry kind rows fitted on wildlife photos and on the extra set's fitting part, which is the form the trained slots will have. "
          "On them TinyCLIP 39M/16 is ahead of TinyCLIP 8M/16 by %s points on %s, paired over the same photos, and the rule's answer there is `%s`. This second look was added after the first answer was seen, so it is evidence and no part of the rule; the trained slots are decided by the rule as written." % (
              DECV["slots_compared"]["tinyclip-39m-16"], DECV["slots_compared"]["tinyclip-8m-16"], pts(dv), "the mean of the share right on the wildlife test photos and on the extra set's test photos" if "extra" in DECV["sets"] else "the wildlife test photos", DECV["choice"]), "",
          table(["Photos", "Measure", "TinyCLIP 39M/16", "TinyCLIP 8M/16", "Paired difference (points)"], [[m_["photos"] + " test", m_["measure"], pc(m_["tinyclip-39m-16"]), pc(m_["tinyclip-8m-16"]), pts(m_["difference"])] for m_ in DECV["measures"]], ["---", "---", "---:", "---:", "---:"]), ""]
if DEC and DEC["train"] == "alachua-pre2025":
    T += ["- **What should ship in the pocket.** The slot `%s`, published as the branch `%s`: the rule's answer on slots whose heads were fitted on the training photos." % (DEC["slot"], DEC["branch"])]
elif DECV and SH.get("val-" + DECV["choice"]):
    w_ = SH["val-" + DECV["choice"]]
    n_, k_ = w_["numbers"], w_["numbers"].get("kind") or {}
    tw_, tx_ = k_.get("test_wildlife"), k_.get("test_extra")
    if tw_ and tx_ and k_.get("kind_at") is not None:
        T += ["- **What should ship in the pocket until the trained slots are measured.** The rule's answer on sentence slots is a tie that falls to the smaller model, and it rests on phrases that neither model should ship with. Of the slots measured so far, the one with the best kind decision is the stand-in `val-%s` (branch `pub/heads-val-%s`): "
              "the kind of eye right for %s of the wildlife test photos and %s of the extra set's test photos; with kind_at %.2f a kind asserted for %s of the wildlife test photos and right for %s of those; a species named for %s and right for %s of those names. "
              "It is a stand-in in two respects: its kind rows and its species rows were fitted on two thirds of the `val` photos (and the kind rows on the extra set's fitting part as well), and its thresholds were set on the remaining %d `val` photos, so they are less steady than thresholds set on all of `val`. "
              "The trained slots replace it when `run/eval/armed-pocket` has run." % (
                  DECV["choice"], DECV["choice"], pci(n_["kind_right"]), pci(tx_["kind_right"]), k_["kind_at"], pci(tw_["asserted"]), pci(tw_["asserted_right"]), pci(n_["named"]), pci(n_["named_right"]), n_["tuning_photos"])]
XN = load("extra-naming-sentences-bioclip2-l14-at-0.78.json")
srv_ = SH.get("sentences-bioclip2-l14")
if XN and srv_ and (srv_["numbers"].get("kind") or {}).get("table_extra"):
    by_ = {g["kind"]: g for g in srv_["numbers"]["kind"]["table_extra"]}
    pn_ = XN["person_or_none"]
    T += ["- **The larger model on people and rooms.** BioCLIP 2's kind phrases say `person` for %s of the extra set's test photos of people and `none` for %s of its photos of rooms, so the kind of such a photo has to come from the pocket model, which runs first. "
          "With name_at %g and offer_at %g the slot names a species on %s of the %d test photos of people and rooms and offers three on %s (`tools/eval/extra_naming.py`). At the nine-in-ten level of the slot's own manifest it names one on %s of the photos of people and %s of the photos of rooms, which is one more reason for the stricter level on the device." % (
              pc(by_["person"]["said_person"]) if "person" in by_ else "–", pc(by_["none"]["said_none"]) if "none" in by_ else "–", XN["fusion"]["name_at"], XN["fusion"]["offer_at"], pci(pn_["named"]), pn_["n"], pci(pn_["offered"]),
              pc(by_["person"]["named"]) if "person" in by_ else "–", pc(by_["none"]["named"]) if "none" in by_ else "–")]
sv = S2.get("val")
if not real:
    tx = ("Fitted heads on the real training set are unmeasured: for both pocket models (prototypes, prototypes with sentence rows, the discriminant head, the map into BioCLIP 2's space) and for BioCLIP 2 itself. "
          "`bash tools/eval/run.sh ROOT alachua-pre2025` measures them, exports the best head of each model as a slot and scores it as the page would. "
          "A build-machine run on the branch `run/eval/armed-pocket` waits for the pocket models' training vectors and then does exactly that; `run/eval/armed-all` also waits for BioCLIP 2's. Both then give the extra set's vectors up to forty minutes to appear and go on with what is published. "
          "Their results come back under `runs/eval/` on the `ci` branch, the slots go to `pub/heads-alachua-pre2025-<model>`, and `docs/eval/decision-pocket.json` in the returned files names the pocket slot to ship. "
          "The whole path was tried in the evaluation sandbox on made-up vectors of the real size (86,915 training rows in the shape of the open-data manifest, with no GBIF record ids); those numbers mean nothing and are kept nowhere.")
    if sv and "bioclip2-l14" in sv["models"]:
        hs = {h["name"]: h for h in sv["models"]["bioclip2-l14"]["species_heads"]}
        if "sentences" in hs and "prototypes + sentences" in hs:
            tx += (" The stand-in gives one hint about BioCLIP 2: adding prototypes from about 1,200 photos to its sentence rows moved top-1 without the prior from %s to %s and top-1 with the prior from %s to %s, so a real gain is not shown yet." % (
                pci(hs["sentences"]["plain"]["top1"]), pci(hs["prototypes + sentences"]["plain"]["top1"]), pci(hs["sentences"]["prior"]["top1"]), pci(hs["prototypes + sentences"]["prior"]["top1"])))
    T += ["- **What waits for the training vectors.** " + tx]
T += [""]

# ---- heads fitted under the licence rule (tools/eval/licences.py), the pocket v3 decision, and the pets and livestock check
LIC = [("all licences (run 25, scored again with build 8's fuse.py)", "alachua-pre2025-tinyclip-39m-16-b8"), ("all licences (run 25 as it ran)", "alachua-pre2025-tinyclip-39m-16"), ("`nc`", "alachua-pre2025-nc-tinyclip-39m-16-at90"), ("`by`", "alachua-pre2025-by-tinyclip-39m-16"),
       ("`nc`, name_at at 92 in 100: the candidate for pocket v3", "alachua-pre2025-nc-tinyclip-39m-16"), ("pocket v2 (live in build 8), scored with build 8's fuse.py", "val-tinyclip-39m-16-b8"), ("pocket v2, the file the rule names (fuse.py before build 8)", "val-tinyclip-39m-16"),
       ("pocket v2 refitted under `nc`", "val-nc-tinyclip-39m-16")]
if any(n_ in SH for _, n_ in LIC[1:4]):
    T += ["## Heads under the licence rule", "",
          "The rule set by the coordinator on 11 October 2026, pending the owner's decision: heads that ship are fitted only on photos in the public domain (CC0, no known copyright restrictions, United States Government work) or shared under CC BY or CC BY-NC, and a list of the photos used (set, id, address, licence) is published beside the heads. "
          "Photos under any licence with ND or SA terms are left out of fitting. In code and in these files the rule is called `nc`; `by` (the public domain and CC BY only) is measured for comparison. `tools/eval/licences.py` holds both, and `tools/eval/study2.py --licence nc` applies the rule to the species rows (training photos), to the kind rows (training photos and the fitting part of the extra set) and, for the stand-in, to the `val` photos it fits on. "
          "The tuning photos choose settings only and are not cut by the rule. Everything else is run 25's procedure: Study 2 fits and chooses on `val`, `tools/eval/export_heads.py` writes the slot, `tools/eval/shipped.py` scores it through `tools/fusion/fuse.py` on the test photos.", ""]
    for k_, v_ in sorted(S2L.items()):
        for m_, r_ in v_["models"].items():
            fo = r_.get("fitted_on", {})
            if fo:
                parts = "; ".join("%s: %s" % (set_, ", ".join("%s %d" % (l_, c_) for l_, c_ in sorted(d_.items(), key=lambda kv: -kv[1]))) for set_, d_ in fo["by_set_and_licence"].items())
                T += ["- `%s`, %s: rows fitted on %d photos (%s). Species head `%s`; kinds head %s." % (k_, m_, fo["photos"], parts, r_["chosen_species_head"]["name"],
                                                                                                  ("`%s`" % r_["kind_decision"]["chosen"]["head"]) if r_.get("kind_decision") else "the kind phrases")]
    T += [""]
    rows = []
    for label, n_ in LIC:
        if n_ not in SH:
            continue
        nn = SH[n_]["numbers"]
        k = nn.get("kind", {})
        tw, tx = k.get("test_wildlife", {}), k.get("test_extra")
        by = {g["kind"]: g for g in k.get("table_extra", [])}
        rows.append([label, "`%s`" % n_, pci(nn["kind_right"]), pci(tx["kind_right"]) if tx else "–", pci(tw.get("asserted")), pci(tw.get("asserted_right")), pci(nn["species_top1"]),
                     "%s at %s" % (pc(nn["named"][0]), nn["name_at"] if nn["name_at"] is not None else "never"), pci(nn["named_right"]),
                     pc(by["person"]["named"]) if "person" in by else "–", pc(by["none"]["named"]) if "none" in by else "–"])
    T += ["TinyCLIP 39M/16 on the test photos (4197 wildlife photos, and 1240 photos of the extra set: 400 of people, 500 of rooms, 77 cats, 63 dogs, 200 grazing animals). The rows for run 25 and for `nc` and `by` set name_at at the nine-in-ten level, as run 25 did. Intervals are 95% bootstrap intervals over photos. "
          "Run 25 (commit c0cd718) and the committed file of pocket v2 (made at 03:23) were scored with the `tools/fusion/fuse.py` from before build 8, which named a species even when the kind was under `kind_at`; build 8's fuse.py and page name one only when the kind is asserted. "
          "The rows marked build 8 are the same slots scored again by `tools/eval/shipped.py` with the present fuse.py: their thresholds and their kind of eye, photo for photo, are the same, and only the naming columns move.", "",
          table(["Heads fitted on", "Slot", "Kind right, wildlife", "Kind right, extra set", "Kind asserted, wildlife", "Right when asserted", "Top species right", "Species named (share, name_at)", "Named species right", "Named on people", "Named on rooms"], rows,
                ["---", "---"] + ["---:"] * 9), ""]
    DV3 = load("decision-pocket-v3.json")
    if DV3:
        t_ = DV3["tests"]
        T += ["**Pocket v3, by the rule set beforehand** (`tools/eval/decide_v3.py`). %s" % DV3["rule"], "",
              "- (i) Kind of eye on the wildlife test photos: %s for the candidate against %s for pocket v2, a paired difference of %s points (%s to %s) over %d photos. %s" % (
                  pci(t_["i_wildlife_kind_paired_difference"]["candidate"]), pci(t_["i_wildlife_kind_paired_difference"]["pocket_v2"]), "%+.1f" % (100 * t_["i_wildlife_kind_paired_difference"]["difference"][0]),
                  "%+.1f" % (100 * t_["i_wildlife_kind_paired_difference"]["difference"][1]), "%+.1f" % (100 * t_["i_wildlife_kind_paired_difference"]["difference"][2]), t_["i_wildlife_kind_paired_difference"]["photos"],
                  "The interval lies wholly below zero, so this test fails." if t_["i_wildlife_kind_paired_difference"]["fails"] else "The interval does not lie wholly below zero, so this test passes."),
              "- (ii) Kind of eye on the extra set's test photos: %s against a bar of 96.5%%. %s" % (pci(t_["ii_extra_kind_right"]["candidate"]), "This test fails." if t_["ii_extra_kind_right"]["fails"] else "This test passes."),
              "- (iii) A species named on %d of the %d test photos of people and rooms (%s) against a bar of 1%%. %s" % (t_["iii_named_on_people_and_rooms"]["named"], t_["iii_named_on_people_and_rooms"]["photos"], pc(t_["iii_named_on_people_and_rooms"]["share"]),
                                                                                                                         "This test fails." if t_["iii_named_on_people_and_rooms"]["fails"] else "This test passes."),
              "", DV3["why"], ""]
        if DV3.get("beside"):
            nm = {"kind_right": "kind of eye right", "asserted_right": "kind asserted and right", "asserted_wrong": "kind asserted and wrong", "named": "a species name shown", "named_right": "a right species name shown"}
            T += ["Beside the rule, deciding nothing: the candidate against pocket v2 on the same photos (paired differences in points, with 95% bootstrap intervals).", "",
                  table(["Photos", "Measure", "Candidate", "Pocket v2", "Paired difference (points)"],
                        [["wildlife test" if b_["photos"] == "wildlife" else "extra test", nm.get(b_["measure"], b_["measure"]), pc(b_["candidate"]), pc(b_["pocket_v2"]),
                          "%+.1f (%+.1f to %+.1f)" % tuple(100 * x_ for x_ in b_["difference"])] for b_ in DV3["beside"]], ["---", "---", "---:", "---:", "---:"]), ""]
    rp = os.path.join(D, "reproduction-licence.txt")
    if os.path.exists(rp):
        lines_ = open(rp, encoding="utf-8").read().splitlines()
        tot_ = next((l_.split(":")[-1].strip() for l_ in lines_ if l_.startswith("numbers that differ")), "?")
        files_ = [l_.split()[0] for l_ in lines_[1:] if ".json" in l_[:80] and "numbers compared" in l_ and not __import__("re").search(r"compared, 0 differ", l_)]
        T += ["**Rerun on a clean machine.** %s In all, %s numbers differ by more than 0.0005, all of them in these files: %s. The comparison is kept in [`docs/eval/reproduction-licence.txt`](eval/reproduction-licence.txt)." % (lines_[0], tot_, ", ".join("`%s`" % f_ for f_ in files_)), ""]
        RD, RS = load("reproduction-licence-decision.json"), load("reproduction-licence-shipped.json")
        if RD and RS:
            rn, rk = RS["numbers"], RS["numbers"]["kind"]
            rt = RD["tests"]
            same = sorted(set(l_.split()[1] for l_ in open(os.path.join(D, "reproduction-licence-sha256.txt"), encoding="utf-8").read().splitlines()) & set(l_.split()[1] for l_ in open(os.path.join(D, "pocket-v3-sha256.txt"), encoding="utf-8").read().splitlines() if l_ in open(os.path.join(D, "reproduction-licence-sha256.txt"), encoding="utf-8").read().splitlines()))
            T += ["On the build machine the kind rows came out different and Study 2 chose another kinds head (%s; rule `%s`, t_kind %g, w_kind %g), so `tools/eval/shipped.py` set kind_at %s, name_at %s and offer_at %s there. "
                  "That slot gets the kind right for %s of the wildlife test photos and %s of the extra set's, asserts a kind for %s of the wildlife photos and is right for %s of those, names a species for %s and is right for %s of those, and names one on %d of the %d test photos of people and rooms. "
                  "It passes the same three tests (paired difference against pocket v2 on wildlife %+.1f points, %+.1f to %+.1f). The files that are byte for byte the same on both machines: %s. "
                  "The sandbox's scikit-learn warned that its optimizer stopped at the 300-iteration limit while fitting kind rows; the kind rows, and every setting chosen with them, should be taken as one draw among close ones. The slot published as pocket v3 is the sandbox's." % (
                      RS["manifest"]["evaluation"].get("kind_head", "?"), RS["manifest"]["fusion"]["rule"], RS["manifest"]["fusion"]["t_kind"], RS["manifest"]["fusion"]["w_kind"], rn["kind_at"], rn["name_at"], rn["offer_at"],
                      pci(rn["kind_right"]), pci(rk["test_extra"]["kind_right"]), pci(rk["test_wildlife"]["asserted"]), pci(rk["test_wildlife"]["asserted_right"]), pci(rn["named"]), pci(rn["named_right"]),
                      rt["iii_named_on_people_and_rooms"]["named"], rt["iii_named_on_people_and_rooms"]["photos"],
                      100 * rt["i_wildlife_kind_paired_difference"]["difference"][0], 100 * rt["i_wildlife_kind_paired_difference"]["difference"][1], 100 * rt["i_wildlife_kind_paired_difference"]["difference"][2],
                      ", ".join("`%s`" % x_ for x_ in same) or "none"), ""]
    PL = load("pets-livestock.json")
    if PL:
        T += ["**Names on pets and livestock** (`tools/eval/pets.py`). %s" % PL["text"], "",
              table(["Category", "Test photos", "A species named", "The domestic species", "Another species", "What it names when wrong"],
                    [[r_["category"], r_["photos"], r_["named"], r_["domestic"], r_["other"], r_["wrong_names"] or "–"] for r_ in PL["rows"]], ["---", "---:", "---:", "---:", "---:", "---"]), ""]

T += ["## The first look, checked", "",
      "A first look at these models, made earlier in the night with a quick script, gave the numbers in the column `First look`. The next column is this study's number for the same model and label set.", ""]
rows = []
lab = {"plain_top1": "top-1", "plain_top5": "top-5", "tuned_top1": "top-1 with prior", "tuned_top5": "top-5 with prior", "kind_from_top": "kind from top species", "kind_phrases": "kind from phrases"}
for m, ls, claims in FIRST_LOOK:
    r = S1["models"].get(m)
    if not r:
        continue
    v = r["labelsets"][ls]
    got = {"plain_top1": v["plain"]["top1"], "plain_top5": v["plain"]["top5"], "tuned_top1": v["tuned"]["top1"], "tuned_top5": v["tuned"]["top5"], "kind_from_top": v["plain"]["kind_from_top"], "kind_phrases": r["kind_phrases"]["accuracy"]}
    for k, c in claims.items():
        g = got[k]
        rows.append([m, lab[k], pc(c), pci(g), "inside the interval" if g[1] - 0.0005 <= c <= g[2] + 0.0005 else "outside the interval"])
T += [table(["Model", "Measure", "First look", "This study", "First look against this study's interval"], rows, ["---", "---", "---:", "---:", "---"]), "",
      "%d of the %d first-look numbers fall inside this study's interval. The first look chose its settings on `val` from a smaller grid and without smoothing choices, so differences of a point with the prior are expected." % (sum(r_[4].startswith("inside") for r_ in rows), len(rows)), ""]

if os.path.exists(os.path.join(D, "others.md")):
    ours = pci(b2["labelsets"]["species_sci"]["tuned"]["top1"]) if b2 else "–"
    T += ["## What others publish, and why none of it is a head-to-head comparison", "",
          "The sources, with quotes, addresses and the day each page was read, are in [`docs/eval/others.md`](eval/others.md). That file was written by hand from the pages it cites. Several of its quotes came through a page-reading tool and are marked there as unchecked against the raw page. In short:", "",
          "- **iNaturalist tests its own model in a way close to ours and states few figures in words.** For each release it draws \"1,000 random Research Grade observations in each group not seen during training time\" and compares the model's suggestion with the community's species. The newest release found is v2.34 (September 2026, 123,618 taxa); its accuracy appears only in a chart image, which was not read. The latest figure stated in words is \"Overall the average accuracy of 2.20 is 88.7%\" (February 2025). The post does not say whether that figure uses location, whether it counts the first suggestion only, or how the average over groups is taken.",
          "- **With and without location.** The only such pair of figures found is from 2023: the first suggestion was right for 75% from the photo alone, 83% with the older location grid and 87% with the Geomodel. The post does not describe its test photos. iNaturalist's open code multiplies the vision score by a location score that is floored at 0.005, and does not use the month in what was read. Our prior uses the month's records within one county's list.",
          "- **Independent tests on photos taken for the purpose give lower and scattered figures.** Six plant apps on 38 species in Ireland: species right at the first attempt for 88% of flower photos and 80% of leaf photos (Pl@ntNet) down to 4% and 7% (the iNaturalist app). Five plant apps on 857 professionally identified images: 69% right with the first suggestion. Tree leaves in New Jersey: iNaturalist right to species for 70%.",
          "- **Research-grade labels are themselves wrong a few times in a hundred.** iNaturalist's two experiments in 2024 put them at 95% and 97% correct. A difference of a point or two between two models on such labels should be read with that in mind.",
          "- **BioCLIP 2's own card** gives a zero-shot top-1 of 55.6 averaged over ten benchmarks, with other photos, another list of labels for each benchmark, and no place or season.",
          "- **Nothing was found** on the accuracy of Seek, on Merlin's photo identifier beyond press figures from 2015 and 2017, or from the makers of Pl@ntNet and Google Lens.", "",
          "**Why none of this can be set beside our numbers.** Our figure of %s is for one county, a list of %d species, the month known, and an average over photos. iNaturalist's 88.7%% covers more than 100,000 taxa over the whole world and is an average whose construction is not stated. The photos differ, the lists differ and the counting differs. "
          "The two tests also share a weakness: research-grade photos are the ones people already agreed on, often after seeing iNaturalist's own suggestion, and nobody we found has measured how much easier that makes them. We could not run iNaturalist's model on our test photos, since its vision endpoint is unpublished and needs a token. "
          "The numbers on this page describe this recognizer on this test. They are no ranking against anyone." % (ours, P["species_in_list"]["1"]), ""]

if CH:
    fails = [c for c in CH["checks"] if c["verdict"] == "FAIL"]
    notes = [c for c in CH["checks"] if c["verdict"] == "note"]
    waits = [c for c in CH["checks"] if c["verdict"] == "waiting"]
    T += ["## Checks for leakage and for mistakes", "",
          "`tools/eval/checks.py` ran %d checks: %d passed, %d failed, %d record a fact to know, and %d could not run because a file was not published. The full table is in [`docs/eval/checks.md`](eval/checks.md)." % (
              len(CH["checks"]), sum(c["verdict"] == "pass" for c in CH["checks"]), len(fails), len(notes), len(waits)), ""]
    T += ["- **%s.** %s" % (c["check"][0].upper() + c["check"][1:], c["detail"]) for c in fails + notes + waits] + [""]
    T += ["What the checks cover: the dates of the photos against the species list's cutoff and against the snapshot behind BioCLIP 2's training data; that no id, observation or photo address repeats; that the split follows from the record id alone; that every vector file has the manifest's 6,000 ids in order; that label rows follow the species list; that no test photo has a copy on `val`; once the training manifest exists, that it shares no record, observation or photo number with the evaluation set and that no training photo is dated after 2024 (a manifest built from iNaturalist's open-data files carries no GBIF record id, so there the dates and the photo numbers do the work); and for the extra set, that COCO's training and validation photos stay on their own sides and that the vectors line up with the manifest. "
          "The image vectors are made from the photo file alone: `tools/lab/lab.py` (`embed_rows`) reads only the row id to find the file.", ""]

T += ["## What this does not show", "",
      "- **These photos are easier than what a phone meets.** Research-grade means that people on iNaturalist, often helped by iNaturalist's own model, already agreed on the species. Photos nobody could identify are absent. A photo taken in passing, at a distance, or of a species that needs a microscope will do worse than these numbers.",
      "- **The large models were trained on photos of this kind.** BioCLIP 2's training data was built from a GBIF snapshot of 2024-05-01 that includes iNaturalist's research-grade photos. No test photo can be in it, since all are dated 2025 or later, yet the test photos come from the same platform, the same county and in part the same observers as its training photos. The result describes that setting.",
      "- **One region.** Every number is for Alachua County and for a list of its own species. A longer list, or a place with fewer records, will give lower numbers.",
      "- **The labels follow GBIF's names.** Where GBIF and iNaturalist split or name a species differently, a photo is counted against GBIF's species.",
      "- **Nothing here compares with iNaturalist's own model.** We cannot run it, and its published accuracy figures are measured on other photos with other rules. No sentence in the app may say or suggest that this recognizer matches it.",
      ("- **People, pets, livestock and rooms are measured on COCO photos only.** They are well-lit photos from a general data set, with the subject large in the frame for people. A phone held at a blank wall, a hand, a toy animal, a painting of a bird or a screen showing a heron is in neither set, and neither is a person standing in a garden, where two answers are defensible."
       if any((v["numbers"].get("kind") or {}).get("test_extra") for v in SH.values()) else
       "- **People, pets and photos with nothing alive in them are unmeasured so far.** The extra set of COCO photos exists and the scripts tune and report with it, but no model's vectors of it were published when this report was written. How often a person is called a person is unmeasured here."),
      "- **Top-5 is measured against the whole list.** The page offers three species of the winning kind; that rule is measured in the section on what the page would show.", ""]

TRIAL = ""
tp = os.path.join(D, "reproduction-trial.txt")
if os.path.exists(tp):
    tl = [l for l in open(tp, encoding="utf-8").read().splitlines() if "numbers compared" in l]
    if tl:
        w = tl[0].split()
        TRIAL = (" An earlier run of Study 1 on another build machine differed from these files in %s of %s numbers, each by a single photo "
                 "([`docs/eval/reproduction-trial.txt`](eval/reproduction-trial.txt)). Two scores that are almost equal can change places when another processor does the arithmetic." % (w[4], w[1]))
rp = os.path.join(D, "reproduction.txt")
if os.path.exists(rp):
    lines = open(rp, encoding="utf-8").read().strip().splitlines()
    files = [l for l in lines if "numbers compared" in l]
    n_num = sum(int(l.split()[1]) for l in files)
    last = next((l for l in lines if l.startswith("numbers that differ")), "")
    head = next((l for l in lines if l.startswith("#")), "")
    T += ["## Rerun on a clean machine", "",
          "The whole evaluation was run again on a GitHub build machine from the published branches alone, and its numbers were compared by `tools/eval/compare.py` with the files as they were committed at that time (%s). "
          "%d numbers in %d files were compared; %s. The comparison is kept in [`docs/eval/reproduction.txt`](eval/reproduction.txt).%s" % (
              head.lstrip("# ").rstrip(".") or "see the file", n_num, len(files), ("%s of them differ by more than 0.0005" % last.rsplit(":", 1)[1].strip()) if last else "see the file", TRIAL), ""]
    r4 = os.path.join(D, "reproduction-r4.txt")
    if os.path.exists(r4):
        l4 = open(r4, encoding="utf-8").read().strip().splitlines()
        cnt = {}
        for l in l4:
            w = l.split()
            if len(w) > 5 and w[2:4] == ["numbers", "compared,"]:
                cnt[w[0]] = (int(w[1]), int(w[4]))
        sen = [v for k_, v in cnt.items() if k_.startswith(("shipped-sentences-", "study2-sentences", "decision-pocket.json", "checks", "variant-"))]
        val = [v for k_, v in cnt.items() if k_.startswith(("shipped-val-", "study2-val"))]
        a13, b13 = SH.get("val-tinyclip-39m-16"), None
        T += ["A second rerun covers the files written since the kind decision was changed to include the extra set (%s). In the sentence slots, their study, the checks, the pocket decision and the int8 comparisons, %d of %d numbers differ by more than 0.0005%s. "
              "In the stand-in files %d of %d numbers differ: their kind rows are fitted by an iterative optimizer, which stopped at slightly different rows on the other machine. %s "
              "A slot with fitted kind rows is therefore the same in substance on another machine and differs in late digits. The comparison is kept in [`docs/eval/reproduction-r4.txt`](eval/reproduction-r4.txt)." % (
                  next((l for l in l4 if l.startswith("#")), "").lstrip("# ").rstrip("."), sum(v[1] for v in sen), sum(v[0] for v in sen),
                  (" (Study 1: %d of %d)" % (cnt["study1.json"][1], cnt["study1.json"][0])) if "study1.json" in cnt else "", sum(v[1] for v in val), sum(v[0] for v in val),
                  " ".join(l.lstrip("# ") for l in l4 if l.startswith("# The stand-in slot"))), ""]
    else:
        T += ["That rerun is older than the present Study 2 and as-shipped files, which were written after the kind decision was changed to include the extra set and to set `kind_at`. Those files have not been confirmed on a clean machine. Every push to a `run/eval/` branch reruns them and returns `compare.txt` under `runs/eval/` on the `ci` branch.", ""]

T += ["## How to rerun", "", "One command does everything (fetch, checks, Study 1, Study 2, export, as-shipped scoring, this report):", "", "```",
      "bash tools/eval/run.sh ROOT sentences          # slots made from sentence rows",
      "bash tools/eval/run.sh ROOT val                # the stand-in for trained heads",
      "bash tools/eval/run.sh ROOT alachua-pre2025    # trained heads for real, once the training vectors are published", "```", "",
      "The steps one at a time:", "", "```",
      "python3 -I tools/eval/fetch.py ROOT                 # the published data and vectors, into ROOT/data and ROOT/lab",
      "python3 -I tools/eval/checks.py ROOT                # docs/eval/checks.json",
      "python3 -I tools/eval/study1.py ROOT                # docs/eval/study1.json, about four minutes on two cores",
      "python3 -I tools/eval/study2.py ROOT --train TRAIN --save ROOT/heads/TRAIN      # docs/eval/study2-TRAIN.json and the chosen heads",
      "python3 -I tools/eval/export_heads.py ROOT --head ROOT/heads/TRAIN/MODEL.npz --out ROOT/slots/TRAIN/MODEL   # a slot in the layout of models/<slot>/",
      "python3 -I tools/eval/shipped.py ROOT ROOT/slots/TRAIN/MODEL --name TRAIN-MODEL   # thresholds and as-shipped numbers through tools/fusion/fuse.py",
      "python3 -I tools/eval/shipped.py ROOT models/pocket --name live-pocket --no-write   # the slot that is live, scored as it stands; its manifest is left alone",
      "python3 -I tools/eval/decide.py                     # docs/eval/decision-pocket.json: which pocket model ships, by the rule written at the top of the script",
      "python3 -I tools/eval/variant.py ROOT SLOT --vectors FILE.f16.npy --ids FILE.ids.json --name LABEL --name-at 0.78 --offer-at 0.66   # another set of vectors of the same test photos, beside the original's",
      "python3 -I tools/eval/naturalist.py SLOT --shipped docs/eval/shipped-NAME.json --out DIR --variant docs/eval/variant-LABEL.json   # head files for models/naturalist",
      "python3 -I tools/eval/report.py                     # this file and the tables under docs/eval/",
      "python3 -I tools/eval/compare.py DIR_A DIR_B        # do two runs give the same numbers?", "```", "",
      "Heads under the licence rule and pocket v3, one step at a time:", "", "```",
      "python3 -I tools/eval/study2.py ROOT --train alachua-pre2025 --models tinyclip-39m-16 --licence nc --save ROOT/heads/alachua-pre2025-nc   # also --licence by",
      "python3 -I tools/eval/export_heads.py ROOT --head ROOT/heads/alachua-pre2025-nc/tinyclip-39m-16.npz --out ROOT/slots/alachua-pre2025-nc/tinyclip-39m-16   # with fitted_on.csv",
      "python3 -I tools/eval/shipped.py ROOT ROOT/slots/alachua-pre2025-nc/tinyclip-39m-16 --name alachua-pre2025-nc-tinyclip-39m-16 --name-bar 0.92",
      "python3 -I tools/eval/decide_v3.py --candidate alachua-pre2025-nc-tinyclip-39m-16      # docs/eval/decision-pocket-v3.json",
      "python3 -I tools/eval/pocket_v3.py SLOT --shipped docs/eval/shipped-alachua-pre2025-nc-tinyclip-39m-16.json --decision docs/eval/decision-pocket-v3.json --ready DIR --publish DIR2",
      "python3 -I tools/eval/shipped.py ROOT DIR --name pocket-v3 --name-bar 0.92 --no-write   # the last check of the assembled files",
      "python3 -I tools/eval/pets.py ROOT DIR --name pocket-v3                               # docs/eval/pets-livestock.json", "```", "",
      "Pushing a commit to a branch named `run/eval/<label>` reruns all of it on a clean build machine (`.github/workflows/eval.yml`), returns the files and a comparison with the committed numbers under `runs/eval/` on the `ci` branch, and publishes the exported slots to `pub/heads-<train>-<model>`. "
      "A branch named `run/eval/armed<label>` waits for the training vectors and then measures the trained heads only; `run/eval/coco<label>` waits for the pocket models' vectors of the extra set and then reruns everything; `run/eval/licence<label>` reruns the heads under the licence rule, the pocket v3 decision, the last check and the pets check, and publishes nothing.", "",
      "Inputs of this run: " + "; ".join("`%s` at `%s`" % (k, v["commit"][:12]) for k, v in sorted(S1["inputs"]["branches"].items())) + "."]
with open(a.out, "w", encoding="utf-8") as f:
    f.write("\n".join(T).rstrip("\n") + "\n")
print("wrote", a.out)
