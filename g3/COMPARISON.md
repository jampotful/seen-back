# The compiler's drafts against the hand-made specs

Agreement means the same value within 10%, or the same string. `grade` agreement is the same letter. A hand-made parameter graded `?` has no grade to compare.

## bee, sonnet-5-5

- Hand-made parameters: 10. Draft parameters: 9. In both: 6.
- Same value (10%): 2 of 6 in both.
- Same grade among those with a hand-made grade: 1 of 2.
- Only in the hand-made spec: 4. Only in the draft: 3.

| Parameter | Hand-made | Draft |
|---|---|---|
| matrices.BEE | [[0,1,0],[0,0,1],[0,0,0]] (?) | [[0.3057,0.47473,0.14613,0.07344],[0.000... (g) |  differs |
| matrices.BEE4 | [[0.24648,0.49787,0.18056,0.07508],[0.00... (m) | - |  missing |
| overlay.polar | 0.8 (i) | - |  missing |
| pace.ratio | 3 (i) | - |  missing |
| params.M | "BEE4" (m) | "BEE" (g) |  differs |
| params.cpd | 1 (?) | 0.26 (m) |  differs |
| params.fov | 320 (?) | 312 (g) |  same |
| params.rate | 0.3 (?) | 0.3 (g) |  same |
| params.uvBlue | 0 (i) | 0.8 (i) |  differs |
| remap.blindAt | - | 180 (g) |  added |
| remap.blindDeg | - | 48 (g) |  added |
| remap.blindSoft | - | 6 (i) |  added |
| spectrum.neutral | 1 (i) | - |  missing |

## jumper, sonnet-5-5

- Hand-made parameters: 58. Draft parameters: 12. In both: 9.
- Same value (10%): 4 of 9 in both.
- Same grade among those with a hand-made grade: 5 of 9.
- Only in the hand-made spec: 49. Only in the draft: 3.

| Parameter | Hand-made | Draft |
|---|---|---|
| by.genus.Habronattus.zones.fovea.uvR | 0 (i) | - |  missing |
| by.genus.Portia.zones.fovea.cpd | 12.5 (m) | - |  missing |
| by.genus.Portia.zones.gaze.cpd | 12.5 (m) | - |  missing |
| by.genus.Portia.zones.gaze.deg | [1.5,21] (i) | - |  missing |
| gaze.any | 0.6 (i) | - |  missing |
| gaze.back | 0.8 (m) | - |  missing |
| gaze.distract | 1.5 (m) | - |  missing |
| gaze.examine | [4000,12000] (m) | - |  missing |
| gaze.floor | 0.06 (i) | - |  missing |
| gaze.habit | 0.75 (m) | - |  missing |
| gaze.hold | 1500 (m) | - |  missing |
| gaze.ior | 5000 (m) | 5000 (i) |  same |
| gaze.iorDeg | 6 (i) | 5 (i) |  differs |
| gaze.living | 1.8 (i) | - |  missing |
| gaze.pursuit | 10 (m) | - |  missing |
| gaze.saccade | [40,4] (m) | - |  missing |
| gaze.sleep.after | 3500 (i) | - |  missing |
| gaze.sleep.bout | [6000,12000] (m) | - |  missing |
| gaze.sleep.gap | [20000,40000] (m) | - |  missing |
| gaze.surround | 0.6 (m) | - |  missing |
| gaze.sweep | [2,1.2] (m) | [2,1.2] (i) |  same |
| gaze.trackDeg | 9 (m) | - |  missing |
| gaze.twist | [25,2000,3500] (m) | [25,2000,3500] (i) |  same |
| gaze.wander | [8000,20000] (m) | - |  missing |
| matrices.PRINCIPAL_Q | [[0.18775,0.50874,0.22597,0.07755],[0.18... (m) | - |  missing |
| matrices.SIDE_GREEN | [[0.007270875763747455,0.313075356415478... (m) | - |  missing |
| matrices.UV_GREEN | [[0.008655804480651732,0.372708757637474... (g) | - |  missing |
| matrices.UV_GREEN_RED | [[0.5601617795753286,0.17290192113245703... (m) | - |  missing |
| pace.ratio | 2 (i) | - |  missing |
| params.M | - | "SIDE" (g) |  added |
| params.cpd | 0.5 (m) | 1.3 (m) |  differs |
| params.fov | 350 (m) | 330 (m) |  same |
| params.gate | - | 1 (i) |  added |
| params.glow | 0.9 (i) | - |  missing |
| params.glowC | [0.78,1,0.62] (i) | - |  missing |
| params.living | 0 (i) | 1 (i) |  differs |
| spectrum.neutral | 1 (i) | - |  missing |
| zones[0].cpd | 1.1 (m) | 3.8 (m) |  differs |
| zones[0].deg | [114,98] (g) | [2,21] (m) |  differs |
| zones[0].living | 1.6 (i) | - |  missing |
| zones[0].soft | 0.2 (i) | - |  missing |
| zones[0].uv | - | [1,0] (i) |  added |
| zones[1].cpd | 3.6 (m) | - |  missing |
| zones[1].deg | [2.5,21] (m) | - |  missing |
| zones[1].gap | 0.75 (m) | - |  missing |
| zones[1].glow | 0 (i) | - |  missing |
| zones[1].living | 0 (i) | - |  missing |
| zones[1].mag | 1.25 (m) | - |  missing |
| zones[1].soft | 0.01 (i) | - |  missing |
| zones[1].tilt | [21,8.5] (m) | - |  missing |
| zones[1].tip | 0.45 (g) | - |  missing |
| zones[1].uv | 1 (i) | - |  missing |
| zones[1].uvR | 0.5 (i) | - |  missing |
| zones[2].cpd | 3.6 (m) | - |  missing |
| zones[2].deg | [5,4] (i) | - |  missing |
| zones[2].glow | 0 (i) | - |  missing |
| zones[2].living | 0 (i) | - |  missing |
| zones[2].mag | 1.25 (m) | - |  missing |
| zones[2].soft | 0.01 (i) | - |  missing |
| zones[2].uv | 1 (i) | - |  missing |
| zones[2].uvR | 0.5 (i) | - |  missing |
