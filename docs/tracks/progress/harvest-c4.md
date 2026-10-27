# harvest-c4: Pilea

## 2026-10-27

Dispatch `regards-issue-28-20261027`, issue #28. Only Pilea, following round4-harvest and desk-screen points 1–10. No evidence was written in this screening pass.

Round counts: 1 genus screened through the full protocol (Pilea), 0 cells closed by measurement, 1 search record (eye_type), 15 wanted lines. No genera remain unscreened in this batch; sense_light_nonvisual, sense_chemical and diel remain open for intake of wanted candidates. The four open queue cells are sense_light_nonvisual, sense_chemical, diel and eye_type for Pilea microphylla (9,451 records). Artillery plant is the common name used. The owner's eye_type reading is none; epidermal focusing belongs under sense_light_nonvisual.

Web search connector results were screened for all four scientific/common trait pairs, germination light/dark, dormancy/GA/smoke and floral volatiles; follow-ups with quoted genus recovered primary light-growth and applied-hormone candidates. Metadata follow-ups did not open papers. The five web-derived wanted leads are a Pilea melatonin/AVG darkness experiment, an ASHS light/fertilizer trial, a Korean indoor light-growth study, a Pilea depressa formaldehyde-response thesis and a Pilea peperomioides auxin/venation study. The last requires intake to distinguish experiments from a model. Ten additional harvest leads cover light/photoperiod trials, nutrient or pollutant treatments, wetland seed dynamics and a CAM nocturnal-acid survey; none is treated as a confirmed Pilea measurement before intake. No measurement is claimed from snippets. No unauthorized source was opened, and no paid API was used.

Initial access failures: ordinary shell HTTPS to api.openalex.org raised ProxyError (proxy:8080, Operation not permitted); direct mode raised NameResolutionError. Connector opens of the scientific/common light query and Urticaceae photoreceptor review API URLs returned not accessible via this tool. After the parent supplied explicit network-enabled execution settings, all nine scientific/common trait and family-review OpenAlex requests succeeded (200, per-page=20). Light and eye scientific/common queries each returned zero works; diel 13/3, chemical 11/20, family review 16. These initial network failures are resolved, not a current reason to stop.

The initial missing-ci error was resolved when the parent fetched origin/ci 55a1f658a687c5d355ae11d9eec65def211f4033. `harvest_get.py Pilea` and `screen_candidates.py Pilea` then succeeded under network-enabled execution. Run 3 and supplements 14/20 contain 12 successful queries with no failed step. The title/abstract candidates were screened; the sole eye_type candidate concerns Magnolia epidermis and is recorded with the owner's focusing interpretation. Light/chemical/diel candidates are held on wanted and receive no null-search records. The chemical citation step on 10.1111/ele.12205 returned zero works; live repeats on that source and 10.1093/hr/uhad232 also returned zero. The Urticaceae photoreceptor-review search returned 16 works, screened without finding Pilea eyes. Canon registry and existing genus evidence were checked locally; no Pilea evidence was found. No access/quota blocker remains. No paper text was fetched, following plant-specific desk-screen 3 and 5 (confirmed by the parent).

Exact web queries (some initial germination/scent queries were repeated after output truncation; listed once; the searched record also lists all harvest and live OpenAlex queries):

- `Pilea seed germination light dark`
- `Pilea germination gibberellin OR smoke OR dormancy`
- `Pilea floral scent volatiles`
- `Pilea photoreceptor phototropism light response`
- `artillery plant photoreceptor phototropism light response`
- `Pilea flower opening time anthesis`
- `artillery plant flower opening time anthesis`
- `Pilea plant ocelli lens-like epidermal cells eye`
- `artillery plant ocelli lens-like epidermal cells eye`
- `Pilea chemical airborne volatile response`
- `artillery plant chemical airborne volatile response`
- `Urticaceae photoreceptor review`
- `"Pilea" seed germination light dark`
- `"Pilea" germination gibberellin smoke dormancy`
- `"Pilea" light intensity growth`
- `"Pilea" auxin gibberellin treatment`
- `"Effects of Melatonin and AVG on Plant Growth" Pilea`
- `"Influence of Light" "Pilea" "226"`
- `"Effects of light intensities and temperatures in various indoor situations"`
- `"The Purification Ability and the Response to Formaldehyde Exposure"`

Required precommit gate: `python3 -I tools/views/screen_candidates.py --check docs/views/searched/harvest-c4.jsonl --wanted docs/views/wanted/harvest-c4.jsonl` printed `0 problems` under network-enabled execution.
