# desk-d378 progress

Angle: multi-species spider papers with per-species eye sentences. 40 records from two European Journal of Taxonomy papers, about 27 search/fetch calls. check.py on the log: 0 problems. Every value was re-read against its quote by script (Uaica by position in the 'diameters' list, Heteropoda by regex on the eye's own label, 'CH' and interdistance labels excluded).

## Filed (docs/views/evidence/desk-d378.jsonl)
- EJT 989: 24-49 (10.5852/ejt.2025.989.2879; publisher PDF prints CC BY 4.0): Uaica (Sparassidae) carapiranga (male holotype, female paratype MPEG 30844), juruena (female holotype), karipuna (male holotype), mapia (male holotype), uatuma (male holotype, female paratype IBSP 7346). eye_diameter_mm; 28 records (7 sentences x AME, ALE, PME, PLE). WSC spec-data 71734-71737 opened (accepted Sparassidae); uatuma page not reachable, flagged UNCHECKED, owner question in each uatuma note.
- EJT 1022: 277-287 (10.5852/ejt.2025.1022.3091; publisher PDF prints CC BY 4.0): Heteropoda curvata and flamma (male holotypes), lucerna (female holotype). sensory_anatomy (Methods list abbreviations only; the sentence is labelled 'Eyes:'); 12 records. WSC spec-data 72184, 72185, 72858 opened (accepted Sparassidae).

## Weak spots
- Uaica: the 'Eyes: diameters a, b, c, d; interdistances ...' sentence has no per-eye labels. The eye is assigned by position using the Methods order 'AME, ALE, PME, PLE'. The Methods sentence reached me as a fragment of the measurement paragraph; auditors should confirm that order on the page. If the order is not as returned, all 28 Uaica records are wrong together.
- Uaica holotype lines other than carapiranga came as summaries, not verbatim; stated in conditions. The genus-level eye sentences (Eight eyes arranged..., Clypeus low...) came via a fetch summary.
- Heteropoda curvata: the fetch tool returned the paratype line as 'CHINA' while the holotype line reads 'MALAYSIA'; not resolved.
- All text came through fetch-tool summaries; no full paragraph was read word for word, and notes say so.

## Not filed
- Pseudopoda xiaozhua, yangae, ying (ZSE 101(1) 10.3897/zse.101.136177): zse.pensoft.net article pages are not reachable (permission refused); Plazi treatment pages are third-party copies and the treatment page returned only a redirect. Not filed.
- Crossref list queries were rate-limited on three tries, so no new-paper listing was possible.
- Shaanxinus shizhuziensis (Zootaxa 5257, closed). Platnickina, Latouchia, Ischnothyreus, Trilacuna, Gamasomorpha, Zora, Wangaraneus, Poeciloneta, Parazygiella, Oedothorax simianensis, EJT 1007: not opened.
- Other EJT Rheims 2025 papers (2025a, 2025b) are likely to use the same 'Eyes: diameters' format; not searched.
