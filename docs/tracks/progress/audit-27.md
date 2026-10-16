# Precision audit 27, 16 October 2026

Scope: twenty records graded `m` that no earlier audit table, recheck file or retract row of `docs/views/audit/ALL.jsonl` had touched, all vertebrates and no insects: ten mammals (five of them canids), five birds and five squamates. They come from eleven evidence files (mammals-met, canon-5, herps-met, intake-4, intake-5, intake-6, intake-7, intake-8, oa-5, sweep-47 and sweep-58). Because more than one record was in error, twelve more were checked from the same files (oa-5, canon-5, mammals-met and sweep-58); they are listed separately and do not enter the rate.

Method as in audit 26, with the focus moved to the quote, the value and units, the grade, the partial flag, the method and the setup. Bibliographic faults are noted only where they were met in passing, since a Crossref pass is filling volumes and accents in bulk. Publisher pages, Frontiers, Wiley, figshare, the eLife XML on GitHub and the Maryland repository all asked for a permission step that was not answered, and Europe PMC was refused by the network proxy, so every reading came from the OpenAlex work record (abstract rebuilt from its inverted index) or from the Zenodo copy of the Caves et al. 2024 dataset. No web searches were run, because the session's search budget was spent. A change to the partial flag, the grade, the method, the setup or the `where` field counts as `correct`. A record read from the abstract alone (access `abstract` or `closed`, quote from the abstract) without a partial flag counts as an error, as in audit 26. Corrections are in `docs/views/recheck/recheck-27.jsonl`. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| mammals-met:15 | Meriones unguiculatus / fovea | m | correct | OpenAlex: quote verbatim after "Introduction:"; raised cone density in the streak confirmed. Method was empty and the abstract-only record had no partial flag. Both corrected |
| mammals-met:6 | Equus caballus / fovea | m | correct | OpenAlex: sentence verbatim; 30 horses of several breeds. Abstract-only record without a partial flag. Set true |
| mammals-met:14 | Cavia porcellus / fovea | m | correct | OpenAlex: sentence verbatim, but under Results where the record says Conclusion. Method "anatomical" filled from the abstract (histology of retinal whole mounts); partial set true |
| canon-5:17 | Aptenodytes patagonicus / acuity_cpd 20.4 | m | correct | Zenodo CSV: row 9 gives 20.4, RGC Density, as logged. The dataset compiles literature values and names no source per row; partial set true and the gap noted |
| canon-5:69 | Cyanocitta cristata / acuity_cpd 18.75 | m | correct | Zenodo CSV: 18.75 as logged. Same fault as canon-5:17 |
| herps-met:35 | Trachylepis quinquetaeniata / eye_type | m | confirm | OpenAlex: "The photoreceptor layer of the retina had cones only." verbatim; single and double cones and oil droplets confirmed; light and transmission electron microscopy |
| herps-met:36 | Pituophis melanoleucus / receptor_classes | m | confirm | OpenAlex: phrase verbatim after "We found that"; all-cone retina, immunohistochemistry and in vitro expression named |
| intake-4:12 | Vulpes lagopus / receptor_classes 2 | m | correct | OpenAlex: phrase verbatim and stated for both foxes. Abstract-only, no partial flag. Set true. The three retinae of the conditions field are not in the abstract |
| intake-4:17 | Vulpes vulpes / fovea | m | correct | OpenAlex: phrase verbatim. Abstract-only, no partial flag. Set true |
| intake-4:18 | Vulpes lagopus / fovea | m | correct | OpenAlex: phrase verbatim. Abstract-only, no partial flag. Set true |
| intake-5:35 | Giraffa camelopardalis / rgc_peak_density 14271 | m | correct | OpenAlex: verbatim with the superscript stored as "mm(2)". Abstract-only, no partial flag. The retina count and range in the method are not in the abstract and were not checked |
| intake-6:22 | Struthio camelus / sws1_type | m | correct | OpenAlex: phrase verbatim. The VS half of the value is earlier spectrometry the abstract does not name; partial set true, probable primary source named as unopened. Ödeen and Håstad had lost their accents |
| intake-6:25 | Paroedura pictus / fovea | m | correct | OpenAlex holds no abstract, so the quote was not seen. The quote and note themselves state a group finding for nocturnal geckos; grade set g. Röll had lost the umlaut |
| intake-7:10 | Mus musculus / lambda_max_nm 360 | m | confirm | OpenAlex: phrase present with "lambda max" spelled out, which is the index's rendering of λ. The value is cited from an unnamed earlier study; the record is already partial and says so |
| intake-7:23 | Tiliqua rugosa / rgc_peak_density 15500 | m | unverifiable | OpenAlex holds no abstract; the Springer page was not tried for want of permission |
| intake-8:2 | Asio flammeus / opsin_transcripts | m | unverifiable | OpenAlex holds no abstract; the Elsevier page was not reachable |
| oa-5:1 | Canis familiaris / lambda_max_nm 555 | m | correct | OpenAlex: sentence verbatim. The 555 nm figure is given once for four canid genera with no dog value; grade set g |
| oa-5:9 | Canis familiaris / lambda_max_nm 508 | m | confirm | OpenAlex: the abstract gives "the dog rod pigment at about 508 nm", a value for the dog alone |
| sweep-47:7 | Circaetus gallicus / binocular_deg 20 | m | confirm | OpenAlex: "maximum width of 20 degrees occurs approximately 15 degrees below the horizontal"; the index spells out the degree signs that the logged repository page printed. Alert restrained birds, ophthalmoscopic reflex technique |
| sweep-58:5 | Ctenophorus decresii / fovea | m | correct | OpenAlex: sentence verbatim and applied to each of six named species, so m stands. The method said counting details were absent, but the abstract names design-based stereology. Corrected |

**Rate: 13 errors in 20 records, 65%**, with 2 unverifiable; among the 18 records that could be checked the rate is 72%. By verdict: 13 correct, 0 requote, 0 retract; 5 confirm; 2 unverifiable. Every quote that could be seen was verbatim.

## Further records from the same files

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| oa-5:2 | Canis familiaris / lambda_max_nm 430-435 | m | correct | Pooled across four genera, as oa-5:1; grade set g |
| oa-5:3 | Urocyon littoralis / lambda_max_nm 555 | m | correct | Same |
| oa-5:4 | Urocyon littoralis / lambda_max_nm 430-435 | m | correct | Same |
| oa-5:6 | Vulpes vulpes / lambda_max_nm 430-435 | m | correct | Same |
| oa-5:7 | Alopex lagopus / lambda_max_nm 555 | m | correct | Same |
| oa-5:8 | Alopex lagopus / lambda_max_nm 430-435 | m | correct | Same |
| canon-5:1 | Acanthiza chrysorrhoa / acuity_cpd 9.12 | m | correct | Zenodo CSV: 9.12, RGC Density. Compiled value without partial flag |
| canon-5:3 | Alauda arvensis / acuity_cpd 11.4 | m | correct | Zenodo CSV: 11.4, Behavior. Same fault |
| canon-5:5 | Alectoris chukar / acuity_cpd 11.7 | m | correct | Zenodo CSV: 11.7, RGC Density. Same fault |
| mammals-met:4 | Ovis aries / depth_cue | m | correct | OpenAlex: sentence verbatim; 18 female sheep, "very low hyperopia". Abstract-only, no partial flag |
| mammals-met:5 | Ovis aries / binocular_deg | m | correct | OpenAlex: sentence verbatim; 10 further sheep. Abstract-only, no partial flag |
| sweep-58:6 | Ctenophorus gibba / fovea | m | correct | Same abstract and same method fault as sweep-58:5 |

All twelve were wrong. Every canon-5 row read so far lacks the partial flag, and every lambda row of oa-5 drawn from the Jacobs et al. 1993 sentence carries a pooled value at `m`; both files probably need the same fix applied throughout.

## Checks

- **Most common fault: a missing partial flag.** Ten of the thirteen errors in the sample (mammals-met:15, mammals-met:6, mammals-met:14, canon-5:17, canon-5:69, intake-4:12, intake-4:17, intake-4:18, intake-5:35, intake-6:22) and seven of the further twelve are records that were read from an abstract or copied from a compilation and carry no partial flag. The intake and mammals-met files were written before the flag was asked for, and the canon-5 file treats a compiled dataset row as a direct reading. A script could set the flag on every record whose access is `abstract` or `closed` and whose `where` names the abstract, which would clear most of this without reading.
- **Grade.** Two records stated a group finding at `m`: oa-5:1 (one figure for four canid genera, and six siblings in the further set) and intake-6:25 (nocturnal geckos as a group). sweep-58:5 was kept at `m` because its abstract assigns the finding to each named species.
- **Method and where.** sweep-58:5 and sweep-58:6 denied that the abstract names a counting method when it names design-based stereology; mammals-met:15 had an empty method and mammals-met:14 a bare "anatomical" and the wrong abstract section.
- **Cited values.** canon-5 rows and the spectrometric half of intake-6:22 rest on earlier studies that the read text does not name. The primary sources were not opened, so the notes name the gap (and a probable source for the ostrich) without asserting it.
- **Quotes.** All seventeen quotes that could be seen matched. Two differences come from the OpenAlex index (λ spelled "lambda", degree signs spelled "degrees") and were not counted.
- **Met in passing.** Several journal fields lack volumes (mammals-met:6, mammals-met:15, oa-5:1, mammals-met:4), the intake-6 records lost the accents on Ödeen, Håstad and Röll, and OpenAlex dates the giraffe paper 2012 against the record's 2013 issue year. These are left to the Crossref pass.

## Rows written

`recheck-27.jsonl`: 25 rows, all `correct`. From the sample: mammals-met:15, mammals-met:6, mammals-met:14, canon-5:17, canon-5:69, intake-4:12, intake-4:17, intake-4:18, intake-5:35, intake-6:22, intake-6:25, oa-5:1, sweep-58:5. From the further records: oa-5:2, oa-5:3, oa-5:4, oa-5:6, oa-5:7, oa-5:8, canon-5:1, canon-5:3, canon-5:5, mammals-met:4, mammals-met:5, sweep-58:6.

## Blocked pages

- Permission step not answered: frontiersin.org for 10.3389/fevo.2019.00321, 10.3389/fvets.2025.1647911 and 10.3389/fmed.2025.1562437 (the last read on OpenAlex instead); raw.githubusercontent.com for the eLife 15675 XML; ndownloader.figshare.com files 41923298 and 47932154; api.drum.lib.umd.edu for the Coyle dissertation. canon-2:38, sweep-27:7, canon-7:42, oa-1:1375, oa-5:643 and external-5:4 were dropped before any check.
- Fetch error: doi.org for 10.1002/ece3.8595 (herps-met:14, dropped).
- Proxy refused: www.ebi.ac.uk (Europe PMC REST).
- Rate limited (HTTP 429): OpenAlex for 10.1242/jeb.108456 (intake-3:38), 10.1007/s00359-009-0439-2 (intake-4:3), 10.1159/000113571 (sweep-14:10) and 10.25675/3.021717 (intake-5:36), all dropped.
- No abstract in OpenAlex: 10.1016/0376-6357(82)90008-0 (intake-2:39) and 10.1016/s0042-6989(03)00304-3 (intake-3:2), dropped and replaced; 10.1007/s00359-011-0635-8 and 10.1016/j.visres.2019.02.005, kept as unverifiable.
