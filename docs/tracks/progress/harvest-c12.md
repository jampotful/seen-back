# harvest-c12

## 2026-10-27 — round 28 checkpoint

This worker: 1/40 genera desk-screened (Equisetum), 0 partially screened, 2 search records, 6 new wanted lines, 0 evidence records. Cumulative: the same; there was no prior harvest-c12 progress/searched/wanted file. No cells closed by measurement; two null traits have completed available-source desk screening. Remaining:39; first incomplete Cardamine in the original batch order.

Read AGENTS.md first, the round28 worker guide, round4-harvest, THOROUGH, BRIEF (including Round2), round3-sweep and desk-screen points1–10 including plant10(e). Harvest_get printed Equisetum “in no harvest run yet”; screen_candidates printed “not in the harvest”. Checked global evidence, searched, wanted and papers-status. Existing oa-9 evidence already covers sense_chemical (antheridiogen responses), so no chemical null or duplicate wanted for that paper. Old sweep-3 search is thin and remains untouched. No canon relevant to Equisetum was marked in_hand; plant canon checked in canon.jsonl and no new canon wanted line added.

Ten web queries ran, in this exact order (first20 titles/snippets where returned; no result page/full text fetched):
- `web: Equisetum seed germination light dark`
- `web: Equisetum germination gibberellin OR smoke OR dormancy`
- `web: Equisetum jasmonate herbivore`
- `web: Equisetum light photoperiod phototropism`
- `web: horsetail light photoperiod phototropism`
- `web: Equisetum flower opening time anthesis`
- `web: horsetail flower opening time anthesis`
- `web: Equisetum eye type epidermal focusing`
- `web: horsetail eye type epidermal focusing`

- `web: Equisetaceae photoreceptor review`

Useful results and dispositions: the six titled works in wanted/harvest-c12.jsonl are unread candidates, not evidence. No duplicate source title/DOI was found in existing wanted or papers-status. Germination lead 10.3389/fpls.2015.00441 was retained under10(e). Guillon2003 light-level sex expression, Nakatani/Noguchi1996 photoperiod growth, the blue-light stomatal paper, low-light field horsetail growth and Thompson’s thesis all concern possible light responses; none licenses an eye_type measurement. Stomatal ultrastructure, fossil epidermal anatomy, silica microprobe papers, botanical identification profiles and medical use of extracts under the eye searches do not measure image-forming eyes. Plant eye_type follows the owner’s “none” reading; no focusing lead was found. Anthesis searches mainly returned botanical descriptions of spore-bearing, nonflowering horsetails and flowering papers on other taxa; seasonal spore dates and daylength growth treatments do not establish a daily activity class. No diel null is written while required OpenAlex steps remain incomplete.

Source limitation: OpenAlex HTTP429 on the first missing-step query `Equisetum light photoperiod phototropism`, URL https://api.openalex.org/works?search=Equisetum+light+photoperiod+phototropism&per-page=20 (network enabled). Three concurrent requests launched; aborted on first refusal with no usable responses saved. Source skipped rest of round. Parent directed continuation through available web sources, and accurate scientific/common-name paired web searches plus family review satisfy available-source screening. OpenAlex queries are not represented as executed successes. Family query `Equisetaceae photoreceptor review` returned general plant reviews including Li/Mathews2016 (canon); no family-specific review or eye/diel measurement was identified in returned titles/snippets. Chased is consequently “none: no measured relative and no family review found”, with places searched named. Two null records cover eye_type/diel only; light is held for the six wanted works; chemical already has evidence. All title/snippet provenance and exact queries retained. Unknown metadata remains empty/null. The blue-light landing page’s kiaf238 identifier was not assumed a DOI because results also showed a kiaf298 PDF.

Next: Cardamine, then Rumex in original order. Do not repeat Equisetum’s completed available-source desk searches. No evidence logged under desk-screen point5; no paper full text committed.
