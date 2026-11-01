# audit-372: desk-d282, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d282 files present untracked in the worktree (docs/tracks/progress/desk-d282.md and docs/views/evidence/desk-d282.jsonl, 7 lines; neither committed here, neither edited; the jsonl is identical to origin/research/desk-d282). Worktree HEAD and origin/main 7443ecfa (Merge d281 after audit 371). `python3 -I tools/senses/check.py | grep 'd282\.'`: "docs/views/evidence/desk-d282.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 2, 2, 12, 7, 16, 25, 4, all within 40. Non-ASCII in quotes: "–" in line 5, as printed. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/works/ for all six DOIs (10.3897/zookeys.1031.62181, 10.3897/subtbiol.43.83592, 10.3897/zse.102.182296, 10.3897/zse.101.154380, 10.3897/zookeys.749.24964, 10.3897/zookeys.1255.164170; all six answered); zookeys.pensoft.net/article/62181/download/xml/ (two passes); subtbiol.pensoft.net/article/83592/download/xml/ (one pass); zse.pensoft.net/article/182296/download/xml/ (one pass); zse.pensoft.net/article/154380/download/xml/ (one pass); zookeys.pensoft.net/article/24964/download/xml/ (two passes); zookeys.pensoft.net/article/164170/download/xml/ (one pass). Names: wsc.nmbe.ch/refincluded/15764 (World Spider Catalog); research.calacademy.org fishcatget spid=78177 (Eschmeyer's Catalog). PMC, GBIF, WoRMS, Plazi, Zenodo, the Butantan repository copy, novataxa, kiwix mirrors and library catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 8 WebSearches.

## Bibliographic and licence

- Lines 1, 2 (Brescovit, Zampaulo, Cizauskas 2021). Crossref: Antonio D. Brescovit, Robson de A. Zampaulo, Igor Cizauskas; title identical; ZooKeys 1031, 143-159, no issue; issued 2021-04-15; CC BY 4.0 vor, delay 0; relation empty. Page citation verbatim: "Brescovit AD, Zampaulo R de A, Cizauskas I (2021) The first two blind troglobitic spiders of the genus Ochyrocera" | "from caves in Floresta Nacional de Carajás, state of Pará, Brazil (Araneae, Ochyroceratidae). ZooKeys 1031: 143–159."; licence "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Licence accepted. Fault: the record's authors "Brescovit AD, Zampaulo RA, Cizauskas I" drop the printed "de" ("Zampaulo R de A"; the World Spider Catalog also prints "Zampaulo, R. de A."). Counted on each line (authors as printed).
- Line 3 (Hernando, Castro 2022). Crossref: Carles Hernando, Agustín Castro; title identical; Subterranean Biology 43, 1-10; issued 2022-04-18; CC BY 4.0 vor; relation empty. Page: "Hernando C, Castro A (2022)" ... "Subterranean Biology 43: 1–10"; licence sentence as above. Accepted. Uncounted: the page title prints a curly apostrophe ("world’s"); Crossref and the record have a straight one.
- Line 4 (Jiang, Zhou, Chen 2026). Crossref: Xuankong Jiang, Jiajun Zhou, Huiming Chen; title identical; Zoosystematics and Evolution 102, journal-issue 2, 601-609; issued 2026-04-06; CC BY 4.0 vor; relation empty. Page licence sentence as above; no formatted citation line returned, so "(2)" and the year rest on the article metadata and Crossref (tool summary). Accepted.
- Line 5 (Zhu, Yuan, Zhang, Zhao 2025). Crossref: Ting-Ting Zhu, Feng-Hua Yuan, Ren-Yi Zhang, Ya-Hui Zhao; title identical; volume 101, journal-issue 4, 1383-1396; issued 2025-08-05; CC BY 4.0 vor; relation empty. Page byline in the same order; licence sentence as above. Accepted. (The species authority "Zhu, Zhang & Yuan" differs from the byline; the record keeps them apart rightly.)
- Line 6 (Perreau, Růžička 2018). Crossref: Michel Perreau, Jan Růžička; title identical; ZooKeys 749, 135-147; issued 2018-04-10; CC BY 4.0 vor; relation empty. Page: "Perreau M, Růžička J (2018)" ... "ZooKeys 749: 135–147"; licence sentence as above. Accepted.
- Line 7 (Mehrafrooz Mayvan, Kováč 2025). Crossref: Mahmood Mehrafrooz Mayvan, Ľubomír Kováč; title identical; ZooKeys 1255, 1-25; issued 2025-10-09; CC BY 4.0 vor; relation empty. Page: "Mehrafrooz Mayvan M, Kováč Ľ (2025)" | "ZooKeys 1255: 1–25."; licence sentence as above. Accepted.

Bibliographic faults 2 (lines 1, 2, one cause); licence faults 0; source.access "open" right throughout.

## Names

None of the six genera is in docs/views/gaps/gbif-names.tsv. All seven names are new species described in the paper cited (original descriptions).
- Ochyrocera ritxoco, O. ritxoo: World Spider Catalog included-taxa page for the reference, verbatim "Ochyrocera ritxoco Brescovit, Zampaulo & Cizauskas, 2021 (Ochyroceratidae)" and "Ochyrocera ritxoo Brescovit, Zampaulo & Cizauskas, 2021 (Ochyroceratidae)". Met (the page lists what the reference described; I did not open the WSC species pages for later changes).
- Geopselaphus bullonorum: original description; title "(Coleoptera, Staphylinidae, Pselaphinae)". No checklist opened. Accepted on the original description.
- Caridina zhaoi: original description; title "(Decapoda, Caridea, Atyidae)". WoRMS refused by rule. Accepted on the original description.
- Triplophysa xiuwenensis: Eschmeyer's Catalog verbatim "Current status: Valid as Triplophysa xiuwenensis Zhu, Zhang & Yuan 2025.", "Nemacheilidae", original citation "in Zhu, Yuan, Zhang & Zhao 2025:1384" (tool summary of the last). Met.
- Ptomaphaginus troglodytes: original description; title "(Coleoptera, Leiodidae, Cholevinae, Ptomaphagini)". No checklist opened. Accepted on the original description.
- Acherontiella nezamdoosti: original description, authority "Mehrafrooz Mayvan & Kováč" "sp. nov.". The Taxonomy section prints, verbatim, "Class Collembola Lubbock, 1873", "Order Poduromorpha Börner, 1913", "Family Hypogastruridae Börner, 1906". So the order is printed in the paper (not in the title); main now files Hypogastruridae under Poduromorpha (desk-d281 lines 7, 8 after audit 371). The empty order field is not a fault (audit 370's Astyanax ruling); filling it is given below, uncounted.

Name faults 0.

## Duplicates

git grep on origin/main (7443ecfa) across the whole docs/ tree (evidence, audit/ALL.jsonl, audit/corrected, sheets, searched/, progress notes) for Ochyrocera, ritxo, Geopselaphus, bullonorum, Caridina zhaoi, zhaoi, xiuwenensis, Ptomaphaginus, Acherontiella, nezamdoosti and the DOIs/article ids (zookeys.1031, 62181, subtbiol.43.83592, 83592, zse.102, 182296, zse.101, 154380, zookeys.749, 24964, zookeys.1255, 164170): only desk-d279.md line 12 (the Ptomaphaginus lead, below) and unrelated numeric matches ("62181" inside an Osmunda search record in sweep-21.jsonl; "24964" as a cells.jsonl line number in codex-findings and in gbif/taxonomy tsvs, audit-87/124/125 and desk-d33 searched records). No Caridina species on main. All 176 remote branches matching origin/research/desk-d2* or origin/research/audit-3*: hits only in desk-d279.md (six branches carrying it) and in research/desk-d282 itself. audit-3*.md hold-outs: none name these genera.

Ptomaphaginus (line 6): desk-d279.md, verbatim, "Ptomaphaginus troglodytes (ZooKeys 749:135-147, CC BY 4.0): eyeless cave beetle; only fragments ("Head without eyes (Fig. 3)") and an abstract clause, not clean sentences; not on main. Possible eye_type "none" lead if a whole sentence can be verified." This was the desk's own hold, not an audit hold-out. The Abstract is one whole sentence, now read end to end (below), so the hold reason no longer applies; the source was rechecked for taxon, type material and meaning.

Duplicates 0.

## Trait keys and rulings

- eye_type filing (main, audits 370, 371): animal absence as "none (...)" (main has "none (eyes absent)" 4 times, "none (no external eye structures)", "none (eyes absent, ocular structures completely degenerated)", "none (ocularium without eyes)"); reduction as a descriptive string. Lines 1, 2, 7 ("none (eyes absent)") and lines 3, 4, 5 (descriptive) fit. Line 6 files "anophthalmic (no eyes)": absence not opening with "none", unlike every absence row on main and lines 1, 2, 7 of this unit; no "anophthalmic" value exists on main. Counted (line 6).
- eyes_count / ommatidia_count: main has both keys (216 and 76 rows). Line 3's "only three unpigmented ommatidia" could also be an ommatidia_count row, but the sentence does not say whether three is per eye or in total, so the eye_type string is the safe filing; not a fault.
- Attribution by heading (lines 1 to 5, 7): each sentence sits under a single new species' Description or Diagnosis heading and states the value itself; acceptable as in audits 362, 364, 370 and 371. Line 6 names the species.

## Per-record findings

### Line 1, Ochyrocera ritxoco, eye_type none (eyes absent)

Under "Description." "Male (Holotype).", verbatim: "Eyes absent." Preceded by "Clypeus with two pairs of long bristles (Fig. 3A)."; followed by the chelicerae sentence (light yellow, orange fang, three promarginal teeth on a very long lamina; tool summary). **Quote MATCH**, 2 words, standalone sentence. Female heading "Female (Paratype IBSP 115499)." and verbatim "Clypeus, eyes, chelicerae (Fig. 5B), sternum, endites, and labium as in male." Abstract, verbatim: "The species have similar body characteristics with the total absence of eyes and complete depigmentation." Holotype verbatim: "Holotype male from Cave N1_0103 (GEM-1301 or Cipó cave; 6°0'13"S, 50°17'55"W)," | "FLONA de Carajás, Parauapebas, Pará, Brazil, 28/XI-03/X/2007, R. Andrade et al. col. (IBSP 115497)." Paratype female Cave N1_0075 (Piranha cave), IBSP 115499 (tool summary). Diagnoses do not mention eyes (tool summary). Value says no more than the quote; holotype-only basis stated. Uncounted: Other material lists many more specimens from Serra Norte caves (sex ratio 2.4F:1M, N = 66; Variation gives size ranges from ten males and ten females; tool summary), none with an eye statement; the conditions could say the eye state is stated only for the holotype and "as in male" for the female paratype, with the Abstract extending it to the species.

Fault: authors field (see Bibliographic).

**Line 1 error (authors not as printed: "Zampaulo R de A").** Fixable.

### Line 2, Ochyrocera ritxoo, eye_type none (eyes absent)

Male heading "Male (IBSP 193194)" (the holotype number); verbatim "Eyes absent.", preceded by "Clypeus with two pairs of long bristles (Fig. 9A)."; followed by the chelicerae sentence (tool summary). **Quote MATCH**, 2 words. Female heading "Female. (Paratype IBSP 193196)." and verbatim "Clypeus, eyes, chelicerae, sternum, endites, and labium as in male." Holotype male Cave S11C_0201, Canaã dos Carajás, 27/VII/2015, BioEspeleo Consultoria Ambiental, IBSP 193194; paratype female Cave S11C_0052, 09/III/2016, IBSP 193196 (tool summary). Conditions match. Uncounted: other material from five further caves (N = 17, 1.4F:1M; tool summary); the record's "where" "male holotype" is right though the printed heading is "Male (IBSP 193194)".

**Line 2 error (authors not as printed, as line 1).** Fixable.

### Line 3, Geopselaphus bullonorum, eye_type reduced (three unpigmented ommatidia)

Under "Description of holotype.", verbatim: "Eyes reduced, with only three unpigmented ommatidia, likely not functional (Fig. 3)." Preceded by "Tomentose pubescence of ventral part, short and sparse, extending from gular protuberance to basal narrowing (Figs 8, 9)."; followed by "Antennae (Fig. 5) extraordinarily long (1.57 mm) and slender, exceeding the posterior margin of elytra when bent backwards". **Quote MATCH**, 12 words, figure reference kept. Value: "probably not functional" renders "likely not functional"; "reduced eyes" is not "eyes absent" and the record keeps it apart rightly. Abstract verbatim: "The new species shows a significant troglomorphy, such as the reduction of the eyes (only three unpigmented ommatidia)". Type material: holotype male "ESP. Málaga, Benaoján / Cueva de la Pileta, 04-26-2013," F. Fadrique leg., MCNB; paratypes two females, one same data (MCNB), one "Cueva de la Pileta, 06-08-2015," T. Pérez leg. (CCH) (tool summary with verbatim pieces). Female description: "General appearance similar to male" with no eye statement (tool summary). Conditions right.

Uncounted: the note's "The diagnosis line calls the holotype 'Apterous and microphtalmic'": the tool found no Diagnosis heading and placed "Apterous and microphtalmic, with only three omatidia (probably non-functional eyes)." under "Description of holotype."; the second paratype's date and collector could be added.

**Line 3 MATCH.**

### Line 4, Caridina zhaoi, eye_type highly reduced

Under "Diagnosis.", verbatim: "Eyes highly reduced, cornea indistinct and unpigmented." Preceded by "Body smooth, strongly depigmented; stygobitic."; followed by "Rostrum relatively long, reaching end of 2nd segment to slightly beyond 3rd segment of antennular peduncle". **Quote MATCH**, 7 words. Description verbatim: "Eyes (Figs 2B, 3A) small, highly reduced, and unpigmented." Remarks: "the complete lack of eye pigment (vs. pigment spot present)" against C. sinanensis (verbatim piece). Type material: holotype male "Dec-aty-00538-1"; locality "Guizhou Province, Guiyang City, Wudang District, Anduo Village, Xiangshui Cave"; "15. III. 2024"; paratypes 2 males and 7 females "Dec-aty-00538-2–10, same data as holotype." Neither Diagnosis nor Description says which specimens it rests on (tool summary; Description gives some holotype values in parentheses, e.g. "with 4–19 (holotype 16) teeth dorsally"). Conditions right. Uncounted: habitat, verbatim "The habitat is defined by an approximately 200-meter-long underground river" and "was found concentrated in a pool at the terminus of this river."

**Line 4 MATCH.**

### Line 5, Triplophysa xiuwenensis, eye_type reduced to black dot

Under "Description.", verbatim: "Eye reduced to black dot, located dorsolaterally on head, orbit indistinct, eye diameter 4.6–6.7% of HL." Preceded by "posterior nostril above maxillary barbel."; it ends the paragraph (next is the Figure 2 caption). **Quote MATCH**, 16 words. Diagnosis verbatim: "body naked, without skin pigmentation, lateral line complete; eye reduced, with diameter of HL 4.6–6.7%;". Table 2 (caption "Morphometric data of Triplophysa xiuwenensis sp. nov.") eye diameter % HL: holotype 4.7; paratypes min 4.6, max 6.7, mean 5.3, SD 0.8 (tool summary). Type material: holotype GZNUSLS202306086, 69.1 mm SL; paratypes "GZNUSLS202306088–090, 40.5–58.2 mm SL," and ASIZB 248338, 56.3 mm SL; sex not stated; Shilin Village, Dashi Buyi Township, Xiuwen County, 23 June 2023 (tool summary with verbatim pieces). No sexual dimorphism statement. Conditions right.

Uncounted: the holotype's 4.7 lies inside the paratypes' 4.6 to 6.7, so Table 2 shows the range covers all five types; the conditions' "the text does not say whether" can be settled.

**Line 5 MATCH.**

### Line 6, Ptomaphaginus troglodytes, eye_type anophthalmic

Abstract, the whole Abstract (one sentence; no sentence before or after), verbatim in two abutting pieces: "Ptomaphaginus troglodytes sp. n., the first anophthalmic species of Ptomaphaginus Portevin, 1914" | "is described from two close caves in Libo Karst, south Guizhou Province, China." Join checked in a second pass: "Portevin, 1914 is described" (no comma after 1914). **Quote MATCH**, 25 words, names the species. Meaning: "anophthalmic" is eyeless; the Description says "Head without eyes" (Fig. 3), the Diagnosis "Distinct from other Ptomaphaginus in the absence of eyes", and the key couplet "Anophthalmic. Transverse microstrigae of elytra tight and orthogonal to the suture". Pigment: "Body widely ovoid, uniformly light brown (depigmented)." Type material: holotype male, NSMT, "Shuiboshu Dong cave (490 m)," 13.ix.1997, "T. Kishmoto [leg.]"; paratypes "1 male and 2 females, same data" and "1 male and 1 female," "Yamen Dong cave" (tool summary with verbatim pieces). The Description's basis is not stated; figures are of the holotype, a male paratype and a female paratype (tool summary). Conditions right on the type series.

Fault: the value "anophthalmic (no eyes)" files absence without the "none" form that main and lines 1, 2, 7 use, so a reader or view selecting eye_type "none (...)" misses it. The paper's own word can stay inside the parentheses.

Uncounted: the label prints the collector as "Kishmoto" (record "Kishimoto", probably the right name; say "as printed: Kishmoto"); the Distribution section says "Libo Karst area, south of Guangxi Province" against Guizhou everywhere else (an internal inconsistency of the paper; tool summary); the note's reason for not filing the Description sentence is right.

**Line 6 error (absence not filed in the "none (...)" form).** Fixable.

### Line 7, Acherontiella nezamdoosti, eye_type none (eyes absent)

Under "Description.", paragraph "Head.": "Eyes and PAO absent." It is the paragraph's first sentence after the run-in label; followed by "Setal formula of labrum 4/5,5,4, four anterior labral setae thickened (Figs 4B, 5C)." **Quote MATCH**, 4 words. Diagnosis verbatim: "Colour white, without pigment. Eyes, PAO, furca and retinaculum absent." Description basis: "Length 0.76 mm on average (n = 8, maximum length 0.84 mm)." (n = 8 = holotype, 5 females, 2 juveniles). Type material: holotype "♂ on slide; Iran, Tehran province, Firouzkouh city, Herandeh village, Burnik Cave;" 2000 m a.s.l., "02 Aug. 2024", slide IrBuAc110; paratypes "5 ♀♀, 2 juveniles, on slides; Iran, same collection data as for holotype;" (IrBuAc111–117). Conditions right.

Uncounted: order can be filled from the paper's "Order Poduromorpha Börner, 1913", matching main's Hypogastruridae rows; the note then changes.

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Ochyrocera ritxoco, none (eyes absent) | error, fixable | source.authors | quote MATCH (2), male holotype; authors drop printed "de" |
| 2 | Ochyrocera ritxoo, none (eyes absent) | error, fixable | source.authors | quote MATCH (2); same author fault |
| 3 | Geopselaphus bullonorum, three unpigmented ommatidia | MATCH | none | quote MATCH (12) under "Description of holotype"; females' eyes unstated, as recorded |
| 4 | Caridina zhaoi, eyes highly reduced | MATCH | none | quote MATCH (7), Diagnosis; basis unstated, as recorded |
| 5 | Triplophysa xiuwenensis, black dot, 4.6-6.7% HL | MATCH | none | quote MATCH (16); Eschmeyer valid; Table 2 shows range covers all five |
| 6 | Ptomaphaginus troglodytes, anophthalmic | error, fixable | value | whole Abstract sentence MATCH (25); absence not in "none (...)" form |
| 7 | Acherontiella nezamdoosti, none (eyes absent) | MATCH | none | quote MATCH (4); description rests on n = 8; order printed in text (fill uncounted) |

Errors 3 of 7 audited records (42.9%), above the 5% bar; none held out. By kind: bibliographic 2 (lines 1, 2, one cause); filing convention 1 (line 6); quotes 0; value exceeding quote 0; sample composition 0; licence 0; names 0; duplicates 0 against main, all 176 desk-d2* and audit-3* branches and the audit-3* hold-outs. If the owner treats author initials as uncounted form, lines 1 and 2 become MATCH and the rate is 1 of 7 (14.3%), still above the bar.

Unchecked: checklist entries for Geopselaphus bullonorum, Caridina zhaoi, Ptomaphaginus troglodytes and Acherontiella nezamdoosti (only the original descriptions seen; WoRMS refused by rule, ZooBank not opened); World Spider Catalog species pages for later changes to the two Ochyrocera; the printed issue "(2)" and "(4)" for the Zoosystematics and Evolution papers on the page itself (metadata and Crossref only); whether a Diagnosis heading exists in the Geopselaphus paper; the Ochyrocera chelicerae sentences and the Other material lists beyond tool summaries; the Ptomaphaginus paratype data and the Guangxi sentence beyond tool summaries; Table 2 of the Triplophysa paper beyond a tool summary.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). "field = new string" replaces the whole field.

Lines 1 and 2, counted (same string in each line):
- `source.authors`: "Zampaulo RA" -> "Zampaulo R de A"

Line 6, counted:
- `value` = "none (anophthalmic: head without eyes)"

Line 6, uncounted:
- `conditions`: "T. Kishimoto leg." -> "T. Kishimoto leg., printed 'Kishmoto' on the label transcription"
- `note`: "neither is a clean short sentence" -> "neither is a clean short sentence (the paper's Distribution section says 'south of Guangxi Province', against Guizhou elsewhere)"

Line 7, uncounted:
- `order` = "Poduromorpha"
- `note`: "so the order field is left empty" -> "and the order is taken from the paper's Taxonomy section ('Order Poduromorpha Börner, 1913'; Collembola is the class)"

Line 5, uncounted:
- `conditions`: "the text does not say whether the 4.6-6.7% range covers all five (Table 2 gives holotype 4.7%, paratypes 4.6-6.7%)" -> "Table 2 gives holotype 4.7% and paratypes 4.6-6.7% (mean 5.3, SD 0.8), so the range covers all five types"

Line 3, uncounted:
- `note`: "The diagnosis line calls the holotype" -> "The holotype description also calls it"

Line 4, uncounted:
- `conditions`: "wild cave specimens" -> "wild cave specimens, collected from a pool at the end of an underground river about 200 m long"
