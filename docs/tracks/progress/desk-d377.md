# desk-d377 progress

Angle: multi-species spider papers with per-species eye sentences. 52 records from three papers, about 50 search/fetch calls. check.py run on the log: 0 problems. Every value was re-read against its quote by script (regex on the eye's own label, interdistance labels excluded) and the quote word counts are all under 40.

## Filed (docs/views/evidence/desk-d377.jsonl)
- ZooKeys 1085: 69-99 (10.3897/zookeys.1085.77966; preview page prints CC BY 4.0, Crossref CC BY 4.0 vor): Phrynarachne (Thomisidae) xuxiake (holotype female), yunhui (single holotype female), zhengzhongi (female; holotype and paratype both female, sentence does not say which). AME/ALE/PME/PLE each, eye_diameter_mm (Methods: eye sizes are the maximum diameter). 12 records. WSC spec-data 66348, 66349, 66350 opened (all Thomisidae, accepted). Completes the paper with d376's four species.
- ZooKeys 1196: 1-14 (10.3897/zookeys.1196.119509; preview prints CC BY 4.0, Crossref CC BY 4.0 vor): four species printed as Anyphaena cibagou (male holotype, female paratype TRU-XZ-ANY-0002), linzhi (male holotype, female paratype TRU-XZ-ANY-0006), shufui (female holotype), yejiei (female). sensory_anatomy ('Eye sizes'; Methods read, no eye measure). 24 records. Filed under the WSC-current name Yinanyphaena (WSC spec-data 69460-69463 opened, transfer logged 2026-10-17); printed name is in each note.
- ZooKeys 1229: 201-212 (10.3897/zookeys.1229.143547; XML prints CC BY 4.0, Crossref CC BY 4.0 vor): Atypus (Atypidae) dawei and liui, male holotype and a named female each. sensory_anatomy (sentence labelled 'Eye diameter(s)' but no Methods definition). 16 records. WSC spec-data 71368, 71369 opened.

## Weak spots
- All text came through fetch-tool summaries, with sentences requested in pieces and rejoined; no full paragraph was read word for word, and notes say so rather than claiming no other eye sentence.
- Phrynarachne yunhui: the Description's first sentence is printed without 'holotype' (only one type exists). zhengzhongi: holotype or paratype not stated.
- Anyphaena/Yinanyphaena yejiei: WSC lists the holotype as male XZ-ANY-0016; the paper's type line (as returned) says female; paper followed, discrepancy in the note. Name choice (accepted Yinanyphaena vs printed Anyphaena) is a judgement for the owner.
- Atypus: eye_diameter_mm was not used because no Methods sentence defines the measure; Paratype lists are summarised, not copied whole; the dawei female specimen ATY-2023-212 is not traced to a locality line.
- Phrynarachne received/accepted dates and licence read on the preview page, not the XML.

## Not filed
- Pseudopoda xiaozhua, yangae, ying (ZSE 101(1), 10.3897/zse.101.136177): both the preview page and the XML stop before the Description sections (XML ends in Materials and methods at 82,517 characters; preview ends inside xiaozhua's Diagnosis). Not reachable.
- Platnickina submaculata and yoshidai (ZooKeys 1250.158643): eye diameters sit in one long semicolon-chained Male/Female sentence far over 40 words; not quotable.
- Latouchia 1265.175629 (same problem, noted by d374), Yinanyphaena 1294.203456 (not found by search), Ischnothyreus, Trilacuna, Gamasomorpha (BDJ e183760), Zora, Wangaraneus, Shaanxinus, Poeciloneta, Parazygiella, EJT 1007, Oedothorax simianensis: not opened.
