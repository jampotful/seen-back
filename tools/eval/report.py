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
      "- **Intervals.** Each share is followed by a 95%% percentile interval from %d bootstrap resamples over photos (seed %d). The intervals describe the luck of which photos were drawn. They say nothing about photos of another kind." % (meth["resamples"], meth["seed"]), ""]

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
    return n.split(" (")[0] if n.startswith(("kind phrases", "trained on")) else n


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
            if short_kind(h["name"]).split(" (rule")[0] not in kn:
                kn.append(short_kind(h["name"]).split(" (rule")[0])
    def kget(m, k):
        return next((h for h in s2["models"][m]["kind_heads"] if short_kind(h["name"]).split(" (rule")[0] == k and "`product`" not in h["name"]), None)
    rows = []
    for k in kn:
        label = k.split(" and the head")[0].split(" of the head")[0]
        if label not in [r_[0] for r_ in rows]:
            rows.append([label] + [pci(kget(m, k)["accuracy"]) if kget(m, k) else "" for m in ms])
        else:
            row = next(r_ for r_ in rows if r_[0] == label)
            for i, m in enumerate(ms):
                if kget(m, k):
                    row[i + 1] = pci(kget(m, k)["accuracy"])
    T += ["Kind of eye right on the test photos:", "", table(["Kind of eye from"] + ms, rows), ""]
    for m in ms:
        r = s2["models"][m]
        if r.get("confidence"):
            T += ["- **%s.** %s" % (m, r["confidence"]["text"])]
    for note in sorted({n_ for m in ms for n_ in s2["models"][m].get("notes", [])}):
        T += ["- " + note]
    T += ["", "Every head, its settings, the reliability tables and the breakdown by fitting photos are in [`docs/eval/study2-%s.md`](eval/study2-%s.md)." % (name, name), ""]

if SH:
    T += ["## What the page would show", "",
          "Each slot below was written by `tools/eval/export_heads.py` in the layout of `models/<slot>/` and then scored by `tools/eval/shipped.py`, which reads the slot's own files as the page does and sends every photo through `tools/fusion/fuse.py`. "
          "The two thresholds were set on the tuning photos so that a named species, and the three offered species, were right at least nine times in ten there. Slots whose name begins with `val-` hold stand-in heads.", ""]
    rows = []
    for name in sorted(SH, key=lambda k: (k.startswith("val-"), k)):
        n = SH[name]["numbers"]
        rows.append(["`%s`" % name, pci(n["kind_right"]), pci(n["species_top1"]), "%s at %s" % (pc(n["named"][0]), n["name_at"] if n["name_at"] is not None else "never"), pci(n["named_right"]),
                     "%s at %s" % (pc(n["offered"][0]), n["offer_at"] if n["offer_at"] is not None else "never"), pci(n["offered_holds_species"]), pc(n["kind_only"][0]), pci(n["kind_only_kind_right"])])
    T += [table(["Slot", "Kind right", "Top species right", "Species named (share, threshold)", "Named species right", "Three offered (share, threshold)", "Offer holds the species", "Kind only", "Kind right when kind only"], rows), ""]
    L = ["# Exported slots, scored as the page would", "", GEN % "docs/eval/shipped-*.json", ""]
    for name in sorted(SH, key=lambda k: (k.startswith("val-"), k)):
        sh = SH[name]
        L += ["## `%s`" % name, "", sh["text"], "", table(["What the page would show", "Share of test photos", "Right"], [[x["what"], pc(x["share"]), x["right"]] for x in sh["outcomes"]], ["---", "---:", "---"]), ""]
        for x in sh.get("extra", []):
            L += [x["text"], "", table(["Photos of", "Photos", "Kind said right", "Said `person`", "Said `none`", "A species named"], [[g["kind"], g["n"], pci(g["right"]), pc(g["person"]), pc(g["none"]), pc(g["named"])] for g in x["rows"]]), ""]
    write("shipped.md", "\n".join(L))
    for name in sorted(SH, key=lambda k: (k.startswith("val-"), k)):
        for x in SH[name].get("extra", []):
            T += ["**`%s` on photos of people, pets, livestock and rooms.** %s" % (name, x["text"]), "", table(["Photos of", "Photos", "Kind said right", "Said `person`", "Said `none`", "A species named"], [[g["kind"], g["n"], pci(g["right"]), pc(g["person"]), pc(g["none"]), pc(g["named"])] for g in x["rows"]]), ""]
    T += ["The text for each slot, with what it needs from the page, is in [`docs/eval/shipped.md`](eval/shipped.md).", ""]

# ---- decisions: sentences around numbers that the studies wrote
real = next((v for k, v in S2.items() if not v.get("standin")), None)
m39, m8 = S1["models"].get("tinyclip-39m-16"), S1["models"].get("tinyclip-8m-16")
WV = "alachua-2025.wasm-int8-per-channel"
T += ["## Decisions", ""]
if m39 and m8 and WV in m39["variants"] and WV in m8["variants"]:
    def wasm(r):
        v = r["variants"][WV]
        return v["kind_phrases"]["accuracy"], v["labelsets"][r["best_labelset_on_val"]]["tuned_top1"]
    k39, s39 = wasm(m39)
    k8, s8 = wasm(m8)
    lat = lambda r: ("about %d ms a photo" % round(r["card"]["wasm_latency_ms"])) if r["card"].get("wasm_latency_ms") else "latency in its card"
    txt = ("On the vectors a phone computes, and scored against sentences, TinyCLIP 39M/16 gets the kind of eye from phrases right for %s and the species with the prior for %s; TinyCLIP 8M/16 gets %s and %s. "
           "The first is a %.1f MB download and took %s in the laboratory's one-thread WASM run; the second is %.1f MB and took %s. " % (
               pci(k39), pci(s39), pci(k8), pci(s8), m39["card"]["ship_bytes"] / 1e6, lat(m39), m8["card"]["ship_bytes"] / 1e6, lat(m8)))
    if real and "tinyclip-39m-16" in real["models"] and "tinyclip-8m-16" in real["models"]:
        def best(r):
            h = next(h for h in r["species_heads"] if h["name"] == r["chosen_species_head"]["name"])
            return h
        h39, h8 = best(real["models"]["tinyclip-39m-16"]), best(real["models"]["tinyclip-8m-16"])
        txt += ("With heads fitted on the training photos, the 39M model's best head (`%s`) names the species for %s of test photos with the prior and the 8M model's (`%s`) for %s. "
                "Recommendation: ship the model whose trained head is ahead by more than the intervals, and prefer the 8M model when they overlap, because it is a quarter of the download and a third of the time." % (
                    h39["name"], pci(h39["prior"]["top1"]), h8["name"], pci(h8["prior"]["top1"])))
    else:
        txt += ("Heads fitted on the real training photos have not been measured, because the training vectors were not published when this report was written, and they decide this choice: a trained head may close the gap between the two models or widen it. "
                "Until then the recommendation is TinyCLIP 39M/16 with its sentence rows and the prior, to show a kind of eye and to offer species only above the thresholds measured below, and TinyCLIP 8M/16 if the download has to stay under 10 MB.")
    T += ["- **The pocket model.** " + txt]
if b2:
    v = b2["labelsets"]["species_sci"]
    t = v["tuned"]
    st = t["settings"]
    b25 = S1["models"].get("bioclip25-h14")
    T += ["- **The server.** BioCLIP 2 (ViT-L/14) with rows made from scientific names, all %d species of the list, and the prior (alpha %g at temperature %g, smoothing lam %g and c %g): top-1 %s, top-5 %s, and the kind of eye from summed species probabilities right for %s. "
          "The kind of eye should come from the species list and the kind phrases should count for little, because this model's kind phrases alone are right for %s.%s" % (
              st["species_in_list"], st["alpha_prior"], st["t_species"], st["lam"], st["c"], pci(t["top1"]), pci(t["top5"]), pci(t["kind_from_sum"]), pci(b2["kind_phrases"]["accuracy"]),
              (" BioCLIP 2.5 measures %s with the prior%s. It runs at about a third of the speed by the coordinator's notes, and its training date is undocumented, so no number for it can be defended in public. BioCLIP 2 is the one to run." % (
                  pci(b25["labelsets"]["species_sci"]["tuned"]["top1"]), (", a paired difference of %s points from BioCLIP 2 on the same photos" % pts(b25["against_bioclip2_l14"]["top1_with_prior_difference"])) if b25.get("against_bioclip2_l14") else "")) if b25 else "")]
    T += ["- **What the app may say about the server.** A sentence the measurements support: \"On photos from Alachua County that iNaturalist's community had already identified, taken in 2025 and 2026, this recognizer named the species for about %d photos in 100.\" It may add that such photos are easier than a photo taken in passing. It may not compare itself with iNaturalist's model." % int(100 * t["top1"][1])]
T += [""]

T += ["## Where the first look differed", "",
      "The coordinator's first look (`quick.py`) gave the numbers in the left column of each pair. The right column is this study's number for the same model and label set.", ""]
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
      "The first look chose its settings on `val` from a smaller grid and without smoothing choices, so differences of a point with the prior are expected.", ""]

if CH:
    fails = [c for c in CH["checks"] if c["verdict"] == "FAIL"]
    notes = [c for c in CH["checks"] if c["verdict"] == "note"]
    waits = [c for c in CH["checks"] if c["verdict"] == "waiting"]
    T += ["## Checks for leakage and for mistakes", "",
          "`tools/eval/checks.py` ran %d checks: %d passed, %d failed, %d are facts to know, and %d wait for a file that is not published yet. The full table is in [`docs/eval/checks.md`](eval/checks.md)." % (
              len(CH["checks"]), sum(c["verdict"] == "pass" for c in CH["checks"]), len(fails), len(notes), len(waits)), ""]
    T += ["- **%s.** %s" % (c["check"][0].upper() + c["check"][1:], c["detail"]) for c in fails + notes + waits] + [""]
    T += ["What the checks cover: the dates of the photos against the species list's cutoff and against the snapshot behind BioCLIP 2's training data; that no id, observation or photo address repeats; that the split follows from the record id alone; that every vector file has the manifest's 6,000 ids in order; that label rows follow the species list; that no test photo has a copy on `val`; and, once the training manifest exists, that it shares no record, observation or photo with the evaluation set. "
          "The image vectors are made from the photo file alone: `tools/lab/lab.py` (`embed_rows`) reads only the row id to find the file.", ""]

T += ["## What this does not show", "",
      "- **These photos are easier than what a phone meets.** Research-grade means that people on iNaturalist, often helped by iNaturalist's own model, already agreed on the species. Photos nobody could identify are absent. A photo taken in passing, at a distance, or of a species that needs a microscope will do worse than these numbers.",
      "- **The large models were trained on photos of this kind.** BioCLIP 2's training data was built from a GBIF snapshot of 2024-05-01 that includes iNaturalist's research-grade photos. No test photo can be in it, since all are dated 2025 or later, yet the test photos come from the same platform, the same county and in part the same observers as its training photos. The result describes that setting.",
      "- **One region.** Every number is for Alachua County and for a list of its own species. A longer list, or a place with fewer records, will give lower numbers.",
      "- **The labels follow GBIF's names.** Where GBIF and iNaturalist split or name a species differently, a photo is counted against GBIF's species.",
      "- **Nothing here compares with iNaturalist's own model.** We cannot run it, and its published accuracy figures are measured on other photos with other rules. No sentence in the app may say or suggest that this recognizer matches it.",
      "- **People, pets and photos with nothing alive in them are missing from the evaluation set.** How often a person is called a person is unmeasured here.",
      "- **Top-5 is measured against the whole list.** The page offers three species of the winning kind; that rule is measured only in the section on shipping, when it is present.", ""]

T += ["## How to rerun", "", "```", "python3 -I tools/eval/fetch.py ROOT            # the published data and vectors, into ROOT/data and ROOT/lab",
      "python3 -I tools/eval/checks.py ROOT           # docs/eval/checks.json", "python3 -I tools/eval/study1.py ROOT           # docs/eval/study1.json (about four minutes on two cores)",
      "python3 -I tools/eval/study2.py ROOT --train val                # trained heads with val standing in for a training set",
      "python3 -I tools/eval/study2.py ROOT --train alachua-pre2025    # trained heads for real, once the training vectors are published",
      "python3 -I tools/eval/export_heads.py ROOT --model MODEL --out DIR   # the chosen heads in the layout of models/<slot>/",
      "python3 -I tools/eval/shipped.py ROOT DIR      # the exported slot, scored through tools/fusion/fuse.py",
      "python3 -I tools/eval/report.py                # this file and the tables under docs/eval/", "```", "",
      "Inputs of this run: " + "; ".join("`%s` at `%s`" % (k, v["commit"][:12]) for k, v in sorted(S1["inputs"]["branches"].items())) + "."]
with open(a.out, "w", encoding="utf-8") as f:
    f.write("\n".join(T).rstrip("\n") + "\n")
print("wrote", a.out)
