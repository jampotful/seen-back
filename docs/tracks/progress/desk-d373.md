# desk-d373 progress

Angle: multi-species spider papers in new genera and venues. 56 records from two papers, about 28 search/fetch calls. check.py run on the log (0 problems).

## Filed (docs/views/evidence/desk-d373.jsonl)
- ZooKeys 1232: 343-355 (10.3897/zookeys.1232.146855; CC BY 4.0 on page, Crossref vor): Spartaeini, Salticidae. Calxattus dengba (male holotype), Spartaeus siloi (male holotype, female paratype), Taraxella chrisfehni (male holotype, female paratype), AME/ALE/PME/PLE each, sensory_anatomy because Methods define no eye measure (20 records). WSC pages 71495, 71496, 71497 opened.
- European Journal of Taxonomy 997: 51-76 (10.5852/ejt.2025.997.2921; page prints CC BY 4.0, Crossref licence content-version unspecified): Paratropis (Paratropididae) amfe, aurelianoi, calarca, chami, macca (male holotype and female paratype), salsa, urku (male holotype and female paratype), 'Ocular sizes and interdistances' sentences, sensory_anatomy (36 records). WSC pages 71950-71956 opened.

## Weak spots
- All text came through the fetch tool's summaries; long sentences were returned in consecutive pieces and rejoined.
- Paratropis: the order of the 'Eyes and ocular tubercle' and 'Anterior eye row' sentences was read directly only for four species; stated in conditions.
- Printed oddities recorded as printed: Taraxella female ALE 0.06; Paratropis urku female PME-PLE 0.6; urku paratype line says same data as holotype but gives other coordinates and date.
- ZooKeys 1232 Diagnosis eye wording: the tool reported none; Description colour sentences mention eye surroundings and are cut in the tool output.

## Not filed
- Paratropis lluspiosa (no eye sizes, refers to Perafan et al. 2019). Paratropis amfe, aurelianoi, calarca paratypes have no eye sentence read.
- Latouchia, Hunan Linyphiidae (1253), Oedothorax simianensis, Sinartoria: not opened this unit.

## Desk disposition after audits 501-507 (2 November 2026)
All 56 records merged with the auditors' replacement lines (55 of 56 had a fault). Two fault families:
- Value errors in all 36 Paratropis lines except line 56 (audits 503-507): the desk filed interdistances (AME-AME, ALE-ALE, AME-PME, ALE-PLE) from the same eye sentence instead of the eye sizes, for example macca AME 0.18 filed where AME is printed 0.19, chami AME 0.1 where 0.28 is printed, amfe AME 0.31 / ALE 0.29 / PME 0.17 / PLE 0.23 as the true sizes. Line 56 was right only because both numbers are 0.15. The auditors replaced every value with the printed eye size.
- Note and conditions faults in the Salticidae lines (audits 501-503): the notes said the Methods have nine sentences (the page has eleven), and the conditions omitted the other sex's eye sentence, "Clypeus absent." in the sentence order, and a false grep claim.
Quotes, labels, trait key (sensory_anatomy, because the Methods of neither paper define a diameter), licence, bibliography and names were correct throughout. Lesson for later units: in a sentence such as "Eye sizes and interdistances" read the label before each number and file only the eye-size values.
