# audit-399: desk-d305, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d305 files present untracked in the worktree (docs/tracks/progress/desk-d305.md and docs/views/evidence/desk-d305.jsonl, 16 lines; neither committed here, neither edited). This audit takes file lines 1 to 8 (1-based); lines 9 to 16 go to another auditor. Worktree based on origin/main (49380a173). `python3 -I tools/senses/check.py | grep d305`: "docs/views/evidence/desk-d305.jsonl: 16 records, 0 problems". Quote lengths (`len(q.split())`): 20, 19, 15, 14, 18, 5, 7, 12, all within 40.

Sources opened (WebFetch, every article URL from a WebSearch result): mdpi.com/1424-2818/16/12/737 (two passes); zookeys.pensoft.net/article/48723/download/xml/ (two passes); europeanjournaloftaxonomy.eu/index.php/ejt/article/download/2409/10653 (two passes); zookeys.pensoft.net/article_preview.php?id=111842; zookeys.pensoft.net/article/129685/download/xml/ (two passes); zookeys.pensoft.net/article/126337/download/xml/ (two passes) and article_preview.php?id=126337. Crossref single-DOI lookups (api.crossref.org/v1/works/) for all six DOIs, all read on the first call. Plazi, Zenodo, BHL, bionames, FishBase, PMC, DOAJ, uni-frankfurt and CONICET repository copies were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

Stitching: the two stitched quotes in my range were rechecked against the page. Line 1: the page returns "Median ocelli absent; two pairs of small lateral ocelli, posterolateral major (PLMa) and median lateral major (MLMa)," then "similar in size.", one sentence ending at the full stop. Line 2: "Median eyes situated anteriorly compared to centre of carapace;" then "three pairs of lateral ocelli with posterior-most one the smallest.", followed by the separate sentence "Median ocular tubercle, coarse with granules and a median furrow." Both joins fall at a space in the printed sentence; the joined text is what the page prints. Verbless sentences: lines 1, 2, 6, 7 and 8 quote telegraphic Description/Diagnosis sentences that run from a capital to a full stop and are not cut from longer sentences; under the audit-395 precedent (telegraphic Diagnosis sentence) they count as whole sentences.

## Bibliographic and licence

- Line 1 (Blasco-Aróstegui, Prendini 2024). Page and Crossref Javier Blasco-Aróstegui, Lorenzo Prendini; title identical; Diversity 16(12): 737; issued 2024-11-29. Page metadata gives only a rights link to CC BY 3.0; Crossref CC BY 4.0 vor. Accepted under the CC BY 3.0 page / CC BY 4.0 Crossref rule.
- Line 2 (Di, Qiao 2020). Page and Crossref Zhiyong Di, Sha Qiao; title identical; ZooKeys 968: 71-83, no issue; issued 2020-09-16; page CC BY 4.0 sentence, Crossref CC BY 4.0 vor. Accepted.
- Lines 3, 4 (Pereira, Gallão, Bichuette, Pérez-González 2024). Page byline "Maria Paula PEREIRA; Jonas E. GALLÃO; Maria E. BICHUETTE; Abel PÉREZ-GONZÁLEZ"; title identical; page prints "European Journal of Taxonomy 921: 36–63 (2024)"; Crossref no issue, issued 2024-01-31; page "This work is licensed under a Creative Commons Attribution License (CC BY 4.0)."; Crossref CC BY 4.0, content-version unspecified. Accepted. The Crossref spelling of the second author came back from the tool as "Galião" (tool summary), not the "Galão" the notes give; the record follows the page either way; uncounted.
- Line 5 (Hou, Zhang 2024). Page and Crossref Yanmeng Hou, Feng Zhang; title identical; ZooKeys 1204: 135-154; issued 2024-06-04; CC BY 4.0 page and vor. Accepted.
- Line 6 (Huang, Hibino, Balisco, Liao 2024). Page and Crossref Wen-Chien Huang, Yusuke Hibino, Rodulf Anthony Balisco, Te-Yu Liao; title identical; ZooKeys 1220: 15-34; issued 2024-12-09; CC BY 4.0 page and vor. Accepted.
- Lines 7, 8 (Hibino, Ho, Huang 2024). Page and Crossref Yusuke Hibino, Hsuan-Ching Ho, Jian-Fu Huang; title identical; ZooKeys 1220: 63-78; issued 2024-12-09; CC BY 4.0 page and vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

Lines 2, 4, 5, 6, 7, 8 are species described as new in the cited papers. Line 1 (Euscorpius studentium Karaman, 2020) is redescribed under that name in a 2024 paper; line 3 (Spaeleoleptes spaeleus) is the genus's type species, redescribed under that name. No sign of synonymy in the search results; WoRMS, GBIF and the World Spider/Scorpion catalogues not opened. Higher taxa as printed:
- Line 1: "Family Euscorpiidae Laurie, 1896"; no order or class printed (MDPI has no classification block). Right.
- Line 2: "Family Scorpiopidae Kraepelin, 1905". The Pensoft "Taxon classification" block under the species heading prints "Animalia", "Scorpiones", "Euscorpiidae" (order Scorpiones, also in the title). Order left empty. **Fault** (see below).
- Lines 3, 4: the Taxonomy section prints "Class Arachnida Lamarck, 1801", "Order Opiliones Sundevall, 1833", "Suborder Laniatores Thorell, 1876", "Family Escadabiidae Kury & Pérez-González in Kury, 2003". Class left empty and the note says "(no class heading)". **Fault** in each line.
- Line 5: "Family Pseudotyrannochthoniidae Beier, 1932"; order Pseudoscorpiones from the title; no class. Right.
- Line 6: classification block "Anguilliformes", "Muraenidae"; filled from it. Right.
- Lines 7, 8: classification blocks under both species print "Animalia; Anguilliformes; Ophichthidae"; order left empty and the notes say Anguilliformes "appears in the title only". **Fault** in each line.

On the order faults (lines 2, 7, 8): audit-397 accepted an empty order where the order appears in the title only. Here the order is printed a second time, in the species' own classification block, which is the source the unit itself used to fill line 6's order. Filled as printed means filled from it; the notes for 7 and 8 also misdescribe the page. Counted.

## Duplicates

`git grep -i` on origin/main (49380a173) over the whole docs/ tree for studentium, "Euscorpiops lii", spaeleus, gimli, tuoliangensis, "Uropterygius hades", kbalanensis, multidentis and the six DOI strings: the only hit is desk-d292.md's drop note for Euscorpiops lii (not a filed record), plus genus-level hits for other species (Euscorpius italicus, Spelaeochthonius yinae) and unrelated numeric matches of "48723" in gaps files. All 305 origin/research/desk-d* branches other than d305 grepped for the same species and DOI patterns under docs/: only the same d292 drop note. Duplicate faults 0.

## Per line

### Line 1, Euscorpius studentium, median ocelli absent, two pairs of small lateral ocelli

Description, Carapace: "Median ocelli absent; two pairs of small lateral ocelli, posterolateral major (PLMa) and median lateral major (MLMa), similar in size." **Quote MATCH.** The Description "is based on an adult male and an adult female" (tool summary), no Variation section, no sex difference in ocelli. Material examined 22.v.2024: "1 ♂, 1 ♀ (AMNH), 1 juv. ♂ (AMCC [LP 20621])"; holotype "1 subad. ♂ holotype (ZZDBE SC1/01)". Diagnosis contrast "in which the ocelli are present and fully developed"; Key "Median ocelli absent, lateral ocelli reduced."; Ecology and Discussion as the conditions say. Uncounted: the type material also has "1 juv. ♀ paratype (ZZDBE SC1/02)", not named in the conditions; it is not part of the redescription material.

**Line 1 MATCH.**

### Line 2, Euscorpiops lii, median eyes anterior, three pairs of lateral ocelli

Holotype Prosoma: the two pieces quoted above. **Quote MATCH.** Type material "Male holotype ... (Ar.-MHBU-XZLZ1901); 6 male and 13 female paratypes (including 1 male and 2 female immatures)". Diagnosis, Variation, Relationships and key without eye text (tool summary); caption "7, 8 eyes and nearby area". Conditions right. Fault: order empty though printed (Scorpiones in the classification block); note says "no order heading" without the block. Fixable.

**Line 2 FIXABLE.**

### Line 3, Spaeleoleptes spaeleus, reduced cornea, no visible retina

Male (holotype): "Ocularium rounded, with several small granules on the surface." / "Two eyes on the lateral surface of the ocularium with reduced cornea, no visible retina." **Quote MATCH.** Holotype ♂ MZUSP 28463, paratype ♀ MZUSP 28462 ("Ocularium with no small granules on the surface."). The Discussion's "the troglomorphic characteristics (cuticle depigmentation and eye reduction)" refers to S. gimli only, as the conditions say. Fault: class empty and note "(no class heading)" while the page prints "Class Arachnida Lamarck, 1801". Fixable.

**Line 3 FIXABLE.**

### Line 4, Spaeleoleptes gimli, two reduced eyes with cornea and retina

Male (holotype): "Two reduced eyes on the lateral surface of the ocularium, with cornea and retina." **Quote MATCH.** Holotype ♂ LES 00341; paratypes "1 ♂, 1 ♀ ... LES 027941" and "1 ♂ ... LES 027942 (SEM voucher)"; the female description does not mention eyes. Fault: class empty, as line 3. Fixable.

**Line 4 FIXABLE.**

### Line 5, Spelaeochthonius tuoliangensis, small eye spots

Discussion: "All 11 currently known Spelaeochthonius species are exclusively found within caves and are completely blind (WPC 2024)." then "Spelaeochthonius tuoliangensis sp. nov. represents the first epigean species of this genus with small eye spots (Fig. 9C)." **Quote MATCH.** Holotype female and one female paratype, 13 May 2018, "(male unknown)"; Diagnosis "visible eyespots"; Cephalothorax clause "with two pairs of eyespots and eye region bulging and convex in dorsal view".

Fault: the value "small eyespots (two pairs); epigean, unlike blind cave congeners" says more than the quote. "two pairs" is in the Cephalothorax clause, not in the quoted sentence; the value must say no more than the quote, and the count belongs in conditions. Fixable. Uncounted: the conditions call the paper's two other new species "sister" species; I did not read a phylogenetic statement either way, and "other" is the safer word (replacement offered).

**Line 5 FIXABLE.**

### Line 6, Uropterygius hades, eyes small and anteriorly placed

Diagnosis: "Anus at mid-length of body." / "Eyes small and anteriorly placed." / "Snout pointed." **Quote MATCH**, a whole telegraphic Diagnosis sentence. Holotype "NMMB-P039570 (349 mm TL, male)"; Description "Eyes small and anteriorly placed, closer to snout tip than to mouth corner,"; Abstract "anteriorly positioned small eyes (5.0–7.2% of head length)".

Faults in conditions: (a) "sexes of paratypes not given in the text read" is false: the paratype list gives four "mature female" (KAUM–I. 132509, KAUM–I. 153507, KMNH VR 100621, PNM 15806) and six "sex unknown"; the Diagnosis adds "female mature at 171 mm TL". (b) The 5.0–7.2% range is for "Paratypes & non-types", n = 13, three non-types included (AMS I.43866-001, ZRC 44083, ZRC 63518), not the type series alone. (c) The comparison is misdescribed: the Comparisons sentence reads "by its exclusively small eyes (5.0–7.2% vs 7.7–11.0% and 7.8–10.4% of HL)" against U. concolor (7.7–11.0) and U. mactanensis (7.8–10.4); the 7.8–9.2% figure is Table 1's "This study (Iriomote Island)" column (n = 2). (d) "not a cave species": the paper calls it estuarine, but paratype PNM 15806 was taken "inside the cave, about 50 m from the entrance of the Puerto Princesa Subterranean River"; the page does not use "brackish". One record error, fixable.

**Line 6 FIXABLE.**

### Line 7, Ophichthus kbalanensis, eye relatively small, 2.4 in snout length

Description: "completely covered by a wide dermal flap." / "Eye relatively small, 2.4 in snout length." / "Mouth subterminal, ...". **Quote MATCH.** Single holotype NMMB-P26381, 414 mm TL, Da-xi, Yilan, no paratypes, no sex. Diagnosis has no eye wording. Key couplet 9 "Eyes small to moderately large, less than 70% of snout length" (as the conditions say). Table 1: eye diameter 6.8% HL, snout 16.4% HL (tool summary).

Faults: (a) order empty though the classification block prints Anguilliformes; the note says it "appears in the title only". (b) Conditions say "The Comparison and Key use eye proportions relative to snout"; the Comparison's only eye wording is the rictus position "(behind posterior margin of eye vs not behind)" against O. obtusus; only the key uses the proportion. One record error, fixable.

**Line 7 FIXABLE.**

### Line 8, Ophichthus multidentis, eye moderate, 1.7–2.6 in snout length

Description: "Eye moderate in size, 1.7–2.6 (2.4 in holotype) times in snout length." **Quote MATCH**, en dash as printed (value uses a hyphen; acceptable). Holotype NMMB-P36205, 433 mm TL; paratypes TOU-AE 7802 (519), 8998 (554), 8999 (597), 9294 (696 mm TL); no sex; Diagnosis and Comparison without eye wording. Uncounted: Table 1 ratios (eye 8.6, 9.2, 8.3, 8.4, 9.1; snout 20.6, 20.1, 21.2, 18.8, 20.9% HL; tool summary) give 2.2 to 2.6, so the printed lower bound 1.7 is not borne out by the table; the record quotes what the text prints. Note too that both holotypes are 2.4 in snout length while the two species' eyes are worded "relatively small" and "moderate"; conditions name the contrast. Fault: order empty, note "Order appears in the title only", as line 7. Fixable.

**Line 8 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Euscorpius studentium, median ocelli absent, 2 pairs lateral | MATCH | | quote, adults of both sexes, contrasts given |
| 2 | Euscorpiops lii, median eyes anterior, 3 pairs lateral | FIXABLE | order, note | Scorpiones printed in classification block |
| 3 | Spaeleoleptes spaeleus, reduced cornea, no retina | FIXABLE | class, note | "Class Arachnida Lamarck, 1801" printed |
| 4 | Spaeleoleptes gimli, reduced eyes with cornea and retina | FIXABLE | class, note | as line 3 |
| 5 | Spelaeochthonius tuoliangensis, small eye spots | FIXABLE | value, conditions | "two pairs" not in quote |
| 6 | Uropterygius hades, eyes small, anterior | FIXABLE | conditions | paratype sexes printed; n=13 includes non-types; comparison taxa and ranges wrong; cave-caught paratype |
| 7 | Ophichthus kbalanensis, eye relatively small | FIXABLE | order, conditions, note | Anguilliformes in classification block; Comparison does not use eye/snout proportion |
| 8 | Ophichthus multidentis, eye moderate | FIXABLE | order, note | Anguilliformes in classification block |

Errors: 7 of 8 records (87.5%); 7 fixable (lines 2 to 8), 0 held out, 0 unfixable; no line to drop. Without the classification-block order faults (lines 2 and 8, and the order part of line 7) the count would be 5 of 8 (62.5%); the rate is far above 5% either way. Lines 1 to 8 merge by the drop-the-errors route: line 1 as filed, lines 2 to 8 with the replacements below (or dropped if the replacements are not applied). Verdict: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 2:
- `order`: `"order": ""` -> `"order": "Scorpiones"`
- `note`: "and no order heading." -> "and no order heading; the Taxon classification block prints 'Animalia, Scorpiones, Euscorpiidae', and the order is taken from it."

Line 3:
- `class`: `"class": ""` -> `"class": "Arachnida"`
- `note`: "(no class heading)" -> "(the Taxonomy section also prints 'Class Arachnida Lamarck, 1801' and 'Suborder Laniatores Thorell, 1876')"

Line 4:
- `class`: `"class": ""` -> `"class": "Arachnida"`
- `note`: "Order and family as printed in the headings (no class heading)." -> "Class, order and family as printed in the headings ('Class Arachnida Lamarck, 1801')."

Line 5:
- `value`: `"value": "small eyespots (two pairs); epigean, unlike blind cave congeners"` -> `"value": "small eye spots; first epigean species of the genus"`
- `conditions`: "The female Cephalothorax description and the Diagnosis ('visible eyespots') agree." -> "The female Cephalothorax description ('with two pairs of eyespots and eye region bulging and convex in dorsal view', a clause of a longer sentence) and the Diagnosis ('visible eyespots') agree."
- `conditions`: "The two sister new species" -> "The two other new species"

Line 6:
- `conditions`: "and 10 paratypes (163-313 mm TL); sexes of paratypes not given in the text read." -> "and 10 paratypes (163-313 mm TL) from Japan (Amami, Okinawa) and the Philippines: four mature females, six of unknown sex; the Diagnosis gives 'female mature at 171 mm TL'. One paratype (PNM 15806) was taken inside the cave of the Puerto Princesa Subterranean River, about 50 m from the entrance."
- `conditions`: "The Abstract gives eye diameter 5.0-7.2% of head length for the type series (holotype 5.2) and the comparison with U. cf. mactanensis (7.8-9.2%) and other congeners (7.7-11.0%) rests on that;" -> "The Abstract gives eye diameter 5.0-7.2% of head length; Table 1 gives this range for paratypes and three non-type specimens together (n = 13; holotype 5.2), and the Comparisons set it against U. concolor (7.7-11.0%) and U. mactanensis (7.8-10.4%);"
- `conditions`: "Brackish estuarine moray, not a cave species." -> "The paper describes it as inhabiting estuarine environments."

Line 7:
- `order`: `"order": ""` -> `"order": "Anguilliformes"`
- `conditions`: "The Comparison and Key use eye proportions relative to snout" -> "The Diagnosis has no eye wording; the Comparison with O. obtusus mentions the eye only for rictus position; the Key uses eye proportion relative to snout"
- `note`: "Anguilliformes appears in the title only." -> "Anguilliformes is printed in the title and in the Taxon classification block under the species heading."

Line 8:
- `order`: `"order": ""` -> `"order": "Anguilliformes"`
- `note`: "Order appears in the title only." -> "Order Anguilliformes is printed in the title and in the Taxon classification block under the species heading."
