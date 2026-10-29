# audit-160: desk-d70 (2 evidence records, no search records, no wanted lines)

Audited 29 October 2026 from the desk-d70 files copied untracked into the worktree (progress note and 2 evidence lines; neither is committed here). Sources checked on publisher, indexer and POWO pages reached through the records' own URLs or WebSearch results; 1 WebSearch used. Duplicates: git grep on origin/main (863737ca) finds neither DOI (10.1093/aob/mcj045, 10.2503/hortj.SZD-065) and no evidence for Marginatocereus or Basella in docs/views/evidence. The only hit is search record sweep-27 line 35 (Rivina), whose `chased` field says it opened Masuda et al. 2025 while looking for Rivina; that is a search note about another genus and files no Basella evidence, so line 2 neither repeats nor contradicts it.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Marginatocereus marginatus | OK | agris record (opened) prints Dar, S.; Arizmendi, Ma. del C.; Valiente-Banuet, A. in order, Annals of Botany 97(3): 423-427, 2006, title and DOI as filed; scilit (opened) agrees on volume, issue, pages and DOI. The quote is verbatim on both, a whole Key Results sentence of 94 characters reporting the study's own finding of nocturnal and diurnal anthesis for the named species. The Methods sentence on marked buds followed for phenology and anthesis time, the exclusion experiment and the Tehuacan Valley setting are all in the abstract, so method and conditions hold, and the conditions say honestly that no clock times are given. Flower opening timing is the owner's plant diel reading. POWO 153112-2 (opened) "This species is accepted" for Marginatocereus marginatus (DC.) Backeb., a species. Grade m and partial true are right for one named species read from the abstract |
| 2 | Basella alba | OK (fault noted) | J-STAGE article page (opened) prints Masuda, Takamatsu, Hiramatsu, Ozaki, Kim, Sakai, Tomiyoshi in order, The Horticulture Journal 94(4): 483-490, 2025, DOI 10.2503/hortj.SZD-065, title as filed. The quote is verbatim, a whole sentence of 86 characters with a direction for each light quality, and the sentence before it says the R and FR effect was clarified "in both species", so the result covers B. alba itself. POWO 164286-1 (opened) "This species is accepted" for Basella alba L. and lists Basella rubra L. as a heterotypic synonym, so the study's two taxa are one accepted species and grade m holds. The abstract confirms scarification, temperature (25 C optimum in darkness) and white-light trials, and gives no scarification state, fluence or temperature for the R and FR trial, as the conditions say. Germination red/far-red trial under sense_light_nonvisual |

Errors: 0 of 2 (0%). Error lines: none.

Pooled with audits 157 to 159: 1 of 13 evidence records (7.7%; audit 157 1 of 3, audit 158 0 of 5, audit 159 0 of 3, audit 160 0 of 2).

Verdict: pass. Both lines can be merged.

Unconfirmed names: none. Both cited POWO ids were opened by this audit and belong to the accepted species itself.

Faults noted, not counted:
- Line 2: "a far-red pulse after red light cancelled red's effect" in conditions uses the word "pulse", which the abstract does not print; the abstract reports far-red given after red reversing red's promotion and a final FR after R/FR/R cancelling it, and one sentence speaks of far-red irradiation "for four days", so the duration of the far-red treatment is not shown to be a pulse. "cancelled" itself is supported.
- Line 2: the value leaves out that seeds also germinated in darkness; that sentence belongs to the white-light trial, so it is no omitted exception for the R and FR result.
- Line 1: "wild plants" in conditions is not printed in the parts of the abstract this audit could read; the field study in the Tehuacan Valley makes it likely.

Blocked: academic.oup.com/aob/article-abstract/97/3/423/291885 (provenance refusal after the doi.org redirect; agris and scilit read instead); pmc.ncbi.nlm.nih.gov/articles/PMC2803642 (reCAPTCHA page). No library proxy, ResearchGate, academia.edu or Sci-Hub page opened; zendy.io search results were left alone.

Stray files: none committed; the two desk-d70 copies stay untracked.
