# desk-d315: eye states of parasitoid wasps, cockroaches, earwigs, stick insects, water striders, mantises and two Mesozoic fossils, 24 records

Branch research/desk-d315 from origin/main. About 45 WebSearches and WebFetch only on URLs returned by searches, plus Pensoft article XML (`/article/ID/download/xml/`) for IDs that appeared in a Pensoft taxon browse page or a Crossref list query. `python3 -I tools/senses/check.py | grep d315`: 24 records, 0 problems. Trait: eye_type only (key on main). Crossref single-DOI lookups answered for every DOI filed (two Pensoft DOIs through a list query).

Repeat check: a text index of origin/main docs/ plus the evidence, progress, searched and audit files of every unmerged desk and audit branch was built once; every species and DOI was grepped before filing (no hit for any of the 24 beyond the desk-d297 DOI and a dropped-candidate note for Nocticola baiguensis).

Filed (docs/views/evidence/desk-d315.jsonl):
1-2. Calogalesus sinicus (female, ZooKeys 626) and Monelata truncata (female holotype, ZooKeys 574), Diapriidae.
3. Nocticola baiguensis, male, eyes reduced to a few ommatidia (ZooKeys 1232; the two sister species are on desk-d297).
4. Mesodiplatys falcifer, cave earwig, eyes conspicuously prominent (ZooKeys 790).
5-7. Rhagovelia depressa, R. tantilloides (apterous males) and Steinovelia vittata (macropterous male), Veliidae (ZooKeys 1126).
8. Ekpagloderma gracilentum, Middle Jurassic fossil earwig, female holotype (Insects 14(7): 614).
9. Pseudoparamenexenus beiliuensis, female, compound eyes prominent, ocelli lacking next (Diversity 17(9): 637).
10. Prolucanus beipiaoensis, Early Cretaceous fossil stag beetle (Insects 13(3): 272).
11-13. Pseudoeupolyphaga duani (male: eyes and ocelli well-developed; female paratype: ocelli degraded to two spots) and P. menglianensis (male) (ZooKeys 1261).
14-16. Cnipsomorpha yunnanensis (female), C. yuxiensis (female, male) (ZooKeys 1176).
17-21. Cranopygia kongqueshana, lisu, liuhuaishana, longibifurcata, shidianensis, identical male Head sentence (ZooKeys 1262).
22. Diplatys sahyadriensis, male holotype (ZooKeys 1088).
23. Didymocorypha libaii, male holotype of a high-altitude wingless mantis (ZooKeys 922).
24. Arria muscoamicta, male holotype (ZooKeys 1028; classification block prints Mantidae, title and text Haaniidae, Haaniidae used).

Dropped candidates:
- Licence: Cindarella eucalla (Sci Rep 3: 2751, over 2,000 ommatidia per eye, lens 60-140 um) is CC BY-NC-ND; the radiodont compound-eye paper (Disparate compound eyes of Cambrian radiodonts) surfaced only as repository copies.
- Pooled or literature-derived: Kronoscorpio danielsi and Mesophonus spp. facet counts (Sci Rep 9: 17797) sit in one 3-species sentence of about 42 words citing earlier work; the Jaekelopterus ">3545 facets" is a clause in a 60-word sentence resting on a cited reference; Palaeocharinus is a genus-level sp.
- No lens, facet or ommatidium numbers in the open text: trilobite papers APP 58 (Remopleurides, Hibbertia, Pliomerina eye clauses inside long sentences) and APP 66 (Anacheirurus), Oelandocaris (APP 53, no compound eye data), Nature Commun. 12: 2081 (comment), Sci Rep 11: 19505 (phacopid hyper-compound eye, counts per genus only), MDPI trilobite review.
- Fossil papers with no eye text or eyes only in long sentences: Osmylopsychopidae, Itaphlebia, Hagloidea (abstract only), Jibaissodes peichenae (compound eye 1.8 mm long inside a long sentence), Applanatiforceps angustus (eye clause ends a long head sentence), Glesoconomorphus ekaterinae and Camelosphecia (amber).
- Eye sentence is a ratio to another structure or colour only: Centistidea spp. (eye 1.8 times temple), Pambolus/Paroplitis, Ismarus spp. (eye height versus malar space), Zagrammosoma dulanense ("Eyes bare."), Cochleopsaltria huboliao (colour), Claviplatys henryi (clauses), Hornylia obtusipetala ("eyes rather small" inside a long sentence), Tachycines trapezialis (on main).
- No eye text reached: Triatoma mopan (XML text returned only introduction and methods), Eucorydia, Unihamus, Margattea and Allacta (not opened), Diplatys/Mesodiplatys beyond the two filed, Termite Rhinotermitidae of New Guinea (abstract only), Pseudoeupolyphaga spelunca (male sentence "Eyes and ocelli well-developed." sat in a truncated part; not filed) and P. vestis.
- Already filed elsewhere: Nocticola cordiformis and appendiculata (desk-d297), N. gonzalezi, Zorotypus komatsui and vinsoni.
- Genus-level only: Pinelema and Telemidae (spiders), Amauropelma (spider, d314).

Angle result: fossil compound-eye numbers (trilobite lens counts, radiodont and fuxianhuiid ommatidia) are in closed or CC BY-NC-ND papers, repository copies or review sentences; two fossil morphological sentences were filed instead (Ekpagloderma, Prolucanus). Termite searches returned no usable species text. Productive route: Pensoft taxon browse pages (Blattodea listing worked) and Crossref list queries to get article IDs, then the article XML.

Weak spots for the auditor:
- Telegraphic sentences without a finite verb in nearly all records (accepted precedent); Cnipsomorpha yunnanensis ("are") and the Ekpagloderma and Nocticola semicolon sentences carry more than the eye clause.
- Nocticola baiguensis quote includes the bold "Head:" label, as desk-d297 did for its sister species; the sentence came back in two consecutive pieces on two passes.
- Ekpagloderma gracilentum: one sentence with commas and a semicolon (second pass confirmed no full stop before "ocelli absent"); eye length 0.41 mm is in the quote but the value is filed as eye_type. Licence page metadata CC BY 3.0 versus Crossref CC BY 4.0. The Introduction and Results disagree on the family (Bellodermatidae versus Semenoviolidae); the Results heading is used.
- Rhagovelia tantilloides: the tool returned the holotype locality and date as placeholders, so conditions say the line was not read. Please check the Material examined on the page.
- Calogalesus sinicus and Monelata truncata: Crossref author order differs from the printed byline (record follows the byline); the Calogalesus citation line returned by the tool reads "Xu X-f" (probably a printed typo; byline gives Zai-fu Xu). Calogalesus paratype counts differ between Material examined (16 and 37) and Materials and methods (13 and 34); both given.
- Pseudoeupolyphaga: holotype collector and Table 1 collector/date discrepancies are quoted in conditions; the female "ocelli degraded to two spots" record covers ocelli only (compound eyes of the female are not described); eye field says ocelli.
- Cranopygia: five records with the identical sentence from one paper; the auditor may sample. Collector names are not printed for three holotypes.
- Pseudoparamenexenus: five unlabelled Hainan females listed under the P. yangi figure caption are not attributed.
- Class is blank in all records except Mesodiplatys, Rhagovelia, Steinovelia and Diplatys (class Insecta printed in the title). Journal page ranges use a hyphen for the printed en dash, as earlier desks did.
- Prolucanus: the holotype sex is "probably female" per the tool; preservation as compression not stated.

Questions: none.
