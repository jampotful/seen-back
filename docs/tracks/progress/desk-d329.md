# desk-d329

Angle: day/night and light-linked behaviour in wild-origin animals (moonlight, artificial light, circadian regime, bioluminescence) and eye size against activity pattern.

Records filed (11, `docs/views/evidence/desk-d329.jsonl`, check.py 0 problems). Key choice: `diel` is plant-only by ruling, so light-driven animal behaviour is filed under `behaviour_vision` (precedent: Puffinus puffinus light-on counts on main), circadian-regime responses under `sense_light_nonvisual`, catch endpoints under `ecological_intervention_outcome`.
1. Leopardus pardalis, behaviour_vision, shorter GPS steps at full moon (PLOS ONE 18(11): e0286393).
2. Lynx rufus, behaviour_vision, null: illumination did not affect step length (same paper; habitat selection did change, in conditions).
3. Anomalops katoptron, behaviour_vision, non-luminescent fish no blink change and about 10% of shrimp captured (PLOS ONE 12(2): e0170489). Captive, commercial wholesaler; 5 luminescent and 3 non-luminescent fish; no statistic for capture.
4. Aotus azarae (paper spells azarai, synonym), behaviour_vision, activity almost fully inhibited during three lunar eclipses (PLoS ONE 5(9): e12572). Contrary 36.6% of activity in fully dark hours.
5. Lampyris noctiluca, behaviour_vision, females glow longer under streetlight (Insects 12(8): 734). Observational, mixed wild and captive-raised females.
6. Molossus molossus, 7. Peropteryx kappleri, behaviour_vision, moon-illumination probabilities from acoustic monitoring (PeerJ 8: e10591).
8. Erinaceus europaeus, behaviour_vision, null: no overall ALAN effect (Animals 10(5): 768). Crossref lookup failed twice; licence rests on page metadata (CC BY 3.0).
9. Alauda arvensis, ecological_intervention_outcome, mist-net occurrence and abundance rise with moonlight (Sci Rep 15: 19944). Weakest trait fit.
10. Rattus rattus, behaviour_vision, 40% slower movement in lit chamber, foraging unchanged (Sci Rep 9: 3739).
11. Odontotermes formosanus, sense_light_nonvisual, circadian rhythm abolished in LD and LL (Insects 15(1): 1); R. chinensis (same sentence) not filed because its accepted-name status was not confirmed.

Skipped, with reason:
- On main already: Hornets (PLOS ONE 0021892), Cymodoce japonica light colour (jmse14191858), Kakapo anatomy (0022945), Aquatica ficta (0191576), Dendrobates UV (0051364), Manx shearwater, and reef-fish eye (BMC Evol Biol 11:338), ants eye size (0257779) and prosimian eye size (0036097) appear in main audit/wanted/progress files.
- Reviews: fireflies and ALAN (fevo.2022.946640), mechanically stimulated bioluminescence (fmars.2023.1299602).
- Pooled or comparative: nocturnal bees threshold paper (five species pooled, s41598-020-72047-x); swarming bats and moonlight (six species pooled, s41598-024-53281-z); anuran eye size across 252 species (fevo.2021.755818, no per-species values in text).
- Lab colony or farm stock: cricket Teleogryllus commodus (PeerJ 1075), grey mouse lemur (captive colony), European seabass (farm fish).
- Not read: swallow-tailed gull lunar phase (PLOS 0056889) and elephant seal bioluminescence (0043565) because journals.plos.org rate-limited three attempts; ocelot-style cat paper and Springer-hosted bat lunar paper (s40462-018-0131-7) redirected to springer; Sci Rep small-mammal moon paper (s41598-023-37166-1) failed to fetch; royalsocietypublishing results (bat spectra, glow-worm, gecko eye size, frog eye size) not attempted because that host is refused.
- Eye size versus activity pattern: no new species-level, open, off-main value found within budget; this part of the angle is open.

Weak spots: PLOS, Nature, MDPI and PeerJ text came through a 125-character summary tool; all quotes are consecutive pieces joined (stated in each note). Moon and light covariates are calculated in several papers, not measured. Trait keys are a judgment call (no animal diel key).

## Desk disposition after audits 442 and 443

Audit 442 (lines 1-6) found all 6 in error (16 faults); audit 443 (lines 7-11) found 4 of 5 in error. The auditors disagreed on trait keys for moonlight correlates with no imposed intervention. Audit 442 refiled lines 1, 2 and 6 as ecological_intervention_outcome with "intervention: none imposed"; audit 443 held lines 7 and 9 (and line 6 by the same logic) because that key requires an intervention and an encounter or catch count against natural, calculated moonlight is not one. The desk followed the stricter reading: five moon-correlate records are held out, not filed (Leopardus pardalis and Lynx rufus step length, Molossus molossus and Peropteryx kappleri acoustic passes, Alauda arvensis net catch). The auditors' corrected text for them is in /audit-442 and /audit-443 reports and can be applied if the owner admits a key.

Filed (6): Anomalops katoptron (line 3, behaviour_vision; added the degenerated light organs confound), Aotus azarae (line 4, behaviour_vision; added the Friedman statistic X2 = 32.35, df 8), Lampyris noctiluca (line 5, ecological_intervention_outcome with the existing streetlighting as intervention, effect estimate and origin counts corrected), Erinaceus europaeus (line 8, ecological_intervention_outcome; light intensity not matched across stations), Rattus rattus (line 10; only three of seven movement behaviours changed), Odontotermes formosanus (line 11, sense_light_nonvisual). Authors converted to Surname Initials. The auditors' optional family/order fills for lines 5 and 6 were not applied.

Owner questions: (1) which trait key, if any, takes an encounter, catch or movement count measured against natural, calculated moonlight (also touches main's Puffinus puffinus light-on counts); (2) main files Aotus azarai, a synonym of Aotus azarae, at oa-1:4050-4051 and canon-5:214; (3) the unit read "diel is plant-only" as a bar on animal behaviour keys; the ruling limits only plant diel, and animal diel rows exist on main. Open angle: eye size versus activity pattern found no open species-level values. cockroach.speciesfile.org returned PROVENANCE_REQUIRED.
