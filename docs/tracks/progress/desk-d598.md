# desk-d598 progress

Angle: taxa and journals not yet worked (salamanders, caecilians, lizard ear opening, bat tragus, shrew or rodent ear length, reptile tympanum/eye rows) in open-licence journals. The OLD-ANGLE paragraph was ignored. Records go to docs/views/evidence/desk-d598.jsonl (unit desk-d598).

## Batch 1 (3 records)
- Tylototriton gaowangjienensis (Herpetozoa 37: 327-338, 10.3897/herpetozoa.37.e135222): holotype ED 3.80 and allotype ED 4.05 from the whole Table 2 ED row (publisher preview page). Pooled columns not filed (no n printed). Paper date conflict (2023 vs 2021) and ASW holotype-number mismatch noted in each record.
- Ichthyophis benjii (Amphibian & Reptile Conservation 15(2): 198-209, e288, no DOI printed): holotype eye E 0.4 mm as sensory_anatomy (Methods print only 'E, eye').

## Checked and dropped
- Scincella qianica (ZSE 101(4) 157713), Pristimantis milpe, Xenophrys (ZSE 158027): already on main.
- Cyrtodactylus arunachalensis (Evol Syst 5(1)): held out earlier (OD label, sex conflict).
- Trimeresurus ciliaris (VZ 109854): on main (d490).
- Nyctophilus holtorum (Rec Aust Mus): only Plazi redirect pages reached, no publisher text. Chalinolobus orarius is Zootaxa (dead).
- Lepidophyma jasonjonesi (Herpetozoa 36): ED label vs 'orbit diameter' definition, held out earlier (d585).
- Hypselotriton oolong / Hakkatriton orphicus (ZSE 100: 127268): on main (d500). Tylototriton vietnamirabilis (ZooKeys 1276): eye length only.
- Palawanosorex ater (ZooKeys 1137): no ear length printed, no measurement table.
- CSV hits that returned only abbreviation tables (ZSE 189932, ZooKeys 73659 and 97624, Herpetozoa 86751): papers not identified or no ED/EL data rows; not pursued.

## Totals
3 records (2 Tylototriton gaowangjienensis, 1 Ichthyophis benjii). About 41 WebSearches. check.py: 0 problems with and without --require-evidence-kind. Pool of Pensoft salamander, lizard and mammal ear/eye rows is nearly exhausted; no open-licence bat tragus, shrew or rodent ear paper was reachable as publisher text this unit (Nyctophilus holtorum reached only Plazi redirect pages; Chalinolobus orarius is Zootaxa).

## Desk disposition after audits 1196 and 1197 (4 November 2026)
3 records filed, 2 merged, 1 dropped. Counted errors: 1.
- Merged: Tylototriton gaowangjienensis ED x2 (holotype 2021051701 = 3.80 mm, allotype 2021051702 = 4.05 mm, Table 2). Audit 1196 found 0 record errors and 5 fixable wording faults (3.8 printed as 3.80; heading path, type list, the Table 1 ED definition and the ASW holotype line added to the notes). The ASW holotype number (2021051702) comes from a personal communication and contradicts the paper; the lines follow the paper and say so. The paper's collection date (17 May 2023) conflicts with the Sampling section (May 2021) and is disclosed.
- Dropped: Ichthyophis benjii E x1 (audit 1197). The paper prints only "E, eye" and never says which dimension E measures, so the undefined-dimension ruling applies and sensory_anatomy does not cure it. The auditor's corrected text (four paratypes, heading path, cut mark) is saved in audit-1197 if CC rules otherwise.
