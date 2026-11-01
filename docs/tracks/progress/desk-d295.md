# desk-d295: eye-state sentences in new species of cave and subterranean fishes, 8 records

Branch research/desk-d295 from origin/main. About 40 WebSearches (3 extended) plus fetches. `python3 -I tools/senses/check.py | grep 'd295\.'`: 8 records, 0 problems. Crossref read for six of the eight DOIs (author order matches the pages; all CC BY 4.0 vor); the Crossref fetch failed for ZooKeys 1281 and 1255 (page CC BY sentence only). Every fetched article URL came from a WebSearch first. Grep of main docs/ and of research/desk-d26x to d29x and audit-3xx branch docs by species and DOI: no repeats. No new trait (eye_type, state as a string).

Filed (docs/views/evidence/desk-d295.jsonl), all Actinopterygii, whole-sentence eye statements from Description sections:
1. Sinocyclocheilus wanlanensis, "Eyes degenerate (dark spots) or absent.", Animals 15(15) 2216; holotype and paratypes, sexes not stated.
2. Triplophysa anshuiensis, "Eyes absent.", ZooKeys 744; holotype and one paratype, sexes not stated.
3. Troglonectes canlinensis, "Eyes reduced, eye diameter 7.5–11.6% of the lateral head length.", Animals 13(10) 1712; only the state is logged.
4. Sinocyclocheilus guiyang, absent in 5, highly reduced and partly skin-covered in 2 (counts as printed, referents not stated), Zoosystematics and Evolution 100(2).
5. Triplophysa dafangensis, "Eyes degenerated; ...", ZooKeys 1281; companion species of d281's zhijinensis (d281 noted it as not filed, no record).
6. Lucifuga gibarensis (Bythitidae), "Eyes pigmented (...)", ZooKeys 946; holotype female, three male paratypes; d280 note had dropped it for the diameter list only.
7. Oreonectes qinae, "Eyes normal, ...", ZooKeys 1255; contrast record in a cave-loach genus; holotype and paratype sexes stated.
8. Protocobitis longibarba, "Eyeless.", ZooKeys 1228; holotype male, paratypes 3 females and 4 males.

Dropped:
- On main already: Triplophysa xiuwenensis, T. zhijinensis (d281/d282), Triplophysa ziyunensis and T. yaluwang (only in other desk notes via abstracts; XML returned front matter only, no Description).
- Arrived in pieces (tool could not return the sentence whole): Caecilia pulchraserrana (ZooKeys 884, "its eyes are not covered by bone and it has tentacles ...", 32 words, returned as two quotes twice), Sinocyclocheilus longicornus (ZooKeys 1141, 22-word eye sentence), Neolissochilus pnar (Vertebrate Zoology 73, long sentence), Triplophysa wulongensis (Diagnosis, long), Triplophysa zhijinensis sentence.
- Text not reached: Indotyphlops gyirongensis (ZooKeys 1292, PROVENANCE_REQUIRED, no search result carried a Pensoft URL), Amphisbaena elbakyanae (Vertebrate Zoology 71, XML ends before the Description), Balitora tiandengensis (ZooKeys 1267, XML has no Description), Paranemachilus (ZooKeys 1269) and Oreonectes (ZooKeys 1196) species (no fetchable URL in results), Sinocyclocheilus xingrenensis (abstract page only), Microcaecilia dermatophaga (PLoS ONE, rate limited).
- Eye sentence not a degeneration/state statement: Sinocyclocheilus panzhouensis (large eyes, sentence over the tool limit), S. sp. ZooKeys 1238 ("Eye large, rounded.", Beipan-Jiang species, a non-cave state; not filed as low value).
- Licence conflict: Phreatobius dracunculus (Papéis Avulsos de Zoologia 47: page says CC BY-NC 4.0 and footer badge CC BY 4.0).
- Not vertebrate: Ptomaphaginus troglodytes (beetle), Harmonicon (spider), Caridina (d282).
- Subterranean Biology Rhamdia papers (SB 46, 50): records of populations, no new species and no eye sentence.
- Blind snakes, amphisbaenians, golden moles, shrews, fossorial rodents, cave salamanders: searches returned Plazi, Zootaxa, Copeia, BHL, PMC or no open Pensoft page; nothing filed.

Retrieval note: Crossref list queries (query.title with prefix 10.3897) gave titles; searching the exact title then surfaced article_preview.php or download/xml URLs that WebFetch opened. Pensoft XML downloads of some papers stop before the Description.
