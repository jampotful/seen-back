# desk-d418 progress

Angle: eye-size records, wider net, thirteenth round. 32 records from three open Pensoft BDJ papers (log docs/views/evidence/desk-d418.jsonl). check.py: 0 problems, also with --require-evidence-kind.

## Filed
- BDJ 14: e182063 (10.3897/BDJ.14.e182063; Theridiidae): Theridion ganjiangyuan, male holotype JXGJY-24-47-04 and female paratype JXGJY-24-47-06, 8 records, sensory_anatomy (sentence prints 'Eye measurements'; no diameter definition). WSC spec-data 73263 opened, accepted.
- BDJ 14: e178386 (10.3897/BDJ.14.e178386; Agelenidae): Coelotes fani, male holotype and female paratype GXGL-25-144-02, 8 records, sensory_anatomy ('sizes'). WSC spec-data 73285 opened, accepted. Holotype code discrepancy (heading GXGL-25-166-01, type line GXGL-25-165-01) reported in conditions.
- BDJ 13: e176953 (10.3897/BDJ.13.e176953; Phrurolithidae): Otacilia baimashan and O. wulong, male holotype and female paratype each, 16 records, eye_diameter_mm (Methods: 'Eye sizes were measured as the maximum dorsal diameter.'). WSC spec-data 73209 and 73210 opened, accepted.

## Weak spots
- Fetch tool cuts sentences at 125 characters; every eye sentence was joined from two consecutive pieces. Type-material lines are tool-returned metadata, not whole printed lines. Class/Order/Family headings are not printed on these BDJ pages.
- Coelotes fani: paratype list ambiguity (one fetch summary mentioned a male paratype; XML lines list four females). Otacilia: the paper does not say which paratype lot the female comes from; no specimen codes in the Description.
- Crossref not read for any paper (UNCHECKED).

## Not filed and why
- Scytodes tanjiashui (BDJ 14 e181164), Zangaraneus zhishengi (e199306), Drapetisca dentata (e180901): already on main.
- Khorata qiyunshanensis (BDJ 12 e141018) and Belisana wangchengi (BDJ 12 e125111): only a PME value is printed (AME absent, no ALE/PLE); not filed.
- Tegenaria amirani (Caucasiana 4): no eye measurements. Cizauskas et al. Taxonomy 4(3):28 (Prodidomidae cave genus): eyes absent. EJT 1067 Morocco (sixteen new species): publisher PDF not reached. Titanidiops logunovi (Arachnology 20(3)): no publisher page reached. Zootaxa papers (Pandercetes, Otiothops, Oedothorax): not open access, skipped. ZooKeys 1116 and BDJ 10 e94853: the Eresus paper has only the two species already filed.
- Leads: BDJ 12 e130526 Xilithus qizimeishanensis (not opened); BDJ 14 e183760 (not reached).

## Desk disposition after audits 756-759 (2 November 2026)
Filed 32, merged 32, counted errors 0. All faults were text faults (licence sentence cut or fragmentary, WSC string or authority, heading path, Description lead-ins split, paratype sex unresolved) and are corrected from the auditors' Replacement blocks. Nothing dropped. Coelotes fani holotype is printed under both codes GXGL-25-165-01 and GXGL-25-166-01; both are recorded. Leads: BDJ 12 e130526 Xilithus qizimeishanensis; EJT 1067 Morocco.
