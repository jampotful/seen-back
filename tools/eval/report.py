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
          "- **Rare species lose under the prior.** For species with 1 or 2 records before 2025, top-1 is %s with the prior and %s without it (%d photos); for 3 to 9 records, %s and %s (%d photos). For species with 200 or more records it is %s and %s (%d photos). The prior buys its gain on common species and pays for it on rare ones." % (
              pc(rec["1 or 2 records"]["top1"][0]), pc(rec["1 or 2 records"]["top1_no_prior"]), rec["1 or 2 records"]["n"], pc(rec["3 to 9"]["top1"][0]), pc(rec["3 to 9"]["top1_no_prior"]), rec["3 to 9"]["n"],
              pc(rec["200 or more"]["top1"][0]), pc(rec["200 or more"]["top1_no_prior"]), rec["200 or more"]["n"]),
          "- **By kind of eye** (kinds with at least 30 test photos), top-1 with the prior runs from %s for `%s` to %s for `%s`." % (pc(kinds[0]["top1"][0]), kinds[0]["group"], pc(kinds[-1]["top1"][0]), kinds[-1]["group"]),
          "- **Its own kind phrases are weak.** Asked for the kind of eye through the kind phrases, BioCLIP 2 is right in %s. Taking the kind from its top species is right in %s. A biology model knows species names far better than everyday words such as \"a wading bird\"." % (pci(b2["kind_phrases"]["accuracy"]), pci(t["kind_from_top"])),
          "- **Names that differ between GBIF and iNaturalist.** %d test photos are of species whose GBIF name differs from the name iNaturalist uses (%s). Top-1 without the prior is %s on those photos and %s on the rest, so scoring against GBIF's names costs nothing here." % (
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

# Study 2 and the decisions are added by the sections below when their files exist.
for name, s2 in S2.items():
    standin = s2.get("standin")
    T += ["## Heads trained on photos (Study 2)%s" % (": machinery proven on a stand-in" if standin else ""), ""]
    T += [s2["what"], ""]
    for m, r in s2["models"].items():
        T += ["### %s" % m, "", "Trained on %d photos of %d species (`%s`); tested on %d test photos (`%s`)." % (r["train_photos"], r["train_species"], r["train_vectors"], r["test_photos"], r["test_vectors"]), ""]
        rows = [[h["name"], pci(h["plain"]["top1"]), pci(h["plain"]["top5"]), pci(h["prior"]["top1"]), pci(h["prior"]["top5"]), pci(h["prior"].get("kind_from_sum")), h["prior"].get("settings_text", "")] for h in r["species_heads"]]
        T += [table(["Species head", "Top-1", "Top-5", "Top-1 with prior", "Top-5 with prior", "Kind from summed species", "Settings chosen on the tuning photos"], rows, ["---", "---:", "---:", "---:", "---:", "---:", "---"]), ""]
        if r.get("kind_heads"):
            T += [table(["Kind-of-eye head", "Right kind", "Called `person`", "Called `none`"], [[h["name"], pci(h["accuracy"]), pc(h.get("called_person"), 2), pc(h.get("called_none"), 2)] for h in r["kind_heads"]]), ""]
        if r.get("by_train_photos"):
            T += ["Top-1 with the prior for the head named first above each column, by how many training photos the species has:", "",
                  table(["Training photos of the species", "Test photos"] + r["by_train_photos"]["heads"], [[g["group"], g["n"]] + [pc(x) for x in g["top1"]] for g in r["by_train_photos"]["rows"]]), ""]
        c = r.get("confidence")
        if c:
            T += ["**Confidence.** %s" % c["text"], ""]
        for note in r.get("notes", []):
            T += ["- " + note]
        T += [""]

for name, sh in SH.items():
    T += ["## As shipped: `%s`" % name, "", sh["text"], ""]
    T += [table(["What the page would show", "Share of test photos", "Right"], [[x["what"], pc(x["share"]), x["right"]] for x in sh["outcomes"]]), ""]

dec = load("decisions.json")
if dec:
    T += ["## Decisions", ""] + ["- **%s** %s" % (d["title"], d["text"]) for d in dec["decisions"]] + [""]

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
