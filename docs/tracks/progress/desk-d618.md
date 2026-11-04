# desk-d618 progress

Angle: African and Madagascan reptile new-species papers (chameleons, geckos, skinks, snakes) in Evolutionary Systematics, Zoosystematics and Evolution and Vertebrate Zoology 2016-2025 that define ED and print a per-specimen mm table; Reptile Database authority. Log: docs/views/evidence/desk-d618.jsonl, trait eye_diameter_mm, evidence_kind anatomical_measurement. 2 records. check.py: 0 problems for desk-d618 (plain and --require-evidence-kind). About 40 WebSearches.

## Filed
- ZSE 95(1): 95-106 (10.3897/zse.95.32818; Scherz, Köhler, Rakotoarison, Glaw, Vences 2019) Brookesia tedi (Chamaeleonidae): holotype ZSM 438/2016 ED 1.6 and paratype ZSM 439/2016 ED 1.8 (Table 1 ED row; Methods list 'ED, eye diameter'; calliper to 0.1 mm; caption 'all in mm'). Reached by the unfiltered search 'Brookesia tedi new dwarf chameleon Marojejy Zoosystematics and Evolution 95 95-106'; Reptile Database page opened from the search 'Brookesia tedi Scherz Köhler Rakotoarison Glaw Vences 2019 reptile-database.reptarium.cz'.

## Weak spots
- Text came through the WebFetch reader (article_preview page and XML); the Table 1 column-to-code mapping is the reader's reading. Reptile Database page prints no explicit 'valid'.
- One WebFetch (zse.pensoft.net/article/9945/) was a URL I typed rather than one from my results; it was refused (PROVENANCE_REQUIRED) and not retried. The same paper was later reached from its own search result (article_preview.php?id=9945).

## Not filed and why
- Afroedura wulfhaackei (holotype PEM R24234) and A. praedicta (holotype NB 854), ZSE 97(1): 55-82 (10.3897/zse.97.57202, CC BY 4.0): Methods define 'eye diameter (ED, measured in horizontal orientation)', but the per-specimen Tables 5 and 6 label the row 'Eye distance' (2.3 and 2.6), and the XML was cut before the tables. Lead if the table label can be tied to ED (Table 4 header uses 'ED (eye diameter)'; diagnosis text says eye 2.3 mm and 2.6 mm wide).
- Atractaspis branchi, ZSE 95(1): 107-123 (10.3897/zse.95.31488): Methods define no eye measurement; eye diameters appear only as description text (holotype ZMB 88529 1.0 horizontal / 0.8 vertical mm; paratype MSNS Rept 280 1.5 / 1.0).
- Trioceros wolfgangboehmei (ZSE 97: 161-179): d616 lead, left to d616 (merged at cc242876a).
- Panaspis ericae / P. mundavambo (Evol. Syst. 8(2): 167-182) and Afroedura otjihipa (ZSE 98(2): 435-453): XML and landing pages cut before the Methods and tables.
- Madascincus miafina / pyrurus (ZSE 92(2): 257-275): Methods do not define ED; Haute Matsiatra survey (ZSE 97(2)) and Tolley North West survey (ZSE 99(1)): no new species or no table.
- Calumma nasutum complex (Vertebrate Zoology 70(1): 23-59): no ED measurement; copyright line only.
- Zootaxa venues (Lygodactylus herilalai) dead; no Vertebrate Zoology African reptile pages returned by filtered searches.

## Desk disposition after audits (4 November 2026)
Audit 1246 judged both lines: 0 errors, 2 merged with the auditor's note extension (heading path, eye passage, type block). Unit slip disclosed: one WebFetch on a URL the unit had built (zse.pensoft.net/article/9945/) was refused PROVENANCE_REQUIRED and not retried; the records come from a later own-search result. Leads left unfiled: Afroedura wulfhaackei/praedicta (ZSE 97(1), per-specimen tables label the row "Eye distance"), Atractaspis branchi (no Methods eye definition).
