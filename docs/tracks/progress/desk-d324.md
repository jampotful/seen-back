# desk-d324: vertebrate ocular anatomy and visual behaviour (amphibians, reptiles, birds, fishes)

Result: 0 evidence records filed (docs/views/evidence/desk-d324.jsonl not created). About 40 WebSearch calls and 25 page fetches.

## Why nothing was filed

Every open-access paper found in the angle was already on main (species or DOI present somewhere under docs/), was a review, or failed the licence or quote rules. The angle looks mined out for papers that search can reach.

## Candidates checked and set aside

On main by DOI or species: Campbell and Loew 2024 anole oil droplets (famrs.2024.1410763); Biagioni et al. 2016 hatchetfishes (fevo.2016.00025); Fritsch et al. 2017 eyeshine (s12983-017-0198-9); Wan/Schott frog opsins; Mitkus et al. 2016 storm petrel and fulmar (jeb.140905); Tashiro et al. 2021 Bothrops and Crotalus (fnana.2021.770804); Hawk Eyes I (pone.0012802); dendrobatid frogs (pone.0312578); Crocodylus porosus and C. johnstoni (jeb.135673); kakapo (pone.0022945); Ultra-rapid vision in birds (pone.0151099); black kite fovea (s41598-020-63039-y); kestrel and little owl (s12917-024-04371-7); reef fish eyes (1471-2148-11-338); whooping crane, Podarcis muralis, Tiliqua rugosa, Pituophis, Python regius, Puffinus pacificus and others.

Not on main but not filed:
- Pointer et al. 2005, Antarctic notothenioids (jeb.01647; Dissostichus mawsoni, Trematomus spp., Gymnodraco acuticeps absent from main) and Pointer et al. 2007, Scopelarchus analis (jeb.006064): both pages print only "(c) The Company of Biologists Limited" with no licence sentence, and Crossref carries no licence for jeb.01647. Held under the brief's "skip none" instruction; a desk ruling on "publisher's own free full text" would release them. Values read: notothenioid rods about 500 nm, MWS cones about 490 nm, SWS about 415 nm (426 nm in T. loennbergii); S. analis RH1A 486 nm and RH1B 479 nm (recombinant opsins, not MSP).
- Lisney et al. 2020, Melanotaenia australis eye morphology (jeb.223644): Crossref licence is the publisher user licence, content-version am. Fails.
- Tovar et al. 2021, Eurycea sosorum retina (peerj.11840): Crossref CC BY 4.0 "unspecified", but the page text read gave no CC sentence, and E. rathbuni from the same paper was held by desk-d280 and d298 (donated freshly dead captive stock). Not filed.
- Potkamp et al. 2026 cichlids (bio062674): behavioural dorsal-light sensitivity plus expression, laboratory-reared, informal Pundamilia names; no usable value.
- Karger BBE Apteronotus albifrons (10.1159/000438448): paywalled.
- nature.com pages (s41598-025-91987-w single cones in fishes; srep39395 Malacosteus niger; s41598-018-25599-y daytime eyeshine) returned client_error and were not read. Their species are absent from main (Malacosteus niger 0 hits), so a later unit could retry.
- Frontiers fmars.2022.797507 (Solea senegalensis opsin expression) has no usable value; fmars.2023.1225067 is a review.

## Tool notes

WebSearch with allowed_domains (journals.plos.org, peerj.com, biologists.com, frontiersin.org, nature.com) works and returns species-level papers; the unfiltered query returns mostly repository pages. Frontiers /full pages open; the /text path on public-pages-files-2025 gave PROVENANCE_REQUIRED once and was not retried. Crossref single-work lookups (api.crossref.org/works/<doi>) give licence and author order.
