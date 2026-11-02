# desk-d438 progress

Angle: eye-size records, wider net, thirty-third round. 8 records from one open paper (log docs/views/evidence/desk-d438.jsonl). check.py and check.py --require-evidence-kind: 0 problems.

## Filed
- Australian Journal of Taxonomy 5: 1-8 (10.54102/ajt.lmcbc; Wilson JD, Harvey MS, Rix MG, 2022; Idiopidae): Euoplos eungellaensis, male holotype QMB S116668 (sentence prints 'Eye diameters', trait eye_diameter_mm, 4 records) and female paratype QMB S116669 (Ocular region sentence without that label, trait sensory_anatomy, 4 records). WSC species page 60625 opened: valid.

## Weak spots
- The fetch tool returned the PDF in reworded pieces; the two eye sentences and the licence line were re-requested piece by piece and joined. The type list and Methods are tool summaries, said so in conditions.
- Licence is the PDF's copyright line (CC BY 4.0); the AJT article page prints no licence sentence. Crossref not read (UNCHECKED). The PDF header title was returned with ', sp. nov.' while the AJT page and WSC omit it; the page form is used.
- The paper prints no Class/Order/Family heading.

## Not filed and why
- ZooKeys 1254 Hahniidae, 1253 Linyphiidae, 1229 Atypus, 1239 Houcosa, 1226 Hippasosa, 1255 Qianlingula, 1200, 1202, 1216, 1175: already on main or on the avoid list. ZooKeys 1239 Kuncosa ningboensis is a new combination with no specimen code (skipped).
- ZooKeys 1209 Belisana and 1216 Belisana: PME only. JoTT 7(3) Thomisus telanganaensis: no numeric eye sizes; JoTT 7(9) reply: one comparison sentence with AME and ALE only.
- Other AJT papers read (Aname hetaera AJT 95, Proshermacha AJT 43, 19, 115, Bungulla pipilata AJT 102): no per-eye diameters.
- Arachnology 20(1) Trabea hirsuta, T. obscura: BioOne page returned meta tags only, no text. EJT 1013 Stethorrhagus, EJT 1004 Cybaeodes, EJT 976 Tanasevitch: no publisher text reached. Zangaraneus zhishengi (BDJ 14 e199306) already on main.

## Leads
- Other Euoplos and Idiopidae papers in the Australian Journal of Taxonomy that print 'Eye diameters:' (searched once, none reached).
- AJT URLs returned by search but not opened: taxonomyaustralia.org.au/ajt/papers/uN5a2aadPK and vg17c0ro0j.

## Desk disposition after audits (2 November 2026)

Audit 843 judged all 8 lines. Four errors (lines 1-4): the Methods define no eye diameter and only the male sentence carries the label "Eye diameters", so the male lines moved from eye_diameter_mm to sensory_anatomy, matching the female lines (one trait reading per paper). All 8 lines also took fixable text corrections (type list as printed, `where` with the "Taxonomy" heading). Values, quotes, licence (CC BY 4.0 on the PDF), source and WSC status passed. Nothing dropped. All 8 merged with the auditor's replacement text.
