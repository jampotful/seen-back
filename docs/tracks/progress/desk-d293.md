# desk-d293: eye counts and eye absence in Collembola (Entomobryidae), 7 records

Branch research/desk-d293 from origin/main. About 40 WebSearches (4 extended) plus fetches. `python3 -I tools/senses/check.py | grep 'd293\.'`: 7 records, 0 problems. Crossref read for the four DOIs (author order matches; all CC BY 4.0 vor; no issue numbers). Every fetched URL came from a WebSearch. Grep of main docs/ and of research/desk-* and audit-* branch docs by genus and DOI: no repeats. New trait: none (eyes_count; the unit is stated per record).

Filed (docs/views/evidence/desk-d293.jsonl), all Collembola, whole-sentence eye statements from Description sections:
1. Pseudosinella hartnerae, "With 5+5 eyes (ABCDH, with H only slightly smaller).", ZooKeys 1063; holotype female, paratypes mixed sexes (the paper's own counts do not reconcile).
2. Pseudosinella altamirensis, "With five eyes (ABDEF or ABCDF; ...)." with the variation kept, ZooKeys 989; paratype sexes not stated; per side or total not stated.
3. Coecobrya sirindhornae, "Eyes absent.", ZooKeys 824; type counts do not reconcile (stated in conditions).
4-7. Coecobrya whitteni, C. troglobia, C. ellisi, C. phitsanulokensis, "Eyes absent.", Subterranean Biology 41; holotype sexes and paratype sex counts from the Type material blocks.

Dropped:
- On main already: Acherontiella nezamdoosti, Schaefferia greensladeae, S. montenegrina, Geopselaphus bullonorum (desk-d281/d282); Asiophrida xanthospilota and Panorpa dubia (ommatidia counts, sweep files).
- Zorotypus komatsui (ZooKeys 1178): ocelli sentence is a clause chain, reached in pieces. Milnesium berladnicorum (ZooKeys 429): eye sentence too long to return whole, begins mid-sentence ("90% of fixed specimens had eyes"). Oroperipatus tiputini: no eye count. Cylindrogaster cavernicola, Astreptolabis: no count or state (and amber fossil). Eurycyde bamberi and other sea spiders (ZooKeys 530): ocular tubercle only, sentences truncated. Beronaphaenops paphlagonicus (ZooKeys 255): sentence returned as a fragment. Bellisotoma joycei: remark about non-type material, sentence truncated. Pseudosinella huetheri: redescription, holotype sex not visible.
- Campodeidae (ZooKeys 1239xx transylvanica, Kyrgyzstancampa sanare EJT 782, Sendra SB 23): no eye sentence returned. Nicoletiidae (SB 49 Alabama): description has no eye sentence. Protura (ZooKeys 604, 876): only figure labels.
- Mayfly, stonefly, caddisfly, Odonata, thrips, aphids, scale insects, lice, fleas, psocids, sawflies, parasitoid wasps, tardigrades, Archaeognatha: searches returned only Plazi, Zenodo, PMC, closed or non-open-access pages, or no usable eye sentence; nothing filed.
- PMC, ResearchGate and Plazi hits were not opened.

Retrieval note: the fetch tool summarises; "Eyes absent." lines were confirmed by asking for the paragraph around them (sirindhornae, ellisi, altamirensis).
