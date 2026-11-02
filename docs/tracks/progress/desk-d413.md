# desk-d413 progress

Angle: eye-size records, wider net, eighth round. 36 records from four open papers (log docs/views/evidence/desk-d413.jsonl). check.py and check.py --require-evidence-kind: 0 problems for desk-d413.jsonl (other files in the tree carry older problems, not touched).

## Filed
- Zoosystematics and Evolution 100(2): 705-720 (10.3897/zse.100.124160; Yang L, Li S, Yao Z, 2024; Linyphiidae): Bifurcia labahe male holotype; B. shuangqiao male holotype and female paratype. 12 records, sensory_anatomy (label 'Eye inter-distances and diameters'; Methods define no eye dimension). WSC pages for both species opened (accepted).
- ZooKeys 1285: 125-145 (10.3897/zookeys.1285.202554; Nagai T, Ballarin F, Eguchi K, 2026; Nesticidae): Nesticus yamabushi male holotype NSMT-Ar 27107 and a female paratype (code not stated). 8 records, eye_diameter_mm (sentence prints 'Eye diameter:'). WSC spec-data 73951 opened.
- Arthropod Systematics & Phylogeny 84: 371-392 (10.3897/asp.84.e181294; Quispe-Colca et al., 2026; Theraphosidae): Kiskalla ignacioi male holotype MUSA-AR 317 and a female paratype (code not stated). 8 records, sensory_anatomy (Methods: eye measurements 'at the widest spans of each lens', no word diameter). WSC spec-data 73860 opened.
- Biodiversity Data Journal 13: e142264 (10.3897/BDJ.13.e142264; Zhou G et al., 2025; Nemesiidae): Raveniola fuzhouensis male holotype FJFZ-24-19-03 and female paratype FJFZ-24-19-04. 8 records, sensory_anatomy. WSC species/64569 opened.

## Weak spots
- The fetch tool paraphrases and cuts long sentences; eye sentences were returned in short pieces and joined. Licence sentences came partly as fragments or summaries. Crossref licence not read for any paper (UNCHECKED); volume and pages for ZooKeys 1285 and ASP 84 were confirmed only through a Crossref list query for prefix 10.3897.
- Nesticus yamabushi: XML and preview gave the eye sentence in two forms (bare abbreviations vs expanded in brackets); the bare form is quoted. Female paratype not identified by code.
- Kiskalla ignacioi: widest-span wording left as sensory_anatomy; owner question whether 'widest spans of each lens' counts as a diameter definition.
- Raveniola fuzhouensis female prints PME-PLE 0.29 (not filed; interdistance).

## Not filed and why (leads)
- Kiskalla yeisoni and K. zukuapasanka (same ASP paper): eye values read (yeisoni female holotype MUSA-AR 319; zukuapasanka female holotype MUBI 226, sentence tail garbled with AME-PME 0.95) but no WSC species page reached from search; WSC genus page counts 3 accepted species.
- Bifurcia xiaojin (ZSE 100(2)): Description not returned by the fetch tool.
- ZooKeys 1287 Damarchus (Bemmeridae): sizes printed as means with plus-minus, pooled across specimens; skipped. ZooKeys 1281 Latrodectus lucacha: no eye sentence. ZooKeys 1255 Qianlingula, ZooKeys 1200 Cheiracanthium, ZooKeys 1229 Atypus, BDJ 14 e199306 Zangaraneus, Zootaxa 5652 Plexippoides: already filed or on the avoid list.
- Not reached to a publisher page: ZSE 102 Songthela (12 species), ASP 84 Kwonkan (page ends before the new species), BDJ 14 e214835 Troglocoelotes doul male, ZooKeys 1293 Batanta Salticidae, ZSE 102 Ovia, BDJ 14 e211761 Raveniola (Jiangxi). Orphnaecus and Eresus/Sinopoda/Shuqiangius siblings not reached.

## Desk disposition after audits 729-733 (2 November 2026)
28 of 36 lines merged with the auditors' replacement text; 8 dropped. Dropped: lines 13-20 (ZooKeys 1285 Nesticus yamabushi, male holotype NSMT-Ar 27107 and female paratype). Audits 730 and 731 found that the paper's text prints no measurement unit for the eye values (mm appears only in figure scale bars) and that the Methods define no eye diameter, so the lines would also have moved to sensory_anatomy; a value without a printed unit says more than its quote, so the desk dropped them. Counted errors 8 (the dropped lines). Owner question: does a unit read only from figure scale bars suffice? If yes, the corrected lines are in audit-730.md (13-16) and audit-731.md (17-20).
Kept lines: Bifurcia labahe and B. shuangqiao (ZSE 100(2)) sensory_anatomy; Kiskalla ignacioi (ASP 84) sensory_anatomy (Methods "widest spans of each lens", no word diameter; owner question); the Kiskalla female paratype is MUSA-AR 318, as printed; Raveniola fuzhouensis (BDJ 13 e142264) sensory_anatomy, where path corrected to the headings the page prints. Crossref remarks removed throughout; WSC checked, all accepted, no transfers.
