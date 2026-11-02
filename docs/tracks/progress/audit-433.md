# Audit 433: desk-d322, lines 1 to 8

Auditor: fresh Opus, 1 November 2026. Scope: 1-based lines 1-8 of docs/views/evidence/desk-d322.jsonl (lines 9-10 go to another auditor). Pages opened myself: Pensoft article_preview and article XML for ZooKeys 795 (28036), 892 (39033), 1215 (129410), 1232 (145622) and 1218 (136555), all URLs from WebSearch results. Crossref single-DOI lookups: 795, 1215, 1232 and 1218 returned CC BY 4.0 (vor), author order, volume and pages matching the page; 892 failed at the site (client_error), so its licence rests on the CC BY 4.0 sentence printed in the article XML. World Spider Catalog: the reference page for ZooKeys 1232 opened, its included-taxa page was refused (PROVENANCE_REQUIRED, not retried); Chilobase not opened. No synonymy found for any of the five species in the searches run. 10 WebSearches.

Main checks: no species or DOI of lines 1-8 occurs anywhere in docs/ outside the unit's own two files (the "spinosissima" hits are Nymphopsis duodorsospinosa and Diplolepis spinosissimae; "hualongensis" occurs only in desk-d288.md as a retrieval note). Class: every page's taxon classification block lists Animalia, order and family only (795 preview shows no block), so blank class is right on all eight. Eye absence: main files it as eyes_count 0 with eye "eyes absent" (Leptonetela arvanitidisi, d283); line 1 follows that. Quote word counts (check.py split): 9, 8, 30, 32, 14, 14, 14, 20.

Trait key for eye diameters: docs/views/research/SENSORY-ANATOMY.md says "Use `sensory_anatomy` when no existing anatomical trait fits." Main already holds spider eye-diameter lines of exactly this form under `eye_diameter_mm` (desk-d292, Typhlonesticus angelicus "Eye diameter: AME 0.03, ALE 0.05; PME 0.05; PLE 0.05.", units from the Methods "All measurements are given in mm."), and the key is used by oa-1, oa-2, d280, d291, d306, d309, d319, d320. Lines 5-7 print "diameters" in the heading, so eye_diameter_mm fits and sensory_anatomy is the wrong key: a reader of eye_diameter_mm misses them. Line 8's "Eye sizes" is undefined (not stated as diameter), so eye_diameter_mm does not fit it and sensory_anatomy/anatomical_measurement stands there.

## Per line

| Line | Record | Verdict | Fault |
|---|---|---|---|
| 1 | Australobius tracheoperspicuus, eyes_count 0 | OK | none |
| 2 | Scolopendra spinosissima, eyes_count 4 | OK | none |
| 3 | Lithobius hualongensis, 1 + 3, 3, 1 | OK | optional: subgenus |
| 4 | Lithobius sui, 1 + 4, 4, 1 | ERROR (fixable) | conditions/note: omitted Variations ocelli formulas |
| 5 | Pholcus chaoyang AME 0.09 | ERROR (fixable) | trait key: eye_diameter_mm |
| 6 | Pholcus chaoyang PME 0.14 | ERROR (fixable) | trait key: eye_diameter_mm |
| 7 | Pholcus chaoyang PME 0.12 (female) | ERROR (fixable) | trait key: eye_diameter_mm |
| 8 | Jingneta qishan PME 0.04 | OK | none |

Errors: 4 of 8 (50%), all fixable, 0 unfixable.

### Line 1, Australobius tracheoperspicuus
Page (article_preview 28036): title "Australobius tracheoperspicuus sp. n., the first subterranean species of centipede from southern China (Lithobiomorpha, Lithobiidae)"; authors Qing Li, Su-jian Pei, Xuan Guo, Hui-qin Ma, Hui-ming Chen; ZooKeys 795: 83-91, 2018; DOI 10.3897/zookeys.795.28036; licence "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)". Crossref same authors in order, 83-91, issued 2018-11-08, CC BY 4.0 vor. Description: "No ocelli on each side of the cephalic plate." **Quote MATCH**. Diagnosis "Antennae with 26 articles, no ocelli, ..."; Key "No ocelli on each side of cephalic plate"; Discussion "absence of ocellus on each side of the cephalic plate vs. 8–9 ocelli in A. magnus". Description has no Male/Female headings; it is continuous prose with inline "Female S XV" and "Male S XV" and "Body length 17.43 –19.24 mm", so the species-level scope in conditions is right. No taxon classification block on the preview; class blank is right. Initials right.

### Line 2, Scolopendra spinosissima
XML 129410: Lectotype "1 unsexed adult; Luzon Island, Manila; 1902" (ZMH-A0000633); paralectotypes "1 ♂, 1 ♀, 1 unsexed; ... Dolores"; heading "Lectotype redescription". "Cephalic plate with four ocelli in each side." **Quote MATCH**; sentence before is the antennae (19 articles, 17-20 in paralectotypes), after is puncta, as the note says. Classification block Animalia, Scolopendromorpha, Scolopendridae (no class). Crossref: Carles Doménech sole author, title, ZooKeys 1215: 311-334, issued 2024-10-17, CC BY 4.0 vor. Remarks and key were not in the tool text, so the note's "no ocelli counts for ... other Scolopendra in the text read" is unchecked, not contradicted.

### Line 3, Lithobius hualongensis
XML 39033: title, authors Penghai Qiao, Wen Qin, Huiqin Ma, Gonghua Lin, Tongzuo Zhang; ZooKeys 892: 77-92, 2019; CC BY 4.0 sentence. Classification block Animalia, Lithobiomorpha, Lithobiidae. Description "Male (Fig. 1A)": "On each side of head, 1 + 3, 3, 1 oval to rounded ocelli arranged in three irregular rows;" + "posterior ocellus large; ocelli adjacent to the Tömösváry organ slightly smaller." **Quote MATCH** (no figure reference in this sentence). Diagnosis "8–11 ocelli on each side, arranged in 3 irregular rows, ..."; Variations "Body length 12.31–16.15 mm; ocelli 1 + 3, 3, 1 or 1 + 4, 3, 3;", both in conditions/note. Holotype ♂ HL9. Optional: main files this genus with the subgenus in the taxon ("Lithobius (Ezembius) varioporus", "Lithobius (Ezembius) tetraspinus", d283 and others); the unit drops it. Not counted.

### Line 4, Lithobius sui
Description "Female (Fig. 2A)": "On each side of head, 1 + 4, 4, 1 oval to rounded ocelli (Fig. 2B), arranged in three irregular rows;" + "posterior ocellus large; ocelli adjacent to the Tömösváry organ slightly small." **Quote MATCH**, "(Fig. 2B)," sits after "ocelli" exactly as quoted. Holotype "♀ (MHA8), Minhe County, Qinghai Province, ... 2280 m, a.s.l., 24 October 2010"; paratypes "1 ♂ (MHA6), 2♀♀ (MHA1, MHA5)". Diagnosis "9–10 ocelli on each side, arranged in 3 irregular rows, ...". **Fault:** the article_preview prints a Variations paragraph for L. sui: "Body length 12.15–18.85 mm; ocelli 1 + 4, 4, 1, 1 + 4, 3, 2 or 1 + 4, 3, 1;". The conditions say "no Variations section on ocelli was found in the text read" and the note says the female holotype is the only sex whose ocelli are described; the paper has no separate male description (its male paragraph covers the posterior segment only, no ocelli). Omitted variation, one error, fixable. Same Crossref failure as line 3; licence from the XML sentence.

### Lines 5-7, Pholcus chaoyang
XML 145622: authors Jinglin Li, Qiaoqiao He, Shuqiang Li, Zhiyuan Yao (Crossref same order); ZooKeys 1232: 285-310; Crossref issued 2025-03-19, CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Methods "All measurements are given in millimeters (mm)." and no eye-measuring method. Holotype ♂ SYNU-Ar00415, 486 m, 17 Jul. 2024; paratypes 1♂ SYNU-Ar00416, 2♀ SYNU-Ar00417–18; habitat "Underside of overhang on rocky cliffs in mountainous area." Headings "Male (holotype)" and "Female (paratype, SYNU-Ar00417)". Male "Eye interdistances and diameters: PME–PME 0.21, PME 0.14, PME–ALE 0.04, AME–AME 0.04, AME 0.09." and female "Eye interdistances and diameters: PME–PME 0.23, PME 0.12, PME–ALE 0.05, AME–AME 0.04, AME 0.08." **Quotes MATCH**. Diagnosis has no eye statement. Values, scope and conditions are right. **Fault (each line):** filed as sensory_anatomy although main's existing key eye_diameter_mm fits a labelled diameter (see trait-key paragraph above). Fixable by changing the key; the replacement drops evidence_kind/structure/measurement (required only for sensory_anatomy) and adds the "new trait" note check.py needs for eye_diameter_mm, as d292 did. Replacement checked: the patched file passes check.py with 0 problems.

### Line 8, Jingneta qishan
XML 136555: authors Shuhui Li, Qiang Chen, Yanfeng Tong (Crossref same); ZooKeys 1218: 99-119; Crossref issued 2024-11-18, CC BY 4.0 vor. Printed name "Jingneta qishan sp. nov."; classification Animalia, Araneae, Leptonetidae. Holotype male SYNU-1168, Qishan Scenic Area, Guichi District, Chizhou, 70 m, 12 January 2022; paratype female SYNU-1169; Methods "Specimens used in this study were collected by sifting forest leaf litter." and "All measurements were taken using an Olympus BX51 compound microscope and are in millimeters." Male "Eye sizes and interdistances: ALE 0.05, PLE 0.05, PME 0.04; ALE–PME 0.06, PLE–PLE 0.02, PLE–PME 0.03; AER 0.08, PER 0.10." **Quote MATCH**; female line also PME 0.04. Diagnosis has no eye statement; Introduction gives the family-level "typically have six eyes" only. "Eye sizes" is not defined, and the record says so and calls it size, not diameter, under sensory_anatomy/anatomical_measurement: consistent with SENSORY-ANATOMY.md, since no existing key fits an undefined size. A novataxa post (Oct 2025) reports the name as described in this paper with no transfer. OK.

## Replacement

Line 4 (conditions; note):
- `no Variations section on ocelli was found in the text read"` -> `the Variations paragraph gives 'ocelli 1 + 4, 4, 1, 1 + 4, 3, 2 or 1 + 4, 3, 1' without assigning counts to specimens or sexes"`
- `so the Description formula sits at the top of the Diagnosis range; the female holotype is the only sex whose ocelli are described in the text read.` -> `so the Description formula sits at the top of the Diagnosis range; the Variations formulas sum to 10, 10 and 9 (my additions). The paper has no separate male description; its male paragraph (posterior segment) does not mention ocelli.`

Line 5 (trait and sensory_anatomy fields; note):
- `"trait": "sensory_anatomy", "evidence_kind": "anatomical_measurement", "structure": "anterior median eye (AME) diameter", "measurement": "AME 0.09 (eye diameter, mm)", ` -> `"trait": "eye_diameter_mm", `
- `"note": "Anatomy only; no visual function is claimed. ` -> `"note": "New trait: eye_diameter_mm (key already in use on main, e.g. desk-d292 spider eye-diameter lines with units from the Methods). The heading names diameters; no visual function is claimed. `

Line 6:
- `"trait": "sensory_anatomy", "evidence_kind": "anatomical_measurement", "structure": "posterior median eye (PME) diameter", "measurement": "PME 0.14 (eye diameter, mm), male holotype", ` -> `"trait": "eye_diameter_mm", `
- `"note": "Anatomy only; no visual function is claimed. ` -> `"note": "New trait: eye_diameter_mm (key already in use on main, e.g. desk-d292 spider eye-diameter lines with units from the Methods). The heading names diameters; no visual function is claimed. `

Line 7:
- `"trait": "sensory_anatomy", "evidence_kind": "anatomical_measurement", "structure": "posterior median eye (PME) diameter", "measurement": "PME 0.12 (eye diameter, mm), female paratype", ` -> `"trait": "eye_diameter_mm", `
- `"note": "Anatomy only; no visual function is claimed. ` -> `"note": "New trait: eye_diameter_mm (key already in use on main, e.g. desk-d292 spider eye-diameter lines with units from the Methods). The heading names diameters; no visual function is claimed. `

Each old string occurs exactly once in its line (checked by script); the patched file gives "10 records, 0 problems" under tools/senses/check.py. If the merge step prefers not to apply the line 5-7 key change, drop those three lines rather than file them under sensory_anatomy.

## Optional fixes (not counted)

- Lines 3 and 4 taxon: `"taxon": "Lithobius hualongensis"` -> `"taxon": "Lithobius (Ezembius) hualongensis"` and `"taxon": "Lithobius sui"` -> `"taxon": "Lithobius (Ezembius) sui"`, matching main's Lithobius records and the printed name; the note sentence about filing without the subgenus would then be dropped.
- Licence notes, lines 1, 2, 5, 6, 7, 8: `Crossref was not consulted for this DOI.` -> `Crossref CC BY 4.0 (vor) on this DOI (audit 433).` Lines 3 and 4 keep the XML-sentence basis (Crossref lookup failed).

## Not checked

World Spider Catalog included-taxa list for ZooKeys 1232 (PROVENANCE_REQUIRED); Chilobase status for the three centipedes; Scolopendra spinosissima Remarks/key text (not in the tool output).
