# Audit 105: desk-d15 (9 plant genera; branch origin/research/desk-d15, head a95d278b)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 3 lines of docs/views/searched/desk-d15.jsonl.
- Evidence records: both lines of docs/views/evidence/desk-d15.jsonl.
- Wanted lines: all 4, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (3 lines) and the wanted file (4 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, the rulings of audits 84, 86, 87 and 88, and the format of audit 90.

Queries. Ratibida and Senecio are in no harvest run (`harvest_get.py` prints "in no harvest run yet"), so all three records list "web: " lines only. That is the accepted shape (audits 86, 87).

Chased. All three name 10.1007/s00239-004-0294-2. My own "Asteraceae photoreceptor review" WebSearch returned doc.rero.ch/record/309979 (239_2004_Article_294.pdf, Lariguet and Dunand) on the first page, so the DOI is supported for both genera.

Main. I checked origin/main (20c0f774) docs/views/evidence/*.jsonl for all nine genera.
- Ratibida: no evidence on main.
- Glechoma: no evidence on main. Main has a null search record for sense_light_nonvisual, harvest-8:51, and a wanted line for it, harvest-c12:83 ("The effects of light intensity on foraging in the clonal herb Glechoma hederacea"). Evidence line 2 closes that cell. It contradicts no main evidence. harvest-8:51 is itself wrong: the Glechoma harvest prints "Changes induced by parental neighboring touch in the clonal plant Glechoma longituba depend on the light environment" (10.3389/fpls.2024.1358924) under its own query. The desk should retire it.
- Senecio: main holds sense_chemical evidence, sweep-9:14 (Senecio articulatus; Kite and Smith 1997; inflorescence odour, volatile emission), and diel evidence, sweep-9:15. Search line 3 is a sense_chemical null for the genus. Desk-screen point 4 says a trait with evidence already on main gets no search record. The record's note never mentions sweep-9:14. The main record's own note says the species is often now placed in Curio. See the fork below.

Searches. I ran 27 WebSearches, inside the 40 the launch prompt allows:
- 6 for Ratibida;
- 10 for Senecio;
- 1 for the family review;
- 3 for taxonomy;
- 4 for wanted lines;
- 3 others.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Search record verdicts (3)

| Line | Record | Verdict |
|---|---|---|
| 1 | Ratibida sense_light_nonvisual | ok, with a lead. Chased is supported. My searches ("Ratibida pinnata seed germination light darkness", "Ratibida columnifera germination light requirement shade growth", a prairie-forb light/dark search, "Ratibida gibberellic acid germination") returned nursery pages, the openprairie and Grinnell pages the record names, and the FEIS page for R. columnifera. FEIS (opened) gives temperature, stratification and scarification results only (Eddleman and Meinhardt 1981; Sorensen and Holden 1974; Bjugstad and Whitman 1989), with no light or dark treatment. Lead: Rischette and Norland 2017, "Germination Characteristics of a Native Non-Indigenous Prairie Forb in Prairie Plantings", Ecol Restor 35(4): 296-298, on R. pinnata. The er.uwpress page (opened) shows only the first sentence, and Project MUSE gave a bot check, so I cannot say whether it holds a light treatment. It is not counted. |
| 2 | Ratibida diel | ok. My searches ("Ratibida flower opening time of day anthesis" and a floret-opening/visitation-hours search) returned garden and flora pages, the sunflower circadian eLife paper, and a sunflower capitulum-orientation paper (par.nsf.gov 10446350, opened: Helianthus only). No Ratibida opening hour. |
| 3 | Senecio sense_chemical | **error: missed measurement** (plus a repeat-of-main fork). My search "Senecio germination GA3 treatment percent germination achenes" returned Kırmızı, Güleryüz and Arslan 2011, "Germination responses to GA3 and short-time chilling of three endemic species: Tripleurospermum pichleri, Cirsium leucopsis and Senecio olympicus (Asteraceae)", Plant Species Biol 26(1): 51-57, 10.1111/j.1442-1984.2010.00302.x (Uludağ repository page opened). The abstract states that chilling with GA3 in darkness raised S. olympicus germination from 45 to 87%. That is an applied-hormone response of living seed (10(d)). The record's searches named only S. vulgaris and S. inaequidens, and a genus null needs the whole genus. I did not confirm S. olympicus on POWO (Euro+Med gave a bot block), and no page I saw places it in another genus. The other set-asides are sound. Jacobaea is a separate genus. Victório et al. 2010 is on S. cineraria. The NaCl response of S. madagascariensis (Cambridge core-reader, opened) is salinity, which main does not log under sense_chemical (audit 88). |

Search record errors: **1 of 3 (33.3%)**, line 3.

## Evidence record verdicts (2)

| Line | Record | Verdict |
|---|---|---|
| 1 | Ratibida sense_chemical (Stahnke and Reese 2000) | **error: wrong taxon and grade.** The openprairie page (opened) confirms the title, the authors (April Stahnke, R. Neil Reese), Proc S Dak Acad Sci 79: 175, the ethephon treatment (two weeks of continuous light, 5 C), and the ~10 to 20% figure.<br>The quote is one whole sentence on the page, so the join of two fetched halves is acceptable here. The fetch confirmed the sentence word for word.<br>The abstract names the species, "Ratibida columnifera (Nutt.) Woot. & Standl.", among its eight species. The record's `conditions` ("species within Ratibida not named on the abstract page") and `note` are wrong. The record should be taxon Ratibida columnifera, rank species, grade m (one named species measured).<br>The value stands, so a rewrite repairs it. |
| 2 | Glechoma longituba sense_light_nonvisual (Zhang et al. 2015) | ok. The Photosynthetica page (opened) confirms the title, the authors, 53(1): 144-153, 10.1007/s11099-015-0092-7 and six light environments.<br>The quote matches the abstract word for word as one sentence, so the join is acceptable. The leaf, chlorophyll, stomata, chloroplast and respiration claims of the value are in the abstract.<br>POWO 447372-1 (opened) gives "This species is accepted" for Glechoma longituba (Nakai) Kuprian.<br>Grade m, partial. A set-light-intensity growth trial counts under 10(d). |

Evidence errors: **1 of 2 (50%)**, line 1.

Joined quotes. Both joined quotes proved to be single whole sentences on the source page, and both notes flagged the join. I accept the practice when both conditions hold. A join that crosses a sentence boundary would still be a requote.

## Held genera (no record written)

Each cell the progress note holds is backed on main, by evidence or by a wanted line (harvest-c12 lines 17 to 87, harvest-30:2 and 3).

| Genus | Cells and what holds them | Weak points |
|---|---|---|
| Fraxinus | sense_chemical has evidence (sweep-12:5, recheck-5-fixed:2). sense_light_nonvisual is held by c12:17 to 28 and 48 to 53. diel is held by c12:44 to 46. | diel rests on sap-flow series (44, 45) and intradiurnal pollen counts (46). Under the owner's diel reading (flower opening and scent timing), only 46 comes near. |
| Adiantum | sense_chemical (oa-9:171, 172) and sense_light_nonvisual (canon-3, oa-12, sweep-13 and others) have evidence. diel is held by c12:57 alone. | c12:57 is spore release in A. peruvianum. A fern has no flower opening or scent timing, so a diel null record would be the better course. |
| Botrypus | No open cell. sense_light_nonvisual has evidence (sweep-31:3), and diel and sense_chemical have main records. | Nothing to hold. |
| Parthenium | sense_light_nonvisual has evidence (sweep-35). sense_chemical is held by c12:64 and 67. diel is held by c12:65 and 66. | None. |
| Cynodon | sense_light_nonvisual has evidence (sweep-44). diel is held by c12:66 and 77. sense_chemical is held by c12:71 to 76, 78 and 79. | None. |
| Andropogon | sense_light_nonvisual already has evidence (sweep-34, Perrin et al. 2025), so the progress note's "held by harvest-c12:68 to 70" misstates it. diel is held by c12:70. sense_chemical is held by new wanted line 3. | Misstatement in the progress note only. |

None of these is counted.

## Counts

- Search records: 1 of 3, 33.3%.
- Evidence: 1 of 2, 50%.
- Unit: 2 of 5, 40%.

Pooled with audits 83 to 90 (from audit 90's figures: 48 in 1026 search records, 52 in 1090 overall):
- Search records: 49 in 1029, 4.8%.
- With evidence included: 54 in 1095, 4.9%.

Forks that would change the count:
- Line 3, Senecio. If the desk reads main's sweep-9:14 (Senecio articulatus) as Senecio evidence, line 3 is also a record point 4 forbids. If it reads that species as Curio articulatus, main's sweep-9:14 and 15 are filed under a synonym's genus (audit 88's rule) and should move. Either way line 3 fails on the missed Kırmızı et al. 2011 measurement, so it is counted once.
- Evidence line 1. If the desk accepts a genus-level g record when the source names the species, line 1 stands. The unit would then be 1 of 5 (20%), and the verdict is unchanged.

**Verdict: fail.** The search records fail at 1 of 3 and the evidence at 1 of 2. The whole unit was judged, so drop or repair the error lines and the rest stands.

**Error lines to drop:**
- docs/views/searched/desk-d15.jsonl: line 3. This reopens Senecio sense_chemical. Kırmızı et al. 2011 (S. olympicus, GA3) can close it, subject to the sweep-9:14 fork.
- docs/views/evidence/desk-d15.jsonl: line 1. Rewrite it as Ratibida columnifera, rank species, grade m, with the same quote and value.

## Wanted lines (listed, not counted)

1. Adams 2008, Kenyon. The page (opened) gives author Chelsea Adams and "Published on 01/01/08", with no DOI. It prints the title with typos ("Ratihida", "ftstulosa"), which the line silently corrects. Fine.
2. Tursun, Dayisoylu, Tursun 2015. The abakus.inonu record (opened) confirms the authors, KSU J Nat Sci 18(4): 48-54 and no DOI (handle 11616/102942, WOS:000409914400006). It confirms 16 h light / 8 h dark as best for S. vulgaris and no hormone treatment. Fine. Main's harvest-c12:85 already holds that cell, and the Cambridge core-reader text on S. madagascariensis (light/dark higher than total darkness) is a further Senecio sense_light_nonvisual lead.
3. Olszewski and Folin 2009. The wildflower.org record 1027 (opened) gives the full title "... Caryopses Subjected to Distilled Water or Potassium Nitrate Prechilling, Sodium Hypochlorite, and Storage". The line drops "Distilled Water or Potassium Nitrate". The authors, HortScience 44(5): 1407-1411, 2009 and the absence of a DOI match.
4. de Vlas 2002. The RUG page (opened) confirms the title, the author, 2002, a master's thesis, and "Glechoma hederacea produced nectar faster during the day than during the night." Fine.

## Leads

- Senecio olympicus sense_chemical: Kırmızı, Güleryüz and Arslan 2011, Plant Species Biol 26(1): 51-57, 10.1111/j.1442-1984.2010.00302.x.
- Ratibida pinnata sense_light_nonvisual: Rischette and Norland 2017, Ecol Restor 35(4): 296-298 (unread).
- Senecio madagascariensis sense_light_nonvisual: the Cambridge core-reader article 345B9246183149BE349CA72B4B9A3381, whose bioone twin is Invasive Plant Sci Manag 17(1), 10.1017/inp.2024.8.
- Glechoma: retire main's harvest-8:51, as above.

## Blocked pages

- muse.jhu.edu/article/673776: bot check.
- europlusmed.org: Anubis block.
- journal.kib.ac.cn: redirect, not followed.
- bioone inp.2024.8 full text: empty page.
- journals.uair.arizona.edu: redirect, not followed.
