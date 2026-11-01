# audit-405: desk-d309, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d309 files present untracked in the worktree (docs/tracks/progress/desk-d309.md and docs/views/evidence/desk-d309.jsonl, 20 lines; neither committed here, neither edited). This audit judges file lines 1 to 7 only; lines 8 to 14 and 15 to 20 go to two other auditors. HEAD equals origin/main (d87091c8f). `python3 -I tools/senses/check.py | grep d309`: "docs/views/evidence/desk-d309.jsonl: 20 records, 0 problems". Quote lengths (`len(q.split())`), lines 1 to 7: 22, 10, 14, 15, 15, 21, 17, all within 40.

The progress note's numbered list does not follow file order (it puts Abyssomysis cornuta at 6 and Cottus at 7; in the file Abyssomysis is line 17, Cottus line 6 and Laspionchis line 7). Line numbers below are file lines.

Sources opened (WebFetch; every URL seen in a WebSearch result or reached from a page so seen): zookeys.pensoft.net/article_preview.php?id=19899 (two passes), id=76412 (three passes, incl. offset 100000), id=36698 (one pass); europeanjournaloftaxonomy.eu/index.php/ejt/article/view/2577/11717 (galley frame only), .../article/download/2577/11717 (three passes; the text returned ends inside the Amblyops arianii description, so the paper's Discussion was not reached), .../article/view/1897 and .../article/download/1897/7539 (one pass each). Crossref single-DOI lookups api.crossref.org/v1/works/ for all five DOIs, each read on the first call. PMC, Plazi, GBIF, Zenodo, openpolar, bora.uib.no and Wikipedia results were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 10 WebSearches.

## Bibliographic and licence

- Lines 1-2 (Tandberg, Vader 2018). Byline "Anne Helene S. Tandberg, Wim Vader" (the page doubles "Vader Vader", a page artefact); Crossref same order. Title verbatim (genus names italic on the page). ZooKeys 731: 103-134, 2018, no issue. Page prints the CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 3 (Wittmann, Chevaldonné 2021). Byline and Crossref identical in order; title identical (Crossref shows a stray quotation mark after "Pseudomma"; the record's title carries none, right). ZooKeys 1079: 145-227, 2021. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Lines 4-5 (Wittmann 2024). Sole author; title as filed (Crossref piece and search-result title agree); EJT 940: 1-180, issued 20 June 2024. PDF prints "This work is licensed under a Creative Commons Attribution License (CC BY 4.0)."; Crossref CC BY 4.0, content-version unspecified. Accepted.
- Line 6 (Sideleva, Kesminas, Zhidkov 2022). Byline and Crossref identical in order; title identical; PDF "European Journal of Taxonomy 834: 38–57 (2022)". PDF prints the CC BY 4.0 sentence; Crossref CC BY 4.0 unspecified. Accepted.
- Line 7 (Dayrat et al. 2019). Byline and Crossref identical in order; title identical; ZooKeys 877: 31-80, 2019. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. **Fault:** the page's citation line prints "Dayrat B, Goulding TC, Khalil M, Comendador J, Ngô Xuân Q, Tan SK, Tan SH (2019)"; the record writes the fifth author "Quảng N X", which turns the given name into the surname. The order is right, the name is not as printed. Counted (bibliographic).

source.access "open" right throughout.

## Names and higher taxa

- Amphilochus (lines 1-2): headings printed "Order AMPHIPODA Latreille, 1816", "Suborder GAMMARIDEA", "Family AMPHILOCHIDAE Boeck, 1871"; no class. Filled right. A. anoculus is described here. A. hamatus is "Amphilochus hamatus (Stephensen, 1925), comb. n." on the page; a GBIF search-result title still carries Amphilochopsis hamatus (not opened); WoRMS cannot be opened under the rules. Not counted; the owner may want to confirm WoRMS status before merge.
- Pseudomma kryotroglodytum (line 3): "Order Mysida Boas, 1883", "Family Mysidae Haworth, 1825", "Subfamily Erythropinae"; no class. Right.
- Amblyops arianii, Thalassomysis tattersalli (lines 4-5): "Order Mysida Boas, 1883", "Family Mysidae Haworth, 1825", "Subfamily Erythropinae", "Tribus Amblyopsini"; no class printed (tool summary). Right.
- Cottus cyclophthalmus (line 6): "Class Osteichthyes Huxley, 1880", "Order Scorpaeniformes Garman, 1899", "Family Cottidae Bonaparte, 1831" printed. Right. Name in use (GBIF and Plazi result titles "Cottus cyclophthalmus Sideleva, Kesminas & Zhidkov, 2022").
- Laspionchis boucheti (line 7): "Family Onchidiidae Rafinesque, 1815" printed; Gastropoda and Pulmonata only in the title, disclosed in the note; acceptable under audit-404's precedent. ZooBank act and Plazi treatment in results under the same name.

## eye_type and shape statements

Main files shape and size statements under eye_type (e.g. Gammarus sezgini "kidney-shaped", Phoxirostus longicarpus "reniform, bulging laterally", Palaumysis jetama "large eye, cornea globular and well pigmented", Uropterygius hades "eyes small, anteriorly placed"). Line 6's "eye round and protruding, near the front of the head" matches that use. Answer to the unit's question 1 for line 6: yes. Question 2: a telegraphic Diagnosis or Description sentence printed as a whole sentence stands (audit-395 precedent); lines 4 and 5 are such sentences, not fragments cut from longer ones. Question 3: no %SL key; such values stay in conditions (main has "eye diameter 4.6-6.7% of head length" inside an eye_type value for Triplophysa xiuwenensis, but that is the quoted value there).

## Repeats

`git grep -il` on origin/main over the whole docs/ tree for anoculus, Amphilochus, hamatus, zookeys.731.19899, kryotroglodytum, zookeys.1079.76412, arianii, tattersalli, ejt.2024.940, cyclophthalm, cyclophtalm, ejt.2022.834, Laspionchis, boucheti, zookeys.877.36698. Hits: "hamatus" only for Helicolestes hamatus (sweep-85) and in gaps files (not Amphilochus); kryotroglodytum only in desk-d303.md as a dropped candidate ("Arrived in pieces or over the tool limit"). No DOI anywhere. Every origin/research/desk-d*, audit-* and sweep-* branch not merged into main (d309 excluded), diffed against main under docs/: one hit, desk-d303's same drop line. No repeats.

## Per line

### Line 1, Amphilochus anoculus, eyes absent

Remarks: "This species is easily recognized because it lacks eyes and has an anterodistal tooth on the propodi of pereopods 1 and 2." **Quote MATCH**, 22 words, one piece. Head "Eyes absent."; Table 2 "Eyes absent"; Abstract "by the absence of eyes"; Etymology "refers to the absence of eyes". Holotype "IceAGE ZMH K-47225, female 3 mm (slide)", station 1057 2504.7 m; paratypes BioIce 2367 male 3 mm and female 3 mm, Mareano R1225-RP112 female 4 mm, IceAGE 1006 male 3 mm, wet sample "TSZCr 14338 (8 specimens)" at 819 m, UNIS station off Spitsbergen. The Introduction's "seemingly no eyes" describes how the specimens were first sorted, before the description; not contrasting. Value restates the quote. Conditions right.

**Line 1 MATCH.**

### Line 2, Amphilochus hamatus, eyes not evident, ill-defined eye-patch

Description, Head: "Eyes not evident, but an ill-defined eye-patch can be seen." **Quote MATCH**, 10 words. Drawn specimens IINH37894, IINH37898, IINH37900, IINH37903 (BioIce 2077, 2236, 2318, 2367), sexes not stated, "Type material not examined." Table 2 "ill defined, bean-shaped or oval". 

Fault: **contrasting wording omitted.** The Remarks under A. anoculus say of A. manudens and A. hamatus "but unlike *Amphilochus anoculus* sp. n., they both have eyes." That sentence states eyes present for this species, against this Description's "Eyes not evident"; the conditions carry Table 2 but not this. One record error, fixable.

**Line 2 FIXABLE.**

### Line 3, Pseudomma kryotroglodytum, red cornea-like eyeplate portions

Description of the holotype, Eyes: "Brilliant red cornea-like portions of eyeplate feign functional eyes in living specimens (Fig. 2B)." **Quote MATCH**, 14 words, whole sentence with a finite verb. Holotype spent female, BL 26.8 mm, NHMW 27296, dive #612, 10 m, 15 Jan 2016; paratype subadult female, BL 21.5 mm, NHMW 27297, dive #611, 13 Jan 2016 (the conditions do not give the paratype's dive or date, not material); "Covers females only." Colour section "Lateral portions of eyeplate, foregut and part of mouthparts brilliant red, hepatic caeca yellow-green." Next sentence (no functional or vestigial ommatidia after bleaching) carried in conditions, right.

Fault: **value says more than the quote.** The value opens "eyes reduced to an eyeplate", which is the genus Diagnosis ("Pseudommini with eyes reduced to single eyeplate without visual elements."), genus-level wording the conditions themselves say was "not used for the value". The quote gives only the red cornea-like portions that feign functional eyes. Also the species Diagnosis states the species has no visual elements (tool summary; the sentence is over the tool's limit); the conditions give the Diagnosis's sulci wording but not that. One record error, fixable.

**Line 3 FIXABLE.**

### Line 4, Amblyops arianii, eye rudiments without visual elements

Diagnosis: "Eye rudiments without visual elements, subovate, converging at mesial third; all around hispid by scales." **Quote MATCH**, 15 words; "Based on adult and subadult females." Telegraphic but whole and printed as one sentence; accepted (audit-395). Holotype description sentences ("Eye rudiments dorsoventrally compressed by a factor of 1.7–1.8.", ocular papilla, scales) as the conditions say.

Fault: **specimen counts and depths wrong.** The conditions say "with 6 further paratype lots ... from the Drake Passage, Weddell Abyssal Plain and South Sandwich Trench (3683 to 4698 m)". The page lists 6 paratypes in 5 lots (ZMH 64655, 64654, 64657, 64658, 64656): one subadult female from the holotype station (about 2893 m), one damaged immature and one damaged juvenile (ANDEEP I 042-2, Drake Passage, 3683-3680 m), one immature each from ANDEEP III 059-5 (4655 m) and 110-8 (4698-4696 m), one damaged adult female from ANDEEP II 139-6, South Sandwich Trench (3941.7-3926.8 m) (tool summary for the list). So 5 lots not 6, and one paratype lies outside the stated depth range. Holotype depth printed 2893.6-2893.2 m (tool summary), filed as 2894 m. One record error, fixable.

**Line 4 FIXABLE.**

### Line 5, Thalassomysis tattersalli, ommatidia without rhabdom

First description of (non-adult) males: "Ommatidia without rhabdom, nonetheless forming a compact laterally positioned cornea (Fig. 10D) delimited from eyestalk." **Quote MATCH**, 15 words; telegraphic, accepted. Material: "1 ♂ imm. (BL = 13.4 mm, on slides)", ANDEEP-II 135-4, 4677.6-4678.2 m; "1 ♀ imm. (BL = 10.3 mm)", ANDEEP-III 059-5; "fragment of one subad. ♂ (posterior ⅔ of body, estimated BL ≈ 14 mm, on slides)", ANDEEP-III 088-8.

Faults: **variation and contrasting wording omitted.** The species Diagnosis says "Eye structure and size of papilla varying with body size (see Notes below and 'Discussion')." and the Notes on the immature female describe a different eye: "Cornea compact, well delimited from eyestalk, with ommatidia reaching surface.", "Cornea brown, well contrasting from opaque eyestalk even after 18 years of preservation in ethanol.", and pigmented cornea with ommatidia reaching the surface together with a ganglion mass "suggesting some visual abilities (see 'Discussion')". The conditions note the female only as "also noted". The subadult male is a posterior fragment, so the eye observation rests on the one immature male; the `eye` field's "non-adult male" should say so. One record error, fixable.

**Line 5 FIXABLE.**

### Line 6, Cottus cyclophthalmus, eye round and protruding

Description: "Eye round and protruding, near to front of head, average eye diameter 7.3% SL (7.4% SL or 22.4% HL in holotype)." **Quote MATCH**, 21 words. Diagnosis "round, protruding (tubular) eyes near front of head"; Etymology "round and convex shape of eyes"; comparison "round bulging eyes"; C. microstomus "eye oval, not bulging". Holotype "♂, SL 83.3 mm", Krasnaya River near Tokarevka, 31 Aug. 2019, ZIN 56687; paratypes "8 specimens, SL 81.0-48.7 mm ... ZIN 56688". Table 2 Krasnaya (n = 9) "7.3 ± 0.3 6.9–7.9", which is the sentence's mean.

Faults: **non-type material omitted and the sample misdescribed.** The page lists non-type specimens: 26 from the Žeimena River (ZIN 56689), 24 from the Neris River (ZIN 56690), 22 from the Siesartis River (ZIN 56691), all Nemunas/Neman basin, and 16 from the Šerkšnė River, Venta basin (ZIN 56692), and Table 2 gives eye horizontal diameter for each river (Neris 7.2 ± 0.4, 6.5–8.0; Žeimena 7.6 ± 0.3, 7.1–8.2; Siesartis 6.9 ± 0.3, 6.5–7.3; Šerkšnė 7.6 ± 0.3, 7.1–8.2). The conditions say "The sample is one river population", which is wrong for the paper, and the Abstract places the species in the Neman/Nemunas and Venta systems. The `eye` field's "adult males and females of the type series" is unsupported: only the holotype's sex is printed. One record error, fixable.

**Line 6 FIXABLE.**

### Line 7, Laspionchis boucheti, three dorsal eyes on the central papilla

Color and morphology of live animals: "A central, much larger papilla, which also bears three dorsal eyes, is entirely retractable within the notum." **Quote MATCH**, 17 words. Preceding "Some papillae bear dorsal eyes at their tip (most papillae bear three eyes)."; following "The number of papillae with dorsal eyes is variable (between 8 and 12, on average)". Genus Diagnosis "Retractable, central papilla (usually with four dorsal eyes) present, often raised above dorsal surface." carried. Holotype 30/20 mm, Darwin, 17 Aug. 2012, NTM P.57614; 23 specimens from Northern Territory and Queensland, Brunei, Sumatra, Peninsular Malaysia, Singapore, Bohol and Vietnam. External morphology "The large, central, retractable papilla at the center of the notum can usually only be seen in live animals." (not contrasting). Value per papilla, no per-side or body total; right. Science right.

Fault: the author name (see Bibliographic). One record error, fixable.

**Line 7 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Amphilochus anoculus, eyes absent | MATCH | | Remarks sentence whole; types right |
| 2 | Amphilochus hamatus, eyes not evident | FIXABLE | conditions | Remarks "they both have eyes" omitted |
| 3 | Pseudomma kryotroglodytum, red cornea-like portions | FIXABLE | value, conditions | "eyes reduced to an eyeplate" is genus wording beyond the quote; species "no visual elements" missing |
| 4 | Amblyops arianii, eye rudiments | FIXABLE | conditions | 6 paratypes in 5 lots, not 6 lots; depth range omits the holotype-station paratype |
| 5 | Thalassomysis tattersalli, ommatidia without rhabdom | FIXABLE | eye, conditions | immature female's ommatidia reaching surface and Diagnosis variation with body size omitted |
| 6 | Cottus cyclophthalmus, eye round and protruding | FIXABLE | eye, conditions | 88 non-type fish from four rivers with eye data omitted; "one river population" wrong; sexes unsupported |
| 7 | Laspionchis boucheti, three dorsal eyes per central papilla | FIXABLE | source.authors, note | fifth author printed "Ngô Xuân Q", filed "Quảng N X" |

Errors: 6 of 7 records (86%); 6 fixable (lines 2 to 7), 0 held out, 0 unfixable; no line to drop. The rate is above 5%; by the drop-the-errors route line 1 merges as filed and lines 2 to 7 merge with the replacements below, or are dropped if they are not applied. Pooled with the other two auditors' shares of desk-d309: to be added by the owner from audits of lines 8-14 and 15-20. Verdict for lines 1-7: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count` on the JSON-escaped text).

Line 2:
- `conditions`: "The paper does not say whether eye visibility varies between specimens." -> "The paper does not say whether eye visibility varies between specimens. The Remarks under A. anoculus say of A. manudens and A. hamatus 'but unlike Amphilochus anoculus sp. n., they both have eyes.', which differs from this Description's 'Eyes not evident'."

Line 3:
- `value`: "eyes reduced to an eyeplate; the cornea-like lateral portions are brilliant red in living specimens and feign functional eyes" -> "brilliant red cornea-like portions of the eyeplate feign functional eyes in living specimens"
- `conditions`: "the Diagnosis calls the cornea-like lateral portions separated by sulci from the main part of the eyeplate," -> "the species Diagnosis calls the cornea-like lateral portions separated by sulci from the main part of the eyeplate and says the species has no visual elements,"

Line 4:
- `conditions`: "Holotype adult female (body length 25.8 mm, ZMH 64653, ANDEEP-I station 046-7, Drake Passage, 2894 m) with 6 further paratype lots of females, immatures and juveniles from the Drake Passage, Weddell Abyssal Plain and South Sandwich Trench (3683 to 4698 m); males unknown." -> "Holotype adult female (body length 25.8 mm, ZMH 64653, ANDEEP-I station 046-7, Drake Passage, about 2893 m) with 6 paratypes in 5 lots: a subadult female from the holotype station, a damaged immature and a damaged juvenile (ANDEEP-I 042-2, Drake Passage, about 3680 m), one immature each from ANDEEP-III 059-5 and 110-8 (Weddell Abyssal Plain, 4655 m and about 4697 m) and a damaged adult female (ANDEEP-II 139-6, South Sandwich Trench, about 3927 to 3942 m); males unknown."

Line 5:
- `eye`: "cornea and ommatidia, non-adult male" -> "cornea and ommatidia, one immature male (13.4 mm; the subadult male is a posterior body fragment)"
- `conditions`: "The paper's wording does not say whether adults keep the rhabdom-free ommatidia." -> "The paper's wording does not say whether adults keep the rhabdom-free ommatidia. The species Diagnosis says 'Eye structure and size of papilla varying with body size', and the Notes on the immature female (10.3 mm) describe a different eye: 'Cornea compact, well delimited from eyestalk, with ommatidia reaching surface.', the cornea brown, and a pigmented cornea with ommatidia reaching the surface together with a ganglion mass in the eyestalk, 'suggesting some visual abilities'."

Line 6:
- `eye`: "eye, adult males and females of the type series (9 fish)" -> "eye, type series (holotype male and 8 paratypes of unstated sex; 9 fish)"
- `conditions`: "The sample is one river population; no live eye observations." -> "Non-type material is also listed: 26 fish from the Žeimena River, 24 from the Neris River and 22 from the Siesartis River (Nemunas/Neman basin) and 16 from the Šerkšnė River (Venta basin); Table 2 gives horizontal eye diameter per river with means 6.9 to 7.6 % SL and ranges 6.5 to 8.2 % SL. The Description sentence's mean 7.3 % SL is the Krasnaya type series (n = 9). No live eye observations."

Line 7:
- `source.authors`: "Comendador J, Quảng N X, Tan S K" -> "Comendador J, Ngô Xuân Q, Tan S K"
- `note`: "the sixth-from-last name is written 'Quảng N X' in the initials style" -> "the fifth name is written 'Ngô Xuân Q' as the page's citation line prints it"
