# audit-403: desk-d307, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d307 files present untracked in the worktree (docs/tracks/progress/desk-d307.md and docs/views/evidence/desk-d307.jsonl, 7 lines; neither committed here, neither edited). All seven lines judged. HEAD equals origin/main (b1ba77167). `python3 -I tools/senses/check.py | grep d307`: "docs/views/evidence/desk-d307.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 11, 14, 34, 23, 20, 9, 12, all within 40.

Sources opened (WebFetch, every article URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=3861 (two passes), id=51067 (two passes), id=100084 (two passes), id=7142 (two passes), id=66435 (two passes), zookeys.pensoft.net/article/114974/zoom/fig/12/ (a figure page; no Abstract), en.wikipedia.org/wiki/Xya (species list credited to Orthoptera Species File). pubmed.ncbi.nlm.nih.gov/38405676/ returned PROVENANCE_REQUIRED and was not retried; no Pensoft article page for 10.3897/zookeys.1191.114974 came back from two searches. Crossref single-DOI lookups (api.crossref.org/v1/works/) for all six DOIs read on the first call. PMC, Plazi, DOAJ, BHL, GBIF, library catalogue and blog results were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 9 WebSearches.

Stitching: Agasicles came back as "Scanning electron microscopy, paraffin sectioning, and transmission electron microscopy revealed that A. hygrophila has" / "apposition compound eyes with both eucones and open rhabdom." (a different split from the unit's, same sentence). The Burmella paucivenosa sentence came back as four pieces ending "lower portion of compound eyes brownish-black (Figs 1, 2A–C)."; the B. clypeata, Electrotettix, Xya and Elocomosta sentences came back whole.

## Bibliographic and licence

- Line 1 (Heads, Thomas, Wang 2014). Page byline "Sam W. Heads, M. Jared Thomas, Yinan Wang"; Crossref "Sam Heads, M. Thomas, Yinan Wang", same order. Title identical; ZooKeys 429: 87–100, issued 2014-07-30, no issue. Page prints the CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Right.
- Line 2 (Cao, Rong, Naveed 2020). Page byline and Crossref identical in order; title identical (printed in two lines); ZooKeys 947: 103–112, 2020; CC BY 4.0 page and Crossref vor. Right.
- Line 3 (Komeda, Ohtsuka, Huys 2024). Crossref order Komeda, Ohtsuka, Huys; title identical; ZooKeys 1191: 307–338, 2024; Crossref CC BY 4.0 vor. Page byline not re-read here (no article page reached); audit-374 read it for the same paper.
- Line 4 (Fan et al. 2023, 12 authors). Page byline and Crossref identical in order; title identical; ZooKeys 1177: 23–40, 2023; page CC BY 4.0 sentence, Crossref CC BY 4.0 vor. Right.
- Line 5 (Lin, Jia, Fikáček 2016). Page byline "Renchao Lin, Fenglong Jia, Martin Fikáček" and citation line "Lin R, Jia F, Fikáček M (2016)"; Crossref lists Jia, Lin, Fikáček. Page followed, as the rules require: right. Title identical; ZooKeys 607: 81-92; CC BY 4.0 page and Crossref vor.
- Lines 6, 7 (Godunko, Martynov, Staniczek 2021). Page byline and Crossref identical in order; title identical; ZooKeys 1036: 99–120, 2021; CC BY 4.0 page and Crossref vor. Right.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Electrotettix attenboroughi: monotypic genus described here ("As for the genus (see above), by monotypy."). Hierarchy lines Order Orthoptera, Suborder Caelifera, Family Tetrigidae, Subfamily Cladonotinae; no class printed. Right.
- Xya xishangbanna: Orthoptera Species File list (via the Wikipedia genus page) carries "Xya xishangbanna Cao, Rong & Naveed, 2020" in this spelling; the epithet is printed "xishangbanna" although the etymology names Xishuangbanna. No classification block or class printed. Right.
- Gyorome guttatum: see repeat below.
- Agasicles hygrophila: no classification block; Coleoptera and Chrysomelidae from the title. No class printed. The eye statement comes from the paper's own SEM, sections and TEM ("Therefore, we confirmed that A. hygrophila possesses apposition compound eyes (Fig. 4A, B)."; "Thus, we confirm that A. hygrophila has an open rhabdom (Fig. 5D)."), on laboratory stock of the species; neither pooled nor review-sourced. Right.
- Elocomosta lilizheni: Abstract prints "Coleoptera: Hydrophilidae: Sphaeridiinae: Coelostomatini"; no class. Right.
- Burmella paucivenosa and B. clypeata: hierarchy lines "Class Insecta Linnaeus, 1758", "Order Ephemeroptera Hyatt & Arms, 1890", "Family Vietnamellidae Allen, 1984". Right.

## Repeats

`git grep -i` on origin/main (b1ba77167) over the whole docs/ tree for attenboroughi, Electrotettix, zookeys.429.8020, xishangbanna, zookeys.947.51067, Gyorome, zookeys.1191.114974, Agasicles, zookeys.1177.100084, Elocomosta, zookeys.607.7142, Burmella, zookeys.1036.66435, paucivenosa, clypeata. Then every origin/research/desk-d* branch not merged into main (307 branches), grepping the docs/views and progress files each branch changes against main.

- **Gyorome guttatum is on main**: docs/views/evidence/desk-d284.jsonl line 1, same species, same DOI (10.3897/zookeys.1191.114974), same trait (eye_type), same Abstract sentence and value ("large, paired, frontal modified eyes, each consisting of a baculiform ocellus, a globular (Gicklhorn's?) organ and a semi-parabolic plate"), audited MATCH in audit-374; desk-queue.md line 342 and desk-d285.md ("Gyorome guttatum already taken (d280-d284).") also name it. Line 3 repeats main: error, unfixable, drop. The unit's progress note says "no hits"; Gyorome was in its own grep list, so the check was not run or not read. Audit-374 also records the printed Abstract as "The most distinguishable feature of G. guttatum gen. et sp. nov. ..." with a curly apostrophe in "Gicklhorn’s?"; line 3's quote spells out "Gyorome guttatum" with a straight apostrophe (not re-verified here: no article page reached; not counted separately).
- **Agasicles hygrophila**: no evidence, sheet, audit/ALL or audit/corrected record anywhere on main. The name appears only in docs/views/searched/ (harvest-34, -43, -45, -48, -49, -53; sweep-28, -33, -47, -52, -58, -64, -102) as a screened or opened work for other genera (Diabrotica, Galeruca, Chrysoteuchia; sweep-52: "Agasicles hygrophila (Galerucinae) shows ERG responses to five colours but the page gives no peak wavelength"), and in progress notes audit-49, audit-50, audit-64 and desk-d279. desk-d279.md line 7 says it is "on main (harvest sheets, d270)"; no sheets file and no desk-d270 file carries it, so that statement is wrong, and line 4 is not a repeat.
- Hits for clypeata on main are other species (bird and bee records, "clypeata" epithets elsewhere); none is Burmella. No hit for the other taxa or DOIs.
- Unmerged branches: hits only in desk-d279, desk-d284, desk-d285 and desk-d299 (the same files already on main, listed above) and desk-d307 itself.

Repeat faults: 1 (line 3).

## Per line

### Line 1, Electrotettix attenboroughi, compound eyes large, globose

Description (female holotype): "Compound eyes large, globose, projecting somewhat dorsally; ventral margin acutely rounded." **Quote MATCH**, whole sentence, 11 words. Holotype INHS 10175, "Well-preserved adult female in a piece of amber approximately 20 × 15 × 12 mm."; male "Unknown"; no other specimen. Preservation sentences ("Protarsus largely obscured by bubbles and debris in the amber."; "Abdomen at least 4.0 mm long, though apical damage prevents accurate measurement."; "Dorsal parts of terminalia (epiproct, cerci, etc.) obscured by bubbles and detritus.") as the conditions say. Abstract and Diagnosis carry no eye wording; Remarks "is similar to Baeotettix in the large eyes projecting dorsally above the fastigium" as recorded. The value says no more than the quote; one specimen, sex and preservation given.

Not counted: the locality is the country only; the page prints "La Toca region, near Santiago de los Caballeros, Santiago Province, Dominican Republic" and "Early Miocene (Burdigalian)" (optional fix below).

**Line 1 MATCH.**

### Line 2, Xya xishangbanna, compound eyes dark brown to black, rounded in front

Male Description: "Compound eyes dark brown to black, 2 times broader than longer, rounded in front." **Quote MATCH**, 14 words. Holotype male, "Yunnan Province, Xishuangbanna, Mengla County, Wuxiangguangchang", "21.92N, 101.11E", "21–24 Mar. 2019"; paratype one female, "same data as holotype"; female Description ends "Others same as male." No Remarks. As recorded.

Fault: the conditions give only the Diagnosis's similarity ("It is most similar to X. leshanensis Cao et al. in the compound eyes with a narrow band along the inner margin.") and leave out the eye colour wording that follows in the same Diagnosis: "It can be distinguished from the latter by the body with dorsal surface not rough, but more shiny;" / "the compound eyes with a prominent brown band along their inner margin on both sides;" against "In X. leshanensis, ... the compound eyes bear a yellowish-white band along the inner margin;", repeated in Table 1 ("With brown band along inner margin" / "With yellowish-white band along inner margin"). For a value that is an eye colour, the paper's diagnostic eye colouring is contrasting wording elsewhere in the paper, and the record paraphrases the similarity sentence ("having") instead of quoting it. One record error, fixable.

**Line 2 FIXABLE.**

### Line 3, Gyorome guttatum, large paired frontal modified eyes

Repeat of docs/views/evidence/desk-d284.jsonl line 1 on main (same species, DOI, trait, sentence and value). Unfixable; drop.

**Line 3 DROP (repeat).**

### Line 4, Agasicles hygrophila, apposition eyes with eucones and open rhabdom

Abstract: "Scanning electron microscopy, paraffin sectioning, and transmission electron microscopy revealed that A. hygrophila has apposition compound eyes with both eucones and open rhabdom." **Quote MATCH**, 23 words, whole sentence. Results confirm each element ("Four wedge-shaped cone cells located just beneath the cornea are involved in forming the eucones."). Material: "Live specimens of A. hygrophila were gifted from the Institute of Plant Protection, Chinese Academy of Agricultural Sciences" (and Shanxi Agricultural University, tool summary); SEM "nine male and female adult heads and prothoraxes were separated from the body"; section, TEM and micro-CT numbers not stated; ERG on 12 adults (not this value). Ommatidia sentence "The number of ommatidia (341.00 ± 3.35 and 345.22 ± 4.48) was not significantly different" continues "between male and female compound eyes"; Discussion "In this study, SEM and TEM experiments revealed that that the compound eyes of A. hygrophila contains few ommatidia" as the conditions quote. Primary data on the species, not pooled or review-sourced. Conditions right.

Not counted: the note's "the page does not say per eye" is loose ("between male and female compound eyes"); the counts are not filed, so nothing turns on it.

**Line 4 MATCH.**

### Line 5, Elocomosta lilizheni, eyes extremely reduced

Species Diagnosis: "Eyes extremely reduced in size, dorsally eyes divided by distance of ca. 20 × the dorsal width of one eye." **Quote MATCH**, 20 words. Description repeats the clause and adds "ventral portion absent." Holotype male, Yinshan Conservation Station, beech forest, 1200 m, 11.vii.2014; "Paratypes (11 spec., SYSU, SHNU, NMPC)": 7 with holotype data, 2 at "Jinxiu County, 7 km", 1300 m, 16.vii.2014, 2 at "Laoshan Forest Farm", 950 m, 26.vii.2014; sexes of paratypes not given. Discussion and E. nigra wording ("dorsally eyes divided by distance of 4.4 × the dorsal width of one eye"), genus redescription ("Eyes well developed and strongly constricted laterally, or largely reduced.") and Abstract as the conditions give.

Fault: the `eye` field scopes the value to "adult male holotype", but the quote is the species Diagnosis, a statement about the species built on the holotype and 11 paratypes of unstated sex. Holotype-only against species-wide scope misstated. One record error, fixable.

**Line 5 FIXABLE.**

### Line 6, Burmella paucivenosa, compound eyes medially contiguous (male)

Description: "Compound eyes well-developed, large, widely rounded, medially contiguous;" / "upper portion of compound eyes translucent and slightly yellowish apically, brownish-black basally;" / "border between dorsal and ventral portions of compound eyes well distinguishable;" / "lower portion of compound eyes brownish-black (Figs 1, 2A–C)." The quote takes the first clause and marks the cut with "…"; the cut text describes colour and the dorsal/ventral border, not a qualifier of the logged shape. **Quote ACCEPTED as cut.** Holotype "Male imago in Mid-Cretaceous Burmese amber, SMNS collection, inventory number BU-179."; "The precise mine from which these stones originate is unknown."; ocelli "Ocelli poorly preserved, relatively small, without conspicuous colouration."; species Diagnosis without eye wording.

Fault: the conditions set this male's contiguous eyes against the B. clypeata female's separated eyes as a difference between species, and omit that the paper does not exclude that the two holotypes are one species: "We do however not per se exclude a possible conspecifity of both fossil specimens." / "This may be supported by a similar, small body size of both specimens, with similar proportions of male/female body length" / "Also, the anterolaterally expanded clypeus in B. clypeata may not exclude their conspecifity.", the authors separating them on wing venation ("However, a clear difference in the venation of fore- and hind wings"). The eye contrast may then be between sexes, and the paper does not compare the eyes. The conditions also say "The Affinities sections carry no eye wording", while the Affinities text says "In contrast to all other representatives of Vietnamellidae, the clypeus in the female" / "the anterior portion of eyes is partly covered by this clypeal shield" (female only). The age is given as Upper Albian only; the page adds "with a maximum age of 98.79 ± 0.62 Ma" / "which is equivalent to the earliest Cenomanian", and the type lines print "Cenomanian, mid-Cretaceous" (folded into the fix). One record error, fixable.

**Line 6 FIXABLE.**

### Line 7, Burmella clypeata, eyes widely separated (female)

Description: "Eyes brown, elongated, relatively large, widely separated medially; facets of eyes hexagonal." **Quote MATCH**, whole sentence, 12 words. Holotype "Female imago in Mid-Cretaceous Burmese amber, SMNS collection, inventory number: BU-321."; "Distance between eyes 0.73× of head width."; "Clypeus expanded anterolaterally, partly covering anterior part of eyes."; "Ocelli well preserved, large, without conspicuous colouration."; species Diagnosis without eye wording; genus diagnosis "in female (p) anterior part of eyes covered by anterolaterally expanded clypeal shield."

Fault: as line 6, the contrast with the male's contiguous eyes is given without the paper's possible conspecificity of the two holotypes, which makes the eye difference possibly sexual. Age as line 6 (folded in). One record error, fixable.

**Line 7 FIXABLE.**

## Unit question

Eye-shape and eye-colour statements as eye_type: main already holds shape values under eye_type (for example "kidney-shaped" and "large eye, cornea globular and well pigmented" in recent desk units), so lines 1, 2, 6 and 7 are not refused on that ground here. Colour alone (line 2's "dark brown to black") is the thinnest; it is filed with shape ("rounded in front") and passes on that.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Electrotettix attenboroughi, eyes large, globose | MATCH | | quote, female holotype only, preservation, Remarks |
| 2 | Xya xishangbanna, eyes dark brown to black | FIXABLE | conditions | Diagnosis's "prominent brown band along their inner margin" (X. leshanensis yellowish-white) omitted |
| 3 | Gyorome guttatum, modified eyes | DROP | | repeats desk-d284.jsonl line 1 on main |
| 4 | Agasicles hygrophila, apposition, eucone, open rhabdom | MATCH | | Abstract sentence, own SEM/TEM data, not on main |
| 5 | Elocomosta lilizheni, eyes extremely reduced | FIXABLE | eye | species Diagnosis (12 specimens) scoped to the male holotype |
| 6 | Burmella paucivenosa, eyes medially contiguous | FIXABLE | conditions | possible conspecificity with the B. clypeata female omitted; Affinities eye wording misreported |
| 7 | Burmella clypeata, eyes widely separated | FIXABLE | conditions | possible conspecificity with the B. paucivenosa male omitted |

Errors: 5 of 7 records (71.4%); 4 fixable (lines 2, 5, 6, 7), 1 unfixable (line 3, repeat), 0 held out. Line to drop: 3. The rate is above 5%, so the unit merges by the drop-the-errors route: lines 1 and 4 as filed, lines 2, 5, 6 and 7 with the replacements below (or dropped if they are not applied), line 3 dropped. Verdict: **ACCEPT AFTER REPLACEMENT, line 3 dropped**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 2:
- `conditions`: "The Diagnosis says the species is most similar to X. leshanensis in the compound eyes having a narrow band along the inner margin." -> "The Diagnosis says the species is most similar to X. leshanensis 'in the compound eyes with a narrow band along the inner margin' and distinguishes it by 'the compound eyes with a prominent brown band along their inner margin on both sides', against 'a yellowish-white band along the inner margin' in X. leshanensis; Table 1 gives 'With brown band along inner margin' for X. xishangbanna."

Line 3: drop (repeat of docs/views/evidence/desk-d284.jsonl line 1).

Line 5:
- `eye`: "compound eyes, adult male holotype" -> "compound eyes, adults (species Diagnosis; holotype male and 11 paratypes of unstated sex)"

Line 6:
- `conditions`: "The Affinities sections carry no eye wording." -> "The paper does not exclude that the two holotypes are one species ('We do however not per se exclude a possible conspecifity of both fossil specimens.'), citing similar small body size and male/female proportions and the clypeus, and separates them by wing venation; the eye difference between this male and the B. clypeata female may therefore be sexual, and the paper does not compare the eyes. The Affinities eye wording concerns only the female, whose anterior eye portion is partly covered by the clypeal shield."
- `conditions`: "Upper Albian," -> "Upper Albian (maximum age 98.79 ± 0.62 Ma, 'equivalent to the earliest Cenomanian'; the type lines print 'Cenomanian, mid-Cretaceous'),"

Line 7:
- `conditions`: "The male holotype of B. paucivenosa has compound eyes medially contiguous." -> "The male holotype of B. paucivenosa has compound eyes medially contiguous; the paper does not exclude that the two holotypes are one species ('We do however not per se exclude a possible conspecifity of both fossil specimens.'; the expanded clypeus 'may not exclude their conspecifity') and separates them by wing venation, so the eye difference may be sexual; the paper does not compare the eyes. The genus diagnosis gives 'in female (p) anterior part of eyes covered by anterolaterally expanded clypeal shield.'"
- `conditions`: "Upper Albian," -> "Upper Albian (maximum age 98.79 ± 0.62 Ma, 'equivalent to the earliest Cenomanian'; the type lines print 'Cenomanian, mid-Cretaceous'),"

Optional, not counted (line 1): `conditions` "(Dominican Republic)" -> "(La Toca region, near Santiago de los Caballeros, Santiago Province, Dominican Republic; Early Miocene, Burdigalian)".

Desk note: desk-d279.md's "Agasicles hygrophila eye (zookeys.1177.100084) ... on main (harvest sheets, d270)" is wrong; the species appears on main only in searched/ screened-works entries and progress notes.
