# desk-d376 progress

Angle: multi-species spider papers with per-species eye sentences. 44 records from two papers, about 38 search/fetch calls. check.py run on the log (0 problems). Every value was re-read against its quote label by label (sizes only; interdistances and clypeus heights not filed).

## Filed (docs/views/evidence/desk-d376.jsonl)
- ZooKeys 1085: 69–99 (10.3897/zookeys.1085.77966; XML prints CC BY 4.0): Phrynarachne (Thomisidae) brevis (female), dreepy (male holotype, female paratype), huangshanensis (male), lancea (female), AME/ALE/PME/PLE each, eye_diameter_mm because Methods say eye sizes are the maximum diameter (20). WSC: spec-data/66347 (dreepy) opened; genus page /genus/3692/Phrynarachne opened and lists the other three; their own species pages were blocked by a permission timeout.
- Zoosystematics and Evolution 101(1): 141-171 (10.3897/zse.101.136177; preview page prints CC BY 4.0): Pseudopoda (Sparassidae) huanglianensis, mamillaris, oliviformis, male and female of new material each (YNZY013/025, 009/010, 011/012), eye_diameter_mm because Methods say eye diameters were measured at the widest part (24). WSC spec-data 67711, 67726, 67737 opened.

## Weak spots
- All text came through fetch-tool summaries; long sentences arrived in two pieces and were rejoined at the semicolon/comma where the piece ended (not at a full stop). Licence sentence read in segments.
- Phrynarachne huangshanensis male and lancea female: no specimen number printed with the description; brevis female is the single Other-material female. Dreepy female is "one paratype" of two listed.
- Phrynarachne received/accepted dates were read (13 Nov 2021, 19 Jan 2022); Pseudopoda dates not returned.
- Pseudopoda: female/other colour sentences were not asked for beyond the male ones listed; Diagnosis eye sentences reported absent by the tool.
- New trait key eye_diameter_mm used as on main (check.py needs "new trait" in the note, included).

## Not filed
- Phrynarachne xuxiake, yunhui, zhengzhongi (new species, same paper): the XML text returned ended inside P. mammillata; their treatments were not reachable.
- Pseudopoda xiaozhua, yangae, ying (new, same paper): preview page returned only xiaozhua's type lines; no descriptions.
- Not opened: Ischnothyreus, Trilacuna, Gamasomorpha, Zora, Wangaraneus, Shaanxinus, Poeciloneta, Parazygiella, EJT 1007, Oedothorax simianensis.

## Desk disposition after audits 517-522 (2 November 2026)
All 44 records merged with the auditors' replacement lines. 36 of 44 in error (82%), all in conditions or note text; no value, quote or trait key was wrong. eye_diameter_mm was confirmed (Methods: "maximum diameter"), and no interdistances were filed. Audit 517 (Phrynarachne brevis, dreepy male): 0 of 8. Audit 518 (P. dreepy female, P. huangshanensis): 8 of 8 (specimens named in the material headings left out: dreepy's three male paratypes, huangshanensis's lot of five females). Audit 519 (P. lancea): 8 of 8 (male paratype IZCAS-Ar18537 and three other-material males left out, "Opisthosoma" sentence skipped, a colour sentence cut without a mark). Audit 520 (Pseudopoda huanglianensis, mamillaris): 8 of 8 (conditions named male YNZY013 instead of female YNZY025, the female "as in males" sentence omitted, a colouration sentence misquoted). Audit 521 (P. mamillaris, oliviformis): 8 of 8 (conditions said the male YNZY009 was measured, but it was the female YNZY010; the male Description sentence was misquoted or cut unmarked; the female colouration sentence omitted). Audit 522 (P. oliviformis): 4 of 4 (male YNZY011 named as the measured specimen, female colour sentence omitted). Lesson: when a record's sex is female, name the female specimen and quote the female sentence; never copy conditions from the male record. The "new trait" note was reworded by the auditors. Owner question: add eye_diameter_mm to the TRAITS list in tools/senses/check.py (not editable by the desk). Unchecked names: the World Spider Catalog pages for Phrynarachne lancea and the three Pseudopoda species depend on what each audit opened; see the audit reports.
