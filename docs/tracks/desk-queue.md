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
- d28 0 / 4 / 2 (audit 118 dropped 4 of 8 records: a missed harvest query list, a missed Potentilla anserina shading trial, two long Kondo quotes); d29 4 / 36 / 3 (audit 119 dropped 4 searches, all missed measurements); d31 5 / 0 / 1 (audit 120 clean: Argentina anserina, Erodium cicutarium, Passiflora incarnata, Erechtites valerianifolius, Carica papaya). Lead-reading of wanted-list leads yields more than genus sweeps now.
- d30 3 / 32 / 4 (audit 121 clean; 19 of 22 genera in batches 22 and 23; Fouquieria and the Bowers 2005 and Lindera 1999 leads still unread).
- d32 4 / 0 / 0 (audit 122 dropped 1: Platanus orientalis quote was a Background statement). Kept: Pteridium aquilinum jasmonic acid, Poa pratensis night light, Sarcopoterium spinosum and Stachys cretica karrikinolide. Not filed: Epacris tasmanica, Melilotus suaveolens and Scilla paui (every usable sentence over 125 characters), Onopordum caricum (POWO unconfirmed), Toxicodendron vernicifluum (fetch refused).
- d34 1 / 0 / 0 (audit 123 dropped 1: Apocynum venetum repeated desk-c11; Apocynum pictum kept). Lead reading of remaining wanted leads is largely blocked (PMC, Wiley, Springer, BioOne refuse fetches); Lonicera insularis needs a POWO check.
- d33 7 / 48 / 17 (audit 124 dropped 5 search records; 25 genera of batches 24 and 25; Campanula not searched; Mycelis, Matteuccia and Struthiopteris are POWO synonyms; Dicentra spectabilis is Lamprocapnos).
- d35 4 / 18 / 4 (audit 125 dropped 6 search records, all missed measurements found by title-only screening; 24 of 30 genera of batches 26 and 27). Six leads are listed in its disposition note for a lead-reading unit.
- d36 3 / 36 / 5 (audit 126: no missed measurement; 5 search records flagged only for an omitted zero-hit citation-step DOI, ruled cosmetic, merged whole). Batch 29 not reached: Galinsoga, Anthyllis, Polypodium, Maclura, Armeria, Hesperoyucca, Ericameria, Yucca, Arum, Asarum, Corydalis.
- d37 2 / 0 / 0 (audit 127 clean: Sarracenia purpurea germination in darkness, Ampelopsis glandulosa var. brevipedunculata light levels). Gleditsia, Hylocomium and Dasiphora leads have only sentences over 125 characters.
- d38 7 / 55 / 9 (audit 128 failed: 3 search lines and 1 evidence line dropped; Larix olgensis was a synonym). Closed cells: Galinsoga light, Armeria GA3/KNO3, Yucca volatiles, Ericameria light, Larix MeJA, Cylindropuntia GA3.
- d39 5 / 0 / 2 (audit 129 clean: Petasites pyrenaicus chemical, Lilium longiflorum photoperiod, Schinus molle and S. terebinthifolia light, Lobularia maritima KNO3 priming). Most of batches 31 and 32 left unscreened; re-queued to d41.
- d40 6 / 25 / 12 (audit 130 failed: 6 search and 2 evidence lines dropped; part-sentence quotes, missed GA3/KNO3/photoperiod results). Gibberellin cells closed for Heliotropium, Amaranthus, Coptis, Hippophae, Fritillaria, Zantedeschia, Sanguisorba; Dodonaea light.
- d41 3 / 4 / 6 (audit 131 failed: 18 of 22 search records dropped, mostly `chased` naming the web DOI for harvest genera; the dropped genera are re-queued to d43). Closed: Parnassia light, Comptonia GA3, Eutrochium light.
- d42 4 / 30 / 8 (audit 132 failed: 5 search lines and 1 evidence line dropped). Closed: Campanulastrum light, Chamaedaphne GA3, Mimosa light, Schizachyrium KNO3.
- d43 2 / 15 / 9 (audit 133 failed: 2 search and 1 evidence line dropped). Closed: Mercurialis annua MeJA, Daphne mucronata GA3.
- d44 5 / 14 / 7 (audit 134 failed: 2 search and 1 evidence line dropped). Closed: Tribulus diel, Carpobrotus light, Helenium light, Pistacia khinjuk GA3, Alisma diel.
- d45 1 / 18 / 3 (audit 135: 0 of 18 search errors, 1 evidence line dropped). Closed: Nuphar variegata GA3. Hieracium chemical re-queued at species level.
- d46 3 / 2 / 3 (audit 136: 1 evidence line dropped; skipped genera of batches 36 to 45 verified as covered on main). Closed: Hieracium terraccianoi and Pilosella hoppeana subsp. sicula GA3, Succisa diel.
- d47 4 / 0 / 0 (lead reading of 67 wanted leads; audit 137 clean: Drosera rotundifolia light, Lactuca serriola diel, Tiarella polyphylla GA3, Borago officinalis light). About 40 leads had no qualifying sentence; about 12 unreadable.
- d48 2 / 0 / 1 (recheck of 49 early nulls under the widened readings; audit 138 clean: Thunbergia grandiflora shade, Lespedeza cuneata ABA/GA at grade g). 47 early nulls unchanged.
- 29 Oct 03:30 UTC: the desk sat idle from 16:00 UTC 28 Oct while waiting on PR 42 and checking issue 25; the live quiet alert is issue 43. Hold mode ended. Lead-reading unit d49 launched under the 125-character rule in force (records within 125 characters are valid under the 40-word rule too).
- d49 9 / 0 / 0 (lead reading; audit 139 clean: Panicum capillare, Minthostachys mollis, Lathyrus aphaca and Foeniculum vulgare light; Minthostachys mollis GA3; diel for Hepatica nobilis, Arabis procurrens, Iberis sempervirens, Melissa officinalis). Eranthis hyemalis diel and Rhus chinensis unfiled.
- d50 7 / 0 / 0 (lead reading; audit 140 clean: Eranthis hyemalis diel, Bidens pilosa and B. subalternans light, Frangula alnus light, Potentilla indica shade, Zanthoxylum fagara and Rumex confertus chemical). Rhus chinensis unfiled.
- d51 10 / 0 / 0 (lead reading; audit 141 clean: Capsella bursa-pastoris chemical; light for Broussonetia papyrifera, Platanus orientalis, Liquidambar orientalis, Alnus incana (g), Smilax brasiliensis; diel for Salvia arborescens, Passiflora foetida, Aconitum lycoctonum, A. carmichaelii).
- d52 13 / 0 / 0 (lead reading; audit 142 clean: Tecoma stans, Micromeles alnifolia, five Cerrado grasses (g), Coreopsis grandiflora and C. lanceolata (g), Antirrhinum majus, Apocynum venetum x2, Cypripedium subtropicum).
- d53 7 / 0 / 0 (lead reading; audit 143 dropped 1: Elodea naias dose unit mis-copied. Kept: Solanum tuberosum chemical, Oenothera biennis and Lotus pedunculatus night light, Dicksonia sellowiana, Pleopeltis pleopeltifolia light and chemical, Spirodela polyrhiza). Bryum argenteum, Dolichomitriopsis diversiformis, Cheilanthes concolor and Blechnum brasiliense held for name checks (d54).
- d54 7 / 0 / 0 (held name checks plus lead reading; audit 144 clean; Blechnum brasiliense held out pending a POWO check. Kept: Bryum argenteum, Cyathea delgadii (g), Geranium carolinianum, Taraxacum coreanum, Euphorbia esula, Ipomoea lacunosa, Erechtites hieraciifolius). Dolichomitriopsis diversiformis and Doryopteris concolor unfiled.
- d55 7 / 0 / 0 (lead reading; audit 145 dropped 2: Pinus sylvestris MeJA part-sentence quote, Rhizophora mangle no direction. Kept: Lemna minor and Spirodela polyrhiza (g), Avicennia germinans, Elodea naias, Cassia fistula diel, Euphorbia heterophylla, Bidens gardneri). Azolla pinnata and Crotalaria sericea unfiled.
- d56 10 / 0 / 0 (name-fork retries plus lead reading; audit 146 clean: Azolla pinnata, Dolichomitriopsis diversiformis, Hemionitis concolor, Handroanthus impetiginosus, Cereus jamacaru x2, Jacobaea maritima, Suaeda aralocaspica, Picea abies, Digitaria insularis). Blechnum brasiliense and Crotalaria sericea unfiled (authorities conflict).
- d57 9 / 0 / 0 (lead reading; audit 147 clean: Cirsium vulgare, Vicia villosa, Aesculus hippocastanum chemical; Conium maculatum, Synedrella nodiflora, Hesperis matronalis, Tripleurospermum inodorum, Potentilla recta, Oenothera biennis light).
- d58 3 / 0 / 0 (audit 148 clean; Pontederia thesis record held out, not peer-reviewed)
- d59 3 / 0 / 0 (audit 149 clean)
- d60 18 / 0 / 0 (audit 150: 1 of 19 dropped, Colocasia author order)
- d61 16 / 0 / 0 (audit 151: 2 of 18 dropped, volume error and a repeat of d54)
- d62 11 / 0 / 0 (audit 152: 2 of 13 dropped, a missing volume and a paraphrased title)
- d63 21 / 0 / 0 (audit 154 clean; 2 dropped on unconfirmed issue and a mis-cited WFO id; 3 wanted lines)
- d64 15 / 0 / 0 (audit 153 clean; 1 dropped for method wording the abstract does not support)
- d65 4 / 0 / 0 (audit 155 clean; 2 pooled Aristida records dropped, value omitted the dark-only condition)
- d66 11 / 0 / 1 (audit 156: 1 error, 1 dropped for an omitted exception; 1 of 5 wanted lines merged)
- d67 2 / 0 / 3 (audit 157: 1 error dropped, a field light gradient; 3 wanted lines merged, Eucalyptus year set to 2018)
- d68 5 / 0 / 5 (audit 158 clean; smoke, karrikin, GA3 and light/dark germination of named fire-prone species; 2 taxa held out for unconfirmed names)
- d69 3 / 0 / 2 (audit 159 clean; alpine and arctic named species, Galax urceolata twice from one paper and Poa alpina; 2 wanted lines merged)
- d70 2 / 0 / 0 (audit 160 clean; Marginatocereus marginatus anthesis and Basella alba red/far-red germination; no wanted lines)
- d71 4 / 0 / 0 (audit 161 clean; SciELO-indexed Latin American native species: Campomanesia aurea, Copaifera oblongifolia, Grona barbata, Paubrasilia echinata; no wanted lines)
- d72 1 / 0 / 0 (audit 162: 1 error dropped, Hosta yingeri omitted the later flowering result; Aster hayatae photoperiod merged; no wanted lines)
- d73 1 / 0 / 0 (audit 163: 2 errors dropped, Pimelea ciliata omitted the printed issue and Acacia pycnantha cited a synonym's WFO id; Trachyandra divaricata red-light germination merged; no wanted lines)
- d74 3 / 0 / 1 (audit 164: 2 errors dropped, Thlaspi arvense left out the GA3-alone result and Centaurium erythraea overstated an ABA reversal; Thlaspi germination, Avena fatua ethephon and Centaurium light merged; 1 wanted line, Balanites aegyptiaca GA3)
- d75 4 / 0 / 0 (audit 165: 0 errors; Richardia scabra ethephon or hormone germination, Stachys floridana photoperiod, Hydrilla verticillata photoperiod tubers, Dipsacus fullonum GA/ABA germination; no wanted lines)
- d76 4 / 0 / 1 (audit 166: 0 errors; Rhododendron catawbiense germination light, Amaranthus pumilus gibberellin germination in two traits, Cycas revoluta germination merged; 1 wanted line, Echinacea purpurea, authors left empty)
- d77 2 / 0 / 0 (audit 167: 0 errors; Lagerstroemia speciosa flower opening and Spathodea campanulata shade versus sun merged; no wanted lines)
- d78 5 / 0 / 1 (audit 168: 0 errors; Enhalus acoroides shading, Stratiotes aloides PAR, Rumex palustris ethylene and GA3, Salicornia fruticosa darkness germination, Sarracenia alata gibberellin germination merged; 1 wanted line, Hydrocharis morsus-ranae shading, authors empty)
- d79 2 / 0 / 0 (audit 169: 0 errors; Polymnia canadensis light and Artemisia tridentata volatile signalling merged; no wanted lines)
- d80 6 / 0 / 0 (audit 170: 0 errors; Anethum graveolens light and photoperiod, Scolymus hispanicus germination light, Centaurea nigra aphid headspace, Fraxinus mandshurica beetle and MeJA volatiles, Atropa acuminata herbivore-induced alkaloids merged; Atropa flagged for the owner as a tissue assay; no wanted lines)
- d81 8 / 0 / 0 (audit 171: 0 errors; eight Flora Mediterranea germination-report light/dark records merged: Lythrum hyssopifolia, Lythrum borysthenicum, Myosotis sicula, Antinoria insularis, Dianthus graminifolius, Senecio leucanthemifolius, Silene nefelites, Dianthus borbonicus; where field of two corrected to iris.unipa.it; no wanted lines)
- d82 4 / 0 / 0 (audit 172: 3 errors dropped, Asynthema gracile omitted a significant smoke-water result and both Minthostachys mollis lines repeated desk-d49; Glaucium flavum, Sideritis chamaedryfolia, Nicotiana linearis smoke and KAR1, Gentiana boissieri merged; no wanted lines)
- d83 5 / 0 / 0 (audit 173: 0 errors; Heliocarpus appendiculatus light-quality null, Crescentia alata light, Vachellia tortilis light-exclusion null, Handroanthus chrysanthus shade, Ochradenus baccatus GA3 merged; journal name of one and conditions of another corrected; no wanted lines)
- d84 3 / 0 / 0 (audit 174: 1 error dropped, Thamniopsis incurva omitted the full-text light 97% and dark 6% result and carried a wrong partial flag; Acrostichum danaeifolium UV-B, Adiantum flabellulatum low light gene expression, Werauhia gladioliflora night flower opening merged; no wanted lines)
- d85 3 / 0 / 0 (audit 175: 0 errors; Eragrostis lehmanniana red light germination, Lolium arundinaceum photoperiod germination, Cenchrus ciliaris KNO3 null merged; no wanted lines)
- d86 4 / 0 / 0 (audit 176: 2 errors dropped, Tetraena coccinea filed under a POWO/WFO synonym and Leucostele pasacana flower opening filed abstract-only with the full text open; Turbinicarpus alonsoi GA3 and Astrophytum asterias LED merged; no wanted lines)
- d87 6 / 0 / 0 (audit 177: 3 errors dropped, Prunus armeniaca Salak omitted significant full-text reductions and both Ferula records omitted the GA-chilling results; Liquidambar orientalis GA3/KAR1, Asphodelus ramosus darkness, Suaeda heterophylla photoperiod merged; no wanted lines)
- d88 6 / 0 / 0 (audit 178: 3 errors dropped, both Laggera light records misstated or omitted the 1.53-day red-light delay and Laggera alata smoke/KNO3 omitted the null KNO3-alone result and interactions; Impatiens walleriana, Mitragyna rubrostipulata, Nauclea latifolia light dependence merged; no wanted lines)
- d89 1 / 0 / 0 (audit 179: 1 error dropped, Aristotelia chilensis GA3/BAP/fluridone omitted the later fluridone onset and the control's equal onset; nothing merged; no wanted lines)
- d90 6 / 0 / 0 (audit 180: 4 errors dropped, Astilboides tabularis light and chemical records omitted full-text speed and KNO3 results, Catolobus pendulus uniformity direction reversed, Hydrangea petiolaris GA3/kinetin omitted kinetin, KNO3 and KCl reductions; Hydrangea petiolaris light and Kadsura coccinea GA3 merged; no wanted lines)
- d91 4 / 0 / 0 (audit 181: 2 errors dropped, Maesa japonica misstated the abstract's dose series as unread and Androsace septentrionalis called a non-significant mean germination time shorter; Euphorbia jolkinii and Pinus pumila GA3 merged; no wanted lines)
- d92 3 / 0 / 3 (audit 182: 1 error dropped, Arabis alpina scent diel null omitted the composition test and the authors' no-rhythm conclusion; Gentiana leucomelaena flower opening and light merged; 3 wanted lines merged)
- d93 7 / 0 / 0 (audit 183: 2 errors dropped, Ilex embelioides GA3 headline held for one dose of six and Barleria prionitis omitted the 100% at 300 days; Ophiorrhiza caudata held out as an unconfirmed accepted name; Salacia fruticosa, Andrographis paniculata, Rhinacanthus polonnaruwensis, Baccaurea courtallensis merged; no wanted lines)
- d94 7 / 0 / 1 (audit 184: 2 errors dropped, Agarista buxifolia GA3 omitted the five-species smoke null and Brighamia rockii light omitted the green-light promotion; Gardenia remyi held out as an unconfirmed name; Erica reunionensis light/GA3/smoke and Agarista buxifolia light merged; 1 wanted line merged)
- d95 6 / 0 / 1 (audit 185: 3 errors dropped, Tulipa iliensis omitted the cold-stratification test, Amorphophallus muelleri omitted the flowering and bulbil abortion results and Spiranthes ochroleuca omitted the significant 16/8 h root length result; Muscari comosum, Eranthis hyemalis, Lapiedra martinezii merged; 1 wanted line merged)
- d96 5 / 0 / 3 (audit 186: 4 errors dropped, Citrullus colocynthis, Linum usitatissimum, Satureja montana and Chenopodium quinoa omitted significant or contrary results, and the Linum quote was half a sentence; Ocimum basilicum light merged; 3 wanted lines merged)
- d97 5 / 0 / 0 (audit 187: 1 error dropped, Striga lutea; Viscum coloratum cited under the accepted WFO id)
- d98 3 / 0 / 1 (audit 188: 3 errors dropped, Rheum alexandrae held out unconfirmed; 1 wanted line)
- d99 2 / 0 / 3 (audit 189: 3 errors dropped or held, Phaius tankervilleae held out on POWO/WFO disagreement; 3 wanted lines)
- d100 4 / 0 / 0 (audit 190: 0 errors)

## Codex lane (26 October 2026)
- Codex runs on the owner's separate ChatGPT allowance, so it takes the plant screening (batches harvest-c7 to c23, 668 genera, 40 a unit, released 26 Oct 04:15 UTC; the free harvest run found nothing to add) and the findings pass. The desk audits and merges; it screens no more plant batches itself.
- An issue is a work request, not a confirmed Codex launch. Follow [CODEX-DISPATCH.md](CODEX-DISPATCH.md): reconcile existing Codex tasks, submit through a verified authenticated interface only when unstarted, and record the returned task URL/ID in the issue. Until that receipt and status exist, execution is unknown; silence is not permission to retry. The chat still follows `docs/tracks/prompts/codex-round.md` and opens a PR titled "Codex round ..." or "Codex findings ...".
- Desk side at each check-in: open pull requests whose title starts with "Codex" (gh api repos/jampotful/seen-back/pulls); audit per desk-audit.md (plant units) or oa-audit.md; merge what passes via the branch (never click merge on the pull request), drop error records, then close the pull request with a comment; triage findings files.
- oa-1 to oa-13 are held until 29 October: Codex's earlier oa pull requests failed audit (50 to 94% errors); release them only after a plant round passes audit and the free oa job (oa-13) has returned copies.
