# Desk queue and yield log

The research desk keeps its work queue here so it survives a recycled session. Every check-in reads it, launches the next item when fewer than 3 units run, and appends a yield line when a unit returns. Order: audits of returned units, then plant screening, then re-screens and rechecks, then oa reading units.

## Pacing (Max plan; nothing beyond it)
- Week runs from Sun 25 Oct 21:59 EDT (26 Oct 01:59 UTC) to Sun 1 Nov 21:59 EST (2 Nov 02:59 UTC), 169 hours because clocks fall back on 1 Nov.
- Even pace: target % used = hours since 26 Oct 01:59 UTC / 169 x 100 (about 0.6% an hour, 14% a day).
- Readings from CC: 26 Oct 03:57 UTC, 2% used at hour 2 (target 1.2%), so ahead of pace; tonight's Opus reorganizing is a one-off.
- Dial: 2 units until the next reading (ahead of pace), then up to 4 if behind or down to 1 if still ahead. Fallback check-in every 90 minutes; units wake the desk when they finish.
- Cost rules: screening and audits on Sonnet; the desk session on Sonnet except for judgment calls; no unit kind that settles fewer than about 5 cells per 100k tokens (recheck-2 settled 9 for 230k, so rechecks are folded into plant and re-screen units as extra cells instead of running alone).

## Running
- oa-13 (fetch of 370 wanted papers; oa job retry with apt-get update on its run branch)
- plant-screen-1 (plant batch 1)
- audits 75 and 76 (recheck-2, rescreen-1)

## Next, in order
- merge recheck-2 and rescreen-1 after audits 75 and 76
- plant batches 2 onward (below), one unit each
- oa reading units, once oa-13's free copies return
- release or rescreen of held plant-1 and replant-1 records under desk-screen.md point 10
- rescreen-2 (with any recheck cells folded in): Iris (no harvest entry), Scoparia (Crambidae review), Parnassius acuity_cpd and interommatidial_deg; audit 62's two Sphenomorphus cells
- carry the oa.yml apt-get update fix to main once it works
- triage of Codex findings (branches codex/findings-*) when they appear

## Yield (tokens as reported by the unit at return)
| unit | tokens | output | merged |
|---|---|---|---|
| recheck-1 | 80k | none (branch name taken; restarted as recheck-2) | - |
| recheck-2 | 230k | 9 search records, 2 wanted lines, 7 cells found on main | pending audit 75 |
| rescreen-1 | 261k | 18 search records, 16 wanted lines | pending audit 76 |
| oa-13 build | 168k | 370-entry batch; oa job failed (run 23) | - |

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

## Codex lane (26 October 2026)
- Codex runs on the owner's separate ChatGPT allowance, so it takes the plant screening (batches harvest-c7 to c23, 668 genera, 40 a unit, released 26 Oct 04:15 UTC; the free harvest run found nothing to add) and the findings pass. The desk audits and merges; it screens no more plant batches itself.
- A round starts when a Codex chat gets the line "Update to the latest main from GitHub, then follow docs/tracks/prompts/codex-round.md" (the owner sends it, or an issue mentioning @codex does if that works). Rounds open a pull request titled "Codex round ..." or "Codex findings ...".
- Desk side at each check-in: open pull requests whose title starts with "Codex" (gh api repos/jampotful/seen-back/pulls); audit per desk-audit.md (plant units) or oa-audit.md; merge what passes via the branch (never click merge on the pull request), drop error records, then close the pull request with a comment; triage findings files.
- oa-1 to oa-13 are held until 29 October: Codex's earlier oa pull requests failed audit (50 to 94% errors); release them only after a plant round passes audit and the free oa job (oa-13) has returned copies.
