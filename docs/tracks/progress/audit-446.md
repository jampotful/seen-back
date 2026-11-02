# audit-446: desk-d332, evidence lines 1 to 6

Audited 1 November 2026 from the desk-d332 files present untracked in the worktree (docs/views/evidence/desk-d332.jsonl, 12 lines; docs/tracks/progress/desk-d332.md). Neither is committed here or edited. This audit covers file lines 1 to 6 only; lines 7 to 12 belong to another auditor. HEAD 96bf60b19 (merge of desk d331 after audit 445). `tools/senses/check.py --require-evidence-kind` on the file: 12 records, 0 problems. Quote word counts (check.py split): 35, 40, 26, 20, 38, 38.

Sources opened (WebFetch, each URL taken from a WebSearch result): threatenedtaxa.org download/1124/2030 (Indirana chiravasi, two passes); threatenedtaxa.org article/view/1521 (Raorchestes ghatei, two passes); threatenedtaxa.org download/2877/4071 (Sphaerotheca pashchima); zookeys.pensoft.net article/2543/download/xml (Monomorium dryhimi); zookeys.pensoft.net article/37531/download/xml (truncated before the new species) and article_preview.php?id=37531 (two passes); Amphibian Species of the World pages for Indirana (genus), Indirana chiravasi, Raorchestes ghatei, Sphaerotheca (genus) and Sphaerotheca maskeyi; mdpi.com Diversity 13(5) 216 (Jablonski, Masroor and Hofmann 2021); antcat.org/catalog/440451; antwiki.org Crematogaster_gryllsi. AntCat for C. jacindae read from the search-result title only. Crossref was not queried; every licence below rests on the sentence printed on the copy read. No PMC, proxy, mirror, repository copy, ResearchGate or academia.edu page opened. 15 WebSearch, 15 WebFetch. WebFetch returns pieces of about 125 characters; quotes marked verified were returned as adjoining pieces with the joins stated by the tool.

Duplicates: grep of the whole docs/ tree (excluding desk-d332 files) for each species, the senior synonyms (Sphaerotheca maskeyi, Monomorium exiguum) and each DOI fragment (o4068, o3702, 2877.9.6, 106.1390, 898.37531). Indirana chiravasi appears in gbif-names.tsv and in oa-2.jsonl as a pupil_shape row (Thomas et al. 2022, doi 10.5519/4q5uvvpa), a different trait and source. Nothing else found. Duplicates 0.

## Unit-wide rulings

- **Tympanum ratios under sensory_anatomy (lines 1 to 3).** No tympanum key exists on main, and SENSORY-ANATOMY.md says to use `sensory_anatomy` "when no existing anatomical trait fits", naming structure and measurement. `relative_eye_size` and `eye_diameter_mm` record the eye, not the tympanum, so neither fits the ratio. All three records state "Anatomy only; hearing not tested", and none is filed under sense_hearing. Fit accepted. Line 3's EL 5.6 mm could also stand as its own `eye_length_mm` row (an existing main key), but that is optional.
- **ommatidia_count for longest-row counts (lines 4 to 6): error.** On main, the ommatidia_count rows hold total facets per eye: d272 "ommatidia/eye", d274 "ommatidia/eye", d283 "ommatidia per eye", d299 "20-25 (mainly 23)" "in 6 rows", d302 "facets per eye", d311 "9 facets". No main row anywhere in docs/ holds a longest-row count (grep "longest row" finds only desk-d332). Filing 6, 12 and 11 under the same key puts a row count, which is several times smaller than the total, beside total counts, and that misstates magnitude. The `units` string says what was counted, but the key is what the gap tables group on. Fix: move the records to `sensory_anatomy` with `evidence_kind: anatomical_measurement`, structure "compound eye, ommatidia" and measurement "number of ommatidia in the longest row". This is counted once inside each record's verdict and is not a separate error.

## Line 1, Indirana chiravasi, sensory_anatomy (tympanum 3/4 of eye in males, 2/3 in females): confirm

Bibliographic: the byline prints "Anand D. Padhye 1, Nikhil Modak 2 & Neelesh Dahanukar 3"; the citation line gives the title as recorded and "Journal of Threatened Taxa 6(10): 6293–6312", "26 September 2014", DOI 10.11609/JoTT.o4068.6293-312. Licence printed on the copy read: "Copyright: © Padhye et al. 2014. Creative Commons Attribution 4.0 International License." Met.

Quote: the Diagnosis sentence was returned whole in pieces. It runs from "Indirana chiravasi sp. nov. differs from all other congeners based on the following combination of characters:" through "medium-sized (24.7–39.2 mm SUL) frog, with median single internal vocal sac, ... distinct canthus rostralis, tympanum 3/4th the diameter of eye in males and 2/3rd in females," and on to "palms and soles dark brown." The record's two cuts are marked and drop only other diagnostic characters. MATCH. Context verified: holotype "tympanum about 3/4th the diameter of eye, very close to eye"; female paratype BNHS 5889 "tympanum about 2/3rd the diameter of eye, slightly more apart from eye than in male"; Sexual Dimorphism "Tympanum about 3/4th the diameter of eye in male and 2/3rd the diameter of eye in female." The type series is 5 males and 2 females, "preserved in absolute alcohol". Morphometry was by "digital caliper ... to the nearest 0.1mm". Holotype SUL 27.3 was not checked.

Name: Amphibian Species of the World prints "Indirana chiravasi Padhye, Modak, and Dahanukar, 2014" with no synonymy (beddomii group per Dahanukar et al. 2016). Accepted.

Uncounted: the conditions say "No millimetre value for the tympanum is given." The paper defines "TYL (maximum tympanum length)" under Morphometry and refers to "Table 2" for morphometric details. That table was not on the page read, so the sentence should be limited to the text read (optional fix below). This does not change the ratio, its sex split or its scope.

## Line 2, Raorchestes ghatei, sensory_anatomy (tympanum indistinct, one third of eye): confirm

Bibliographic: the article page gives the title as recorded; authors "A.D. Padhye, A. Sayyed, A. Jadhav, N. Dahanukar"; Vol. 5, No. 15 (2013), 4913–4931, published 26 November 2013; DOI 10.11609/JoTT.o3702.4913-31. The page states the journal is registered under CC BY 4.0, which is the publisher's own free copy. Met.

Quote: the abstract sentence was returned in seven pieces from "The species differs from its congeners based on a combination of characters including small to" through "snout slightly projecting beyond mouth ventrally, tympanum indistinct and one third of the eye" + "diameter, tongue without papilla" ... "lateral side marbled with white blotches on brown to black" + "background." The cuts are marked and drop only other characters. 40 words, at the limit. MATCH. partial true is right for an abstract-only read.

Name: ASW prints "Raorchestes ghatei Padhye, Sayyed, Jadhav, and Dahanukar, 2013", "Formerly confused with Raorchestes bombayensis", with no synonyms. Accepted.

Uncounted: `access` is "open" on an abstract-only record. Desk-d3xx practice is mostly "abstract" (29 of 37 partial records), so changing it is optional.

## Line 3, Sphaerotheca pashchima, sensory_anatomy (tympanum about 2/3 of eye; TYL 3.6, EL 5.6 mm): ERROR (taxon)

Bibliographic: the byline prints "Anand Padhye 1, Neelesh Dahanukar 2, Shauri Sulakhe 3, Nikhil Dandekar 4, Sunil Limaye 5 & Kirti Jamdade 6"; the title is as recorded; "Journal of Threatened Taxa 9(6): 10286–10296", 26 June 2017; DOI 10.11609/jott.2877.9.6.10286-10296. The page prints "Creative Commons Attribution 4.0 International License." Met.

Quote: "Description of the Holotype: (BNHS 6000, male, Image 1) (all measurements in mm)" + " Medium sized frog (SUL 41.0); head wider than long ..." through " tympanum about ⅔rd the diameter of eye (TYL =3.6; EL= 5.6), very close to eye;". MATCH. The parenthesis "(all measurements in mm)" sits on the heading line, and the quote prefixes it as the note says. That is not counted.

**Error: the taxon is a junior synonym.** ASW's Sphaerotheca maskeyi page lists "Sphaerotheca pashchima Padhye, Dahanukar, Sulakhe, Dandekar, Limaye, and Jamdade, 2017" with "Synonymy by Jablonski, Masroor, and Hofmann, 2021, Diversity, 13 (216): 7," and Khatiwada et al. 2021, and marks the common name "[no longer recognized]". The ASW Sphaerotheca genus page does not mention pashchima. Jablonski et al. (Diversity 13(5) 216) state: "Similarly, according to our analysis, the recently described S. pashchima is conspecific with S. maskeyi." The note's "Amphibian Species of the World lists the 2017 description (not individually opened)" is therefore wrong. Fixable: file under Sphaerotheca maskeyi. Main has no Sphaerotheca row.

Context: the type series is 21 specimens (holotype; paratypes 9 female, 6 male, 5 sub-adults), and Table 1 holds the morphometric variation. The Methods list "tympanum diameter (TYD)", and Results report the new species has relatively higher TYD. The record is one male holotype and says so ("one specimen"), so the holotype confound is disclosed. The replacement adds the series size. Not separately counted.

Uncounted: `units` "mm" sits on a value that leads with a ratio. Optional fix below.

## Line 4, Monomorium dryhimi, ommatidia_count 6: ERROR (taxon; trait fit)

Bibliographic: the XML gives the title as recorded (including ", with a key to the Arabian Monomorium monomorium-group"); Abdulrahman S. Aldawood; Mostafa R. Sharaf; ZooKeys 106: 47–54, 2011; DOI 10.3897/zookeys.106.1390. Licence: "This is an open access article distributed under the terms of the Creative Commons Attribution License," linked to CC BY 3.0. Met.

Quote: Worker description, "Eyes oval and of moderate size (EL 0.19–0.25 × HW) with 6 ommatidia in the longest row (Figs 2, 3)." MATCH, whole sentence. The next sentence ("eyes consist of a peripheral ring of ommatidia encircling two rows of ommatidia within the ring") gives no total. The holotype plus 13 paratypes were measured. Discussion: M. holothir has "8–9 ommatidia in the longest row".

**Error: the taxon is a junior synonym, and the trait key misfits.** AntCat prints "Monomorium dryhimi Aldawood & Sharaf, 2011 junior synonym of current valid taxon Monomorium exiguum Forel, 1894". The synonymising work was not shown on the page read. The note's "Accepted: AntCat/AntWiki list Monomorium dryhimi" is wrong. File under Monomorium exiguum (no main row) and say that the value describes the dryhimi type series, a single region of a widespread species. The trait-fit ruling is above. Both are fixed in one replacement; counted once.

## Line 5, Crematogaster gryllsi, ommatidia_count 12: ERROR (quote; trait fit)

Bibliographic: the XML gives the title in two parts as recorded; "Mostafa R. Sharaf, Abdulrahman S. Aldawood, Francisco Hita Garcia"; ZooKeys 898: 27–81, published 10 December 2019; DOI 10.3897/zookeys.898.37531. It also prints "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)". Met.

Quote: article_preview returned the Head paragraph in five pieces: "Head as long as or little broader than long with convex sides and feebly concave posterior margin;" ... "eyes of" + "moderate size (OI 22–31), located nearly at mid-length of head in full-face view and with about 12" + "ommatidia in the longest row; anterior clypeal margin broadly convex." A second pass confirmed the text between "eyes of moderate size" and "located" is " (OI 22–31), " and that "The abbreviation is not expanded inline." **Error: the quote inserts the unmarked words "(Ocular index)"** ("(OI (Ocular index) 22–31)"). That text is not in the paper. OI is defined only under Indices: "OI Ocular index: EL / HW × 100". The other cuts are marked and drop no eye qualifier. The trait-fit ruling also applies. Counted once. The holotype and 15 paratypes were measured (type series 30); the diagnosis does not mention ommatidia.

Name: AntWiki prints "Crematogaster gryllsi Sharaf & Hita Garcia, in Sharaf, Aldawood & Hita Garcia, 2019: 52" with no synonyms. AntCat was not opened for this name. Accepted.

## Line 6, Crematogaster jacindae, ommatidia_count 11: ERROR (quote; trait fit)

Bibliographic: same paper as line 5. Met.

Quote: Head paragraph pieces: "Head as long as or little broader than long with convex sides and feebly concave posterior margin;" + " antennae 12-segmented; ... fail to reach posterior margin of head; eyes of moderate size (OI 16–27), located nearly at " + "mid-length of head in full-face view and with ca. eleven ommatidia in the longest row; " + "anterior clypeal margin broadly convex." **Error: the same unmarked insertion "(Ocular index)"** appears in "(OI (Ocular index) 16–27)". The key, couplet 3, gives "eyes with ca. 11 ommatidia in longest row". The holotype and 20 paratypes were measured. The trait-fit ruling also applies. Counted once.

Name: AntCat's search-result title reads "Crematogaster jacindae Sharaf & Hita Garcia, 2019 valid" (page not fetched). Accepted.

## Summary

| Line | Taxon | Verdict | Reason |
|---|---|---|---|
| 1 | Indirana chiravasi | confirm | Quote, bibliography, licence and name verified; "no millimetre value" limited to the text read (uncounted) |
| 2 | Raorchestes ghatei | confirm | Abstract sentence verified whole, 40 words; ASW valid; access field optional |
| 3 | Sphaerotheca pashchima | error (fixable) | Name is a junior synonym of Sphaerotheca maskeyi (ASW; Jablonski et al. 2021) |
| 4 | Monomorium dryhimi | error (fixable) | Junior synonym of Monomorium exiguum (AntCat); longest-row count under a total-count key |
| 5 | Crematogaster gryllsi | error (fixable) | Quote inserts unmarked "(Ocular index)"; longest-row count under a total-count key |
| 6 | Crematogaster jacindae | error (fixable) | Same quote insertion; same trait-key misfit |

Errors 4 of 6 records (67%), all fixable; none held out, none unfixable. By kind: taxon 2 (lines 3, 4); quote 2 (lines 5, 6); trait key 3 (lines 4 to 6, folded into those records); bibliographic 0; licence 0; duplicates 0; omitted contrary results 0. Tested: the replacements below, applied to a scratch copy, give 12 records and 0 problems under check.py --require-evidence-kind, each old string occurring exactly once in its line.

## Replacement

Strings are decoded text. Literal double quotes inside new strings are shown escaped (\") as they must appear in the raw JSON line. Apply in order within each line.

### Line 3

- `"taxon": "Sphaerotheca pashchima"` -> `"taxon": "Sphaerotheca maskeyi"`
- `note`: "Quote begins" -> "Filed as Sphaerotheca pashchima Padhye et al., 2017 (holotype BNHS 6000); Amphibian Species of the World lists Sphaerotheca pashchima under Sphaerotheca maskeyi (Schleich and Anders, 1998) with \"Synonymy by Jablonski, Masroor, and Hofmann, 2021, Diversity, 13 (216): 7\" and Khatiwada et al. 2021, so the record is filed under S. maskeyi (audit 446). Quote begins"
- `note`: "Accepted: Amphibian Species of the World lists the 2017 description (not individually opened); not in gbif-names.tsv. " -> "" (delete)
- `conditions`: "Holotype BNHS 6000, male, SUL 41.0 mm; one specimen." -> "Holotype BNHS 6000, male, SUL 41.0 mm; one specimen of a 21-specimen type series (holotype, 9 female, 6 male and 5 sub-adult paratypes) whose morphometric Table 1 (with tympanum diameter TYD) was not read."

### Line 4

- `"taxon": "Monomorium dryhimi"` -> `"taxon": "Monomorium exiguum"`
- `"trait": "ommatidia_count", "value": 6, "units": "ommatidia in the longest row"` -> `"trait": "sensory_anatomy", "evidence_kind": "anatomical_measurement", "structure": "compound eye, ommatidia", "measurement": "number of ommatidia in the longest row of the eye (not total facets)", "value": 6, "units": "ommatidia in the longest row"`
- `note`: "new trait: ommatidia_count (follows the key used on main, e.g. desk-d283/d306 rows). Whole sentence. Accepted: AntCat/AntWiki list Monomorium dryhimi (search results; AntWiki page not opened in full)." -> "Filed under sensory_anatomy because main's ommatidia_count rows hold total facets per eye and this is a longest-row count (audit 446). Described as Monomorium dryhimi Aldawood & Sharaf, 2011; AntCat prints \"Monomorium dryhimi Aldawood & Sharaf, 2011 junior synonym of current valid taxon Monomorium exiguum Forel, 1894\", so the record is filed under M. exiguum and describes the dryhimi type series only, not the species' full range (audit 446). Whole sentence."
- `conditions`: "(type series; sample size not stated in the sentence)" -> "(type series; the holotype and 13 paratype workers were measured, per the Measurements section)"

### Line 5

- `quote`: "(OI (Ocular index) 22–31)" -> "(OI 22–31)"
- `"trait": "ommatidia_count", "value": 12,` -> `"trait": "sensory_anatomy", "evidence_kind": "anatomical_measurement", "structure": "compound eye, ommatidia", "measurement": "number of ommatidia in the longest row of the eye (not total facets)", "value": 12,`
- `note`: "new trait: ommatidia_count (follows the key used on main, e.g. desk-d283/d306 rows)." -> "Filed under sensory_anatomy because main's ommatidia_count rows hold total facets per eye and this is a longest-row count (audit 446). OI is defined in the Indices section as \"OI Ocular index: EL / HW × 100\"; the holotype and 15 paratype workers were measured (audit 446)."

### Line 6

- `quote`: "(OI (Ocular index) 16–27)" -> "(OI 16–27)"
- `"trait": "ommatidia_count", "value": 11,` -> `"trait": "sensory_anatomy", "evidence_kind": "anatomical_measurement", "structure": "compound eye, ommatidia", "measurement": "number of ommatidia in the longest row of the eye (not total facets)", "value": 11,`
- `note`: "new trait: ommatidia_count (follows the key used on main, e.g. desk-d283/d306 rows)." -> "Filed under sensory_anatomy because main's ommatidia_count rows hold total facets per eye and this is a longest-row count (audit 446). OI is defined in the Indices section as \"OI Ocular index: EL / HW × 100\"; the holotype and 20 paratype workers were measured; AntCat lists Crematogaster jacindae Sharaf & Hita Garcia, 2019 as valid (audit 446)."

## Optional fixes (not counted)

- Line 1 `conditions`: "No millimetre value for the tympanum is given." -> "The text read gives no millimetre value for the tympanum; Morphometry defines TYL (maximum tympanum length) and refers to Table 2, which was not read. Type series 5 males and 2 females, preserved in absolute alcohol."
- Line 2 `source.access`: "open" -> "abstract" (desk practice for abstract-only records).
- Line 3 `units`: "mm" -> "fraction of eye diameter; TYL and EL in mm".
- Owner question: if longest-row counts recur, a dedicated key (for example `ommatidia_longest_row`) would separate them from sensory_anatomy. This audit invents none.
