# audit-393: desk-d301, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d301 files present untracked in the worktree (docs/tracks/progress/desk-d301.md and docs/views/evidence/desk-d301.jsonl, 7 lines; neither committed here, neither edited). Line numbers are the file's (1-based). HEAD equals origin/main (9c8063f4). `python3 -I tools/senses/check.py | grep 'd301\.'`: "docs/views/evidence/desk-d301.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 8, 12, 16, 16, 21, 3, 20, all within 40; non-ASCII characters only µ (lines 3, 4, 5), the en dash (line 5), ± and μ (line 7).

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article/91147/download/xml/; zookeys.pensoft.net/article/6603/download/xml/ (two passes) and zookeys.pensoft.net/article_preview.php?id=6603 (Tables 1, 3); europeanjournaloftaxonomy.eu/index.php/ejt/article/download/526/1179; zookeys.pensoft.net/article_preview.php?id=72964; Crossref single-DOI lookups api.crossref.org/v1/works/ for all five DOIs. No journals.plos.org URL came back from three searches for the Pectinereis paper (results: aggregators, news pages, DOAJ, an academia.edu profile, which was not opened), so the PLoS ONE page was not read. Plazi, DOAJ, bionames, Zenodo and repository copies were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 10 WebSearches.

## Bibliographic and licence

- Line 1 (Villalobos-Guerrero, Huč, Tilic, Hiley, Rouse 2024). Crossref: Tulio F. Villalobos-Guerrero, Sonja Huč, Ekin Tilic, Avery S. Hiley, Greg W. Rouse; title identical; PLOS ONE 19(3): e0297961; issued 2024-03-06; CC BY 4.0 vor. The publisher page was not reached, so the page byline, the page licence sentence and the quote could not be checked. Held out (rules: a record whose page the auditor cannot open is held out).
- Line 2 (Yang, Min 2023). Page and Crossref Hee-Min Yang, Gi-Sik Min; title identical; ZooKeys 1141: 185-199, no issue; issued 2023-01-23; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Lines 3, 4 (Pilato, Lisi 2016). Page and Crossref Giovanni Pilato, Oscar Lisi; title identical; ZooKeys 580: 1-12; issued 2016-04-12; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Lines 5, 6 (Atherton, Jondelius 2018). Page and Crossref Sarah Atherton, Ulf Jondelius; title identical; European Journal of Taxonomy 398, pages 1-18 printed (Crossref gives no pages); issued 2018-01-25; Crossref CC BY 3.0 content-version unspecified; page prints "This work is licensed under a Creative Commons Attribution 3.0 License." Accepted under the "unspecified + page-printed" rule. The journal field omits the printed pages (audit-392 line 7 form "European Journal of Taxonomy 342: 1-21"); uncounted fix below.
- Line 7 (Shi, Zeng, Wang, Zhang, Deng, Wang 2022). Page and Crossref Yongshi Shi, Zhiyu Zeng, Jia Wang, Siyu Zhang, Li Deng, Antai Wang; title identical; ZooKeys 1099: 1-28; issued 2022-05-03; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.

Bibliographic faults 0 on the lines read; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All seven species are described as new in the cited papers; names rest on the original descriptions (no checklist opened). Higher taxa as printed:
- Line 2: "Phylum Rotifera Cuvier, 1817", "Class Eurotatoria De Ridder, 1957", "Subclass Monogononta Plate, 1889", "Order Ploima Hudson & Gosse, 1886", "Family Notommatidae Hudson & Gosse, 1886". The record leaves order and class empty although both are printed, and its note says only "Family and subclass as printed". Counted with line 2.
- Lines 3, 4: Milnesiidae, Eutardigrada, Apochela in the title; filed right (order Apochela, class Eutardigrada).
- Lines 5, 6: Macrostomorpha, Microstomidae in the title; filed as order Macrostomorpha (the desk convention for this group), family Microstomidae. Accepted.
- Line 7: the paper prints "Family Macrostomidae Beneden E, 1870" above Macrostomum (tool summary for the head text); the record leaves family empty. Counted with line 7.

## Trait keys

eye_type (lines 1, 3, 4, 5, 6) and eyes_count (lines 2, 7) are on main; no new key. Trait-key faults 0.

## Duplicates

`git grep -il` on origin/main (9c8063f4) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for strickrotti, binoculata, "Milnesium minutum", sandrae, laurae, edmondi, "Macrostomum littorale" and the five DOI strings: one hit only, binoculata in docs/views/gaps/try-species.json (a gap list of species to try, not a filed value). The 94 remote desk-d250 to d399 and audit-350 to 399 branches (desk-d301 excluded) grepped under docs/views and docs/tracks/progress for the same strings: hits only in docs/views/gaps/try-species.json (the same gap list); a rerun excluding docs/views/gaps returned no hit. Duplicate faults 0.

## Per line

### Line 1, Pectinereis strickrotti, eye_type "none (eyes and lens absent)"

Crossref confirms authors, title, volume 19, issue 3, article e0297961 and CC BY 4.0 vor. The PLoS ONE article page did not appear in any WebSearch result (three searches), and the desk's own URL cannot be fetched without that provenance. The quote, the type material, the claim that the genus description repeats the sentence and the claim that Abstract, Diagnosis and Discussion are silent on eyes are all unchecked. **Line 1 HOLD OUT** (page not opened). It may return in a later unit or audit once a searchable journals.plos.org URL is found.

### Line 2, Cephalodella binoculata, eyes_count 2 eyespots

Description: "Two distinct red eyespots located in front of the head (Fig. 3C)." **Quote MATCH**; next sentence "Distance between the two eyespots far and clear." Abstract "distinguished by having two frontal eyespots"; Differential diagnosis "(1) the new species has two distinct eyespots, whereas C. carina has one small eyespot;" and "(3) the new species has two eyespots, while C. graciosa has one eyespot;"; Etymology "bi, meaning "two" and oculata, meaning "eyed"". Count is the total (two frontal), right. Holotype "1 female, glycerol permanent slide, NIBRIV0000896982."; paratypes "2 female, glycerol permanent slides, NIBRIV0000896983, NIBRIV0000896984" plus an SEM trophi preparation (NIBRIV0000896985); soil, Incheon, 19 June 2019; "Total length 134–155 μm"; animals brought "alive" and anaesthetised with bupivacaine "Before the observation and preservation of living rotifers". Method and conditions right.

Fault: order "Ploima" and class "Eurotatoria" are printed and left empty (see Names). Fixable.

**Line 2 FIXABLE.**

### Line 3, Milnesium minutum, eye_type "eyespots present"

Description of the holotype: "Body colourless, 288 µm long; cuticle smooth without pseudopores, reticulum, tubercles or gibbosities; eye spots present." **Quote MATCH**; heading "Description of the holotype" under M. minutum. Specific diagnosis "colourless; cuticle smooth; eye spots present"; Differential diagnosis "The new species clearly differs from Milnesium barbadosense by having eyes." (a comparison, not used, rightly). No count printed, so "present" without a count is right. Methods: "All studied specimens were mounted in polyvinyl lactophenol." and phase contrast at x100; the eye spots are thus reported from mounted specimens, and the paper says nothing about live animals or loss of pigment in mountant; "slide-mounted" in the method is right (uncounted addition of the mountant below). Holotype and paratype slide 4127 (Moio Alcantara), paratype slide 3238 (Noto); "Eggs not found."

Fault: the conditions say "developmental stage not stated" but omit what the paper does say about stage. Differential diagnosis: "considering the body size, it was necessary to determine whether they were three young specimens of" M. asiaticum, and the authors conclude they "were not young examples of Milnesium asiaticum but, independent of body size, belonged to a distinct species."; Abstract "The body size of Milnesium minutum is the smallest of the known species of the genus." Table 1 gives the slide-4127 paratype as 284 µm and the Noto paratype as "?" (tool summary of the row). The record must give the size of the whole type series and the juvenility question, since three very small specimens are the whole basis. Fixable.

**Line 3 FIXABLE.**

### Line 4, Milnesium sandrae, eye_type "eyespots present"

Description of the holotype: "Body 567 µm long, colourless, cuticle smooth without pseudopores, reticulum, tubercles or gibbosities; eye spots present." **Quote MATCH**; heading "Description of the holotype" under M. sandrae. Specific diagnosis "Colourless; cuticle smooth; eye spots present"; Differential diagnosis has no eye statement (tool summary), so no comparison sentence was taken. Holotype slide 4290 and "16 paratypes (slides Nos. 4268, 4288–4290; 4293)", Hawai'i Island, 1994; Table 3 measures the holotype and three paratypes, body length 401, 504, 522 and 567 µm; Remarks "The paratypes are similar to the holotype in both qualitative and quantitative characters (Table 3)."; mounted in polyvinyl lactophenol (Methods). All as filed.

**Line 4 MATCH.**

### Line 5, Microstomum laurae, eye_type "paired red eyespots"

Description: "Paired red eyespots approximately 43 µm long and present in the lateral margins of the body level with brain (Fig. 1A–B)." **Quote MATCH.** Diagnosis "Paired red eyespots 43 µm long and located in the lateral margins at level of the brain."; Abstract "paired lateral red eyespots located level with the brain"; Remarks "the eyespots of M. laurae sp. nov. are red", "whereas they are level with the brain in M. laurae sp. nov." and "there are no pigment cells apart from the eyespots" (all on M. laurae, not a congener). Holotype SMNH-Type-8903 and additional SMNH-Type-8904, both vegetative, Strömstad, Saltö; "two vegetative zooids", 760 µm; "Reproductive system unknown." Methods: animals documented by micrographs and video, then "fixed in 95% ethanol". All as filed.

**Line 5 MATCH.**

### Line 6, Microstomum edmondi, eye_type "none (no pigmented eyes)"

Description: "Pigmented eyes absent." **Quote MATCH**; the Diagnosis carries the identical sentence; Remarks "both lack eyespot pigmentation" (M. edmondi and M. ulum); Abstract and Discussion silent on eyes. Holotype male SMNH-Type-8890, Fiskebäckskil; additional material "2 ♂♂, 5 vegetative, same data as holotype" (SMNH-Type-8891–8897) and "3 ♀♀, 1 ♂, 1 vegetative, Munkedal" (SMNH-Type-8898–8902).

Faults:
1. The value "none" asserts eyelessness; the quote says only that pigmented eyes are absent, and the record's own note says it "states absence of pigmented eyes only, not of any photoreceptor". The value says more than the quote. Fixable.
2. The conditions place all material at Fiskebäckskil by omission; five of the twelve additional specimens come from Munkedal. The species Description also does not say whether the eye statement rests on live or fixed animals (Methods: documented alive, then fixed in ethanol), which the record should state for an absence-of-pigment claim. Fixable (counted with fault 1 as one record error).

**Line 6 FIXABLE.**

### Line 7, Macrostomum littorale, eyes_count 2 eyes

Description: "Two round eyes, separated from each other by a distance of 37 ± 6.1 μm (n = 6) (Fig. 3A)." **Quote MATCH**; only the count is logged. Diagnosis "A Macrostomum species with dorsoventrally flattened body, two almost round eyes, and rounded rostrum (Fig. 3A)."; Abstract, Remarks and Discussion silent on eyes (tool summary). Holotype IZCAS PLA–Ma0140 whole-mounted in neutral balsam; paratype IZCAS PLA–Ma0141 serially sectioned; Waterlands Resort, Pearl River estuary, Shenzhen, April 2018; "Mature individual 920 ± 109 μm in length".

Faults:
1. `family` empty although "Family Macrostomidae" is printed (see Names). Fixable.
2. The conditions omit the five non-type specimens (IZCAS PLA–Ma0140a-e) photographed "in vivo", which with the holotype make up the n = 6 behind the eye spacing; the method "(whole mounts)" thus understates the live observations. Fixable (counted with fault 1 as one record error).

**Line 7 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Pectinereis strickrotti, eyes and lens absent | HOLD OUT | | PLoS ONE page not reachable from search results; quote unchecked |
| 2 | Cephalodella binoculata, 2 eyespots | FIXABLE | order, class, note | Ploima and Eurotatoria printed but left empty |
| 3 | Milnesium minutum, eyespots present | FIXABLE | conditions | juvenility question and paratype size omitted |
| 4 | Milnesium sandrae, eyespots present | MATCH | | quote, type series and Table 3 lengths right |
| 5 | Microstomum laurae, paired red eyespots | MATCH | | quote, two vegetative specimens, Remarks on this species |
| 6 | Microstomum edmondi, no pigmented eyes | FIXABLE | value, conditions | "none" says more than "Pigmented eyes absent"; Munkedal material and live/fixed basis omitted |
| 7 | Macrostomum littorale, 2 eyes | FIXABLE | family, method, conditions | Macrostomidae printed but left empty; five in-vivo non-type specimens omitted |

Errors: 5 of 7 records (71%); 4 fixable (lines 2, 3, 6, 7), 1 held out (line 1, page not opened). Verdict: **ACCEPT AFTER REPLACEMENT, LINE 1 HELD OUT** (lines 4, 5 as filed; lines 2, 3, 6, 7 with the replacements below; line 1 not merged).

## Replacement

Each old string is copied from the desk file and occurs once in its field in the line named.

Line 2:
- `order`: "" -> "Ploima"
- `class`: "" -> "Eurotatoria"
- `note`: "Family and subclass as printed in the title/keywords." -> "Class Eurotatoria, Subclass Monogononta, Order Ploima and Family Notommatidae as printed in the classification heads."

Line 3:
- `conditions`: "developmental stage not stated; eggs not found" -> "paratype on slide 4127 284 um long, the Noto paratype not measured; developmental stage not stated, but the Differential diagnosis asks whether the three small specimens were young Milnesium asiaticum and concludes they were not, 'independent of body size' (the Abstract calls M. minutum the smallest species of the genus); eggs not found"

Line 6:
- `value`: "none (no pigmented eyes)" -> "pigmented eyes absent"
- `conditions`: "plus additional material (3 females, 3 males and 6 vegetative specimens in all; no paratypes designated)" -> "plus additional material from Fiskebackskil (2 males, 5 vegetative) and Munkedal (3 females, 1 male, 1 vegetative), 12 specimens in all; no paratypes designated; the Description does not say whether the eye statement rests on live or fixed animals (Methods: specimens documented alive, then fixed in 95% ethanol)"

Line 7:
- `family`: "" -> "Macrostomidae"
- `method`: "morphological description of mature worms (whole mounts)" -> "morphological description of mature worms (live non-type specimens photographed in vivo; holotype whole mount, paratype serial sections)"
- `conditions`: "mature worms measured n = 6, 920 +/- 109 um long" -> "mature worms measured n = 6, 920 +/- 109 um long; five further non-type specimens (IZCAS PLA-Ma0140a-e) photographed in vivo"

Lines 5 and 6 (uncounted):
- `source.journal`: "European Journal of Taxonomy 398" -> "European Journal of Taxonomy 398: 1-18"

Lines 3 and 4 (uncounted):
- `method`: "morphological description of slide-mounted type specimens" -> "morphological description of type specimens mounted in polyvinyl lactophenol (phase contrast); the paper says nothing on eye spots in live animals"

Line 7 (uncounted):
- `note`: "Species described as new in this paper; no checklist opened." -> "Species described as new in this paper; no checklist opened. Family Macrostomidae from the paper's classification head."
