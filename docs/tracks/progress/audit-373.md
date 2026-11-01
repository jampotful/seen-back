# audit-373: desk-d283, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d283 files present untracked in the worktree (docs/tracks/progress/desk-d283.md and docs/views/evidence/desk-d283.jsonl, 7 lines; neither committed here, neither edited; the jsonl is identical to origin/research/desk-d283). Worktree HEAD and origin/main 14b92427 (Merge d282 after audit 372). `python3 -I tools/senses/check.py | grep 'd283\.'`: "docs/views/evidence/desk-d283.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 13, 9, 27, 19, 17, 32, 36, all within 40. Non-ASCII in quotes: four "–" in line 3 (two printed double en dashes "––"), as printed. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/works/ for all six DOIs (10.3897/zookeys.569.6921, 10.3897/subtbiol.42.79190, 10.3897/zookeys.960.53564, 10.3897/zse.99.89957, 10.3897/zookeys.931.47305, 10.3897/zookeys.829.30884; all answered); zookeys.pensoft.net/article/6921/download/xml/ (two passes); subtbiol.pensoft.net/article_preview.php?id=79190 (three passes); zookeys.pensoft.net/article/53564/download/xml/ (two passes); zse.pensoft.net/article/89957/download/xml/ (one pass); zookeys.pensoft.net/article/47305/download/xml/ (one pass); zookeys.pensoft.net/article_preview.php?id=30884 (one pass). Names: wsc.nmbe.ch/refincluded/13343, wsc.nmbe.ch/spec-data/61150 and 61151 (World Spider Catalog); wac.nmbe.ch/order/pseudoscorpiones/bibliography/taxonincluded/7266 (Pseudoscorpions of the World); chilobase.biologia.unipd.it/searches/result_subgenres/82 (ChiloBase); zoobank.org NomenclaturalActs eea2d1dd-... (genus-level act only, no species entry). Refused, not retried and not worked around: subtbiol.pensoft.net/article/79190/download/xml/ and zookeys.pensoft.net/article/30884/download/xml/ (PROVENANCE_REQUIRED, permission not answered); the same papers were then read on the publisher's article_preview pages, which a WebSearch returned. PMC, GBIF, WoRMS, Plazi, Zenodo, BHL, novataxa, myriatrix, DOAJ mirrors and library catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 9 WebSearches.

## Bibliographic and licence

- Lines 1, 2 (Wu, Wang, Zheng, Li 2016). Crossref: Guo Zheng, Shuqiang Li, Yi Wu, Chunxia Wang (order differs from print); title identical; ZooKeys 569, 23-35, no issue; issued 2016-02-24; CC BY 4.0 vor, delay 0; relation empty. Page byline Yi Wu, Chunxia Wang, Guo Zheng, Shuqiang Li; citation verbatim "Wu Y, Wang C, Zheng G, Li S (2016) Three new species of the genus Leptonetela from Greece (Araneae, Leptonetidae)." | "ZooKeys 569: 23–35. doi: 10.3897/zookeys.569.6921"; licence "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Printed order used, rightly. Accepted.
- Line 3 (Prado, Du Preez, Ferreira 2022). Crossref: Guilherme C. Prado, Gerhard C. Du Preez, Rodrigo L. Ferreira; title identical (leading byte-order mark in Crossref); Subterranean Biology 42, 125-138; issued 2022-03-18; CC BY 4.0 vor; relation empty. Page "Prado GC, Du Preez GC, Ferreira RL (2022)" | "Subterranean Biology 42: 125-138"; licence sentence as above. Accepted.
- Line 4 (Lee, Tomikawa, Min 2020). Crossref: Chi-Woo Lee, Ko Tomikawa, Gi-Sik Min; title identical to the record; ZooKeys 960, 1-15; issued 2020-08-17; CC BY 4.0 vor; relation empty. Page citation "Lee C-W, Tomikawa K, Min G-S (2020)" ZooKeys 960: 1–15 (tool summary with verbatim title); licence sentence as above. Accepted.
- Line 5 (Özbek, Aksu, Baytaşoğlu 2023). Crossref: Murat Özbek, İsmail Aksu, Hazel Baytaşoğlu; title identical; Zoosystematics and Evolution 99, journal-issue 1, 15-27; issued 2023-01-06; CC BY 4.0 vor; relation empty. Page (XML) has no formatted citation line; byline in the same order; licence sentence as above. Accepted.
- Line 6 (Pei, Ma, Liu, Lu, Hou 2020). Crossref same order; title identical; ZooKeys 931, 35-48; issued 2020-04-30; CC BY 4.0 vor; relation empty. Page "Pei S, Ma H, Liu H, Lu Y, Hou X (2020)" ... "ZooKeys 931: 35–48."; licence sentence as above. Accepted.
- Line 7 (Pei, Liu, Lu, Hou, Ma 2019). Crossref same order; title identical; ZooKeys 829, 1-13; issued 2019-03-11; CC BY 4.0 vor; relation empty. Page "Pei S, Liu H, Lu Y, Hou X, Ma H (2019) Lithobius (Ezembius) ternidentatus sp. n. (Lithobiomorpha, Lithobiidae)," | "a new species from China." | "ZooKeys 829: 1-13."; licence sentence as above. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Leptonetela paragamiani, L. arvanitidisi: World Spider Catalog, verbatim "Leptonetela paragamiani Wang & Li, 2016", "Leptonetela arvanitidisi Wang & Li, 2016", both "ACCEPTED", "Leptonetidae Simon, 1890"; references "Wang & Li, in Wu et al., 2016: 28" and ": 25" "Original description". Met. Leptonetidae in Araneae (paper title). The species authority (Wang & Li) differs from the byline; the record does not file an authority, so nothing to fix. The desk's "World Spider Catalog refused" is out of date (uncounted note fix below).
- Selachochthonius naledi: Pseudoscorpions of the World lists "Selachochthonius naledi" "Prado, Du Preez and Ferreira, 2022", family Pseudotyrannochthoniidae, order Pseudoscorpiones (tool summary); the paper prints "Family Pseudotyrannochthoniidae Beier, 1932" and "Genus Selachochthonius Chamberlin, 1929". The launch prompt's Chthoniidae is the older placement; the record's Pseudotyrannochthoniidae is right. Met.
- Pseudocrangonyx wonkimi: paper prints "Order: Amphipoda", "Family: Pseudocrangonyctidae Holsinger, 1989" (tool summary of headings); WoRMS refused by rule; ZooBank returned only the genus-level act. Accepted on the original description.
- Gammarus tumaf: paper's treatment headings "Order: Amphipoda", "Family: Gammaridae" (tool summary). No checklist opened (WoRMS refused). Accepted on the original description.
- Lithobius (Ezembius) varioporus and L. (E.) ternidentatus: ChiloBase subgenus page lists both under "Valid Species", "Lithobius (Ezembius) ternidentatus Pei, Liu, Lu, Hou, Ma, 2019" and "Lithobius (Ezembius) varioporus (Pei, Ma, Liu, Lu & Hou, 2020)"; "Order: Lithobiomorpha", "Family: Lithobiidae" (tool summary). Met.

Name faults 0.

## Duplicates

git grep on origin/main (14b92427) across the whole docs/ tree (evidence, audit/ALL.jsonl, audit/corrected, sheets, searched/, progress notes) for Leptonetela, Selachochthonius, Pseudocrangonyx, Gammarus tumaf, tumaf, Ezembius, Lithobius, varioporus, ternidentatus, paragamiani, arvanitidisi, naledi, wonkimi and the DOIs/article ids (zookeys.569, 6921, subtbiol.42, 79190, zookeys.960, 53564, zse.99, 89957, zookeys.931, 47305, zookeys.829, 30884): only unrelated matches ("naledi" inside the run-together word "operationaledit" in harvest-c8.md and harvest-c11.md; "6921" in docs/eval JSON numbers; "30884" not the DOI in audit-141.md; Lithobius forficatus and Chilopoda behaviour_vision/sense_chemical rows in ground-invertebrates, other species and traits; desk-d151/152/159 list Lithobius as searched without a record). No main row for any of the seven species. All 178 remote branches matching origin/research/desk-d2* or origin/research/audit-3*: hits only in research/desk-d283 itself. audit-3*.md hold-outs: none name these genera.

Duplicates 0.

## Trait keys and rulings

- eyes_count units: main files per-side counts with per-side units ("stemmata per side" 5 rows, "eyes per side" 2 rows, "ommatidia per side" 1 row), and ranges as two-number lists (cubozoan [10, 20] eyespots; eye_diameter_mm lists accepted in audit 370). Lines 6, 7 ([9, 10] and [5, 6], "ocelli per side") fit.
- eyes_count 0 vs eye_type "none": main holds eyes_count 0 rows for eyeless taxa (Polydesmida, Apheloria, Platydesmida, Geophilomorpha, Theatops, Nematostella vectensis in audit/ALL and audit/corrected) and eye_type "none (eyes absent)" rows. Line 2 (eyes_count 0, eyes absent) sits beside line 1's eyes_count 2 from the same sentence frame and follows the first use; lines 3, 4 file absence as eye_type "none (...)", the form audits 370 to 372 enforce for eye_type. Both keys are in use on main; not a fault.
- Attribution: lines 1, 2, 4 to 7 sit under single-species description headings (each paper, or each treatment, covers that one species); line 3's Discussion sentence names "the new species" in a paper describing one species (title), accepted as in audits 362 to 372.

## Per-record findings

### Line 1, Leptonetela paragamiani, eyes_count 2

Under the species' "Male (holotype)" description, verbatim: "Ocular area with a pair of setae, two eyes, reduced to white spots." Preceded by "Prosoma yellowish, with one seta on the median part."; followed by "Median groove, cervical groove and radial furrows indistinct." **Quote MATCH**, 13 words. Value 2 says no more than "two eyes". Types verbatim: "Holotype ♂ (IZCAS): GREECE, near Athens, Pan Cave, 38°08'48.54"N, 23°40'06.04"E," | "elevation 660 m, 7 April, 2013, S. Li leg." | "Paratypes 2 ♀ (IZCAS), same data as holotype." Diagnosis has no eye statement. Female description, verbatim: "Similar to male in color and general features but larger and with longer legs."; no ocular sentence. Abstract has no eye statement (tool summary). Conditions right (holotype-only basis stated).

Uncounted: the female paratype is "Similar to male in color and general features", which the conditions could record beside "their eyes are not described"; the World Spider Catalog now confirms the name.

**Line 1 MATCH.**

### Line 2, Leptonetela arvanitidisi, eyes_count 0

Under "Male (holotype)", verbatim: "Ocular area with a pair of setae, eyes absent." Preceded by "Prosoma yellowish, with one seta in the middle of the carapace."; followed by "Median groove, cervical grooves and radial furrows indistinct." **Quote MATCH**, 9 words. Types verbatim: "Holotype ♂ (IZCAS): GREECE, Athens, Attica, Leondari Cave, 37°59'14.61"N, 23°49'47.03"E," | "elevation 553 m, 28 March 2013, S. Li leg." | "Paratypes 2♀ (IZCAS), same data as holotype." Diagnosis has no eye statement (verified). Female, verbatim: "Similar to male in color and general features but larger and with shorter legs." Conditions right. L. penevi's male prints the same sentence (the desk left it out; no fault).

Uncounted: as line 1.

**Line 2 MATCH.**

### Line 3, Selachochthonius naledi, eye_type none

Discussion, subsection "Selachochthonius taxonomy and distribution in South Africa", verbatim in two abutting pieces: "The absence of eyes or eyespots –– a feature frequently attributed to subterranean-adapted species ––" | "is observed in the new species and in *S. cavernicola* (Lawrence 1935)." Preceded by a sentence ending "Ellingsen 1912; Beier 1955, 1964)."; ends seen. **Quote MATCH**, 27 words. Diagnosis verbatim "Selachochthonius naledi sp. nov. differs from other members of the genus by the following combination of characters:" ... "absence of eyes or eyespots"; carapace verbatim "absence of eyes or eyespots; epistome strongly dentate and saw-like". Type material: holotype female NCA 2021/1351, Villa Louisa cave, "09 October 2019"; paratype male NCA 2021/1352, Yom Tov Cave, "17 October 2019", R.L. Ferreira (tool summary with verbatim dates). Habitat verbatim: "The two individuals were collected from under block rocks in the cave floor."; method verbatim "All invertebrates were collected with a fine brush and stored in 70% ethanol." The description covers both sexes with ranges (tool summary). Conditions right; family right (see Names).

Uncounted: "hand-collected" can read "collected with a fine brush", as printed.

**Line 3 MATCH.**

### Line 4, Pseudocrangonyx wonkimi, eye_type none (eyes absent)

"Description." "Female (NNIBRIV35119, 8.9 mm).", Head sentence verbatim in two abutting pieces: "Head (Fig. 2) without setae; rostrum short; lateral cephalic lobe rounded; antennal sinus shallow with rounded angle;" | "eyes absent." Followed by a sentence beginning "Pereonites 3–5". **Quote MATCH**, 19 words. Diagnosis lists "eyes absent;"; Remarks "eyes completely absent" (verbatim pieces). Type material: holotype female 8.9 mm, paratypes one male (8.3 mm; heading "Male (NNIBRIV36158, BL = 8.3 mm).") and one female, Jungchangjin Cave, 17 February 2017, Yong Gun Choi; Methods "were collected from the groundwater of Jungchangjin Cave" | "using a fine-meshed hand net"; 99% ethanol (tool summary). Male description opens at antenna 1, no eye statement. Conditions right.

**Line 4 MATCH.**

### Line 5, Gammarus tumaf, eye_type small ovoid

"Description of holotype male.", Head, verbatim: "Eyes small, ovoid; shorter than the diameter of the first peduncular segment of antenna 1 (Fig. 1d)." First sentence of the paragraph; next paragraph (Antennae) opens on antenna 1 length (tool summary). **Quote MATCH**, 17 words, figure reference kept. Variability verbatim: "In some individuals, the size of the eyes is slightly smaller than in the holotype." (in the note). Diagnosis verbatim: "A medium-large species with a smooth body, lacking body pigmentation, minute eyes,". Type material: holotype male 12.6 mm ESFM-MALI/20-10, 03.ix.2020, M. Elverici; paratypes 3 males, 3 females; "sampled with the help of a hand aspirator" (tool summary with verbatim pieces). Female description has no eye statement. Value says no more than the quote. Conditions right.

Uncounted: the Diagnosis's "minute eyes" (species level) could be added to the note; the tool remarks that Fig. 1 is the habitus/locality figure, so "(Fig. 1d)" may be a misprinted figure reference in the paper (kept as printed, rightly).

**Line 5 MATCH.**

### Line 6, Lithobius (Ezembius) varioporus, eyes_count [9, 10] per side

"Description.", cephalic plate, verbatim in two abutting pieces: "Nine to ten approximate oval ocelli on each side (Figs 2, 3), domed, translucent, usually darkly pigmented," | "situated in three irregular rows; the posterior two ocelli comparatively large; others subequal in size." Preceded by the sentence ending "the middle of the posterior edge is very slightly concaved forward (Fig. 1)."; followed by "Tömösváry's organ situated at anterolateral margin of the cephalic plate, slightly smaller than the adjoining ocelli". **Quote MATCH**, 32 words. Diagnosis verbatim "9–10 ocelli on each side of the head, arranged in three irregular rows, posterior two comparatively large ocelli." Type material: holotype male 19.1 mm, Heiyagou Village, Fuping County, Hebei, 5 August 2014, S. Pei and H. Ma; paratypes 13 females, 19 males; "All specimens were hand-collected under leaf litter or stones." No left/right, sex or size statement on ocelli (tool summary). Conditions right.

Uncounted: "Other material" adds 26 females and 32 males (Liaodaobei) and 20 females and 21 males (Wuyuezhai Mountain); the plectrotaxy tables rest on 59 females and 73 males, i.e. the whole series (tool summary), and the text does not say which specimens the 9 to 10 rests on. The conditions could list the other material.

**Line 6 MATCH.**

### Line 7, Lithobius (Ezembius) ternidentatus, eyes_count [5, 6] per side

"Description", cephalic plate, verbatim in three abutting pieces: "Five or six oval to rounded ocelli on each side (Fig. 1B), most of them rounded, domed, translucent," | " usually darkly pigmented, situated in two irregular rows;" | " the posterior two ocelli comparatively large; others subequal in size." Neighbouring sentences on the lateral marginal ridge and on Tömösváry's organ (tool summary). **Quote MATCH**, 36 words. Diagnosis verbatim "5–6 ocelli on each side of head, arranged in two irregular rows, posterior two ocelli comparatively large;". Discussion verbatim "with five or six ocelli in new species instead of eight ocelli in L. (E.) multispinipes". Type material: holotype female, Wuyuezhai Mountain, Lingshou County, Hebei, 480 m, 28 September 2014, S. Pei and H. Ma; paratypes 33 females, 38 males, same data; other material 9 females, 6 males, Shanyanggou, 7 September 2014 (tool summary); method verbatim "All specimens were hand-collected under leaf litter or stones." No left/right or sex statement on ocelli. Conditions right.

Uncounted: the note's "Methods wording not read" can now be replaced by the Methods sentence; the other material could be listed.

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Leptonetela paragamiani, eyes_count 2 | MATCH | none | quote MATCH (13), holotype male; WSC accepted |
| 2 | Leptonetela arvanitidisi, eyes_count 0 | MATCH | none | quote MATCH (9), holotype male; WSC accepted |
| 3 | Selachochthonius naledi, none | MATCH | none | Discussion sentence MATCH (27); Pseudotyrannochthoniidae confirmed |
| 4 | Pseudocrangonyx wonkimi, none (eyes absent) | MATCH | none | quote MATCH (19), holotype female |
| 5 | Gammarus tumaf, small ovoid eyes | MATCH | none | quote MATCH (17), holotype male; variability in note |
| 6 | L. (E.) varioporus, 9-10 per side | MATCH | none | quote MATCH (32); ChiloBase valid |
| 7 | L. (E.) ternidentatus, 5-6 per side | MATCH | none | quote MATCH (36); ChiloBase valid |

Errors 0 of 7 audited records (0%), within the 5% bar; none held out. By kind: quotes 0; value exceeding quote 0; sample composition 0; bibliographic 0; licence 0; names 0; filing convention 0; duplicates 0 against main, all 178 desk-d2* and audit-3* branches and the audit-3* hold-outs. Verdict: pass; merge with the uncounted fixes below at the owner's choice.

Unchecked: checklist entries for Pseudocrangonyx wonkimi and Gammarus tumaf (WoRMS refused by rule; ZooBank gave only the genus act); the World Spider Catalog pages for L. paragamiani and L. arvanitidisi were read but not their later-reference lists beyond the original description; the two refused XML URLs (subtbiol 79190, zookeys 30884) were not reopened, so lines 3 and 7 rest on the publisher's article_preview pages; the sentences around line 7's quote and the Gammarus Antennae sentence, the type-material details of lines 3 to 7 and the Lithobius specimen basis rest partly on tool summaries; Fig. 1 of the Gammarus paper not checked.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). All changes uncounted.

Lines 1 and 2 (same strings in each line):
- `note`: "not checked against the World Spider Catalog (its page refused)" -> "World Spider Catalog lists it as accepted (authority Wang & Li, 2016, in Wu et al. 2016, original description)"
- `conditions`: "(2 female paratypes; their eyes are not described)" -> "(2 female paratypes; their eyes are not described, the female description saying only 'Similar to male in color and general features')"

Line 3:
- `conditions`: "hand-collected from cave floor under block rocks" -> "collected with a fine brush from under block rocks in the cave floor"

Line 5:
- `note`: "Family and order from the paper's title; no checklist opened." -> "The Diagnosis says 'minute eyes'. Family and order from the paper's title and treatment headings; no checklist opened."

Line 6:
- `conditions`: "paratypes 13 females and 19 males;" -> "paratypes 13 females and 19 males; other material 26 females and 32 males (Liaodaobei) and 20 females and 21 males (Wuyuezhai Mountain), the text not saying which specimens the ocelli count rests on;"

Line 7:
- `conditions`: "paratypes 33 females and 38 males;" -> "paratypes 33 females and 38 males; other material 9 females and 6 males (Shanyanggou, 7 September 2014);"
- `note`: "Wild-collected statement for this paper: specimens found under litter; Methods wording not read." -> "Methods: 'All specimens were hand-collected under leaf litter or stones.'"
