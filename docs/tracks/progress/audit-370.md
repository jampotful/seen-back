# audit-370: desk-d280, evidence lines 1 to 5

Audited 1 November 2026 from the desk-d280 files present untracked in the worktree (docs/tracks/progress/desk-d280.md and docs/views/evidence/desk-d280.jsonl, 5 lines; neither committed here, neither edited; both identical to origin/research/desk-d280). Worktree HEAD and origin/main 1a3e38c1 (Close d279 with 0). `python3 -I tools/senses/check.py | grep 'd280\.'`: "docs/views/evidence/desk-d280.jsonl: 5 records, 0 problems". Quote lengths (`len(q.split())`): 14, 14, 39, 26, 32, all within 40. Non-ASCII in quotes: only "–" and "±" in line 4, as printed. File order differs from the launch prompt: line 4 is Sinocyclocheilus longicornus, line 5 is Astyanax mexicanus; line numbers below are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/works/ for all five DOIs (10.3897/vz.72.e79911, 10.3897/subtbiol.56.188075, 10.1371/journal.pone.0223828, 10.3897/zookeys.1141.91501, 10.3897/subtbiol.26.26643; all five answered); vertebrate-zoology.arphahub.com/article/79911/download/xml/ (two passes); subtbiol.pensoft.net/article/188075/download/xml/ (one pass); journals.plos.org pone.0223828 (one pass, not rate-limited); zookeys.pensoft.net/article/91501/download/xml/ (truncated at Table 1, no Table 4) and article_preview.php?id=91501 (two passes); subtbiol.pensoft.net/article_preview.php?id=26643 (two passes). Names: amphibiansoftheworld.amnh.org Gegeneophis carnosus page; Eschmeyer's Catalog (researcharchive.calacademy.org fishcatget spid=77196). PMC, GBIF, Wikipedia mirrors, core.ac.uk, typeset.io, ri.conicet.gov.ar and the library catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 11 WebSearches.

## Bibliographic and licence

- Line 1 (Palakkool, Gower, Kotharambath 2022). Crossref: Shamna Rajan Palakkool, David J. Gower, Ramachandran Kotharambath; title identical; Vertebrate Zoology 72, 561-576, no issue; issued 2022-07-20; CC BY 4.0 vor, delay 0; relation empty. Page: "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)". Accepted.
- Line 2 (He et al. 2026). Crossref: Yue-Ming He, Hong-Quan Xiang, Jin-Mei Yang, Hui Zheng, Suo-Zhu Yang, Yu-Feng Zhou, Jian Zheng, in that order; title identical; Subterranean Biology 56, 127-136, no issue; issued 2026-05-29; CC BY 4.0 vor; relation empty. Page prints the CC BY 4.0 sentence and the same author line. Accepted.
- Line 3 (Acosta 2019). Crossref: Luis E. Acosta; title identical; PLOS ONE 14(10) e0223828; issued 2019-10-23; CC BY 4.0 vor; relation empty (no correction). Page: "This is an open access article distributed under the terms of the Creative Commons Attribution License". Accepted.
- Line 4 (Xu et al. 2023). Crossref: Cheng Xu, Tao Luo, Jia-Jun Zhou, Li Wu, Xin-Rui Zhao, Hong-Fu Yang, Ning Xiao, Jiang Zhou; title identical; ZooKeys 1141, 1-28, no issue; issued 2023-01-17; CC BY 4.0 vor; relation empty. Page: "open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)". Accepted.
- Line 5 (Espinasa et al. 2018). Crossref: Luis Espinasa, Laurent Legendre, Julien Fumey, Maryline Blin, Sylvie Rétaux, Monika Espinasa; title identical; Subterranean Biology 26, 39-53; issued 2018-07-04; CC BY 4.0 vor; relation empty. Page citation line verbatim: "Citation: Espinasa L, Legendre L, Fumey J, Blin M, Rétaux S, Espinasa M (2018) A new cave locality for Astyanax" | "cavefish in Sierra de El Abra, Mexico. Subterranean Biology 26: 39-53."; licence "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout. Printed year on the page seen only for line 5; lines 1 to 4 rest on Crossref issued, which agrees with the record.

## Names

None of the five genera is in docs/views/gaps/gbif-names.tsv.
- Gegeneophis carnosus: Amphibian Species of the World species page "Gegeneophis carnosus (Beddome, 1870)", filed under Gymnophiona / Grandisoniidae / Gegeneophis (page path; the page text returned names no family, tool summary). Family Grandisoniidae as printed in the paper's title and as main files four other caecilians (oa-5.jsonl, Grandisoniidae / Gymnophiona). Met. The launch prompt's "Gegeneophiidae/Siphonopidae?" does not apply; the record files Grandisoniidae.
- Erhaia dijiang: described in this paper ("sp. nov.", authority "Y.-M. He, H.-Q. Xiang, Y.-F. Zhou & H. Zheng"); family Erhaiidae Davis & Kuo, 1985, superfamily Truncatelloidea (tool summary). No checklist entry found (one search; MolluscaBase not returned). Accepted on the original description; unchecked against a checklist. Order not filed is acceptable; the treatment metadata give Littorinimorpha (tool summary), which could be added.
- Otilioleptes marcelae: new genus, species and family in this paper (Otilioleptidae, Gonyleptoidea, Opiliones). No later checklist opened (GBIF refused by rule). Accepted on the original description; later reassignment unchecked.
- Sinocyclocheilus longicornus: Eschmeyer's Catalog verbatim "Valid as Sinocyclocheilus longicornus Luo, Xu, Wu, Zhou & Zhou 2023", "Cyprinidae: Cyprininae." Met.
- Astyanax mexicanus: printed as "The blind Mexican tetra *Astyanax mexicanus* De Filippi 1853" (Introduction). Family and order not filed. Main files all its rows as Acestrorhamphidae / Characiformes (desk-d162 and others; audit 304 ruled Characidae a fault). Leaving the fields empty is not a fault; filling them from main is suggested below (uncounted).

Name faults 0.

## Duplicates

git grep on origin/main (1a3e38c1) across the whole docs/ tree (evidence, audit/ALL.jsonl, audit/corrected, sheets, searched/, progress notes) for Gegeneophis, Erhaia, Erhaiidae, Otilioleptes, Otilioleptidae, "Sinocyclocheilus", Chiquitita and the five DOIs (vz.72.e79911, subtbiol.56, pone.0223828, zookeys.1141, subtbiol.26): no hit. Astyanax mexicanus on main: sense_airflow 4 (eLife.77387), sense_light_nonvisual 4 (peerj.8148), sense_hearing 1 and absolute_sensitivity 1 (fevo.2023.1085975), sense_chemical 1 (d12100395); no eye_type row, no Chiquitita row, no subtbiol.26 DOI. All 172 remote branches matching origin/research/desk-d2* or origin/research/audit-3*: only origin/research/desk-d280 holds these names or DOIs, and no branch-only Astyanax file outside the d162 to d218 units already on main. audit-3*.md hold-outs: Astyanax appears only in audit-304 (Blin et al. 2020, sense_chemical). Duplicates 0.

## Trait keys and rulings

- eye_type for absence and reduction follows main: animal absence is filed as "none (...)" (e.g. "none (no external eye structures)") and reduction as a descriptive string ("degenerated eyes", "reduced eyes covered by skin or bone"). Line 2 "none (eyes absent, ...)" and the descriptive strings of lines 1, 3 and 5 fit. The plant "none" ruling does not bear on these animals.
- eye_diameter_mm (line 4) is not in check.py's TRAITS, so the "new trait" note is what lets it pass; but the key is not new: main holds 346 `"trait": "eye_diameter_mm"` rows (oa-1, oa-2, oa-5, oa-6, audit/corrected, ALL.jsonl), 283 of them noting "new trait", with floats and three two-number lists for ranges ([9.56, 11.57], [6, 7]). Line 4's key and its [0, 1.6] list follow that use. The note's "no eye-size key exists" is false and must go; the phrase "new trait" must stay for check.py.
- Attribution by heading (lines 2, 3) and by title (line 1): each sentence sits in a single-species description or a single-species paper and states the value itself; the species is fixed by the heading or title. Acceptable, as in audits 362 and 364.

## Per-record findings

### Line 1, Gegeneophis carnosus, eye_type

Results, subsection "Skull", verbatim in one piece: "The eyes are small and covered by maxillopalatines, and so orbits are absent (closed)." Ends seen: the sentence before ends a sentence on the os basale and pterygoquadrates (Fig. 1C), the one after begins "The seven major external openings are the foramen magnum and the paired external nares, …". Abstract verbatim: "The eye is covered by the maxillopalatine, and an (open) orbit is absent." **Quote MATCH**, 14 words. Value says no more than the quote ("bones" is a gloss of maxillopalatines). Verified: "Nine specimens of *G. carnosus* were collected from the vicinity of its type locality Peria, Wayanad" (14 July 2015); "all are female, based on observation of ova via incisions into the coelom."; "The specimens ranged from 112–209 mm in total length"; RAM 0020 scanned, 198 mm preserved total length (tool summary). Only G. carnosus examined; comparisons are with published data (verbatim: "We make comparisons with available data for other members of Grandisoniidae"). No eye diameter or external visibility statement (tool summary), as the note says. Licence, names, duplicates clean.

**Line 1 MATCH.**

### Line 2, Erhaia dijiang, eye_type none

Under the species heading "Erhaia dijiang ... sp. nov.", subheading "Description", verbatim in one piece: "All individuals examined to date absence of eyes, with complete degeneration of ocular structures." Preceded by a Figure 3 caption after a paragraph ending "Umbilicus narrow."; followed by "Snout slender, anterior slight enlargement; tentacles slender, translucent." **Quote MATCH**, 14 words, grammar as printed. Abstract verbatim: "This species is a member of the family Erhaiidae, characterized by the absence of eyes." Verified verbatim: holotype "NCUDX251201, shell length 2.05 mm"; paratypes "3 specimens, NCUDX251202-04 (NCUDX251202-03 living specimens, NCUDX251204 empty shell)"; "altitude 2062 m"; "in August 2025"; "using a fishing net with a mesh size of less than 1.5 mm"; the co-occurring Pomatiopsidae snail "possesses normal eyes". Uncounted: only three of the four specimens were living, so "all individuals" covers at most three animals; the conditions could say so.

**Line 2 MATCH.**

### Line 3, Otilioleptes marcelae, eye_type

Description of Otilioleptes marcelae sp. nov., paragraph "Dorsal scutum" (not a holotype-only description), verbatim in three pieces: "Ocular mound low and unarmed, covered by small granules; eyes are hard to find among granulation" | "since corneas are extremely reduced (in all specimens, two spots of retinal pigment deepened," | "probably because of retraction of internal tissues during fixation)." Joins match the record's; the paragraph before ends "Similar granulation forms a row both sides on the anterior border," and the next sentence begins "Scattered small granules behind and beside the ocular mound give this part a tenuous rugulose look." **Quote MATCH**, 39 words. Type material verified verbatim (holotype male and 1 female paratype FML-OPIL 00211, "~350 m from entrance, 20 August 2006"; 1 male paratype FML-OPIL 00218, "04 April 2012").

Fault: the value says more than the quote. It opens "eyes extremely reduced:", but the quote says the corneas are extremely reduced and the eyes are hard to find; "eyes extremely reduced" is the desk's inference (the family diagnosis's "extremely rudimentary eyes" and the Abstract's "reduction of eyes" are elsewhere and not quoted). And the value files "two deepened spots of retinal pigment" as a trait while the quote attributes the deepening probably to fixation; the qualifier is only in the note. Uncounted: "where" can name the "Dorsal scutum" paragraph.

**Line 3 error (value exceeds the quote; fixation qualifier dropped from the value).** Fixable.

### Line 4, Sinocyclocheilus longicornus, eye_diameter_mm [0, 1.6]

Table 4, caption verbatim: "Morphological comparison of Sinocyclocheilus longicornus sp. nov. (SL), S. angularis (SA), S. bicornutus (SB)," | "S. rhinocerous (SR), S. zhenfengensis (SZ), and S. hyalinus. All units in mm." | "P-values are at 95% significance." Header order (tool layout): Measurements | S. longicornus (N = 15) | S. angularis (N = 7) | S. bicornutus (N = 2) | S. rhinocerous (N = 11) | S. zhenfengensis (N = 8) | S. hyalinus (N = 1) | P-value from Mann-Whitney U test; sub-columns Range, Mean ± SD for each species except S. hyalinus (Range only), then SL vs. SA, SL vs. SB, SL vs. SR, SL vs. SZ. ED row cell by cell: "ED | 0–1.6 | 1.1 ± 0.5 | 1.5–2.6 | 1.9 ± 0.4 | 2.2–3.5 | 2.9 ± 0.9 | 0.6–4.1 | 1.3 ± 1.0 | 2.1–2.84 | 2.3 ± 0.2 | 0 | 0.000 | 0.015 | 0.291 | 0.000". The record's quote is this row whole, 16 cells; **quote MATCH**, 26 words. Column assignment right: S. longicornus is the first Range/Mean pair; 16 cells fit 5 × 2 + 1 + 4.

Faults:
- Measured quantity not stated. Methods verbatim: "ED** eye diameter (diameter of the exposed portion of the eyeball);" and "A total of 31 measurements were recorded to the nearest 0.1 mm with digital calipers"; "All specimens were fixed in 10% buffered formalin and later transferred to 75% ethanol". The record files the number as eye diameter and says only that "the ED abbreviation is explained in the paper's methods". The value 0 is the diameter of the exposed part of the eye, which is 0 when the eye is covered as well as when it is absent; the note's "(a range starting at 0 means some specimens have no measurable eye)" is the desk's reading and should say "no exposed eyeball". Table 3 codes the new species' eye state "1/0" (reduced/absent) (tool summary), which the note could cite.
- Sample composition omitted: holotype "adult male" and "fourteen adult males" as paratypes (tool summary), so N = 15 is all adult males; the conditions do not say so.
- The note's "(no eye-size key exists)" is false (346 eye_diameter_mm rows on main).
- Uncounted: SL vs. SR P = 0.291 (not different from S. rhinocerous) is printed in the quoted row; holotype collected 6 May 2021 (tool summary).

**Line 4 error (ED is the exposed-eyeball diameter, not stated; all-male sample not stated; false note).** Fixable.

### Line 5, Astyanax mexicanus, eye_type variable

Results verbatim in two pieces: "There was high variability in the eye, with individuals having phenotypes such as small eye size (Fig. 3A)," | "closed pupil (Fig. 3B), embedded eye (Fig. 3C), and eye mostly absent (Fig. 3D)." Preceded by "Fish were highly depigmented and were easily differentiated from the surface congeners" | "by their characteristic pinkish-white coloration."; followed by "Introgression between the surface morph and the cave morph is suggested by the presence of individuals" | "that are highly depigmented, but with eyes (Fig. 4B) or individuals with pigment and reduced eyes (Fig. 3A–B)." **Quote MATCH**, 32 words, figure references kept.

Verified verbatim: juveniles "(2.7 and 3 cm standard length)" "collected from the small cave under the tree on 3/20/16", together with "A poecilid, an epigeomorphic juvenile *Astyanax*"; "Four adult (3.48 cm standard length, 0.96 gr; 5.60 cm, 4.82 gr; 6.08 cm, 4.63 gr; 6.68 cm, 6.49 gr in fixed fish)" from the well on 3/23/16; "Adults were taken alive to the laboratory where behavioral experiments were conducted the following day."; "Photographs were taken on the field with a Canon EOS100 camera." Fig. 3 caption: "High variability in the eye and pigmentation level within the population inhabiting Chiquitita Cave." | "... C in the foreground a troglomorphic fish with reduced and embedded eyes" | "and in the background a pigmented fish with large eyes D eyes and pigment mostly absent." Wild vs lab: all fish are wild-collected; no lab-raised surface fish is in the record. Met.

Faults:
- Qualifier dropped from the value: the quote lists phenotypes "such as" four kinds; the value "variable among individuals: small eye, closed pupil, embedded eye, or eye mostly absent" reads as a closed list.
- Sample composition misdescribed: the conditions call it the "Troglomorphic population of Chiquitita Cave", but the authors conclude, verbatim, "it is a mixed population with surface individuals probably hybridizing with the troglomorphic population." and in the Discussion "These fish showed variability in their eye development and pigmentation level like in the Chica cave," | "consistent with introgression."; the cave also held an epigeomorphic juvenile and (Fig. 3C) a pigmented large-eyed fish. The note's paraphrase of the next sentence is not enough: the eye variability is that of a probably introgressed mixed population, which the conditions must say.
- On the launch prompt's pooling question: this is one population's among-individual variation, not a value pooled across populations or taxa, and the morphs are one species, so the record is not a hybrid-taxon or pooled record under the rules; with the disclosure it is fileable. The owner may still prefer to hold mixed-population eye_type rows.
- Uncounted: adults were kept alive to the laboratory a day for behaviour trials before fixation (still wild fish); family and order could be filled from main (Acestrorhamphidae, Characiformes).

**Line 5 error ("such as" dropped from the value; mixed, probably hybridizing population not disclosed).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Gegeneophis carnosus, eyes small, covered, orbit closed | MATCH | none | quote whole (14), ends seen; licence, names, duplicates clean |
| 2 | Erhaia dijiang, none | MATCH | none | quote whole (14) under species heading; licence clean |
| 3 | Otilioleptes marcelae, corneas extremely reduced | error, fixable | value | "eyes extremely reduced" not in quote; fixation qualifier only in note |
| 4 | Sinocyclocheilus longicornus, ED 0-1.6 mm | error, fixable | method, conditions, note | row MATCH (26), column right; ED = exposed-eyeball diameter unstated; all adult males unstated; false "no key" note |
| 5 | Astyanax mexicanus, variable eye phenotypes | error, fixable | value, conditions | quote MATCH (32); "such as" dropped; mixed probably hybridizing population not disclosed |

Errors 3 of 5 audited records (60%), above the 5% bar; none held out. By kind: value exceeding quote or dropping a qualifier 2 (lines 3, 5); measured quantity and sample composition 2 (lines 4, 5); bibliographic 0; licence 0; names 0; duplicates 0 against main, all 172 desk-d2* and audit-3* branches and the audit-3* hold-outs; trait keys 0 (eye_diameter_mm is an existing key on main, passing check.py through its "new trait" note).

Unchecked: a checklist entry for Erhaia dijiang and for Otilioleptes marcelae / Otilioleptidae after 2019 (only the original descriptions seen); Amphibian Species of the World family as page text (path only); printed year on the pages of lines 1 to 4; the Table 3 "1/0" coding and the holotype date for line 4 (tool summary only); which Chiquitita fish appear in Fig. 3; the S. hyalinus "0" cell's meaning; the line 1 micro-CT specimen details (tool summary).

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). "field = new string" replaces the whole field.

Line 3, counted:
- `value`: "eyes extremely reduced: corneas extremely reduced, eyes hard to find on the ocular mound, two deepened spots of retinal pigment" -> "corneas extremely reduced, eyes hard to find among the granulation of the ocular mound; two spots of retinal pigment deepened in all specimens, probably from retraction of internal tissues during fixation"
- `where` (uncounted): "sp. nov., Description" -> "sp. nov., Description, Dorsal scutum"

Line 4, counted:
- `method`: "morphometrics of preserved cave-collected specimens" -> "digital caliper morphometrics (nearest 0.1 mm) of formalin-fixed, ethanol-preserved cave-collected specimens; ED is the diameter of the exposed portion of the eyeball"
- `conditions`: "N = 15 (holotype plus 14 paratypes)" -> "N = 15 (holotype plus 14 paratypes, all adult males)"
- `note`: "new trait: eye_diameter_mm (no eye-size key exists)." -> "new trait: eye_diameter_mm (not in check.py's list; the same key is used on main)."
- `note`: "(a range starting at 0 means some specimens have no measurable eye)" -> "(the Methods define ED as the diameter of the exposed portion of the eyeball, so a range starting at 0 means some specimens have no exposed eyeball; Table 3 codes the species' eyes as reduced/absent, 1/0)"

Line 5, counted:
- `value`: "variable among individuals: small eye" -> "variable among individuals, with phenotypes such as small eye"
- `conditions`: "Troglomorphic population of Chiquitita Cave" -> "Troglomorphic Astyanax of Chiquitita Cave, which the authors conclude is a mixed population with surface individuals probably hybridizing with the troglomorphic population (variability consistent with introgression; an epigeomorphic juvenile was also caught and Fig. 3C shows a pigmented fish with large eyes)"
- `conditions` (uncounted): "sex not reported)" -> "sex not reported; adults were kept alive one day for behaviour trials before fixation)"

Line 2, uncounted:
- `conditions`: "one an empty shell)" -> "one an empty shell, so at most three living animals were examined for eyes)"
