#!/usr/bin/env python3
"""The group of creatures a taxon belongs to, from iNaturalist's taxonomy, for the world photos (docs/COVERAGE.md).

There are 33 groups of living things: the fourteen kinds of eye with views (docs/CONTRACTS.md, "The sixteen kinds of
eye", less `person` and `other`) and the nineteen groups that have no view yet (GROUPS in src/cam.a.js). `person` and
`other` are kept as they are. The rules for the fourteen are the ones tools/species/eyes.py carries out on GBIF's
backbone; the rules for the nineteen follow the sorting of docs/views/world-orders.csv as docs/COVERAGE.md merges it,
with two moves the plan makes: seaweed and other algae (Ochrophyta) go to `plant`, and springtails (Collembola,
with Diplura and Protura) to `insect`.

iNaturalist ranks some groups differently from GBIF (whales are an infraorder of Artiodactyla in iNaturalist and an
order in GBIF), so every rule is a test for a name anywhere among a taxon's ancestors, whatever its rank, except the
genus Homo and the family Formicidae, which are tested by rank. The first rule that matches wins.

As a script it reads taxa.csv.gz from the open-data snapshot and writes one line a taxon:
  taxon_id <TAB> group <TAB> unit <TAB> order
where `unit` is the taxon's species (a subspecies, variety, form or hybrid counts as the species above it; a taxon
above species is its own unit) and `order` is its order's taxon id, or its class's or phylum's when it has none.

Usage: python3 -I tools/world/groups.py --taxa taxa.csv.gz --out taxmap.tsv [--summary groups-summary.tsv]
"""
import argparse
import csv
import gzip
import sys
from collections import Counter

VIEWS = ("cat", "dog", "squirrel", "deer", "rabbit", "hawk", "wader", "bird", "alligator", "reptile", "frog", "bee",
         "insect", "plant")
NEW = ("fungus", "slime", "spider", "jumper", "fish", "shark", "snail", "sealife", "crab", "salamander", "worm",
       "scorpion", "tick", "mammal", "primate", "whale", "bat", "flyingfox", "cephalopod")
GROUPS = VIEWS + NEW                        # the 33 groups of creatures
ALL = GROUPS + ("person", "other")

DEER_FAMILIES = {"Cervidae", "Bovidae", "Equidae", "Antilocapridae", "Camelidae", "Giraffidae"}
WHALES = {"Cetacea", "Phocidae", "Otariidae", "Odobenidae", "Pinnipedia", "Sirenia"}
VULTURES = {"Cathartidae", "Cathartiformes"}
HAWK_ORDERS = {"Accipitriformes", "Falconiformes"}
WADER_FAMILIES = {"Ardeidae", "Threskiornithidae", "Ciconiidae", "Gruidae", "Aramidae", "Rallidae"}
WADER_ORDERS = {"Columbiformes", "Galliformes"}
CROCODILIANS = {"Crocodylia", "Crocodilia"}
REPTILES = {"Reptilia", "Squamata", "Testudines", "Sphenodontia", "Rhynchocephalia"}
SALAMANDERS = {"Caudata", "Urodela", "Gymnophiona"}
SHARKS = {"Chondrichthyes", "Elasmobranchii", "Holocephali"}
FISH = {"Actinopterygii", "Sarcopterygii", "Dipnoi", "Dipnomorpha", "Actinistia", "Coelacanthiformes", "Myxini",
        "Petromyzonti", "Petromyzontida", "Hyperoartia", "Cephalaspidomorphi"}
TUNICATES = {"Tunicata", "Urochordata", "Ascidiacea", "Thaliacea", "Appendicularia", "Cephalochordata", "Leptocardii"}
INSECTS = {"Insecta", "Collembola", "Diplura", "Protura", "Entognatha"}
SCORPIONS = {"Scorpiones", "Opiliones", "Pseudoscorpiones", "Solifugae", "Amblypygi", "Uropygi", "Thelyphonida",
             "Schizomida", "Ricinulei", "Palpigradi"}
CRUSTACEANS = {"Crustacea", "Merostomata", "Xiphosura", "Xiphosurida", "Pycnogonida"}
WORMS = {"Myriapoda", "Diplopoda", "Chilopoda", "Symphyla", "Pauropoda", "Annelida", "Platyhelminthes", "Nematoda",
         "Nematomorpha", "Nemertea", "Sipuncula", "Acanthocephala", "Chaetognatha", "Priapulida", "Xenacoelomorpha",
         "Echiura"}
SNAILS = {"Gastropoda", "Polyplacophora", "Scaphopoda", "Monoplacophora", "Solenogastres", "Caudofoveata",
          "Aplacophora"}
SEA_LIFE = {"Bivalvia", "Cnidaria", "Echinodermata", "Porifera", "Bryozoa", "Ectoprocta", "Brachiopoda", "Ctenophora",
            "Phoronida", "Entoprocta", "Hemichordata", "Placozoa"}
ALGAE = {"Ochrophyta"}                      # brown algae (Phaeophyceae) and their kin, in Chromista
SLIME_MOULDS = {"Mycetozoa", "Myxomycetes", "Myxogastria", "Myxogastrea", "Protosteliomycetes",
                "Dictyosteliomycetes"}


def group_of(names, genus=None, family=None):
    """The group for a taxon whose ancestors and own name are `names` (a set); `genus` and `family` are the names at
    those ranks, when the taxon has them."""
    n = names
    if genus == "Homo":
        return "person"
    if "Felidae" in n:
        return "cat"
    if "Canidae" in n:
        return "dog"
    if "Rodentia" in n:
        return "squirrel"
    if "Lagomorpha" in n:
        return "rabbit"
    if n & DEER_FAMILIES:
        return "deer"
    if n & WHALES:
        return "whale"
    if "Pteropodidae" in n:
        return "flyingfox"
    if "Chiroptera" in n:
        return "bat"
    if "Primates" in n:
        return "primate"
    if "Mammalia" in n:
        return "mammal"
    if "Aves" in n:
        if n & VULTURES:
            return "bird"
        if n & HAWK_ORDERS:
            return "hawk"
        if n & WADER_FAMILIES or n & WADER_ORDERS:
            return "wader"
        return "bird"
    if n & CROCODILIANS:
        return "alligator"
    if n & REPTILES:
        return "reptile"
    if "Anura" in n:
        return "frog"
    if n & SALAMANDERS:
        return "salamander"
    if n & SHARKS:
        return "shark"
    if n & FISH:
        return "fish"
    if n & TUNICATES:
        return "sealife"
    if "Hymenoptera" in n:
        return "insect" if family == "Formicidae" else "bee"
    if n & INSECTS:
        return "insect"
    if "Salticidae" in n:
        return "jumper"
    if "Araneae" in n:
        return "spider"
    if "Ixodida" in n:
        return "tick"
    if n & SCORPIONS:
        return "scorpion"
    if n & CRUSTACEANS:
        return "crab"
    if n & WORMS:
        return "worm"
    if "Cephalopoda" in n:
        return "cephalopod"
    if n & SNAILS:
        return "snail"
    if n & SEA_LIFE:
        return "sealife"
    if "Plantae" in n or n & ALGAE:
        return "plant"
    if "Fungi" in n:
        return "fungus"
    if n & SLIME_MOULDS:
        return "slime"
    return "other"


INFRA = {"subspecies", "variety", "form", "infrahybrid"}


def read_taxa(path):
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8", newline="") as f:
        r = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        head = next(r)
        col = {h: i for i, h in enumerate(head)}
        for need in ("taxon_id", "ancestry", "rank", "name"):
            if need not in col:
                sys.exit("taxa: no column %r in %r" % (need, head))
        for row in r:
            if len(row) < len(head):
                continue
            yield int(row[col["taxon_id"]]), row[col["ancestry"]], row[col["rank"]], row[col["name"]]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--taxa", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--summary", default="")
    args = ap.parse_args()
    rank, name, anc = {}, {}, {}
    for tid, ancestry, rk, nm in read_taxa(args.taxa):
        rank[tid], name[tid] = rk, nm
        anc[tid] = [int(a) for a in ancestry.split("/") if a.isdigit()] if ancestry else []
    print("taxa read: %d" % len(rank), flush=True)
    per_group, per_rank = Counter(), Counter()
    with open(args.out, "w", encoding="utf-8") as out:
        for tid in rank:
            line = anc[tid] + [tid]
            names = {name.get(a, "") for a in line}
            genus = next((name[a] for a in line if rank.get(a) == "genus"), None)
            family = next((name[a] for a in line if rank.get(a) == "family"), None)
            g = group_of(names, genus, family)
            unit = tid
            if rank[tid] in INFRA or rank[tid] == "hybrid":
                sp = [a for a in anc[tid] if rank.get(a) == "species"]
                if sp:
                    unit = sp[-1]
            order = None
            for want in ("order", "class", "phylum", "kingdom"):
                hit = [a for a in line if rank.get(a) == want]
                if hit:
                    order = hit[-1]
                    break
            out.write("%d\t%s\t%d\t%d\n" % (tid, g, unit, order or 0))
            per_group[g] += 1
            if rank[tid] == "species":
                per_rank[g] += 1
    if args.summary:
        with open(args.summary, "w", encoding="utf-8") as s:
            s.write("group\ttaxa\tspecies\n")
            for g in ALL:
                s.write("%s\t%d\t%d\n" % (g, per_group[g], per_rank[g]))
    for g in ALL:
        print("%-11s taxa %8d  species %8d" % (g, per_group[g], per_rank[g]))


if __name__ == "__main__":
    main()
