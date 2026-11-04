# desk-d593 progress

Angle: per-specimen table rows (frogs, lizard ear opening, bat/rodent ear length) in open-licence journals, 2010-2021 papers preferred, plus the Natalus lanatus lead (ZSE 96(2): 411-429; MDD page and Table 3 column 'E' check). Method copied from d455 and d459 (trait eye_diameter_mm or sensory_anatomy, evidence_kind anatomical_measurement). Log: docs/views/evidence/desk-d593.jsonl (19 records so far).

## Status
- Started. Read rules.md, EVIDENCE-INTAKE, d455/d459 notes. Natalus and Blommersia nataliae checked on main: Natalus lanatus not on main under any trait; Blommersia nataliae is d592's (unmerged).

## Filed (batch 1)
- ZSE 96(2): 411-429 (10.3897/zse.96.51059; Turcios-Casco et al., 2020) Natalus mexicanus (MDD name; the paper says N. lanatus, which MDD lists as a synonym): Table 3 row E, two Honduran museum specimens TCWC 10992 (M, 15 mm) and TCWC 11008 (F, 14 mm), sensory_anatomy. Ear length has only the label 'ear length (E)' in the Methods (no procedure), disclosed.
- Herpetozoa 34: 131-140 (10.3897/herpetozoa.32.e69755; Liu et al., 2021) Micryletta hekouensis: Table 3 TMP and EL rows, holotype and paratype (4 records).

- ZSE 101(4): 2221-2242 (10.3897/zse.101.175246; Xu et al., 2025) Gekko tesselatus (Gekkonidae): Table 4 EL row (maximum ear opening diameter) for 13 paratypes, sensory_anatomy. ED already on main (d479). Holotype EL not filed: table 1.11 vs description 1.12 mm. Reptile Database page opened.

## Not filed
- Raorchestes (PeerJ 9 e10791): per-specimen data only in supplementary Table S2.
- Chiromyscus thomasi (ZooKeys 451): publisher XML has no tables; Methods do not define ear length.
- Tonatia bakeri/maresi holotype 'Length of ear from notch' (ZooKeys 915, CSV): values 14.00 and 30.00 look implausible together, species are synonym-level (Tonatia saurophila paper); not filed.
- Hyperolius ZooKeys 546 (tadpoles), Trinycteris ZooKeys 787 (no ear row), Artibeus and Mimon ZooKeys CSVs (series means), Raorchestes dulongensis (Zootaxa), ZooKeys 103713 Hemiphyllodactylus lungcuensis (ED on main d343/d500; ear only as ratios).
- Trimeresurus liqibini (ZSE 102(1) 303-314): still no Reptile Database page after one more search; table prints no ear.
- Cnemaspis adangrawi/tarutaoensis (ZooKeys 858, CC0): the XML page reader stops before the descriptions and measurement tables; ED and ear-opening definitions are in the Methods. Lead only.

## Status at end
19 records, check.py 0 problems for desk-d593 (plain and --require-evidence-kind). About 39 WebSearches. Crossref not used. Natalus taxon is a judgment call (MDD lists lanatus as a synonym of mexicanus; filed under the MDD name with the paper's name in the measurement). Scientific-preflight receipt not generated (prompt did not require it).

## Desk disposition after audits 1176, 1177, 1178 (4 November 2026)
All 19 records merged. Counted errors: 0. Wording faults only (heading paths missing Family, Genus and Subgenus lines, tooltip text, Methods wording, missing Methods sentence on paired measurements) and the auditors' replacement text was applied. Natalus is filed under Natalus mexicanus (MDD: "includes the recently described lanatus"; audit 1176 confirmed); the E column is labelled in the Methods. The Gekko tesselatus holotype EL was not filed (cell 1.11 versus description 1.12).
