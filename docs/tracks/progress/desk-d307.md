# desk-d307: eye states of a pygmy grasshopper, a pygmy mole cricket, a copepod, two beetles and two amber mayflies in CC BY papers, 7 records

Branch research/desk-d307 from origin/main (merged to b1ba77167 after d306). About 52 WebSearches; WebFetch only on URLs returned by searches or the Pensoft download/xml and article_preview pages of those papers; Crossref single-DOI lookups through WebFetch for every DOI filed (api.crossref.org/v1/works/<doi>, one at a time after a rate limit); Crossref list queries (prefix 10.3897 title words eye/eyes/reduced/blind/ocelli) used to find leads. `python3 -I tools/senses/check.py | grep d307`: 7 records, 0 problems. Trait eye_type throughout; no new trait key.

Repeat check: every species and DOI grepped over origin/main docs/ and over the evidence files of all origin/research/desk-* branches (dumped once to a scratch file) before filing; no hits.

Angle result: Hymenoptera (Braconidae, Ichneumonidae, Chalcidoidea, Encyrtidae), Diptera, Hemiptera (Aphididae), Thysanoptera, Ostracoda and Copepoda description pages gave only measurement lines (ocular-ocellar line, postocellar line) or clauses inside long sentences. The yield came from Orthoptera (Tetrigidae, Tridactylidae), a harpacticoid copepod, Coleoptera (Hydrophilidae, Chrysomelidae) and Burmese-amber mayflies.

Filed (docs/views/evidence/desk-d307.jsonl):
1. Electrotettix attenboroughi (Tetrigidae), compound eyes large, globose, projecting dorsally; female holotype in Miocene Dominican amber; ZooKeys 429.
2. Xya xishangbanna (Tridactylidae), compound eyes dark brown to black, rounded in front; male holotype; ZooKeys 947.
3. Gyorome guttatum (Tisbidae), large paired frontal modified eyes (baculiform ocellus, globular organ, semi-parabolic plate); Abstract sentence rebuilt from three consecutive pieces; ZooKeys 1191.
4. Agasicles hygrophila (Chrysomelidae), apposition compound eyes with eucones and open rhabdom; Abstract sentence; ZooKeys 1177.
5. Elocomosta lilizheni (Hydrophilidae), eyes extremely reduced, dorsally divided by about 20 times the dorsal width of one eye; Diagnosis; ZooKeys 607.
6-7. Burmella paucivenosa (male imago: eyes large, medially contiguous; quote cut at the semicolon with a marked "…") and B. clypeata (female imago: eyes large, widely separated medially); Burmese amber; ZooKeys 1036.

Weak spots for the auditor:
- WebFetch returns at most about 125 characters per quoted piece, so every sentence is rebuilt from consecutive pieces or taken whole; Gyorome (3 pieces), Agasicles (2 pieces) and Burmella (3 pieces for the cut quote) are the stitched ones.
- Author bylines: Heads (page "Sam W. Heads, M. Jared Thomas, Yinan Wang", Crossref "Sam Heads, M. Thomas, Yinan Wang"); Elocomosta (page "Lin R, Jia F, Fikáček M", Crossref lists Jia first, Lin second); page followed in both.
- Class left empty where the Pensoft classification block prints no class (Electrotettix, Xya, Gyorome, Agasicles, Elocomosta); Burmella has Class Insecta in the paper's hierarchy line.
- Agasicles: desk-d279 says the eye paper is "on main (harvest sheets, d270)", but no evidence, sheet or audit record carries a value for the species (only searched/ screened-works lists and audit notes); filed on that basis. Ommatidia counts (341.00 +/- 3.35 male, 345.22 +/- 4.48 female) not filed because the page does not say per eye and the Discussion sentence says "few ommatidia".
- Xya xishangbanna's "2 times broader than longer" is printed that way; value copies it.
- Electrotettix, Xya and Burmella clypeata/paucivenosa are fossil (the first and last two) or eye-shape/colour statements, a thin reading of eye_type.

Dropped:
- Fragment or run-on sentences: Apharinodes baixiensis (BDJ, "about 20 facets" inside a long sentence), Araneibatrus gracilipes (ZooKeys 69; facet sentence continues with labrum, mandibles and labium), Formosatettix leigongshanensis and F. wulongensis (ZooKeys 936; eye sentences run on), Rusmithia gorochovi ("Eyes globose." two words), Xya yunnanensis ("Compound eyes grayish black." and "Three white ocelli." too thin or a noun phrase), Qingryllus jiguanshanensis (lowercase clause), Astreptolabis laevis (only phrases), Archaeocercoides puchkovi and Rovnopositor voblenkoi (fragments), Apterygothrips flavescens (semicolon clause), Witteia dentilabrum (sentence over the tool limit), Trichopsenius huaxiensis (over the limit).
- No eye sentence: Ostracoda of northern China (ZooKeys 294 and the Yu et al. paper), Clausidium rodriguesi, Tigriopus iranicus, Campoletis deserticola, Alexeter beijingensis, Campoplex bazariae, Trieces etuokensis (measurement lines only), Aphidura species, Termitotrox venus (no "eye" in text).
- Already taken: Ptomaphaginus troglodytes (d282).
- Licence: Pristimantis sira (Evolutionary Systematics 5; the page prints CC0 while the XML licence-type says attribution), held out.
- Access: zookeys 55693 and 47983 download/xml (frogs) returned a permission refusal and were not retried; Temnothorax tuberum-group SEM eye paper (Taxonomy 6(2): 35) only found as a preprint; the arphahub Pseudimares paper (robots_disallowed); Zootaxa/Mapress, Plazi, biostor pages not used.
- Frogs: Megophrys anlongensis (ZooKeys 986) gives eye diameter only in Table 1 (the male summary row does not match the individual rows); Pristimantis sira ED only in Table 1. No prose mm sentence found, so no eye_diameter_mm record.
- Snakes and lizards (Typhlopidae, Leptotyphlopidae, Anomalepididae, Dibamidae, Amphisbaenia): searches returned Zootaxa, biostor, Plazi, Taprobanica and Australian Museum PDFs; the Indotyphlops Qinghai-Xizang paper (ZooKeys 1292) was found by Crossref title but its page URL did not come back from a search.
- Review-sourced: A review of sexual dimorphism of eye size in Colubroidea snakes (Vertebrate Zoology 68).
- Not a state: A butterfly with olive green eyes (ZooKeys 305) is eye colour, not opened.

Questions: Do eye-shape or eye-colour statements (globose, dark brown to black, rounded in front) count as eye_type states? Records 1, 2, 6 and 7 depend on the answer.
