# desk-d380 progress

Angle: multi-species spider papers with per-species eye sentences. 52 records from four open Pensoft papers, 40 search/fetch calls. check.py on the log: 0 problems. Every value was re-read against its quote by script (regex on the eye's own label; interdistance labels excluded).

## Filed (docs/views/evidence/desk-d380.jsonl)
- BDJ 14: e199306 (10.3897/BDJ.14.e199306; XML prints CC BY 4.0): Zangaraneus zhishengi (Araneidae), male holotype and female paratype TRU-Araneidae-794. sensory_anatomy ('Eye sizes'; Methods do not define the dimension); 8 records. WSC spec-data 73846 opened (accepted Araneidae).
- BDJ 14: e180901 (10.3897/BDJ.14.e180901; XML prints CC BY 4.0): Drapetisca dentata (Linyphiidae), male holotype and female paratype. eye_diameter_mm (Methods: 'Eye sizes were measured at the maximum dorsal diameter.'); 8 records. WSC species page not opened (reference page 18963 only): UNCHECKED, owner question in each note.
- ZooKeys 1245: 269-287 (10.3897/zookeys.1245.152487; XML prints CC BY 4.0): Sinoamaurobius baima (female holotype), chengkou (male holotype, female paratype), yintiaoling (male holotype, female paratype), Amaurobiidae. eye_diameter_mm (same Methods sentence); 20 records. WSC spec-data 72196 and genus catalogue opened; baima and chengkou species pages not opened.
- ZooKeys 1245: 383-397 (10.3897/zookeys.1245.145389; XML prints CC BY 4.0): Spiricoelotes metyr and zhengi (Agelenidae), male holotype and female paratype each. eye_diameter_mm (label 'Eye diameters and interdistances'); 16 records. WSC genus catalogue 241 opened.

## Weak spots
- All text came through fetch-tool answers; eye sentences of Sinoamaurobius, Drapetisca and Spiricoelotes arrived in two pieces (cut at the 125-character limit) and were joined; auditors should confirm each is one sentence.
- Drapetisca: printed 'AME–ALE, 0.05,' with a comma after the label (kept as returned).
- Zangaraneus: male and female print identical eye sizes (0.10, 0.08, 0.13, 0.08).
- Spiricoelotes female paratype catalogue numbers not returned; S. metyr is a reduced-eye cave species (stated in conditions).
- Sinoamaurobius chengkou paratype dates read 17.05.2025 against a 2.11.2022 holotype; catalogue codes printed inconsistently.

## Not filed
- Platnickina (ZooKeys 1250: 135-154, 10.3897/zookeys.1250.158643, CC BY 4.0): eye diameters and interdistances sit inside the long Male/Female measurement sentence (total length, carapace, legs); that sentence is over 40 words, so no whole-sentence quote is possible.
- Gelotia korowai (ZooKeys 1286: 355-372): Description has no eye measurements.
- Zoological Systematics 51(1) Araneidae (Qomolangma, 10.11865/zs.2026101): journal and licence not checked.
- Drapetisca/Spiricoelotes female codes; Sinahahnia yintiaoling, Pseudopoda xiaozhua/yangae/ying, Ischnothyreus, Trilacuna, Gamasomorpha, Zora, Wangaraneus (ZooKeys 1291.203690 not reachable), Shaanxinus, Poeciloneta, Parazygiella, Oedothorax simianensis, EJT 1007, Draconarius jiemuxiensis (Plazi only): not opened.

## Desk disposition after audits 541-547 (2 November 2026)
All 52 records merged with the auditors' replacement lines. 52 of 52 in error (100%), all in conditions, note and author-initial text; no value, quote, trait or taxon changed, no record repeats main, and no line was dropped. Audit 541 (Zangaraneus zhishengi, 1-8): carapace and fovea sentences, the female "Habitus shape and colouration similar to that of male." sentence and full paratype codes omitted; the note said the Methods give "only" glossary items though they print "Methods mainly follow Mi et al. (2024)." Audit 542 (Drapetisca dentata, 9-16): male eye-arrangement sentence, carapace, clypeus, chelicerae, sternum and the female's opisthosoma sentence omitted; Drapetisca is accepted on the World Spider Catalog species list; the printed "AME–ALE, 0.05," is confirmed. Audits 543 and 544 (Sinoamaurobius baima and chengkou, 17-32): clypeus, carapace, chelicerae, Variation and other-sex eye sentences omitted, author initials lost the printed hyphens (J-X, Y-N); both species pages are accepted in Amaurobiidae and the chengkou paratype dates and codes match the paper. Audit 545 (S. yintiaoling female, S. metyr male, 33-40): clypeus, chelicerae, opisthosoma, Variation and genus Eyes-region sentences omitted. Audit 546 and 547 (Spiricoelotes metyr female, zhengi, 41-52): conditions incomplete; zhengi paratypes are 9 females, not 8 (World Spider Catalog "5m 9f").
Owner questions: (1) the Spiricoelotes paper (ZooKeys 1245: 383-397) prints no measurement unit; mm comes only from figure scale bars. Lines 37-52 are filed with units mm and the note says so. Accept inferred mm or hold out lines 37-52? (2) Sinoamaurobius baima and chengkou had no registry check by the unit; the auditors opened both and confirm them.
