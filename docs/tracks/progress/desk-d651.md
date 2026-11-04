# desk-d651 progress

Angle: eye_diameter_mm (trait key as on main, evidence_kind anatomical_measurement) for pupil_shape-vetted reptile and amphibian species with no eye_diameter_mm row on main and not tried in d646 or d647. Started 4 November 2026. Log: docs/views/evidence/desk-d651.jsonl, 6 records; check.py 0 problems for this file (plain and --require-evidence-kind). About 14 WebSearches (the pool ran out), no classifier denial, no Crossref, Plazi, zenodo, PMC, zobodat or blog fetch, no typed URLs, no proxy hosts. Scratch folder deleted.

Pool computed from main: pupil_shape rows (any unit, non-dataset sources) for species with no eye_diameter_mm row: 23 taxa; all but three were settled by d646 or d647. The untried three were Pareas orientalis, Pareas dabieshanensis and Odorrana calciphila.

## Filed
- Odorrana calciphila (ZSE 101(3): 935-952, 10.3897/zse.101.142746): Table 2 whole rows (specimens as rows, ED the tenth cell), holotype SYS a009287 (male) ED 4.7 and five adult female paratypes SYS a008923 5.5, a009288 4.7, a009289 4.7, a009290 5.5, a009295 5.4. Methods define ED (anterior to posterior corner of the eye), 0.1 mm caliper, caption in mm. ASW page opened from my own results (no explicit validity line).

## Weak spots
- Text through the WebFetch page reader (Pensoft article_preview and XML, read to 100000 of 100516 characters). The reader returned only the opening of the licence sentence ('...Creative Commons Attribution License (CC BY 4.0),') and a paraphrase; stated in each note. Table 2 column order from the reader; paratype rows read in a second fetch, species cell 'O. calciphila sp. nov.' shown for all six rows.
- The XML copy is truncated (ends in Results), so the Methods text came from the preview page and XML together.

## Not filed and why
- Pareas orientalis and P. dabieshanensis (ZSE 101(4)): Methods define ED, but Table 2 prints only species ranges (P. dabieshanensis 2.53-2.87, n = 3; P. orientalis 2.27-3.1, n = 9, no mean) and the holotype descriptions give no ED; specimen tables are supplementary. A range with no mean has no single value.
- Theloderma woltersi (RBZ 72: 252-267, publisher PDF at lkcnhm.nus.edu.sg opened): pupil circular, holotype ED 3.3 mm, Table 3 ED row printed, but the page text shows only '© National University of Singapore', no Creative Commons sentence; not filed.
- Phyllodytes gravata (EJT 1048): ED defined only as 'ED = eye diameter'; the holotype text gives ratios only; Table row 'ED 2.2 2.2 ± 0.1 (1.8-2.3) 2.7' has a garbled header (names MZUESC 23889 and 23891 together; text says 23891 is the holotype) so the column of each value is unsafe.
- Scutiger kanjiroba (ZooKeys 1210): Methods define 'horizontal diameter of eye (ED)' but the page prints no mm value (only EHD/HL 0.4); table S6 is supplementary.
- Boulenophrys youran (ZSE 102(1)): only figure pages and PMC in results; mm table supplementary (as d647).
- Odorrana nagao (ZooKeys 1280): already on main (eye_diameter_mm desk-d512, sensory_anatomy desk-d624, pupil desk-d629).
- All other pupil-vetted species without an ED row (Cyrtodactylus arnei, C. jayadityai, C. menglianensis, C. zhenkangensis, Lycodon walli, L. irwini, Bungarus suzhenae, Vietnamophryne abscondita, Micryletta, Microhyla, Amnihyla, Boulenophrys lichun, Theloderma khoii, Goniurosaurus wuzhengjuni) were settled by d646 and d647 (no ED definition, EL or OD only, ear diameter, conflicts); not searched again.

## Desk disposition after audits (4 November 2026)
Six Odorrana calciphila eye_diameter_mm lines audited by one fresh Opus agent (1359): 0 counted errors, 18 fixable faults (3 per line: paraphrased licence sentence replaced by the whole printed sentence, ASW comment added, Variation heading path completed); all six merged. Raw fault rate far above 5%, a standing owner question. No unit slip and no classifier denial; the unit stopped at about 14 searches because the pupil-vetted pool without an ED row is used up. Not fileable: Pareas orientalis and P. dabieshanensis (Table 2 gives only ranges), Theloderma woltersi (NUS copyright line, no Creative Commons sentence), Phyllodytes gravata (ED undefined beyond the abbreviation, garbled table header), Scutiger kanjiroba and Boulenophrys youran (mm tables supplementary).
