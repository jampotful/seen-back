## 2026-10-14

This round completed the first two genera, Zanthoxylum and Ceratophyllum. Added 3 evidence records (2 species measurements graded m, 1 genus-level review report graded g), 1 wanted line and 5 null search records. Remaining: 48 genera, beginning with Saucerottia. Every open trait in the first two genera has an evidence, wanted or complete search record. Canon checks remain subject to the desk's compilation intake; null searches are not asserted to be exhausted cells before that step.

Sources opened this round:
- Bodede et al. (2015), DOI 10.21010/ajtcam.v12i5.10: full four-page publisher PDF, including methods and germination results. Logged treatment-dependent responses to light, avoiding a general dark-germination claim.
- Ren et al. (2024), DOI 10.1094/PDIS-09-23-1880-RE: Europe PMC abstract, chemical elicitation by salicylic acid. Publisher returned HTTP 403; marked partial.
- Hölker et al. (2023), DOI 10.1098/rstb.2022.0360: full Europe PMC XML, with focused reading of plant response, knowledge gaps and reference 126. The review names Ceratophyllum only at genus level, hence grade g. Requested original Mondy et al. (2021), DOI 10.1016/j.aquabot.2021.103447, to confirm measured species and exposure. Crossref confirmed title, authors and DOI; DOI route returned tunnel 403 and Semantic Scholar supplied the same DOI URL only.
- DOI 10.3390/microorganisms12112261: full Europe PMC XML, co-culture methods/results screened. Co-culture responses do not isolate chemical sensing.
- DOI 10.3389/fpls.2016.00470: full Europe PMC XML, Ceratophyllum passages and references screened; metal toxicity and detoxification were not treated as a measured chemical sensory pathway.
- DOI 10.3390/metabo15090614: full Europe PMC XML, genus review and references screened; pharmacology rather than plant sensory physiology.

The nearest chemical record sweep-20#7 lacks a DOI and explicitly uses a summariser's restatement as its quote. It measures Melia volatiles and human responses, so no trait was carried from it. Crossref recovered its DOI as 10.1080/0972060X.2021.1978869; a Europe PMC later-work reference query naming Zanthoxylum found no result. Family/genus review searches were also completed.

OpenAlex returned useful results before HTTP 429 on common-name queries. Stopped using that host; Europe PMC completed replacement scientific/common-name queries. Failed requests were never logged as null findings. Ceratophyllum fullTextXML for DOI 10.1093/aob/mcae059 returned HTTP 500; its abstract concerns endogenous hormone profiles, not an isolated sensory response, and supplied no new trait record.

Validation: all three evidence quotes passed tools/views/quotecheck.py verbatim against source text; tools/senses/addlog.py accepted all records. No app checks run.

Next: (1) Saucerottia scientific/common-name searches and Trochilidae pigment searches; (2) Oreamnos optics and nearest-source citation trail; (3) Achyra optics and nearest-source citation trail. Scratch API responses and PDFs are in untracked work/external-3/ and must not be committed.
