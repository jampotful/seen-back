# desk-d407 progress

Angle: eye-size records, wider net, second round. 44 records from four open Pensoft papers (log docs/views/evidence/desk-d407.jsonl). check.py and check.py --require-evidence-kind: 0 problems.

## Filed
- Zoosystematics and Evolution 101(2): 711-734 (10.3897/zse.101.146895; Zhang J et al., 2025; Mimetidae): Mimetus guiyang (female holotype), M. lanmeiae (male holotype), and M. caudatus Wang, 1990 (male and female of the Guizhou series, not types), 16 records, eye_diameter_mm (Methods: 'Eye diameters were measured at the widest part.').
- Biodiversity Data Journal 13: e153747 (10.3897/BDJ.13.e153747; Jiang Z et al., 2025; Phrurolithidae): Aculithus languan (female holotype), A. ruijin (male holotype, female paratype), 12 records, sensory_anatomy (sentence prints 'Eye sizes'; Methods define no eye dimension).
- Biodiversity Data Journal 12: e133875 (10.3897/BDJ.12.e133875; Wang Z et al., 2024; Anyphaenidae): Anyphaena leidashi, male holotype and a female, 8 records, sensory_anatomy.
- Biodiversity Data Journal 14: e182804 (10.3897/BDJ.14.e182804; Wang Y et al., 2026; Trachelidae): Planochelas jingda, male holotype and female paratype, 8 records, eye_diameter_mm (label 'Eye (Fig. 1A and B) diameters and interdistances'; the figure reference splits the literal 'Eye diameters', flagged for audit).

## Weak spots
- Fetch tool returns paraphrase plus pieces of about 125 characters; eye sentences are joined from consecutive pieces. Type lines for Aculithus and Anyphaena came as summaries of occurrence records, not verbatim.
- Aculithus languan: holotype and paratype both print catalogue Phu-178. Anyphaena leidashi: no catalogue numbers; the female is headed 'Female. As in male, except as noted.' with no paratype word.
- Mimetus caudatus: description lead-ins returned as 'Male (MGNU-2014-MIMC001)' and 'Female (MGNU-2014-MIMC002)'; the word 'Measurements.' not confirmed for them. These are new specimens of an existing species, not types.
- Licence sentences for the three BDJ papers returned as the first part only ('...Creative Commons Attribution License (CC BY 4.0)'); full sentence verbatim only for ZSE. Crossref not read for any paper (UNCHECKED); DOIs are as printed on the publisher pages.
- WSC: species pages read for M. guiyang, M. lanmeiae, M. caudatus, A. languan, A. ruijin, P. jingda (all accepted, no synonyms). Anyphaena leidashi: species page not opened; only the WSC list of taxa included for the paper (refincluded/17942) was read (UNCHECKED validity).

## Not filed and why
- (a) Same-paper species of desk-d406: Shuqiangius (ZooKeys 1261) has only S. chuan (filed) and a comb. nov. S. rarobulbus with no eye data; BDJ 10 e94853 describes only the two Eresus species already filed; Subterranean Biology 52 describes only O. libmanan and O. tangcongvaca; ZooKeys 1116 species already filed. Nothing further.
- Scytodes tanjiashui (BDJ 14 e181164): already on main (desk-d383). Phlogiellus khampheng (ZooKeys 1247) and Spiricoelotes metyr/zhengi (ZooKeys 1245) are in the avoid list; ZooKeys 1189 Liphistius prints no eye measurements. Troglocoelotes sinanensis (BDJ 11 e103265): no eye measurements printed.
- Leads not opened as a publisher page or lacking open licence on the copy read: Cybaeus eremospelyngus (Species Diversity 30(1): 49-54, 10.12782/specdiv.30.49, CC BY 4.0 on the J-STAGE page; the page gave no eye numbers and the full-text PDF reached in search was a university repository copy, not used). Cheiracanthium sistani and C. monstrum (Zamani and Marusik, 2025; Zootaxa, likely closed). Pinelema (Taxonomy 4: 28, MDPI) not opened.

## Desk disposition after audits 694-699 (2 November 2026)
All 44 lines merged with the auditors' replacement text. Counted errors 0; nothing dropped or held out. Text faults corrected: 694 sub-headings, second sex, Methods, paratype hedging (28); 695 "Measurements." lead-ins, holotype "Examined.", M. caudatus female first described, Methods, licence, Crossref remark removed (36); 696 licence, Methods, journal string ": e153747", Crossref claim, dates, neighbouring sentence, Materials, WSC family authority (60); 697 licence, Methods, heading paths (all 8); 698 licence, neighbouring sentences (lines 37-40); 699 neighbouring sentences, Fig. label, licence, Methods (20).
Desk ruling: Planochelas jingda (lines 37-44) filed as sensory_anatomy. Audit 699 moved lines 41-44 there because the Methods print no eye-diameter definition and the label "Eye (Fig. 1A and B) diameters" is split by a figure reference; audit 698 kept eye_diameter_mm for 37-40. The desk applied 699's reading to all eight for consistency (merge script edit to trait, structure, method and note of lines 37-40). Owner question: does a label split by a figure reference count as printing "Eye diameters".
Owner questions carried: Anyphaena leidashi WSC species page not reached (validity unchecked); Crossref not reached; M. caudatus is a new-specimen description of an existing species (WSC Df).
