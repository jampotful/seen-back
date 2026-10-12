#!/usr/bin/env python3
"""Checks of tools/world/groups.py on lineages as iNaturalist's taxonomy writes them. Run: python3 -I tools/world/test_groups.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from groups import group_of, GROUPS, ALL  # noqa: E402

ANIMALS = ["Animalia"]
CHORDATES = ANIMALS + ["Chordata", "Vertebrata"]
MAMMALS = CHORDATES + ["Mammalia"]
ARTHROPODS = ANIMALS + ["Arthropoda"]
CASES = [
    (MAMMALS + ["Primates", "Hominidae", "Homo", "Homo sapiens"], "Homo", "Hominidae", "person"),
    (MAMMALS + ["Carnivora", "Felidae", "Lynx", "Lynx rufus"], "Lynx", "Felidae", "cat"),
    (MAMMALS + ["Carnivora", "Canidae", "Vulpes"], "Vulpes", "Canidae", "dog"),
    (MAMMALS + ["Rodentia", "Sciuridae", "Sciurus"], "Sciurus", "Sciuridae", "squirrel"),
    (MAMMALS + ["Lagomorpha", "Leporidae", "Sylvilagus"], "Sylvilagus", "Leporidae", "rabbit"),
    (MAMMALS + ["Artiodactyla", "Cervidae", "Odocoileus"], "Odocoileus", "Cervidae", "deer"),
    (MAMMALS + ["Artiodactyla", "Cetacea", "Delphinidae", "Tursiops"], "Tursiops", "Delphinidae", "whale"),
    (MAMMALS + ["Carnivora", "Otariidae", "Zalophus"], "Zalophus", "Otariidae", "whale"),
    (MAMMALS + ["Sirenia", "Trichechidae", "Trichechus"], "Trichechus", "Trichechidae", "whale"),
    (MAMMALS + ["Chiroptera", "Pteropodidae", "Pteropus"], "Pteropus", "Pteropodidae", "flyingfox"),
    (MAMMALS + ["Chiroptera", "Vespertilionidae", "Eptesicus"], "Eptesicus", "Vespertilionidae", "bat"),
    (MAMMALS + ["Primates", "Cercopithecidae", "Macaca"], "Macaca", "Cercopithecidae", "primate"),
    (MAMMALS + ["Carnivora", "Procyonidae", "Procyon"], "Procyon", "Procyonidae", "mammal"),
    (MAMMALS + ["Didelphimorphia", "Didelphidae", "Didelphis"], "Didelphis", "Didelphidae", "mammal"),
    (MAMMALS + ["Artiodactyla", "Suidae", "Sus"], "Sus", "Suidae", "mammal"),
    (CHORDATES + ["Aves", "Cathartiformes", "Cathartidae", "Coragyps"], "Coragyps", "Cathartidae", "bird"),
    (CHORDATES + ["Aves", "Accipitriformes", "Cathartidae", "Cathartes"], "Cathartes", "Cathartidae", "bird"),
    (CHORDATES + ["Aves", "Accipitriformes", "Accipitridae", "Buteo"], "Buteo", "Accipitridae", "hawk"),
    (CHORDATES + ["Aves", "Pelecaniformes", "Ardeidae", "Ardea"], "Ardea", "Ardeidae", "wader"),
    (CHORDATES + ["Aves", "Galliformes", "Phasianidae", "Meleagris"], "Meleagris", "Phasianidae", "wader"),
    (CHORDATES + ["Aves", "Passeriformes", "Cardinalidae", "Cardinalis"], "Cardinalis", "Cardinalidae", "bird"),
    (CHORDATES + ["Reptilia", "Crocodylia", "Alligatoridae", "Alligator"], "Alligator", "Alligatoridae", "alligator"),
    (CHORDATES + ["Reptilia", "Squamata", "Dactyloidae", "Anolis"], "Anolis", "Dactyloidae", "reptile"),
    (CHORDATES + ["Testudines", "Testudinidae", "Gopherus"], "Gopherus", "Testudinidae", "reptile"),
    (CHORDATES + ["Amphibia", "Anura", "Hylidae", "Dryophytes"], "Dryophytes", "Hylidae", "frog"),
    (CHORDATES + ["Amphibia", "Caudata", "Salamandridae", "Notophthalmus"], "Notophthalmus", "Salamandridae", "salamander"),
    (CHORDATES + ["Amphibia", "Gymnophiona", "Caeciliidae"], None, "Caeciliidae", "salamander"),
    (CHORDATES + ["Elasmobranchii", "Carcharhiniformes", "Carcharhinidae"], None, "Carcharhinidae", "shark"),
    (CHORDATES + ["Elasmobranchii", "Myliobatiformes", "Dasyatidae"], None, "Dasyatidae", "shark"),
    (CHORDATES + ["Actinopterygii", "Centrarchiformes", "Centrarchidae", "Lepomis"], "Lepomis", "Centrarchidae", "fish"),
    (CHORDATES + ["Petromyzonti", "Petromyzontiformes"], None, None, "fish"),
    (ANIMALS + ["Chordata", "Tunicata", "Ascidiacea"], None, None, "sealife"),
    (ARTHROPODS + ["Hexapoda", "Insecta", "Hymenoptera", "Apidae", "Apis"], "Apis", "Apidae", "bee"),
    (ARTHROPODS + ["Hexapoda", "Insecta", "Hymenoptera", "Formicidae", "Camponotus"], "Camponotus", "Formicidae", "insect"),
    (ARTHROPODS + ["Hexapoda", "Insecta", "Lepidoptera", "Nymphalidae"], None, "Nymphalidae", "insect"),
    (ARTHROPODS + ["Hexapoda", "Collembola", "Entomobryomorpha"], None, None, "insect"),
    (ARTHROPODS + ["Chelicerata", "Arachnida", "Araneae", "Salticidae", "Phidippus"], "Phidippus", "Salticidae", "jumper"),
    (ARTHROPODS + ["Chelicerata", "Arachnida", "Araneae", "Lycosidae"], None, "Lycosidae", "spider"),
    (ARTHROPODS + ["Chelicerata", "Arachnida", "Ixodida", "Ixodidae", "Amblyomma"], "Amblyomma", "Ixodidae", "tick"),
    (ARTHROPODS + ["Chelicerata", "Arachnida", "Trombidiformes", "Eriophyidae"], None, "Eriophyidae", "other"),
    (ARTHROPODS + ["Chelicerata", "Arachnida", "Opiliones"], None, None, "scorpion"),
    (ARTHROPODS + ["Chelicerata", "Arachnida", "Solifugae"], None, None, "scorpion"),
    (ARTHROPODS + ["Chelicerata", "Merostomata", "Xiphosurida", "Limulidae"], None, "Limulidae", "crab"),
    (ARTHROPODS + ["Crustacea", "Malacostraca", "Isopoda", "Armadillidiidae"], None, "Armadillidiidae", "crab"),
    (ARTHROPODS + ["Crustacea", "Malacostraca", "Decapoda", "Cambaridae"], None, "Cambaridae", "crab"),
    (ARTHROPODS + ["Myriapoda", "Diplopoda"], None, None, "worm"),
    (ANIMALS + ["Annelida", "Clitellata", "Haplotaxida"], None, None, "worm"),
    (ANIMALS + ["Platyhelminthes", "Rhabditophora", "Tricladida"], None, None, "worm"),
    (ANIMALS + ["Mollusca", "Cephalopoda", "Octopoda"], None, None, "cephalopod"),
    (ANIMALS + ["Mollusca", "Gastropoda", "Stylommatophora"], None, None, "snail"),
    (ANIMALS + ["Mollusca", "Polyplacophora", "Chitonida"], None, None, "snail"),
    (ANIMALS + ["Mollusca", "Bivalvia", "Unionida"], None, None, "sealife"),
    (ANIMALS + ["Cnidaria", "Anthozoa", "Actiniaria"], None, None, "sealife"),
    (ANIMALS + ["Echinodermata", "Asteroidea"], None, None, "sealife"),
    (ANIMALS + ["Porifera", "Demospongiae"], None, None, "sealife"),
    (ANIMALS + ["Tardigrada", "Eutardigrada"], None, None, "other"),
    (["Plantae", "Tracheophyta", "Magnoliopsida", "Fagales", "Fagaceae", "Quercus"], "Quercus", "Fagaceae", "plant"),
    (["Chromista", "Ochrophyta", "Phaeophyceae", "Laminariales"], None, None, "plant"),
    (["Chromista", "Oomycota", "Peronosporea"], None, None, "other"),
    (["Fungi", "Basidiomycota", "Agaricomycetes", "Agaricales"], None, None, "fungus"),
    (["Fungi", "Ascomycota", "Lecanoromycetes", "Lecanorales"], None, None, "fungus"),
    (["Protozoa", "Mycetozoa", "Myxomycetes", "Physarales"], None, None, "slime"),
    (["Bacteria", "Cyanobacteria"], None, None, "other"),
]


def main():
    bad = 0
    for names, genus, family, want in CASES:
        got = group_of(set(names), genus, family)
        if got != want:
            bad += 1
            print("WRONG %s -> %s (wanted %s)" % ("/".join(names), got, want))
    seen = {c[3] for c in CASES}
    missing = [g for g in ALL if g not in seen]
    if missing:
        bad += 1
        print("groups with no case: %s" % ", ".join(missing))
    assert len(GROUPS) == 33, len(GROUPS)
    print("%d cases, %d wrong" % (len(CASES), bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
