# desk-d300: eye states and counts in flatworms (triclads, polyclads, land planarians), 7 records

Branch research/desk-d300 from origin/main. About 55 WebSearches (2 extended) plus fetches; every fetched article URL came from a WebSearch first (one Pensoft XML, 39524, was refused until a search listed it). `python3 -I tools/senses/check.py | grep 'd300\.'`: 7 records, 0 problems. Crossref read by DOI for all seven (author order matches the pages except ZooKeys 470, where Crossref lists Leal-Zanchet first and the Pensoft XML lists de Souza first; page order used). All CC BY (3.0 for EJT 342, with the page-printed sentence and Crossref "unspecified"; 4.0 vor elsewhere). Repeat check after filing: grep of docs/ on origin/main and on every origin/research/desk-* and audit-* branch (other than d300) by species name and by DOI: no hits for any filed species or DOI. No new trait key (eye_type string, eyes_count).

Filed (docs/views/evidence/desk-d300.jsonl), all Platyhelminthes (class left empty, not printed):
1. Girardia multidiverticulata (Dugesiidae), eyeless, live specimens; holotype and 3 paratypes, ZooKeys 470.
2. Dugesia bifida (Dugesiidae), eyes_count 2; holotype and paratype section series, all 22 collected animals asexual, ZooKeys 425.
3. Pasipha ferrariaphila (Geoplanidae), monolobate eyes in an irregular row around the anterior tip; holotype only, ZooKeys 776 (later sentences on dorsal spread stated in conditions).
4. Stylochus marimarensis (Polycladida), cerebral eyes in two elongated clusters; holotype only, Zoosystematics and Evolution 100(4).
5. Stylochus erytheius, marginal eyes along the entire margin; holotype only plus separately listed additional material, same paper.
6. Emprosthopharynx hartei (Polycladida), 20-30 eyes per nuchal tentacle (per tentacle, not total); holotype and 7 paratypes, ZooKeys 1221.
7. Dendrocoelum obstinatum (Dendrocoelidae), lacking eyes, Movile Cave; holotype, 2 paratypes and an immature specimen, European Journal of Taxonomy 342.

Dropped:
- On main or another branch already: Erhaia dijiang (SB 56), Horatia ozimeci (SB 37), Iranobelgrandia persica (SB 58), Placobdelloides sirikanchanae (ZooKeys 882), Paladilhiopsis stellatus and P. arion (ZooKeys 1046), Vitropyrgus lillianae and Phreatodrobia bulla (SB 47).
- Sentence arrives in pieces (over the tool's ~125 characters): Piima ata (EJT 705, eye distribution sentence, two parts), Stylochoplana sisalensis (ZooKeys 1221, three parts), Obama apiguara and Paraba tata (EJT 705, passages returned as fragments).
- No eye sentence in the species descriptions: Zospeum simplex (ZooKeys 1071), three Carychium species (ZooKeys 675), Sinoxychilus melanoleucus (ZooKeys 870, only "ommatophores" in the etymology), East African slugs (ZooKeys 723), Ostracolethe penevi (ZooKeys 1249), Bythinella spp. (ZooKeys 481), Pleurobranchaea britannica (ZSE 100), Phreatomascogos and Balconorbis (SB 29), Onchidium paper (ZooKeys 892, XML lacks the descriptions).
- Not a species-level or too weak: Callochiton septemvalvis (ZooKeys 312, records paper, abridged description, no type material, the shell-eye sentence is a fragment); Caridina zhaoi (decapod, not this angle); Eupera troglobia (bivalve, paper says eye absence is not applicable); Diversity 13(5) 178 (review of groundwater planarians, review-sourced).
- Licence or access: Plazi, Zenodo, PMC, BHL, zobodat and uni-repository copies not used; Swiss cave flatworm (Revue suisse de Zoologie, no licence); Wiley Dugesia paper (not open).
- Not reached (no fetchable Pensoft URL in results): Zospeum vasconicum (Basque papers), Koreozospeum nodongense (PMC only), Dugesia Chinese species of Chen and Dong (Plazi only), Elysia and Ercolania sacoglossans, freshwater limpets (no hits), pteropods, nudibranch descriptions (results were Plazi, Zootaxa or blogs).

Retrieval note: WebFetch splits sentences longer than about 125 characters into quotes; sentences kept here arrived whole in two separate passes (Dugesia bifida 120 characters, Pasipha 118, Stylochus marimarensis 62, S. erytheius 43, Emprosthopharynx 69, Girardia 50, Dendrocoelum 62).
