# desk-d412 progress

Angle: eye-size records, wider net, seventh round (families and journals not yet filed). 34 records from four open Pensoft papers (log docs/views/evidence/desk-d412.jsonl). check.py and check.py --require-evidence-kind: 0 problems.

## Filed
- Biodiversity Data Journal 13: e153601 (10.3897/BDJ.13.e153601; Cheng, Liu, Wei 2025; Trechaleidae): Metashinobius hikariae, male holotype, AME/ALE/PME/PLE, 4 records, eye_diameter_mm (sentence prints 'Eye diameters and interdistances').
- Zoosystematics and Evolution 99(1): 273-280 (10.3897/zse.99.99227; Villarreal, Chame-Vazquez 2023; Drymusidae): Drymusa huberi, female holotype and male paratype, PME/ALE/PLE (no AME printed), 6 records, eye_diameter_mm (label 'eye diameters').
- Biodiversity Data Journal 11: e109714 (10.3897/BDJ.11.e109714; Gunduz 2023; Desidae): Paracedicus turcicus, male holotype and female paratype, 8 records, eye_diameter_mm (label 'Eye diameters and interdistances').
- Zoosystematics and Evolution 100(2): 705-720 (10.3897/zse.100.124160; Yang, Li, Yao 2024; Linyphiidae): Bifurcia kangding and B. luding, male and female each, 16 records, sensory_anatomy (label 'Eye inter-distances and diameters' is not the label 'Eye diameters'; Methods define no eye dimension).

## Weak spots
- Fetch tool cuts sentences at about 125 characters; eye sentences were joined from consecutive pieces. Drymusa text came from the publisher XML copy (sentence boundaries asked for and returned).
- Metashinobius holotype has no catalogue code on the page; the page prints no Family heading. Paracedicus page prints no Family or Genus heading.
- Bifurcia kangding: the page was not read for the exact 'Male (holotype)' lead-in, so the where field says 'Description'; the female paratype code is not tied to the female in the type list.
- DOIs are as printed on or returned with the publisher page; Crossref was not read for any (UNCHECKED). Year of Bifurcia (2024) comes from the citation returned with the page.
- WSC: Metashinobius hikariae (72089), Drymusa huberi (67877), Paracedicus turcicus (68458), Bifurcia kangding and B. luding (species pages 63231, 63233) opened and accepted.

## Not filed and why (leads)
- Scytodes tanjiashui (BDJ 14 e181164) is already on main (desk-d383).
- Bifurcia labahe, shuangqiao, xiaojin: values and sentences read, but WSC species pages were not opened (UNCHECKED); candidates for a later unit.
- Chicosa cinnameopilosa (ZooKeys 1260: 'Eye sizes were defined as the maximum dorsal diameter', male and female 'Eyes:' lines) is a new combination with no type material, so not filed.
- Zimirina corsica (ZooKeys 1250), Solenysa (ZooKeys 1232), Latrodectus sp. (ZooKeys 1281), Bisetifer tactus (ZooKeys 1230), Nopsma (ZSE 97), Myrmecotypus mazaxoides (ZSE 97): no eye diameters printed.
- Ctenus igatu (J. Arachnol. 50(1)), Zimirina-style BioOne page, ZSE issue PDF 3587: publisher page not reachable. Missulena (ASP 79) reached only a Zenodo copy.
- Unchecked on main by DOI but not opened: ZooKeys 1081.77072 and BDJ 10 e96467 (Chilobrachys), BDJ 11 e113290 (Liphistius), ZooKeys 1037 Songthela, ASP 81 Cenemus, ZooKeys 1124 Chthonopes, 1185.104120 Simonia, 1029 Pimoa, BDJ 9 e73109 Bassaniana.
