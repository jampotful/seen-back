# desk-d351 progress

Angle: fish, amphibian and reptile functional/physiological papers in open-access journals. 4 records filed from one paper (target 8), about 38 WebSearch/WebFetch calls. check.py: 0 problems for the new file.

## Filed (docs/views/evidence/desk-d351.jsonl)
- Protopterus dolloi and Lepidosiren paradoxa (Frontiers in Ecology and Evolution 4: 78, 2016, 10.3389/fevo.2016.00078): photoreceptor type counts from the abstract sentence (P. dolloi 1 rod + 2 cone types; L. paradoxa 1 rod + 1 cone type) and "No double cones were observed." for each. sensory_anatomy; no spectral claim.

## Weak spots
- Both species rest on one individual each for measurements (table footnotes); P. dolloi also has a yellow-pigment cone type (36 cells) that may make the cone count three; stated in conditions.
- Names unchecked in WoRMS/GBIF (refused). Crossref has no licence field; the licence rests on the printed CC BY sentence.
- Abstract sentence covers both species and is used for two records.

## Not filed
- Already on main: Amphiprion akindynos and Platichthys stellatus (Sci Rep), Bothrops jararaca and Crotalus durissus retina (Front Neuroanat 770804), Tripterygion delaisi (fnana 2017.122), zebrafish, Gekko subpalmatus, spookfish (Opisthoproctidae), Tiliqua rugosa, Cephaloscyllium isabellum, Neoceratodus forsteri.
- Crocodylus porosus/johnstoni (J Exp Biol 219:1394): no printed licence sentence; held out.
- Dendrobatid frog ERG (PLoS ONE 10.1371/journal.pone.0312578): PMC and journals.plos.org not reachable; values in figures; dendrobatids dense on main.
- Frontiers Malawi cichlid paper (fevo.2016.00012): no per-species sentence, no licence visible.
- Crossref keyword search is too noisy to find functional papers; Springer-hosted Sci Rep and frontiersin PDFs opened. Lead: other Frontiers Collin-lab retina papers not yet on main.

## Desk disposition after audit 466 (2 November 2026)

Audit 466 found all 4 records in error (100%, 5 faults, all fixable): order corrected from Lepidosireniformes to Ceratodontiformes on every line (FishBase and main's own lungfish row), and the Protopterus dolloi no-double-cones record now carries the printed contrary result (Pfeiffer 1968 reported double cones). Replacement lines merged; check.py 0 problems.
