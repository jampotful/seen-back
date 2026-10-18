#!/usr/bin/env python3
"""The species that borrow each view behind ?try= (track trydrafts, 18 October), for tools/views/rows.py.

    python3 -I tools/views/try_species.py [--views owl,duck] [--traits]

The gap table (tools/views/gaps.py, docs/views/gaps/cells.jsonl) lists species only for the fourteen offered views, and the build machine
that runs rows.py checks out one branch, so this script writes the list for the views behind ?try= to docs/views/gaps/try-species.json:
  1. the 60 species with the most research-grade records worldwide (origin/pub/naturalist-world, rows.tsv) whose world group is the view,
     or, for views that have no world group of their own (owl, duck, bigcat, fox, millipede, centipede, harvestman, woodlouse, reef), whose
     genus falls in the view's taxa (the spec's applies_to, or TAXA below), with genus, family and order from the county list
     (origin/pub/data-alachua), docs/views/gaps/taxonomy-extra.tsv and the evidence;
  2. every other species of the view with a species-level record in the evidence logs, so that rows about one group (elephants,
     cheetahs, chitons) have that group's measured species to draw on.
Each species carries its worldwide record count, which weights the row grades in rows.py exactly as for the offered views.
With --traits it also prints, for each view, the evidence traits of its species and genera with their counts.
"""
import argparse
import collections
import csv
import datetime
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("rows", os.path.join(HERE, "rows.py"))
R = importlib.util.module_from_spec(_spec)
sys.modules["rows"] = R
_spec.loader.exec_module(R)

# The views behind ?try= other than the jumping spider and the spiders, whose species rows.py reads from the county list.
TRY_VIEWS = ("bat bigcat centipede cephalopod crab duck fish flyingfox fox fungus harvestman mammal millipede owl primate reef "
             "salamander scorpion sealife shark slime snail tick whale woodlouse worm").split()
WORLD_TOP = 60
OUT = os.path.join(ROOT, "docs", "views", "gaps", "try-species.json")

# Taxa for views whose spec has no applies_to, or whose applies_to names a class that the genus tables cannot place.
# Own construction from general knowledge (the reef families and the myriapod orders); check against GBIF.
REEF_FAMILIES = ["Pomacentridae", "Labridae", "Scaridae", "Chaetodontidae", "Pomacanthidae", "Acanthuridae", "Serranidae", "Epinephelidae",
                 "Lutjanidae", "Haemulidae", "Holocentridae", "Apogonidae", "Gobiidae", "Blenniidae", "Tetraodontidae", "Balistidae",
                 "Monacanthidae", "Ostraciidae", "Diodontidae", "Mullidae", "Siganidae", "Zanclidae", "Pseudochromidae", "Syngnathidae",
                 "Muraenidae", "Scorpaenidae", "Lethrinidae", "Caesionidae", "Cirrhitidae", "Synodontidae", "Tripterygiidae", "Labrisomidae",
                 "Grammatidae", "Opistognathidae", "Plesiopidae", "Ephippidae", "Sparidae", "Kyphosidae"]
ORDER_CLASS = {o: "Chilopoda" for o in ("Scutigeromorpha", "Lithobiomorpha", "Scolopendromorpha", "Geophilomorpha", "Craterostigmomorpha")}
ORDER_CLASS.update({o: "Diplopoda" for o in (
    "Julida", "Polydesmida", "Spirobolida", "Spirostreptida", "Glomerida", "Polyxenida", "Chordeumatida", "Callipodida", "Platydesmida",
    "Polyzoniida", "Siphonophorida", "Sphaerotheriida", "Stemmiulida", "Glomeridesmida", "Siphoniulida", "Siphonocryptida")})
ORDER_CLASS.update({o: "Pauropoda" for o in ("Tetramerocerata", "Hexamerocerata")})
TAXA = {"reef": {"family": REEF_FAMILIES}}
# The world groups were made before the views for harvestmen, woodlice, millipedes and centipedes, and the genus tables do not know the order
# of every genus in them, so the English name decides as well: a species named for a narrower view leaves the broader group and joins that
# view. GENUS_PHYLUM holds genera of the worm group that the applies_to of the worm view leaves out.
BY_NAME = {"harvestman": ("harvestman",), "woodlouse": ("woodlouse", "pill-bug", "pillbug", "sowbug", "slater"),
           "millipede": ("millipede",), "centipede": ("centipede",)}
GENUS_PHYLUM = {"Litylenchus": "Nematoda"}
# Orders of genera that are common in these groups and missing from the genus tables (own construction from general knowledge; check
# against GBIF).
GENUS_ORDER = {g: "Opiliones" for g in ("Odiellus", "Paroligolophus", "Opilio", "Mitopus", "Oligolophus", "Lacinius", "Dicranopalpus", "Rilaena",
                                         "Platybunus", "Megabunus", "Nemastoma", "Trogulus", "Homalenotus", "Mitostoma", "Phalangium", "Leiobunum")}
GENUS_ORDER.update({g: "Isopoda" for g in ("Oniscus", "Philoscia", "Porcellio", "Armadillidium", "Trachelipus", "Porcellionides", "Ligia",
                                            "Cylisticus", "Armadillo", "Hemilepistus", "Venezillo", "Ligidium", "Androniscus")})
GENUS_ORDER.update({g: "Julida" for g in ("Pachyiulus", "Ommatoiulus", "Tachypodoiulus", "Cylindroiulus", "Julus", "Nemasoma")})
GENUS_ORDER.update({g: "Polydesmida" for g in ("Xystocheir", "Polydesmus", "Harpaphe", "Apheloria", "Oxidus", "Motyxia", "Pseudopolydesmus",
                                                "Boraria", "Pachydesmus", "Sigmoria", "Desmoxytes")})
GENUS_ORDER.update({"Narceus": "Spirobolida", "Trigoniulus": "Spirobolida", "Anadenobolus": "Spirobolida", "Glomeris": "Glomerida",
                    "Polyxenus": "Polyxenida", "Brachycybe": "Platydesmida", "Lithobius": "Lithobiomorpha", "Scolopendra": "Scolopendromorpha",
                    "Hemiscolopendra": "Scolopendromorpha", "Scolopocryptops": "Scolopendromorpha", "Cormocephalus": "Scolopendromorpha",
                    "Ethmostigmus": "Scolopendromorpha", "Otostigmus": "Scolopendromorpha", "Rhysida": "Scolopendromorpha",
                    "Scutigera": "Scutigeromorpha", "Thereuonema": "Scutigeromorpha", "Allothereua": "Scutigeromorpha",
                    "Geophilus": "Geophilomorpha", "Strigamia": "Geophilomorpha", "Stigmatogaster": "Geophilomorpha"})
GENUS_ORDER.update({g: "Balanomorpha" for g in ("Balanus", "Semibalanus", "Chthamalus", "Tetraclita", "Megabalanus", "Amphibalanus")})
GENUS_ORDER.update({"Pollicipes": "Scalpelliformes", "Lepas": "Lepadiformes"})
CLASS_PHYLUM = {"Chilopoda": "Arthropoda", "Diplopoda": "Arthropoda", "Pauropoda": "Arthropoda", "Arachnida": "Arthropoda", "Insecta": "Arthropoda",
                "Malacostraca": "Arthropoda", "Hexapoda": "Arthropoda", "Collembola": "Arthropoda", "Gastropoda": "Mollusca", "Bivalvia": "Mollusca",
                "Cephalopoda": "Mollusca", "Polyplacophora": "Mollusca", "Clitellata": "Annelida", "Polychaeta": "Annelida"}


def git_show(ref, path):
    return subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (ref, path)], check=True, capture_output=True).stdout.decode("utf-8")


def view_taxa(v):
    if v in TAXA:
        return TAXA[v]
    try:
        spec = json.load(open(os.path.join(ROOT, "views", v + ".json"), encoding="utf-8"))
    except OSError:
        return None
    return spec.get("applies_to")


def mismatch(taxa, family, order, cls, phylum, kingdom):
    """True when the taxonomy that is known places the species outside the view's taxa (used to clean the world groups)."""
    if not taxa:
        return False
    if family and family in taxa.get("not_family", []):
        return True
    cls = cls or ORDER_CLASS.get(order, "")
    phylum = phylum or CLASS_PHYLUM.get(cls, "")
    for rank, val in (("family", family), ("order", order), ("class", cls), ("clade", cls), ("phylum", phylum), ("kingdom", kingdom)):
        if rank in taxa and val and not any(":" in t for t in taxa[rank]):
            return val not in taxa[rank]
    return False


def member(taxa, genus, family, order, cls):
    if not taxa:
        return False
    if family and family in taxa.get("not_family", []):
        return False
    if "genus" in taxa:
        return genus in taxa["genus"]
    if "family" in taxa:
        return family in taxa["family"]
    if "order" in taxa:
        return order in taxa["order"]
    if "class" in taxa:
        return (cls or ORDER_CLASS.get(order, "")) in taxa["class"]
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--views", default=",".join(TRY_VIEWS))
    ap.add_argument("--traits", action="store_true")
    a = ap.parse_args()
    views = a.views.split(",")

    world = list(csv.DictReader(git_show("origin/pub/naturalist-world", "rows.tsv").splitlines(), delimiter="\t"))
    wrec = {}
    wgroup = {}
    for r in world:
        r["records"] = int(r["records"])
        if r["records"] > wrec.get(r["sci"], -1):
            wrec[r["sci"]], wgroup[r["sci"]] = r["records"], r["group"]
    groups = set(wgroup.values())
    county = json.loads(git_show("origin/pub/data-alachua", "regions/us-fl-alachua/species.json"))["species"]
    tax, gclass, gphylum, gkingdom = R.GAPS.Tax(), {}, {}, {}
    for s in county:
        tax.add(s["genus"], s["family"], R.GAPS.clean_order(s["order"], s["class"]))
        gclass.setdefault(s["genus"], s["class"])
        gphylum.setdefault(s["genus"], s["phylum"])
        gkingdom.setdefault(s["genus"], s["kingdom"])
    for r in csv.DictReader(open(os.path.join(ROOT, "docs", "views", "gaps", "taxonomy-extra.tsv"), encoding="utf-8"), delimiter="\t"):
        tax.add(r["genus"], r["family"], r["order"])
    recs, index, ord_ev = R.load_evidence(ROOT, tax)
    for r in recs:
        if r.get("class") and r.get("_genus"):
            gclass.setdefault(r["_genus"], r["class"])
    en_of = {r["sci"]: r["en"] for r in world}

    def taxo(sci):
        g = sci.split(" ")[0]
        return g, tax.family(g), tax.order(g) or GENUS_ORDER.get(g, ""), gclass.get(g, "")

    def named(sci):
        en = (en_of.get(sci) or "").lower()
        if "spider" in en:
            return None
        return next((k for k, words in BY_NAME.items() if any(w in en for w in words)), None)

    def off(taxa, sci):
        g, fam, order, cls = taxo(sci)
        if named(sci) and named(sci) != v:
            return True
        return mismatch(taxa, fam, order, cls, gphylum.get(g, "") or GENUS_PHYLUM.get(g, ""), gkingdom.get(g, ""))

    out = {}
    for v in views:
        taxa = view_taxa(v)
        own = v in groups

        def belongs(sci):
            if own and sci in wgroup:
                return wgroup[sci] == v and not off(taxa, sci)
            return named(sci) == v or (member(taxa, *taxo(sci)) and not (named(sci) and named(sci) != v))
        top = [r for r in world if belongs(r["sci"])] if not own else [r for r in world if r["group"] == v and not off(taxa, r["sci"])]
        top = sorted(top, key=lambda r: (-r["records"], r["sci"]))
        sel = collections.OrderedDict()
        for r in top[:WORLD_TOP]:
            sel[r["sci"]] = "world group" if own else "taxa"
        for r in recs:
            if r["_lvl"] != "species":
                continue
            sci = r["_names"][0]
            if sci in sel:
                continue
            g = r["_genus"]
            if (own and sci in wgroup and wgroup[sci] == v and not off(taxa, sci)) or (not (own and sci in wgroup) and member(
                    taxa, g, r.get("family") or tax.family(g), r.get("order") or tax.order(g) or GENUS_ORDER.get(g, ""),
                    r.get("class") or gclass.get(g, ""))):
                sel[sci] = "measured"
        lst = []
        for sci, how in sel.items():
            g, fam, order, cls = taxo(sci)
            lst.append({"sci": sci, "en": en_of.get(sci, ""), "genus": g, "family": fam, "order": order, "records": wrec.get(sci, 0), "how": how})
        lst.sort(key=lambda e: (-e["records"], e["sci"]))
        out[v] = lst
        print("%-11s %3d species (%d from the world rows, %d measured only); most recorded: %s" % (
            v, len(lst), sum(1 for e in lst if e["how"] != "measured"), sum(1 for e in lst if e["how"] == "measured"),
            ", ".join(e["en"] or e["sci"] for e in lst[:4])))
        if a.traits:
            names = {e["sci"] for e in lst}
            genera = {e["genus"] for e in lst}
            c = collections.Counter()
            for r in recs:
                if (r["_lvl"] == "species" and r["_names"][0] in names) or (r["_lvl"] == "genus" and r["_genus"] in genera):
                    c[r["_trait"]] += 1
            print("    traits:", " ".join("%s:%d" % kv for kv in c.most_common(30)))
    old = {}
    if os.path.exists(OUT):
        old = json.load(open(OUT, encoding="utf-8")).get("views", {})
    old.update(out)
    blob = {"_note": "Species that borrow each view behind ?try=, written by tools/views/try_species.py for tools/views/rows.py. "
                     "how: 'world group' (the view's group in the world rows, the 60 most recorded), 'taxa' (the view's applies_to, "
                     "or TAXA in the script, the 60 most recorded), 'measured' (a species-level evidence record and no place among those 60). "
                     "records: research-grade records worldwide.",
            "made": datetime.date.today().isoformat(), "views": {k: old[k] for k in sorted(old)}}
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("{\"_note\": %s,\n\"made\": %s,\n\"views\": {\n" % (json.dumps(blob["_note"]), json.dumps(blob["made"])))
        keys = list(blob["views"])
        for i, k in enumerate(keys):
            f.write("%s: [\n%s\n]%s\n" % (json.dumps(k), ",\n".join(json.dumps(e, ensure_ascii=False) for e in blob["views"][k]), "," if i < len(keys) - 1 else ""))
        f.write("}}\n")
    print("wrote", os.path.relpath(OUT, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
