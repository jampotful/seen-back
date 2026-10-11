"""Leaks and soft spots in the evaluation: dates, overlaps, near-copies, kinds, rare species, outings, pets and garden plants.

usage: python3 -I tools/audit/softspots.py ROOT REPO OUT.json
Reuses only tools/audit/recompute.py (the audit's own reading of the page's rule).
"""
import csv, json, re, sys, os
from collections import Counter, defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recompute as rc

B = 2000
RNG = np.random.default_rng(11)


def pct(x):
    return None if x is None else round(100 * float(x), 1)


def share(flags):
    f = np.asarray(flags, bool)
    return [int(f.sum()), int(len(f)), pct(f.mean()) if len(f) else None]


def group_ci(flags, groups):
    """95% percentile interval resampling whole groups; returns (share, lo, hi, groups)."""
    f = np.asarray(flags, float)
    g = np.asarray(groups)
    uniq, inv = np.unique(g, return_inverse=True)
    sums = np.bincount(inv, weights=f, minlength=len(uniq))
    cnts = np.bincount(inv, minlength=len(uniq)).astype(float)
    draws = RNG.integers(0, len(uniq), size=(B, len(uniq)))
    m = sums[draws].sum(axis=1) / cnts[draws].sum(axis=1)
    return [pct(f.mean()), pct(np.percentile(m, 2.5)), pct(np.percentile(m, 97.5)), int(len(uniq))]


def photo_ci(flags):
    f = np.asarray(flags, float)
    draws = RNG.integers(0, len(f), size=(B, len(f)))
    m = f[draws].mean(axis=1)
    return [pct(f.mean()), pct(np.percentile(m, 2.5)), pct(np.percentile(m, 97.5)), int(len(f))]


def photo_id(url):
    m = re.search(r'/photos/(\d+)/', url)
    return int(m.group(1)) if m else None


def max_cos(A, Bm, chunk=8000):
    """for each row of A, the largest cosine to any row of Bm and its index."""
    best = np.full(len(A), -2.0, np.float32)
    arg = np.zeros(len(A), np.int64)
    for s in range(0, len(Bm), chunk):
        C = A @ Bm[s:s + chunk].T
        j = C.argmax(axis=1)
        v = C[np.arange(len(A)), j]
        upd = v > best
        best[upd] = v[upd]
        arg[upd] = j[upd] + s
    return best, arg


def main(root, repo, outpath):
    out = {}
    man = rc.read_manifest(f'{root}/data/eval/alachua-2025/manifest.csv')
    row = {r['id']: r for r in man}
    tman = rc.read_manifest(f'{root}/data/train/alachua-pre2025/manifest.csv')
    sp = json.load(open(f'{root}/data/regions/us-fl-alachua/species.json'))
    species = sp['species']

    # ---- dates and overlaps
    ev_dates = sorted(r['date'] for r in man)
    tr_dates = sorted(r['date'] for r in tman)
    out['dates'] = {'eval_first': ev_dates[0], 'eval_last': ev_dates[-1], 'train_first': tr_dates[0], 'train_last': tr_dates[-1],
                    'species_list_records_through': sp['source']['records_through'],
                    'species_list_query': sp['source']['doi_or_query'][:200],
                    'eval_rows_before_2025': sum(d < '2025-01-01' for d in ev_dates),
                    'train_rows_after_2024': sum(d > '2024-12-31' for d in tr_dates)}
    ev_pid = Counter(photo_id(r['photo_url']) for r in man)
    tr_pid = Counter(photo_id(r['photo_url']) for r in tman)
    out['overlaps'] = {
        'eval_photo_ids_repeated': sum(1 for v in ev_pid.values() if v > 1),
        'eval_obs_urls_repeated': sum(1 for v in Counter(r['obs_url'] for r in man).values() if v > 1),
        'eval_gbif_ids_repeated': sum(1 for v in Counter(r['gbif_id'] for r in man).values() if v > 1),
        'photo_ids_in_both_train_and_eval': len(set(ev_pid) & set(tr_pid)),
        'train_photo_ids_repeated': sum(1 for v in tr_pid.values() if v > 1),
        'train_largest_photo_id': max(k for k in tr_pid if k), 'eval_smallest_photo_id': min(k for k in ev_pid if k),
        'eval_photo_ids_below_train_largest': sum(1 for k in ev_pid if k and k < max(tr_pid)),
    }
    # split as a function of gbif_id alone: same gbif_id never on both sides (trivially, one row each); record shares
    out['split_counts'] = dict(Counter(r['split'] for r in man))

    # ---- vectors
    ids = json.load(open(f'{root}/bc2/images/alachua-2025.ids.json'))
    Ebc = rc.unit(rc.load_f16_npy(f'{root}/bc2/images/alachua-2025.f16.npy'))
    Etc = rc.unit(rc.load_f16_npy(f'{root}/tc39/images/alachua-2025.f16.npy'))
    Ewa = rc.unit(rc.load_f16_npy(f'{root}/tc39/images/alachua-2025.wasm-int8-per-channel.f16.npy'))
    assert json.load(open(f'{root}/tc39/images/alachua-2025.ids.json')) == ids
    split = np.array([row[x]['split'] for x in ids])
    test = np.where(split == 'test')[0]
    val = np.where(split == 'val')[0]
    key = np.array([int(row[x]['key']) for x in ids])
    date = np.array([row[x]['date'] for x in ids])
    eyes = np.array([row[x]['eyes'] for x in ids])
    month = np.array([int(row[x]['month']) - 1 for x in ids])

    # ---- near-copies, test against val (val fitted pocket v2's rows and set every threshold)
    bv, ba = max_cos(Ebc[test], Ebc[val])
    tv, ta = max_cos(Etc[test], Etc[val])
    same_sd_val = set(zip(key[val], date[val]))
    twin_val = np.array([(key[i], date[i]) in same_sd_val for i in test])
    nc = {}
    for th in (0.95, 0.98, 0.99, 0.995, 0.999):
        m = bv > th
        nc[f'bioclip2_cos_gt_{th}'] = {'test_photos': int(m.sum()), 'same_species': int((key[val][ba[m]] == key[test][m]).sum()),
                                       'same_species_same_date': int(((key[val][ba[m]] == key[test][m]) & (date[val][ba[m]] == date[test][m])).sum())}
        m2 = tv > th
        nc[f'tinyclip39_cos_gt_{th}'] = {'test_photos': int(m2.sum()), 'same_species': int((key[val][ta[m2]] == key[test][m2]).sum())}
    nc['same_species_same_date_on_val'] = int(twin_val.sum())
    out['near_copies_test_vs_val'] = nc

    # ---- near-copies, test against the training photos (TinyCLIP 39M original vectors; BioCLIP 2's are unpublished)
    tids = json.load(open(f'{root}/tc39/images/alachua-pre2025.ids.json'))
    trow = {r['id']: r for r in tman}
    Etr = rc.unit(rc.load_f16_npy(f'{root}/tc39/images/alachua-pre2025.f16.npy'))
    trkey = np.array([int(trow[x]['key']) for x in tids])
    trdate = np.array([trow[x]['date'] for x in tids])
    rv, ra = max_cos(Etc[test], Etr)
    nt = {'training_rows_with_vectors': len(tids)}
    for th in (0.98, 0.99, 0.995, 0.999):
        m = rv > th
        nt[f'tinyclip39_cos_gt_{th}'] = {'test_photos': int(m.sum()), 'same_species': int((trkey[ra[m]] == key[test][m]).sum())}
    # examples of the closest pairs, for a person to look at
    order = np.argsort(-rv)[:12]
    nt['closest_pairs'] = [{'test': ids[test[i]], 'test_obs': row[ids[test[i]]]['obs_url'], 'test_date': date[test[i]], 'train': tids[ra[i]],
                            'train_obs': trow[tids[ra[i]]]['obs_url'], 'train_date': trdate[ra[i]], 'cos': round(float(rv[i]), 4),
                            'same_species': bool(trkey[ra[i]] == key[test[i]])} for i in order]
    out['near_copies_test_vs_train'] = nt
    del Etr

    # ---- slots as the page answers
    slots = {'naturalist': (rc.read_slot(f'{repo}/models/naturalist'), Ebc),
             'pocket_live': (rc.read_slot(f'{repo}/models/pocket'), Ewa),
             'pocket_run25_trained_39m': (rc.read_slot(f'{root}/slots/pre2025-39m'), Ewa)}
    T = test
    nrec = {s['key']: s['n'] for s in species}
    rec_t = np.array([nrec.get(k, 0) for k in key[T]])
    res = {}
    for name, (slot, E) in slots.items():
        r = rc.page_rule(slot, E[T], month[T])
        slot['_offers'] = {}
        r0 = rc.page_rule(slot, E[T], month[T], kind_at_override=None)
        slot['_offers'] = {}
        keys = np.array(slot['keys'])
        top_right = keys[r['top']] == key[T]
        kind_right = r['kind'] == eyes[T]
        d = {'all': {'kind_right': share(kind_right), 'kind_asserted': share(r['sure']), 'kind_right_when_asserted': share(kind_right[r['sure']]),
                     'top_species_right': share(top_right), 'named': share(r['named']), 'named_right': share(top_right[r['named']]),
                     'named_if_kind_at_ignored': share(r0['named']), 'named_right_if_kind_at_ignored': share(top_right[r0['named']])}}
        # without near-copies of val photos (same species on the same date, or BioCLIP 2 cosine above 0.995)
        keep = ~(twin_val | (bv > 0.995))
        d['without_val_twins'] = {'photos': int(keep.sum()), 'kind_right': share(kind_right[keep]), 'top_species_right': share(top_right[keep]),
                                  'named': share(r['named'][keep]), 'named_right': share(top_right[r['named'] & keep])}
        keep2 = ~(rv > 0.995)
        d['without_train_near_copies_tinyclip_0.995'] = {'photos': int(keep2.sum()), 'kind_right': share(kind_right[keep2]),
                                                          'top_species_right': share(top_right[keep2]), 'named': share(r['named'][keep2]),
                                                          'named_right': share(top_right[r['named'] & keep2])}
        # by kind of eye
        bk = {}
        for k in sorted(set(eyes[T]), key=lambda k: -(eyes[T] == k).sum()):
            m = eyes[T] == k
            bk[k] = {'photos': int(m.sum()), 'kind_right': pct(kind_right[m].mean()), 'kind_asserted': pct(r['sure'][m].mean()),
                     'kind_right_when_asserted': pct(kind_right[m & r['sure']].mean()) if (m & r['sure']).any() else None,
                     'top_species_right': pct(top_right[m].mean()), 'named': pct(r['named'][m].mean()),
                     'named_right': pct(top_right[m & r['named']].mean()) if (m & r['named']).any() else None,
                     'named_n': int((m & r['named']).sum())}
        d['by_kind'] = bk
        # by the species' records before 2025
        br = {}
        for lo, hi in ((0, 0), (1, 2), (3, 9), (10, 49), (50, 199), (200, 10 ** 9)):
            m = (rec_t >= lo) & (rec_t <= hi)
            br[f'{lo}-{hi if hi < 10 ** 9 else "more"}'] = {'photos': int(m.sum()), 'top_species_right': pct(top_right[m].mean()) if m.any() else None,
                                                          'named': pct(r['named'][m].mean()) if m.any() else None,
                                                          'named_right': pct(top_right[m & r['named']].mean()) if (m & r['named']).any() else None,
                                                          'named_n': int((m & r['named']).sum())}
        d['by_records'] = br
        # outings: resample whole groups
        g_sd = np.array([f'{a}|{b}' for a, b in zip(key[T], date[T])])
        g_d = date[T]
        d['intervals'] = {
            'kind_right': {'photos': photo_ci(kind_right), 'species_day': group_ci(kind_right, g_sd), 'day': group_ci(kind_right, g_d)},
            'named_right': {'photos': photo_ci(top_right[r['named']]), 'species_day': group_ci(top_right[r['named']], g_sd[r['named']]),
                            'day': group_ci(top_right[r['named']], g_d[r['named']])},
        }
        res[name] = d
        if name == 'naturalist':
            # coin's edge: w_kind 0.5 under the mix rule; photos where the kinds head and the species list disagree
            labels = slot['man']['kinds']['labels']
            pk_, qk_ = r['p'].argmax(axis=1), r['q'].argmax(axis=1)
            dis = pk_ != qk_
            d['heads_disagree'] = {'photos': share(dis), 'kind_right_when_disagree': share(kind_right[dis]),
                                   'winner_is_kinds_head': share((r['cc'].argmax(axis=1) == pk_)[dis]),
                                   'not_sure_when_disagree': share(~r['sure'][dis]),
                                   'kind_right_if_species_list_alone_when_disagree': share((np.array(labels)[qk_] == eyes[T])[dis])}
    out['slots'] = res

    # ---- what a person photographing a pet, a houseplant or a garden flower meets: are they in the list?
    names = {s['sci']: s['n'] for s in species}
    probe = ['Felis catus', 'Canis familiaris', 'Canis lupus', 'Equus caballus', 'Bos taurus', 'Ovis aries', 'Capra hircus', 'Gallus gallus',
             'Monstera deliciosa', 'Epipremnum aureum', 'Dracaena trifasciata', 'Sansevieria trifasciata', 'Ficus lyrata', 'Ficus elastica',
             'Chlorophytum comosum', 'Spathiphyllum wallisii', 'Zamioculcas zamiifolia', 'Phalaenopsis aphrodite', 'Aloe vera',
             'Hydrangea macrophylla', 'Rosa chinensis', 'Camellia japonica', 'Gardenia jasminoides', 'Hibiscus rosa-sinensis',
             'Lantana camara', 'Tagetes erecta', 'Zinnia elegans', 'Petunia atkinsiana', 'Pelargonium hortorum', 'Rhododendron indicum',
             'Nandina domestica', 'Ligustrum sinense', 'Lagerstroemia indica', 'Plumbago auriculata', 'Catharanthus roseus']
    out['pets_and_garden'] = {p: names.get(p) for p in probe}
    out['list_species_by_kingdom'] = dict(Counter(s['kingdom'] for s in species))
    json.dump(out, open(outpath, 'w'), indent=1)
    print(json.dumps(out, indent=1)[:3000])


if __name__ == '__main__':
    main(*sys.argv[1:4])
