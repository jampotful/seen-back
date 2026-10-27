# harvest-c6

## 2026-10-27 — round #28 regards-issue-28-20261027

Counts added this round: 1 of 1 genera screened (Succisa); 0 cells closed by measurement; 1 null-search record (eye_type); 5 wanted lines; 0 evidence records. No genera remain to screen. Diel and sense_chemical await full-text intake, so neither has a null-search record. Existing Succisa pratensis sense_light_nonvisual evidence (sweep-39:7 and its rechecked copy) was preserved.

Read AGENTS.md, round4-harvest.md, THOROUGH.md, the Round 2 BRIEF section, round3-sweep.md, desk-screen.md points 1–10 and audits 53/54. Used main 96225855ff44ad1bdb15cc365314b3b4e06cb284 and restored origin/ci 55a1f658a687c5d355ae11d9eec65def211f4033. No manual fetch or branch switch was made by this unit. The harvest tools invoke their own fetch internally.

The queue names three open traits, diel, eye_type and sense_chemical, each for Succisa pratensis (9961 records). Ran harvest_get.py and screen_candidates.py, screened the stored titles/abstracts, and checked the relevant canon registry and existing evidence. Successful harvest queries from runs 3, 15 and 20 appear in their original order in the search record, including zero-hit queries. Earlier supplement failures were repaired by run 15 and do not appear in current output. The harvest citation step on 10.1111/ele.12205 returned zero works; the Caprifoliaceae family review from run 17 was also screened.

Completed missing OpenAlex common-name queries (per-page=20): `devil's-bit scabious flower opening time anthesis` (0 hits), `devil's-bit scabious epidermal lens cells` (0), and `devil's-bit scabious volatile signalling` (7). The common name is confirmed by indexed Wildlife Trust species pages. Read every returned title and available abstract. Also read the first 20 titles/abstracts of `Caprifoliaceae photoreceptor review`; this repeated an existing harvest step while the harvest was temporarily inaccessible, rather than filling an additional missing step.

The search record lists every exact web query run, prefixed `web: `, after the harvest and missing OpenAlex queries. These include scientific/common-name pairs for flower-opening/anthesis, plant eye/lens cells and volatile signalling; the plant germination/light-dark and gibberellin/smoke/dormancy searches; floral scent; a broader chemical pair; and two candidate metadata-verification searches. Read returned titles/snippets. The connected search service provides no result-count control; no claim of a fixed 20 returned results per web query is made. Encyclopedia and other unverified-copy results were not used as evidence. No ResearchGate, paid API, library login or proxy-mirror page was opened.

The candidate tool lists zero eye_type candidates. The owner's 25 October rule sets plant eye_type to none and assigns epidermal focusing to sense_light_nonvisual. General plant-ocelli search results do not establish an eye in Succisa. The in-hand Animal eyes canon covers Metazoa, not this genus; it is named in canon with that limitation in the record. No plant evidence was fabricated from an animal compilation.

Wanted leads, all absent from the owner's n/a marks:

- Štenc et al. 2023, 10.1002/ajb2.16179: daily pollen-presentation schedule in Succisa pratensis (diel).
- Peñuelas et al. 2005, 10.1111/j.1469-8137.2005.01459.x: living-plant herbivory-induced volatiles (sense_chemical).
- Holder et al. 2020, 10.1016/j.gecco.2020.e01345: responses to ozone and nitrogen treatments (sense_chemical).
- 2017, 10.1371/journal.pone.0175160: nutrient treatment of living Succisa and altered floral rewards (sense_chemical).
- 2003, 10.1046/j.1365-2745.2003.00785.x: responses to eutrophication and acidification (sense_chemical).

Metadata came from indexed PubMed/publisher results, the OpenAlex API and the harvest, not memory. The last two leads retain empty authors fields because the harvest supplies no authors. Nutrient/acidification studies are living-plant chemical-response candidates; the reader should judge the measured response from full text. The 2017 essential-oil/extract study (10.1111/jphp.12784) concerns removed tissue in its indexed abstract and was not requested for sense_chemical. Generic methods/reviews and studies explicitly of other genera do not replace the concrete Succisa leads; no chemical null-search record was written.

Initial access failures were resolved: harvest_get.py and screen_candidates.py first reported no harvest because origin/ci was absent; connected web open could not access the OpenAlex family-query URL; and default shell curl failed to connect to proxy port 8080 (HTTP 000). After the parent restored origin/ci and enabled network access, helpers and OpenAlex requests succeeded. These failures are historical attempts, not remaining blockers.

Screening writes no evidence under desk-screen.md point 5. No paper full text was fetched. No app startup, build, server, browser test, self-test or gate edit was performed. Required screen_candidates.py check was run before commit; its result is recorded below.

Pre-commit gate: `python3 -I tools/views/screen_candidates.py --check docs/views/searched/harvest-c6.jsonl --wanted docs/views/wanted/harvest-c6.jsonl` printed `0 problems`.
