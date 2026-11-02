# desk-d322: eye states and spider eye sizes in non-insect arthropods, 10 records

Branch research/desk-d322 from origin/main. 17 WebSearches; WebFetch only on URLs returned by searches (Pensoft article XML, article_preview). Every species and DOI grepped over docs/ on main before filing (no hits for the 10 records). `python3 -I tools/senses/check.py | grep 'd322\.'`: 10 records, 0 problems.

Filed (docs/views/evidence/desk-d322.jsonl):
1. Australobius tracheoperspicuus, no ocelli (eyes_count 0), ZooKeys 795: 83-91 (cave centipede).
2. Scolopendra spinosissima, four ocelli per side (eyes_count 4), lectotype redescription, ZooKeys 1215: 311-334.
3-4. Lithobius hualongensis (1 + 3, 3, 1) and L. sui (1 + 4, 4, 1), ocelli per side as printed formulas, ZooKeys 892: 77-92.
5-7. Pholcus chaoyang, AME 0.09 and PME 0.14 (male holotype) and PME 0.12 (female paratype), sensory_anatomy, ZooKeys 1232: 285-310.
8-9. Jingneta qishan PME 0.04 and Leptonetela jingde PME 0.07 (male holotypes), sensory_anatomy, ZooKeys 1218: 99-119.
10. Mysidella hoshinoi, eye and cornea (cornea nearly half of the eye), sensory_anatomy anatomical_presence, ZooKeys 620: 21-32.

Dropped:
- On main: Tyrannochthonius pandus / Lagynochthonius laoxueyanensis (ZooKeys 1097, clauses in long sentences, earlier desks), Ochyrocera ritxoco / ritxoo, Nereis tricirrata, Oroperipatus tiputini, Pasipha ferrariaphila, Iandumoema smeagol, Otilioleptes marcelae, Sarax timorensis, Odontostreptus fadriquei, Hyleoglomeris alba, Cylindroiulus villumi, Gyorome guttatum.
- Fragment or clause only: Bogidiella pingxiangensis ("Head. (Figure 3A): eyes absent." is a figure-labelled head paragraph; earlier desks also left it), Neobisium adjaricum (clauses), Mesomexovis caxcan (long clause chain), Pholcus jiuzhai / pingwu (fragments), Dimorphostylis pilocorpus (52- and 164-word sentences).
- Text unreadable or without an eye sentence: Niphargus elburzensis / zagrosensis (XML cut), Mecistocephalus chuensis / huangi (XML cut before Description), Phalangodus andresi (excerpt only), Polydesmidae of Vietnam (no eye sentence).
- Not opened: prolekare.cz copy of Otilioleptes (URL too long; already on main), Zootaxa and Mapress pages.

Weak spots for the auditor:
- Crossref was not consulted for any DOI; licence rests on the CC BY 4.0 sentence printed in the article XML (fetched summaries), and journal/volume/pages and author order come from the same tool readings. Initials follow the main-file style (Surname Initials) and are my rendering of the printed given names.
- Class is blank on all records because none of the pages prints a class line.
- WebFetch summaries, not raw text, supplied the quotes; the Lithobius sentences were read in two passes (first part, then remainder) that agree with each other. Re-check the Lithobius sui "(Fig. 2B)," position and the hualongensis sentence against the page.
- Australobius: the page gives no Male heading; the Description is species-level and the holotype is a male.
- Spider eye lines print bare numbers; units rest on the Methods sentence, and the Anhui paper does not define "Eye sizes". Value is the printed number, not a recomputed diameter. The ALE/PLE/PME lists imply six eyes but no count is filed.
- Lithobius values are formulas as printed; sums (8 and 10) appear only in notes.
