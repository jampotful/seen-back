# desk-d6 (27 October 2026): Hamamelis, Apios, Nothoscordum, Clematis, Carpinus, Cocculus, Sagittaria, Richardia

All eight genera are accepted names (Richardia is the Rubiaceae genus; POWO page for R. grandiflora opened: accepted). POWO search pages for the others were refused by the fetch tool, so their status rests on the species names the queue and sources use.

## Cells closed by a measurement (evidence/desk-d6.jsonl, 8 records)
- Nothoscordum diel: N. bivalve flowers opened 12:30 to 15:00 and closed after 17:00 (Weiherer et al. 2020, open PDF).
- Clematis sense_light_nonvisual: C. vitalba light against dark (Jarvis-Lowry et al. 2024, open PDF).
- Clematis sense_chemical: C. microphylla gibberellic acid and nitrate (Lush et al. 1984, abstract, partial); C. vitalba nitrate (partial).
- Carpinus sense_chemical: C. caroliniana gibberellic acid (Woody Plant Seed Manual entry, citing Bretzloff and Pellet 1979); C. betulus methyl jasmonate branch induction (Volf et al., abstract, partial).
- Carpinus sense_light_nonvisual: C. betulus four light levels (Zhou et al. 2022, open PDF).
- Richardia sense_light_nonvisual: R. scabra continuous dark against light (Biswas et al. 1975 part I, abstract, partial).

## Search records (searched/desk-d6.jsonl, 8 lines)
Hamamelis sense_chemical; Apios diel, eye_type, sense_chemical, sense_light_nonvisual; Nothoscordum eye_type; Clematis eye_type; Sagittaria diel, eye_type; Richardia eye_type. Only the cells the harvest header lists as open (or, for genera in no harvest run, the queue's open traits without genus evidence on main) got a record.

## Wanted lines (wanted/desk-d6.jsonl, 4)
Richardia brasiliensis preanthesis cleistogamy 2024 (diel); Mediterranean Clematis floral traits 2022 (diel); Floral Volatiles from South American Alliaceae 2025 (Nothoscordum sense_chemical); Biswas et al. 1975 part II, chemical germination stimulants (Richardia scabra sense_chemical; no DOI found, authors blank, Cambridge page refused, so the desk may hold it).

## Skipped or short
- Cocculus: the harvest shows "error gave up" on three supplement queries (flower opening time, nyctinasty, volatile signalling), so desk-screen point 6 bars a search record. Searches found nothing new (germination, dormancy, anthesis, scent).
- Carpinus: no search record, since the closing evidence covers the only open cell.
- Apios and Sagittaria have no family review; `chased` uses the "none:" form with the reason.
- Fetch limits: ncbi/PMC, Cambridge abstract pages for part II, Crossref and doi.org links were refused (permission not answered), so Volf et al. and Lush et al. are partial and the Clematis S Afr J Bot and Richardia cleistogamy papers went to the wanted list.
- About 88 WebSearch calls used.

## Desk disposition after audit 96
Audit 96 failed the unit (1 of 10 search records, 0 of 8 evidence; 1 in 18, 5.6%). The desk dropped searched line 1 (Hamamelis sense_chemical; it missed Rehill and Schultz 2012, J Chem Ecol 38(5): 496-498, on tannin changes in aphid galls on living Hamamelis virginiana) and merged the other 9 search records and all 8 evidence records. Evidence line 3 quotes a Methods fragment where the abstract's nitrate sentence belongs; it needs a requote (not counted). Wanted lines: 3 filled from the registry (Crossref run 69); Biswas 1975 part II has no DOI or authors and stays held. Lead: Rehill and Schultz 2012 for Hamamelis.
