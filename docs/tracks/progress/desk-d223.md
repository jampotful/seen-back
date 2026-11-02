# desk-d223 progress

Scope: animal sensory-trait records from open full text (PLOS ONE and PLOS NTDs pages, PeerJ). Records are in docs/views/evidence/desk-d223.jsonl; check.py reports 0 problems for the unit. Candidates came from WebSearch restricted to peerj.com and journals.plos.org (Crossref list queries returned mostly human-medicine titles and rate-limited quickly). Species and DOI were checked against origin/main (whole docs tree) before opening each paper, and Crossref confirmed authors, volume, issue, article number and licence for every DOI filed. Older PLOS ONE papers (2011 to 2018) were far less covered on main than recent ones.

## Records (14)
- Gekko subpalmatus (PLoS ONE 11(1): e0146677), sense_hearing: ABR thresholds about 40 dB SPL from 1.0 to 3.5 kHz (sentence reassembled from overlapping first/last 100 characters).
- Diaprepes abbreviatus (PLoS ONE 8(1): e53120), two behaviour_vision records: citrus + conspecific odour attraction lost under green light; red preferred over green (P<0.001).
- Triatoma dimidiata (PLoS ONE 7(4): e36207), behaviour_vision: attraction decreased with increasing wavelength.
- Diaphorina citri (PLoS ONE 12(12): e0189228), behaviour_vision: UV added to green or yellow targets enhanced attraction (CC0).
- Nesidiocoris tenuis (PLoS ONE 16(1): e0245165), behaviour_vision: Y-tube attraction highest at 385 nm (73.5%).
- Phlebotomus perniciosus (PLoS Negl. Trop. Dis. 18(12): e0012787), sense_chemical: attraction index 0.53 nonanal to -0.47 p-cymene.
- Gnorimus nobilis (PLoS ONE 13(11): e0206526), two sense_chemical records: Y-tube sex difference to 2-propyl (E)-3-hexenoate; male EAG dose-dependent. The fetched page returned no licence sentence, so the basis is the publisher page plus Crossref CC BY 4.0 (version of record).
- Anopheles gambiae (PLoS ONE 8(5): e62995), sense_chemical (odour + heat longer flights, more landings) and sense_thermal (heat alone similarly short and direct).
- Chiloscyllium punctatum (PLoS ONE 8(1): e52551), sense_electric: stage 34 embryos responded at fields as low as 0.4 uV/cm (lowest tested value).
- Anguilla anguilla (PLoS ONE 17(6): e0270573), sense_electric: juvenile eel preferred the low-field route at 1.22, 2.17, 3.74 V/cm under 2 Hz.
- Spheniscus humboldti (PLoS ONE 6(9): e25002), sense_chemical: more time with non-kin than kin odour (t11 = 2.724, P = 0.02).

## Held out
- Monarch magnetic/cold paper (PLoS ONE 20(8): e0328737, CC0): only one whole abstract sentence (coldness reverses orientation poleward) and it names no magnetic cue; Results sentences over 125 characters and the cold-group n differs between Methods and Results.
- Podarcis erhardii throat colours (PLoS ONE 20(10): e0334557): colour discrimination is modelled with other species' visual systems.
- Elasmobranch electrosensitive spatial vectors (PLoS ONE 6(1): e16008): canal anatomy only.
- Rheophilic fish visual cues (minnow and trout, PLoS ONE 18(3): e0281741): two species, key sentences over the limit.
- Hissing cockroach habituation (PeerJ 13: e19805): learning of tactile response, no sensory-trait value; stickleback flow refuge (PeerJ 5: e3121): key sentence truncated.
- Carp/eel pulsed-DC paper (PeerJ 12: e17962): previously held out and no V/cm values in the text.
- Florida manatee boat-noise detection (PLoS ONE 17(5): e0268513): detection is estimated from a prior audiogram of captive manatees and field background noise, no new hearing measurement; Results text has no dB thresholds.
- Not reached because journals.plos.org returned rate-limit errors for about 10 minutes: harp seal vibrissae frequency response (PLoS ONE 8: e0054876) and tsetse odour baits (PLoS Negl. Trop. Dis. 4: e0000632). Neither is on main by DOI.
- Already on main by species or DOI: Trabala vishnou gigantina EAG (PeerJ 13: e20124), Electrogena lateralis, octopus plumes, Lymnaea, Culex, many carp, catfish and cichlid hearing papers.

## Owner questions
- Gnorimus nobilis: is the publisher page without a licence sentence plus Crossref CC BY 4.0 (vor) enough, as the audit licence rule now says? Records are filed on that basis.
- Several PLOS papers have Crossref licence content-version "unspecified" (Diaprepes, Triatoma, Nesidiocoris, Anopheles, Spheniscus, Chiloscyllium) while the page states "Creative Commons Attribution License"; filed as CC BY on the page statement.
- Anopheles gambiae colony origin and strain are not stated in the parts read; say if a mosquito lab strain should be flagged differently.
- Chiloscyllium punctatum electric value is the lowest tested intensity (0.4 uV/cm), not a threshold floor; stated in conditions.

## Desk disposition after audits 310 and 311

Audit 310 (lines 1 to 7): 6 of 7 in error (85.7%); line 6 (Nesidiocoris tenuis) passed. Audit 311 (lines 8 to 14): 7 of 7 in error (100%). Combined for d223: 13 of 14 (92.9%), all fixable and corrected with the auditors' replacement text; none dropped. Pooled audits 172 to 311: 349 of 753 (46.3%).

Faults were omissions of design the papers print: Diaprepes odour (weevils walked toward green LEDs set perpendicular to the odour stream, so the odour response was redirected, not abolished); Diaprepes colour (red preferred over green only against bright green; green preferred over blue and UV); Diaphorina citri (no trial paired the same colour with and without UV, so the UV effect is inferred across pairs); Triatoma dimidiata (no LED intensity in the Methods); Phlebotomus perniciosus (11 of 14 compounds gave no significant Y-tube choice despite EAG activity); Gnorimus nobilis (Table 1: males avoided the compound at 1 to 100 ng and 1 ug was not significant; EAG dose series); Anopheles gambiae x2 (colony is Wageningen, from Suakoko, Liberia, 1987, not unstated; testing order randomised); Chiloscyllium punctatum (quote dropped "(Fig. 3I)" unmarked; field strength calculated, not measured; intensity bands); Anguilla anguilla (both routes carried a field, high 1.5 to 2 times low; auditor could not open the full text, so its other details are unchecked); Spheniscus humboldti (both kin-test odours came from unfamiliar birds; test order not counterbalanced).

Desk deviations from the replacement text: the optional Gnorimus value rewrite and the Anopheles landing-note value rewrite were not applied, because the value must say no more than the quote; the Gnorimus conditions now state the table contradiction against the quote's "1 ug and above".

Owner questions: licence rulings (both auditors): a Crossref licence of content-version "unspecified" with a page-printed "Creative Commons Attribution License" is acceptable, and a page with no licence sentence plus a Crossref CC BY 4.0 for the version of record (Gnorimus nobilis) is acceptable under the audits 307 and 308 rule; Anopheles gambiae filed as printed (sensu stricto in the title) with the colony as a lab-strain condition, no M or S form statement seen; Triatoma dimidiata, Diaphorina citri, Nesidiocoris tenuis, Phlebotomus perniciosus, Gnorimus nobilis, Chiloscyllium punctatum and Gekko subpalmatus names to gbif-names.tsv if absent; Anguilla anguilla full text still worth a second look once PLOS stops rate-limiting.
