# harvest-c13 progress

## 2026-10-27

Desk screen only: no pages fetched and no evidence records. OpenAlex skipped throughout this round after the coordinator received HTTP 429 (free-IP budget exhausted); missing OpenAlex steps remain incomplete. No null search rows are written for incomplete protocol. Existing evidence and wanted coverage are adopted; owner n/a sources are never re-requested.

### Tussilago — web-screened, protocol partial

- Open queue traits reviewed: eye_type, sense_chemical, sense_light_nonvisual. Main already holds diel. Existing plant-1 eye/chemical null screens do not replace this round’s germination searches.
- 9 real web queries; titles/snippets returned were screened. Bostock 1978 explicitly measures light and nitrate responses in T. farfara, so both traits wait for reading (2 wanted lines including the callus lead below). Oil/extract composition results concern removed tissue and do not count as living signaling. Callus light/dark growth (Induction and Characteristics of Callus Cultures of the Medicinal Plant Tussilago farfara L., https://www.mdpi.com/2223-7747/13/21/3080) is an additional light lead; whole-plant applicability needs reader judgment. No eye null row: the incomplete OpenAlex common-name step is not claimed complete.
- Harvest run 4 and supplements were screened, including genus queries, both zero-hit citation steps (10.1016/j.tree.2009.09.010; 10.18016/ksutarimdoga.vi.926160), and Asteraceae photoreceptor review. The two eye candidates concern Populus trichomes and human macular supplementation, not Tussilago eyes.
- Harvest queries (verbatim, in output order): ["Tussilago phytochrome photoreceptor", "Tussilago light perception", "Tussilago phototropism", "Tussilago volatile signalling", "Tussilago photoperiod", "Tussilago circadian rhythm", "Asteraceae photoreceptor review"]
- Web queries (verbatim): ["Tussilago seed germination light dark", "Tussilago germination gibberellin OR smoke OR dormancy", "Tussilago floral scent volatiles", "Tussilago light response photoperiod", "coltsfoot light response photoperiod", "Tussilago response to airborne volatile signals", "coltsfoot response to airborne volatile signals", "Tussilago plant ocelli lens-like epidermal cells eye", "coltsfoot plant ocelli lens-like epidermal cells eye"]


### Lotus — web-screened, protocol partial

No harvest run for Lotus; harvest_get.py and screen_candidates.py both confirmed absence. Main diel evidence adopted. All returned titles/snippets screened; many results concern Nelumbo nucifera, Nymphaea or Diospyros lotus and were excluded because they are different genera. Fabaceae family-review web search returned Beyond the CO–FT regulatory module: E1 and PHYA emerge as players in photoperiodic regulation of flowering in legumes (10.1093/jxb/erag313); review search screened, no page fetched. Lotus seed light/dark, L. japonicus LED growth, birdsfoot trefoil photoperiod, and L. japonicus methyl-jasmonate nodulation studies retained as four wanted leads. Missing OpenAlex work remains; no null search rows.

Web queries (verbatim): ["Lotus seed germination light dark", "Lotus germination gibberellin OR smoke OR dormancy", "Lotus floral scent volatiles", "Lotus light response photoperiod", "birdsfoot trefoil light response photoperiod", "Fabaceae photoreceptor review", "Lotus response to airborne volatile signals", "birdsfoot trefoil response to airborne volatile signals", "Lotus plant ocelli lens-like epidermal cells eye", "birdsfoot trefoil plant ocelli lens-like epidermal cells eye", "Lotus jasmonate herbivore", "birdsfoot trefoil floral scent volatiles"]

Counts this round so far: 2 genera web-screened / protocol partial; 0 full-protocol genera; 0 search rows; 6 wanted lines; 0 evidence rows. Next genus: Lythrum. Remaining: 38 untouched genera.
