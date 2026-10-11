"""Tests for eyes.kind_of_eye. Run: python3 -m unittest discover -s tools/species -v

Taxonomies are written the way the GBIF backbone gives them (kingdom, phylum, class, order, family, genus),
including its habit of ranking Crocodylia, Squamata and Testudines as classes.
"""
import unittest

from eyes import KINDS, kind_of_eye, kind_of_record

A, CH, AR = "Animalia", "Chordata", "Arthropoda"


def k(kingdom, phylum, class_, order, family, genus):
    return kind_of_eye(kingdom, phylum, class_, order, family, genus)


class EveryRule(unittest.TestCase):
    def test_person_genus_homo(self):
        self.assertEqual(k(A, CH, "Mammalia", "Primates", "Hominidae", "Homo"), "person")

    def test_other_great_apes_are_not_person(self):
        self.assertEqual(k(A, CH, "Mammalia", "Primates", "Hominidae", "Pan"), "other")

    def test_cat_felidae(self):
        self.assertEqual(k(A, CH, "Mammalia", "Carnivora", "Felidae", "Felis"), "cat")
        self.assertEqual(k(A, CH, "Mammalia", "Carnivora", "Felidae", "Lynx"), "cat")

    def test_dog_canidae(self):
        self.assertEqual(k(A, CH, "Mammalia", "Carnivora", "Canidae", "Canis"), "dog")
        self.assertEqual(k(A, CH, "Mammalia", "Carnivora", "Canidae", "Urocyon"), "dog")

    def test_squirrel_rodentia(self):
        self.assertEqual(k(A, CH, "Mammalia", "Rodentia", "Sciuridae", "Sciurus"), "squirrel")
        self.assertEqual(k(A, CH, "Mammalia", "Rodentia", "Muridae", "Rattus"), "squirrel")
        self.assertEqual(k(A, CH, "Mammalia", "Rodentia", "Castoridae", "Castor"), "squirrel")

    def test_rabbit_lagomorpha(self):
        self.assertEqual(k(A, CH, "Mammalia", "Lagomorpha", "Leporidae", "Sylvilagus"), "rabbit")

    def test_deer_families(self):
        for fam, gen in (("Cervidae", "Odocoileus"), ("Bovidae", "Bos"), ("Equidae", "Equus"),
                         ("Antilocapridae", "Antilocapra"), ("Camelidae", "Lama"), ("Giraffidae", "Giraffa")):
            order = "Perissodactyla" if fam == "Equidae" else "Artiodactyla"
            self.assertEqual(k(A, CH, "Mammalia", order, fam, gen), "deer", fam)

    def test_hawk_orders(self):
        self.assertEqual(k(A, CH, "Aves", "Accipitriformes", "Accipitridae", "Buteo"), "hawk")
        self.assertEqual(k(A, CH, "Aves", "Accipitriformes", "Pandionidae", "Pandion"), "hawk")
        self.assertEqual(k(A, CH, "Aves", "Falconiformes", "Falconidae", "Falco"), "hawk")
        self.assertEqual(k(A, CH, "Aves", "Falconiformes", "Falconidae", "Caracara"), "hawk")

    def test_wader_families(self):
        for order, fam, gen in (("Pelecaniformes", "Ardeidae", "Ardea"), ("Pelecaniformes", "Threskiornithidae", "Eudocimus"),
                                ("Ciconiiformes", "Ciconiidae", "Mycteria"), ("Gruiformes", "Gruidae", "Antigone"),
                                ("Gruiformes", "Aramidae", "Aramus"), ("Gruiformes", "Rallidae", "Gallinula")):
            self.assertEqual(k(A, CH, "Aves", order, fam, gen), "wader", fam)

    def test_wader_orders(self):
        self.assertEqual(k(A, CH, "Aves", "Columbiformes", "Columbidae", "Zenaida"), "wader")
        self.assertEqual(k(A, CH, "Aves", "Galliformes", "Phasianidae", "Meleagris"), "wader")
        self.assertEqual(k(A, CH, "Aves", "Galliformes", "Odontophoridae", "Colinus"), "wader")

    def test_bird_any_other_aves(self):
        self.assertEqual(k(A, CH, "Aves", "Passeriformes", "Cardinalidae", "Cardinalis"), "bird")
        self.assertEqual(k(A, CH, "Aves", "Anseriformes", "Anatidae", "Anas"), "bird")
        self.assertEqual(k(A, CH, "Aves", "Charadriiformes", "Charadriidae", "Charadrius"), "bird")
        self.assertEqual(k(A, CH, "Aves", None, None, None), "bird")

    def test_alligator_crocodylia_as_class(self):
        self.assertEqual(k(A, CH, "Crocodylia", None, "Alligatoridae", "Alligator"), "alligator")

    def test_alligator_crocodylia_as_order_of_reptilia(self):
        self.assertEqual(k(A, CH, "Reptilia", "Crocodylia", "Alligatoridae", "Alligator"), "alligator")
        self.assertEqual(k(A, CH, "Reptilia", "Crocodylia", "Crocodylidae", "Crocodylus"), "alligator")

    def test_reptile_squamata_as_class_and_as_order(self):
        self.assertEqual(k(A, CH, "Squamata", None, "Dactyloidae", "Anolis"), "reptile")
        self.assertEqual(k(A, CH, "Reptilia", "Squamata", "Dactyloidae", "Anolis"), "reptile")
        self.assertEqual(k(A, CH, "Squamata", None, "Colubridae", "Coluber"), "reptile")

    def test_reptile_testudines_as_class_and_as_order(self):
        self.assertEqual(k(A, CH, "Testudines", None, "Testudinidae", "Gopherus"), "reptile")
        self.assertEqual(k(A, CH, "Reptilia", "Testudines", "Emydidae", "Pseudemys"), "reptile")

    def test_reptile_sphenodontia(self):
        self.assertEqual(k(A, CH, "Reptilia", "Sphenodontia", "Sphenodontidae", "Sphenodon"), "reptile")
        self.assertEqual(k(A, CH, "Reptilia", "Rhynchocephalia", "Sphenodontidae", "Sphenodon"), "reptile")

    def test_reptile_class_without_order(self):
        self.assertEqual(k(A, CH, "Reptilia", None, None, None), "reptile")

    def test_frog_anura(self):
        self.assertEqual(k(A, CH, "Amphibia", "Anura", "Ranidae", "Lithobates"), "frog")
        self.assertEqual(k(A, CH, "Amphibia", "Anura", "Hylidae", "Dryophytes"), "frog")

    def test_bee_hymenoptera(self):
        self.assertEqual(k(A, AR, "Insecta", "Hymenoptera", "Apidae", "Apis"), "bee")
        self.assertEqual(k(A, AR, "Insecta", "Hymenoptera", "Vespidae", "Polistes"), "bee")

    def test_ants_are_insects_not_bees(self):
        self.assertEqual(k(A, AR, "Insecta", "Hymenoptera", "Formicidae", "Solenopsis"), "insect")
        self.assertEqual(k(A, AR, "Insecta", "Hymenoptera", "Formicidae", "Camponotus"), "insect")

    def test_insect_any_other(self):
        self.assertEqual(k(A, AR, "Insecta", "Lepidoptera", "Nymphalidae", "Danaus"), "insect")
        self.assertEqual(k(A, AR, "Insecta", "Odonata", "Libellulidae", "Erythemis"), "insect")
        self.assertEqual(k(A, AR, "Insecta", None, None, None), "insect")

    def test_plant_kingdom(self):
        self.assertEqual(k("Plantae", "Tracheophyta", "Magnoliopsida", "Fagales", "Fagaceae", "Quercus"), "plant")
        self.assertEqual(k("Plantae", "Bryophyta", "Bryopsida", None, None, None), "plant")

    def test_other(self):
        self.assertEqual(k("Fungi", "Basidiomycota", "Agaricomycetes", "Agaricales", "Amanitaceae", "Amanita"), "other")
        self.assertEqual(k(A, AR, "Arachnida", "Araneae", "Araneidae", "Argiope"), "other")
        self.assertEqual(k(A, CH, "Actinopterygii", "Perciformes", "Centrarchidae", "Micropterus"), "other")
        self.assertEqual(k(A, "Mollusca", "Gastropoda", None, "Ampullariidae", "Pomacea"), "other")
        self.assertEqual(k("Chromista", None, None, None, None, None), "other")
        self.assertEqual(k("Protozoa", "Mycetozoa", None, None, None, None), "other")
        self.assertEqual(k(None, None, None, None, None, None), "other")


class AwkwardCases(unittest.TestCase):
    def test_new_world_vultures_are_bird_under_either_order(self):
        self.assertEqual(k(A, CH, "Aves", "Accipitriformes", "Cathartidae", "Cathartes"), "bird")
        self.assertEqual(k(A, CH, "Aves", "Accipitriformes", "Cathartidae", "Coragyps"), "bird")
        self.assertEqual(k(A, CH, "Aves", "Cathartiformes", "Cathartidae", "Cathartes"), "bird")
        self.assertEqual(k(A, CH, "Aves", "Cathartiformes", None, None), "bird")

    def test_owls_are_bird(self):
        self.assertEqual(k(A, CH, "Aves", "Strigiformes", "Strigidae", "Strix"), "bird")
        self.assertEqual(k(A, CH, "Aves", "Strigiformes", "Tytonidae", "Tyto"), "bird")

    def test_pelicans_bird_but_herons_and_ibises_wader(self):
        self.assertEqual(k(A, CH, "Aves", "Pelecaniformes", "Pelecanidae", "Pelecanus"), "bird")
        self.assertEqual(k(A, CH, "Aves", "Pelecaniformes", "Ardeidae", "Egretta"), "wader")
        self.assertEqual(k(A, CH, "Aves", "Pelecaniformes", "Threskiornithidae", "Platalea"), "wader")
        self.assertEqual(k(A, CH, "Aves", "Suliformes", "Anhingidae", "Anhinga"), "bird")

    def test_mammals_without_an_eye_of_their_own_are_other(self):
        cases = {
            "pig": ("Artiodactyla", "Suidae", "Sus"),
            "bat": ("Chiroptera", "Molossidae", "Tadarida"),
            "raccoon": ("Carnivora", "Procyonidae", "Procyon"),
            "opossum": ("Didelphimorphia", "Didelphidae", "Didelphis"),
            "armadillo": ("Cingulata", "Dasypodidae", "Dasypus"),
            "otter": ("Carnivora", "Mustelidae", "Lontra"),
            "manatee": ("Sirenia", "Trichechidae", "Trichechus"),
        }
        for name, (order, fam, gen) in cases.items():
            self.assertEqual(k(A, CH, "Mammalia", order, fam, gen), "other", name)

    def test_salamanders_are_other(self):
        self.assertEqual(k(A, CH, "Amphibia", "Caudata", "Salamandridae", "Notophthalmus"), "other")
        self.assertEqual(k(A, CH, "Amphibia", "Caudata", "Sirenidae", "Siren"), "other")

    def test_fungi_and_spiders_are_other(self):
        self.assertEqual(k("Fungi", "Ascomycota", "Lecanoromycetes", None, None, None), "other")
        self.assertEqual(k(A, AR, "Arachnida", "Araneae", "Salticidae", "Phidippus"), "other")

    def test_blank_strings_count_as_missing(self):
        self.assertEqual(k(A, CH, "  ", "", "Felidae", ""), "cat")
        self.assertEqual(kind_of_eye(), "other")

    def test_record_form_uses_gbif_field_names(self):
        rec = {"kingdom": A, "phylum": CH, "class": "Aves", "order": "Pelecaniformes", "family": "Ardeidae", "genus": "Ardea"}
        self.assertEqual(kind_of_record(rec), "wader")
        self.assertEqual(kind_of_record({"kingdom": "Plantae"}), "plant")

    def test_answers_are_always_one_of_the_sixteen(self):
        self.assertEqual(len(KINDS), 16)
        samples = [(A, CH, c, o, f, g) for c in ("Aves", "Mammalia", "Squamata", None)
                   for o in ("Rodentia", "Falconiformes", None) for f in ("Felidae", "Ardeidae", None) for g in ("Homo", None)]
        for s in samples:
            self.assertIn(k(*s), KINDS)


if __name__ == "__main__":
    unittest.main()
