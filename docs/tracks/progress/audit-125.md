# Audit 125: desk-d35 (24 plant genera; branch origin/research/desk-d35, head ae1c531c)

Work in progress; sections are filled as checks finish.

## Gate
`screen_candidates.py --check` on the 24-line searched file with the 8-line wanted file prints "0 problems".

## Queries
A script compared each record's unprefixed `queries` with the `query` and `family review` lines `harvest_get.py` prints. All 14 harvested genera match word for word and in order, and none shows "gave up". The 10 genera in no harvest run list "web: " lines only.

## Interim findings (to be tabled)
- Evidence 1 to 4: quotes verbatim on AGRIS, npj.uwpress.org, ruj.uj.edu.pl and AGRIS pages; POWO: Hepatica nobilis var. asiatica is a synonym of Hepatica asiatica; Hypopitys monotropa is a synonym of Monotropa hypopitys.
- Chased: both pooled family searches return nutrition-evidence.com 249643 (Li and Mathews 2016, J Plant Res 129(2): 115-22, 10.1007/s10265-016-0785-4).
- Errors so far: line 3 Gleditsia light (Tognetti et al. 2019 AoB 124(2): 307-318, dark-light and R:FR germination); line 5 Hylocomium chemical (Bay et al. 2013 New Phytol 10.1111/nph.12403); line 7 Dasiphora diel (Denisow, Antoń, Szymczak 2013 J Apic Sci 57(1): 95-106, morning opening by 8.00 h); line 8 Ampelopsis light (Frampton, Valencia, Zimmerman 2018, three light levels); line 9 Phleum chemical (Bender 2021 Agraarteadus 32(1): 17-24, Moddus growth regulator).
