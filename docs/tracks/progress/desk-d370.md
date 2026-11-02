# desk-d370 progress

Angle: multi-species spider papers. 32 records from three ZooKeys papers, about 30 search/fetch calls. check.py run on the log.

## Filed (docs/views/evidence/desk-d370.jsonl)
- ZooKeys 1236: 185-196 (10.3897/zookeys.1236.146324; CC BY 4.0, Crossref vor): Weintrauboa (Linyphiidae) denticulata, shenwu, wanglangensis, AME/ALE/PME/PLE eye_diameter_mm for male holotypes (12). Methods: "Eye sizes were measured at the maximum dorsal diameter."
- ZooKeys 1226: 339-348 (10.3897/zookeys.1226.137240): Hippasosa (Lycosidae) thailandica, yunnanensis, male holotypes, eye_diameter_mm (8). Methods: "Eye sizes were measured as maximum dorsal diameter."
- ZooKeys 1226: 121-137 (10.3897/zookeys.1226.137752): Mutatus (Phrurolithidae) gelao, tujia, tianyan, male holotypes (12), filed as sensory_anatomy because no Methods sentence defines eye sizes as diameters.
- WSC species pages opened for all eight species (accepted; families as filed).

## Weak spots
- All text came through the fetch tool's summaries of the publisher XML, eye sentences read in two consecutive pieces and rejoined.
- Hippasosa: two reads gave the order of "Carapace yellowish brown." / "Eye region black." differently; stated in conditions.
- Weintrauboa female lines: the tool returned a full stop after the last interdistance before ALE-PLE; stated in conditions.
- Mutatus yintiaoling treatment never appeared in the fetch output; not filed.

## Not filed
- Sinartoria (ZooKeys 1244): only S. dui has a male; Methods define no eye measure; not filed.
- Latouchia, Hunan Linyphiidae (1253), ZooKeys 1232, Oedothorax simianensis: not opened.

## Desk disposition after audits 495-498 (2 November 2026)
All 32 records merged with the auditors' replacement lines. Every line carried a fixable fault in note or conditions text, none in quote, value, eye label or trait. Audit 495 (Weintrauboa denticulata, shenwu): notes quoted a male paragraph opening not on the page and wrongly said the grep found no hits. Audit 496 (W. wanglangensis, Hippasosa thailandica): male opening misquoted, total length put in the wrong sentence. Audit 497 (H. yunnanensis, Mutatus gelao): false grep claims, misattributed total-length sentence, sentence order wrong and the EAW sentence omitted. Audit 498 (M. tujia, tianyan): sentence order wrong and the EAW and CH/AME sentences omitted. Audit 496's first Replacement block held the wrong records and was rewritten by its auditor; the merge asserted taxon, quote, eye label and trait against the unit file.
