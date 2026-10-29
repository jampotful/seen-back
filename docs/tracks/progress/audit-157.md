# audit-157: desk-d67 (3 evidence records, no search records, 3 wanted lines)

Audited 29 October 2026 against origin/research/desk-d67 (merge-base diff: progress note, 3 evidence lines, 3 wanted lines; no stray files; the desk-d67.jsonl and wanted-d67.jsonl copies in the worktree root are untracked and not committed). About 9 WebSearches used. Duplicates: none of the three taxa or DOIs appears in docs/views/evidence/*.jsonl on main.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Thuja plicata | ERROR | Not a set-light trial: title and abstract describe "field-planted" seedlings responding to "ambient light levels" "under field conditions" (zhenzhi, sciencegate, isc.ac records), i.e. a field light-gradient study, which does not count for sense_light_nonvisual. Otherwise the quote is verbatim (zhenzhi), 103 chars; authors Coates KD, Burton PJ in order; CJFR 1999, pp. 1374-1382; volume 29(9) only inferred from the DOI cjfr-29-9-1374 (no page printed volume or issue); publisher page not reached. POWO 60443333-2 accepted |
| 2 | Gaultheria shallon | OK | Messier C (sole author), Can J Bot 70(11): 2271-2276, 1992, DOI 10.1139/b92-282 (zhenzhi); title verbatim (pestinfo prints it in sentence case, zhenzhi in capitals with "GAULTHERIA-SHALLON"); quote verbatim, 96 chars; set neutral-shade treatments 100/30/10/5% full sunlight; "5 times as much total dry weight in 100% as in 5%" supports the value. POWO 317388-2 accepted |
| 3 | Lonicera maackii | OK (fault noted) | Lieurance D, Cipollini D in order, Ann Bot 112(4): 741-749, 2013, title verbatim, DOI (Penn State Pure, Wright State CORE); quote verbatim on Pure, 108 chars; experiment 1 set high and low light crossed with nitrogen. POWO 60463205-2 accepted |

Errors: 1 of 3 (33%). Error line: 1.

Unconfirmed names: none. All three POWO ids opened by this audit and each is the accepted name itself ("This species is accepted").

Faults noted, not counted:
- Line 3: the value's parenthesis "(low light crossed with low nitrogen)" narrows "resource limitations" (light and soil fertility, each varied) to the combined treatment; the quote pools light with nitrogen, so it does not isolate a light response. Method's "caterpillar damage" belongs to experiment 2, which varied nutrients and damage, not light.
- Line 1: volume 29 and issue 9 are not printed on any page reached (inferred from a DOI string); "conditions" omits that light was ambient.
- Line 2: the note's "no author initials beyond C. Messier" is right; title case is the desk's normalisation.

Wanted lines:
- 1 Jatropha curcas: OK. DOAJ prints six authors in this order: Manuel Rincón-Rabanales, Laura I. Vargas-López, Lourdes Adriano-Anaya, Alfredo Vázquez-Ovando, Miguel Salvador-Figueroa, Isidro Ovando-Medina; PeerJ page prints the title, PeerJ 4: e1819, 2016, DOI 10.7717/peerj.1819 (DOAJ: March 2016).
- 2 Stevia rebaudiana: OK. doi.org 10.5539/ijb.v3n4p83 redirects to ccsenet article 11244 (the redirect target was then refused by the fetcher); search result for the DOI carries the title. IIUM repository prints Abdullateef, Raji Akintunde and Osman, Mohamad (two authors, in that order), 2011, Int J Biol 3(4): 83-91.
- 3 Eucalyptus: FAULT (year). CSIRO page prints five authors in order (Ruiz-Talonia, Carr, Smith, Whalley, Reid), 66(8): 657-666, DOI, submitted 31 May 2018, accepted 10 January 2019, published 14 February 2019; no issue date. CSIRO's own ExportCitation prints "(2018) ... Australian Journal of Botany 66, 657-666"; the connectsci PDF prints "Aust J Bot (2019) 66 (8)" and copyright 2018. Volume 66 is the 2018 volume; the citation should carry 2018 (the publisher's export, volume year), with online 14 February 2019 noted. The desk's change from 2018 to 2019 should be reverted.

Blocked: doi.org/10.1139/x99-091 and doi.org/10.1139/b92-282 (provenance refusal, so CJFR and CJB publisher pages unread); ccsenet article 11244. No library proxy, ResearchGate, academia.edu or Sci-Hub page opened.

Stray files: none.
