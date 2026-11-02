# desk-d362 progress

Angle: multi-species spider papers, new journals/families. 16 records filed from two Pholcus papers, about 27 WebSearch/WebFetch calls. check.py: 0 problems.

## Filed (docs/views/evidence/desk-d362.jsonl), eye_diameter_mm, one record per labelled eye (PME, AME) of the male holotype
- ZooKeys 1240: 39-64 (10.3897/zookeys.1240.147905, XML copy prints CC BY 4.0 sentence, Crossref CC BY 4.0 vor): Pholcus qiaojia, P. aba, P. wenchuan, P. mengding, P. miyi, P. yaan (Pholcidae). 12 records.
- ZooKeys 1264: 37-50 (10.3897/zookeys.1264.175373, page-printed CC BY 4.0, Crossref CC BY 4.0 vor): Pholcus jiuzhai, P. pingwu. 4 records.

## Weak spots
- Only PME and AME diameters are printed ("Eye interdistances and diameters"); no ALE or PLE values. Methods define no eye-measuring procedure; key eye_diameter_mm chosen because the sentence itself says "diameters" (as Pholcus chaoyang, audit 433). An auditor may prefer sensory_anatomy.
- Licence for 1240 was read on the publisher XML download copy in three pieces; the preview page url in source.url returned only a CC BY 4.0 summary. Titles were returned in halves and joined.
- Female paratype of P. qiaojia: voucher not retrieved. Female values are in each record's conditions.
- WebFetch pages for 1240 are truncated in the XML copy after P. aba; the preview page returned all six species.
- Crossref list queries rate-limited twice; retried singly.

## Not filed
- Other leads from search results not opened: ZooKeys 1232 (146855), ZooKeys 147905-related Pholcus qin (WSC 71516). No other families reached.

## Desk disposition after audits 479 and 480 (2 November 2026)

Audit 479 (lines 1-8, Pholcus qiaojia, aba, wenchuan, mengding) found 8 of 8 in error, one note fault each: the note said no other sentence gives eye numbers, but the female sentence does; the female voucher (SYNU-Ar00473) is now added. Audit 480 (lines 9-16) found 2 of 8 in error (25%): the P. yaan notes left out the female paratype's "Ocular area without eye-stalks." Six lines (miyi, jiuzhai, pingwu) confirmed. Overall 10 of 16 in error, all note or condition text. The eye_diameter_mm key stands (audit 433 ruling; the paper prints the numbers under "Eye interdistances and diameters"). Quotes, values, names, licence and bibliography held. Replacement lines merged; check.py 0 problems.
