# Precision audit 35, 18 October 2026

Scope: the corrected records in `docs/views/evidence/recheck-42-fixed.jsonl` to `recheck-52-fixed.jsonl` (499 lines), in their latest versions. Records are named `recheck-N-fixed:LINE`. ALL.jsonl retracts 247 of these ids; each was replaced by its recheck-53 version (journal volume and issue) and, where one exists, by its recheck-54 version (grade m to g for group statements). `docs/views/fixes/requote-partial.jsonl` was applied as an override that sets `partial` to true. The worktree was cut from `research/repair-crossref`.

Draw: `random.seed(35)`, `random.sample` of positions in the 499 records (file order, then line order). Skipped: the Kott et al. 2010 records (recheck-46) and every record named in audits 33 and 34 (recheck-43:11, 43:13, 43:24, 43:28, 43:29, 43:59, 45:42, 47:61, 52:45, 48:6 and others). The first 20 usable records fall in seven files (43, 45, 47, 49, 50, 51, 52). Because errors were found, the next 15 usable positions in the same sample were checked; they add file 42.

Method as in audits 16 and 34: WebSearch on the title, then WebFetch on a page the search or the record returned. The fetch tool gives about 125 characters per quote, so each quote was read back in consecutive pieces. No library login, proxy, Sci-Hub, LibGen, academia.edu or ResearchGate page was opened, and no paper text is committed. A record whose paper would not open is `unverifiable`.

## First 20

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 1 | recheck-47-fixed:73 | Orgyia antiqua / acuity_cpd | i | confirm | eje.cz PDF p. 251, verbatim and complete; Table 1 gives 1.92 and 3.03 deg, and 0.2604 is 1/(2 x 1.92). Two authors, 104(2): 247-258 |
| 2 | recheck-45-fixed:73 | Nephrolepis cordifolia / chemical_exposure_response | m | error (journal) | Frontiers PDF, Conclusion: verbatim and complete; 15 and 21 days confirmed (Abstract). The source has no journal field at all (volume 11, article 566824 are missing). Seven authors match |
| 3 | recheck-50-fixed:43 | Pontella / eye_role | g | confirm | Cambridge PDF (Nilsson 2013): verbatim, leading ellipsis marks the cut; review, `partial` true; 30(1-2): 5-20 |
| 4 | recheck-43-fixed:47 | Pelodiscus sinensis / opsin_status | m | error (grade, journal) | quote verbatim (Whittier PDF), but it states the inactivating mutations for "all four crocodylian species and all four testudines"; table 1 lists clades, not Pelodiscus. A group statement, so `g`. Journal "34: 666-676" lacks the issue (34(3)) |
| 5 | recheck-50-fixed:41 | Echinoidea / sense_light_nonvisual | g | confirm | verbatim and complete (Nilsson 2013), including the citations |
| 6 | recheck-51-fixed:26 | Galium aparine / sense_light_nonvisual | m | confirm | GWCT page prints the abstract sentence verbatim (40 words); abstract only, `partial` true; 39(12): 1759-1764 |
| 7 | recheck-43-fixed:58 | Pisum sativum / sense_light_nonvisual | g | confirm | verbatim and complete (RERO PDF); Pisum and Vicia pooled, `g`; 61(4): 559-569 |
| 8 | recheck-45-fixed:48 | Caretta caretta / visual_field_area | m | confirm | verbatim and complete (bycatch-library copy of the ESR PDF, section 3.1); loggerheads only, n = 10; three authors; 41: 67-77. The sentence starts on p. 71 and ends on p. 72 where the record says pp. 72-73 (not counted) |
| 9 | recheck-47-fixed:14 | Macroglossum stellatarum / lambda_max_nm | g | confirm | verbatim and complete, p. 484; annual review, `partial` true; Table 1 lists 348, 430, 500 nm; 46(1): 471-510 |
| 10 | recheck-52-fixed:50 | Crotalus durissus / lambda_max_nm | g | confirm | verbatim with the marked cut; "In both species" and a predicted value taken from Bittencourt et al. 2019, so `g` is right; three authors; 15: 770804 |
| 11 | recheck-45-fixed:31 | Habrocestum africanum / opsin_localization | m | confirm | verbatim and complete (NSF copy, section 3.3, p. 9); seven authors; 217: 108367 |
| 12 | recheck-47-fixed:83 | Vaccinium angustifolium / chemical_exposure_response | g | confirm (note) | the Frontiers page prints the sentence as the record gives it (verbatim, section 3.3.2); it opens mid-citation ("Percival and MacKenzie, 2007) noted ...") because the page drops the opening bracket. Cited value, `g`; review, `partial` true. Not counted |
| 13 | recheck-47-fixed:62 | Anolis carolinensis / oil_droplets | m | error (grade) | quote verbatim with a marked opening cut (section 4.2, p. 8). The finding covers the three species of the study ("regardless of eye or species", A. carolinensis, A. cristatellus, A. sagrei), so `m` is wrong |
| 14 | recheck-50-fixed:45 | Sapphirina / eye_role | g | confirm | same sentence as #3 |
| 15 | recheck-51-fixed:25 | Opuntia ficus-indica / sense_light_nonvisual | m | error (journal, value) | MDPI section 2.6: quote verbatim with a marked cut. The quote supports the PAL increase only; the value also claims increased phenolic accumulation, which the quote does not state. The source has no journal field (Int J Mol Sci 20(21): 5327 missing) |
| 16 | recheck-52-fixed:31 | Meleagris gallopavo / oil_droplets | m | unverifiable | the abstract page (Europe PMC REST) was refused and PubMed did not open; searches returned other papers |
| 17 | recheck-50-fixed:68 | Deinopis spinosa / diel | m | confirm | verbatim and complete (UNL copy); "These creatures" follows the sentence naming D. spinosa; five authors; 30(24): 5033-5039 |
| 18 | recheck-49-fixed:30 | Corvus macrorhynchos / fovea | m | error (value) | Utsunomiya page: the quote ("two areas of highly populated ganglion cells") is verbatim with a marked cut, but it names neither area. The value "area centralis and dorsotemporal acute zone" comes from the abstract's earlier sentence ("highest density found in the area centralis ... and dorso-temporal part"). The journal field gives no volume or pages (a conference abstract with no printed pages) |
| 19 | recheck-50-fixed:71 | Otocolobus manul / tapetum | m | unverifiable | the quote is verbatim and the Pallas's cat has its own value ("blue-green"), but the Springer page hides part of the author list ("..."), BMC and Europe PMC would not open, so the six printed names could not be compared with the full list |
| 20 | recheck-50-fixed:26 | Deinopis / behaviour_vision | g | confirm | verbatim and complete, p. R979; Primer article, `partial` true; 30(17): R975-R980 |

First 20: 2 unverifiable, 18 verifiable, 5 errors (1 journal-only).

## Extension, 15 more

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 21 | recheck-52-fixed:26 | Deilephila elpenor / neural_summation_sensitivity_ratio | i | confirm | verbatim and complete (KOPS copy, p. 825); three authors; 26(6): 821-826 |
| 22 | recheck-52-fixed:32 | Meleagris gallopavo / oil_droplets | m | unverifiable | same paper and blocks as #16 |
| 23 | recheck-42-fixed:5 | Tetragona ziegleri / eye_type | g | confirm | verbatim and complete (Springer, Introduction); cites Land 1997, `g` |
| 24 | recheck-47-fixed:56 | Glycine max / sense_light_nonvisual | g | confirm | Frontiers page, soybean section; the sentence opens as quoted; review, `partial` true; the authors field prints surnames first ("Weller James L, Ortega Raúl"), a formatting slip not counted |
| 25 | recheck-42-fixed:6 | Tetragona ziegleri / eye_topography | g | confirm | verbatim and complete (Results, Eye morphology); the sentence speaks for all species studied, so `g` |
| 26 | recheck-50-fixed:28 | Drassodes cupreus / tapetum | g | confirm | verbatim and complete, p. R979; the sentence follows the one naming D. cupreus |
| 27 | recheck-47-fixed:46 | Fabaceae / photoreceptor_gene_count | g | confirm | verbatim, section Flowering Genes; legumes in general |
| 28 | recheck-50-fixed:33 | Cubozoa / eye_type | g | confirm | verbatim with the marked cut; the sentence goes on with polychaete and gastropod eyes |
| 29 | recheck-42-fixed:13 | Partamona orizabaensis / eye_type | g | confirm | same sentence as #23 |
| 30 | recheck-50-fixed:4 | Araneae / tapetum | g | confirm | verbatim and complete, p. R976 |
| 31 | recheck-47-fixed:47 | Pisum sativum / sense_light_nonvisual | g | confirm | verbatim (pea, Induced Mutants - Photoperiod Response) |
| 32 | recheck-43-fixed:6 | Chrysemys picta / opsin_status | m | error (grade, journal) | the sentence names two species ("Chrysemys picta and Chelonia mydas, possess all five visual opsins"), so `m` for one is wrong (`g`); it prints on p. 666, not 667; journal lacks the issue (34(3)) |
| 33 | recheck-42-fixed:12 | Trigona fulviventris / eye_topography | g | confirm | same sentence as #25 |
| 34 | recheck-45-fixed:22 | Menemerus bivittatus / opsin_localization | m | confirm | verbatim and complete (section 3.3, p. 8); seven authors |
| 35 | recheck-45-fixed:68 | Bos taurus / lambda_max_nm | g | unverifiable | the thesis page (digitalcommons.usu.edu/etd/4117) is Gilbert 1985, but its PDF link (article=5135) opens an unrelated paper on Rudbeckia in vitro regeneration, so the quote could not be found |

Extension: 2 unverifiable, 13 verifiable, 1 error.

## Error rate

- First 20: 5 errors in 18 verifiable records (27.8%).
- Both draws: **6 errors in 31 verifiable records, 19.4%** (4 of 35 unverifiable).
- Excluding the journal-only fault (recheck-45-fixed:73): **5 errors in 31, 16.1%**.
- The 5% threshold is not met on any counting.

## Distinct fault patterns

1. **Group statement graded `m`** (recheck-43-fixed:47, recheck-47-fixed:62, recheck-43-fixed:6). Each quote is verbatim, but it speaks for several species and the record gives one of them `m`. The recheck-54 pass did not reach them: 43:47 and 43:6 are testudine statements (two or eight species) and 47:62 says "regardless of eye or species".
2. **Journal field missing or without the issue** (recheck-45-fixed:73 and 51-fixed:25 have no journal at all; 43:47 and 43:6 lack the issue, 34(3)). Recheck-53 covered only the retracted ids, so records that stood without a journal field or with a bare "34: 666-676" were not repaired.
3. **Value broader than the quote** (recheck-49-fixed:30, recheck-51-fixed:25). The quote supports part of the value; the rest comes from another sentence or an unquoted result.
4. Noted, not counted: a quote that opens mid-citation because the page lost a bracket (47:83); surname-first author strings (47:56 and its Weller and Ortega siblings); page numbers off by one (45:48, 43:6).

## Blocked pages

- pmc.ncbi.nlm.nih.gov (PMC7511530 and the Europe PMC REST pages), the BMC article page, PubMed, and the avesis page: permission step not answered or URL too long.
- The Gilbert thesis PDF opens a different document (see #35).
- Hart et al. 1999 and Klećkowska-Nawrot et al. 2026 could not be checked on an opened page.

No evidence file was edited and no correction rows were written.
