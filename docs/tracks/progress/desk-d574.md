# desk-d574 progress

evidence_intake: evidence-kind-v2; intake_base: 9d4ef53ed7d533b7d1ceb2756dd18c71b76ffc96 (origin/main when checked).

Angle: the pupil_shape vein is drained, so the switch trait is sensory_anatomy with structure tympanum / external ear opening (about 14 amphibian rows on main from desk-d332, d344, d354, d365, d366; no species below is among them). About 35 WebSearches. 8 records filed (docs/views/evidence/desk-d574.jsonl), evidence_kind anatomical_presence (3) or anatomical_measurement (5). check.py: 0 problems (plain and --require-evidence-kind); check_submission.py: 8 new, 0 problems.

## Filed (all Pensoft, CC BY 4.0 sentence read on the article_preview page; ASW or Reptile Database page opened from my own search)
- Brachytarsophrys wui (ZSE 102(1): 71-85, 10.3897/zse.102.161437): tympanum completely hidden (holotype, cuts marked).
- Leptobrachella wumingensis (ZooKeys 1178: 1-16, 10.3897/zookeys.1178.106038): tympanum diameter about 49% of eye diameter (holotype).
- Gracixalus weii (ZSE 101(1): 405-417, 10.3897/zse.101.133735): tympanum 0.69 times eye diameter (holotype).
- Leptobrachella yongshunensis (ZSE 101(1): 103-117, 10.3897/zse.101.135586): TD 1.8 mm (holotype).
- Pristimantis etsa (ZooKeys 1282: 205-228, 10.3897/zookeys.1282.187506): tympanic membrane differentiated, annulus rounded (whole 9-word sentence).
- Pristimantis fergusoni (ZooKeys 1269: 83-105, 10.3897/zookeys.1269.162260): tympanum diameter 52% of eye diameter (holotype, one cut).
- Vitreorana micaelae (ZooKeys 1291: 93-110, 10.3897/zookeys.1291.193210): TD 42.8% of ED (whole sentence; the Diagnosis prints ~33% for the species, stated in conditions).
- Sphenomorphus tamchucensis (ZooKeys 1266: 263-279, 10.3897/zookeys.1266.176724): external ear opening nearly round, smaller than eye length, without lobules; tympanum sunk (Reptile Database page opened; two cuts).

## Searches that reached the full text
Exact title plus "article preview" returned the article_preview.php link in every case; ASW pages came from "amphibiansoftheworld.amnh.org <species> <authors year>".

## Weak spots
- WebFetch is a page reader that returns pieces of about 125 characters; sentences were reassembled from numbered pieces and are not checked against raw page text. The reader contradicted itself on the ending of the Sphenomorphus puhoatensis holotype sentence, so that species was dropped.
- Holotype sentences are long semicolon chains in Chinese megophryid and rhacophorid descriptions, so five quotes carry marked cuts; each cut was chosen so that no tympanum qualifier is lost.
- Zootaxa papers (Cophixalus flavopunctatus) skipped as a dead venue. Not filed: Sphenomorphus puhoatensis (ZooKeys 1279; reader unreliable), Brachytarsophrys wui Diagnosis item (part of a 100-word sentence).
- Crossref not used. Family for the two Pristimantis comes from the ASW path (Craugastoridae); fergusoni's title says Strabomantidae.

## Desk disposition after audits 1123, 1124 (4 November 2026)
All 8 lines merged with the auditors' replacement text. Values, trait, names, families, citations, DOIs and licences were correct and no line repeats main (B. wui's eye_diameter_mm rows are desk-d457, a different trait; the skink's eye-length rows from desk-d476 are the same trait family but a different finding). Faults fixed on all eight: paratypes left out, preservation paraphrased instead of quoted, fergusoni's cut dropped the annulus qualifier, tympanum wording from the etsa Definition and the fergusoni and micaelae Diagnoses missing, an invented "Taxonomy" heading and a 70% ethanol sentence about liver tissue (micaelae), heading path omitting "Results >" and a self-contradicting search statement (wumingensis). 8 of 8 counted as errors; all fixed.
