# desk-d314: eye states of a cave spider, a cave earwig, a cave fish, two polychaetes and two amphipods, 7 records

Branch research/desk-d314 from origin/main. About 56 WebSearches (most restricted with allowed_domains to Pensoft, PeerJ and MDPI hosts, which raised the yield) and WebFetch only on URLs returned by searches (Pensoft article XML and preview pages). Traits: eye_type only (key on main).

Repeat check: a taxon and DOI index of origin/main docs/ and of the evidence files of every unmerged origin/research/desk-d* branch was built once; each species was grepped before filing (no hit for the 7). Earlier-desk records seen again and dropped: Nereis tricirrata, Pseudomma kryotroglodytum, Leptanilla voldemort, Cephalodella binoculata, Amphisbaena amethysta, Tachycines ziyunensis, Cylindroiulus villumi (DOI on main), Triplophysa pair of ZooKeys 1281.

Filed (docs/views/evidence/desk-d314.jsonl):
1. Amauropelma matakecil (Ctenidae), eyes vestigial, female holotype, cave in Java, ZooKeys 163: 1-11.
2. Cylindrogaster cavernicola (Diplatyidae), eyes prominent, male holotype, ZooKeys 713: 25-52.
3. Henicorhynchus thaitui (Cyprinidae), eyes smaller than epigean congeners but not vestigial or absent, ZooKeys 965: 85-101.
4. Linopherus beibuwanensis (Amphinomidae), two pairs of reddish eyes, ZooKeys 640: 37-43.
5. Amathillopsis inkenae (Amathillopsidae), eyes visible and white in life, fading in fixation, ZooKeys 1031: 19-39.
6. Orchomenella compressa (Tryphosidae), no trace of eyes in ethanol material, ZooKeys 1184: 261-271.
7. Eunice siphoninsidiator (Eunicidae), eyes dark, lateral to ceratophores, ZooKeys 1230: 25-36.

Dropped candidates:
- Sentence only in the abstract or Description not reached by the tool (it returned abstract and tables only): Sinocyclocheilus zhenningensis (ZooKeys 1238, "normal eyes (5.8-8.2% SL)" is a list item), Triplophysa ziyunensis and T. yaluwang (ZooKeys 1214, "eyes reduced, diameter 2.4-4.9% / 4.6-6.1% of head length" abstract list items), Lucifuga gibarensis (already on main), Indotyphlops gyirongensis (ZooKeys 1292: long semicolon list; d311 also dropped it), Rhombophryne nilevina and Trachischium lalremsangai (no eye text reached or none), Epictia phenops (fragment in a diagnostic list, no new species).
- Clause or fragment only: Princaxelia marianaensis ("eyes absent." ends a longer head sentence), Deltanthura palpus ("eyes dorsolateral, with scattered ommatidia" clause), Xuedytes bellus (eyeless only in genus characteristics and a Diagnosis fragment), Mesomexovis caxcan (scorpion eye sentence split over several clauses, type counts unclear), Protoblepharus apatani (eyelid scale counts only), Ultratenuipalpus parameekeri ("eyes red" inside a colour list), Euplocania spp. (eye colour only), Zorotypus (long sentences, on earlier desks).
- Genus-level: Pinelema/Telemidae eye sentences, Arenivaga, Nipponomyia, Cholevinae of Borneo ("fully developed eyes" for a genus).
- No eye text: Ixodes bat ticks (ZooKeys 1148 area, 108418), Remycampa/Spaniocampa Diplura, Stigmus, Lepidodasys ligni, Nicolea qingdaoensis (abstract only).
- Unreachable: SciELO Neotropical Ichthyology pages (client error), Crossref (client error), Plazi and library catalogue copies not opened.
- Not reached in the allowed budget: bats and golden moles with a measured eye diameter, cephalopod eye measurements (searches returned review/PMC/Frontiers pages), rotifer eyespot sentences, Coleoptera cave-beetle larvae.

Weak spots for the auditor:
- Crossref could not be read; bibliographic data are from the publisher's article XML (author order as the XML byline), licence sentence as printed (CC BY 3.0 for ZooKeys 163, CC BY 4.0 for the rest).
- Records 1, 2, 6 and 7 are telegraphic sentences without a finite verb; records 3 to 5 have finite verbs or are phrase sentences (4: prepositional description).
- Amauropelma quote is 39 words and stops before the "(Figs 2, 3)" reference, marked with an ellipsis; the whole printed sentence is 42 words. The tool reproduced it in consistent pieces on two passes, but WebFetch summarises and does not guarantee character identity of the symbols (ALE>AME=PME>PLE).
- Class is blank in six records (no Class line printed); Cylindrogaster class Insecta comes from the title only. Henicorhynchus: title and heading print the genus in curly single quotation marks; the taxon field omits them.
- Henicorhynchus and Amathillopsis sentences are Remarks/Troglomorphic-paragraph statements rather than Description sentences; both papers also carry Description eye wording (given in conditions).
- Orchomenella compressa: paratype catalogue number equals the holotype's in the paper (noted in conditions).

Questions: none.

## Desk disposition after audit 420
Audit 420 (all 7 lines): 2 fixable errors (line 1 juveniles listed as additional material, not paratypes; line 2 cave-entrance collection and the Etymology's troglobite doubt omitted), fixed; optional fixes applied. 2 errors in 7 (28.6%); none held out or dropped; no repeats on main or unmerged branches.
