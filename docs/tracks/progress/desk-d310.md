# desk-d310: eye states of a giant longhorn beetle, an intertidal ant and a truffle-feeding beetle larva, 5 records

Branch research/desk-d310 from origin/main. About 58 WebSearches (several restricted to pensoft, mdpi, plos, peerj domains); WebFetch only on URLs returned by searches, plus Crossref single-DOI lookups (api.crossref.org/v1/works/) for all three DOIs filed. `python3 -I tools/senses/check.py | grep d310`: 5 records, 0 problems. Traits: eye_type, ommatidia_count, facet_diameter_um, rhabdom_um (all keys already on main; notes say so where check.py needs it).

Repeat check: every species and DOI grepped over origin/main docs/views and docs/tracks/progress and over the evidence and progress files of origin/research/desk-d296 to d309 before filing; no hits for the three species or DOIs.

Filed (docs/views/evidence/desk-d310.jsonl):
1. Titanus giganteus, eye_type apposition ("It seems ..."), one dead male, SEM only, Insects 11(2): 120.
2-4. Polyrhachis sokolova workers: ommatidia_count 596.2 per eye (n = 5; the Discussion rounds to 590, in conditions), facet_diameter_um 23.5 (n = 50 facets, 5 ants; largest 33 um), rhabdom_um length 79 to 135 um by region, PLoS ONE 8(10): e76015.
5. Leiodes cinnamomea, larval stemmata absent (instars I to III) and adults with eyes, Insects 13(3): 249.

Dropped candidates:
- Already on main: Panorpa dubia, Camponotus consobrinus, Notemigonus crysoleucas (PeerJ 1113), Calyptommatus nicterus, Rousettus aegyptiacus, Cacopsylla chinensis, Tomicus yunnanensis, Ceratosolen gravelyi, Histia flabellicornis, Cylindroiulus villumi, Iandumoema smeagol, Dineutus mellyi.
- Pooled or unclear species: Megaphragma (PLOS ONE 0175566, count given for two species together, "Compound eyes lateral, consisting of 28-30 ommatidia"); Meimuna mongolica (Insects 13: 1170, eye sentences are Introduction literature statements, no count); Mantis religiosa/Tenodera/Polyspilota (EJE 2012, 4,000 to 9,000 image points across species, no licence sentence).
- Telegraphic sentences without a verb: Zorotypus vinsoni alata female ("Compound eyes and three black ocelli present."), Zorotypus komatsui (long semicolon sentence), Phasmomantella (globular eyes), Cylindrogaster cavernicola ("Eyes prominent, ..."), Cangshanaltica fuanensis larva ("Stemmata absent, one pair of black eyespots ... present behind antenna"), Leschenius vulcanorum larva ("Stemmata absent."), Leptanilla voldemort ("Eyes absent.").
- Genus- or family-level: Scolopocryptops troglocaudatus ("The lack of eyes is shared by all species of Scolopocryptopidae").
- Lab strain: Danio rerio AB strain (PeerJ 1113).
- No numbers or values only in tables/supplement: Pontoniine shrimps (PLOS ONE 0099505), Protopolybia sedula (JEB 229: jeb252873), Orientogomphus minor nymph (long sentence), Bagous claudicans larva (stemmata only in Discussion fragments).
- Licence: Myrmecia ocellar structure (JEB 220: 4383, user licence, not CC), Tupaia belangeri treeshrew retina (Folia Morphologica, CC BY-NC-ND), Rousettus retina (Egyptian J Histol, no licence on page).
- Not reachable: nature.com Scientific Reports pages (client error), PMC copies, macvetrev blind mole-rat PDF (binary), EJT view pages (abstract only; Zephronia and Sphaeromimus eye sentences not in text returned), Pensoft landing pages for isopods (no description text).

Angle result: terrestrial isopods, Opiliones, Symphyla, Diplura, Protura, Dermaptera, Mantodea, Isoptera, Psocoptera gave only telegraphic Diagnosis or Description lines or pages without body text; the yield came from MDPI Insects and PLOS ONE physiology/anatomy papers whose eye sentences have verbs. Bat, rodent and primate searches returned PMC copies, closed papers or no species-level eye sentences.

Weak spots for the auditor:
- Titanus: the value is hedged ("It seems"); one specimen.
- Polyrhachis ommatidia sentence ends with a figure reference that the tool omitted; the quote ends with an ellipsis. The facet sentence ends "(Fig. 2)." as the tool returned it. Family and order are printed only in a reference title.
- Leiodes sentence is a long comma sentence read in three consecutive pieces; the "adults have eyes" clause is not backed by an adult description in the paper.

Questions: none.

## Desk disposition after audit 408
Audit 408: 2 fixable errors in 5 (lines 1 and 4); replacements and the auditor's optional additions applied; all 5 records merged. Open owner question: the PLOS correction of 12 Nov 2013 (10.1371/annotation/b18fcad6-597e-4ba9-86bc-f21030ed3a1b) to the Polyrhachis sokolova paper could not be read (PLOS rate limit; PMC refused); lines 2 to 4 carry a note saying so.
