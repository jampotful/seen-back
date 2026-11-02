# desk-d360 progress

Angle: multi-species spider papers. 16 records filed from one paper, about 22 WebSearch/WebFetch calls. check.py: 0 problems.

## Filed (docs/views/evidence/desk-d360.jsonl), sensory_anatomy, one record per labelled eye (AME, ALE, PME, PLE) of the male holotype
- ZooKeys 1245: 243-267 (10.3897/zookeys.1245.154908, page-printed CC BY 4.0, Crossref CC BY 4.0 vor): Synagelides dajueshan, S. guangfeng, S. kangding, S. wuyuan (Salticidae).

## Weak spots
- "Eye sizes" is undefined in the Methods, so sensory_anatomy rather than eye_diameter_mm (precedent audits 433, 471).
- WSC page for Synagelides wuyuan not opened (id not in a search result; fetch blocked); name checked only on the Jumping Spiders Catalog, which prints no family. WSC accepted for the other three.
- The eye sentences came back in two pieces and were joined at the comma after AME-ALE.
- Licence sentence read in pieces.

## Not filed
- ZooKeys 1253: 243-254 (10.3897/zookeys.1253.165585, Linyphiidae of Hunan, CC BY 4.0): eye sizes undefined; male holotype only for Gongylidioides heimifengensis (AME 0.04, ALE 0.07, PME 0.07, PLE 0.07); other three species have female holotypes; full sentences not retrieved.
- Synagelides female paratypes (all four species): not filed.
- Crossref list queries rate-limited twice; two Pensoft candidates (ZooKeys 1232 146855, 175373) surfaced in search, not opened.

## Desk disposition after audits 476 and 477 (2 November 2026)

Audit 476 (lines 1-8, Synagelides dajueshan and S. guangfeng) found 8 of 8 in error, one fixable note fault each: the note said no other eye sentences exist although an MOA sentence is printed, and said "year only" for dates the page prints in full. Audit 477 (lines 9-16) confirmed S. kangding (lines 9-12) and found the four S. wuyuan lines in error (4 of 8, 50%): each note cited WSC spec-data/72192, which is the S. dajueshan species page, as a genus page. Overall 12 of 16 in error, all note or condition text. Quotes, values, eye labels, the sensory_anatomy key (the Methods never define eye size), female values, bibliography and licence held. Crossref was unreachable for the auditors; S. wuyuan's World Spider Catalog status is still unchecked. Replacement lines merged; check.py 0 problems.
