# audit-407: desk-d309, evidence file lines 15 to 20

Audited 1 November 2026 from the desk-d309 files present untracked in the worktree (docs/tracks/progress/desk-d309.md and docs/views/evidence/desk-d309.jsonl, 20 lines; neither committed here, neither edited). This audit judges file lines 15 to 20 only (two other auditors take 1 to 7 and 8 to 14). The progress note's numbered list is offset from the file: file lines 15 and 16 are Asymmetrione tuxtlaensis, 17 Abyssomysis cornuta, 18 Mesembrius arcuatus, 19 and 20 Protanilla gengma. HEAD equals origin/main (d87091c8f). `python3 -I tools/senses/check.py | grep d309`: "docs/views/evidence/desk-d309.jsonl: 20 records, 0 problems". Quote lengths (`len(q.split())`): 12, 18, 18, 15, 11, 11, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): europeanjournaloftaxonomy.eu/index.php/ejt/article/download/2073/8655 (publisher PDF, four passes), .../download/903/2157 (publisher PDF, one pass; text ends on p. 31, the Abyssomysis account is complete in it), .../article/view/2867 (one pass) and .../download/2867/13025/ (publisher PDF, two passes), zookeys.pensoft.net/article_preview.php?id=57052 (two passes). Crossref single-DOI lookups api.crossref.org/v1/works/ for all four DOIs, each read on the first call. AntCat "Protanilla gengma Xu, 2012 valid" and the Plazi treatment "Asymmetrione tuxtlaensis, Romero-Rodriguez & Álvarez, 2023" seen as search-result titles only. Plazi, Zenodo, DOAJ, sciencepress.mnhn.fr, Frankfurt repository, bionames and biomed.reviewer.ly results were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Bibliographic and licence

- Lines 15 and 16 (Romero-Rodriguez, Álvarez 2023). PDF byline Jesús Romero-Rodriguez and Fernando Álvarez; Crossref same order. Title identical (Crossref splits it at the comma only as a display artefact). Citation line "European Journal of Taxonomy 861: 132–167", 2023; Crossref volume 861, page 132–167, no issue. Licence printed "This work is licensed under a Creative Commons Attribution License (CC BY 4.0)."; Crossref CC BY 4.0, content-version unspecified. Accepted. The page range was read and can be filled (optional, below).
- Line 17 (Wittmann 2020). Byline Karl J. Wittmann; Crossref same. Title identical apart from straight/curly quotes (note says so). Citation line "European Journal of Taxonomy 628: 1–43"; Crossref issue 628, no volume, no page. Licence sentence printed as above; Crossref CC BY 4.0 unspecified. Accepted. Page range optional below.
- Line 18 (Jordaens, Goergen, Skevington, Kelso, De Meyer 2021). Byline and Crossref identical in order; title identical; ZooKeys 1046: 1-141, issued 2021-06-21, no issue. Page "distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)"; Crossref CC BY 4.0 vor. Accepted.
- Lines 19 and 20 (Griebenow, Richter, Economo, Dang, Yamada 2025). Byline and Crossref identical in order; title identical; EJT 987: 98–145, 2025 (article view page); Crossref volume 987, no issue. The article view page carries no licence sentence (tool summary); the publisher PDF is the copy read and the unit's note cites its CC BY 4.0 sentence; Crossref CC BY 4.0 unspecified. Accepted under the publisher's-own-free-full-text clause.

Bibliographic faults counted 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Asymmetrione tuxtlaensis: described in this paper; Plazi treatment under the same name in results. Headings printed "Suborder Cymothoida Wägele, 1989", "Family Bopyridae Rafinesque, 1815", "Subfamily Pseudioninae Codreanu, 1967"; no Order Isopoda or Class Malacostraca heading anywhere (asked directly; tool answered none). Family filled, order and class blank: right.
- Abyssomysis cornuta: described in this paper; headings "Order Mysida Boas, 1883", "Family Mysidae Haworth, 1825" (subfamily Erythropinae, tribe Calyptommini); no class heading ("Crustacea" only in the title). Right.
- Mesembrius arcuatus: described in this paper; no Taxon classification line under any species heading (asked directly); title "(Diptera, Syrphidae)". Order and family from the title, class blank: right.
- Protanilla gengma: AntCat "Protanilla gengma Xu, 2012 valid" (result title). Headings printed "Class Insecta Linnaeus, 1758", "Order Hymenoptera Linnaeus, 1758", "Family Formicidae Latreille, 1802". Right.

## Repeats

`git grep -il` on origin/main (d87091c8f) over the whole docs/ tree for tuxtlaensis, Asymmetrione, 2023.861.2073, Abyssomysis, ejt.2020.628, "Mesembrius arcuatus", zookeys.1046.57052, "Protanilla gengma", gengma, 2025.987.2867, and at genus level Mesembrius, Protanilla, Abyssomysis, Asymmetrione: no hits. Unmerged origin/research/desk-d* branches (309) grepped in docs/ for the same species and DOIs: see the line below the verdict table.

Shape statements under eye_type: main files such statements under eye_type ("large eye, cornea globular and well pigmented", Palaumysis jetama; "small eye, round pupil", Toxicocalamus longhagen; "divided compound eye; dorsal division as large as the ventral division (male)", Blepharicera balangshana; "round eyes with star-shaped eye pigment", Flaccisagitta enflata). Line 20 ("large ... and oval") and line 18 (holoptic) fit that use; line 17 (rudiments) fits the reduced-eye rows.

## Per line

### Line 15, Asymmetrione tuxtlaensis, female eyes at ventral anterolateral head edges

Description "Based on female holotype", Head paragraph (opens "Head. Ovoid, surface smooth, distinct from first pereomere."; sentence before the eye sentence "Frontal lamina broad, bent upwards with medial notch and two semi-triangular lobes, anterolateral corners rounded."): "Eyes at ventral anterolateral edges of head, barely visible dorsally (Fig. 7A)." **Quote MATCH**, whole telegraphic Description sentence (precedent audit-395), 12 words, figure reference kept. Holotype CNCR-36493-A1, ovigerous female 2.86 mm, Montepío, Los Tuxtlas, Veracruz, 19 Feb. 1996, on a female Clibanarius antillensis: as in conditions. Diagnosis and Remarks have no eye wording for this species (tool summary); bopyridium "conspicuous eyes at mid-lateral margin of head." and the Stegias clibanarii female "small eyes on the anterolateral margins of head (Fig. 5A)" are carried, right. Value restates the quote.

Fault: **specimen material misstated.** Conditions say "plus paratype pairs from several Veracruz and Quintana Roo localities (1959 to 2016)". The Material examined lists 16 paratype lots of 28 specimens (tool summary from the lot list): 12 lots are an ovigerous or adult female with a male, but CNCR-36498-A is a juvenile female with a cryptoniscus larva, CNCR-36498-B and CNCR-36492-A are single cryptoniscus larvae, CNCR-36492-B is the bopyridium and CNCR-36500 a single female detached from its host. "Pairs" hides the juveniles and larval stages, which matter here because the eye state differs by stage (the bopyridium's conspicuous eyes). Years 1959 to 2016 right. One record error, fixable.

**Line 15 FIXABLE.**

### Line 16, Asymmetrione tuxtlaensis, male eyes conspicuous on posterolateral edges

Male (allotype) description: "Head. Ovoid with anterior margin straight, nearly fused to first pereomere medially, conspicuous eyes on posterolateral edges (Fig. 8A)." "Head." is a run-in label, so the quote opening at "Ovoid" is the whole sentence. **Quote MATCH**, 18 words; the eye clause came back verbatim ("conspicuous eyes on posterolateral edges (Fig. 8A).") and the start was confirmed. Allotype CNCR-36493-A2, male 1.58 mm, same data as holotype: right. Separate sex and trait state from line 15, not a repeat of it.

Fault: the same "paratype pairs" text as line 15. One record error, fixable.

**Line 16 FIXABLE.**

### Line 17, Abyssomysis cornuta, horn-like eyestalk rudiments on an eyeplate

Holotype description (Fig. 5A): "Eyes without visual elements." then "Small, horn-like rudiments of eyestalks widely set apart on a common eyeplate probably homologous to the ocular symphysis." then a sentence beginning "Eyeplate dorsally covered by rostral plate". **Quote MATCH**, whole sentence, 18 words; "probably" kept in the quote and named in the conditions. Holotype adult male BL 6.6 mm, ZMH 58250, station #350, 5433–5434 m, 29 Jul. 2000; paratypes 9 (4 males, 5 females, adult and immature, 3.4 to 8.0 mm) from stations 344, 348 and 350: as in conditions. Genus diagnosis "eyeplate formed by a transverse, median lamina (= ocular symphysis) connecting separate, rudimentary eyestalks" and "visual elements absent" is genus-level and not filed; the species sentence is filed, right. Discussion "the horns and lappets are here interpreted as remnants of convergent eye reduction" carried. Conditions right.

**Line 17 MATCH.**

### Line 18, Mesembrius arcuatus, male eyes holoptic

Description (male), Head: "Eyes bare; holoptic, length of eye contiguity equal to approx. the length of ocellar triangle." **Quote MATCH**, 15 words, semicolon as printed. Differential diagnosis "The male of Mesembrius arcuatus sp. nov. is holoptic." and "The female is unknown."; Female heading "Unknown.". Holotype Entebbe, 21.8.11, C.C. Gowdey, NHMUK; 28 male paratypes from Entebbe, N.E. side of Lake Albert (1906), "?Kanue", Mbarara, near Entebbe (1972, 1973) and Mabamba Swamps (2018): count, sex and years right; "?Kanue" (uncertain locality, one male) is not named but nothing stated is wrong. M. caffer "Eyes bare; slightly dichoptic, distance between eyes approx. the width of ocellus." carried. Value adds "(meeting on the midline)" as a gloss of holoptic, which the quote's "eye contiguity" supports.

Not counted: the conditions say "The Variation text read has no remark on eye contiguity"; the M. arcuatus account has no Variation section at all (Variation exists only under M. caffer). Optional fix below.

**Line 18 MATCH.**

### Line 19, Protanilla gengma, gyne compound eye with 12 ommatidia

Gyne description: "Compound eye anteroposteriorly compressed, small (REL = 10), with 12 ommatidia." **Quote MATCH**, 11 words, telegraphic Description sentence. Material: Cuc Phuong NP, 8 Aug. 2022, 4 workers, 1 gyne CASENT0842884, 30 larvae; Tay Yen Tu, 30 Mar. 2003, 2 males, 1 worker, 1 gyne CSUENT6000047; 27 May 2004, 1 worker: as in conditions. Diagnosis "As for worker, but with compound eye." quoted right; workers never described with eyes, inference flagged as inference. No genus-level eye sentence. Per eye or both: value and conditions say not stated, right. Not a repeat of line 20: different caste (gyne vs male) and different trait (count vs eye form).

Faults: (a) **caste mislabelled.** The `eye` field calls the female a "winged-form queen without alar sclerites". The paper says the opposite of winged: Description "As for worker, completely lacking alar sclerites, but somewhat larger (WL = 1.05–1.07 mm) and with compound eye (Fig. 5B)."; Remarks "The ergatogyne here described is the first reproductive female documented for the Protanilla bicolor species-group." and "alar sclerites are completely lacking in the ergatogyne of P. gengma."; the Remarks contrast it with "Most Protanilla gynes are alate". (b) **variation omitted.** The measurement line "Gyne (n = 2)" gives "REL = 8–10", while the conditions quote only the description's REL = 10 and do not say the two gynes differ or that the paper does not say which gyne gave the 12-ommatidia count. One record error, fixable.

**Line 19 FIXABLE.**

### Line 20, Protanilla gengma, male compound eyes large and oval

Male description: "Compound eyes large (REL = 53–57), oval; all margins weakly convex." **Quote MATCH**, 11 words, en dash as printed. Male measurement sample n = 2; 2 males in the material: right. Value restates the quote. Shape and size wording fits eye_type as main uses it.

Not counted: the conditions say "The male has no ocellar tubercle (previous sentence)". The male description does print "Ocellar tubercle absent.", but the sentence before the eye sentence is "Occipital carina present only dorsally."; and the conditions' gyne aside gives REL = 10 only, not the measured 8–10, and does not carry the ergatogyne wording. Optional fixes below.

**Line 20 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 15 | Asymmetrione tuxtlaensis, female eyes ventral anterolateral | FIXABLE | conditions | paratypes called "pairs"; 16 lots, 28 specimens incl. juveniles, cryptoniscus larvae, bopyridium |
| 16 | Asymmetrione tuxtlaensis, male eyes conspicuous | FIXABLE | conditions | same paratype misstatement |
| 17 | Abyssomysis cornuta, eyestalk rudiments | MATCH | | holotype sentence, "probably" kept; types right |
| 18 | Mesembrius arcuatus, male holoptic | MATCH | | 28 male paratypes, female unknown, caffer contrast carried |
| 19 | Protanilla gengma, gyne 12 ommatidia | FIXABLE | eye, conditions | female called "winged-form queen" though the paper's ergatogyne lacks alar sclerites; gyne REL 8–10 (n = 2) omitted |
| 20 | Protanilla gengma, male eyes large, oval | MATCH | | male n = 2; separate caste from line 19 |

Errors: 3 of 6 records (50%); 3 fixable (lines 15, 16, 19), 0 held out, 0 unfixable; no line to drop. Repeats: none on main for any species, genus or DOI. Answers to the unit's questions as they touch these lines: telegraphic Description sentences (lines 15 to 20) are whole sentences under the audit-395 precedent; the line 16 quote starts after a run-in "Head." label, which is acceptable. The rate is above 5%, so this sixth merges by the drop-the-errors route: lines 17, 18 and 20 as filed, lines 15, 16 and 19 with the replacements below (or dropped if they are not applied). Verdict for lines 15 to 20: **ACCEPT AFTER REPLACEMENT**.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 15:
- `conditions`: "plus paratype pairs from several Veracruz and Quintana Roo localities (1959 to 2016)." -> "plus 16 paratype lots (28 specimens) from several Veracruz and Quintana Roo localities (1959 to 2016): 12 lots are an adult female (mostly ovigerous) with a male, the others hold a juvenile female with a cryptoniscus larva, two single cryptoniscus larvae, the bopyridium (CNCR-36492-B) and a single female detached from its host."

Line 16:
- `conditions`: "plus paratype pairs from several Veracruz and Quintana Roo localities (1959 to 2016)." -> "plus 16 paratype lots (28 specimens) from several Veracruz and Quintana Roo localities (1959 to 2016): 12 lots are an adult female (mostly ovigerous) with a male, the others hold a juvenile female with a cryptoniscus larva, two single cryptoniscus larvae, the bopyridium (CNCR-36492-B) and a single female detached from its host."

Line 19:
- `eye`: "compound eye, gyne (winged-form queen without alar sclerites)" -> "compound eye, gyne (the paper's ergatogyne, a reproductive female 'completely lacking alar sclerites')"
- `conditions`: "The eye is described as small (REL = 10) against 'large (REL = 53-57)' in the male." -> "The eye is described as small (REL = 10) against 'large (REL = 53-57)' in the male; the gyne measurements (n = 2) give 'REL = 8–10', so the two gynes differ in relative eye length, and the paper does not say which gyne gave the 12-ommatidia count. The Remarks call this female an ergatogyne: 'alar sclerites are completely lacking in the ergatogyne of P. gengma', against 'Most Protanilla gynes are alate'."

Optional, not counted:
- Line 15 and line 16 `source.journal`: "\"journal\": \"European Journal of Taxonomy 861\"" -> "\"journal\": \"European Journal of Taxonomy 861: 132-167\"" (citation line and Crossref).
- Line 17 `source.journal`: "\"journal\": \"European Journal of Taxonomy 628\"" -> "\"journal\": \"European Journal of Taxonomy 628: 1-43\"" (citation line); the note's "page range not read" then goes.
- Line 18 `conditions`: "The Variation text read has no remark on eye contiguity." -> "The M. arcuatus account has no Variation section (the paper's Variation text is under M. caffer)."
- Line 20 `conditions`: "The male has no ocellar tubercle (previous sentence)." -> "The male description also says 'Ocellar tubercle absent.' (the sentence before the eye sentence is 'Occipital carina present only dorsally.')."
- Line 20 `conditions`: "The gyne eye is small (REL = 10) with 12 ommatidia." -> "The gyne eye is small (REL = 10 in the description, 8–10 in the measurements of n = 2) with 12 ommatidia; the paper calls this female an ergatogyne completely lacking alar sclerites."
