# audit-371: desk-d281, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d281 files present untracked in the worktree (docs/tracks/progress/desk-d281.md and docs/views/evidence/desk-d281.jsonl, 8 lines; neither committed here, neither edited). Worktree HEAD and origin/main 16530c42 (Merge d280 after audit 370). `python3 -I tools/senses/check.py | grep 'd281\.'`: "docs/views/evidence/desk-d281.jsonl: 8 records, 0 problems". Quote lengths (`len(q.split())`): 19, 25, 14, 11, 14, 12, 2, 2, all within 40. Non-ASCII in quotes: only "–" in lines 2 and 5, as printed. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/works/ for all five DOIs (10.3897/zookeys.1216.132155, 10.5852/ejt.2020.668, 10.3897/zookeys.537.6073 and 10.3897/subtbiol.54.157228 answered; 10.3897/zookeys.1281.186268 and 10.3897/subtbiol.43.81308 failed with client_error, not retried or worked around); zookeys.pensoft.net/article/132155/download/xml/ (two passes); zookeys.pensoft.net/article_preview.php?id=186268 (two passes); europeanjournaloftaxonomy.eu article/download/985/2347 (one pass); zookeys.pensoft.net/article/6073/download/xml/ (two passes); subtbiol.pensoft.net/article/81308/download/xml/ (two passes); subtbiol.pensoft.net/article/157228/download/xml/ (one pass). Names: Eschmeyer's Catalog (research.calacademy.org fishcatget spid=78559); species.biodiversitydata.se/species/10845522 and /9323892; en.wikipedia.org/wiki/Iandumoema. PMC, GBIF, WoRMS, Plazi, Zenodo, ZooBank, doi.org and the library catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 8 WebSearches.

## Bibliographic and licence

- Line 1 (Wang, He 2024). Crossref: Cheng-Bin Wang, Li He; title identical; ZooKeys 1216, 27-42, no issue; issued 2024-10-18; CC BY 4.0 vor; relation empty. Page citation verbatim: "Wang C-B, He L (2024) First discovery of troglobitic Paederinae (Coleoptera, Staphylinidae) from China. ZooKeys 1216: 27–42."; licence "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Accepted.
- Line 2 (Zhu et al. 2026). Crossref single-DOI fetch failed (client_error); not worked around. Page citation verbatim: "Zhu T-T, Yuan F-H, Zhang R-Y, Zhao Y-H (2026) Two new cave-dwelling species of Triplophysa" | "(Cypriniformes, Nemacheilidae) from Guizhou, China." | "ZooKeys 1281: 123-145."; licence sentence "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Publisher's own free full text with the licence printed: accepted on the page sentence alone. The printed year 2026 is now seen on the page (and Eschmeyer gives 2026), so the note's "not independently checked on the page" is stale (uncounted).
- Line 3 (Enghoff, Reboleira 2020). Crossref: Henrik Enghoff, Ana Sofia Reboleira; EJT, number 668 (deposited as issue, no volume), no pages; issued 2020-06-17; CC BY 4.0 "unspecified"; relation empty. Page: "Enghoff H. & Reboleira A.S. 2020." and "European Journal of Taxonomy 668: 1–11."; licence "This work is licensed under a Creative Commons Attribution License (CC BY 4.0)." Crossref unspecified plus the page-printed sentence: accepted.
- Line 4 (Pinto-da-Rocha et al. 2015). Crossref: Ricardo Pinto-da-Rocha, Rafael Fonseca-Ferreira, Maria Bichuette; title identical; ZooKeys 537, 79-95; issued 2015-11-18; CC BY 4.0 vor; relation empty. Page citation verbatim "Pinto-da-Rocha R, Fonseca-Ferreira R, Bichuette ME (2015)" ... "ZooKeys 537: 79–95."; licence sentence as line 1. Accepted.
- Lines 5, 6 (Cardoso et al. 2022). Crossref fetch failed (client_error); not worked around. Page citation verbatim "Cardoso GM, Bastos-Pereira R, Ferreira RL (2022) Two new troglobitic species of Iansaoniscus from Brazilian caves" (the rest, Subterranean Biology 43: 127–143, tool summary); licence sentence as line 1. Accepted on the page sentence alone.
- Lines 7, 8 (Kováč et al. 2025). Crossref: Ľubomír Kováč, Marko Karaman, Mahmood Mehrafrooz Mayvan; title identical; Subterranean Biology 54, 1-22; issued 2025-11-05; CC BY 4.0 vor, delay 0; relation empty. Page licence sentence as line 1. The page prints the DOI "https://doi.org/10.3897/subtbiol.22.157228" (tool reading); the record's 10.3897/subtbiol.54.157228 is the one Crossref resolves, as the note says. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names

None of the six genera is in docs/views/gaps/gbif-names.tsv. All eight names are new species described in the paper cited (original descriptions), each with a ZooBank URL printed in the paper (ZooBank itself not opened).
- Domene lizeyui: printed ZooBank "https://zoobank.org/0E20A8F4-460E-4C7B-9AAA-06C071B41AF3". Two searches found no checklist entry. Accepted on the original description; unchecked against a checklist. Staphylinidae / Coleoptera as printed in the title.
- Triplophysa zhijinensis: Eschmeyer's Catalog verbatim "Current status: Valid as Triplophysa zhijinensis Zhu, Yuan, Zhang & Zhao 2026.", family "Nemacheilidae.", holotype "GZNUSLS 202410072". Met.
- Odontostreptus fadriquei: paper prints "Order Spirostreptida Brandt, 1833" and "Family Spirostreptidae Brandt, 1833" (the launch prompt's Odontopygidae does not apply) and ZooBank "urn:lsid:zoobank.org:act:767E2E89-4A01-4CA1-B246-09C4792F4333". Swedish Bioatlas lists it as "Accepted Name" under Spirostreptida > Spirostreptidae (source field blank). Met on the original description; MilliBase not seen.
- Iandumoema smeagol: printed ZooBank "http://zoobank.org/AAFD82A9-FA5B-4A71-958A-1150951CB142"; Gonyleptidae / Opiliones as printed; Wikipedia lists I. smeagol under Gonyleptidae, Pachylinae (no checklist cited). Accepted on the original description; checklist unchecked. Main files 12 Gonyleptidae / Opiliones rows.
- Iansaoniscus leilae, I. paulae: printed ZooBank URLs for both; Pudeoniscidae / Isopoda as printed in the title (launch prompt's Philosciidae/Styloniscidae does not apply). Swedish Bioatlas lists genus Iansaoniscus as accepted under Isopoda > Pudeoniscidae with leilae and paulae among its four species (source field blank, tool summary of the list). Met on the original description; WoRMS refused by rule.
- Schaefferia greensladeae, S. montenegrina: printed ZooBank URLs for both; title "(Collembola, Poduromorpha, Hypogastruridae)" (Hypogastruridae / Poduromorpha confirmed; not Tomoceridae / Entomobryomorpha). collembola.org checklist page last updated 2024-10-31, before the description; not opened. Accepted on the original description.

Name faults 0. Rank fault in the order field of lines 7 and 8 (below).

## Duplicates

git grep on origin/main (16530c42) across the whole docs/ tree (evidence, audit/ALL.jsonl, audit/corrected, sheets, searched/, progress notes) for Domene, Triplophysa, Odontostreptus, Iandumoema, Iansaoniscus, Schaefferia and the DOIs/article ids (zookeys.1216, zookeys.1281, ejt.2020.668, zookeys.537, subtbiol.43, subtbiol.54, 132155, 186268, 157228): no hit except Triplophysa wulongensis in desk-d280.md's not-filed list (another species, eyes present, not filed) and unrelated numeric matches of "6073" and "81308" in docs/eval and gbif-names.tsv (Phrynus id 2181308, a Celastrus search record). All 173 remote branches matching origin/research/desk-d2* or origin/research/audit-3* other than desk-d281: no hit for the six genera or six DOIs; no origin/research/desk-d281 branch exists. audit-3*.md hold-outs: none name these genera. Duplicates 0.

## Trait keys and rulings

- eye_type filing follows main and audit 370: animal absence as "none (...)" (main: "none (no external eye structures)", "none (eyes absent, ocular structures completely degenerated)"), reduction or variation as a descriptive string. Lines 3, 4, 5, 7, 8 ("none (...)") and lines 1, 2, 6 (descriptive) fit. Line 4's "ocularium without eyes": the ocularium is the eye mound; a mound without eyes is eye absence, and the Diagnosis ("eyes absent") and Table 1 ("Absent") say so, so "none" is right. Line 6 "vestigial" is kept apart from absence, rightly.
- Attribution by heading (lines 1, 2, 4 to 8): each sentence sits under a single new species' "Description" heading and states the value itself; acceptable as in audits 362, 364 and 370. Line 3 names the species.

## Per-record findings

### Line 1, Domene lizeyui, eye_type

Description, Head, verbatim in two pieces: "Eyes (Fig. 2E) extremely reduced, 0.06 times as long as postocular region in lateral view," | "lacking pigmentation, ommatidia unidentifiable." Preceded by "interstices wider than diameter of punctures, lacking microsculpture."; followed by "Neck region 3/8 width of head capsule." **Quote MATCH**, 19 words. Type material verbatim: holotype "♂, China, Sichuan, Leshan City, Hulu Town, Shiqianggou, Taojindong [=Taojin Cave]" ... "alt. 513 m, 28.V.2023"; paratypes "3♂♂4♀♀. 3♀♀, same data as holotype" | "• 3♂♂1♀, same data as holotype except 16.VI.2024". Habitat: "lives deep in the dark zone of the cave". Differential diagnosis: "eyes reduced, and wings absent."

Fault: the eye sentence is from the male holotype's description, which opens verbatim "Male holotype. Measurements." The male paratypes are covered only by "Three male types without evident variations to the holotype." and the females by "Body 8.9–9.2 mm long, similar to male in general appearance" (no eye statement). The record's method ("description of type specimens") and conditions ("from the species description") present the value as observed on all eight types. Uncounted: "dolomite shaft cave" ("shaft" not seen; the tool gave "a dolomite cave").

**Line 1 error (sample composition: holotype description filed as all type specimens).** Fixable.

### Line 2, Triplophysa zhijinensis, eye_type

Description verbatim in two pieces with the join confirmed: "Snout pointed; eyes highly degenerated–absent in three specimens examined" | ", and " | "two individuals retaining eyes as small black spots, eye diameter 1.3 and 2.9% of HL." Preceded by "Head robust, width slightly greater than depth, 22.4–25.7% of SL."; followed by "Interorbital width 35.1/35.3% of head length." **Quote MATCH**, 25 words. Diagnosis verbatim: "eyes are either absent or have degenerated into a small black spot with a diameter of 1.3–2.9% of HL". The value carries the 3-of-5 split and both diameters. Type material verbatim: holotype "GZNUSLS202410072 (Fig. 1), 74.1 mm SL, collected by Ren-Yi Zhang, Ting-Ting Zhu, and local people on October 30, 2024,"; paratypes "GZNUSLS202410063–065, 69.0–86.6 mm SL, GZNUSLS202410073, 60.7 mm SL,"; "The new species was collected from an underground river in Xiongjiachang Town, Zhijin County,". Uncounted: the Sexual dimorphism section identifies the holotype as male ("In one male specimen (GZNUSLS202410072, 74.1 mm SL)"), so "specimen sexes not stated" can be narrowed; the habitat is an underground river; the year note is stale.

**Line 2 MATCH.**

### Line 3, Odontostreptus fadriquei, eye_type none

Discussion, first sentence, verbatim: "Odontostreptus fadriquei sp. nov. shows some troglomorphic characters, notably lack of eyes and pigment." No sentence before (opens the Discussion); the next begins "Compared to other spirostreptids, the only other known troglomorphic spirostreptid, Orthoporus kiemi Loomis, 1962, is paler". **Quote MATCH**, 14 words; names the species. Head description "No eyes."; Diagnosis "Differs from other species of Odontostreptus, and from all other known spirostreptid millipedes, by the lack of eyes." Type material verbatim: holotype "MOROCCO • ♂; Agadir, Ifni (= Cave) Bougayou, Ouauosrou Kbt, Immouzer des Ida ou Tanane; 30 Jul. 2003;" ... "MZB 2003-1301."; paratype "MOROCCO • 1 ♀; same collection data as for holotype; MZB 2019-2016." Conditions match.

**Line 3 MATCH.**

### Line 4, Iandumoema smeagol, eye_type none

Description, "Male: Dorsum (Figures 2, 3, 4)", verbatim: "Ocularium without eyes; with high upwardly directed spine, apex curved backwards." Preceded by "Frontal hump with five tubercles (paramedian pair largest), anterior margin of dorsal scutum with 4–5 tubercles on each side."; followed by "Each side of ocularium with 2-3 tubercles." **Quote MATCH**, 11 words. Diagnosis "eyes absent and the penial ventral process slender ..."; Table 1 I. smeagol "Absent"; female: "Only characteristics different from those of males are mentioned." (no eye entry, so the same). Methods verbatim: "The type material were collected, fixed in 70% ethanol and examined under a stereomicroscope." Type material (tool summary with verbatim pieces): holotype male MZUSP 67946, Toca do Geraldo, 8 July 2014; paratypes "same locality of holotype, 22.II.2014 ... one male" (LES/UFSCar 0006298) and two males MZUSP 67947, 67948; one female LES/UFSCar 0006299, Lapa do Santo Antônio, 21 February 2014. Conditions match.

**Line 4 MATCH.**

### Line 5, Iansaoniscus leilae, eye_type none

Description verbatim: "Body outline in lateral view as in Fig. 1A, colorless, eyes absent (Fig. 1A–C)." Preceded by "Maximum length: male and female, 6 mm." (first sentence under "Description.", so the description covers both sexes); followed by "Cephalon lateral lobes with straight distal margin; frontal shield triangular with frontal margin directed upward". **Quote MATCH**, 14 words. Discussion: eyes absent in I. iraquara, I. georginae and I. leilae, "but present and vestigial in I. paulae sp. nov." Material (tool summary): holotype male ISLA 95911, Toca do Gonçalo, 10 December 2018; paratypes 1 ♂ + 2 ♀ (ISLA 95912), 1 ♂ + 1 ♀ (95913) and 6 ♀ (95914) of 5 January 2008, and Toca da Tiquara "1 male (mounted in slide), 1 female; municipality of Campo Formoso, Toca da Tiquara cave" ... "RL Ferreira leg.; ISLA 95917." with no date: 13 paratypes, as the record says.

**Line 5 MATCH.**

### Line 6, Iansaoniscus paulae, eye_type

Description verbatim: "Body outline as in Fig. 5A, colorless, vestigial eyes (Fig. 5A, B)." Preceded by "Maximum length: male, 3 mm; female 5 mm."; followed by "Cephalon with well-developed lateral lobes, round distal margin; frontal shield rounded, weakly developed (Fig. 5B)." **Quote MATCH**, 12 words. "present" in the value is backed by the Discussion's "present and vestigial in I. paulae sp. nov." and adds nothing beyond vestigial eyes. Material (tool summary): holotype slide-mounted male ISLA 95915, Lapa do Bode, Itaeté, 26 July 2007; five females ISLA 95916, same data. Conditions match.

**Line 6 MATCH.**

### Line 7, Schaefferia greensladeae, eye_type none

Description, run-in heading "Head.": "Eyes absent." Preceded by the antenna paragraph ending "and 20 setae around sensilla."; followed by "PAO near base of Ant I well developed, large, about 33 µm in diameter, with 7 subequal lobes formed around central circle (Fig. 3F)." **Quote MATCH**, 2 words. The Description covers the type series ("Length 1.9 mm on average (n = 3, max. length 2 mm)."); Diagnosis "Eyes absent, PAO large ..."; Abstract "Both species are characterized by the absence of eyes and postantennal organ (PAO)" (tool reading; the abstract wording on the PAO is internally inconsistent per the tool and was not filed). Type material (tool summary with verbatim pieces): holotype female on slide, "dark zone, collected from surface of water puddle, 15.x.2023,", Danial Cave, Iran; two paratypes, sex not stated. Conditions match.

Fault: `order` is "Collembola", which the title prints as the class-level group; the order it prints is Poduromorpha ("(Collembola, Poduromorpha, Hypogastruridae)"), and the note's "Family and order as printed in the title" is therefore not true of the order field. Main is mixed (Dicyrtomidae filed once under Collembola, twice under Symphypleona); the printed order should win.

**Line 7 error (order field: class filed as order).** Fixable.

### Line 8, Schaefferia montenegrina, eye_type none

Description, "Head.": "Eyes absent." Preceded by "...and 18 setae around sensilla."; followed by "PAO small but very distinct and located near base of Ant I, about 17 µm in diameter, with 5–6 equal lobes...". **Quote MATCH**, 2 words. Description covers the type series ("Length 1.4 mm on average (n = 4, max. length 1.5 mm)."); Diagnosis "Eyes absent, PAO small, forming a rosette of 5–6 regular oval vesicles." The Taxonomic remarks sentence ("Similarly to S. montenegrina sp. nov. the following species have reduced number of eyes to 0–1:", whole sentence not seen) compares congeners and does not contradict absence; the note handles it rightly. Type material (tool summary): holotype female "dark zone, collected from surface of water, 06.vi.2015,", Babatuša Cave, Montenegro; paratypes one female rotten wood 23.vi.2011, one female water surface 06.vi.2015, one male sinter pool 23.vi.2011. Conditions match except "near Trnovo", not seen (uncounted).

Fault: as line 7, `order` "Collembola" for printed order Poduromorpha.

**Line 8 error (order field: class filed as order).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Domene lizeyui, eyes extremely reduced | error, fixable | method, conditions | quote MATCH (19); eye sentence is the male holotype's description, filed as all eight types |
| 2 | Triplophysa zhijinensis, absent in 3 of 5 | MATCH | none | quote MATCH (25), join seen; variation carried; licence page-only (Crossref failed) |
| 3 | Odontostreptus fadriquei, none | MATCH | none | quote MATCH (14), names species; Spirostreptidae as printed |
| 4 | Iandumoema smeagol, none (ocularium without eyes) | MATCH | none | quote MATCH (11); Diagnosis and Table 1 "Absent" |
| 5 | Iansaoniscus leilae, none | MATCH | none | quote MATCH (14); licence page-only (Crossref failed) |
| 6 | Iansaoniscus paulae, vestigial eyes | MATCH | none | quote MATCH (12); vestigial kept apart from absent |
| 7 | Schaefferia greensladeae, none | error, fixable | order, note | quote MATCH (2); order "Collembola" for printed Poduromorpha |
| 8 | Schaefferia montenegrina, none | error, fixable | order, note | quote MATCH (2); same order fault |

Errors 3 of 8 audited records (37.5%), above the 5% bar; none held out. By kind: sample composition 1 (line 1); taxonomy field 2 (lines 7, 8, one shared cause); quotes 0; value exceeding quote 0; bibliographic 0; licence 0 (lines 2, 5, 6 rest on the publisher's printed CC BY 4.0 sentence, Crossref single-DOI failed and was not worked around); names 0; duplicates 0 against main, all 173 desk-d2* and audit-3* branches and the audit-3* hold-outs; trait keys 0.

Unchecked: checklist entries for Domene lizeyui, Iandumoema smeagol and the two Schaefferia species (only the original descriptions and their printed ZooBank URLs seen; ZooBank not opened); the source behind the Swedish Bioatlas entries for Odontostreptus and Iansaoniscus; Crossref metadata for 10.3897/zookeys.1281.186268 and 10.3897/subtbiol.43.81308 (client_error); the printed year on the Schaefferia and Iansaoniscus pages beyond the tool's citation reading; "shaft" (line 1) and "near Trnovo" (line 8); the whole Schaefferia Taxonomic remarks sentence; the Iansaoniscus and Schaefferia type-material paragraphs beyond tool summaries.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). "field = new string" replaces the whole field.

Line 1, counted:
- `method`: "morphological description of type specimens" -> "morphological description of the male holotype (three male paratypes stated to show no evident variation from it)"
- `conditions`: "the eye measurement is from the species description in lateral view" -> "the eye measurement is from the description of the male holotype, in lateral view (the male paratypes are said to be without evident variation; the female description states no eye character)"

Lines 7 and 8, counted (same strings in each line):
- `order` = "Poduromorpha"
- `note`: "Family and order as printed in the title (Collembola, Poduromorpha, Hypogastruridae)." -> "Family and order as printed in the title (Collembola, Poduromorpha, Hypogastruridae; Collembola is the class)."

Line 2, uncounted:
- `conditions`: "specimen sexes not stated in the material read" -> "the holotype is identified as male in the Sexual dimorphism section; paratype sexes not stated; collected from an underground river"
- `note`: "; not independently checked on the page" -> "; the page's citation line prints 2026"
