# desk-d576 progress

evidence_intake: evidence-kind-v2; intake_base: 13d9f795a45c3369698b3e5af9ff37594196de65 (origin/main when checked).

Angle: sensory_anatomy, tympanum / external ear, from Pensoft new-species descriptions (OLD-ANGLE paragraph ignored). 6 records (docs/views/evidence/desk-d576.jsonl), evidence_kind anatomical_measurement (5) or anatomical_presence (1); one record per species. check.py: 0 problems (plain and --require-evidence-kind). About 39 WebSearches; no Crossref, no proxy hosts, every WebFetch URL came from my own search results. Form follows desk-d574 on main (anatomical_measurement for ratios, anatomical_presence for presence/absence).

## Filed (licence sentence read on the publisher article_preview page; ASW page opened from my own search)
- Stumpffia froschaueri, ZooKeys 933: 139-164 (10.3897/zookeys.933.47619): holotype ZSM 169/2019, tympanum about 58% of eye diameter (one cut; Table 1 TD 1.1 / ED 1.9 agrees). Search: "Stumpffia froschaueri new species Madagascar ZooKeys 933 amphibiansoftheworld"; ASW via '"Stumpffia froschaueri" Amphibian Species of the World holotype ZSM 169/2019'.
- Noblella madreselva, ZooKeys 516: 71-84 (10.3897/zookeys.516.9776): holotype CORBIDI 15769, tympanic membrane absent, annulus not visible (one cut). Search: "Noblella madreselva new species ZooKeys tympanic membrane article preview" (also reached the ASW page).
- Hyloscirtus tolkieni, ZooKeys 1141: 75-92 (10.3897/zookeys.1141.90290): holotype ZSFQ-4142, TD/ED = 0.41 (two cuts). Search: "new species Hyloscirtus OR Gastrotheca OR Osteocephalus OR Boana tympanum holotype ZooKeys article preview Pensoft".
- Oreophryne cameroni and O. parkopanorum, ZooKeys 333: 93-121 (10.3897/zookeys.333.5795): whole sentences, TY/SV 0.045 and 0.050. Page prints CC BY 3.0 (quoted). Search: "new species Oreophryne OR Cophixalus OR Litoria OR Callulops OR Papurana tympanum New Guinea Vertebrate Zoology OR ZooKeys article preview".
- Ranitomeya aquamarina, ZooKeys 1236: 51-83 (10.3897/zookeys.1236.146533): holotype INPA-H 47568, tympanum 44.4% of eye diameter (whole sentence). Same species and DOI have an eye_diameter_mm row on main (desk-d343, different trait). Search: "new species Ameerega OR Ranitomeya OR Hyalinobatrachium OR Centrolene OR Allophryne tympanum holotype ZooKeys OR \"Evolutionary Systematics\" article preview".

## Weak spots
- All text came through the WebFetch page reader (about 125 characters per piece); sentences were reassembled from pieces and sentence starts were checked by asking for the preceding text. Holotype designation details (sex, SVL) for the Oreophryne holotypes and Noblella come from the reader's reading of the type line / figure caption.
- The Oreophryne page header prints ZooKeys 333: 93-121 while its Citation line prints 75-103; ASW cites pages 96 and 103, consistent with 93-121.
- ASW lists Oreophryne under Asterophryinae with 'Asterophrys' names by implication (Dubois et al. 2021); filed under the paper's names. Noblella family Craugastoridae per paper and ASW path.

## Not filed and why
- Oreophryne gagneorum (same Kraus paper, sentence read): no ASW species page reached.
- Rhinella yunga (ZooKeys 371: 35-56): ASW page not reached and the absence clause sits in a ~2,300-character sentence the reader would not return.
- Gekko wuzhengjuni (ZSE 102(2): 719-729): ear clause is part of one very long sentence and no Reptile Database page was reached (other units reported the same).
- Pristimantis maryanneae (ZooKeys 1081): ASW page reached, article_preview page not reached from my own results.
- Scincella ngati, Sphenomorphus lingnanensis, Leptobrachella deocaensis: dropped by earlier units (see d575, d572 notes); not retried. Vertebrate Zoology 66(2) Oreophryne (id 31544): reader returned front matter only.
- Searches for lizard/snake ear-opening papers (ZooKeys, Herpetozoa) returned only figure pages, novataxa blog pages and already-used species.

## Desk disposition after audits 1127, 1128 (4 November 2026)
All 6 lines merged with the auditors' replacement text. Quotes, licences (CC BY 3.0 and 4.0), citations, ASW names and main-repeat checks passed on every line (ZooKeys 333 pages 93-121 confirmed). Errors: line 6 (Ranitomeya aquamarina) left out that Table 2 gives the holotype as TD 0.9 / ED 1.0 mm, which contradicts the 44.4% in the text (the ED value looks misprinted); lines 1-3 and 4-5 carried only faults (missing paratypes and paratopotype, paraphrased preservation and caliper sentences, incomplete heading paths, field-tag wording, holotype code not as printed, a misquoted ASW heading, and the Hyloscirtus Diagnosis clause on the supratympanic fold). Counting rule applied by the audits: 7 faults on lines 1-3 across all three records, which the auditor counted as 3 errors; 1 error on lines 4-6. 4 of 6 counted as errors; all fixed.

Open owner question (audit 1127, line 2): Noblella madreselva text says the tympanic membrane is absent and the annulus not visible, while Table 1 prints a holotype tympanum diameter of 0.8 mm. The merged record discloses the conflict in its conditions; the owner may prefer to drop it.
