# audit-437: desk-d325 lines 6 to 9 (4 evidence records; lines 1 to 5 audited separately)

Audited 1 November 2026 from the desk-d325 files copied untracked into the worktree (evidence file, 9 lines, and the progress note; neither is committed here). Scope: 1-based file lines 6 to 9, all from one paper (Yohe, Hoffmann, Curtis 2018, 10.3389/fnana.2018.00032). `python3 -I tools/senses/check.py docs/views/evidence/desk-d325.jsonl`: 9 records, 0 problems. Quote lengths (whitespace words as check.py counts), lines 6 to 9: 21, 29, 29, 29. 6 WebSearch and 12 WebFetch calls used.

Sources opened (all URLs from my WebSearch results or the single-DOI Crossref API): www.frontiersin.org/journals/neuroanatomy/articles/10.3389/fnana.2018.00032/pdf (seven passes, no refusal); api.crossref.org/works/10.3389/fnana.2018.00032; mammaldiversity.org/taxon/1004888, 1004884, 1004885; en.wikipedia.org/wiki/Cuban_fruit-eating_bat; one plazi treatment page (redirect only, nothing read). PMC, par.nsf.gov and peeref results surfaced and were not opened. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page opened. WebFetch returns pieces of about 125 characters and paraphrases longer passages; sentences below were reassembled from verbatim pieces, and points marked "(tool paraphrase)" were not returned verbatim. No paper text committed beyond single sentences and short fragments.

## Repeats of main

grep of the whole docs/ tree (evidence, audit/ALL, audit/corrected, sheets, searched, wanted, gaps, recheck, notes) for Brachyphylla, Erophylla, Phyllonycteris, "vomeronasal", "Yohe" and fnana.2018.00032: no hit outside desk-d325 for the three Brachyphyllini genera, the DOI or the author. Artibeus jamaicensis is on main only for vision and diel traits (oa-1 fovea, acuity_cpd, eye_axial_length_mm, diel; sheets/bat Gessinger 2021 echolocation). Vomeronasal hits on main are caecilian and squamate sense_chemical records. No repeat, no contradiction.

## Citation and licence

- Printed (PDF): Laurel R. Yohe, Simone Hoffmann, Abigail Curtis, in that order; title "Vomeronasal and Olfactory Structures in Bats Revealed by DiceCT Clarify Genetic Evidence of Function" (verbatim); Frontiers in Neuroanatomy volume 12, article 32; published 08 May 2018; DOI 10.3389/fnana.2018.00032. Crossref (single-DOI lookup) gives the same three authors in the same order, volume 12, article-number 32, issued 2018-05-08. Record's "Yohe LR, Hoffmann S, Curtis A", 2018, "Frontiers in Neuroanatomy 12: 32" and DOI all match.
- Licence: the PDF states the article is open access under the Creative Commons Attribution License (CC BY) (tool paraphrase; "Copyright © 2018 Yohe, Hoffmann and Curtis" quoted). Crossref licence entry: creativecommons.org/licenses/by/4.0/, content-version "unspecified", start 2018-05-08. Crossref "unspecified" plus a page-printed CC BY licence is accepted under rules.md. No conflict.

## Names (Mammal Diversity Database pages, opened)

- Artibeus jamaicensis: docs/views/gaps/gbif-names.tsv row EXACT, ACCEPTED (usage key 2433272). OK.
- Phyllonycteris poeyi: MDD taxon 1004888 lists it as a valid species, authority J. Gundlach in W. C. H. Peters 1861, Phyllostomidae, Glossophaginae, tribe Brachyphyllini, range Cuba and Hispaniola (Dominican Republic listed). Synonyms listed are Phyllonycteris obtusa Miller 1929 and the poeyi/obtusa trinomials. OK.
- Erophylla bombifrons: MDD taxon 1004885 lists it as a species, authority G. S. Miller 1899 (as Phyllonycteris bombifrons), Brachyphyllini, range Hispaniola and Puerto Rico (Dominican Republic listed); Erophylla sezekorni bombifrons appears only as a synonym combination. OK.
- Brachyphylla pumila: MDD taxon 1004884 (Brachyphylla nana G. S. Miller 1902, valid species, range includes Hispaniola, Dominican Republic and Haiti) lists "Brachyphylla pumila G. S. Miller, 1918", type locality Haiti, as a synonym, and Brachyphylla cavernarum pumila Hall 1981 as a name combination. Wikipedia's Cuban fruit-eating bat page also lists pumila (spelled "pumilia") as a synonym of B. nana. None of the three Brachyphyllini names is in gbif-names.tsv. The record is filed under a synonym. Error (line 7).

## Paper facts checked (all lines)

- Specimens (Methods, tool paraphrase plus short quotes): one specimen of each of A. jamaicensis (control), E. bombifrons, P. poeyi and B. pumila, collected on a February 2015 expedition to the Dominican Republic, fixed in 4% buffered formalin, decapitated and stained about 10 to 15 weeks in 11.25% I2KI, scanned at AMNH on a GE V|tome|x µCT; "imported into Amira 6.0 (FEI Thermo Fisher Scientific) for segmentation." Sex and age not stated; no museum catalogue numbers (MorphoSource media numbers only). The record's `conditions` is accurate.
- Scan extent: "The nasal region of all specimens was scanned." A footnote reads "The head of Phyllonycteris poeyi was not completely scanned." Voxel sizes (Table 1, tool paraphrase): A. jamaicensis 0.0196 mm, E. bombifrons 0.0149 mm, P. poeyi 0.0194 mm, B. pumila 0.0207 mm.
- Family: the text prints "New World Leaf-nosed bats (Phyllostomidae)" and "compared to other members of Phyllostomidae", calls A. jamaicensis "a frugivorous phyllostomid" and the Brachyphyllini "Caribbean nectar-feeding phyllostomids". "Chiroptera" appears only in reference titles. So family Phyllostomidae is printed for all four species; the records leave it blank and their notes say "Family and order not recorded from the sections read". Order blank is right. Listed as a fault below and in the replacement, not counted as a line error on its own (the desk treated family sourcing as optional after audit 435).
- Contrary or stronger wording: Results say only "not detectable" and "at best, rudimentary in Brachyphyllini"; the Abstract says the organ is "rudimentary or absent in species with a disrupted TRPC2 gene". No species in the paper other than A. jamaicensis shows a vomeronasal organ; the paper gives no VNO dimensions for the Brachyphyllini and mentions no vomeronasal duct or cartilage in them (paraseptal cartilages are named only for B. cavernarum, which was not sampled). The next Results sentence ties the result to "Bhatnagar and Meisami's (1998:4I) identification of a possible rudimentary vomeronasal organ" in B. cavernarum (not a contrary result). The Discussion says diceCT can "identify the presence or absence of the vomeronasal organ on a macroscopic level" and that fine detail "can, at least for now, only be obtained through microscopic histological sections"; no sentence names voxel size or single specimens as a detection limit.

## Per line

| line | taxon / value | verdict | evidence |
|---|---|---|---|
| 6 | Artibeus jamaicensis / VNO 1.7 mm long, 0.3 mm tall | OK | Results, Vomeronasal Organ, reassembled from two verbatim pieces: "Based on the surface reconstruction, the vomeronasal organ of A. jamaicensis is 1.7 mm long (anteroposteriorly)" + "and 0.3 mm tall (dorsoventrally)." Whole sentence, 21 words, no figure reference cut, contains both values; the figure is the organ, not the epithelium. Note's extra facts verified verbatim: "The volume of the epithelium is 0.07 mm3and the surface area of the epithelium is 2.1 mm2." and "The greatest length is similar to the length given by Cooper and Bhatnagar (1976) of 1.6 mm." No other A. jamaicensis VNO dimension in the paper (the Discussion says only that the length "is comparable to that of the length obtained from histology"). sensory_anatomy with anatomical_measurement and units mm is right (no existing key for VNO size). Fault not counted: family Phyllostomidae printed. |
| 7 | Brachyphylla pumila / VNO not detectable in the scans | fixable | Quote verified from three verbatim pieces: "The vomeronasal organ was not detectable in the diceCT scans of B. pumila, E. bombifrons, and P. poeyi" + "(Figures 2C–E, 3B–D, and Supplementary Figures S3–S5)," + "indicating that the organ is, at best, rudimentary in Brachyphyllini." The filed quote replaces only the figure parenthesis with "[...]" and keeps the comma; it starts at the sentence start, keeps the "at best, rudimentary" qualifier, 29 words, contains the value. Value says no more than the quote ("not detectable in the scans", not "absent"); the note carries "a null in one scan is not proof of absence" and the conditions carry one specimen. Shared sentence filed once per named species follows main practice (audit 435 lines 5 and 6). Fault: taxon is a synonym (Brachyphylla pumila Miller 1918 is a synonym of Brachyphylla nana Miller 1902 per MDD; see Names). Also family Phyllostomidae printed (not counted). |
| 8 | Erophylla bombifrons / VNO not detectable in the scans | OK | Same sentence and checks as line 7; name accepted (MDD). Fault not counted: family Phyllostomidae printed. Optional: method says "scan of the head"; the paper says the nasal region was scanned. |
| 9 | Phyllonycteris poeyi / VNO not detectable in the scans | fixable | Same sentence and quote checks as line 7; name accepted (MDD). Fault: the record's method reads "diceCT scan of the head, one specimen", but the paper says only the nasal region was scanned and adds in a footnote "The head of Phyllonycteris poeyi was not completely scanned." For a non-detection, a scan limitation of this very specimen is a design qualifier the record must carry; the record omits it and states the opposite. The nasal region (where the VNO lies) was scanned in all specimens, so the finding stands once the method is corrected. Also family Phyllostomidae printed (not counted). |

Evidence errors: 2 of 4 (lines 7 and 9), both fixable. Name faults: 1 (line 7). Omitted design qualifier / misstated method: 1 (line 9). Family left blank where printed: 4 (lines 6 to 9; recorded, not counted). Quote-form faults: 0. Licence faults: 0. Citation faults: 0. Repeats: 0.

Trait and kind: no existing key covers vomeronasal-organ size or presence, so sensory_anatomy is right for all four. For lines 7 to 9, check.py (evidence_scope.py) admits only anatomical_presence or anatomical_measurement under sensory_anatomy, and SENSORY-ANATOMY.md defines anatomical_presence as "A named structure is observed"; a non-detection filed as anatomical_presence with value "not detectable" is the only form the checker accepts and is stated plainly in the value, so it is not counted. Owner question below.

## Replacement

Every old string below occurs exactly once in its line (checked by script). A scratch copy with all edits below applied passes `python3 -I tools/senses/check.py` (9 records, 0 problems).

Line 7 (multi-field raw JSON edit; apply all three):
- `"taxon": "Brachyphylla pumila"` -> `"taxon": "Brachyphylla nana"`
- `"family": ""` -> `"family": "Phyllostomidae"`
- `"note": "One sentence covers all three species;` -> `"note": "The paper names this specimen B. pumila (Hispaniola); the Mammal Diversity Database lists Brachyphylla pumila G. S. Miller, 1918 (type locality Haiti) as a synonym of Brachyphylla nana G. S. Miller, 1902, whose range includes Hispaniola and the Dominican Republic. One sentence covers all three species;`

Line 9 (multi-field raw JSON edit; apply both):
- `"method": "diceCT scan of the head, one specimen"` -> `"method": "diceCT scan of the nasal region, one specimen; the paper notes the head of this specimen was not completely scanned"`
- `"family": ""` -> `"family": "Phyllostomidae"`

Lines 6 and 8 (recommended, not counted):
- `"family": ""` -> `"family": "Phyllostomidae"`

## Optional fixes

- Lines 6 to 9 notes: "Family and order not recorded from the sections read" is now wrong once family is filled; replace with "Family printed in the text (Phyllostomidae); order not printed outside reference titles."
- Lines 7 and 8 method: `"method": "diceCT scan of the head, one specimen"` -> `"method": "diceCT scan of the nasal region, one specimen"` (the paper: "The nasal region of all specimens was scanned").
- Lines 7 to 9 conditions: add the specimen's voxel size from Table 1 (B. pumila 0.0207 mm, E. bombifrons 0.0149 mm, P. poeyi 0.0194 mm) as the resolution of the null.

## Owner questions

- Whether a non-detection under sensory_anatomy should keep evidence_kind anatomical_presence (the only kind the checker allows besides measurement) or whether an explicit absence/null kind is wanted.
- Add Brachyphylla nana, Erophylla bombifrons and Phyllonycteris poeyi to gbif-names.tsv; confirm the Mammal Diversity Database as the animal name authority for desk units (asked before in audits 294 and 339).
