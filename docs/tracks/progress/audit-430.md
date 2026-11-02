# audit-430: desk-d319, all 8 evidence lines

Audited 1 November 2026 from the desk-d319 files present untracked in the worktree (docs/tracks/progress/desk-d319.md and docs/views/evidence/desk-d319.jsonl, 8 lines; neither committed here, neither edited). HEAD equals origin/main (de75597ad). `python3 -I tools/senses/check.py | grep d319`: "docs/views/evidence/desk-d319.jsonl: 8 records, 0 problems". Quote lengths (`len(q.split())`): 38, 29, 28, 22, 34, 29, 15, 3, all within 40. `eyes_count` is a check.py trait key; `eye_diameter_mm` is not in check.py but is used on main (desk-d280, d291, d292, d306, oa-1), and line 3's note carries "new trait".

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article/5251/download/xml/ (two passes), www.mdpi.com/2079-7737/15/4/363 (three passes), zookeys.pensoft.net/article/14885/download/xml/ (three passes), zookeys.pensoft.net/article/2409/download/xml/ (two passes), zookeys.pensoft.net/article/26862/download/xml/ (one pass), en.wikipedia.org/wiki/Mantophasmatidae and sealifebase.ca species pages for Paralovenia yongalensis and Melicertissa antrichardsoni (names only). Crossref single-DOI lookups (api.crossref.org/v1/works/) for all four DOIs, each read on the first call. mantophasmatodea.speciesfile.org redirected to misc.speciesfile.org, which was refused (PROVENANCE_REQUIRED) and not retried; species.wikimedia.org failed; the Plazi treatment page returned only a redirect notice. WoRMS was not opened (on the desk's refused list). PMC, DOAJ, library catalogues (lib.cas.cz, utm.my, uitm.edu.my, uv.mx, ufrj.br), core.ac.uk, zenodo, BHL and reviewer.ly were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 11 WebSearches.

## Bibliographic and licence

- Line 1 (Toshino, Miyake, Shibata 2015). Citation line "Toshino S, Miyake H, Shibata H (2015) Meteorona kishinouyei, a new family, genus and species" ... "(Cnidaria, Cubozoa, Chirodropida) from Japanese Waters."; Crossref same authors in order, same title, ZooKeys 503, 1-21, issued 2015-05-11, CC BY 4.0 vor. Page prints the CC BY 4.0 sentence. Accepted.
- Lines 2 and 3 (Liu et al. 2026). The page byline is cut: "Wanjie Liu, Jun Li, Zhen Zhao, Jinkuan Wei, Jingyue Huang, Qisheng Zheng, Yanping Qin, Haitao Ma, Ziniu Yu … Yuehuan Zhang"; the page carries no expanded list or citation string (tool summary: only one citation_author meta tag). The visible printed names agree with Crossref's 11 in order, and the Author Contributions statement prints eleven sets of initials including "Y.P." and "Y.Z."; the one hidden name (Ying Pan) is Crossref's, placed tenth as in Crossref. Accepted, since the page prints no other order. Title identical; "Biology 2026, 15(4), 363"; Crossref 15, issue 4, page 363, issued 2026-02-21, CC BY 4.0 vor. Page: "This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license." Accepted.
- Line 4 (Wipfler, Theska, Predel). **Year fault.** The Citation line prints "Wipfler B, Theska T, Predel R (2017) Mantophasmatodea from the Richtersveld in South Africa" ... "ZooKeys 746: 137–160."; collection year 2018, epub 27 March 2018, Crossref issued 2018-03-27. Under the owner ruling (rules.md FORMAT: printed year wins over Crossref issued year) the record must carry 2017; it files 2018. Authors, title and ZooKeys 746: 137-160 match the page and Crossref; CC BY 4.0 sentence on the page, Crossref CC BY 4.0 vor. Licence accepted.
- Lines 5 and 6 (Wipfler, Pohl, Predel 2012). The XML prints no Citation line for this article; pub-date collection 2012, epub 20 January 2012; Crossref same authors in order, title identical, ZooKeys 166, 75-98, issued 2012-01-20, CC BY 3.0 vor. Page: "Creative Commons Attribution License 3.0 (CC-BY)". Accepted.
- Lines 7 and 8 (Uribe-Palomino, Pausina, Gershwin 2018). Citation line "Uribe-Palomino J, Pausina S, Gershwin L-a (2018)" (tool rendering of the last initial; the record's "L-A" is not counted), ZooKeys 783: 17-36; Crossref same order, issued 2018-09-03, CC BY 4.0 vor; page CC BY 4.0 sentence. Accepted.

Bibliographic faults: 1 (line 4 year). Licence faults: 0. source.access "open" right throughout.

## Names and higher taxa

- Meteorona kishinouyei: Results heading prints "Class Cubozoa Werner, 1973"; Chirodropida and Chiropsellidae printed. WoRMS not opened (refused list); the name is the original description and nothing seen contradicts it.
- Tridacna maxima, T. squamosa: the Introduction prints "Class Bivalvia, Order Venerida, Family Tridacnidae", as filed. Main files Tridacna under Cardiidae, Cardiida (sea-invertebrates, canon-3, methods); the printed placement is what the record must carry, so not counted, but the merger may want to note the difference.
- Kuboesphasma compactum: the classification block prints "Animalia", "Notoptera", "Mantophasmatidae"; "Insecta" appears nowhere in the article (tool summary), so class blank is right. Family Mantophasmatidae agrees with the current scheme (Wikipedia, Mantophasmatidae: tribe Austrophasmatini in Mantophasmatinae holds Kuboesphasma and Striatophasma; Pachyphasma in Mantophasmatini); the text itself places Kuboesphasma inside "the remaining Austrophasmatidae" phylogenetically. Order "Notoptera" is printed, so not counted; lines 5 and 6 and the title use Mantophasmatodea (optional fix below for consistency).
- Striatophasma naukluftense, Pachyphasma brandbergense: title prints Insecta and Mantophasmatodea. The note's "the text assigns no family to Striatophasma itself" is slightly off: the genus "Description and diagnosis" says it "is placed as sistergroup to all remaining South African" Austrophasmatidae (tool summary for the last word). Family Mantophasmatidae stands as the current placement. Optional note fix.
- Melicertissa antrichardsoni (Family LAODICEIDAE Agassiz, 1862, under Order LEPTOTHECATA) and Paralovenia yongalensis (Family LOVENELLIDAE Russell, 1953) as printed; SeaLifeBase lists both as Hydrozoa, Leptothecata, with the same families and no synonyms. WoRMS not opened.

## Repeats

`git grep -il` on origin/main over the whole docs/ tree for Meteorona, zookeys.503.9047, Tridacna, biology15040363, Kuboesphasma, zookeys.746.14885, Striatophasma, Pachyphasma, zookeys.166.1802, antrichardsoni, Paralovenia, zookeys.783.26862. Hits only for Tridacna: genus-level lambda_max_nm/receptor_classes rows (canon-3, oa-1, audit/corrected/methods), and **Tridacna maxima on main** in docs/views/audit/corrected/sea-invertebrates.jsonl (eyes_count "several hundred pinhole eyes on the exposed mantle", acuity_cpd, acceptance_deg; Land 2003, Proc R Soc B 270(1511): 185-188), with the same in audit/ALL.jsonl and sheets/sealife.md. Line 2 is a different paper and a juvenile hatchery count, and it agrees with the Land value, so by the rule of earlier audits (different paper, agreeing finding) it does not repeat main. Line 2's note, however, says "Tridacna rows on main are lambda_max_nm book rows", which misses the T. maxima eyes_count row (fix below). T. squamosa is not on main. Unmerged origin/research/desk-d* branches (319, not merged into main): each branch's docs/views/evidence/desk-dN.jsonl and docs/tracks/progress/desk-dN.md read with one `git cat-file --batch` and grepped for the same 12 patterns: hits only in desk-d319 itself.

## Per line

### Line 1, Meteorona kishinouyei, six eyes per rhopalium

Description: "Each of the four rhopalia bearing a set of six eyes, with the two median possessing prominent" / "lenses and the four lateral ones adjacent to the lens eyes being pigment pits and slit (Fig. 6I–K, Fig. 7G, H)." Previous sentence "Subumbrellar rhopalial windows flat (Fig. 6H)."; next "A single broad bean shaped statolith located behind each complex eye (Fig. 6I–K)." **Quote MATCH**, 38 words, whole telegraphic sentence, figure references kept. Material examined: "Holotype: NSMT-Co1572. Eastern Japan, Fukushima Prefecture, Souma, Matsukawa-ura," "37°48'39.3"N, 140°58'3.3"E, 14 October 2013, collector: Ko Tomikawa, one adult male."; paratypes "NSMT-Co1568, 1569, 1570 ... Enoshima, Shonan Port, 35°18'4.75"N, 139°28'61.0"E, 23 August 2011, collector: Haruka Shibata, one adult female." and "NSMT-Co1571 ... Onahama Port ... 18 October 2013, collector: Shun Ishikawa, one adult female." Table 3 (tool summary): NSMT-Co1572 female, 1568 male, 1569 and 1570 female, 1571 female. The conditions state both disagreements as printed (holotype male in text vs female in Table 3; NSMT-Co1568 male in Table 3). Figure 6 "Meteorona kishinouyei sp. n., holotype." and Figure 7 "... holotype." as stated. Family and genus Diagnoses mention only "Sensory niches U-shaped ..." on the rhopaliar scale, no eyes; no species Diagnosis. Value says no more than the quote.

**Line 1 MATCH.**

### Line 2, Tridacna maxima, 221 eyes per individual

Results 3.1, in order: "Regarding ocular parameters (Figure 3), significant interspecific variations were observed" "in the total number of eyes per individual." then "Specifically, T. maxima exhibited the highest eye count (221 ± 8), which was significantly higher than" "T. crocea (75 ± 11) and T. squamosa (60 ± 8) (p < 0.001)."

Fault: **quote starts mid-sentence.** The printed sentence begins "Specifically,"; the record drops that word with no cut mark (the note admits the preceding text was not read). With the word restored the quote is 30 words, still within 40. Second, the note's repeat statement is wrong ("Tridacna rows on main are lambda_max_nm book rows"; main has T. maxima eyes_count from Land 2003, see Repeats). Value, units ("total number of eyes per individual"), method ("For counting the number of eyes, 30 individuals were randomly selected from each species," "and the number of eyes present on the left and right mantles was tallied independently."), state ("All specimens were obtained from hatchery-reared populations in Sanya City of Hainan Province in China."; "The one-year-old individuals"), shell lengths (27.69 ± 3.16, 39.54 ± 3.62, 34.61 ± 4.48 mm, in Results 3.1) and lens absence ("None of the three species possesses differentiated lenses") all right. The Discussion's "eye number is a genetically fixed trait specific to each species, rather than being driven by differences in shell length" is carried. One record error, fixable.

**Line 2 FIXABLE.**

### Line 3, Tridacna squamosa, eye diameter 0.490 mm

Results 3.1, in order: "Distinct variation in eye diameter per individual was observed among the 3 giant clams." "T. squamosa exhibited significantly larger eye diameters compared to the other species." "In contrast, T. crocea and T. maxima showed no significant difference in this trait." "Specifically, T. squamosa (0.490 ± 0.099 mm) was significantly larger than both T. crocea (0.285 ± 0.061 mm) and T. maxima (0.303 ± 0.057 mm) (p < 0.001)." **Quote MATCH**, whole sentence, 28 words. Method: "To determine eye diameter and pupil size, we examined 5 randomly chosen individuals per species using a stereomicroscope", "Subsequently, 6 eyes were randomly sampled from each individual.", "Microscopic images were acquired and processed using Leica Application Suite V4.6 software". Abstract "T. squamosa the largest mean eye diameter (0.490 ± 0.082 mm)" against Results ± 0.099: carried. Same state as line 2.

**Line 3 MATCH.**

### Line 4, Kuboesphasma compactum, eyes prominent, ocelli absent (male)

Description male, Head: "Compound eyes prominent, tapered ventro-mesally, about 1.5 times as long as high;" + "interoccular distance ca. the length of one eye, ocelli absent." Previous "Head (Fig. 4): globular, orthognathous, posteriorly covered by pronotum, green without darker stripe; compound eyes whitish with black or brown spots; head slightly wider than prothorax, about twice as wide as long; head capsule covered with setae, setation increasing dorsally."; next "Coronal and frontal suture indistinct, pleurostomal ridge well developed." **Quote MATCH**, 22 words. Female "Head (Fig. 7): compound eyes slightly smaller than in the male." Types: "Male. SOUTH AFRICA: Kuboes, S28°26'25", E16°59'44", 18.viii.2012, 250 m, R. Predel, specimen in ethanol." (SAMC); "four males and two females, specimens in ethanol." (SAMC, ZFMK, ZMBN): as in conditions.

Faults (one record error, fixable): (a) **year** 2018 filed against a printed 2017 (see Bibliographic). (b) **Diagnosis wording on eyes misreported.** The conditions say "The genus-level Description and diagnosis have no eye wording"; the genus "Description and diagnosis" prints "Additionally, the head capsule is distinctly broader on the level of the compound eyes than on the level of the genae" " in Minutophasma while they are equal in Kuboesphasma." It is a head-width character referenced to the eyes, so it belongs in conditions with the eye colour clause of the male Head sentence.

**Line 4 FIXABLE.**

### Line 5, Striatophasma naukluftense, eyes kidney-shaped, ocelli absent (male)

Description male: "Compound eyes tapered dorso-laterally and prominent, kidney-shaped, antero-ventral edge tapered, about twice as long as high;" + "interoccular distance ca. the length of one eye, on vertex larger than on ventral eye margin; ocelli absent." Previous "Head width similar to width of thorax, about as wide as long; sparsely covered with setae."; next "Gena higher than compound eyes; ventral parts of occipital ridge very prominent; ...". **Quote MATCH**, 34 words. Female sentences quoted in conditions match. Holotype "Male, NAMIBIA: Naukluft Mountains, northern slope" "-24.15, 16.32, 1200–1400 m, 04.v.2006, R. Predel (NMNW), specimen in ethanol."; paratypes "three males and four females; same data as holotype," "Nauchas: three males, -23.61, 16.37, 1750 m, 08.iv.2008", "Remhoogte: two males and two females, -23.96, 16.30, 1475 m, 08.iv.2008" (14): as in conditions. Genus diagnosis eye comparisons ("genae that protrude from the compound eyes"; "compound eyes that do not protrude from the genae distinguish" it from Tanzaniophasma) carried in substance.

**Line 5 MATCH.**

### Line 6, Pachyphasma brandbergense, eyes kidney-shaped, globular, ocelli absent (male)

Description male: "Compound eyes kidney-shaped, prominent, globular, about 1.5 times as long as high;" + "interoccular distance ca. the length of eye, on vertex larger than on ventral eye margin; ocelli absent." Previous "Head capsule slightly broader than thorax; sparsely covered with setae."; next "Coronal and frontal suture as well as frontoclypeal and temporal ridge indistinct; ...". **Quote MATCH**, 29 words. Female "Compound eyes less bulged than in male." Paratypes "four males and eight females; same data as holotype." (= the conditions' 12, 4 males and 8 females by depository); "Two juveniles and six heavily damaged specimens (1 juvenil, 2♀, 3♂) were excluded from the type-series." (the conditions' "does not clearly match" is fair). Genus diagnosis has no eye wording (tool summary).

**Line 6 MATCH.**

### Line 7, Melicertissa antrichardsoni, black ocellus at each tentacle and cordylus base

Colour section, whole: "Paratypes have a transparent and colourless bell and cordyli, pale yellowish gonads, and darkly pigmented tentacle bulbs." "A black ocellus is found at the base of each tentacle and cordylus (Figure 4A)." **Quote MATCH**, 15 words. Diagnosis and holotype description have no ocellus sentence ("Tentacle bulbs voluminous, heart-shaped, short; approximately 0.3 mm across the base." is the only bulb sentence). Table 1 "Black, at base of tentacles and cordyli". The `eye` field and conditions scope it to the paratypes, as the section reads.

**Line 7 MATCH.**

### Line 8, Paralovenia yongalensis, "No ocelli observed."

Description of holotype, "Other marginal structures" paragraph: "... Whether this structure exists on the other perradii could not be determined." "No ocelli observed." **Quote MATCH**, 3 words, a whole sentence of the species' holotype Description (the species is known from that one specimen), so it is a species-level statement and acceptable under the brief. Table 2 sense organs: "Ocelli absent; statocysts open, on broad conical base" for P. yongalensis, "Statocysts and ocelli absent" (P. bitentaculata), "Statocysts absent; ocelli not specified" (P. latigaster), as carried. The value "ocelli absent (none observed)" is no stronger than Table 2. Diagnosis has no ocellus sentence; Remarks cut off in the text returned (as the conditions say).

**Line 8 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Meteorona kishinouyei, six eyes per rhopalium | MATCH | | Material examined vs Table 3 sexes stated as printed |
| 2 | Tridacna maxima, 221 eyes | FIXABLE | quote, note | printed sentence begins "Specifically,", dropped without a cut mark; note misses T. maxima eyes_count on main |
| 3 | Tridacna squamosa, eye diameter 0.490 mm | MATCH | | whole sentence; Abstract SD discrepancy carried |
| 4 | Kuboesphasma compactum, ocelli absent (male) | FIXABLE | source.year, conditions, note | printed citation year 2017 (owner ruling) filed as 2018; genus diagnosis eye wording reported as absent |
| 5 | Striatophasma naukluftense, ocelli absent (male) | MATCH | | |
| 6 | Pachyphasma brandbergense, ocelli absent (male) | MATCH | | |
| 7 | Melicertissa antrichardsoni, black ocelli | MATCH | | Colour section, paratypes, as scoped |
| 8 | Paralovenia yongalensis, no ocelli | MATCH | | whole Description sentence on the only specimen; Table 2 "Ocelli absent" |

Errors: 2 of 8 records (25%); 2 fixable (lines 2, 4), 0 held out, 0 unfixable; no line to drop. Repeats: none (T. maxima on main from Land 2003 is a different paper that agrees). Verdict for desk-d319: **ACCEPT AFTER REPLACEMENT** (lines 1, 3, 5 to 8 as filed; lines 2 and 4 with the replacements below, or dropped if they are not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 2:
- `quote`: "T. maxima exhibited the highest eye count (221 ± 8)," -> "Specifically, T. maxima exhibited the highest eye count (221 ± 8),"
- `note`: "Whole printed Results sentence (about 27 words), read in two consecutive pieces on two passes; the sentence before it was not read." -> "Whole printed Results sentence (30 words as check.py counts), beginning 'Specifically,'; it follows 'Regarding ocular parameters (Figure 3), significant interspecific variations were observed in the total number of eyes per individual.'"
- `note`: "(Tridacna rows on main are lambda_max_nm book rows)" -> "(Tridacna on main: genus-level lambda_max_nm and receptor_classes book rows, and T. maxima eyes_count 'several hundred pinhole eyes on the exposed mantle', acuity_cpd and acceptance_deg from Land 2003 in audit/corrected/sea-invertebrates; a different paper whose count this record agrees with, so not a repeat)"

Line 4:
- `source.year`: "\"year\": 2018" -> "\"year\": 2017"
- `note`: "2018 is filed." -> "2017 is filed (the printed year wins, owner ruling)."
- `conditions`: "The genus-level Description and diagnosis have no eye wording;" -> "The genus Description and diagnosis mentions the eyes only as a reference level for head width: 'Additionally, the head capsule is distinctly broader on the level of the compound eyes than on the level of the genae in Minutophasma while they are equal in Kuboesphasma.' The male Head sentence before the quote gives 'compound eyes whitish with black or brown spots';"

Optional, not counted:
- Line 4 `order`: "\"order\": \"Notoptera\"" -> "\"order\": \"Mantophasmatodea\"" (Notoptera is the printed classification keyword; the title, text and lines 5 and 6 use Mantophasmatodea).
- Line 5 `note`: "the text assigns no family to Striatophasma itself" -> "the genus Description and diagnosis places Striatophasma as sistergroup to all remaining South African Austrophasmatidae (sensu Klass et al. 2003), now the tribe Austrophasmatini of Mantophasmatidae"
- Line 2 `note`: "so the order is the Crossref list (11 authors, ending Ying Pan, Yuehuan Zhang)" -> "so the order is the Crossref list (11 authors, ending Ying Pan, Yuehuan Zhang); the visible byline 'Wanjie Liu, ... Ziniu Yu … Yuehuan Zhang' agrees with it, and the hidden name is the tenth"
