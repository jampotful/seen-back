# desk-d298: eye-state sentences in new species of fishes, caecilians and squamates outside the cave-cypriniform group, 4 records

Branch research/desk-d298 from origin/main. About 40 WebSearches and fetches, WebFetch only on URLs returned by search or Crossref list queries. `python3 -I tools/senses/check.py | grep 'd298\.'`: 4 records, 0 problems. Crossref read for all four DOIs (author order matches the pages; all CC BY 4.0, three vor and PLoS ONE content-version unspecified with the page-printed Creative Commons Attribution License sentence). Main docs/ and the desk-d26x to d297 and audit-3xx evidence files grepped by species and DOI: no repeats. No new trait.

Filed (docs/views/evidence/desk-d298.jsonl), eye_type, whole sentences:
1. Yirrkala nkust (Ophichthidae), "Eye small, covered by a transparent skin; center of eye anterior to mid-jaw …", ZooKeys 1220; holotype and three paratypes, sexes not reported; only the first clause logged; trailing figure reference cut and marked.
2. Microcaecilia dermatophaga (Siphonopidae), "Eyes not visible.", PLoS ONE 8(3) e57756; holotype-only description (mature male); the Introduction says the genus has small eyes covered with bone (genus-level, not logged).
3. Amphisbaena amethysta (Amphisbaenidae), "Eyes slightly visible.", ZooKeys 1213; holotype-only description (male); 9 paratypes of both sexes not described for the eye.
4. Toxicocalamus longhagen (Elapidae), "Eye small (diameter 1.6); pupil round.", Zoosystematics and Evolution 98(2); known from the single holotype (male); the diameter number is not logged.

Dropped:
- Eurycea rathbuni ocular histology (PeerJ 11840, "No lens was identified in any adult E. rathbuni."): already held by d280 (donated freshly dead captive stock), not refiled.
- Amphisbaena elbakyanae (VZ 71): eye clause sits inside a single 247-word sentence.
- Siagonodon exiguum (VZ 73): eye wording is clauses inside semicolon lists, no standalone sentence.
- Geophis lorancai (ZooKeys 610): eye sentence is a size ratio (measurement).
- Ichthyophis griseivermis (VZ 75): the text has no eye statement (orbital apertures in the skull atlas only).
- Gnathophis johnsoni (JMSE 13): eye moderately large, ratio form, not a degeneration statement; Bidenichthys okamotoi (JMSE 9) and Listrura elongata (ZSE 101): the publisher page could not be fetched (blocked or the preview id returned another article).
- Trichomycterus dali (Neotropical Ichthyology): "Eyes not visible externally (Fig. 3).", no authors, volume or licence sentence reachable; held out.
- Trachischium sp. (Herpetozoa 39): only an orbit/supralabial sentence.
- Calyptommatus frontalis, Dibamus species, Letheobia, other blind snakes, Caecieleotris, Typhleotris: Zootaxa or Copeia, not open.
- Barbodes klapanunggalensis and other cave cypriniforms: inside the d295 group.
- Searches for Ipnops, Bathypterois, Aphyonidae, Zoarcidae, Gonostomatidae, Cetomimidae, gymnotiforms, loricariids, cave salamanders (Speleomantes, Proteus, Typhlomolge) and Sci Rep/Animals/Diversity items returned only Zootaxa, Plazi, ResearchGate, BHL or repository copies.

Retrieval note: Crossref list queries (prefix 10.3897, query.title plain words; "OR" in the query string fails) gave titles; searching the exact title then surfaced article_preview.php or download/xml URLs that WebFetch opened. The Pensoft id in article_preview.php is not always the DOI suffix.
