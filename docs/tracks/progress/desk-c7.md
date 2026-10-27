# desk-c7: plant screening unit (27 October 2026, branch research/desk-c7)

Genera, all 12 done in the order given: Salvia, Rhus, Gaillardia, Serenoa, Acer, Monarda, Nekemias, Taxodium, Mitchella, Euphorbia, Eupatorium, Juniperus.

Files: docs/views/evidence/desk-c7.jsonl (18 records), docs/views/searched/desk-c7.jsonl (13 records), docs/views/wanted/desk-c7.jsonl (12 lines). Gate: `screen_candidates.py --check` prints "0 problems"; `senses/check.py` shows no new problems (its 11 non-zero files are older units).

## Method and limits
- The OpenAlex API was refused by the session proxy (HTTP 403 on CONNECT to api.openalex.org). I did not work around it. Every step the harvest had not run (common-name searches, germination searches, family review, citation steps for genera in no run) was a labelled "web: " WebSearch. Harvest genera list the harvest's own queries word for word first. For genera in no harvest run the family step is the web search "<Family> photoreceptor review", and `chased` names 10.1007/s44372-025-00446-3 (Discover Plants 2025, a general photoreceptor review whose page I opened; it names no Asteraceae genus but sunflower by common name and no genus of this unit). That is a weak family review; the desk may prefer "none" reasons for those records.
- WebSearch returns titles and URLs only. Pages were opened with WebFetch, which summarises; verbatim quotes in evidence are the tool's returns (under 120 characters), so every evidence record is `partial: true` with that said in `note`. quotecheck.py against the pages may fail some.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (an academia.edu profile appeared in one result list and was not opened). Blocked pages: link.springer.com/article/10.1007/s10310-014-0451-4 (Acer pycnanthum; abstract read through an informahealthcare mirror), doi.org/10.32473/fshs.135.1.136612 (Serenoa), thescholarship.ecu.edu thesis download (Taxodium).

## Cells closed by a measurement (14)
Salvia sense_chemical (S. officinalis GA3 priming, Tropentag 2022 abstract; S. assurgens and S. madrigalii floral volatiles, Botanical Sciences 2024). Rhus sense_chemical (R. aromatica GA3, Li, Baskin and Baskin 1999; R. coriaria GA3, 2024). Gaillardia sense_light_nonvisual (G. aristata dark germination, Skinner 2006 protocol) and sense_chemical (genus-level GA3, Bharathi et al. 2007, grade g). Serenoa diel (S. repens buds open 02:00 to 04:00, Carrington et al. 2003). Acer sense_chemical (A. pseudoplatanus GA3), sense_light_nonvisual (A. mono light quality; species-level sentence is the fetch tool's reading), diel (A. caesium, anthesis 12 to 2 pm, Semalty and Sharma 1996). Monarda sense_chemical (M. fistulosa herbivore volatiles, Keefover-Ring 2013) and sense_light_nonvisual (M. fistulosa, M. didyma; direction of the light effect not on the abstract). Euphorbia sense_chemical (E. jolkinii GA3, 2021). Juniperus sense_chemical (J. procera GA3, PeerJ 2024). Eupatorium sense_chemical (E. adenophorum MeJA and aphid volatiles, 2010) and sense_light_nonvisual (E. adenophorum and E. riparium photoblastic, Rai 1987).

## Search records (13, found "none")
Gaillardia diel and eye_type; Serenoa eye_type; Acer eye_type; Monarda diel and eye_type; Nekemias sense_chemical; Taxodium diel and eye_type; Mitchella diel and eye_type; Eupatorium diel and eye_type. Plant eye_type records carry the owner's wording (point 10(b)).

## Wanted lines (12)
Salvia: S. verticillata germination (Plovdiv page, no authors), eleven-species GA3 trial (ijsst page, no title or authors), S. officinalis seed priming (Notulae Botanicae), 10.1016/j.phytochem.2018.07.016. Rhus: 10.3390/molecules25153412. Serenoa: 10.32473/fshs.135.1.136612 (sense_light_nonvisual, so that trait has no record). Acer: A. monspessulanum subsp. turcomanicum (no authors on page), A. pycnanthum (10.1007/s10310-014-0451-4, title and authors unread), A. trautvetteri. Taxodium: Liu et al. 2009 chemical soaks (borderline under point 10(a)/(d); sense_chemical has no record). Mitchella: Hayden 2012 (sense_light_nonvisual, no record). Euphorbia: E. esula growth regulators (10.1614/WS-07-179.1, extra species).

## Left open and why
- Taxodium sense_chemical and Mitchella sense_light_nonvisual wait on their wanted lines; Serenoa sense_light_nonvisual waits on the Florida State Horticultural Society paper.
- Light-photoperiod and floral-scent searches were not run for genera where the trait was already closed by the germination search; the queries list shows what ran.
- Extra search outside the protocol: one bald cypress flooding-hormone query (Taxodium) and one MeJA query (Nekemias); both listed in `queries`.
