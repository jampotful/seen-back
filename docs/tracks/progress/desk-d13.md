# desk-d13 (plant genera: Cortaderia, Nasturtium, Tecoma, Cosmos, Achillea, Apocynum, Marchantia, Vachellia, Poa)

About 55 WebSearch calls. eye_type was not searched: main holds 27 October eye_type records (desk-c11, desk-d1) for all nine genera. WebFetch of URLs that no search had returned was refused (provenance), so every page opened came from a search result.

## Evidence logged (10, all in docs/views/evidence/desk-d13.jsonl)
- Cortaderia selloana sense_chemical (Sellmer et al. 2001, growth-retardant drenches, abstract).
- Nasturtium officinale sense_chemical (Klimek-Szczykutowicz et al. 2022, elicitors on in vitro microshoots; abstract).
- Cosmos bipinnatus sense_chemical (Yu et al. 2024, methyl jasmonate; abstract).
- Achillea millefolium sense_light_nonvisual (Lima et al. 2020, shading nets; abstract); Achillea collina sense_chemical (Giorgi et al. 2015, aphid and jasmonic acid volatiles; abstract; A. collina accepted per WFO).
- Apocynum cannabinum sense_light_nonvisual (Huebner 2026, high versus low light germination); Apocynum androsaemifolium sense_light_nonvisual (Boyd and Hughes, abstract).
- Vachellia karroo diel (Robbertse et al. 2014, flowers open in the morning, full text from the UP repository); Vachellia farnesiana sense_light_nonvisual (Chauhan et al. 2021, abstract).
- Poa bulbosa sense_chemical (Ofir and Kigel 1998, applied ABA; abstract).

## Search records (4, docs/views/searched/desk-d13.jsonl): diel for Cortaderia, Nasturtium, Cosmos, Achillea. 

## Wanted lines: 0 (empty file). Every lead I could not open is already on main's wanted lists.

## Cells left open because an unread lead on main keeps the null out (desk-screen point 3)
- Tecoma sense_chemical: harvest-c11 lead "Effect of certain phytohormones on seed germination ... Tecoma stans" (no URL surfaced in four searches).
- Apocynum diel (W2384640753, "A Preliminary Study on Pollination Biology of Apocynum venetum", 2007; Chen et al. 2015 opened, no hour) and Apocynum sense_chemical (SA germination of A. venetum, 10.1007/s44372-026-00880-x; not surfaced).
- Vachellia sense_chemical: somatic embryogenesis lead 10.1007/s44415-025-00064-7 (not surfaced; tissue culture).
- Poa diel: desk-d1 lead on Poa annua anthesis (Holcus, Festuca, Poa annua); the archive.org biostor-137766 PDF it points to was refused by the fetcher.
- Marchantia diel: not re-searched; desk-d1 already holds a null record (liverwort, no flowers; circadian photosynthesis papers are not opening or scent timing).

## Notes
- Newman et al. 1990/1992 (watercress glucosinolate defence against amphipods) were not logged: damage-activated tissue chemistry, not a cue response.
- Nasturtium GA3/light germination (Latakia University Journal, no DOI; quote could not be assembled from Arabic abstract) not logged; the cell is closed by Klimek-Szczykutowicz.
- Huebner 2026 also shows reduced germination on woodpile soil (Ailanthus); not logged under sense_chemical.

## Desk disposition after audit 103

Audit 103 judged the whole unit and found 4 errors (28.6%): search lines 2 (Nasturtium) and 3 (Cosmos), whose `chased` DOI no family-review search supports, and evidence lines 5 (Achillea collina, repeats desk-c11:3 on main) and 9 (Vachellia farnesiana, repeats desk-d1:2). Those four lines are dropped and the other 2 search and 8 evidence records are merged. The Marchantia diel null the unit relied on is sweep-29:24 on main, not desk-d1. The Nasturtium and Cosmos diel cells return to the queue.
