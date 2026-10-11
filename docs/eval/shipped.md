# Exported slots, scored as the page would

_This file is written by `tools/eval/report.py` from `docs/eval/shipped-*.json`. Rerun the script to change it._

## `sentences-bioclip2-l14`

The slot holds the head `sentences` for `bioclip2-l14` (species_sci), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.7, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.05 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 98.3% (97.8 to 98.6); the top species is right for 92.5% (91.6 to 93.2) and is among the first five for 97.5% (97.0 to 97.9). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 99.5% | the name is right for 92.8% (92.1 to 93.6); the kind for 98.6% (98.3 to 99.0) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 0.5% | the kind is right for 30.4% (13.0 to 47.8) |

## `sentences-bioclip2-l14-product`

The slot holds the head `sentences` for `bioclip2-l14` (species_sci), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 20, w_kind 0.5, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.05 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 98.3% (97.9 to 98.6); the top species is right for 92.5% (91.6 to 93.2) and is among the first five for 97.5% (97.0 to 97.9). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos.

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 99.5% | the name is right for 92.8% (92.0 to 93.5); the kind for 98.6% (98.2 to 99.0) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 0.5% | the kind is right for 30.0% (10.0 to 50.0) |

## `sentences-tinyclip-39m-16`

The slot holds the head `sentences` for `tinyclip-39m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.5, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.40 and offer_at 0.53. On the 4197 test photos the kind of eye is right for 83.9% (82.8 to 85.0); the top species is right for 34.9% (33.5 to 36.4) and is among the first five for 53.8% (52.3 to 55.3). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 15.4% | the name is right for 92.7% (90.7 to 94.6); the kind for 98.8% (97.8 to 99.5) |
| three species to choose from | 3.3% | the three hold the species for 84.9% (78.4 to 90.6); the kind is right for 99.3% (97.8 to 100.0) |
| a kind of eye only | 81.3% | the kind is right for 80.5% (79.2 to 81.8) |

## `sentences-tinyclip-39m-16-product`

The slot holds the head `sentences` for `tinyclip-39m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 20, w_kind 0.5, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.40 and offer_at 0.53. On the 4197 test photos the kind of eye is right for 84.5% (83.4 to 85.6); the top species is right for 34.9% (33.5 to 36.4) and is among the first five for 53.8% (52.3 to 55.3). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos.

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 15.4% | the name is right for 93.0% (91.0 to 94.9); the kind for 98.9% (98.1 to 99.7) |
| three species to choose from | 3.3% | the three hold the species for 84.9% (78.4 to 90.6); the kind is right for 99.3% (97.8 to 100.0) |
| a kind of eye only | 81.3% | the kind is right for 81.2% (79.8 to 82.5) |

## `sentences-tinyclip-8m-16`

The slot holds the head `sentences` for `tinyclip-8m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.7, alpha_prior 0.625. On 1803 tuning photos (val) the thresholds came out as name_at 0.42 and offer_at 0.47. On the 4197 test photos the kind of eye is right for 78.8% (77.6 to 80.0); the top species is right for 25.3% (24.0 to 26.7) and is among the first five for 43.2% (41.7 to 44.7). `person` was said for 0.02% of these photos and `none` for 0.02%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 9.2% | the name is right for 89.9% (86.8 to 92.7); the kind for 98.7% (97.4 to 99.7) |
| three species to choose from | 5.1% | the three hold the species for 81.9% (76.8 to 86.6); the kind is right for 97.2% (94.9 to 99.1) |
| a kind of eye only | 85.7% | the kind is right for 75.6% (74.1 to 77.0) |

## `sentences-tinyclip-8m-16-product`

The slot holds the head `sentences` for `tinyclip-8m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 20, w_kind 0.5, alpha_prior 0.625. On 1803 tuning photos (val) the thresholds came out as name_at 0.42 and offer_at 0.47. On the 4197 test photos the kind of eye is right for 78.9% (77.7 to 80.1); the top species is right for 25.3% (24.0 to 26.7) and is among the first five for 43.2% (41.7 to 44.7). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos.

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 9.2% | the name is right for 90.1% (87.0 to 93.2); the kind for 99.0% (97.7 to 99.7) |
| three species to choose from | 5.1% | the three hold the species for 81.9% (76.8 to 86.6); the kind is right for 97.2% (94.9 to 99.1) |
| a kind of eye only | 85.7% | the kind is right for 75.7% (74.3 to 77.1) |

## `val-bioclip2-l14`

The slot holds the head `prototypes + sentences` for `bioclip2-l14` (species_sci, beta 8, bias for species without photos 0.65), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.5, alpha_prior 0.6. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.05 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 98.5% (98.1 to 98.9); the top species is right for 91.7% (90.9 to 92.6) and is among the first five for 97.6% (97.1 to 98.0). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: species.bias_url (build 7 of the page); fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 99.6% | the name is right for 92.0% (91.2 to 92.8); the kind for 98.7% (98.3 to 99.0) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 0.4% | the kind is right for 46.7% (20.0 to 73.3) |

## `val-tinyclip-39m-16`

The slot holds the head `prototypes + sentences` for `tinyclip-39m-16` (species_com, beta 8, bias for species without photos 0.65), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.7, alpha_prior 0.75. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.63 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 86.8% (85.7 to 87.7); the top species is right for 36.9% (35.5 to 38.4) and is among the first five for 55.8% (54.3 to 57.3). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: species.bias_url (build 7 of the page); fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 19.4% | the name is right for 88.7% (86.6 to 90.9); the kind for 98.4% (97.4 to 99.3) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 80.6% | the kind is right for 83.9% (82.7 to 85.2) |

## `val-tinyclip-8m-16`

The slot holds the head `discriminant + sentences` for `tinyclip-8m-16` (shrinkage 0.03, species_com, gamma 3), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 50, w_kind 0.3, alpha_prior 0.5. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.31 and offer_at 0.33. On the 4197 test photos the kind of eye is right for 77.5% (76.2 to 78.8); the top species is right for 25.6% (24.3 to 26.9) and is among the first five for 43.8% (42.3 to 45.3). `person` was said for 0.02% of these photos and `none` for 0.10%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: species.bias_url (build 7 of the page); fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 8.3% | the name is right for 89.9% (86.5 to 92.8); the kind for 99.1% (98.0 to 100.0) |
| three species to choose from | 6.7% | the three hold the species for 78.2% (73.2 to 82.9); the kind is right for 97.1% (95.0 to 98.9) |
| a kind of eye only | 85.1% | the kind is right for 73.9% (72.5 to 75.3) |
