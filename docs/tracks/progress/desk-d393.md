# desk-d393 progress

Angle: open-access Pholcidae (Belisana) papers printing per-sex eye sentences. 33 records from two open Pensoft papers (log docs/views/evidence/desk-d393.jsonl). check.py and check.py --require-evidence-kind: 0 problems. Every value was compared by script with the PME figure printed in its quote (all 33 match, none zero).

## Filed
- ZooKeys 1216: 265-302 (10.3897/zookeys.1216.132561; Wang B, Li J, Li S, Yao Z, 2024): nine new Belisana from Guizhou caves (bijie, liupanshui, majiang, nayong, qixingguan, xiuwen, yongcong, zhouxi, zunyi), male and female each, 18 records.
- ZooKeys 1202: 255-286 (10.3897/zookeys.1202.121633; Zhang L, Wu Z, Li S, Yao Z, 2024): eight new Belisana from Yunnan (honghe, jiuxiang, lincang, luxi, tengchong, tongi, yongsheng male only, yunnan), 15 records.
- Trait eye_diameter_mm, eye PME only: the sentence 'Eye interdistances and diameters: PME-PME x, PME y, PME-ALE z' prints one diameter (PME) and two interdistances. Belisana has no AME ('AME absent' printed in ZooKeys 1202, not a measurement, not filed) and the sentence prints no ALE or PLE diameter. Methods give 'All measurements are given in millimeters (mm).' and no eye definition; the label prints 'diameters' but not the bare 'Eye diameter(s)', flagged in each note for the auditor.

## Weak spots
- Text came as fetch-tool excerpts (pieces under 125 characters, some summarised); neighbouring sentences, type lines and opening words are tool-returned and abridged where marked. Several species' male/female openings came without the 'Male (holotype):' or 'Female (paratype, code):' prefix (xiuwen, zhouxi, zunyi female, majiang unchecked for some); where not returned, conditions say so.
- Licence sentence for ZooKeys 1216 returned as a paraphrase (CC BY 4.0); ZooKeys 1202 sentence returned in quotation marks. Crossref version of record not reached (rate-limited and client_error): UNCHECKED. DOIs are those printed on the publisher pages.
- WSC opened: B. bijie (64096), B. honghe (63198), B. tengchong (63202), all accepted. Other 14 species UNCHECKED (yunnan page 69678 seen in results, not opened).
- Grep of docs/ for each species name and both DOIs found nothing on main.

## Not filed and why
- Search results for Salticidae, Theridiidae, Gnaphosidae, Philodromidae, Oxyopidae, Corinnidae, Tetragnathidae and Araneidae gave only Plazi, Zenodo, aggregator, old (2013) or pre-2022 copies; no publisher page reached. Leads: Icius entebbensis (Wisniewski and Wesolowska 2024, Plazi only); Theridiidae by Lin and Li 2024 (Plazi only); BDJ 129438 (figure pages only).

## Desk disposition after audits 613-617 (2 November 2026)
All 33 lines (Belisana PME diameters: ZooKeys 1216: 265-302 bijie, liupanshui, majiang, nayong, qixingguan, xiuwen, yongcong, zhouxi, zunyi; ZooKeys 1202: 255-286 honghe, jiuxiang, lincang, luxi, tengchong, tongi, yongsheng, yunnan) were audited by fresh Opus agents (audits 613 to 617). 0 counted errors: every quote, PME value, DOI, author list and CC BY 4.0 licence was confirmed on the publisher pages and all species are accepted at WSC; none repeats main. Faults corrected in notes: paraphrased licence, abridged type lines, missing female labels and paratype codes, an invented Variation section (bijie), unchecked WSC notes. All five auditors kept eye_diameter_mm for the label "Eye inter-distances and diameters", noting main files this label the same way (audit 433). Every line replaced with the auditor's text and merged; none dropped. OWNER QUESTION (same as desk-d390 Micropholcus, bare "diameter PME/AME" kept as sensory_anatomy): confirm whether a printed "Eye inter-distances and diameters" label counts as the 'Eye diameter(s)' label for eye_diameter_mm, and align the two. Crossref vor unchecked.
