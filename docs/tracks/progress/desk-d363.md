# desk-d363 progress

Angle: multi-species spider papers in unmined families. 16 records filed from one Linyphiidae paper, about 16 WebSearch/WebFetch calls. check.py run on all evidence files: no problems reported for desk-d363.

## Filed (docs/views/evidence/desk-d363.jsonl), eye_diameter_mm, one record per labelled eye (AME, ALE, PME, PLE) of the male holotype
- ZooKeys 1219: 195-214 (10.3897/zookeys.1219.133899, page-printed CC BY 4.0, Crossref CC BY 4.0 vor): Tapinocyba centralis, T. denticulata, T. triangularis, T. virga (Linyphiidae). Methods: "Eye sizes were measured at the maximum dorsal diameter." Quotes are cut after PLE and marked [...].

## Weak spots
- All text came through the fetch tool in pieces of about 125 characters; the male sentences were read to the end of PME-PME, the centralis one to its full stop (it prints a stray comma in "AME-ALE, 0.02", outside the quote).
- Licence read in three pieces on the preview page. Authors: printed byline converted to Surname Initials; the page's own citation line reverses given and family names.
- Female values (denticulata, triangularis, virga) are in conditions; centralis female unknown. Female paratype codes for triangularis and virga are not itemised in the paper.
- "No other eye-number sentence" rests on the fetch tool's reading of each treatment, not on a text search.
- WSC spec-data pages 70818, 70819, 70820, 70821 opened (70819/70820 after a first blocked attempt, then surfaced by search).

## Not filed
- ZooKeys 1232: 343-355 (146855): three Spartaeini species in three genera, Salticidae; not one genus; male eye values printed (e.g. Calxattus dengba AME 0.63, ALE 0.26, PME 0.43, PLE 0.37) but not read in full.
- ZooKeys 1253 (165585) Linyphiidae of Hunan: only Gongylidioides heimifengensis has a male holotype; eye sizes undefined; not opened.
- Oedothorax simianensis (Irfan et al. 2025, Plazi hit): not opened.

## Desk disposition after audits 481 and 482 (2 November 2026)

Audits 481 (lines 1-8, Tapinocyba centralis and denticulata) and 482 (lines 9-16, T. triangularis and virga) found 16 of 16 in error, all in note text. The notes' claim that no other sentence gives eye information was false: they omitted the male-only "PMEs present on cephalic lobe" and cephalic pits (centralis, triangularis), the modified ocular region (virga), the denticulata female eye sentence, and misstated the female comparison (triangularis omits ALE; virga's PME is equal). Quotes, values, eye labels, eye_diameter_mm key (Methods define eye size as maximum dorsal diameter), WSC names, licence, authors and bibliography held; no duplicates. Replacement lines merged; check.py 0 problems.
