# Harvest c3 progress

## 2026-10-17

Checkpoint at the round stop condition: **5 of 40 genera screened**, in the assigned order: Rhododendron, Coccinella, Euonymus, Ribes, Polygonatum. **4 genera are represented by retained evidence**: Rhododendron, Coccinella, Euonymus and Ribes. **0 genera completed the full protocol.** **35 genera have not yet been screened**, starting with Epargyreus. **36 genera remain in the final queue**, including screened Polygonatum, which has no retained evidence or search record. The Epargyreus summary was inspected, but no entry is claimed complete and no work beyond the first five is logged.

Added **9 evidence records** through addlog.py: **7 grade m and 2 grade g**, **8 from full texts and 1 abstract-only/partial**. The full-text evidence comes from four primary articles and one thesis. Added **7 wanted lines**. **0 search records retained**: harvest queries omit common names (english=[] for these genera), and plant queries also omit diel/chemical/eye-type terms. Incomplete search rows were removed because coverage.py ignores protocol_complete and would falsely mark cells exhausted. All screening and citation details are preserved below instead.

**0 directly measured open queued species-trait cells closed**: the newly measured species are not the species with these traits open in the queue. Full-source upgrades and congeneric evidence are recorded, without assuming a new carry exception. No coverage/build/test/server commands were run; addlog.py performed its required per-record checks.

Harvest runs 1–4 were read from origin/ci cdc1fb99d1df7885bdf07bc6f7beda5e659f37ca. Queries were not repeated. A concurrent shallow fetch initially blocked ci access; central fetch resolved it. Publisher access failures were HTTP 403/proxy tunnel 403, not a new usage or rate limit. The desk reported Semantic Scholar 429 elsewhere and requested this checkpoint. Downloads and scripts stayed under /tmp/harvest-c3 outside the repository. Owner full/partial/n/a marks were checked; no marked paper was requested again.

Canon: no plant-specific compilation is marked in_hand in canon.jsonl; Animal Eyes is scoped to Metazoa and is not claimed checked for plants. Coccinella CFF compilation/evidence lookup is described below.

### Rhododendron

Full PDFs opened: Zaimenko et al. 2026 (10.15414/ainhlq.2026.0005), the J-STAGE flower/gravity review (10.2187/bss.18.52), and Christiaens 2014 thesis (https://biblio.ugent.be/publication/4428604/file/4428639.pdf). The LED experiment measured spectrum-dependent foliar metabolites in R. catawbiense. Pertinent thesis chapters and tables report applied ABA response and photoperiod responses of R. simsii hybrid cultivars; these are grade g, with cultivar differences explicit. The flower/gravity review only illustrates Rhododendron flowers. UMass thesis landing page (10.7275/20482811) yielded metadata and actual thesis date 1983, but no readable full text. Other plausible light/circadian papers were attempted through harvested OA links; ASHS, Wiley, OUP and MDPI returned 403, Elsevier proxy tunnel 403. Four direct candidates are wanted. No endogenous diel measurement read; eye_type and chemical sensing were not exhaustively searched.

Exact harvested queries:
- `Rhododendron phytochrome photoreceptor` (97 hits; first harvested titles/abstract starts screened).
- `Rhododendron light perception` (4192 hits; first harvested titles/abstract starts screened).
- `Rhododendron phototropism` (60 hits; first harvested titles/abstract starts screened).

Citation step: 10.1111/ele.12205 (0 works naming Rhododendron).

Protocol limitation: no common-name query was supplied. The harvested scientific-name queries are screening evidence, not a full exhaustion claim.

### Coccinella

All 29 unique hits (30 appearances) screened. Full Lin 1993 primary PDF opened from https://www.zin.ru/animalia/coleoptera/addpages/andrey_ukrainsky_library/References_files/Lin93.pdf; it measures spectral maxima, three spectral receptor types and polarization sensitivity, and reports no CFF or corner frequency. All three results logged from the full source, upgrading abstract-only prior reading. Full Ecocycles review (10.19040/ecocycles.v8i2.221) opened and gives no Coccinella temporal threshold. Foraging study DOI page (10.1007/s004420050518) exposes the public abstract, not a temporal-resolution experiment. Agee 1990 spectral study OUP DOI page was 403. In-hand CFF compilations/evidence (10.1007/bf00213682: Diptera; 10.1007/s00359-020-01429-3: Lepidoptera) contain no Coccinella record. The scientific-name flicker query returned zero hits; corner_hz was absent from this harvest and remains incomplete.

Exact harvested queries:
- `Coccinella vision` (517 hits; first harvested titles/abstract starts screened).
- `Coccinella eye` (887 hits; first harvested titles/abstract starts screened).
- `Coccinella flicker fusion temporal resolution` (0 hits; first harvested titles/abstract starts screened).

Citation step: 10.1007/BF00207188 (0 works naming Coccinella).

Protocol limitation: no common-name query was supplied. The harvested scientific-name queries are screening evidence, not a full exhaustion claim.

### Euonymus

Full PDFs opened: Wei et al. 2023 (10.1186/s13717-023-00449-6), Baghalian and Ranasingha 2026 (10.3389/fpls.2025.1697104), reviews 10.3389/fpls.2021.631810 and 10.1111/j.1469-8137.2006.01707.x, and 10.5073/jabfq.2025.098.017. The two primary light experiments give E. japonicus physiological treatment responses; the first upgrades prior abstract-only evidence. The reviews cite E. fortunei shade/disease effects, not measured chemical sensing. The 2025 ALAN paper uses Euonymus as prior literature, not a measured study species. Untitled J-STAGE 1926 PDF 10.15281/jplantres1887.40.477_499 opened: taxonomic notes, not a sensory experiment. Pollination scent and nectary title/abstract hits concern emissions/anatomy, not chemical sensing by the plant. Preprint v2 on light and methyl-jasmonate response and Forests 2024 ALAN experiment returned 403 and remain wanted. No endogenous diel rhythm measurement read.

Exact harvested queries:
- `Euonymus phytochrome photoreceptor` (15 hits; first harvested titles/abstract starts screened).
- `Euonymus light perception` (616 hits; first harvested titles/abstract starts screened).
- `Euonymus phototropism` (21 hits; first harvested titles/abstract starts screened).

Citation step: no measured-relative chase supplied; no family-review record supplied for Celastraceae. A family-review search is still needed to complete that step.

Protocol limitation: no common-name query was supplied. The harvested scientific-name queries are screening evidence, not a full exhaustion claim.

### Ribes

Citation step yielded 10.17660/ActaHortic.2024.1388.28. Public publisher abstract opened at https://www.actahort.org/books/1388/1388_28.htm and species/cultivar photoperiod results logged partial=true, access=abstract. Its PDF link requires publisher member access, so full text is wanted; no login attempted. Full review 10.3389/fpls.2014.00534 opened: Ribes flavonoid/latitude correlations do not isolate light perception. Light/growth, dormancy, currant, pulvini and stomatal reviews were attempted via harvested links but returned 403 (10.3390/f15030523, 10.1038/hortres.2014.59, 10.1300/j301v02n03_03, 10.1086/327125, 10.1111/nph.17913, 10.1104/pp.119.3.809). No chemical/diel/eye-type search claim is made.

Exact harvested queries:
- `Ribes phytochrome photoreceptor` (167 hits; first harvested titles/abstract starts screened).
- `Ribes light perception` (30306 hits; first harvested titles/abstract starts screened).
- `Ribes phototropism` (156 hits; first harvested titles/abstract starts screened).

Citation step: 10.1080/14620316.2021.2009743 (1 works naming Ribes); 10.1093/oxfordjournals.aob.a086894 (0 works naming Ribes).

Protocol limitation: no common-name query was supplied. The harvested scientific-name queries are screening evidence, not a full exhaustion claim.

### Polygonatum

All 25 unique hits screened (26 appearances). Full preprint 10.21203/rs.3.rs-3447626/v1 opened: germination hormones and annotated ABA-receptor proteomics, without an experimental light response or receptor binding assay. Full 10.3389/fpls.2025.1645666 opened: temperature stress tested under constant light regime; phytochrome-interacting-factor annotation does not measure light perception. Full 10.1186/s12866-023-02992-w opened: fumigation alters soil, microbes and later plant survival, not chemical sensing by Polygonatum. Other title/abstract hits concern processing, food, taxonomy or unrelated species. No qualifying light-perception measurement logged; common-name, diel, chemical and eye-type protocol steps remain incomplete.

Exact harvested queries:
- `Polygonatum phytochrome photoreceptor` (5 hits; first harvested titles/abstract starts screened).
- `Polygonatum light perception` (290 hits; first harvested titles/abstract starts screened).
- `Polygonatum phototropism` (6 hits; first harvested titles/abstract starts screened).

Citation step: no measured-relative chase supplied; no family-review record supplied for Asparagaceae. A family-review search is still needed to complete that step.

Protocol limitation: no common-name query was supplied. The harvested scientific-name queries are screening evidence, not a full exhaustion claim.
