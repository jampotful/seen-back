# desk-d390 progress

Angle: open-access arachnid taxonomy papers (spiders) with printed per-species eye sizes or diameters outside the papers already used. 34 records from two open Pensoft papers (log docs/views/evidence/desk-d390.jsonl). check.py: 0 problems.

## Filed
- ZooKeys 1161: 69-87 (10.3897/zookeys.1161.102375; Mi X, Li S, Pham D-S, 2023; Araneidae, Vietnam): sentence 'Eye sizes and interdistances: AME ..., ALE ..., PME ..., PLE ...' for Zhuaraneus eugenei (male holotype, female paratype), Z. ethani (female holotype), Araneus liami (male holotype, female paratype), Wangaraneus ryani (male holotype, female paratype), four eyes each, 28 records, trait sensory_anatomy (label 'sizes'; Methods define no eye dimension). Taxon names are current WSC combinations; printed names are Araneus eugenei, A. ethani, Hypsosinga ryani.
- ZooKeys 1213: 95-182 (10.3897/zookeys.1213.133178; Huber BA, Meng G, 2024; Pholcidae, Saudi Arabia): 'diameter PME x µm ... diameter AME y µm' for male holotypes of Micropholcus dhahran, M. harajah, M. alfara, 6 records, sensory_anatomy with a note that the label is the bare word 'diameter' (not 'Eye diameters'), so an auditor may promote to eye_diameter_mm. Values are µm / 1000.

## Weak spots
- Fetch tool cuts sentences at 125 characters; each eye sentence is joined from two consecutive pieces. All Methods, type and neighbouring sentences are tool-returned.
- ZooKeys 1161 liami paratype list is summarised by code in conditions (12 lines), the measured paratype line is verbatim.
- ZooKeys 1213: the page text returned stops inside Micropholcus abha; the other new species (tanomah, bashayer, maysaan, darbat, shaat, ghar, khenifra, bukidnon, abha) were not read. Only the three species with full text were filed.
- Crossref: first check of ZooKeys 1161 used a URL built from the printed DOI (contrary to the desk rule); it was repeated with a list query (query.bibliographic) and agrees. ZooKeys 1213 checked by list query. Both: CC BY 4.0 vor.
- WSC: species pages opened for all seven species; family pages not opened (UNCHECKED).

## Not filed and why
- Hypsosinga zioni (ZooKeys 1161, female holotype): WSC page 61519 lists it as a junior synonym of Wangaraneus cruciformis (logged 2026-09-28).
- Micropholcus jacominae male (redescription, ZooKeys 1213): measured specimen not identified in the text read.
- ZooKeys 862 Zhezhoulinyphia (id 31406 reached): 2019, outside the year range.
- BDJ 12 e128884 (Khorata ninhbinh): prints 'Eye interdistances and diameters' for a single new species; not read further. Taxonomy 4:574 (Paleotoca diminas, MDPI): eyes absent. EJT download 313/621: fetch failed. Other searches returned only Plazi/Zenodo/aggregator copies.

## Desk disposition after audits 599-603 (2 November 2026)
All 34 lines (ZooKeys 1161: 69-87 Zhuaraneus eugenei, ethani, Araneus liami, Wangaraneus ryani; ZooKeys 1213: 95-182 Micropholcus dhahran, harajah, alfara) were audited by fresh Opus agents (audits 599 to 603). No value, quote, unit, bibliography or licence errors; counted faults on 16 lines (lead-ins filed as headings, "Material and method" heading wording, liami paratype list summarised by code, Holotype:/Paratypes: punctuation). Hypsosinga zioni was dropped by the unit (junior synonym). Every line replaced with the auditor's corrected text and merged; none dropped. Micropholcus values are micrometres in the quote converted to mm (stated in each measurement field); they stay sensory_anatomy because the label is a bare "diameter PME/AME". Owner question: desk-d371 filed a similar bare "diameter" label as eye_diameter_mm; should the two be aligned? Crossref vor unchecked.
