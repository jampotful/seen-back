# desk-d431 progress

Angle: eye-size records, wider net, twenty-sixth round. 51 records (log docs/views/evidence/desk-d431.jsonl); check.py and check.py --require-evidence-kind: 0 problems for this file. About 33 searches.

## Filed
- ZooKeys 1137: 75-108 (10.3897/zookeys.1137.96306; Mi & Li 2022; Araneidae): Araneus bidentatus, A. bidentatoides, A. complanatus, male holotype and female paratype each, AME/ALE/PME/PLE (24 records). Sentence 'Eye sizes and interdistances', Methods define no eye dimension: sensory_anatomy. WSC pages 67451, 67452, 67453 accepted.
- ZooKeys 1072: 49-81 (10.3897/zookeys.1072.73345; Mi & Li 2021; Araneidae): Acusilas tongi, Chorizopes yui, male holotype and female paratype each (16 records), sensory_anatomy. WSC pages 66220, 66221 accepted.
- Zoosystematics and Evolution 99(2): 299-305 (10.3897/zse.99.103893; Kaya et al. 2023; Agelenidae): Anatextrix monstrabilis, male holotype and female paratype (8 records), sentence 'Eye sizes:', sensory_anatomy. WSC page 68024 accepted.
- European Journal of Taxonomy 1067: 1-88 (10.5852/ejt.2026.1067.3292; Lecigne et al. 2026; Dysderidae): Dysdera asaahil male holotype; D. sidimaafa male holotype and female paratype (3 records), AME. Sentence prints 'anterior eyes diameter': eye_diameter_mm, with the strict-reading caveat and the anterior-eyes = AME inference stated in the note. WSC pages 73792, 73793 accepted.

## Weak spots
- The fetch tool returns pieces of 100 to 125 characters; sentences and type lines are rejoined pieces. Neighbouring sentences for Araneus complanatus were not returned. Acusilas tongi and Chorizopes yui paratype lists are abridged where marked.
- Anatextrix female: heading 'Female (paratype, ZMUT)' with no specimen number.
- Dysdera paragraph: fetch tool reported the first word of the measurement paragraphs garbled; the sentence begins 'Total length' as returned. D. sidimaafa female code (CSL MOR_1637) is from a tool summary.
- Licence sentences for ZooKeys 1137, 1072 and ZSE came from the publisher XML via the fetch tool; Crossref version of record not reached (UNCHECKED). Family pages at WSC not opened (UNCHECKED).

## Not filed and why (leads)
- Araneus arcuatus (ZooKeys 1137): eye values read (male AME 0.10, ALE 0.08, PME 0.10, PLE 0.08; female 0.10, 0.08, 0.13, 0.08) but no WSC species page reached; file once the page is seen. Araneus corrugis (female holotype), A. cucullatus and the other ZooKeys 1137 species: sentences not read.
- ZooKeys 1072: Chorizopesoides guoi (WSC page 66222 in results, eye sentence not read), Deione, Hypsosinga, Mangora, Milonia species not read.
- EJT 1004 Cybaeodamus ampullatus, C. spinosissimus, C. malkini (10.5852/ejt.2025.1004.2965; 'Eye sizes and interdistances' AME/ALE/PME/PLE read only from a repository copy at africamuseum.be, which the licence rule excludes; the publisher PDF fetch was blocked). EJT 1016 zodariids (publisher download failed twice).
- EJT 981 Indothele (ocular tubercle only), AJT 118, 102, 109 (ratios or none), EJT 1067 other species (no numeric eyes in the parts read; Zelotes, Oecobius sections truncated).
- Zootaxa Sidymella (not open access).
- Pensoft was in maintenance early in the unit and recovered later; article_preview pages still failed for ZooKeys 1239 Houcosa zhaoi.
