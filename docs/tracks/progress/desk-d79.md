# desk-d79 progress (North American native and restoration species)

Started 29 October 2026. Branch research/desk-d79. About 52 WebSearch calls used. No search records and no wanted lines were written (no trait protocol was completed for a genus).

## Filed (2 records, docs/views/evidence/desk-d79.jsonl, both abstract-only, partial true)
- Polymnia canadensis, sense_light_nonvisual. Bender MH, Baskin JM, Baskin CC, "Seed germination ecology of Polymnia canadensis (Asteraceae), a monocarpic species of the North American Temperate Deciduous Forest", Plant Ecology 168(2): 221-253, 2003, DOI 10.1023/A:1024437510330. Authority: GBIF species 5385137 (api.gbif.org/v1/species/5385137 opened, ACCEPTED); POWO/WFO pages not openable. Quote is the far-red/red sentence (114 characters); the light-versus-dark result sits in a longer sentence and is in value. Bibliographic details come from the University of Kentucky scholars record; Springer and doi.org would not open.
- Artemisia tridentata, sense_chemical (volatile signalling). Karban R, Shiojiri K, Huntzinger M, McCall AC, "Damage-induced resistance in sagebrush: volatiles are key to intra- and interplant communication", Ecology 87(4): 922-930, 2006, DOI 10.1890/0012-9658(2006)87[922:drisva]2.0.co;2 (as scilit prints it). Authority: POWO urn:lsid:ipni.org:names:20780-2 opened, "This species is accepted". Authors/journal from a pherobase literature record; abstract from scilit; publisher page not opened.

## Held out
- Collinsia verna (Baskin and Baskin, J Torrey Bot Soc 110(3): 311-315, 1983, DOI 10.2307/2996184): the light-and-darkness germination sentence is 127 characters.
- Phlox divaricata (Majetic, Am Midl Nat 173(2), floral scent diel peaks): result sentence 186 characters.
- Solidago albopilosa (Albrecht, Dell, Long, J Torrey Bot Soc 147(2): 172-184, DOI 10.3159/TORREY-D-19-00038.1): photoperiod and dark-germination results only in sentences over 125 characters.
- Solidago altissima (Helms et al., BMC Plant Biology 14: 173, DOI 10.1186/1471-2229-14-173): volatile-priming result sentence 178 characters.
- Artemisia tridentata Shiojiri, Karban, Ishizaki 2012 (Arthropod-Plant Interactions 6: 197-202): abstract says only "sagebrush".
- Lupinus perennis germination (DOI 10.24266/0738-2898-14.4.167, Journal of Environmental Horticulture, horticultural; authors not printed on page; "Germination occurred equally well in the light or dark").
- Alnus maritima (Castanea 84(2): 144-160): no light or chemical trial. Dionaea muscipula (Pavlovic et al. 2017, New Phytologist 216(3)): only a paraphrase of the abstract was readable.
- Rhododendron catawbiense (Rowe et al. 1994, SNA conference): taxon and trait already on main; conference paper.

## Blocked
PMC pages (bot check), gbif.org taxon pages, worldfloraonline.org (robots), powo species page for Polymnia canadensis never surfaced, Springer and doi.org pages, bohrium (WAF), scholars.uky.edu Aster pilosus page returned PROVENANCE_REQUIRED once, then opened with a second URL (abstract shown was cut after two sentences; sentence 1 is 145 characters).

## Advice
GBIF api.gbif.org/v1/species/<key> opens through WebFetch and shows taxonomicStatus; scholars.uky.edu Baskin records give clean abstracts with volume, issue and pages. The summariser refuses long verbatim chunks; ask for the last 60 characters of a sentence to complete a character count.
