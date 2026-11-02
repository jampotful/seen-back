# desk-d397 progress

Angle: Salticidae continuation (ZooKeys 1192 leftovers, ZooKeys 1221 later species, then another open Pensoft paper). 42 records (log docs/views/evidence/desk-d397.jsonl). check.py: 0 problems, also with --require-evidence-kind.

## Filed
- ZooKeys 1192: 141-178 (10.3897/zookeys.1192.114589; Wang C, Mi X, Li S, 2024; page prints CC BY 4.0, Crossref vor CC BY 4.0 re-checked): Stertinius liqingae, Synagelides tianquan, Yaginumaella erlang, male and female each, AME/ALE/PLE; 18 records.
- ZooKeys 1148: 119-165 (10.3897/zookeys.1148.98271; Wang C, Li S, Pham D-S, 2023; Crossref vor CC BY 4.0 checked; publisher XML text prints CC BY 4.0): Chinattus crewsae, Chinattus logunovi, Eupoa maidinhyeni, Eupoa maddisoni, male and female each, AME/ALE/PLE; 24 records.
- All sensory_anatomy: sentences print 'Eye sizes', Methods define no eye dimension. Values are the figures printed against each eye label; no zeros. WSC species pages opened for all 7 species (accepted); family pages not opened.

## Weak spots
- Fetch tool summarises and cuts at 125 characters; type lines and neighbouring sentences are tool-returned pieces, joined where noted. Neither paper says which type specimen was measured; mixed-sex paratype ranges stated.
- ZooKeys 1148 prints no family heading and no Results heading; where-path is Taxonomy, genus, species. The female headings of the four 1148 species were not returned.
- Page copy for 1148 is the publisher XML download (URL from my search results), not the article_preview page.

## Not filed and why
- ZooKeys 1192: Synagelides medog (female only) and Phintella longapophysis (female): both fetches return identical numbers (AME 0.36, ALE 0.20, PLE 0.19, AERW 1.04, PERW 1.08, EFL 0.84, total length 4.06, abdomen 2.48 x 1.24) for two different species; possible duplication in the paper or a tool artefact, held out. Icius zang female (missing comma) not retried.
- ZooKeys 1221: the preview and XML text stop at Piranthus maddisoni (preview) or Irura qiuhangi (XML); Simaetha hainan, Stertinius lhoba, Synagelides kongmingi/xuandei/yunchangi/yidei/zilongi, Yaginumaella daweishan/moinba/pingbian unreachable from search-result URLs (BHL page is metadata only; Plazi and PMC copies not used).
- ZooKeys 1148: Eupoa ninhbinh, E. zabkai, Indopadilla cuc, Synagelides ani/mii/pengi/sancha, Yaginumaella hagiang not reached (text stops in Eupoa ninhbinh type material).
- BDJ 12: e138400 (On two species of Phintella from Hainan; Phintella hongkan M/F, P. liae female; labels AME/ALE/PME): eye sentences retrieved, but the type data are structured fields and no verbatim type statement came back, and the Crossref check was rate-limited; lead for a later unit.
