# The compiler's drafts against the hand-made specs

Agreement means the same value within 10%, or the same string. `grade` agreement is the same letter. A hand-made parameter graded `?` has no grade to compare.

## alligator, sonnet-5-5

- Hand-made parameters: 7. Draft parameters: 7. In both: 3.
- Same value (10%): 2 of 3 in both.
- Same grade among those with a hand-made grade: 0 of 0.
- Only in the hand-made spec: 4. Only in the draft: 4.

| Parameter | Hand-made | Draft |
|---|---|---|
| params.M | - | "CROC" (g) |  added |
| params.cpd | 9 (?) | 8.4 (m) |  same |
| params.dof | 24 (?) | - |  missing |
| params.fall | 2.6 (?) | 1 (i) |  differs |
| params.fov | 280 (?) | - |  missing |
| params.gain | 1.6 (?) | - |  missing |
| params.pupil | - | "v" (i) |  added |
| params.sat | 0.9 (?) | - |  missing |
| params.sheen | - | 0.6 (i) |  added |
| params.topoS | 1 (?) | 1 (i) |  same |
| spectrum.adaptAt | - | [-1.6,-0.6] (i) |  added |

## bee, sonnet-5-5

- Hand-made parameters: 10. Draft parameters: 9. In both: 6.
- Same value (10%): 0 of 6 in both.
- Same grade among those with a hand-made grade: 1 of 2.
- Only in the hand-made spec: 4. Only in the draft: 3.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.BEE | [[0,1,0],[0,0,1],[0,0,0]] (?) | [[0.22664,0.50311,0.19444,0.07581],[0.00... (g) |  differs |
| matrices.BEE4 | [[0.24648,0.49787,0.18056,0.07508],[0.00... (m) | - |  missing |
| overlay.polar | 0.8 (i) | - |  missing |
| pace.ratio | 3 (i) | - |  missing |
| params.M | "BEE4" (m) | "BEE" (g) |  differs |
| params.cpd | 1 (?) | 0.35 (g) |  differs |
| params.fall | - | 1 (i) |  added |
| params.fov | 320 (?) | 285 (g) |  differs |
| params.pupil | - | "none" (i) |  added |
| params.rate | 0.3 (?) | 0.46 (g) |  differs |
| params.topoA | - | 1 (i) |  added |
| params.uvBlue | 0 (i) | 0.7 (i) |  differs |
| spectrum.neutral | 1 (i) | - |  missing |

## bird, sonnet-5-5

- Hand-made parameters: 14. Draft parameters: 8. In both: 6.
- Same value (10%): 2 of 6 in both.
- Same grade among those with a hand-made grade: 1 of 1.
- Only in the hand-made spec: 8. Only in the draft: 2.

| Parameter | Hand-made | Draft |
|---|---|---|
| magnet.k | 1 (i) | - |  missing |
| matrices.PASSERINE | - | [[0.33891,0.45753,0.13066,0.07291],[0.04... (g) |  added |
| matrices.SONGBIRD | [[0.49977,0.32908,0.09213,0.07902],[0.05... (g) | - |  missing |
| motion.holdMs | 700 (i) | - |  missing |
| motion.maxDeg | 8 (i) | - |  missing |
| motion.thrust | 3 (i) | - |  missing |
| motion.thrustMs | 140 (i) | - |  missing |
| params.M | "SONGBIRD" (g) | "PASSERINE" (g) |  differs |
| params.cpd | 25 (?) | 8 (g) |  differs |
| params.fall | 0.6 (?) | 1.0 (i) |  differs |
| params.fov | 300 (?) | 300 (g) |  same |
| params.rate | 0.5 (?) | 0.45 (g) |  same |
| params.sheen | 0 (i) | - |  missing |
| params.topoA | 0.5 (?) | 1 (i) |  differs |
| params.uvBlue | - | 0.5 (i) |  added |
| spectrum.neutral | 1 (i) | - |  missing |

## cat, sonnet-5-5

- Hand-made parameters: 15. Draft parameters: 10. In both: 7.
- Same value (10%): 5 of 7 in both.
- Same grade among those with a hand-made grade: 0 of 2.
- Only in the hand-made spec: 8. Only in the draft: 3.

| Parameter | Hand-made | Draft |
|---|---|---|
| gaze.saccade | - | [25,3.1] (g) |  added |
| matrices.CAT | [[0.27629,0.48752,0.16204,0.07415],[0.27... (m) | [[0.3057,0.47473,0.14613,0.07344],[0.305... (g) |  same |
| matrices.CAT_ROD | [[0.06646,0.45296,0.39222,0.08836],[0.06... (m) | - |  missing |
| matrices.DEUTAN | [[0.29275,0.70725,0],[0.29275,0.70725,0]... (?) | - |  missing |
| params.M | "CAT" (m) | "CAT" (g) |  same |
| params.cpd | 8 (?) | 8.1 (g) |  same |
| params.dof | 26 (?) | - |  missing |
| params.fall | 2 (?) | 1.0 (i) |  differs |
| params.fov | 200 (?) | - |  missing |
| params.gain | 1.7 (?) | 1.6 (i) |  same |
| params.pupil | - | "v" (g) |  added |
| params.sat | 0.8 (?) | 0.6 (i) |  differs |
| params.sheen | - | 0.6 (i) |  added |
| params.topoA | 1 (?) | 1 (i) |  same |
| slow.mix | null (i) | - |  missing |
| slow.windowS | 3 (i) | - |  missing |
| spectrum.adaptAt | [-2,-1] (i) | - |  missing |
| spectrum.neutral | 1 (i) | - |  missing |

## deer, sonnet-5-5

- Hand-made parameters: 15. Draft parameters: 9. In both: 7.
- Same value (10%): 2 of 7 in both.
- Same grade among those with a hand-made grade: 0 of 2.
- Only in the hand-made spec: 8. Only in the draft: 2.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.DEER | [[0.21189,0.50602,0.20567,0.07642],[0.21... (m) | [[0.21189,0.50602,0.20567,0.07642],[0.21... (g) |  differs |
| matrices.DEER_ROD | [[0.05575,0.43645,0.41731,0.09049],[0.05... (m) | - |  missing |
| matrices.DEUTAN | [[0.29275,0.70725,0],[0.29275,0.70725,0]... (?) | - |  missing |
| params.M | "DEER" (m) | "DEER" (g) |  same |
| params.cpd | 8 (?) | 5 (m) |  differs |
| params.dof | 22 (?) | - |  missing |
| params.fall | 2.2 (?) | 1.2 (i) |  differs |
| params.fov | 310 (?) | 360 (g) |  differs |
| params.gain | 1.5 (?) | 1.4 (i) |  same |
| params.sat | 0.85 (?) | - |  missing |
| params.sheen | - | 0.5 (i) |  added |
| params.topoS | 1 (?) | 0.7 (i) |  differs |
| params.uvBlue | - | 0.4 (i) |  added |
| slow.mix | null (i) | - |  missing |
| slow.windowS | 3 (i) | - |  missing |
| spectrum.adaptAt | [-2,-1] (i) | - |  missing |
| spectrum.neutral | 1 (i) | - |  missing |

## dog, sonnet-5-5

- Hand-made parameters: 13. Draft parameters: 14. In both: 9.
- Same value (10%): 3 of 9 in both.
- Same grade among those with a hand-made grade: 3 of 3.
- Only in the hand-made spec: 4. Only in the draft: 5.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.DARK_508 | - | [[0.08817,0.47704,0.34962,0.08517],[0.08... (m) |  added |
| matrices.DEUTAN | [[0.29275,0.70725,0],[0.29275,0.70725,0]... (?) | - |  missing |
| matrices.DOG | [[0.30084,0.477,0.14861,0.07355],[0.3008... (m) | [[0.30084,0.477,0.14861,0.07355],[0.3008... (m) |  same |
| matrices.DOG_ROD | [[0.08817,0.47704,0.34962,0.08517],[0.08... (m) | - |  missing |
| params.M | "DOG" (m) | "DOG" (m) |  same |
| params.cpd | 11 (?) | 7.5 (i) |  differs |
| params.dof | 10 (?) | - |  missing |
| params.fall | 1.6 (?) | 1.2 (i) |  differs |
| params.fov | 240 (?) | 240 (g) |  same |
| params.gain | 1.3 (?) | 1.5 (i) |  differs |
| params.pupil | - | "o" (g) |  added |
| params.rate | - | 0.8 (g) |  added |
| params.sat | 0.85 (?) | 0.7 (i) |  differs |
| params.sheen | - | 0.5 (i) |  added |
| params.topoS | 1 (?) | 0.6 (i) |  differs |
| params.uvBlue | - | 0.3 (i) |  added |
| spectrum.adaptAt | [-2,-1] (i) | [-2.5,-1] (i) |  differs |
| spectrum.neutral | 1 (i) | - |  missing |

## frog, sonnet-5-5

- Hand-made parameters: 4. Draft parameters: 8. In both: 3.
- Same value (10%): 1 of 3 in both.
- Same grade among those with a hand-made grade: 0 of 0.
- Only in the hand-made spec: 1. Only in the draft: 5.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.FROG | - | [[0.37036,0.43871,0.11821,0.07271],[0.06... (g) |  added |
| params.M | - | "FROG" (g) |  added |
| params.cpd | 4 (?) | 4.3 (m) |  same |
| params.fall | - | 1.33 (g) |  added |
| params.fov | 340 (?) | 300 (i) |  differs |
| params.gate | 1 (?) | 0.6 (i) |  differs |
| params.glow | - | 0.8 (i) |  added |
| params.persist | 0.15 (?) | - |  missing |
| params.topoS | - | 1 (i) |  added |

## hawk, sonnet-5-5

- Hand-made parameters: 4. Draft parameters: 10. In both: 3.
- Same value (10%): 0 of 3 in both.
- Same grade among those with a hand-made grade: 0 of 0.
- Only in the hand-made spec: 1. Only in the draft: 7.

| Parameter | Hand-made | Draft |
|---|---|---|
| gaze.examine | - | [2000,5000] (g) |  added |
| params.cpd | 60 (?) | 40 (g) |  differs |
| params.fall | - | 1 (i) |  added |
| params.fov | 180 (?) | 280 (g) |  differs |
| params.fovea | 2.2 (?) | - |  missing |
| params.rate | 0.6 (?) | 0.77 (g) |  differs |
| params.sat | - | 1 (g) |  added |
| params.topoA | - | 1 (i) |  added |
| remap.blindAt | - | 180 (i) |  added |
| remap.blindDeg | - | 71 (g) |  added |
| remap.blindSoft | - | 6 (i) |  added |

## insect, sonnet-5-5

- Hand-made parameters: 8. Draft parameters: 7. In both: 4.
- Same value (10%): 1 of 4 in both.
- Same grade among those with a hand-made grade: 1 of 1.
- Only in the hand-made spec: 4. Only in the draft: 3.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.INSECT | [[0.13373,0.50272,0.28269,0.08085],[0.00... (g) | - |  missing |
| matrices.insect_uvbg | - | [[0.22664,0.50311,0.19444,0.07581],[0.00... (g) |  added |
| overlay.polar | 0.8 (i) | - |  missing |
| params.M | "INSECT" (g) | "insect_uvbg" (g) |  differs |
| params.cpd | 1 (?) | 0.5 (g) |  differs |
| params.fov | 320 (?) | 300 (g) |  same |
| params.pupil | - | "none" (i) |  added |
| params.rate | 0.45 (?) | 0.3 (g) |  differs |
| params.sheen | 0.8 (?) | - |  missing |
| params.uvBlue | - | 0.6 (i) |  added |
| spectrum.neutral | 1 (i) | - |  missing |

## plant, sonnet-5-5

- Hand-made parameters: 3. Draft parameters: 10. In both: 2.
- Same value (10%): 1 of 2 in both.
- Same grade among those with a hand-made grade: 0 of 0.
- Only in the hand-made spec: 1. Only in the draft: 8.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.plant_light | - | [[0.52237,0.23491,0.1361,0.10662],[0.017... (g) |  added |
| params.M | - | "plant_light" (g) |  added |
| params.field | 1 (?) | 1 (i) |  same |
| params.gain | - | 2 (i) |  added |
| params.noGreen | 1 (?) | - |  missing |
| params.persist | 2.5 (?) | 20 (i) |  differs |
| params.pupil | - | "none" (i) |  added |
| params.uvBlue | - | 0.6 (i) |  added |
| slow.everyMs | - | 3000 (i) |  added |
| slow.rightS | - | 20 (i) |  added |
| slow.windowS | - | 600 (i) |  added |

## rabbit, sonnet-5-5 (REFUSED by the checks, compared as returned)

- Hand-made parameters: 11. Draft parameters: 9. In both: 6.
- Same value (10%): 3 of 6 in both.
- Same grade among those with a hand-made grade: 1 of 2.
- Only in the hand-made spec: 5. Only in the draft: 3.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.DEUTAN | [[0.29275,0.70725,0],[0.29275,0.70725,0]... (?) | - |  missing |
| matrices.RABBIT | [[0.14657,0.50601,0.26748,0.07994],[0.14... (m) | - |  missing |
| matrices.RABBIT_ROD | [[0.05831,0.44075,0.411,0.08993],[0.0583... (m) | - |  missing |
| matrices.rabbit_cones | - | null (g) |  added |
| matrices.rabbit_rod | - | null (g) |  added |
| params.M | "RABBIT" (m) | "rabbit_cones" (g) |  differs |
| params.cpd | 3 (?) | 2.1 (g) |  differs |
| params.dof | 6 (?) | - |  missing |
| params.fall | 2 (?) | 2 (i) |  same |
| params.fov | 350 (?) | 360 (g) |  same |
| params.glow | - | 0.6 (i) |  added |
| params.topoS | 1 (?) | 1 (i) |  same |
| spectrum.adaptAt | [-2,-1] (i) | [-3,-1] (i) |  differs |
| spectrum.neutral | 1 (i) | - |  missing |

## reptile, sonnet-5-5

- Hand-made parameters: 5. Draft parameters: 5. In both: 2.
- Same value (10%): 0 of 2 in both.
- Same grade among those with a hand-made grade: 0 of 0.
- Only in the hand-made spec: 3. Only in the draft: 3.

| Parameter | Hand-made | Draft |
|---|---|---|
| params.M | - | "REPTILE" (g) |  added |
| params.cpd | 15 (?) | 6.1 (g) |  differs |
| params.fall | 1.2 (?) | 1 (i) |  differs |
| params.fov | 280 (?) | - |  missing |
| params.sheen | 0.6 (?) | - |  missing |
| params.topoA | 1 (?) | - |  missing |
| params.topoS | - | 0.6 (i) |  added |
| params.uvBlue | - | 0.5 (i) |  added |

## squirrel, sonnet-5-5

- Hand-made parameters: 12. Draft parameters: 9. In both: 6.
- Same value (10%): 1 of 6 in both.
- Same grade among those with a hand-made grade: 1 of 2.
- Only in the hand-made spec: 6. Only in the draft: 3.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.DARK_502 | - | [[0.06933,0.45679,0.38602,0.08786],[0.06... (g) |  added |
| matrices.PROTAN | [[0.11238,0.88762,0],[0.11238,0.88762,0]... (?) | - |  missing |
| matrices.SQUIRREL | [[0.24151,0.49932,0.18392,0.07525],[0.24... (m) | - |  missing |
| matrices.SQUIRREL_DI | - | [[0.12916,0.50121,0.28844,0.0812],[0.129... (g) |  added |
| matrices.SQUIRREL_ROD | [[0.06933,0.45679,0.38602,0.08786],[0.06... (m) | - |  missing |
| params.M | "SQUIRREL" (m) | "SQUIRREL_DI" (g) |  differs |
| params.cpd | 6 (?) | 3.9 (m) |  differs |
| params.dof | 4 (?) | - |  missing |
| params.fall | 1 (?) | 1 (i) |  same |
| params.fov | 270 (?) | - |  missing |
| params.rate | 0.56 (?) | 0.92 (g) |  differs |
| params.sat | - | 0.7 (i) |  added |
| params.topoS | 1 (?) | 0.6 (i) |  differs |
| spectrum.adaptAt | [-2,-1] (i) | [-2,-0.5] (i) |  differs |
| spectrum.neutral | 1 (i) | - |  missing |

## wader, sonnet-5-5

- Hand-made parameters: 7. Draft parameters: 9. In both: 4.
- Same value (10%): 1 of 4 in both.
- Same grade among those with a hand-made grade: 0 of 0.
- Only in the hand-made spec: 3. Only in the draft: 5.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.WADER | - | [[0.32957,0.46264,0.13475,0.07303],[0.04... (m) |  added |
| params.M | - | "WADER" (m) |  added |
| params.cpd | 25 (?) | 11.04 (g) |  differs |
| params.fall | 0.8 (?) | - |  missing |
| params.fov | 300 (?) | 320 (m) |  same |
| params.hold | 280 (?) | 20 (i) |  differs |
| params.rate | - | 0.78 (g) |  added |
| params.sheen | 0.6 (?) | - |  missing |
| params.thrust | 120 (?) | 50 (i) |  differs |
| params.topoS | 0.6 (?) | - |  missing |
| remap.blindAt | - | 180 (i) |  added |
| remap.blindDeg | - | 40 (g) |  added |
