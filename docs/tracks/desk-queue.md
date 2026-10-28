# Desk queue and yield log

The research desk keeps its work queue here so it survives a recycled session. Every check-in reads it, launches the next item when fewer than 3 units run, and appends a yield line when a unit returns. Order: audits of returned units, then plant screening, then re-screens and rechecks, then oa reading units.

## Pacing (Max plan; nothing beyond it)
- Week runs from Sun 25 Oct 21:59 EDT (26 Oct 01:59 UTC) to Sun 1 Nov 21:59 EST (2 Nov 02:59 UTC), 169 hours because clocks fall back on 1 Nov.
- Even pace: target % used = hours since 26 Oct 01:59 UTC / 169 x 100 (about 0.6% an hour, 14% a day).
- Readings from CC: 26 Oct 03:57 UTC, 2% used at hour 2 (target 1.2%), so ahead of pace; tonight's Opus reorganizing is a one-off.
- Dial: 2 units until the next reading (ahead of pace), then up to 4 if behind or down to 1 if still ahead. Fallback check-in every 90 minutes; units wake the desk when they finish.
- Cost rules: screening and audits on Sonnet; the desk session on Sonnet except for judgment calls; no unit kind that settles fewer than about 5 cells per 100k tokens (recheck-2 settled 9 for 230k, so rechecks are folded into plant and re-screen units as extra cells instead of running alone).

## Running (as of 27 Oct 18:40 UTC)
- No desk unit is running. Codex rounds for issues 28, 29, 30 and 38 are all reviewed and merged through branches; the dispatcher ledger shows all four as reviewed.
- Raw plant queue: 559 entries (85 are prior-covered residue per Codex round 2). Remaining batches harvest-c13 to c21 (40 each), c22 (27), c23 (14).
- Papers Wanted holds 2,973 papers (1,797 needed) after the round 2 refresh.
- Desk units resumed plant screening on 27 Oct (OpenAlex returns a proxy 403 to agents, so their new steps are labelled web searches). Merged: desk-c7 (audit 86) and desk-c8 (audit 87). Running: desk-c9 (19 genera), desk-c11 (20), desk-c12 (26). `codex_queue.py` still lists these genera as left because it counts only records with explicit "harvest run N" provenance; do not send them to Codex.

## Next, in order
- audit any new Codex plant unit with a fresh Opus unit (audit 86 onward), merge what passes, registry-fill wanted lines (run/crossref/desk-wanted-62 onward), refresh Papers Wanted
- fixes-needed-a A3, A4 and B1; the cannot-tell lines (57 B, 7 A); triage-A ci script changes on research/codex-triage-a (merge only if a CI run proves them)
- oa-1 to oa-13 stay held until 29 October; more oa reading through own-key jobs if new free copies appear
- the Danum Valley table (10.30880/jsunr.2023.04.02.002, 165 records, entry 56 of oa-14) waits for CC's decision

## Yield (tokens as reported by the unit at return)
| unit | tokens | output | merged |
|---|---|---|---|
| recheck-1 | 80k | none (branch name taken; restarted as recheck-2) | - |
| recheck-2 | 230k | 9 search records, 2 wanted lines, 7 cells found on main | pending audit 75 |
| rescreen-1 | 261k | 18 search records, 16 wanted lines | pending audit 76 |
| oa-13 build | 168k | run 24 succeeded (159 of 370 have free copies); oa.yml fix on main | - |
| codex round 2 (issue 38, PR 40) | Codex allowance | 1,056 wanted lines with registry authors, progress notes, findings 1 to 8; no search records, no closed cells | merged 27 Oct; raw queue still 559 |

## Plant batches (15 genera each, ordered by Alachua County records)
1. Bidens Callicarpa Tillandsia Ardisia Liquidambar Parthenocissus Cnidoscolus Vitis Magnolia Pleopeltis Tradescantia Sabal Smilax Erythrina Ruellia (plant-screen-1, running)
2. Salvia Stachys Rhus Pontederia Phytolacca Sambucus Oxalis Phyla Toxicodendron Youngia Trifolium Broussonetia Passiflora Urena Campsis
3. Verbesina Triadica Quercus Saururus Cirsium Ilex Gaillardia Serenoa Acer Monarda Nekemias Taxodium Mitchella Euphorbia Eupatorium
4. Juniperus Albizia Ambrosia Diospyros Rubus Baccharis Morella Nephrolepis Medicago Aesculus Cephalanthus Bignonia Platanus Euonymus Calyptocarpus
5. Lorinseria Osmundastrum Nuttallanthus Melilotus Cercis Centrosema Erechtites Chamaecrista Celtis Rivina Sphagneticola Pteridium Lonicera Asplenium Ipomoea
6. Nandina Ligustrum Zanthoxylum Geranium Lepidium Melothria Commelina Lygodium Pilea Ludwigia Monotropa Mikania Phoradendron Triodanis Asclepias
7. Erigeron Colocasia Solanum Heterotheca Prunus Lamium Osmunda Sisyrinchium Melia Catharanthus Antigonon Ostrya Mirabilis Vicia Diodia
8. Nymphaea Polygonatum Cornus Portulaca Plantago Sassafras Raphanus Teucrium Eryngium Galium Tilia Rudbeckia Ceratophyllum Hibiscus Liriodendron
9. Eclipta Hedera Lantana Sonchus Juncus Conoclinium Hamamelis Apios Nothoscordum Clematis Carpinus Cocculus Sagittaria Richardia Veronica
10. Oenothera Tridax Momordica Pluchea Modiola Taraxacum Capsella Persicaria Leucaena Amorpha Carica Thelypteris Fagus Eleusine Stellaria
11. Typha Pueraria Thunbergia Morus Symphyotrichum Melinis Nyssa Potentilla Populus Amphicarpaea Lolium Agave Verbascum Calystegia Tipularia
12. Sideroxylon Ulmus Malvaviscus Carya Pyrus Zizia Ptelea Iris Ricinus Conopholis Tropaeolum Chasmanthium Paulownia Chenopodium Aquilegia
13. Helianthus Arundo Sorghum Dioscorea Vinca Lobelia Foeniculum Hypochaeris Sorghastrum Packera Cortaderia Nasturtium Tecoma Cosmos Achillea
14. Mahonia Apocynum Bromus Marchantia Vachellia Poa Parkinsonia Panicum Artemisia Polystichum Ailanthus Equisetum Cardamine Rumex Centaurea
15. Ratibida Fraxinus Adiantum Botrypus Parthenium Andropogon Cynodon Glechoma Senecio Ranunculus Datura Lunaria Juglans Castilleja Ficus
16. Lespedeza Salix Asparagus Coccoloba Cenchrus Olea Cerastium Hemerocallis Chromolaena Cyanthillium Hexastylis Hypoxis Carex Alliaria Prunella
17. Cichorium Daucus Chamaenerion Ficaria Urtica Larrea Tussilago Lotus Lythrum Pinus Phragmites Chelidonium Bellis Tanacetum Impatiens
18. Silene Convolvulus Linaria Onoclea Podophyllum Maianthemum Erodium Leucanthemum Rosa Dactylis Echium Sanguinaria Arisaema Eschscholzia Caltha
19. Claytonia Hypericum Digitalis Tsuga Lysimachia Sorbus Ajuga Viburnum Coronilla Robinia Anthriscus Ageratina Aegopodium Hesperis Pseudotsuga
20. Dipsacus Symplocarpus Fragaria Erythronium Anemone Carnegiea Saponaria Corylus Rhamnus Argentina Convallaria Filipendula Reynoutria Chimaphila Cypripedium
21. Epipactis Vaccinium Frangula Jacobaea Lactuca Rabelera Heracleum Matricaria Trillium Eriogonum Cytisus Aralia Berteroa Elaeagnus Geum
22. Calluna Cymbalaria Conium Crataegus Pilosella Celastrus Heteromeles Lapsana Primula Dactylorhiza Kalmia Tripleurospermum Gaultheria Berberis Abies
23. Fouquieria Epilobium Athyrium Dipterostemon Arctostaphylos Papaver Betula Thuja Linnaea Lindera Lupinus Picea Encelia Symphoricarpos Malva
24. Knautia Anaphalis Asimina Sherardia Matteuccia Mertensia Drosera Sedum Alnus Echinocereus Humulus Thlaspi Thalictrum Arbutus Anacamptis
25. Campanula Pastinaca Barbarea Carduus Tragopogon Nicotiana Mycelis Dryopteris Clintonia Dicentra Struthiopteris Centranthus Actaea Lathyrus Ornithogalum
26. Phlox Solidago Gleditsia Cakile Clinopodium Hylocomium Holodiscus Dasiphora Ampelopsis Phleum Ferocactus Spiraea Prosopis Galanthus Sarracenia
27. Hypopitys Angelica Echinocystis Silybum Origanum Spinulum Houstonia Dianthus Leonurus Buddleja Verbena Hepatica Medeola Viscum Helminthotheca
28. Ulex Scilla Diphasiastrum Xanthium Goodyera Lysichiton Calamagrostis Marrubium Lycopus Allium Orchis Diplacus Amelanchier Orthilia Viola
29. Anemonastrum Polypodium Arctium Galinsoga Anthyllis Opuntia Maclura Armeria Hesperoyucca Ericameria Rhododendron Yucca Arum Asarum Corydalis
30. Lycopodium Cylindropuntia Hordeum Hydrophyllum Draba Adenostoma Claytosmunda Larix Amauropelta Umbellularia Veratrum Malosma Symphytum Empetrum Holcus
31. Petasites Calypso Epigaea Agrimonia Oemleria Eutrochium Torilis Sequoia Briza Chelone Paris Comarum Daphne Microstegium Lilium
32. Sitobolium Pulmonaria Phalaris Schinus Melampyrum Scutellaria Anthoxanthum Betonica Comptonia Cocos Lobularia Valeriana Cynoglossum Parnassia Mercurialis
33. Ballota Dodonaea Heliotropium Ophrys Coptis Borago Amaranthus Osteospermum Ribes Fritillaria Hippophae Sanguisorba Campanulastrum Zantedeschia Shepherdia
34. Hieracium Castanea Sanicula Eriophyllum Chamaedaphne Pulsatilla Tiarella Menyanthes Corallorhiza Mimosa Tribulus Schizachyrium Pedicularis Tellima Echinochloa
35. Carpobrotus Bunias Helenium Uvularia Ipomopsis Alloberberis Pistacia Nuphar Epifagus Alisma Gymnadenia Marah Adelinia Chlorogalum Malus
36. Acacia Doellingeria Phacelia Sisymbrium Ruscus Bistorta Picris Calla Umbilicus Neottia Perilla Clethra Euthamia Mimulus Scrophularia
37. Taxus Jasione Wyethia Penstemon Gymnocarpium Platanthera Erythranthe Nepeta Poterium Circaea Pentagramma Succisa Diervilla Scorzoneroides Spartium
38. Echinocactus Hypnum Crithmum Chrysosplenium Abutilon Vincetoxicum Rhizophora Butomus Oplopanax Laportea Aruncus Hylocomiadelphus Micranthes Glebionis Pleurozium
39. Macrocystis Myosotis Silphium Polytrichum Setaria Trollius Phegopteris Pyrola Engelmannia Dryas Triteleia Pterospora Bouteloua Cucurbita Andromeda
40. Pimpinella Bryonia Echinacea Lunularia Conocephalum Fucus Atriplex Cyperus Dodecatheon Cistus Comandra Myrica Pentanema Cleomella Syringa
41. Rhinanthus Muscari Polygaloides Endotropis Parietaria Macaranga Phlomoides Erysimum Centaurium Agropyron Caladenia Scaevola Alopecurus Viscaria Elymus
42. Staphylea Hylotelephium Simmondsia Liatris Caragana Nereocystis Croton Scirpus Huperzia Reseda Coreopsis Polygonum Arctotheca Eurybia Honckenya
43. Isocoma Onopordum Cystopteris Sphaeralcea Anchusa Egregia Nemophila Heliopsis Galactites Calandrinia Adonis Dalea Nerium Epacris Polemonium
44. Physocarpus Dittrichia Sidalcea Cochemiea Antennaria Lagurus Genista Pulicaria Nonea Hylodesmum Pelecyphora Cota Calendula Cephalanthera Armoracia
45. Bellardia Eriophorum Desmanthus Sapindus Helleborus Dermatophyllum Himantoglossum Sesuvium Themeda Mentha Oncosiphon Stylophorum Cyclamen Delphinium

## Yield log, 28 October 2026 (units kept after audit; evidence / search / wanted)
- d12 (batch 13 start) 10 / 8 / 1, audit 102 clean. d13 8 / 2 / 0, audit 103 dropped 4 lines (chased DOI with no supporting search, two repeats of main).
- d14 (batch 14) 5 / 0 / 0, audit 104 dropped 1 line (hybrid synonym); 7 of 9 genera skipped because main already holds leads.
- d15 (batch 15 start) 1 / 2 / 4, audit 105 dropped 2 lines. d16 9 / 1 / 0, audit 108 clean. d17 0 / 2 / 1, audit 106 dropped 2 lines (Hexastylis is Asarum). d18 (re-screen of dropped leads) 8 / 0 / 0, audit 107 clean.
- Yield per unit has fallen: most open cells now carry a wanted lead on main, and a lead means no null. Batches 16 onward (from Cerastium on) and the leads themselves are the remaining work; prefer a unit that reads open-access text for held leads over a genus sweep.
- Lead-reading and sweep units, 28 October (kept after audit; evidence / search / wanted): d19 5 / 0 / 0 (audit 110 clean); d20 3 / 0 / 0 (audit 109 dropped 1); d21 2 / 0 / 0 (audit 111 dropped 1, a synonym); d22 3 / 0 / 0 (audit 113 dropped 1, cut twigs); d23 2 / 0 / 0 (audit 112 clean); d24 3 / 0 / 0 (audit 114 dropped 1, long quote); d25 4 / 5 / 5 (audit 115 dropped 1 null). Yield is 2 to 5 records per unit. Untried work: roughly 90 plant leads, the Erodium cicutarium shade trial (Dryad 10.5061/dryad.gd3qh), the Pyrus betulifolia ABA record needing a shorter quote, and batches 17 onward (Linaria, Onoclea, Podophyllum, Rosa, Dactylis, Echium and later).
- d26 2 / 0 / 0 (audit 116 clean); d27 3 / 5 / 0 (audit 117 dropped 1 search record, an unsupported chased DOI). Leads still unread: Jones and Newell 1946 (Dactylis pollen-shedding hours) and Xiong et al. 2013 (Podophyllum hexandrum).

## Codex lane (26 October 2026)
- Codex runs on the owner's separate ChatGPT allowance, so it takes the plant screening (batches harvest-c7 to c23, 668 genera, 40 a unit, released 26 Oct 04:15 UTC; the free harvest run found nothing to add) and the findings pass. The desk audits and merges; it screens no more plant batches itself.
- An issue is a work request, not a confirmed Codex launch. Follow [CODEX-DISPATCH.md](CODEX-DISPATCH.md): reconcile existing Codex tasks, submit through a verified authenticated interface only when unstarted, and record the returned task URL/ID in the issue. Until that receipt and status exist, execution is unknown; silence is not permission to retry. The chat still follows `docs/tracks/prompts/codex-round.md` and opens a PR titled "Codex round ..." or "Codex findings ...".
- Desk side at each check-in: open pull requests whose title starts with "Codex" (gh api repos/jampotful/seen-back/pulls); audit per desk-audit.md (plant units) or oa-audit.md; merge what passes via the branch (never click merge on the pull request), drop error records, then close the pull request with a comment; triage findings files.
- oa-1 to oa-13 are held until 29 October: Codex's earlier oa pull requests failed audit (50 to 94% errors); release them only after a plant round passes audit and the free oa job (oa-13) has returned copies.
