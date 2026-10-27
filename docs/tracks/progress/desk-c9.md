# desk-c9: plant genera screen, first half of batch c9 (27 October 2026, branch research/desk-c9)

Worktree /tmp/dc9. Launch list of 19 genera: Asclepias, Erigeron, Colocasia, Solanum, Heterotheca, Prunus, Lamium, Osmunda, Sisyrinchium, Melia, Catharanthus, Antigonon, Ostrya, Mirabilis, Vicia, Diodia, Nymphaea, Polygonatum, Cornus.

## Genera done (11)
Asclepias, Erigeron, Colocasia, Heterotheca, Prunus, Melia, Mirabilis, Nymphaea, Polygonatum.
No open cell: Solanum, Lamium, Cornus (harvest_get.py prints empty "open traits"; nothing written).

## Not finished (budget)
Osmunda, Sisyrinchium, Catharanthus, Antigonon, Ostrya, Diodia: no searches run.
Vicia: skipped, its first harvest query ("Vicia phytochrome photoreceptor") shows "error gave up" (desk-screen point 6).

## Cells closed by a measurement: 18 evidence records in docs/views/evidence/desk-c9.jsonl (all abstract-level, partial)
- Asclepias sense_chemical: A. curassavica and A. incarnata (aphid-induced volatiles, Meier and Hunter dataset), A. syriaca (herbivore-induced resistance and jasmonate signalling, Agrawal et al. 2014).
- Erigeron: sense_light_nonvisual (E. speciosus, E. canadensis, E. bonariensis, E. canadensis again from Vidal 2007); sense_chemical (E. canadensis, nutrient ions, Follmer et al. 2021: FORK, see below).
- Colocasia esculenta: sense_chemical (GA3 flowering), sense_light_nonvisual (shade levels).
- Melia azedarach: diel (anthesis 08:00 to 10:00).
- Mirabilis jalapa: sense_chemical (GA3 germination).
- Nymphaea: sense_light_nonvisual (N. minuta LED trial; N. alba light and dark), sense_chemical (N. alba growth-regulator media).
- Polygonatum: sense_chemical (P. odoratum GA3), sense_light_nonvisual (P. cyrtonema and P. sibiricum light quality; P. cyrtonema shade levels).
- Prunus: diel (P. cerasoides), sense_light_nonvisual (P. sellowii, P. avium), sense_chemical (P. spachiana GA3).

## Search records: 11 lines in docs/views/searched/desk-c9.jsonl
Erigeron diel and eye_type; Colocasia diel and eye_type; Heterotheca sense_chemical; Prunus eye_type; Mirabilis eye_type; Nymphaea eye_type; Melia eye_type; Polygonatum diel and eye_type. Harvest queries copied word for word, then every web search run, labelled "web: ". Heterotheca light/diel/eye are not open. No record for Mirabilis or Melia sense_light_nonvisual (wanted instead).

## Wanted lines: 5 (docs/views/wanted/desk-c9.jsonl)
Erigeron canadensis auxin-herbicide transcriptomics (10.1093/jxb/eraa124); Erschbamer et al. 2010 on E. uniflorus in light and dark (no DOI, authors read); Melia volkensii light and cytokinin (10.3390/plants15020322); Mirabilis jalapa lighting trial (10.56013/bio.v14i1.3530); Tyagi et al. 2004 taro germination (10.1071/SP04007).

## Forks and limits to know
- Follmer et al. 2021 (Conyza canadensis germination in P, K, Ca, Mg nutrient solutions): dissolved ions are neither hormone, elicitor nor volatile. Logged under sense_chemical with the fork named in the note; the desk may drop the line.
- Erigeron canadensis/bonariensis are logged under their accepted names; the sources print Conyza (the pestinfo records list the same species as Erigeron).
- Nymphaea minuta is the name the source prints; not checked against an accepted list. The genus is right.
- Hanik et al. 2024 (Mirabilis jalapa field note on opening) was opened and is not a light trial; the diel cell is not open for Mirabilis.
- OpenAlex (api.openalex.org) returned a proxy 403 for the whole environment; no live query. WebFetch worked only on URLs a search had returned; the OUP, MDPI, Cambridge (redirect) and PMC (reCAPTCHA) pages were refused or blocked and are not read. The Cambridge Weed Science camphorweed germination paper has no DOI in any tool output, so it is not on the wanted list.
- Quotes come from WebFetch page summaries asked for verbatim text; quotecheck has not been run against the papers.
- Citation step: harvest DOIs where the output prints them (Erigeron, Heterotheca, Mirabilis); Colocasia has no relative and its family search found no Araceae review; Prunus, Nymphaea, Melia and Polygonatum name a family-search result that is not a family review (weak).
