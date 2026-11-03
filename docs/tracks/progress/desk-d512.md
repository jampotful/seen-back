# desk-d512 progress

Angle: reptile, amphibian and fish eye_diameter_mm (no spiders). Open-licence Pensoft papers that print eye diameter in millimetres per named specimen. 13 records so far (log docs/views/evidence/desk-d512.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems (plain and --require-evidence-kind). About 30 WebSearches so far.

## Filed
- ZSE 100(3): 851-862 (10.3897/zse.100.120224) Rhacophorus dulongensis: holotype ANU010645 (3.5) and paratype ANU010646 (3.4), Table 3 ED row. The syntype column (BMNH1940.6.1.30, 3.5) and the R. turpes paratype (3.0) are not filed.
  Search: 'Microhyla OR Nyctibatrachus OR Rhacophorus OR Amolops new species holotype paratypes ED eye diameter table mm India OR Vietnam OR Sri Lanka', allowed_domains zookeys/zse/herpetozoa/bdj/evolsyst/vertebrate-zoology .pensoft.net; text at zse.pensoft.net/article_preview.php?id=120224&skip_redirect=1. ASW species page opened (via a second search naming the species).
- ZooKeys 1280: 245-263 (10.3897/zookeys.1280.192981) Odorrana nagao: holotype + 4 paratypes, Table 4 ED row. ASW page opened. Search: 'Leptobrachella OR Boulenophrys OR Odorrana OR Gracixalus new species Guangxi OR Yunnan OR Vietnam holotype paratypes "ED" eye diameter measurements mm' (same allowed_domains) returned related ZooKeys pages; the paper itself surfaced from 'Sphenomorphus OR ... skink' / 'Leptobrachella OR ...' searches and was read at article_preview.php?id=192981&skip_redirect=1.
- ZooKeys 1259: 185-204 (10.3897/zookeys.1259.164646) Leptobrachella kungfu: holotype + 5 paratypes (all males), Table 2 EYE row (EYE defined as eye diameter). ASW page opened. Same search as above (result zookeys.pensoft.net/article/164646/download/xml/); read at article_preview.php?id=164646&skip_redirect=1.

## Weak spots
- All text came through the WebFetch page reader on Pensoft article_preview pages; table rows and column-to-code mappings are the reader's cell-by-cell reading. Several fetches returned a different article than the one requested (Hebius maximus came back for herpetozoa ids); only fetches whose title, DOI and species matched the requested paper were used.
- Crossref not checked. Species validity from ASW pages, which print no explicit 'valid'.

## Not filed and why
- Calamaria berezowskii (ZSE 100(3): 897-911, 10.3897/zse.100.125798; EyeD table row 0.7/-/0.6/0.7/-): the Reptile Database species page was blocked (permission unanswered); only the genus result list was opened. The paper also contradicts itself on eye versus eye-mouth distance. Lead for a unit that can open the species page.
- Ovophis jenkinsi (ZooKeys 1203: 173-187, 10.3897/zookeys.1203.119218): holotype ED 2.7 mm sits in a Description sentence far over 40 words; Table 4 has no ED row. Reptile Database page opened.
- Amolops gudao (ZooKeys 1227: 349-367, Table 1 ED 6.3/6.1/6.6/6.1): no ASW page found, genus page reader returned no species list.
- Cyrtodactylus luci (ED = ear length), C. phamiensis (ED in supplement), Oligodon churahensis (one text diameter, no table), Hemidactylus kalinga (no Methods text), Rhacophorus/Leptobrachella darongshanensis and Gracixalus liusanjieae (holotype only in text or summary tables), Leptobrachella guinanensis (ranges only): held out.
- Fish: Claea dafangensis, Triplophysa (ZSE 102(2) 443-456), Pseudophoxinus galilaeus print eye as % HL only.
- Already on main or other units: Hemiphyllodactylus laowozhenensis, H. lungcuensis, Scincella qianica, Sphenomorphus lingnanensis, Bac Kan amphibian records.
