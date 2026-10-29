# desk-d60 progress (family-targeted strategy)

Started 29 October 2026. Branch research/desk-d60. WebSearch used: about 98 of 100. Families were chosen from the family counts over docs/views/evidence/*.jsonl (Cupressaceae 2, Pinaceae 19, Cucurbitaceae 12, Solanaceae 25, Orchidaceae 25, Araceae 11, Zosteraceae 0, Marchantiaceae 2, Dipterocarpaceae 1, Araucariaceae 0) and the open plant queue. Every record is abstract-only (partial true); each quote was checked verbatim on the page that printed it, and each accepted name on a POWO page (WFO for the liverwort). Each unit was copied as printed.

## Families and species tried
- Pinaceae and Araucariaceae: Pseudotsuga menziesii, Pinus strobus, P. banksiana, P. pinaster, P. radiata, P. contorta, Picea abies, P. glauca, Tsuga canadensis, Araucaria angustifolia.
- Cupressaceae: Juniperus procera, J. communis, Thuja occidentalis, Thujopsis dolabrata, Sequoia sempervirens, Taxodium distichum.
- Orchidaceae: Eulophia bicallosa, Dactylorhiza majalis, Calopogon tuberosus, Ophrys sphegodes, Cypripedium cordigerum, C. guttatum, Orchis militaris, Dendrobium nobile, Gymnadenia conopsea (scent rhythm).
- Cucurbitaceae and Solanaceae: Cucumis anguria, Cucurbita moschata, C. pepo, Momordica charantia, Citrullus lanatus, Luffa cylindrica, Solanum nigrum, S. lycopersicum, Physalis peruviana, Capsicum annuum, Nicotiana spp.
- Ferns, bryophytes, aquatics: Ceratopteris richardii, Marchantia polymorpha, Lycopodium clavatum, Zostera marina, Vallisneria americana, Lemna minor.
- Araceae, Poaceae and others: Colocasia esculenta, Oryza sativa, Zea mays, Sorghum bicolor, Raphanus sativus, Dipterocarpus, Ochroma, Luehea, Swietenia, Cycas, Cicer arietinum, Kalanchoe blossfeldiana, Hylocereus and Selenicereus.

## Filed (19 records, docs/views/evidence/desk-d60.jsonl)
Ceratopteris richardii (spore light), Colocasia esculenta (shade nets), Pinus strobus (low light emergence), Eulophia bicallosa (colour trial with dark), Zostera marina (neutral-density shading), Marchantia polymorpha (spore germination needs light), Dipterocarpus retusus (paper names D. macrocarpus, a POWO synonym), Cucumis anguria (germination red/far-red), Araucaria angustifolia (shade cloth null), Juniperus procera (light, and smoke null as sense_chemical), Oryza sativa (red light germination), Picea abies (white light inhibits germination), Ochroma pyramidale and Luehea seemannii (grade g, simulated gap light regimes; Ochroma's POWO page shows an "Accepted by" section and no explicit status line), Pinus banksiana (red/far-red reversal), Calopogon tuberosus, Ophrys sphegodes, Cypripedium cordigerum (dark germination).

## Read, not filed
- No DOI printed: Cucurbita moschata flower opening 0330 to 0400 h (Turkish J Bot 31(5), Agbagwa et al.; whole sentence verified, held because the launch prompt asks for a printed DOI), Hoddinott and Scott 1996 on Pinus banksiana (no DOI on the page), Physalis peruviana (no light result), Luffa cylindrica (no authors).
- Sentence over 125 characters or no direction: Solanum nigrum (Bithell et al. 2002, 128 characters), Tsuga canadensis (Mohammed and Parker 1999), Thujopsis and Metasequoia (Trees 2022), Citrullus MeJA (Frontiers 2025), Pinus pinaster and radiata MeJA (Trees 2019), Cicer arietinum photoperiod, Dendrobium nobile (two papers), Cucumis sativus spider mite, Raphanus raphanistrum far-red (already on main, desk-d5).
- Name or authority fork: Tomato 'Beaufort' rootstock UV-B (a hybrid), Raphanus sativus (POWO lists var. sativus under R. raphanistrum), Hylocereus species (sunk into Selenicereus in POWO; four-species HortScience flower-opening sentence, author list incomplete), Cypripedium guttatum (no POWO species page surfaced).
- Missing authors or journal: Cycas HortScience 2025, Lemna minor Tehran, Vallisneria americana (Carter et al. 1996; the biomass sentence is 131 characters), Zostera marina seedlings (MEPS 223), Lycopodium clavatum (Whittier 2008, page has no abstract), bromeliad germination papers (no authors on the scielo pages).
- Not a living response or a thesis: Selenicereus setaceus (thesis), Taxodium and Sequoia (proceedings paper with no DOI).
- Blocked: pmc.ncbi.nlm.nih.gov (reCAPTCHA, several), pubmed (reCAPTCHA), cyberleninka (captcha), enauka and katalog.lib.cas.cz (Anubis), peeref (login), frontiersin.org redirect target (not fetchable). Several ezproxy, elogim and proxy-mirror results surfaced and were left alone.

No wanted lines written: the Gymnadenia conopsea scent-rhythm paper (10.1093/aob/mcx203) is already in wanted files from sweep-34, and no other unreadable lead carried a DOI copied from a result.

## Advice on yield
Orchid germination papers gave the best return: the abstracts report light against dark outcomes in one short sentence, the pages (Springer, MDPI, CUP, Reference Global, EJES) print authors and DOI, and most orchid species are not yet on main. Conifer germination and seedling-shade papers (Pinaceae, Cupressaceae, Araucariaceae) came second, mostly through Springer and Silva Fennica pages. Seagrass and liverwort or fern spore papers gave single records each but are worth one targeted search per species. Cucurbitaceae and Solanaceae crops gave little: their abstracts run long, concentrate on yield and stress, and the flower-opening papers often lack a DOI. Tropical rainforest tree and mangrove shade papers mostly sit on scielo or repository pages without authors or DOIs. Cactaceae are already dense on main and the climbing-cactus names are in flux under Selenicereus.

## Desk disposition after audit 150
Audit 150 found 1 error in 19 records (5.3%): line 2, Colocasia esculenta, author order wrong (Gondim first per DOAJ and the Redalyc PDF). The audit covered the whole unit, so the desk dropped that record and merged the other 18. Pinus banksiana and Picea abies could not be opened on POWO for the auditor; both names surfaced on POWO, WFO and GBIF result pages in a desk search and were kept.
