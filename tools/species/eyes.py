"""The kind of eye a species is drawn with, from its GBIF backbone taxonomy.

The rules are the table in docs/CONTRACTS.md ("The sixteen kinds of eye"); the first rule that matches wins.
Two things the table states in prose are coded here as rules:
  - New World vultures (family Cathartidae, order Cathartiformes) go to `bird` before the `hawk` rule,
    because the GBIF backbone may file Cathartidae under Accipitriformes.
  - GBIF ranks Crocodylia, Squamata and Testudines either as orders of class Reptilia or as classes of their own;
    both forms are recognized.
Usage: kind_of_eye(kingdom, phylum, class_, order, family, genus) -> one of KINDS.

Since build 22 the pocket model's kinds head also names the nineteen groups of creatures that have no view yet (GROUPS
in src/cam.a.js), and a species table may file a species under its group. kind_or_group gives the kind of eye, or for a
taxon kind_of_eye sends to `other`, its group, by the rules of tools/world/groups.py on the backbone's ranks (the rules
the group head's photos were sorted by). Three moves come with them: springtails and their kin (Collembola, Diplura,
Protura) are `insect`, and seaweeds and their kin (Ochrophyta) `plant`, as the head learned them.
Usage: kind_or_group(kingdom, phylum, class_, order, family, genus) -> one of KINDS or GROUPS.
"""
import importlib.util
import os

KINDS = ("cat", "dog", "squirrel", "deer", "rabbit", "hawk", "wader", "bird",
         "alligator", "reptile", "frog", "bee", "insect", "plant", "other", "person")
GROUPS = ("fungus", "slime", "spider", "jumper", "fish", "shark", "snail", "sealife", "crab", "salamander", "worm",
          "scorpion", "tick", "mammal", "primate", "whale", "bat", "flyingfox", "cephalopod")

DEER_FAMILIES = {"Cervidae", "Bovidae", "Equidae", "Antilocapridae", "Camelidae", "Giraffidae"}
HAWK_ORDERS = {"Accipitriformes", "Falconiformes"}
VULTURE_FAMILIES = {"Cathartidae"}
VULTURE_ORDERS = {"Cathartiformes"}
WADER_FAMILIES = {"Ardeidae", "Threskiornithidae", "Ciconiidae", "Gruidae", "Aramidae", "Rallidae"}
WADER_ORDERS = {"Columbiformes", "Galliformes"}
CROCODILIANS = {"Crocodylia", "Crocodilia"}
# Reptile groups other than crocodilians, as GBIF may rank them (order of Reptilia, or a class of its own).
REPTILE_GROUPS = {"Squamata", "Testudines", "Sphenodontia", "Rhynchocephalia"}
REPTILE_CLASSES = {"Reptilia"} | REPTILE_GROUPS


def _clean(v):
    if v is None:
        return None
    v = str(v).strip()
    return v or None


def kind_of_eye(kingdom=None, phylum=None, class_=None, order=None, family=None, genus=None):
    """Return the kind of eye for a taxon given its backbone ranks (any of them may be None)."""
    kingdom, phylum, class_, order, family, genus = map(_clean, (kingdom, phylum, class_, order, family, genus))
    if genus == "Homo":
        return "person"
    if family == "Felidae":
        return "cat"
    if family == "Canidae":
        return "dog"
    if order == "Rodentia":
        return "squirrel"
    if order == "Lagomorpha":
        return "rabbit"
    if family in DEER_FAMILIES:
        return "deer"
    if family in VULTURE_FAMILIES or order in VULTURE_ORDERS:
        return "bird"
    if order in HAWK_ORDERS:
        return "hawk"
    if family in WADER_FAMILIES:
        return "wader"
    if class_ == "Aves" and order in WADER_ORDERS:
        return "wader"
    if class_ == "Aves":
        return "bird"
    if class_ in CROCODILIANS or order in CROCODILIANS:
        return "alligator"
    if class_ in REPTILE_CLASSES or order in REPTILE_GROUPS:
        return "reptile"
    if order == "Anura":
        return "frog"
    if order == "Hymenoptera" and family != "Formicidae":
        return "bee"
    if class_ == "Insecta":
        return "insect"
    if kingdom == "Plantae":
        return "plant"
    return "other"


def kind_of_record(rec):
    """kind_of_eye for a dict carrying GBIF field names (kingdom, phylum, class, order, family, genus)."""
    return kind_of_eye(rec.get("kingdom"), rec.get("phylum"), rec.get("class"), rec.get("order"),
                       rec.get("family"), rec.get("genus"))


def _world_groups():
    """tools/world/groups.py, loaded by its path so that nothing in that folder can stand in for a module of Python's."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "world", "groups.py")
    spec = importlib.util.spec_from_file_location("regards_world_groups", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_GROUPS_MOD = None


def kind_or_group(kingdom=None, phylum=None, class_=None, order=None, family=None, genus=None):
    """The kind of eye, or for a taxon kind_of_eye sends to `other`, its group of creatures (or `other` still)."""
    global _GROUPS_MOD
    k = kind_of_eye(kingdom, phylum, class_, order, family, genus)
    if k != "other":
        return k
    if _GROUPS_MOD is None:
        _GROUPS_MOD = _world_groups()
    ranks = [_clean(v) for v in (kingdom, phylum, class_, order, family, genus)]
    g = _GROUPS_MOD.group_of({v for v in ranks if v}, ranks[5], ranks[4])
    return "other" if g == "person" else g


def kind_or_group_of_record(rec):
    """kind_or_group for a dict carrying GBIF field names."""
    return kind_or_group(rec.get("kingdom"), rec.get("phylum"), rec.get("class"), rec.get("order"),
                         rec.get("family"), rec.get("genus"))
