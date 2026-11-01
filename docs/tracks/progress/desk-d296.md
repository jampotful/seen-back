# desk-d296: adult eye numbers and eye states in Hymenoptera and Diptera taxonomy papers, 5 records

Branch research/desk-d296 from origin/main. About 55 WebSearches (3 extended) plus fetches. `python3 -I tools/senses/check.py | grep 'd296\.'`: 5 records, 0 problems. Crossref read for all three DOIs (author order matches the pages; all CC BY 4.0 vor; no issue numbers). Grep of main docs/ and desk/audit branches by species and DOI: no repeats. No new key (ommatidia_count already used on main; eye_type string).

Filed (docs/views/evidence/desk-d296.jsonl):
1. Strumigenys subterranea (Formicidae), eye a single facet, holotype worker only (n = 1), ZooKeys 970.
2. Leptanilla voldemort (Formicidae), "Eyes absent.", worker caste (holotype and paratype), ZooKeys 1197. Cited URL is the Pensoft XML returned by search.
3-5. Blepharicera gengdica, B. balangshana, B. kongsica (Diptera, Blephariceridae), Diagnosis sentences giving the dorsal:ventral size ratio of the divided male eye (1/20, equal, 1/15), ZooKeys 1085. Male only; no ommatidia numbers (those sentences are too long).

Dropped:
- On main (any trait, species or DOI): Lymantria xylina, Grapholita molesta, Scythris sinensis, Camponotus consobrinus, Temnothorax albipennis, Vespa crabro / Vespula vulgaris facet (pone.0021892), Myrmecia midas / tarsata, Formica wood ants (srep24204), Cacopsylla chinensis, Empoasca onukii, Ceratosolen gravelyi, Arge similis, honeybee five-species PLOS ONE paper, Platythyrea and Carebara (ZooKeys 1115, 1190).
- Sentence arrives in pieces (over the tool's ~125 characters): Monomorium brachypterum and M. intrudens ommatidia (ZooKeys 1250, counts in a Mann-Whitney sentence and a Remarks sentence; Worker description sentence also long); Strumigenys subterranea Diagnosis and Comments; Blepharicera Male/Female Head sentences (row counts).
- Wrong page returned: article_preview.php for ids 114072 and 36139 returned other articles (Aptesis; Leptanilla for a Ponera query), so the Ponera tudigong (ZooKeys 867) record was not made and Leptanilla was filed from the XML URL that came from search.
- Licence absent or restricted: Bactrocera cucurbitae, B. tau, B. dorsalis morphometry (Florida Entomologist 98, BioOne page without licence).
- Numbers absent: Osmia cornuta / Halictus scabiosae / Polistes dominula urban eye study (Scientific Reports 14, no absolute counts), Mythimna separata (Insects 15), Blepharicera introduction sentence (family-level, literature statement).
- Outside the angle or order list: Cactisma camanchaca (Zygentoma), Odontothrips loti (Thysanoptera), Omma (beetle fossil).
- Searches for Aedes/Anopheles, hoverfly, horsefly, Trichoptera, Neuroptera, Orthoptera (mantis, cricket, locust), bee eye scaling (Bombus, Osmia) returned PMC, Springer, eLife, Wiley, theses or items already on main; nothing filed.
- Crossref list queries with container-title filter worked for Insects and Scientific Reports only; PLOS ONE, Biology and Frontiers in Zoology filters returned client errors.
