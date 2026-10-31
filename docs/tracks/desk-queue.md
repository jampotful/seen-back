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
- d101 2 / 0 / 1 (audit 191: 1 error dropped, Guettarda scabra; Lonicera wanted line dropped as already on main; 1 wanted line)
- d102 3 / 0 / 0 (audit 192: 1 error dropped, Zostera marina GA3 to refile from full text)
- d103 2 / 0 / 1 (audit 193: 4 errors dropped; 1 wanted line)
- d104 0 / 0 / 0 (audit 194: 3 errors dropped; nothing merged)
- d105 1 / 0 / 0 (audit 195: 1 error, missing DOI; DOI added from Crossref before merge)
- d106 0 / 0 / 0 (audit 196: 3 errors dropped; nothing merged)
- d107 0 / 0 / 0 (audit 197: 3 errors dropped; refile unit, nothing merged)
- d108 2 / 0 / 1 (audit 198: 4 errors dropped; refile unit; 1 wanted line)
- d109 2 / 0 / 0 (audit 199: 2 errors dropped)
- d110 3 / 0 / 0 (audit 200: 0 errors; refile unit under the 40-word rule; notes added to conditions before merge)
- d111 4 / 0 / 1 (audit 201: 1 error dropped, Parthenium shading to refile; 1 wanted line, Ageratina adenophora)
- d112 1 / 0 / 0 (audit 202: 0 errors; vein mostly covered on main; Gyrostemon, Brassica tournefortii and several Lamiaceae held out)
- d113 0 / 0 / 0 (WFO pages refused; six leads read and filed by d116)
- d114 2 / 0 / 0 (audit 203: 0 errors; Parthenium shading refile, 60/90% and 30% levels)
- d115 0 / 0 / 0 (WFO pages refused; Cyathea delgadii pair passed to d117)
- d116 5 / 0 / 0 (audit 204: 0 errors; volatile reception, Zea mays x3, Arabidopsis thaliana, Phaseolus lunatus; Solanum lycopersicum and Vicia faba held out)
- d117 2 / 0 / 0 (audit 205: 1 error corrected before merge, pigment sampling at 2 months; Cyathea delgadii light quality; Azolla filiculoides, Polypodium lepidopteris held out)
- d118 4 / 0 / 0 (audit 206: 0 errors; Ambrosia confertiflora light, Pinus koraiensis ABA, Heliotropium europaeum GA3, Maianthemum dilatatum GA3 null; Reynoutria, Solanum lycopersicum, Alyssum montanum held out)
- d119 5 / 0 / 0 (audit 207: 0 errors; plant diel, Cestrum nocturnum scent, Selenicereus undatus opening and odour onset, Cereus jamacaru, Pereskia aculeata; Cestrum petal-phase lead unfiled)
- d120 3 / 0 / 0 (audit 209: 0 errors; sense_touch, Aldrovanda vesiculosa, Drosera allantostigma, Mimosa pudica)
- d121 4 / 0 / 0 (audit 208: 0 errors; Cestrum nocturnum petal phases, Paeonia peregrina GA3, Pyrus pashia GA3 abstract-only, Primula florindae GA3; Alyssum montanum, Reynoutria and others held out)
- d122 2 / 0 / 0 (audit 210: 1 of 3 errors, Ghosh line dropped; held out: Drosera spatulata, Utricularia)
- d123 3 / 0 / 0 (audit 211: 0 errors; Pyrus pashia full text not reached; held out: Miconia chamissois, Solanum tabacifolium, Primula secundiflora, Salsola ferganica)
- d124 1 / 0 / 0 (audit 212: 1 of 2 errors, Nelumbo line dropped; held out: Arum, Symplocarpus, Sauromatum, Crocus, Tulipa for licence or access)
- d125 0 / 0 / 0 (audit 213: 6 of 6 errors, none merged; Veits already on main as sense_hearing; Brito is physics)
- d126 1 / 0 / 0 (audit 214: 1 of 2 errors, Rosa rugosa dropped; held out: Nelumbo thermal refile, Nymphaea colorata, Clerodendrum inerme, Nicotiana attenuata, Ipomoea)
- d127 2 / 0 / 0 (audit 215: 1 of 3 errors, Arabidopsis line dropped; held out: Oryza sativa, Solanum tuberosum for WFO, Brassica rapa, Solanum lycopersicum, Camellia, Gossypium)
- d128 3 / 0 / 0 (audit 216: 0 errors; held out: Oryza sativa Zhao 2018, wheat, Passiflora caerulea, Populus, Pinus, Cuscuta for access or licence)
- d129 0 / 0 / 0 (no WFO species page surfaced for Oryza sativa, Solanum tuberosum, Alyssum montanum, Reynoutria japonica, Rhodothamnus, Drosera spatulata)
- d130 4 / 0 / 0 (audit 217: 1 of 5 errors, Colobanthus quercetin line dropped; held out: Kobresia humilis for WFO, Salix polaris, Bennie night light, Montagnoli, Albert, Gommers)
- d131 2 / 0 / 0 (audit 218: 0 errors; held out: Gentianopsis paludosa for POWO/WFO, Nelumbo, Magnolia denudata, Magnolia ovata, Philodendron selloum, Adonis amurensis)
- d132 2 / 0 / 0 (audit 219: 1 of 3 errors, Orobanche cumana line dropped; held out: Triphysaria versicolor for POWO, Cuscuta racemosa, Rhinanthus, Phtheirospermum, Alectra)
- d133 1 / 0 / 0 (audit 220: 2 of 3 errors, ABA antheridia and IAA lines dropped; held out: Ceratopteris richardii auxin, Azolla filiculoides, Selaginella martensii, bryophytes for POWO)
- d134 0 / 0 / 0 (audit 221: 3 of 3 errors, none merged; Artemisia omitted the 2012 non-repeat, Pinus lines misread cause; held out: Picea abies and Fagus sylvatica for WFO, Brassica nigra synonym, Quercus robur licence)
- d135 2 / 0 / 0 (audit 222: 1 of 2 errors, a method sentence corrected before merge; held out: Gentianopsis paludosa, Triphysaria versicolor)
- d136 0 / 0 / 0 (no WFO species page surfaced on second attempt for Picea abies, Fagus sylvatica, Kobresia humilis, Solanum tuberosum, Alyssum montanum, Oryza sativa)
- d137 3 / 0 / 0 (audit 223: 2 of 3 errors, both omitted the authors' own explanation of a null and were corrected before merge; held out: Cistus salviifolius, Gyrostemon, Conostylis, Leucadendron, Motta 2024)
- d138 0 / 0 / 0 (audit 224: 1 of 1 error, Populus balsamifera population contrast under natural day length; held out: Betula papyrifera for WFO, Populus tremula, Picea glauca, Mimulus laciniatus)
- d139 0 / 0 / 0 (no audit; held out for a missing name authority: Drosera rotundifolia Ivesic 2022 for WFO, Loasaceae thigmonastic stamens for POWO, Utricularia gibba Westermeier 2017; Phaseolus Wiley licence, Berberis no licence, Mimulus preprint)
- d140 2 / 0 / 0 (audit 225: 1 of 2 error, fixable and corrected: Harris 2009 conditions; Paponov 2021 where; Arabidopsis thaliana sense_magnetic x2)
- d141 0 / 0 / 0 (audit 226: 3 wanted lines not merged; Appel and Cocroft already on main, Brito and Nunes are floral physics, not a plant response)
- d142 0 / 0 / 0 (audit 227: 1 of 1 error, Anolis sagrei acuity 1.21 repeats herps:174 on main; held out: Passer domesticus Ensminger 2014 for quote length)
- d143 13 / 0 / 0 (audit 228: 4 of 13 error, all fixable and corrected: Etroplus synonym renamed Pseudetroplus, Pipistrellus 120 degree limiting result, Tursiops one animal at 5 and 25 Hz, Caretta prior light; hearing, magnetic, electric, infrared, airflow)
- d144 8 / 0 / 0 (audit 229: 1 of 8 error, fixable and corrected: Panulirus argus size effect misread as unconfirmed; Aedes aegypti thermal x2, Merimna atrata infrared x2, Dicentrarchus labrax hearing, Bufo bufo magnetic x2)
- d145 4 / 0 / 0 (audit 230: 2 of 4 error, both fixable and corrected: Eigenmannia sp. electric x2 had mV/uV unit error and the DF record was a jamming avoidance threshold; Galleria mellonella hearing x2)
- d146 6 / 0 / 0 (audit 231: 1 of 6 error, fixable and corrected: Nomophila quote cut without marking; Cicadatra atra, Dryophytes chrysoscelis, Copiphora gorgonensis hearing; Pagurus bernhardus vibration x2)
- d147 9 / 0 / 0 (audit 232: 3 of 9 error, all fixable and corrected: Gymnotus omarorum value from another sentence, two electric-threshold quotes dropped (Figure 4); clownfish hearing x3, Monochamus alternatus vibration x2)
- d148 2 / 0 / 0 (audit 233: 0 of 2 error; Gadus morhua hearing, Rhodnius prolixus in-vitro channel thermal)
- d149 3 / 0 / 0 (audit 234: 0 of 3 error; Ophiomastix wendtii behaviour_vision x2, Euperipatoides rowelli acuity_cpd 0.11 computed, first Onychophora vision record)
- d150 13 / 0 / 0 (audit 235: 9 of 13 error, all fixable and corrected: Streptocephalus mackini opsin doubt misattributed from notostracans, Platynereis eye field empty; Triops longicaudatus and Streptocephalus mackini lambda_max_nm x12, Platynereis dumerilii behaviour_vision)
- d151 0 / 0 / 0 (audit 236: 6 of 6 error, no open licence found for the author-deposited Egri 2022 copy; Ephoron virgo lambda_max_nm x6 not merged; content faults also listed for a refile)
- d152 5 / 0 / 0 (audit 237: 3 of 5 error, all fixable and corrected: Ciona two-species Methods, phototaxis refiled at genus; Ciona eye_role x2, Lymnaea stagnalis eyes_count and behaviour_vision)
- d153 3 / 0 / 0 (audit 238: 1 of 3 error, fixable and corrected: acuity_cpd eye/note, best-case patch value with hyperopic defocus caveat)
- d154 8 / 0 / 0 (audit 239: 5 of 8 errors, all fixable and corrected: tested-frequency edges, DPOAE primary-frequency spans, 40 C heat-limit context)
- d155 10 / 0 / 0 (audit 240: 9 of 11 errors, 8 fixable and corrected, Gryllus airflow line dropped: humidity design, sample size, caste pairing, null delays)
- d156 7 / 0 / 0 (audit 241: 4 of 7 errors, all fixable and corrected: Chandel 2024 IR-only assay design, source area, mutant nulls, Anopheles 27 C ambient)
- d157 7 / 0 / 0 (audit 242: 5 of 7 errors, all fixable and corrected: vibration amplitude and airborne sound, volatile percentages, cultivars, residual-field control, contrary tomato and lettuce results)
- d158 7 / 0 / 0 (audit 243: 6 of 7 errors, all fixable and corrected: slow-ramp protocol, TT-neuron transient coding, honeybee non-differing structures, no test above 1000 Hz, baseline n)
- d159 10 / 0 / 0 (audit 244: 1 of 10 error, fixable and corrected: Amphiprion single-cone 400 nm is captive-fish co-expression)
- d160 12 / 0 / 0 (audit 245: 2 of 12 errors, fixable and corrected: common carp tested frequencies, stimulus-level limit on the 7 to 9 kHz null)
- d161 8 / 0 / 0 (audit 246: 2 of 8 errors, fixable and corrected: 10 uT bat roosting random for first three days, eel bearing relative to displacement direction)
- d162 8 / 0 / 0 (audit 247: 0 of 8 errors; uncounted fixes applied: evoked n unit, ABR threshold rule, authors umlaut)
- d163 8 / 0 / 0 (audit 248: 3 of 8 errors, all fixable and corrected: Pinus NSC not significant at every shade level, 3-year-old root biomass, soybean far-red height at normal PAR only)
- d164 11 / 0 / 0 (audit 249: 4 of 11 errors, all fixable and corrected: mayfly ERG intact-adult preparation, template-fit peaks, UV flicker intensity)
- d165 5 / 0 / 0 (audit 250: 0 of 5 errors; uncounted fixes applied; new trait key pupil_lens_ratio is an owner question)
- d166 8 / 0 / 0 (armadillo ABR, zebra finch magnetic, monk seal in-air hearing)
- d167 7 / 0 / 0 (Xiphophorus optomotor acuity, budgerigar target acuity, Ischnura elegans LWS opsins, Electrogena female cff)
- d168 7 / 0 / 0 (Xenopus cold response, Apteronotus contrast threshold, goldfish startle)
- d169 4 / 0 / 0 (Apium graveolens smoke/KAR1 germination, Epipremnum aureum hormone spray)
- d170 5 / 0 / 0 (Castiarina phototaxis, Rattus norvegicus red/NIR vision, Meriones visual streak)
- d171 8 / 0 / 0 (five odontocete AEP audiograms, Spodoptera and Periplaneta magnetic, Atta sexdens vibration)
- d172 5 / 0 / 0 (reed warbler magnetic x3, Egernia stokesii colour pilot and pattern null)
- d173 1 / 0 / 0 (Scaphoideus titanus leaf-to-leaf vibration duet)
- d174 2 / 0 / 0 (fat-tailed dunnart ABR, Ischnocnema parva ABR)
- d175 5 / 0 / 0 (Diplotaxis UV-B, Diplachne fusca germination dark and GA3, Lactuca sativa far-red)
- d176 6 / 0 / 0 (Calanus polarotaxis, Meganyctiphanes, Talitrus polarized light, Tripneustes, Strongylocentrotus intermedius x2)
- d177 2 / 0 / 0 (Neohelice granulata noise-exposure responses; 6 held for name checks and owner ruling)
- d178 6 / 0 / 0 (Drosophila larva thermal sensitivity, Nilaparvata lugens magnetic, Anopheles coluzzii heat with odour)
- d179 7 / 0 / 0 (noise-exposure re-files: Neocaridina davidi, Crassostrea virginica, Acartia tonsa; Lycoriella ingenua ERG and behaviour)
- d180 1 / 0 / 0 (Meriones unguiculatus ABR; four duplicate Nilaparvata lugens records dropped)
- d181 9 / 0 / 0 (Copiphora gorgonensis pinnae and startle, Betta splendens AEP, Hippoglossus hippoglossus opsins)
- d182 8 / 0 / 0 (bat SWS1 UV pigments, Sepia officinalis optomotor, turbot and sole electric thresholds)
- d183 4 / 0 / 0 (Carcharhinus plumbeus magnetic with electrosense confound, Apis mellifera motion acuity; three repeats of main dropped)
- d184 8 / 0 / 0 (doradid catfish hearing, Silurus glanis and Cyprinus carpio temperature effect; two penguin repeats dropped)
- d185 9 / 0 / 0 (spookfish eyes, Astyanax mexicanus non-visual light responses, Rattus norvegicus airflow turning)
- d186 7 / 0 / 0 (Xenopus laevis tadpole magnetic response, mole-rat burrow orientation, Salamandra salamandra larval vision)

## Codex lane (26 October 2026)
- Codex runs on the owner's separate ChatGPT allowance, so it takes the plant screening (batches harvest-c7 to c23, 668 genera, 40 a unit, released 26 Oct 04:15 UTC; the free harvest run found nothing to add) and the findings pass. The desk audits and merges; it screens no more plant batches itself.
- An issue is a work request, not a confirmed Codex launch. Follow [CODEX-DISPATCH.md](CODEX-DISPATCH.md): reconcile existing Codex tasks, submit through a verified authenticated interface only when unstarted, and record the returned task URL/ID in the issue. Until that receipt and status exist, execution is unknown; silence is not permission to retry. The chat still follows `docs/tracks/prompts/codex-round.md` and opens a PR titled "Codex round ..." or "Codex findings ...".
- Desk side at each check-in: open pull requests whose title starts with "Codex" (gh api repos/jampotful/seen-back/pulls); audit per desk-audit.md (plant units) or oa-audit.md; merge what passes via the branch (never click merge on the pull request), drop error records, then close the pull request with a comment; triage findings files.
- oa-1 to oa-13 are held until 29 October: Codex's earlier oa pull requests failed audit (50 to 94% errors); release them only after a plant round passes audit and the free oa job (oa-13) has returned copies.
