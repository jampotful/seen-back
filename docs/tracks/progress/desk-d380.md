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
