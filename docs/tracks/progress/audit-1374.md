# audit-1374: desk-d673, evidence line 1

Audited 4 November 2026 from the desk-d673 files present untracked in the worktree (docs/tracks/progress/desk-d673.md and docs/views/evidence/desk-d673.jsonl, 1 line; neither edited nor committed). HEAD equals origin/main (b05da1259). `python3 -I tools/senses/check.py --require-evidence-kind docs/views/evidence/desk-d673.jsonl`: 1 record, 0 problems. Field shape follows the diel rows on main (Crotalus atrox, Liolaemus nigroviridis, desk-d665).

Sources opened (WebFetch, URLs from my own WebSearch results only): reptile-database.reptarium.cz/Phymaturus/williamsi; www.scielo.br/j/aabc/a/WbPpDfpLWV3b8cJsdCW37Bc/ (four passes: metadata and licence, Results paragraph, Methods, Figure 3 caption and Table IV). No Crossref, PMC, Plazi, zenodo, proxy, ResearchGate or academia.edu page opened. 2 WebSearches. Points marked "(tool summary)" were not returned verbatim.

## Bibliographic and licence

Page prints "An. Acad. Bras. Ciênc. 96 (1) • 2024", first page e20191190, DOI https://doi.org/10.1590/0001-3765202320191190; byline ALEJANDRO LASPIUR, MARLIN MEDINA, MARÍA SOLEDAD AUSAS, JUAN CARLOS ACOSTA, JOHN D. KRENZ, NORA RUTH IBARGÜENGOYTÍA, matching "Laspiur A, Medina M, Ausas MS, Acosta JC, Krenz JD, Ibargüengoytía NR". Year 2024 is the printed year (DOI string 2023 ignored). Title verbatim. Licence sentence on the scielo.br page: "This is an open-access article distributed under the terms of the Creative Commons Attribution License", as filed. No Crossref claim in the note. Bibliographic faults 0; licence faults 0.

## Name

Reptile Database: Phymaturus williamsi LOBO, LASPIUR & ACOSTA 2013; higher taxa "Liolaemidae, Iguania, Sauria, Squamata"; type locality "Quebrada vallecito, 40 km W of Calingasta town"; Comment: "Abundance: apparently only known from 2 localities (Valdez-Ovallez et al. 2025)." No split or synonymy. Study site is the type locality. Names faults 0.

## Duplicates

grep under docs/ for "Phymaturus williamsi": desk-d261 evidence (sense_thermal, 10.3390/biology15090729, Quebrada La Puerta), desk-d261.md, desk-d278.md, audit-357.md, desk-queue.md; all the other paper. grep for "20191190" / the DOI: only the desk-d673 files. Not a repeat. Duplicate faults 0.

## Line 1, Phymaturus williamsi, diel "bimodal (most active individuals late morning and afternoon)"

Quote: Results > Periods of activity > Quebrada Vallecito: "P. williamsi showed a bimodal pattern of activity with the most active individuals during late morning (12:00 – 14:00 h) and afternoon (15:00 – 18:00 h; Figure 3c)." It follows "...Table IV)." so it starts at the real sentence start; whole sentence, no cut, within 40 words. **Quote MATCH.** 'Bimodal' is the paper's own category for the daily activity pattern, and the value says no more than the quote. Capture-time distributions are what the paper uses as its activity measure (Methods: "Time of day at capture was also recorded."; Figure 3: "Grey bars are the mean number of active lizards per hour."), so the diel category is the paper's as stated.

Conditions checked: months (October 2008, December 2008, April 2009) and the 10:00-19:00 h window confirmed ("All specimens were caught by hand or noose between 10:00 and 19:00 h"); pooling across months not stated (the contingency table combines "frequencies calculated for each population (N = 4), and for each activity period (N = 8...)"); N = 84 (27 males, 40 females, 17 juveniles) confirmed; hourly n not printed in the text, Table IV read only to 12:00-13:00 (P. williamsi 0, 14, 25); fewer than expected at 13:00-14:00 and L. parvus unimodal confirmed.

Faults:
1. Sample composition (counted). The lizards were not released: "All individuals were collected under permits ..." and "After laboratory experiments, the captured specimens were euthanized ... and deposited into the herpetological collection". The record says nothing about the specimens' fate. The activity data are field capture times, so the captive rule does not remove the record, but the brief's wild-and-released question answers "wild-caught, collected", which the conditions must say. Fixable.
2. Location (counted with 1 as one record error). `where` "Results, Quebrada Vallecito" drops the printed subheading "Periods of activity". Fixable.
3. Not counted: the conditions gave "chi-square P < 0.0001"; the page prints χ2 (21) = 13.06 and "Multiple comparison, z = -3.61, P < 0.0001", so the P belongs to the multiple comparison. Corrected. Added that the 13:00-14:00 low lies inside the quoted 'late morning (12:00-14:00 h)' window, and that sampling excluded night and early morning.

**Line 1 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Phymaturus williamsi, diel bimodal | FIXABLE | where, method, conditions, note | lizards collected and euthanized, not released, unstated; heading path missed "Periods of activity"; chi-square/z statistic misattributed |

Errors 1 of 1 audited record (100%). By kind: quotes 0; location 1 (folded into the record error); value meaning 0; omitted variation 0; sample composition 1; bibliographic 0; licence 0; names 0; trait key 0; duplicates 0. Fixable; nothing dropped, nothing held out. Verdict: merge line 1 with the Replacement applied.

Unchecked: Table IV rows after 13:00 and Figure 3 not viewed, so the hourly n is not confirmed; whether the 50 non-laboratory captures were also euthanized is not stated on the page.

## Replacement

Validated with check.py --require-evidence-kind on a scratch copy: 1 record, 0 problems.

```json
{"taxon": "Phymaturus williamsi", "rank": "species", "family": "Liolaemidae", "order": "Squamata", "class": "Reptilia", "trait": "diel", "value": "bimodal (most active individuals late morning and afternoon)", "units": "", "eye": "", "method": "hourly frequency of active lizards from the recorded time of capture of free-living lizards caught by hand or noose between 10:00 and 19:00 h (no separate activity survey described); Pearson chi-square on hourly frequencies with multiple comparisons (Table IV)", "conditions": "Free-living lizards at Quebrada Vallecito (Calingasta Department, San Juan Province, Argentina; type locality of the species), captured in October 2008, December 2008 and April 2009; the paper does not say whether the three months were pooled for the hourly pattern (the contingency table combines frequencies per population and activity period). 84 P. williamsi were captured at the site (27 males, 40 females, 17 juveniles); the n used in the hourly analysis is not stated in the text read (Table IV, read only to 13:00, gives 0, 14 and 25 for 10:00-11:00, 11:00-12:00 and 12:00-13:00 h). Activity was inferred from the times lizards were caught active, not from continuous observation, and sampling ran only 10:00-19:00 h (no night or early-morning sampling). Lizards were not released: 'All individuals were collected' under permit, and after the laboratory experiments 'the captured specimens were euthanized' and deposited in a collection; the activity times are field capture times, so not a captive record. The same paragraph reports activity over 7 hours (11:00-18:00 h) with fewer lizards than expected at 13:00-14:00 h (chi-square 13.06, df 21; multiple comparison z = -3.61, P < 0.0001), inside the 'late morning (12:00-14:00 h)' window of the quoted sentence; the syntopic Liolaemus parvus at the same site was unimodal. The paper also measured preferred body temperature in a laboratory gradient, which is not part of this record.", "source": {"authors": "Laspiur A, Medina M, Ausas MS, Acosta JC, Krenz JD, Ibargüengoytía NR", "year": 2024, "title": "Thermal niches and activity periods in syntopic Phymaturus and Liolaemus lizards from the Andes, Argentina", "journal": "Anais da Academia Brasileira de Ciências 96(1): e20191190", "doi": "10.1590/0001-3765202320191190", "url": "https://www.scielo.br/j/aabc/a/WbPpDfpLWV3b8cJsdCW37Bc/", "access": "open"}, "where": "Results, Periods of activity, Quebrada Vallecito", "quote": "P. williamsi showed a bimodal pattern of activity with the most active individuals during late morning (12:00 – 14:00 h) and afternoon (15:00 – 18:00 h; Figure 3c).", "grade": "m", "opened": true, "note": "Reptile Database species page for Phymaturus williamsi opened from own search results (Liolaemidae, Squamata; type locality Quebrada Vallecito, San Juan; its comment notes only abundance, no split or synonymy). Licence sentence read on the SciELO page: 'This is an open-access article distributed under the terms of the Creative Commons Attribution License'. Page prints An. Acad. Bras. Cienc. 96 (1), 2024, e20191190 and DOI 10.1590/0001-3765202320191190; the printed year 2024 is filed. Category word 'bimodal' is the paper's. Phymaturus williamsi is on main only under sense_thermal from a different paper (10.3390/biology15090729); this DOI is not on main. Reached by WebSearch 'Phymaturus lizard daily activity cycle thermal ecology Andes unimodal Revista Chilena de Historia Natural OR Herpetozoa OR PeerJ' (scielo.br result).", "unit": "desk-d673"}
```
