# audit-404: desk-d308, evidence lines 1 to 5

Audited 1 November 2026 from the desk-d308 files present untracked in the worktree (docs/tracks/progress/desk-d308.md and docs/views/evidence/desk-d308.jsonl, 5 lines; neither committed here, neither edited). All five lines judged. HEAD equals origin/main (b1ba77167). `python3 -I tools/senses/check.py | grep d308`: "docs/views/evidence/desk-d308.jsonl: 5 records, 0 problems". Quote lengths (`len(q.split())`): 14, 32, 5, 13, 12, all within 40.

Sources opened (WebFetch, every article URL from a WebSearch result): vetdergikafkas.org/pdf.php?id=3057 (two passes), zookeys.pensoft.net/article_preview.php?id=35776 (two passes), id=118358 (one pass), id=125639 (one pass), id=76884 (one pass), antwiki.org/wiki/Ooceraea_hainingensis. Crossref single-DOI lookups api.crossref.org/v1/works/ for all five DOIs, each read on the first call. Amphibian Species of the World seen in a search result only (URL path Gymnophiona/Caeciliidae/Caecilia/Caecilia-pulchraserrana). Plazi, Zenodo, PMC, DOAJ, GBIF, the kafkas.edu.tr repository and biomed.reviewer.ly results were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 9 WebSearches.

Stitching: the Caecilia pulchraserrana sentence came back as two pieces, "The new species is assignable to the genus Caecilia because its eyes are not covered by bone" / " and it has tentacles below the nostrils (Type D sensu Lynch, 1999, Fig. 3 D–E).", and the tool stated the pieces are contiguous with nothing omitted. The join falls at a space of one printed sentence (here after "bone", not after "tentacles" as the unit's note says), and the joined text equals the record's quote character for character. Under the quote rule stitching is a fault only when the stitched text differs from the page; it does not here, so the quote stands. desk-d295's drop of this sentence ("arrived in pieces") was a retrieval decision, not a finding that the sentence is unusable.

## Bibliographic and licence

- Line 1 (Ermutlu, Balyen, Özaydın, Kılıç, Aksoy, Büyükbaki, Büyükbaki, Aydın, Yıldız, Ermutlu 2024). Page byline in capitals ("Celal Şahin ERMUTLU 1 (*) Lokman BALYEN 2 İsa ÖZAYDIN 1 Engin KILIÇ 1 Özgür AKSOY 1 Hatice Gizem BÜYÜKBAKİ 3" / "Burak BÜYÜKBAKİ 4 Uğur AYDIN 1 Uğur YILDIZ 1 Dilem Gülece ERMUTLU 5"); Crossref lists the same ten in the same order. Page title "Anterior and Posterior Segment Parameters of the Eye in Eagle Owls (Bubo bubo)" (Crossref omits "(Bubo bubo)"); the printed title is filed, right. Running header "Kafkas Univ Vet Fak Derg 30 (1): 81-86, 2024"; Crossref gives no volume, issue or page and year 2023; printed year 2024 and 30(1): 81-86 filed, right. Licence: the publisher's own PDF prints "This article is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)"; Crossref carries no licence. Judged against the rule as written: the copy read is the publisher's own free full text (accepted on that ground alone), and CC BY-NC is on the accepted list; the "Crossref unspecified plus page-printed CC" clause is not needed, since nothing on Crossref conflicts with the page. Accepted.
- Line 2 (Acosta-Galvis, Torres, Pulido-Santacruz 2019). Byline and Crossref identical in order. Page-top title and Crossref "A new species of Caecilia (Gymnophiona, Caeciliidae) from the Magdalena valley region of Colombia"; the citation line prints a longer form ("(Gymnophiona: Caeciliidae) ... Colombia, with comments on the genus Parvicaecilia."). The page-top title is the article's printed title; the unit's choice is acceptable and is disclosed in the note. ZooKeys 884: 135-157, 2019, no issue. Page prints the CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 3 (Gao, Long, Liu, Liu, Ran, Lacy, Kronauer 2024). Byline and Crossref identical in order; title identical; ZooKeys 1205: 101-113, issued 2024-06-20, no issue. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 4 (Sun, Yang, Tan, Li, Jacobus 2024). Byline and Crossref identical in order; title identical; ZooKeys 1205: 349-371, issued 2024-07-01. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 5 (Martins, Azevêdo, Hamada, Grillet, Contreras-Ramos 2022). Byline "Caleb Califre Martins, Carlos A. S. de Azevêdo, Neusa Hamada, Maria E. Grillet, Atilano Contreras-Ramos"; Crossref same order. Order right. The page's own citation line prints "Martins CC, de Azevêdo CAS, Hamada N, Grillet ME, Contreras-Ramos A (2022)"; the record has "Azevêdo CAS" (the form of the species authority, "Corydalus ralphi Martins, Azevêdo, Hamada & Contreras, sp. nov."). Optional fix below, not counted. Title identical; ZooKeys 1111: 339-353, 2022. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.

Bibliographic faults counted 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Bubo bubo: the page prints no family (Introduction "belong to the owl family of the Raptors family"); "Aves: Strigiformes" is printed only inside two reference titles about owls ("Eye shape and retinal topography in owls (Aves: Strigiformes)", "Comparative study of visual pathways in owls (Aves: Strigiformes)"). That is printed text on the page placing owls, of which this paper's species is one, and the note says where it came from; acceptable. Blank family is acceptable: the rule fills what is printed and the page prints none (main's intake-8 row carries Strigidae from its own source; it is not copied here). Name in current use; main holds many Bubo bubo rows under the same name.
- Caecilia pulchraserrana: Amphibian Species of the World lists it under Gymnophiona/Caeciliidae/Caecilia (search-result URL, page not opened); no synonymy seen. Order and family from the title, Amphibia from the keywords: acceptable as disclosed.
- Ooceraea hainingensis: AntWiki cites Bolton's catalogue "Ooceraea hainingensis Gao et al., 2024: 104, figs. 1-3 (w.dq.) CHINA (Zhejiang)." with no status change. Family and order from the title, class blank: right.
- Cincticostella jianchuan: Order and Family headings printed on the page (unit's note); described 2024, no later change found. Right.
- Corydalus ralphi: order, family and subfamily from the title; class blank; Plazi treatment in results under the same name. Right.

## Repeats

`git grep -i` on origin/main (b1ba77167) over the whole docs/ tree for "Bubo bubo", "Eagle Owls", kvfd.2023.30500, pulchraserrana, zookeys.884.35776, hainingensis, zookeys.1205.118358, jianchuan, zookeys.1205.125639, "Corydalus ralphi", ralphi, zookeys.1111.76884. Hits: pulchraserrana only in desk-d295.md (dropped, "arrived in pieces"); kvfd only for other DOIs (oa-5 and rechecks); none of the four ZooKeys DOIs or the KVFD DOI anywhere. All origin/research/desk-d* branches not merged into main, grepped in their docs/ files that differ from main: hits only in desk-d295 (the same progress note) and desk-d308 itself.

**Bubo bubo already has eye data on main, under the same key.** Main's Bubo bubo rows: acuity_cpd, bill_tip_projection_deg, binocular_deg, binocular_max_elevation_deg, cff_hz, corneal_thickness_mm, eye_axial_length_mm, fov_h_deg, fov_v_deg, interreceptor_deg, lambda_max_nm, lens_thickness_mm, ocular_media rows, opsin_spectral_class, spectral_range_nm, visual_field_margin_separation_deg. The eye_axial_length_mm row is oa-1.jsonl line 4943: 40.3 mm, "whole eye", "axial-length measurement from cryotome image or cited source", Olsson, Lind, Mitkus, Delhey, Kelber 2021, Journal of Experimental Biology 224:jeb243129 (doi 10.1242/jeb.243129), one animal, one eye. Different paper, method (cryotome against live optical biometry) and value, so line 1 is not a repeat; but the unit's repeat claim and "New trait" note are wrong, and the 40.3 against 31.1 mm gap should be visible in the record.

Trait key: `eye_axial_length_mm` is absent from check.py's TRAITS but is a key in use on main (oa-1, oa-6, oa-7, desk-d243, d244, d245, audit/ALL, recheck-codex-b-fixed). Answer to the unit's question: keep eye_axial_length_mm. The paper measures axial globe length ("axial lengths in mm with an optical biometric device"; Discussion "Eye shape has been defined as the ratio of corneal diameter (CD) to axial length (AL)"), which is what main's key holds; filing it as eye_diameter_mm would be wrong. Main's wording for this case is "new trait: eye_axial_length_mm (key already in use on main)", which also keeps check.py passing.

## Per line

### Line 1, Bubo bubo, eye axial length 30.9-31.35 mm

Discussion: "Eye axial lengths of eagle owls, were measured between 30.9 mm and 31.35 mm." followed by "In this respect, the eye axial lengths of eagle owls are similar to the Snowy owl species." **Quote MATCH**, whole sentence with the printed comma, 14 words. The value (a range) says no more than the quote. Animals: "The animal material consisted of 6 eagle owls"; age "considering their wing structures and body sizes, it was decided that the birds were of adult age"; method "axial lengths in mm with an optical biometric device" (no model named; ultrasonography "Opticon 2000, 15 MHz" used for anterior and posterior segments). Abstract "AGL 31.108±0.1773 mm"; Table 2 total 12 eyes 31.10±0.17. Primary paper.

Faults: (a) **Significant result omitted.** Results: "...there were no statistically significant differences between the right and left eyes (P>0.05) but" / "statistically significant difference were found in axial lengths values (P<0.05)."; Table 2 AL right eye (n = 6) 31.20±0.24, left eye (n = 6) 31.01±0.27, P 0.020. The conditions give only the pooled mean; the right-left difference, the one significant result in the axial-length data, is missing. (b) Sexes not given: Methods "In 4 birds (3 males, 1 female) used in the study had uninfected open wing wounds and 2 birds (1 male, 1 female) had closed fractures (radius)." and "The sex of the birds was estimated based on their body size." The conditions say only "sex estimated from body size only"; 4 males and 2 females (estimated) and the wing wounds and radius fractures are missing. (c) The note's "New trait" with no mention that the key and species are on main (above). One record error, fixable.

Not counted, for the owner: the printed range (width 0.45 mm) sits uneasily with Table 2's ± values if those are SEM (12 eyes, SEM 0.17 implies an SD near 0.6 mm); the page labels them SEM (tool summary). The record reports both as printed, which is right; the owner may want the note to flag it.

**Line 1 FIXABLE.**

### Line 2, Caecilia pulchraserrana, eyes not covered by bone

Description of new species, Generic assignment: "The new species is assignable to the genus Caecilia because its eyes are not covered by bone and it has tentacles below the nostrils (Type D sensu Lynch, 1999, Fig. 3 D–E)." **Quote MATCH** (stitched at a space, identical to the page; see Stitching), 32 words by check.py. Type material confirmed: holotype "IAvH-Am-15487 ... an adult female", type locality "Colombia, Santander Department, El Carmen de Chucurí Municipality, vereda La Belleza, Cascajales River," 789 m; paratypes IAvH-Am-15488 and UIS-MHN-A-6575 "adult females", IAvH-Am-15489–90 "adult males" (paratype locality 731 m); referred "UIS-MHN-A-6576–7 ... juveniles". Holotype eye sentence, Variation "Eye diameter 4–8% of the head length and 10–19% of eye-nostril distance.", Table 3 ED 0.2–0.4, "eyeballs completely violet blue (Fig. 4b)" all as in the conditions. Diagnosis has no eye wording; the Abstract has none (tool summary). The value restates the quote's species-level generic character. Conditions right. Not counted: the note says "29 words" and places the join "after 'tentacles'"; check.py counts 32 and the join is after "bone" (optional fix below).

**Line 2 MATCH.**

### Line 3, Ooceraea hainingensis, workers without eyes and ocelli

Description of the workers, Head: "Compound eyes and ocelli absent." after "Antennal sockets fully exposed." **Quote MATCH**, whole sentence. Holotype one worker, "China, Zhejiang, Haining, Qianjiang village, Yuemiao Mountain", "10.VI.2022"; paratypes "five workers from the same colony as the holotype". Queen: "Dealate queen (N = 1)", non-type (Fig. 3 caption), "compound eyes present approximately at mid-length of the head side; ocelli present and closely approximated"; "Male. Unknown."; Recognition "eyes absent in the worker caste"; Abstract "a queen caste with wings and well-developed eyes" (the conditions carry the queen's eyes; the Abstract wording adds nothing they lack). Value restricted to workers. Conditions right.

**Line 3 MATCH.**

### Line 4, Cincticostella jianchuan, male imago compound eyes contiguous

Male imago (in ethanol), Head: "Compound eyes contiguous, upper portion brown and lower portion black (Fig. 7B, D)." **Quote MATCH**, whole sentence with figure reference, 13 words. Holotype "male imago, with final nymphal instar exuviae (in ethanol)", Jinlong River, Jianchuan County, 2371 m, "09.V.2022"; paratypes "40 nymphs, 24 imagos and 20 subimagos reared from nymphs with same data as holotype". Female imago, nymph, both subimagos, Diagnosis, Abstract, Discussion and captions carry no eye wording (tool summary); the quoted sentence is the only one in the paper. Value limited to the male imago. Conditions right.

**Line 4 MATCH.**

### Line 5, Corydalus ralphi, three yellow ocelli ringed brown

Description, "Head (Figs 2A, C, 3A, C)": "Vertex infuscated, with three yellow ocelli each surrounded by darkish brown ring." after "Pale reddish brown, unpatterned." **Quote MATCH**, 12 words. The Head paragraph is a general (both-sex) description with sex-specific mandible sentences; the ocelli sentence is not sex-specific, and the Female mandible sentence is the only female head wording. Holotype "male, VENEZUELA: Bolívar, Parque Nacional Canaima, Gran Sabana, Río Tarotá ... 1,324 m a.s.l., 14.iii.2007"; "Paratype, female, same data as holotype". No genus-level ocelli or compound-eye wording in Introduction, Diagnosis, Comments or key; species-level only. Conditions right.

**Line 5 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Bubo bubo, eye axial length 30.9-31.35 mm | FIXABLE | conditions, note | right/left AL difference P = 0.020 omitted; 4 males, 2 females (estimated) and injuries missing; key and species already on main (40.3 mm, Olsson 2021) not said |
| 2 | Caecilia pulchraserrana, eyes not covered by bone | MATCH | | stitched text equals the page; types, variation, Diagnosis |
| 3 | Ooceraea hainingensis, workers eyeless | MATCH | | worker caste only; queen non-type with eyes; male unknown |
| 4 | Cincticostella jianchuan, male imago eyes contiguous | MATCH | | only eye sentence in the paper; types right |
| 5 | Corydalus ralphi, three yellow ocelli | MATCH | | general Head description; holotype male, paratype female |

Errors: 1 of 5 records (20%); 1 fixable (line 1), 0 held out, 0 unfixable; no line to drop. Answers to the unit's questions: eye_axial_length_mm stands (key in use on main; the paper measures axial length, so not eye_diameter_mm); blank family for Bubo bubo is acceptable when the page prints none. The rate is above 5%, so the unit merges by the drop-the-errors route: lines 2 to 5 as filed, line 1 with the replacements below (or dropped if they are not applied). Verdict: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 1:
- `note`: "New trait: eye_axial_length_mm (axial length of the globe, not an equatorial diameter; the key eye_diameter_mm is not used because the paper measures axial length)." -> "New trait: eye_axial_length_mm (key already in use on main; axial length of the globe, not an equatorial diameter; the key eye_diameter_mm is not used because the paper measures axial length). Main already holds Bubo bubo eye_axial_length_mm 40.3 mm (one eye of one animal, cryotome, Olsson et al. 2021, doi 10.1242/jeb.243129, oa-1); this is a separate measurement by a different method on live birds, not a repeat."
- `conditions`: "birds judged adult from wing structure and body size, sex estimated from body size only;" -> "birds judged adult from wing structure and body size; 4 males and 2 females, sex estimated from body size only ('In 4 birds (3 males, 1 female) used in the study had uninfected open wing wounds and 2 birds (1 male, 1 female) had closed fractures (radius).');"
- `conditions`: "The Discussion also says the axial lengths are similar to those of the Snowy owl." -> "The Discussion also says the axial lengths are similar to those of the Snowy owl. Right and left eyes differ: the Results say there were no significant right-left differences in the other measures 'but statistically significant difference were found in axial lengths values (P<0.05)', and Table 2 gives right eyes 31.20±0.24 mm and left eyes 31.01±0.27 mm (6 eyes each, P 0.020)."

Optional, not counted:
- Line 2 `note`: "Whole sentence, 29 words," -> "Whole sentence, 32 words as check.py counts," (and the join falls after "bone", not after "tentacles").
- Line 5 `source.authors`: "Azevêdo CAS" -> "de Azevêdo CAS" (the page's citation line prints "de Azevêdo CAS"; order is already right).
