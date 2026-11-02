# audit-402: desk-d306, evidence lines 7 to 12

Audited 1 November 2026 from the desk-d306 files present untracked in the worktree (docs/tracks/progress/desk-d306.md and docs/views/evidence/desk-d306.jsonl, 12 lines; neither committed here, neither edited). This audit takes file lines 7 to 12 (1-based); lines 1 to 6 go to another auditor. HEAD equals origin/main (23d6aba84). `python3 -I tools/senses/check.py | grep d306`: "docs/views/evidence/desk-d306.jsonl: 12 records, 0 problems". Quote lengths (`len(q.split())`): 17, 29, 13, 13, 13, 12, all within 40. The full printed Bathylychnops sentence counts 44 words (counted from the page text, figure reference included).

Sources opened (WebFetch, every article URL from a WebSearch result): nature.com/ncomms/2016/160119/ncomms10320/full/ncomms10320.html (three passes), frontiersin.org/articles/10.3389/fevo.2022.1044565 (three passes), zookeys.pensoft.net/article_preview.php?id=15061 (one pass), mdpi.com/2410-3888/9/6/213 (two passes), wsc.nmbe.ch species pages for Pinelema xiezi (56401) and P. spirulata (spec-data 62882), obis.org/taxon/273688 and two Catalog of Fishes pages (genus page and an unrelated species page; neither gave the Pholis fangi entry). Crossref single-DOI lookups api.crossref.org/v1/works/ for 10.1038/ncomms10320, 10.3389/fevo.2022.1044565 and 10.3390/fishes9060213 read on the first call; 10.3897/zookeys.734.15061 failed (client_error), retried once, failed again, not worked around (author order checked against the page byline instead). HAL, PMC, phys.org, City Research Online, scribd, core.ac.uk, Plazi, BHL and GBIF results were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 9 WebSearches.

Stitching: the Bathylychnops sentence came back as three consecutive pieces ("...roughly spherical main globe, with a dorsally positioned cornea" / "and lens collecting light from the dorsolateral field of view, and an extensive rostrolateral diverticulum" / "containing a sclerally derived lens gathering ventrolateral illumination." plus "(Figures 5a–d)"); asked directly, the tool gave the printed end as "gathering ventrolateral illumination (Figures 5a–d)." The joins fall at spaces in one printed sentence. The Dollocaris, Pinelema and Pholis sentences each came back as one piece.

## Bibliographic and licence

- Line 7 (Vannier, Schoenemann, Gillot, Charbonnier, Clarkson 2016). Page byline "Jean Vannier, Brigitte Schoenemann, Thomas Gillot, Sylvain Charbonnier & … Euan Clarkson" (the page collapses the list behind "Show authors"; first four and last shown in this order); Crossref lists exactly these five in this order. Title identical. Page: "Nature Communications volume 7, Article number: 10320 (2016)"; Crossref volume 7, issue 1, article 10320, issued 2016-01-19. No issue printed on the page, so "Nature Communications 7: 10320" is right. Licence: the page text read printed no CC sentence; Crossref CC BY 4.0 (vor and tdm); accepted under the publisher-page-plus-Crossref-vor rule.
- Line 8 (Wagner, Genner, Partridge, Chung, Marshall, Robison, Douglas 2022). Page byline and Crossref identical in order; title identical (colon, then "Ocular diverticula in barreleye spookfish (Opisthoproctidae)"); Frontiers in Ecology and Evolution 10, article 1044565, published 1 December 2022; no issue. Licence: no CC sentence in the page text read; Crossref CC BY 4.0 vor; accepted.
- Lines 9, 10 (Zhao, Pham, Song, Do, Li 2018). Page byline Huifeng Zhao, Pham Dinh-Sac, Yang Song, Thi-Duyen Do, Shuqiang Li; record order matches, and matches the d292 records of the same paper on main. Title identical; ZooKeys 734: 13–42 (2018), no issue. Page prints the CC BY 4.0 sentence; accepted. Crossref not read (two failures), so the notes' "Author order matches Crossref" is unchecked here; not counted.
- Lines 11, 12 (Liu, Zhang, Ji, Peng, Qin, Yao 2024). Page byline and Crossref identical in order; title identical; page "Fishes 2024, 9(6), 213"; Crossref volume 9, issue 6, article 213, issued 2024-06-03. Licence: page says "Creative Commons Attribution (CC BY) license", footer 4.0, metadata 3.0 (tool summary); Crossref CC BY 4.0 vor. Both tags are CC BY (3.0 against 4.0), accepted as on main (desk-d291 Arge similis note).

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Dollocaris ingens: the page refers only to "Thylacocephala" without a rank and prints no order or family; blank fields right.
- Bathylychnops exilis: Table 1 row "Bathylychnops exilis ( Cohen, 1958 )"; family from the title. **The page prints the order**: Introduction "Diverticula such as these are common in the Opisthoproctidae (aka barreleyes or spook fish), a remarkable family of argentiniform teleosts" and elsewhere "recovered a monophyletic Argentiniformes, comprising all Argentinidae, Bathylagidae, Microstomatidae, and Opisthoproctidae". The record leaves order blank: fault (fixable). No class printed ("teleosts" only).
- Pinelema spirulata and P. xiezi: World Spider Catalog lists both as "SPECIES | ACCEPTED" in Pinelema Wang & Li, 2012, authority Zhao & Li, 2018, no synonymy. Family heading "Family Telemidae Fage, 1913"; Araneae in the title only; no class heading. Right.
- Pholis fangi: OBIS taxon 273688 gives "Pholis fangi Wang & Wang, 1935" in Pholidae; a 2019 Zootaxa record uses the name (search result only); Catalog of Fishes species entry not reached. No sign of synonymy. **The page prints family and order**: Introduction "belongs to the order Perciformes, suborder Zoarcoidei, and family Pholidae." Both records leave family and order blank, and their notes say "Family and order not read from the page": fault (fixable), lines 11 and 12.

## Repeats

`git grep -i` on origin/main (23d6aba84) over the whole docs/ tree for Dollocaris, ncomms10320, Bathylychnops, fevo.2022.1044565, "Pinelema spirulata", "Pinelema xiezi", spirulata, xiezi, zookeys.734.15061, "Pholis fangi", fishes9060213. Hits: fevo.2022.1044565 in desk-d185.jsonl (other spookfish species), audit-269 and desk-d181 progress notes; spirulata, xiezi and zookeys.734.15061 only in audit-382 (a list of the paper's treatments) and desk-d292.jsonl (other Pinelema species, damtaoensis and others). No Dollocaris, Bathylychnops, Pinelema spirulata, P. xiezi or Pholis fangi record and no ncomms10320 or fishes9060213 DOI anywhere on main. All origin/research/desk-d* branches grepped in their docs/ files that differ from main: hits only in desk-d306 itself. Repeat faults 0.

Trait keys: `ommatidia_count` is already on main (desk-d270, d271, d272, d274, d291, d296, d297, d299, d302, oa-14, audit/ALL and audit/corrected), as is `eye_diameter_mm` (oa-1, oa-2, d280, d291, d292 and others). The unit's progress note calls ommatidia_count a "New trait"; main records with a key outside check.py's list write "new trait: ommatidia_count (key already in use on main)". Line 7's note has the "new trait" note; the missing "key already in use on main" is folded into the line 7 note replacement, not counted separately.

## Per line

### Line 7, Dollocaris ingens, more than 18,000 ommatidia per eye

Results, "Reconstructing the eye structure of Dollocaris": "This means that each eye (for example, see Fig. 2a) would have borne more than 18,000 ommatidia." after "The Dollocaris eye surface displays a dense, regular, hexagonal pattern of facets (Fig. 2b–e)" / "as in numerous modern insects and crustaceans, with an estimated density of more than 500 ommatidia per mm2" / "(Supplementary Note 1)." **Quote MATCH**, whole sentence, 17 words. The value (> 18000, per eye) says no more than the quote. Primary paper, not a review.

Fault: the record calls the number "a lower bound estimate" (note) and the conditions present it as derived from the density sentence only. The Discussion states how it was made and gives it as an approximation: "Each compound eye of Dollocaris has an exceptionally high number of ommatidia that can be estimated" / "to ∼18,000 on the basis of facet countings in well-preserved specimens and assuming that each eye" / "is approximately an hemisphere with evenly distributed ommatidia (Supplementary Note 1 and Supplementary Fig. 7)." The hemisphere assumption (a calculated, not counted, total) and the "∼18,000" wording are omitted, and "lower bound" is the unit's reading, not the paper's (the Abstract's "about 18,000 lenses on each eye" is in the conditions). Second part of the same fix: the conditions say the specimen number is "not stated in the text read"; the figure legends name eight Dollocaris ingens specimens (Fig. 1: MNHN.F.R50939, MHNL-20293244, MNHN.F.R06202, UJF-ID-1799, FSL 710067; Fig. 2: FSL 710064, the "complete specimen preserved in a nodule" of Fig. 2a, and MNHN.F.A29278; Fig. 4: FSL 710064 and MNHN.F.R06206); the Methods give repositories but no count, and the facet-counted specimens are not named (tool summary; Supplementary Note 1 not read). Facet "∼40 μm in diameter" confirmed. Not checked: "apposition eye" in the eye field (not counted). One record error, fixable.

**Line 7 FIXABLE.**

### Line 8, Bathylychnops exilis, bipartite eye

Results, Bathylychnops exilis: printed sentence "The eye of B. exilis examined here consisted of a roughly spherical main globe, with a dorsally positioned cornea and lens collecting light from the dorsolateral field of view, and an extensive rostrolateral diverticulum containing a sclerally derived lens gathering ventrolateral illumination (Figures 5a–d)." 44 words. The quote cuts "with a dorsally positioned cornea and lens collecting light from the dorsolateral field of view," and the trailing "(Figures 5a–d)." and marks both with "…"; the quoted text between the marks is verbatim and starts at the sentence's start. The cut clause describes the main globe's own optics and is not a qualifier of the value (which logs the globe's shape and the diverticulum with its lens); no spurious mark. **Quote ACCEPTED as cut.** Material: Table 1 row "200 | 580 | 7.5 | 9.2 | 4.5 | 400–600 | North Atlantic" / "RRS Discovery 243 | Histology | Figures 5, 6"; Methods "were caught specifically for this study" for O. soleatus, W. telescopa, B. exilis and M. microstoma, "All animals were caught using rectangular midwater trawls" (tool summary for the species list). One animal, one eye. Conditions right on these points.

Faults: (a) order blank although the page prints Argentiniformes (above). (b) Contrasting wording omitted: the conditions cite the Figure 10 legend's "characterised by a prominent, sclerally derived, lens" but not its next sentence, "The light rays entering the diverticulum ventrolaterally are shown as focussed on the diverticula retina" / "on the unproven assumption that the scleral lens is sufficiently refractive.", nor the Abstract's hedge that the diverticula form images "using either reflection or possibly refraction" (tool returned the quoted phrase). The value calls the structure a lens; the paper says its refractive function is unproven. One record error, fixable.

**Line 8 FIXABLE.**

### Line 9, Pinelema spirulata, six eyes

Male Description: "Six eyes encircled by black rings, clypeus 0.08 long, ocular quadrangle 0.15 wide." **Quote MATCH.** Type material: holotype male, Lap Cave, Xuan Son National Park, Phu Tho Province, 403 m, 2.X.2012; paratypes 3 males and 5 females, same data. Female Description "Six eyes, clypeus 0.09 long, ocular quadrangle 0.17 wide." Diagnosis has no eye wording (embolus only); no Remarks. Genus Comments "Six eyes are normally developed, vestigial, or in some species are completely absent." Conditions right.

**Line 9 MATCH.**

### Line 10, Pinelema xiezi, six eyes

Male Description: "Six eyes encircled by black rings, clypeus 0.15 long, ocular quadrangle 0.19 wide." **Quote MATCH.** Type material: holotype male, Tien Son Cave, Phong Nha-Ke Bang National Park, Quang Binh Province, 102 m, 17.V.2016; paratypes 3 males and 5 females, same data. Female Description "Six eyes, clypeus 0.12 long, ocular quadrangle 0.18 wide." Diagnosis has no eye wording; no Remarks. Conditions right.

**Line 10 MATCH.**

### Line 11, Pholis fangi, eye diameter 0.29 mm, flexion larva

Results, flexion larva: "The total length is 10.65 mm, with the body length at 10.31 mm." ... "The head length is 1.28 mm, representing 12.4% of the body length." then "The eye diameter is 0.29 mm, making up 22.7% of the head length." **Quote MATCH**, whole sentence. Stage counts as the conditions give (6 yolk-sac, 67 preflexion, 182 juveniles, no flexion count); no measurement table; the Abstract, Discussion and Conclusions do not mention the eye (asked directly), so the conditions' "no comparison" is right.

Faults: (a) family and order blank although printed (above). (b) Measuring basis incomplete: the conditions say the specimen identity is an inference "which the text does not state", but the Figure 3 and 4 legends print "(d,e) 10.31 mm BL flexion larva" / "(d) 10.31 mm BL flexion larva"; and the Methods (tool summary) give a Nikon SMZ 25 stereomicroscope and list eye diameter among the measurements without defining it, which the conditions do not say (method field says only "microscope measurement"). One record error, fixable.

**Line 11 FIXABLE.**

### Line 12, Pholis fangi, eye diameter 1.41 mm, juvenile

Results, juvenile: "Body length varies from 32.64 to 43.86 mm (n = 182), with a total length of 43.45 mm and a body length of 39.82 mm." ... "The head length measures 3.92 mm, constituting 9.8% of the body length." then "The eye diameter is 1.41 mm, representing 36% of the head length." **Quote MATCH**, whole sentence.

Faults: (a) family and order blank (above). (b) Stage and n misstated: the conditions tie the value to "the juvenile stage (body length 32.64-43.86 mm, n = 182)" and say the text "does not say whether it is a mean or one fish". The paragraph names one fish after the range ("a total length of 43.45 mm and a body length of 39.82 mm"), and the figure legends print "(f) 39.82 mm BL juvenile" and "(e) 39.82 mm BL juvenile"; 1.41/3.92 = 36%, the printed ratio for that fish's head length. The value is one 39.82 mm BL juvenile, not a stage value over 182 fish. Measuring basis missing as in line 11. One record error, fixable.

**Line 12 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 7 | Dollocaris ingens, > 18,000 ommatidia per eye | FIXABLE | note, conditions | Discussion's "∼18,000" from a hemisphere assumption omitted, called a lower bound; eight figured specimens not given |
| 8 | Bathylychnops exilis, bipartite eye | FIXABLE | order, conditions, note | Argentiniformes printed; "unproven assumption that the scleral lens is sufficiently refractive" omitted |
| 9 | Pinelema spirulata, six eyes | MATCH | | quote, types, female wording, genus Comments |
| 10 | Pinelema xiezi, six eyes | MATCH | | quote, types, female wording, genus Comments |
| 11 | Pholis fangi, eye 0.29 mm, flexion larva | FIXABLE | family, order, note, conditions | Pholidae and Perciformes printed; specimen named in legends; measuring basis |
| 12 | Pholis fangi, eye 1.41 mm, juvenile | FIXABLE | family, order, note, conditions | Pholidae and Perciformes printed; value is one 39.82 mm BL juvenile, not n = 182 |

Errors: 4 of 6 records (66.7%); 4 fixable (lines 7, 8, 11, 12), 0 held out, 0 unfixable; no line to drop. Answers to the unit's questions for my lines: a lower-bound reading of "more than 18,000" is supportable from the Results sentence, and value_relation ">" may stay, but the record must carry the Discussion's "∼18,000" and its hemisphere assumption; the Bathylychnops cut is acceptable. The rate is above 5%, so lines 7 to 12 merge by the drop-the-errors route: lines 9 and 10 as filed, lines 7, 8, 11 and 12 with the replacements below (or dropped if the replacements are not applied). Verdict: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 7:
- `note`: "(per eye, fossil, a lower bound estimate)" -> "(key already in use on main; per eye, fossil, an estimate: 'more than 18,000' in the Results, '∼18,000' in the Discussion)"
- `conditions`: "three-dimensionally preserved specimens (the number is not stated in the text read)." -> "three-dimensionally preserved specimens; the text gives no count, and the figure legends name eight Dollocaris ingens specimens (MNHN.F.R50939, MHNL-20293244, MNHN.F.R06202, UJF-ID-1799, FSL 710067, FSL 710064, MNHN.F.A29278, MNHN.F.R06206), Fig. 2a being FSL 710064; the facet-counted specimens are not named in the text read."
- `conditions`: "and the Discussion calls it" -> "and the Discussion gives the number as estimated 'to ∼18,000 on the basis of facet countings in well-preserved specimens and assuming that each eye is approximately an hemisphere with evenly distributed ommatidia' (a calculated total, not a count), and calls it"

Line 8:
- `order`: empty -> fill with "Argentiniformes"
- `conditions`: "the Figure 10 legend calls the rostrolateral diverticulum 'characterised by a prominent, sclerally derived, lens'." -> "the Figure 10 legend calls the rostrolateral diverticulum 'characterised by a prominent, sclerally derived, lens' and shows light focused on the diverticular retina only 'on the unproven assumption that the scleral lens is sufficiently refractive'; the Abstract says the diverticula form images 'using either reflection or possibly refraction'."
- `note`: "Family from the paper's title;" -> "Family from the paper's title; order from the text ('a remarkable family of argentiniform teleosts'; 'a monophyletic Argentiniformes, comprising all Argentinidae, Bathylagidae, Microstomatidae, and Opisthoproctidae');"

Line 11:
- `family`: empty -> fill with "Pholidae"
- `order`: empty -> fill with "Perciformes"
- `note`: "Family and order not read from the page." -> "Family and order from the Introduction ('belongs to the order Perciformes, suborder Zoarcoidei, and family Pholidae')."
- `conditions`: "apparently one specimen (the 10.31 mm body length matches the specimen in Figure 3d,e, which the text does not state)." -> "one specimen, which the Figure 3 and 4 legends label '10.31 mm BL flexion larva'. Measured under a Nikon SMZ 25 stereomicroscope; the Methods list eye diameter among the measurements but do not define it."

Line 12:
- `family`: empty -> fill with "Pholidae"
- `order`: empty -> fill with "Perciformes"
- `note`: "Family and order not read from the page." -> "Family and order from the Introduction ('belongs to the order Perciformes, suborder Zoarcoidei, and family Pholidae')."
- `conditions`: "This value is for the juvenile stage (body length 32.64-43.86 mm, n = 182; head length 3.92 mm); the text gives a single value and does not say whether it is a mean or one fish." -> "This value is for one juvenile: the paragraph gives the stage range (body length 32.64-43.86 mm, n = 182) and then 'a total length of 43.45 mm and a body length of 39.82 mm', the fish the Figure 3 and 4 legends label '39.82 mm BL juvenile'; its head length is 3.92 mm and the eye is 36% of it. Measured under a Nikon SMZ 25 stereomicroscope; the Methods list eye diameter among the measurements but do not define it."

Optional, not counted (lines 9, 10): the notes' "Author order matches Crossref" could read "Author order matches the page byline" (Crossref for this DOI could not be read in this audit).
