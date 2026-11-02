# desk-d440 progress

Angle: eye-size records, wider net, thirty-fifth round. 24 records (log docs/views/evidence/desk-d440.jsonl), trait sensory_anatomy (the sentences print 'Eye sizes'; the Methods give no eye-size definition). check.py and check.py --require-evidence-kind: 0 problems for this file.

## Filed
- ZooKeys 1034: 199-236 (10.3897/zookeys.1034.60411; Mi X, Li S, 2021; Araneidae), publisher XML from my search results, CC BY 4.0 sentence printed: Eriovixia ganae (male holotype, female paratype), E. liuhongi, E. tangi (male holotype, female paratype each). 24 records. WSC pages 65756, 65757, 65758 opened (accepted).

## Weak spots
- The fetch tool caps quotes at about 120 characters; each eye sentence was assembled from two consecutive pieces and rejoined with one space. Type lists are abbreviated after the first entries where stated in conditions.
- E. ganae: the female heading prints paratype IZCAS-Ar40650 while the type list prints the range 'IZCAS-Ar41649–40650'; both reported as printed.
- Species headings for E. liuhongi and E. tangi were returned by the tool as 'Eriovixia ... sp. nov.' and not otherwise checked.
- Crossref not read (UNCHECKED); the DOI is the one the fetch tool returned from the XML and the WSC pages print.
- Main check: git grep of origin/main (074589ee5) and of every research/desk-* remote branch for the three species names and 1034.60411 returned no hit.

## Not filed and why
- E. pengi, E. wangchengi, E. yaoi, E. yinae, E. zhengi (same paper): the XML text reached ends inside the E. wangchengi Diagnosis and the article_preview page returned no eye sentences. Lead: reach a fuller copy from a new search.
- Searched and dropped: Australoechemus vickyae (African Invertebrates 64(3); no numeric eye sizes); ZooKeys 1209 Belisana (PME only); BDJ Belisana wangchengi (PME only); JoTT Araneus tubabdominus (eye diameters given only as an inequality); Ctenus igatu (BioOne page returned no text); Vitalius ornatissimus (Zoologia 41 e24011; SciELO page failed); Atypus dawei, A. liui and Spiricoelotes already on main.
