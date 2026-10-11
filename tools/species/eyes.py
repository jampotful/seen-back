"""The kind of eye a species is drawn with, from its GBIF backbone taxonomy.

The rules are the table in docs/CONTRACTS.md ("The sixteen kinds of eye"); the first rule that matches wins.
Two things the table states in prose are coded here as rules:
  - New World vultures (family Cathartidae, order Cathartiformes) go to `bird` before the `hawk` rule,
    because the GBIF backbone may file Cathartidae under Accipitriformes.
  - GBIF ranks Crocodylia, Squamata and Testudines either as orders of class Reptilia or as classes of their own;
    both forms are recognized.
Usage: kind_of_eye(kingdom, phylum, class_, order, family, genus) -> one of KINDS.
"""

KINDS = ("cat", "dog", "squirrel", "deer", "rabbit", "hawk", "wader", "bird",
         "alligator", "reptile", "frog", "bee", "insect", "plant", "other", "person")

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
