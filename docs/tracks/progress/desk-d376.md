# desk-d376 progress

Angle: multi-species spider papers with per-species eye sentences. 44 records from two papers, about 38 search/fetch calls. check.py run on the log (0 problems). Every value was re-read against its quote label by label (sizes only; interdistances and clypeus heights not filed).

## Filed (docs/views/evidence/desk-d376.jsonl)
- ZooKeys 1085: 69–99 (10.3897/zookeys.1085.77966; XML prints CC BY 4.0): Phrynarachne (Thomisidae) brevis (female), dreepy (male holotype, female paratype), huangshanensis (male), lancea (female), AME/ALE/PME/PLE each, eye_diameter_mm because Methods say eye sizes are the maximum diameter (20). WSC: spec-data/66347 (dreepy) opened; genus page /genus/3692/Phrynarachne opened and lists the other three; their own species pages were blocked by a permission timeout.
- Zoosystematics and Evolution 101(1): 141-171 (10.3897/zse.101.136177; preview page prints CC BY 4.0): Pseudopoda (Sparassidae) huanglianensis, mamillaris, oliviformis, male and female of new material each (YNZY013/025, 009/010, 011/012), eye_diameter_mm because Methods say eye diameters were measured at the widest part (24). WSC spec-data 67711, 67726, 67737 opened.

## Weak spots
- All text came through fetch-tool summaries; long sentences arrived in two pieces and were rejoined at the semicolon/comma where the piece ended (not at a full stop). Licence sentence read in segments.
- Phrynarachne huangshanensis male and lancea female: no specimen number printed with the description; brevis female is the single Other-material female. Dreepy female is "one paratype" of two listed.
- Phrynarachne received/accepted dates were read (13 Nov 2021, 19 Jan 2022); Pseudopoda dates not returned.
- Pseudopoda: female/other colour sentences were not asked for beyond the male ones listed; Diagnosis eye sentences reported absent by the tool.
- New trait key eye_diameter_mm used as on main (check.py needs "new trait" in the note, included).

## Not filed
- Phrynarachne xuxiake, yunhui, zhengzhongi (new species, same paper): the XML text returned ended inside P. mammillata; their treatments were not reachable.
- Pseudopoda xiaozhua, yangae, ying (new, same paper): preview page returned only xiaozhua's type lines; no descriptions.
- Not opened: Ischnothyreus, Trilacuna, Gamasomorpha, Zora, Wangaraneus, Shaanxinus, Poeciloneta, Parazygiella, EJT 1007, Oedothorax simianensis.
