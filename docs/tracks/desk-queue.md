# Desk queue and yield log

The research desk keeps its work queue here so it survives a recycled session. Every check-in reads it, launches the next item when fewer than 3 units run, and appends a yield line when a unit returns. Order: audits of returned units, then plant screening, then re-screens and rechecks, then oa reading units.

Before the next fresh evidence launch, the existing desk follows
[desk-launch.md](prompts/desk-launch.md) to record the actual launch time,
accepted-main base, supplied instruction versions and acknowledgment in the
unit's usual progress note. Inventory running units from the live session logs;
leave their pinned instructions and tools unchanged. The dated Running section
below is historical, not proof of current runtime state. Link final strict,
baseline-aware and scientific-preflight results and immutable audit commits on
return. This adds provenance to the existing workflow, not another dispatcher or
another research assignment. See the [adoption investigation](progress/desk-intake-adoption-2026-11-02.md)
for the unresolved d325/d326 launch evidence.

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
- d187 7 / 0 / 0 (Astyanax mexicanus cave-morph light/dark activity, Trachemys scripta elegans ABR, Halichoerus grypus underwater audiogram, Alytes obstetricans vibration)
- d188 7 / 0 / 0 (Nannospalax ehrenbergi burrow-orientation null, Branta canadensis and Molothrus ater light avoidance, Leptophobia aripa colour choice)
- d189 7 / 0 / 0 (Protaetia brevitarsis, Spodoptera frugiperda and Encarsia formosa colour choice)
- d190 7 / 0 / 0 (Acrocephalus scirpaceus magnetic alignment, Eptesicus fuscus ageing hearing null, Grammostola pulchra leg vibration)
- d191 8 / 0 / 0 (Megalopta genalis light-intensity nulls, larval Danio rerio UV avoidance)
- d192 9 / 0 / 0 (Asiophrida xanthospilota ERG, Exolontha castanea and Anoplophora glabripennis phototaxis, Endebius florensis, Octopus vulgaris visual choice; 1 repeat dropped)
- d193 7 / 0 / 0 (Eretmochelys imbricata and Chelonia mydas balloon colour choice, Procambarus clarkii and Cherax quadricarinatus, Arctocephalus forsteri audiogram, Siganus guttatus, Bactrocera dorsalis)
- d194 8 / 0 / 0 (Austruca lactea vibration exposure, Carcinus maenas touch null, Lycorma delicatula EAG null, Schizothorax kozlovi and Sebastiscus marmoratus colour choice, Canis lupus familiaris audiogram)
- d195 6 / 0 / 0 (Coloeus monedula colour discrimination, Astyanax mexicanus hearing and ERG null, Culex territans CO2 null)
- d196 1 / 0 / 0 (Tropilaelaps mercedesae thermal gradient choice)
- d197 6 / 0 / 0 (Portunus trituberculatus shelter colour, Bombus terrestris and Aphis gossypii EAG and Y-tube)
- d198 4 / 0 / 0 (Gallus gallus ABR audiogram, Callosobruchus maculatus thermal preference x2, Tripterygion delaisi fluorescence)
- d199 6 / 0 / 0 (Tetranychus urticae repellence and electrotarsal detection, Varroa destructor sensory pit and physical cues, Anoeconeossa bundoorensis grey choice)
- d200 6 / 0 / 0 (Diaphorina citri wavelength and polarization, Amblyomma americanum and Ixodes scapularis Peltier choice, Pogona vitticeps ELF-EMF)
- d201 1 / 0 / 0 (Aedes aegypti DEET EAG with and without heating)
- d202 1 / 0 / 0 (Kogia breviceps hearing, Houser 2022)
- d203 7 / 0 / 0 (Eucryptorrhynchus x4, Cacopsylla chinensis x2, Asiophrida polarization; one repeat dropped)
- d204 4 / 0 / 0 (Sebastes schlegelii hearing, Dendrobaena veneta CO2 x2, Anoplophora glabripennis EAG)
- d205 4 / 0 / 0 (Tiliqua adelaidensis scent, Echinotriton chinhaiensis larvae x3; 2 Dendrobaena repeats of d204 dropped)
- d206 3 / 0 / 0 (Euperipatoides rowelli acuity, Campylomormyrus tamandua, Serrasalmidae hearing; 2 held on name and licence)
- d207 5 / 0 / 0 (Chrysoperla carnea, Aspidoscelis inornata, Esox masquinongy x2, Myrmeleon bore; Milnesium held on name and licence)
- d208 3 / 0 / 0 (Pygocentrus nattereri colour learning x3; Scolia hirta and Megaphragma held)
- d209 2 / 0 / 0 (Gryllotalpa major ultrasound band, Abudefduf abdominalis hearing)
- d210 3 / 0 / 0 (Erinaceus europaeus hearing, Uranotaenia lowii hearing, Periophthalmus barbarus corneal reflex)
- d211 5 / 0 / 0 (Phoca vitulina vibrissa sensing x5; vibrissae-covered control row dropped)
- d212 3 / 0 / 0 (Hipposideros pratti Doppler shift compensation, Chrysochloris asiatica ossicle resonance, Lophiobagrus cyclurus hearing)
- d213 2 / 0 / 0 (Ophiomastix wendtii looming, Brevoortia tyrannus neuromast block; Doryteuthis hearing dropped as a repeat of main)
- d214 12 / 0 / 0 (Epidalea calamita x2, Eurycea lucifuga x2, Gyrinophilus porphyriticus, Fukomys darlingi, Heterocephalus glaber, Spalacopus cyanus, Fratercula arctica, Loxosceles laeta x3; octopus and Conomurex dropped as repeats)
- d215 7 / 0 / 0 (Kryptopterus vitreolus magnetic, Histia flabellicornis, Hypanus sabinus, Oreochromis niloticus, Neopsephotus bourkii, Melopsittacus undulatus, Fukomys mechowii; Lepomis gibbosus dropped as on main)
- d216 7 / 0 / 0 (Scylla paramamosain x2, Trabala vishnou, Ateles geoffroyi, Platydoras armatulus, Cyprinella venusta, Megalechis thoracata)
- d217 12 / 0 / 0 (Blattella germanica, Drosophila suzukii, Cyprinus carpio magnetic, Larimichthys crocea, Hyphantria cunea, Triatoma rubida x2, Cimex lectularius, Lobesia botrana, Dastarcus helophoroides, Eptesicus fuscus magnetic, Sclomina erinacea)
- d218 3 / 0 / 0 (Neophoca cinerea hearing, Astyanax mexicanus chemical, Anas platyrhynchos touch; Equus caballus hearing dropped as review-sourced)
- d219 4 / 0 / 0 (Lymantria xylina x2, Culex tarsalis, Culex quinquefasciatus; Odocoileus virginianus dropped as a repeat of main)
- d220 3 / 0 / 0 (Trichogramma japonicum, Orius maxidentex, Papilio polytes; Trialeurodes vaporariorum held out as unchecked)
- d221 11 / 0 / 0 (Serangium japonicum, Anomalops katoptron x3, Xenopus laevis, Melipona eburnea, Huia cavitympanum x2, Pieris rapae, Chrysomela populi x2)
- d222 3 / 0 / 0 (Stygoparnus comalensis, Podarcis lilfordi null, Pimephales promelas)
- d223 14 / 0 / 0 (Gekko subpalmatus, Diaprepes abbreviatus x2, Triatoma dimidiata, Diaphorina citri, Nesidiocoris tenuis, Phlebotomus perniciosus, Gnorimus nobilis x2, Anopheles gambiae x2, Chiloscyllium punctatum, Anguilla anguilla, Spheniscus humboldti)
- d224 9 / 0 / 0 (Frankliniella occidentalis x3, Danio rerio larval acuity, Xyleborus affinis, Xyleborus ferrugineus, Fopius arisanus, Aedes albopictus x2)
- d225 8 / 0 / 0 (Puffinus puffinus, Microtus ochrogaster, Odontotermes formosanus, Apis mellifera, Hippodamia variegata, Passer domesticus, Rana dalmatina, Culex pipiens)
- d226 8 / 0 / 0 (Trogonophis wiegmanni x2, Rhagoletis cerasi x2, Curculio elephas, Cerambyx welensii, Leptoglossus chilensis, Lucilia coeruleiviridis)
- d227 8 / 0 / 0 (Aromia bungii, Phthonoloba viridifasciata, Rhoptroceros cyatheae, Tomicus yunnanensis, Nyctereutes procyonoides, Glossina swynnertoni, Bufotes balearicus x2)
- d228 8 / 0 / 0 (Trypodendron lineatum, Ips acuminatus, Neolamprologus pulcher x2, Porichthys notatus, Aquatica ficta, Magallana gigas, Oryctes rhinoceros)
- d229 10 / 0 / 0 (Anguilla marmorata x5, Careproctus rhodomelas, Coregonus kiyi, Salvelinus namaycush, Myoxocephalus thompsonii, Emblemasoma auditrix)
- d230 3 / 0 / 0 (Macropus eugenii colour_vision, Oophaga pumilio, Phymaturus tenebrosus)
- d231 1 / 0 / 0 (Monolepta signata)
- d232 4 / 0 / 0 (Tyto alba, Falco tinnunculus, Tipula autumnalis, Rosalia batesi)
- d233 9 / 0 / 0 (Anoplophora chinensis, Bagrada hilaris x2, Coryphodema tristis, Xylotrechus quadripes, Archips strojny, Musca domestica, Bradysia odoriphaga, Leptinotarsa decemlineata)
- d234 3 / 0 / 0 (Pelophylax ridibundus, Rhinella marina, Staurois parvus)
- d235 5 / 0 / 0 (Metellina segmentata, Hydrophis major, Spodoptera frugiperda, Lycorma delicatula, Procambarus clarkii)
- d236 8 / 0 / 0 (Cyclopterus lumpus x2, Matsumurasca onukii x2, Deilephila elpenor, Macroglossum stellatarum, Cymodoce japonica x2)
- d237 4 / 0 / 0 (Poecilia parae x3, Gasterosteus aculeatus)
- d238 6 / 0 / 0 (Agalychnis callidryas, Xenopus laevis, Apis mellifera x2, Gryllus bimaculatus x2)
- d239 4 / 0 / 0 (Mecopoda elongata, Mormyrus rume, Dascyllus aruanus, Culex pipiens)
- d240 5 / 0 / 0 (Agriotes obscurus, Culex quinquefasciatus, Aedes aegypti, Thamnophis melanogaster x2; Cuon and Speothos held out)
- d241 9 / 0 / 0 (Alouatta caraya, Sylvia atricapilla x2, Sylvia borin, Erithacus rubecula, four bats absolute_sensitivity)
- d242 4 / 0 / 0 (Thysanoessa inermis x2, Leucorrhinia intacta, Libellula pulchella)
- d243 4 / 0 / 0 (Lethenteron camtschaticum, Orycteropus afer x2, Bolinichthys longipes)
- d244 3 / 0 / 0 (Ursus thibetanus x2, Siganus luridus)
- d245 4 / 0 / 0 (Cerdocyon thous, Micaelamys namaquensis x2, Apteryx mantelli)
- d246 5 / 0 / 0 (Acanthaster planci x3, Neogonodactylus oerstedii, Amphiura filiformis)
- d247 2 / 0 / 0 (Leptograpsus variegatus, Allobathynella bangokensis)
- d248 3 / 0 / 0 (Faxonius virilis x2, Triakis semifasciata)
- d249 1 / 1 / 0 (Gelasimus dampieri; Scyliorhinus canicula held out, repeat of d227 held by audit 317)
- d250 7 / 1 / 0 (Harpalus affinis, Pterostichus melanarius, Amara littoralis, Phyllostomus discolor, Danaus plexippus, Hediste diversicolor x2; Carcharodon carcharias held out)
- d251 6 / 0 / 0 (Dikerogammarus villosus, Argiope bruennichi, Carcharhinus melanopterus, Rattus norvegicus, Anoplotrupes stercorosus x2)
- d252 4 / 1 / 0 (Ciconia ciconia, Molothrus ater, Carcharhinus leucas, Pyrocoelia atripennis; Xenopus laevis feral held out)
- d253 9 / 0 / 0 (Pipistrellus nathusii, P. pygmaeus, Iberolacerta cyreni, Ephoron virgo, Pekania pennanti, Canis lupus, Alces alces, Urocitellus richardsonii, Cervus elaphus)
- d254 7 / 1 / 0 (Notomys alexis, Chelonia mydas, Carcharodon carcharias x2, Chaoborus flavicans, Darevskia praticola, Podarcis muralis; Phocoena phocoena held out)
- d255 6 / 1 / 0 (Gadus morhua, Sebastes schlegelii, Pseudopleuronectes yokohamae, Culex pipiens, Cryptomys pretoriae, Cydia pomonella; Calonectris borealis held out)
- d256 7 / 0 / 0 (Monochamus galloprovincialis x2, Anthonomus pomorum x2, Lasioglossum villosulum x2, Paracentrotus lividus)
- d257 6 / 0 / 0 (Ectatomma brunneum, Neoponera inversa, Frankliniella occidentalis, Chionoecetes opilio, Asproparthenis punctiventris x2)
- d258 7 / 1 / 0 (Bombus terrestris, Trissolcus basalis, Linepithema humile, Listronotus bonariensis, Salvator merianae, Parus major, Passer domesticus; Leptoglossus zonatus held out)
- d259 7 / 1 / 0 (Lasius niger, Oxycarenus hyalinipennis, Rivomarginella morrisoni, Odontothrips loti, Ctenarytaina eucalypti, C. bipartita, Anoeconeossa bundoorensis; Rivomarginella behaviour_vision held out)
- d260 6 / 0 / 0 (Sceloporus occidentalis, Ilyanassa obsoleta, Partamona helleri, Melipona bicolor, Bagrada hilaris, Cyanistes caeruleus)
- d261 7 / 0 / 0 (Apolygus lucorum, Pagiophloeus tsushimanus, Culex quinquefasciatus, Aedes albopictus, Phymaturus williamsi, Nezara viridula x2)
- d262 0 / 0 / 0 (no candidate passed; held leads in desk-d262.md; allowed-domain open-access vein looks exhausted, widened to biologists.com, Wiley OA, PNAS from d263)
- d263 8 / 0 / 0 (Stenocercus angel, cadlei, festae, ornatus, chota; Phyllodactylus gerrhopygus x2; Cnemaspis mysoriensis)
- d264 1 / 0 / 0 (Laudakia stellio)
- d265 0 / 0 / 0 (no candidate passed; held leads in desk-d265.md; Podarcis muralis acuity jeb.249422 not reachable by search)
- d266 0 / 0 / 0 (discovery-channel test: only single-DOI Crossref works; OpenAlex, DOAJ, Semantic Scholar and publisher URLs from Crossref output refused PROVENANCE_REQUIRED)
- d267 3 / 1 / 0 (gradient Tpref: Iberolacerta galani, Podarcis bocagei, P. siculus Menorca; Craugastor loki pooled mean held out; audit 360)
- d268 0 / 0 / 0 (extended-search harvest of other traits; PMC reCAPTCHA, hosts blocked; progress note only)
- d269 4 / 0 / 0 (Giglio et al. 2022 Life 12(5):741 interommatidial_deg x4; all fixed after audit 361)
- d270 8 / 1 / 0 (MDPI Insects ommatidia_count and facet_diameter_um: Arge similis x4, Ceratosolen gravelyi, Histia flabellicornis x3; Histia interommatidial_deg repeats d215; audits 362, 363)
- d271 6 / 0 / 0 (MDPI Insects ommatidia_count: Asiophrida xanthospilota x2, Scythris sinensis x4; Scythris fixed after audit 364)
- d272 4 / 0 / 0 (Grapholita molesta Front Physiol 15:1343702: ommatidia_count x2, facet_diameter_um, rhabdom_um; all fixed after audit 365)
- d273 0 / 0 / 0 (gap-queue vertebrate/bumblebee/butterfly search; every open paper already on main)
- d274 7 / 0 / 0 (MDPI Biology/Insects eye morphology: Tomicus yunnanensis x5, Cacopsylla chinensis x2; fixed after audit 366)
- d275 1 / 0 / 0 (Okanagana rimosa sense_vibration leg-nerve threshold; fixed after audit 367; non-visual-sense vein saturated)
- d276 1 / 0 / 0 (held-lead retry: Phalacrocorax carbo in-air hearing threshold; fixed after audit 368; other leads held)
- d277 1 / 0 / 0 (aquatic sweep: Carcharhinus limbatus sound-avoidance with estimated received levels; fixed after audit 369)
- d278 0 / 0 / 0 (2026-recency sweep; its 4 Scythris sinensis ommatidia_count records repeat d271, not merged)
- d279 0 / 0 / 0 (small OA society/taxonomic journals; no licence sentences, reviews, lab stock; progress note only)
- d280 5 / 0 / 0 (eye absence/reduction in cave and subterranean taxa: Gegeneophis carnosus, Erhaia dijiang, Otilioleptes marcelae, Astyanax mexicanus Chiquitita, Sinocyclocheilus longicornus; 3 fixed after audit 370)
- d281 8 / 0 / 0 (eye absence/reduction in new cave species: Domene lizeyui, Triplophysa zhijinensis, Odontostreptus fadriquei, Iandumoema smeagol, Iansaoniscus x2, Schaefferia x2; 3 fixed after audit 371)
- d282 7 / 0 / 0 (eye absence/reduction in new cave species: Ochyrocera x2, Geopselaphus, Caridina, Triplophysa xiuwenensis, Ptomaphaginus troglodytes, Acherontiella; fixed after audit 372)
- d283 7 / 0 / 0 (eyes_count and eye_type in taxonomic descriptions: Leptonetela x2, Selachochthonius naledi, Pseudocrangonyx wonkimi, Gammarus tumaf, Lithobius x2; audit 373 found 0 errors)
- d284 7 / 0 / 0 (eye states in marine and groundwater invertebrates: Gyorome guttatum, Nereis tricirrata, Caridina incolor, Vitropyrgus lillianae, Phreatodrobia bulla, Paladilhiopsis x2; audit 374 found 0 errors)
- d285 5 / 0 / 0 (eye states in minor invertebrate groups: Eurycyde bamberi, Dugesia gemmulata, Tachycines trapezialis, Zorotypus komatsui, Neocarus proteus; 2 fixed after audit 375)
- d286 0 / 0 / 0 (vertebrate eye-diameter tables: holotype measurement lists run far over 40 words; table CSVs carry no species/DOI; progress note only)
- d287 7 / 0 / 0 (invertebrate eye states: Graeconiscus gevi, Alpioniscus onnisi, Horatia ozimeci, Cylindroiulus villumi, Typhlonesticus gocmeni, Tritomurus veles, Oncopodura moghanensis; audit 376 0 errors)
- d288 6 / 0 / 0 (eyes_count: Troglobentosminthurus luridus, Trogolaphysa reneaui, Lithobius sinuispineus, minuticornis, tetraspinus, zhangi; audit 377 1 fixable error)
- d289 6 / 0 / 0 (ocelli: Glyphiulus longus, Paracortina kyrang, Hyleoglomeris alba, halang, translucida, Trichoniscoides castanheirensis; audit 378 1 fixable error)
- d290 7 / 0 / 0 (eye_type, crustaceans: Asellus ismailsezarii, Caridina tashanica, Spelaeocaris electa, Siamcyclops isanus, Mixtacandona thessalica, Pseudocandona sulphurella, Tuberocandona leonidasi; audit 379 0 errors)
- d291 15 / 0 / 0 (ant and termite ommatidia/eye diameter: Carebara x3, Platythyrea x2, Brachyponera x2, Ooceraea x2, Rugitermes tinto and others; audits 380 and 381: 2 fixable errors in 15)
- d292 15 / 0 / 0 (spider eye states/counts and eye_diameter_mm: Pinelema x8, Dysderocrates kibrisensis, Harpactea kalavachiana, Troglocoelotes sinanensis, Typhlonesticus angelicus and santinellii; audits 382 and 383: 3 fixable errors in 15)
- d293 7 / 0 / 0 (Collembola eye statements: Pseudosinella hartnerae and altamirensis, Coecobrya sirindhornae, whitteni, troglobia, ellisi, phitsanulokensis; audit 384: 1 fixable error in 7)
- d294 7 / 0 / 0 (non-arthropod invertebrate eyes: Tetranemertes bifrost, Tetrastemma album and shohoense, Placobdelloides sirikanchanae, Oerstedia pseudoculata, Leitoscoloplos olei, Iranobelgrandia persica; audit 385: 3 fixable errors in 7)
- d295 8 / 0 / 0 (cave and surface fishes eye_type: Sinocyclocheilus wanlanensis and guiyang, Triplophysa anshuiensis and dafangensis, Troglonectes canlinensis, Lucifuga gibarensis, Oreonectes qinae, Protocobitis longibarba; audit 386: 3 fixable errors in 8)
- d296 5 / 0 / 0 (Strumigenys subterranea, Leptanilla voldemort, Blepharicera gengdica, balangshana, kongsica; audit 387: 1 fixable error in 5)
- d297 9 / 0 / 0 (cave and soil insects: Cixius theseus and palmirandus, Nocticola appendiculata, cordiformis, gonzalezi, Iuiuia caeca, Valenciolenda fadaforesta, Spelaeometra hypogea, Camptochaeta prolixa; audits 388 and 389: 1 fixable error in 9)
- d298 4 / 0 / 0 (eye_type: Yirrkala nkust, Microcaecilia dermatophaga, Amphisbaena amethysta, Toxicocalamus longhagen; audit 390: 1 fixable error in 4)
- d299 6 / 0 / 0 (amphipod, millipede eye counts: Synurella odessana, Hyleoglomeris erecta and rukouqu, Gammarus sezgini, Caucaseuma strasseri, Phoxirostus longicarpus; audit 391: 3 fixable errors in 6)
- d300 7 / 0 / 0 (flatworm eye states: Girardia multidiverticulata, Dugesia bifida, Pasipha ferrariaphila, Stylochus marimarensis and erytheius, Emprosthopharynx hartei, Dendrocoelum obstinatum; audit 392: 3 fixable errors in 7)
- d301 6 / 1 / 0 (meiofauna eyespots: Cephalodella binoculata, Milnesium minutum and sandrae, Microstomum laurae and edmondi, Macrostomum littorale; Pectinereis strickrotti held out, page unopenable; audit 393: 5 errors in 7, 4 fixable)
- d302 6 / 0 / 0 (beetle eye states: Dayao emeiensis, Linan tendothorax, Batrisodes zhouchaoi, Duvalius gejzadunayi, Wanoblemus huangshanicus, Protopholeuon ponoricum; audit 394: 2 fixable errors in 6)
- d303 8 / 0 / 0 (stygobiont and marine crustacean eye states; audit 395: 1 fixable error in 8)
- d304 22 / 0 / 0 (polychaete, sea spider, tardigrade and mole eye states; audits 396-398: 8 fixable errors in 22)
- d305 16 / 0 / 0 (scorpion, pseudoscorpion, eel, chaetognath, schizomid and amblypygid eye states; audits 399-400: 11 fixable errors in 16)
- d306 12 / 0 / 0 (spider, larval, fossil, deep-sea fish and Pholis eye states; audits 401-402: 9 fixable errors in 12)
- d307 6 / 1 / 0 (amber insects, mole cricket, flea beetle and moth eye states; audit 403: 1 repeat dropped, 4 fixable errors in 7)
- d308 5 / 0 / 0 (owl axial length, caecilian, ant, mayfly and dobsonfly eye states; audit 404: 1 fixable error in 5)
- d309 20 / 0 / 0 (mysid, amphipod, fish, tabanid, flatworm, isopod, hoverfly and ant eye states; audits 405-407: 12 fixable errors in 20)
- d310 5 / 0 / 0 (flower beetle, ant ommatidia/facet/rhabdom and leiodid larva eye states; audit 408: 2 fixable errors in 5)
- d311 50 / 0 / 0 (Pselaphinae eye facet counts, Oedipina, Chodsigoa and Linan; audits 409-415: 10 fixable errors in 50, all fixed)
- d312 12 / 0 / 0 (Tachycines cave crickets, planthopper, ant, scale insect and aphid eye states; audits 416-417: 3 fixable errors in 12; Crossref refused, page citation lines used)
- d313 16 / 0 / 0 (leaf insects, twisted-wing parasite, thrips, lacewing and velvet worm eye states; audits 418-419: 6 fixable errors in 16)
- d314 7 / 0 / 0 (huntsman spider, earwig, fish, polychaete, amphipod and eunicid eye states; audit 420: 2 fixable errors in 7)
- d315 23 / 0 / 1 (cockroach, earwigs, water striders, fossil beetles, wood roaches, Diapriidae and Cranopygia eye states; audits 421-423: 4 fixable errors fixed, 1 synonym record dropped)
- d316 12 / 0 / 0 (gall midges, fungus gnat, keroplatid and cave cricket eye states; audits 424-425: 3 fixable errors in 12)
- d317 16 / 0 / 0 (cave and soil beetles, harvestman, fairyfly and others; audits 426-427: 5 fixable errors in 16)
- d318 14 / 0 / 0 (moth-fly and sand-fly relatives, parasitoid wasp, assassin-like bug, flatworm and bristle worm eye states; audits 428-429: 2 fixable errors in 14)
- d319 8 / 0 / 0 (open-access new-species descriptions and Tridacna eye counts; audit 430 found 2 fixable errors)
- d320 10 / 0 / 0 (eye length and diameter tables; audits 431/432 found 5 fixable errors in 10)
- d321 0 / 0 / 0 (threshold papers; everything open-licence already on main or held out)
- d322 10 / 0 / 0 (centipede ocelli, spider and mysid eyes from ZooKeys; audits 433/434 found 4 fixable errors in 10)
- d323 7 / 0 / 0 (non-arthropod invertebrate eyes; audit 435 found 3 fixable errors in 7)
- d324 0 / 0 / 0 (vertebrate eye anatomy; open-licence papers already on main or fail licence/quote rules)
- d325 8 / 0 / 1 (bat echolocation, mole cochlear nerve, bat vomeronasal organs; audits 436/437 found 4 errors in 9, one unfixable dropped)
- d326 2 / 0 / 0 (Pipistrellus terminal frequency, Sorex cochlear nerve; audit 438 found 3 fixable errors in 2)
- d327 9 / 0 / 1 (polarization, colour and looming behaviour in JEB papers; audits 439/440 found 7 errors in 10, one repeat dropped)
- d328 8 / 0 / 0 (antennal glomeruli and sensilla counts; audit 441 found 5-8 errors in 8, all fixed incl. a synonym refile)
- d329 6 / 0 / 5 (light and moon effects on behaviour; audits 442/443 found 10 errors in 11; five moon-correlate records held out pending a trait-key ruling)
- d330 5 / 0 / 1 (bat echolocation, pit-organ papillae; audit 444 held Philaenus out unverifiable and found 11 errors in 5, all fixed)
- d331 2 / 0 / 0 (cephalopod eye range, flashlight-fish dummy response; audit 445 found 2 fixable errors in 2)
- d332 12 / 12 / 0 (tympanum ratios, ant and isopod eye counts; audits 446/447 found 10 errors in 12, all fixed)
- d333 4 / 4 / 0 (Collembola eyes_count; audit 448 found 0 errors)
- d334 6 / 6 / 0 (cavefish/loach eye-diameter ratios, Gekko eye diameter; audit 449 found 2 fixable errors in 6)
- d335 4 / 4 / 0 (millipede ocelli/ommatidia, scorpion eyes; audit 450 found 1 fixable error in 4)
- d336 3 / 3 / 0 (ganglion cell densities, cave catfish eye size; audit 451 found 0 errors)
- d337 6 / 6 / 0 (antennal sensilla in Megaphragma, Bactericera antenna; audit 452 found 6 fixable errors in 6)
- d338 4 / 4 / 0 (shark saccular hair cells, ground-squirrel stapes; audit 453 found 4 fixable errors in 4)
- d339 9 / 9 / 0 (snake eye diameters from one Frontiers table; audit 454 found 0 counted errors)
- d340 10 / 10 / 0 (second set of snake eye diameters from the d339 paper; audit 455 found 1 fixable error in 10)
- d341 11 / 11 / 0 (deep-sea sergestid shrimp eye diameters, Schweikert 2022; audits 456/457 found 11 fixable quote-cut errors in 11)
- d343 8 / 8 / 0 (fish, gecko and frog eye diameters from taxonomy tables; audit 458 found 2 fixable errors in 8)
- d344 8 / 8 / 0 (PeerJ frog holotype eye and tympanum diameters; audit 459 found 1 fixable error in 8)
- d345 3 / 3 / 0 (Bagarius eye ratios, Murina ear length; audit 460 found 2 fixable errors in 3)
- d346 5 / 5 / 0 (antennal and mouthpart sensilla counts; audit 461 found 1 fixable error in 5)
- d347 4 / 4 / 0 (bat and shrew holotype ear and tragus lengths; audit 462 found 0 errors)
- d348 4 / 4 / 0 (amphipod and shrimp eye absence/presence; audit 463 found 2 fixable errors in 4)
- d349 5 / 8 / 2 (spider, pseudoscorpion eyes; hei split into four per-eye records; 2 fixable errors)
- d350 2 / 2 / 0 (Gryllotalpa xinjiangica ocelli, eyes, tympanum; most Orthoptera/Blattodea leads already on main)
- d351 4 / 4 / 4 (lungfish photoreceptor types, one paper; order Ceratodontiformes; contrary result added)
- d352 0 / 0 / 0 (birds and mammals physiology; page tool returned no usable licence or text; leads: Oreoryzomys jumandi/hesperus PeerJ 20515, Enhydra lutris vibrissae)
- d353 8 / 8 / 2 (Pensoft fish and gecko eye ratios; 2 fixable errors)
- d354 3 / 3 / 1 (frog tympanum and pupil statements, ZooKeys; 1 fixable note error)
- d355 3 / 3 / 3 (behaviour findings in MDPI papers; context and contrary-result omissions, all fixable)
- d356 1 / 1 / 1 (Paleotoca diminas eyes absent; author form and note fixed)
- d357 11 / 11 / 7 (spider PME sizes, three ZooKeys papers; ZooKeys 1174 lines moved to eye_diameter_mm)
- d358 3 / 3 / 2 (Collembola eyes 8+8, millipede ommatidia; P. canastra refiled as P. ambuatinga)
- d359 16 / 16 / 16 (Asceua, Mallinella eye diameters, ZooKeys 1200; note-only errors plus female values; quotes and values all correct)
- d360 16 / 16 / 12 (Synagelides eye sizes, ZooKeys 1245; note-only errors; S. wuyuan name unchecked)
- d361 5 / 5 / 1 (Myrmecina worker ommatidia counts, DEZ 72(2); 1 fixable conditions fault)
- d362 16 / 16 / 10 (Pholcus PME/AME diameters, ZooKeys 1240 and 1264; note-only errors; female values added)
- d363 16 / 16 / 16 (Tapinocyba eye diameters, ZooKeys 1219; note-only errors, values and quotes all correct)
- d364 10 / 10 / 2 (Collembola eyes 8+8, Parobisium eye spots, Acherontiella eyes absent; 2 quote-form errors fixed)
- d365 10 / 10 / 10 (frog tympanum and eye diameters: Nectophrynoides table means, Pristimantis holotypes; note-only errors, family added)
- d366 4 / 4 / 1 (Choerophryne ED/SUL and TyD/ED, ZSE 93(2); subadult female caveat added)
- d367 5 / 3 / 5 (small-mammal ear and tragus; 3 fixed, 2 Kerivoula lines dropped as unfixable)
- d368 24 / 24 / 4 (Clubiona eye diameters, ZooKeys 1248; best audit result of the multi-species spider papers)
- d369 24 / 24 / 12 (Sudesna, ZooKeys 1234; all faults in note text, fixed)
- d370 32 / 32 / 32 (Weintrauboa ZooKeys 1236; Hippasosa and Mutatus ZooKeys 1226; all faults in note and conditions text, fixed)
- d371 8 / 8 / 3 (Collembola ZooKeys 1282, mite ZooKeys 1284, scorpion ZSE 101(3), centipede BDJ 14; Collembola notes fixed)
- d372 2 / 2 / 1 (Paranemachilus, ZSE 100(4); liui conditions fixed)
- d373 56 / 56 / 55 (ZooKeys 1232 Salticidae notes fixed; EJT 997 Paratropis: interdistances filed as eye sizes, values replaced)
- d374 32 / 32 / 8 (Neischnocolus EJT 1022; Hunan Linyphiidae ZooKeys 1253; all values right, quote faults fixed)
- d375 40 / 40 / 24 (Sinartoria ZooKeys 1244; Hamataliwa ZooKeys 1282; values right, Hamataliwa conditions fixed)
- d376 44 / 44 / 36 (Phrynarachne ZooKeys 1085; Pseudopoda ZSE 101(1); values right, conditions fixed)
- d377 52 / 52 / 44 (Phrynarachne ZooKeys 1085; Yinanyphaena ZooKeys 1196; Atypus ZooKeys 1229 moved to eye_diameter_mm; values right, conditions fixed)
- d378 40 / 40 / 36 (Uaica EJT 989 eye order confirmed; Heteropoda EJT 1022; values right, conditions fixed)
- d379 43 / 43 / 35 (ZooKeys 1200 Asceua chayu and Cydrela; ZooKeys 1254 Hahnia and Sinahahnia chengkou; BDJ 13 Neoantistea; ZooKeys 1197 Sinahahnia; values right, conditions fixed)
- d380 52 / 52 / 52 (BDJ 14 Zangaraneus and Drapetisca; ZooKeys 1245 Sinoamaurobius and Spiricoelotes; values right, conditions fixed; Spiricoelotes units inferred from scale bars)
- d381 40 / 40 / 40 (ZooKeys 1283 Pholcus baegamsan, hongcheon, namhae, yeongcheon; ZooKeys 1275 Pholcus alashan, chifeng; values right, conditions fixed)
- d382 44 / 4 / 44 (BDJ 14 Pholcus yajiyagama merged; ZooKeys 1292 Pseudopoda and ZooKeys 1296 Poeciloneta, 40 records, held out: publisher pages not reachable by the auditors, fetched by the unit from non-search URLs)
- d383 34 / 34 / 34 (BDJ 14 Scytodes tanjiashui; ZooKeys 1280 Sinopoda honghe, kuan; ZooKeys 1269 Parazygiella jianxini, yanghongae; values right, conditions and unit field fixed)
- d384 48 / 48 / 48 (ZooKeys 1269 Tetragnatha tricuspidata, hirashimai; ZooKeys 1200 Cheiracanthium bannaensis, bifurcatum; ZooKeys 1255 Qianlingula jiafu, turbinata; values right, conditions fixed)
- d385 36 / 36 / 36 (ZooKeys 1278 Sudesna chayu, mii, medog, flavipes, linzhiensis; values right, conditions fixed)
- d386 40 / 40 / 40 (ZooKeys 1217 Thomisidae Camaricus medog, Monaeses xizang, Sinothomisus beibeng, S. dawai, Spilosynema motuo; values right, conditions and where fixed; non-spider angle found nothing usable)
- d387 24 / 24 / 24 (ZooKeys 1240 Acantholycosa zang, zhangi; ZooKeys 1217 Thomisus yarang)
- d388 60 / 60 / 22 (ZooKeys 1146 Dysdera, 14 new Iranian species; faults in where/conditions only)
- d389 57 / 57 / 28 (ZooKeys 1247 Leptonetela zhaoruii, Pararana x3; ZooKeys 1189 Leptonetela, Longileptoneta, Pararana mingxuani; PLE values 0.0 corrected)
- d390 34 / 34 / 16 (ZooKeys 1161 Zhuaraneus, Araneus liami, Wangaraneus ryani; ZooKeys 1213 Micropholcus; values right, faults in where/conditions)
- d391 45 / 45 / 12 (ZooKeys 1187 Hahniidae: Goblinia, Myahnia, Troglohnia x4, Typhlohnia banlaksao; eye_diameter_mm)
- d392 20 / 20 / 0 (ZooKeys 1236 Agelenidae: Ageleradix dulong, jinfoshan, nangunhe; faults in notes only)
- d393 33 / 33 / 0 (ZooKeys 1216 and 1202 Belisana PME diameters, 17 species; faults in notes only; eye_diameter_mm kept, owner question on the label)
- d394 35 / 35 / 13 (ZooKeys 1125 Tetragnatha x3; ZooKeys 1108 Haplodrassus yinae, Hitobia xiaoxi; sensory_anatomy)
- d395 42 / 42 / 0 (ZooKeys 1221 Salticidae: Dendroicius, Icius, Irura x2, Myrmarachne, Nandicius, Pancorius; faults in text only; lead: Wang et al. 2024 may define eye size)
- d396 45 / 41 / 6 (ZooKeys 1221 Cheliceroides, Protaeus (ex Mintonia) shiwandashan, Pancorius medog; ZooKeys 1192 Attulus, Colaxes, Epeus, Evarcha, Icius, Pancorius; 4 held out)
- d397 42 / 42 / 0 (ZooKeys 1192 Stertinius liqingae, Synagelides tianquan, Yaginumaella erlang; ZooKeys 1148 Chinattus crewsae, C. logunovi, Eupoa maidinhyeni, E. maddisoni; faults in text only)
- d398 39 / 39 / 4 (ZooKeys 1148 Eupoa ninhbinh, E. zabkai, Indopadilla cuc, Synagelides ani, S. mii, S. pengi, S. sancha, Yaginumaella hagiang; 4 lines said female holotype, each holotype is male)
- d399 48 / 48 / 13 (BDJ 12 e138400 Phintella hongkan, P. liae; BDJ 13 e156957 Jerzego qiuhangi; ZooKeys 1257 Chuanattus, Dianattus, Yaginumaella x4; 5 lines wrong paratype counts, 8 lines wrong heading path)
- d400 36 / 36 / 16 (ZooKeys 1210 Altimella nedong, A. ngamring, eye_diameter_mm; ZooKeys 1123 Himalaphantes arcuatus, lingulatus, uncatus; 16 lines wrong heading path or missing paratype lead-in; heading paths between auditors not reconciled)
- d401 60 / 60 / 16 (EJT 917 Spinirta hongyui, liuae, simianshan, yintiaoling, aviformis, quadrata, eye_diameter_mm; EJT 947 Heteropoda dulongensis, longa, vaginalis; 16 lines: copied male fetch note, where-path missing printed headings; 16 cut quotes completed)
- d402 40 / 40 / 20 (EJT 947 Heteropoda bawanglingensis; BDJ 13 e144222 Asiopisinus anfu, implicatus, pseudonubilus; EJT 968 Meotipa lingulata, pseudomultuma, tortuosa; where-paths missing printed Class and Order headings, A. anfu wrong next sentence; Meotipa family is Theridiidae)
- d403 60 / 60 / 16 (ZooKeys 1218 Maimuna antalyensis, Tegenaria ballarini, beyazcika, egrisiana, hoeferi; ZooKeys 1224 Clubiona longyangensis, multiprocessa, eye_diameter_mm; ZooKeys 1183 Grandilithus chongzuo; 16 Clubiona lines missing the printed Clubiona corticalis group heading; false Crossref claims removed)
- d404 44 / 44 / 0 (ZooKeys 1183 Grandilithus xiaohuangshan, lanxi; BDJ 13 e144804 Otacilia tongboshan; ZooKeys 1181 Sinocranum menghai, Xantharia baizilongi, X. cucphuong; faults in text only; Xantharia family Systariidae per WSC)
- d405 32 / 32 / 0 (ZooKeys 1175 Euryeidon dian, Mallinella banna, M. mengla; ZooKeys 1169 Sinoamaurobius guangwushanensis, wulongdongensis (printed Amaurobius); faults in text only; Koppe ninger is a synonym, not filed)
- d406 48 / 48 / 0 (ZooKeys 1261 Shuqiangius chuan; BDJ 10 e94853 Eresus da, E. yukuni; BDJ 12 e142805 Hersilia lelabah; ZooKeys 1116 Sinopoda muyuensis, S. wuyiensis; Subterranean Biology 52 Orphnaecus libmanan, O. tangcongvaca)
- d407 44 / 44 / 0 (ZSE 101(2) Mimetus guiyang, M. lanmeiae, M. caudatus; BDJ 13 e153747 Aculithus languan, A. ruijin; BDJ 12 e133875 Anyphaena leidashi; BDJ 14 e182804 Planochelas jingda)
- d408 30 / 30 / 0 (BDJ 14 e178451 Philodromus uljin; ZooKeys 1265 Latouchia jihe; BDJ 13 e143433 Falcileptoneta taoqii; BDJ 13 e157512 Hellamalthonica kazdagensis)
- d409 36 / 36 / 0 (ZooKeys 1290 Hexura vandal; BDJ 10 e85436 Arabelia xizang; BDJ 10 e82406 Selenocosmia zhangzhengi; BDJ 13 e153724 Thelcticopis lini, Olios sericeus)
- d410 56 / 56 / 40 (ZooKeys 1052 Vacrothele emei, Spinathele hanfeii, S. nanning, Gigathele hungae, G. limenghuai [genus corrected from Macrothele per WSC]; EJT 932 Macrothele nullispine, M. auriculata)
- d411 60 / 60 / 0 (Evolutionary Systematics 10(2) Yunka suenos, Y. guasaganda, Y. baboso, Homoeomma josti; BDJ 10 e91350 Anahita menglun, Bowie haiphong, B. mengla, B. zhengi, Sinoctenus zhui [24 lines moved to sensory_anatomy]; BDJ 10 e90967 Orientothele washanensis)
- d412 34 / 34 / 0 (BDJ 13 e153601 Metashinobius hikariae; ZSE 99(1) Drymusa huberi; BDJ 11 e109714 Paracedicus turcicus [18 lines moved to sensory_anatomy]; ZSE 100(2) Bifurcia kangding, B. luding)
- d413 36 / 28 / 8 (ZSE 100(2) Bifurcia labahe, B. shuangqiao; ASP 84 Kiskalla ignacioi; BDJ 13 e142264 Raveniola fuzhouensis; ZooKeys 1285 Nesticus yamabushi dropped: no printed unit)
- d414 31 / 31 / 0 (ZSE 100(2) Bifurcia xiaojin; ASP 84 Kiskalla yeisoni, K. zukuapasanka; ZooKeys 1215 Trachelas kavanaughi, T. ventriosus; ZooKeys 1226 Siskiyu armilla, Cybaeozyga furtiva [7 lines moved to sensory_anatomy])
- d415 59 / 59 / 4 (ZooKeys 1248 Hamus qingming, Tekellina zhangziqingi; BDJ 11 e102450 Siamspinops yejiei; BDJ 10 e82682 Haplocosmia sherwoodae [quote corrected]; ZooKeys 1080 Taksinus bambus; BDJ 12 e137852 Latouchia calcicola, L. linmufu, L. wenchuan)
- d416 40 / 40 / 4 (BDJ 13 e160680 Selenops ab; ZooKeys 1159 Sinopoda guiyang, S. xishui, S. horizontalis; ZooKeys 1260 Pseudopoda rongxianensis, P. spiralis; ZooKeys 1116 Sinopoda wuyiensis female; ZooKeys 1117 Edelithus puer, E. shenmiguo)
- d417 36 / 36 / 0 (ZooKeys 1241: 205-246 Rangkayo hitam, R. perkaso, Ibana svarnadvipa, Crockeria neofelis, Pharta roseomaculata)
- d418 32 / 32 / 0 (BDJ 14 e182063 Theridion ganjiangyuan; BDJ 14 e178386 Coelotes fani; BDJ 13 e176953 Otacilia baimashan, O. wulong)
- d419 52 / 52 / 0 (ZSE 102(4) Metashinobius daweishan, M. dulongjiang; ZSE 101(1) Pimoa shimian; ZSE 100(3) Pamirosa kudratbekovi; ZSE 102(3) Ovia chayu, O. dawai, O. dulong)
- d420 57 / 57 / 0 (ZSE 102(3) Ovia medog, O. separata; ZSE 101(4) Bogdocosa yunshani; BDJ 12 e130526 Xilithus qizimeishanensis; ZSE 102(1) Pikelinia floydmuraria (moved to sensory_anatomy); EJT 976 Vacrothele fuyuanensis, V. jiangkouensis, V. baiseensis male; ZooKeys 1203 Shinobius cona)
- d421 24 / 24 / 0 (ASP 83 Euathlus basalticus, E. kupal, E. susanae; all 24 lines had wrong pages, corrected to 713-736 from the publisher XML)
- d422 20 / 20 / 0 (Evolutionary Systematics 9(2) Platnickina debu, P. adamsoni, P. fritilla)
- d423 16 / 16 / 0 (Evolutionary Systematics 9(2) Platnickina harapan; ZooKeys 1278 Ilocomba yotoco; auditors moved all lines to sensory_anatomy, desk kept eye_diameter_mm, owner question)
- d424 48 / 48 / 0 (EJT 1081 Psechrus luopingensis, P. mingshengi, P. cornutus, P. cordatus (kept eye_diameter_mm, owner question; lab-reared sentence flagged); Evolutionary Systematics 10(1) Acanthogonatus monicae; Evolutionary Systematics 9(1) Gephyrellula condeuba)
- d425 24 / 24 / 0 (ZooKeys 1266 Megama decimaculata, Meotipa cordata, M. vittiforma; ZooKeys 1248 Draposa zhanjiangensis; unit read a Crossref list query, reported in the progress note)
- d426 12 / 12 / 0 (ZooKeys 1286 Paratropis barragani, P. intag male)
- d427 12 / 12 / 0 (Evolutionary Systematics 10(2): 217-261 Romopelma chirapa; Taprobanica 14(1): 39-47 Heligmomerus australis)
- d428 36 / 36 / 0 (ZooKeys 1219: 61-72 Cicurina chengkou, C. dabashan, Longicicurina longihamata; BDJ 12 e124006 Otacilia wuxi; BDJ 12 e116569 Xizangiana plankton)
- d429 10 / 2 / 8 (ASP 84: 95-121 Caipira mineira merged; Acta Zoologica Mexicana 42: 1-7 Filistatinella bacanora held out: trait, header-tag licence, WSC page unread)
- d430 8 / 8 / 0 (Australian Journal of Taxonomy 49: 1-6 Artoriopsis dubia)
- d431 51 / 48 / 3 (ZooKeys 1137 Araneus x3; ZooKeys 1072 Acusilas tongi, Chorizopes yui; ZSE 99(2) Anatextrix monstrabilis merged; EJT 1067 Dysdera asaahil, D. sidimaafa held out: publisher PDF unreachable)
- d432 32 / 24 / 8 (ZooKeys 1197 Sinahahnia yintiaoling; ZooKeys 1233 Chilocosmia dichromata; Diversity 18(1): 54 Herennia eva, H. maj, H. tsoi merged; ZooKeys 1233 Selenobrachys x2 held out: publisher text unreachable past Results)
- d433 60 / 60 / 0 (ZooKeys 1137 Araneus corrugis, Qianaraneus cucullatus, A. tetracanthus, A. minisculus, A. ovoideus, A. pseudodigitatus, A. semiorbiculatus; ZooKeys 1072 Chorizopesoides guoi, Deione yangi, Milonia gemella)
- d434 36 / 36 / 0 (BDJ 11 e103298 Asceua haocongi, A. zijin; BDJ 10 e96467 Chilobrachys qishuoi; ZooKeys 1081 C. dominus, C. jinchengi; Diversity 18(1): 54 Herennia tone)
- d435 20 / 20 / 0 (JoTT 12(4) Icius alboterminus; JoTT 17(8) Pellenes iva, Thyene bivittata; JoTT 18(1) Sonoita lightfooti; JoTT 18(7) Steatoda albomaculata)
- d436 36 / 36 / 0 (ZooKeys 1239 Houcosa zhaoi; ZooKeys 1173 Araneus chenjingi, A. lihaiboi; ZooKeys 1160 A. fenzhi, A. mayanghe)
- d437 56 / 56 / 8 (ZooKeys 1160: 169-190 Araneus zhoui, A. mayanghe female; ZooKeys 1137 A. arcuatus corrected to A. xiang (preoccupied name, 8 counted); Insects 16(10): 992 Megaraneus gabonensis; ZooKeys 1257 Phrynarachne x4; ZooKeys 1160: 75-87 Ebelingia spirala, Lysiteles longensis)
- d438 8 / 8 / 0 (Australian Journal of Taxonomy 5: 1-8 Euoplos eungellaensis; trait move only, not counted)
- d439 20 / 20 / 0 (ZooKeys 1072: 49-81 Mangora baii, M. cephala, Hypsosinga pulla, Deione cheni; ZooKeys 1160: 169-190 Araneus shiwandashan)
- d440 36 / 24 / 12 (ZooKeys 1034: 199-236 Eriovixia ganae, E. liuhongi, E. tangi merged; ZooKeys 1223: 169-184 Yaginumia medog, Y. qiong dropped: WSC species page not reached)
- d441 40 / 40 / 0 (ZooKeys 1191: 75-88 Gea jingdong; ZooKeys 1157: 163-176 Clubiona x3; BDJ 12: e137014 Otacilia subshanxi)
- d442 52 / 52 / 0 (ZooKeys 1034: 199-236 Eriovixia x4; ZooKeys 1233: 139-193 Selenobrachys x2; PeerJ 12: e16781 Dolomedes bedjanic, D. hydatostella male)
- d443 36 / 36 / 0 (ZooKeys 1265: 103-127 Latouchia x4; ZooKeys 1278: 201-213 Calommata yueluensis male)
- d444 20 / 20 / 0 (ZooKeys 1232: 285-310 Pholcus hebei, P. huludao, P. jinzhou, P. liaoning, P. qin)
- d445 32 / 32 / 0 (ZooKeys 1173: 243-273 Araneus yuboi, A. shii, A. wanghuai, A. yangchuandongi)
- d446 8 / 8 / 0 (BDJ 13: e137852 Latouchia jinyun; trait kept eye_diameter_mm to match d415)
- d447 57 / 21 / 36 (EJT 861 Ammonius, EJT 856 Cuiambuca, EJT 821 Neostasina maisi merged; EJT 921 Loxosceles and Neostasina aceitillar, N. bani dropped: WSC species page not reached; Cuiambuca vacabrava male and borborema PME/PLE dropped: publisher text not reached by auditor)
- d448 32 / 32 / 0 (EJT 989: 289-310 Devade longa, D. pulla, D. mongolica, D. qiemuensis)
- d449 0 / 0 / 0 (no records: every candidate on main, no numeric eye values, or no publisher page reached)
- d450 8 / 8 / 0 (Sudesna wangi, ZooKeys 1278)
- d451 21 / 18 / 4 (frogs and geckos, eye_diameter_mm; 3 pooled means dropped, 1 quote cut)
- d452 40 / 40 / 0 (Hortophora x4 and Mangrovia albida, eye_diameter_mm on the label precedent; open owner question on label-only evidence)
- d453 36 / 36 / 0 (Pholcus x9 species, ZSE 100(1), AME and PME, eye_diameter_mm)
- d454 24 / 16 / 8 (Neostasina x3 merged; Hortophora porongurup x8 dropped, page not reached)
- d455 10 / 9 / 3 (non-spider: Osornophryne, Pristimantis paganus, Calamaria x2; C. incredibilis dropped, no Reptile Database page)
- d456 32 / 32 / 16 (Salticidae: Stenaelurillus x2, Phintella x3; 16 Methods-unit quote errors fixed)
- d457 28 / 28 / 15 (frogs: Odorrana yangi, Brachytarsophrys wui, Boulenophrys x2, Leptobrachella x2; quote and conditions faults fixed)
- d458 16 / 16 / 12 (Phintella handersoni x8 eye_diameter_mm, Langelurillus tertius x8 sensory_anatomy; inferred female code and author-name faults fixed)
- d459 24 / 24 / 6 (Paramesotriton, Tylototriton, Gracixalus, Leptobrachella, Achalinus; ZSE 101(4)-102(4); type-list and unit-caption faults fixed)
- d460 2 / 2 / 2 (Kambiwa neotropica, EJT 1054, sensory_anatomy in micrometres; heading, WSC citation and conditions faults fixed)
- d461 24 / 24 / 16 (Corinnidae x5 species, ZooKeys 1165; Methods-heading and inferred female code faults fixed)
- d462 53 / 33 / 24 (Salticidae Hainan ZooKeys 1118, Chinattus BDJ 13, Stemmops BDJ 11; 20 dropped for unreachable WSC/publisher pages, 4 specimen-code errors)
- d463 34 / 27 / 7 (Amaurobius ZooKeys 1245, Zoica ZooKeys 1249; 7 male/female Zoica lines already carried in main conditions)
- d464 18 / 6 / 12 (Moneta ZooKeys 1251, Zoica oculata ZooKeys 1249; 8 lines repeat main's conditions text, 4 dropped for no WSC page)
- d465 4 / 4 / 4 (Vappolotes tianjiayu male, BDJ 11 e114147; conditions and heading faults corrected)
- d466 16 / 16 / 16 (Argiope beibeng, A. caesarea, BDJ 12 e125601; all lines carried fixable licence and conditions faults)
- d467 12 / 12 / 4 (Euprosthenops insperatus ZooKeys 1065, Pax leila ZooKeys 1035; lines 1-4 specimen and method wording errors, trait kept eye_diameter_mm pending owner ruling)
- d469 4 / 4 / 4 (Zoica oculata male, ZooKeys 1249; heading and material faults corrected)
- d473 5 / 5 / 5 (Andrias yaoluopingensis ZSE 102(2), Boulenophrys daxuemontis paratypes BDJ 13 e153987; Methods heading, quote and licence faults corrected)
- d474 2 / 1 / 2 (Oreonectes damingshanensis ZooKeys 1180 kept; Monomorium brachypterum mean of N=20 dropped as pooled)
- d475 4 / 4 / 4 (Hebius shantianfangi EDH, ZooKeys 1254; licence, type block and table header faults corrected)
- d476 21 / 18 / 3 (Cyrtodactylus nebulicola ZooKeys 1278, Sphenomorphus tamchucensis ZooKeys 1266; 3 Eublepharis jhuma lines already carried in desk-d353 conditions dropped)
- d477 23 / 23 / 7 (seven reptile papers; family and table-row quote errors on 7 lines corrected)
- d478 20 / 20 / 0 (Trimeresurus lii ZSE 102(1), Hemiphyllodactylus venkatadri Herpetozoa 38; note and heading faults corrected)
- d479 14 / 14 / 0 (Gekko tesselatus ZSE 101(4); heading-path faults corrected)
- d480 17 / 17 / 10 (Occidozyga nishikawai 15 records, Vietnamophryne abscondita 2; audits 963-965; fixable errors corrected, two lines moved to sensory_anatomy)
- d481 5 / 5 / 5 (Cyrtodactylus jayadityai OD; audit 966; moved to sensory_anatomy)
- d482 9 / 9 / 9 (Hemiphyllodactylus ziegleri EyeD; audit 967; sex conflict between type list and Table 2 noted)
- d483 4 / 4 / 0 (Lycodon irwini 1, Hemiphyllodactylus laowozhenensis 3; audit 968)
- d484 9 / 9 / 0 (Ingerophrynus chrysolophus ED; audit 969)
- d485 7 / 7 / 0 (Plagiopholis pluvialis ED; audit 970; holotype-vs-paratype spread disclosed)
- d486 14 / 14 / 4 (Ablepharus eremchenkoi 4, Lygosoma siamense 4, Trimeresurus uetzi 1, Bungarus suzhenae 1, Ovophis zayuensis 2, Leptobrachella tamdil 1, Euprepiophis mandarinus 1; audits 971-974)
- d487 4 / 3 / 1 (Rhinophis siruvaniensis 3 merged; Trimeresurus pretiosus dropped for unconfirmed licence; audit 975)
- d488 19 / 19 / 1 (Cyrtodactylus teraiensis 1, C. nebulosus 18; audits 976-978; teraiensis paratype ED 2.9 unfiled)
- d489 8 / 8 / 0 (Scincella tenuistriata ED; audit 979)
- d490 13 / 13 / 0 (Cyrtodactylus teraiensis paratype 1, Trimeresurus ciliaris 5, Balitora tiandengensis 1, Hebius gilhodesi 5, Herpetoreas davidi 1; audits 980-981; citation and transcription faults only)
- d493 1 / 1 / 1 (Trimeresurus nujiang holotype ED; audit 982; trait moved to eye_diameter_mm). d491 and d492 filed 0.
- d494 12 / 7 / 5 (Boulenophrys calciphila 7 merged; Ichnotropis robusta 5 dropped because the table could not be reached by the auditor; audits 983-984)
- d495 6 / 6 / 6 (Hemidactylus kalinga ED; audit 985)
- d497 21 / 21 / 11 (Cnemaspis enneaporus, Leptobrachella shimentaina, Gloydius lateralis, Hebius citrinoventer, Acanthosaura liui ED; audits 986-989)
- d498 23 / 18 / 16 (Cyrtodactylus makwanpurgadhiensis paratypes, C. arnei OD, Achalinus nanshanensis; 5 Gekko fengshanensis paratype lines dropped as repeats of d334 conditions; audits 990-992)
- d499 11 / 11 / 0 (Calamaria synergis holotype, Boulenophrys dalaolingensis ED; audits 993-994)
- d500 17 / 16 / 1 (Hemiphyllodactylus lungcuensis and Cyrtodactylus peninsularis paratypes, Hypselotriton oolong ED; one peninsularis line dropped as a repeat of d343 conditions; audits 995-997)
- d501 7 / 6 / 7 (Scincella truongi eye length moved to sensory_anatomy; Sillago nigrofasciata held out for want of a Catalog of Fishes species page; audit 998)
- d502 0 / 0 / 0 (eye_diameter_mm pool exhausted; ZooKeys 1129 Cyrtodactylus lead dead). d503 0 / 0 / 0 (invertebrates, birds, mammals, salamanders, turtles: nothing met the rules). d504 1 / 1 / 0 (Euscorpiops doiphukha eye_type; cave invertebrate eye-state pool near exhausted; audit 999)
- d505 7 / 4 / 7 (Otomops harrisoni echolocation by site kept; Creobroter nebulosa bristle counts held out for want of an authority page; Cyrtorhinus lividipennis pooled; audits 1000-1001)
- d506 55 / 55 / 31 (Vertebrate Zoology geckos: Cnemaspis pakkamalaiensis, cavernicola, azhagu, mundanthuraiensis, jayaweerai, nanayakkarai; Hemidactylus easai, pakkamalaiensis; Cyrtodactylus irulaorum, relictus; audits 1002-1009)
- d507 34 / 34 / 34 (Cnemaspis salimalii, agayagangai; Hemidactylus quartziticolus; Cyrtodactylus raglai, monilatus; Oligodon speleoserpens ED; faults were mostly the eye side and provenance, values all matched; audits 1010, 1012-1015, 1011 replaced by re-audit 1015)
- d508 15 / 1 / 14 (Colubroelaps adleri merged; Trimeresurus lanna, Cnemaspis auriventralis, Gekko paucituberculatus, Hemiphyllodactylus gengmaensis held out: no auditor reached the publisher full text in four attempts; audits 1016-1019)
- d509 22 / 7 / 15 (Colubroelaps nguyenvansangi and Bungarus sagittatus merged; Cyrtodactylus santana, Cnemaspis umashaankeri, Lycodon truongi held out for unreachable full text; audits 1020-1022)
- d510 32 / 24 / 8 (C. khlonghatensis, Cnemaspis samui merged; C. kampingpoiensis held out for unreachable full text)
- d511 12 / 12 / 0 (Cnemaspis vangoghi, C. sathuragiriensis)
- d512 13 / 13 / 0 (Rhacophorus dulongensis, Odorrana nagao, Leptobrachella kungfu)
- d513 10 / 10 / 0 (Amolops gudao, Zhangixalus thaoae, Calamaria berezowskii)
- d514 0 / 0 / 0 (no filable record: authority pages unreachable, fish tables in % only)
- d515 9 / 9 / 6 (Rhinolophus hilli, Pharotis imogene, Barbastella caspica; sense_echolocation)
- d516 32 / 31 / 29 (Neophocaena asiaeorientalis; Duco et al. 2023 Philippine bats; sense_echolocation)
- d517 47 / 43 / 47 (Duco et al. 2023 ten Philippine bats minus R. macrotis; Pham et al. 2021; sense_echolocation)
- d518 27 / 24 / 27 (Jung et al. 2014 molossids: five species; sense_echolocation)
- d519 64 / 25 / 64 (Jung et al. 2014 molossids, Bittencourt et al. 2025 Pontoporia; sense_echolocation; 32 lines held out for third-party copy only)
- d520 0 / 0 / 0 (followed the exhausted reptile/fish angle; nothing filable)
- d521 8 / 4 / 4 (Rhinolophus hipposideros merged; R. capensis held out for third-party copy only; sense_echolocation)
- d522 9 / 9 / 10 (Rhinolophus capensis, Odendaal 2014 populations; all errors fixable and fixed; sense_echolocation)
- d523 0 / 0 / 0 (no publisher-reachable open paper found; sense_echolocation)
- d524 10 / 10 / 22 (Rhinolophus andamanensis; Vu 2025 four species; all faults fixable and fixed; sense_echolocation)
- d525 10 / 10 / 26 (Salsamendi 2012 two species; Vu 2025 four species; all faults fixable and fixed; sense_echolocation)
- d526 3 / 3 / 19 (Dai 2023 three Rhinolophus peak frequencies; one refiled as R. nippon; all fixable and fixed; sense_echolocation)
- d527 13 / 13 / 12 (Dai 2023 R. osgoodi; Thong 2022 three species; Caruso 2022 Neophocaena phocaenoides; all errors fixable and fixed, plus about 40 faults; sense_echolocation)
- d528 2 / 2 / 1 (Weinbeer 2013 Macrophyllum macrophyllum; error fixed; sense_echolocation)
- d529 3 / 3 / 3 (de Framond 2023 Plecotus auritus medians; errors fixed; sense_echolocation)
- d530 10 / 10 / 10 (Redgwell 2009 ten European bat species Emax, mean +/- s.e.m.; errors fixed, plus 15 faults; sense_echolocation)
- d531 10 / 10 / 10 (Thong, Limbert and Limbert 2022 Son Doong Cave three species; errors fixed, plus 38 faults; sense_echolocation)
- d532 0 / 0 / 0 (cff_hz angle; Alexander 2024 Front Cell Neurosci and Myrmecia iScience 2022 are leads awaiting a readable licence sentence)
- d533 2 / 0 / 2 (eye_axial_length_mm: Python bivittatus held out as a repeat under another trait and for an unlisted NC-SA licence; Alexander 2024 dropped; lead: sea turtles Acta Vet Scand 62:52)
- d534 0 / 0 / 0 (eye_axial_length_mm for reptiles, fish, amphibians, cephalopods; leads: Ișler 2020 Kafkas Univ Vet Fak Derg 26(4): 521-524 sea turtle polar axis, no units or definition, NC licence on abstract page only; Acta Vet Scand 62:52 table not readable)
- d535 3 / 1 / 8 (sense_magnetic: Erithacus rubecula merged; Periplaneta americana and Apis mellifera held out for no licence sentence read; replacement text saved)
- d536 4 / 1 / 11 (animal sense_chemical: Metanephrops challengeri merged; Perca fluviatilis, Cynops ensicauda and Liolaemus tenuis held out because authors or licence came from Crossref, which breaks the access rule; replacement text saved)
- d537 1 / 1 / 3 (animal sense_chemical: Cyprinodon rubrofluviatilis alarm cue merged; lead: Astyanax mexicanus EvoDevo 4:25 needs a full byline)
- d538 2 / 2 / 0 (animal sense_chemical: Astyanax mexicanus EvoDevo 4:25, Rana aurora PeerJ 12:e17307; 3 note faults fixed; open question Rana vs Amerana)
- d539 2 / 1 / 5 (animal sense_chemical: Petromyzon marinus Sci Rep 12:17400 merged; Haemorhous mexicanus held out because no IOC page could be opened; 5 faults fixed)
- d540 2 / 1 / 3 (animal sense_chemical: Clethrionomys glareolus merged; Parus major (a null) held out because no IOC page could be opened; nulls confirmed valid by EVIDENCE-INTAKE.md)
- d541 2 / 2 / 3 (animal sense_chemical: Vulpes vulpes Sci Rep 6:30078, Varanus gouldii J Chem Ecol 48:401; errors fixed)
- d542 2 / 2 / 2 (Pomacentrus amboinensis, Canis lupus; sense_chemical)
- d543 0 / 0 / 0 (thin senses electric, infrared, airflow, gravity, hearing: nothing fileable)
- d544 2 / 2 / 2 (Pleurodema thaul, Vulpes vulpes; sense_chemical)
- d545 1 / 1 / 2 (Vipera ammodytes; sense_chemical)
- d546 0 / 0 / 0 (Pensoft journals, animal sense_chemical: nothing fileable)
- d547 2 / 2 / 2 (Nyctereutes procyonoides, Vulpes vulpes; sense_chemical, one paper)
- d548 2 / 1 / 1 (Vulpes vulpes merged; Petromyzon marinus held out, no Catalog of Fishes species page)
- d549 2 / 1 / 0 (Wallabia bicolor merged; Bombus rufocinctus held out, no insect authority host)
- d550 1 / 1 / 0 (Halichoeres garnoti; sense_chemical)
- d342 0 / 0 / 0 (behavioural and physiological thresholds; main holds nearly every open lead; Akashi 2021 pooled means held out)

## Codex lane (26 October 2026)
- Codex runs on the owner's separate ChatGPT allowance, so it takes the plant screening (batches harvest-c7 to c23, 668 genera, 40 a unit, released 26 Oct 04:15 UTC; the free harvest run found nothing to add) and the findings pass. The desk audits and merges; it screens no more plant batches itself.
- An issue is a work request, not a confirmed Codex launch. Follow [CODEX-DISPATCH.md](CODEX-DISPATCH.md): reconcile existing Codex tasks, submit through a verified authenticated interface only when unstarted, and record the returned task URL/ID in the issue. Until that receipt and status exist, execution is unknown; silence is not permission to retry. The chat still follows `docs/tracks/prompts/codex-round.md` and opens a PR titled "Codex round ..." or "Codex findings ...".
- Desk side at each check-in: open pull requests whose title starts with "Codex" (gh api repos/jampotful/seen-back/pulls); audit per desk-audit.md (plant units) or oa-audit.md; merge what passes via the branch (never click merge on the pull request), drop error records, then close the pull request with a comment; triage findings files.
- oa-1 to oa-13 are held until 29 October: Codex's earlier oa pull requests failed audit (50 to 94% errors); release them only after a plant round passes audit and the free oa job (oa-13) has returned copies.
