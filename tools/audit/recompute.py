"""Independent recomputation of the headline accuracy numbers in docs/EVAL.md.

Written from the prose of docs/EVAL.md, docs/CONTRACTS.md and tools/fusion/README.md only.
Nothing here imports or copies tools/eval/ or tools/fusion/.

usage: python3 -I tools/audit/recompute.py ROOT REPO OUT.json
  ROOT  a directory holding the published files (see tools/audit/README.md for the layout)
  REPO  a checkout of the repository (models/pocket and models/naturalist are read from it)
"""
import csv, hashlib, json, sys
import numpy as np

KINDS17 = None  # read from each manifest
B = 2000
RNG = np.random.default_rng(7)  # my own seed; EVAL.md's intervals use 20261011 with its own code


def load_f16_npy(path):
    a = np.load(path)
    return a.astype(np.float32)


def unit(a):
    return a / np.linalg.norm(a, axis=1, keepdims=True)


def boot(flags, idx_sets=None):
    """share, and a 95% percentile interval from B resamples over photos."""
    f = np.asarray(flags, dtype=np.float64)
    n = len(f)
    if n == 0:
        return [None, None, None, 0]
    draws = RNG.integers(0, n, size=(B, n))
    m = f[draws].mean(axis=1)
    # the count is kept beside the share so that a percentage is rounded once, from the count (see README)
    return [round(float(f.mean()), 6), round(float(np.percentile(m, 2.5)), 4), round(float(np.percentile(m, 97.5)), 4), n, int(f.sum())]


def read_manifest(path):
    with open(path, newline='') as fh:
        return list(csv.DictReader(fh))


def softmax_rows(z):
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)


def shares_from_weights(W):
    """W: species x 12 weights -> species x 12 share of each month's total."""
    return W / W.sum(axis=0, keepdims=True)


# ---------------------------------------------------------------- Study 1 style (BioCLIP 2, scientific names)

def study1(root, out):
    man = read_manifest(f'{root}/data/eval/alachua-2025/manifest.csv')
    sp = json.load(open(f'{root}/data/regions/us-fl-alachua/species.json'))['species']
    labels = json.load(open(f'{root}/bc2/text/species_sci.labels.json'))['labels']
    assert [l['key'] for l in labels] == [s['key'] for s in sp], 'label rows do not follow the species list'
    T = unit(load_f16_npy(f'{root}/bc2/text/species_sci.f16.npy'))
    ids = json.load(open(f'{root}/bc2/images/alachua-2025.ids.json'))
    E = unit(load_f16_npy(f'{root}/bc2/images/alachua-2025.f16.npy'))
    row = {r['id']: r for r in man}
    assert len(ids) == len(E) == 6000
    test = [i for i, x in enumerate(ids) if row[x]['split'] == 'test']
    keypos = {s['key']: j for j, s in enumerate(sp)}
    eyes_of = np.array([s['eyes'] for s in sp])
    truth = np.array([keypos.get(int(row[ids[i]]['key']), -1) for i in test])
    teyes = np.array([row[ids[i]]['eyes'] for i in test])
    month = np.array([int(row[ids[i]]['month']) - 1 for i in test])
    C = E[test] @ T.T  # cosines, photos x species
    n = np.array([s['n'] for s in sp], dtype=np.float64)
    M = np.array([s['m'] for s in sp], dtype=np.float64)
    lam, c, a_over_t = 2.0, 1.0, 0.012
    W = M + lam * n[:, None] / 12.0 + c
    S = shares_from_weights(W)  # species x 12
    P = C + a_over_t * np.log(S[:, month].T)
    res = {}
    for name, sc in (('noprior', C), ('prior', P)):
        top5 = np.argpartition(-sc, 5, axis=1)[:, :5]
        top1 = sc.argmax(axis=1)
        res[f'top1_{name}'] = boot(top1 == truth)
        res[f'top5_{name}'] = boot((top5 == truth[:, None]).any(axis=1))
        res[f'kind_from_top_species_{name}'] = boot(eyes_of[top1] == teyes)
    # kind from summed species probabilities with the prior, at T=100
    prob = softmax_rows(100.0 * P)
    kinds = sorted(set(eyes_of))
    q = np.stack([prob[:, eyes_of == k].sum(axis=1) for k in kinds], axis=1)
    res['kind_from_summed_species_prior'] = boot(np.array(kinds)[q.argmax(axis=1)] == teyes)
    res['test_photos'] = len(test)
    res['test_species_not_in_list'] = int((truth < 0).sum())
    # paired gain
    g = (P.argmax(axis=1) == truth).astype(float) - (C.argmax(axis=1) == truth).astype(float)
    res['gain_prior_points'] = [round(100 * x, 1) if x is not None else None for x in boot(g)[:3]]
    out['study1_bioclip2_species_sci'] = res
    return dict(test=test, ids=ids, truth=truth, teyes=teyes, month=month, sp=sp, row=row, P=P, C=C, eyes_of=eyes_of)


# ---------------------------------------------------------------- the page's rule, from a slot's own files

def read_slot(slot):
    man = json.load(open(f'{slot}/manifest.json'))
    width = man['width']
    tab = json.load(open(f'{slot}/{man["species"]["table"]}'))
    rows = tab['species']
    K = None
    if 'kinds' in man:
        K = np.frombuffer(open(f'{slot}/{man["kinds"]["url"]}', 'rb').read(), dtype='<f2').astype(np.float32).reshape(-1, width)
    S = np.frombuffer(open(f'{slot}/{man["species"]["url"]}', 'rb').read(), dtype='<f2').astype(np.float32).reshape(-1, width)
    sb = None
    if man['species'].get('bias_url'):
        sb = np.frombuffer(open(f'{slot}/{man["species"]["bias_url"]}', 'rb').read(), dtype='<f4').astype(np.float64)
    kb = np.array(man['kinds'].get('bias', [0.0] * len(man['kinds']['labels'])), dtype=np.float64) if K is not None else None
    assert len(rows) == len(S) == man['species']['count']
    return dict(man=man, K=K, kb=kb, S=S, sb=sb, rows=rows, keys=tab.get('keys'))


def page_rule(slot, E, month, kind_at_override='manifest'):
    """E: photos x width unit vectors; month: 0..11 per photo. Returns per-photo answers as arrays."""
    man, fu = slot['man'], slot['man']['fusion']
    labels = man['kinds']['labels']
    rows = slot['rows']
    sk = np.array([r[2] for r in rows])
    Wm = np.array([r[3] for r in rows], dtype=np.float64)  # species x 12
    share = Wm / Wm.sum(axis=0, keepdims=True)
    floor = fu.get('prior_floor', 1e-6)
    zs = fu['t_species'] * (E.astype(np.float64) @ slot['S'].T.astype(np.float64))
    if slot['sb'] is not None:
        zs = zs + slot['sb'][None, :]
    if fu.get('alpha_prior', 0):
        zs = zs + fu['alpha_prior'] * np.log(np.maximum(share[:, month].T, floor))
    s = softmax_rows(zs)
    zk = fu['t_kind'] * (E.astype(np.float64) @ slot['K'].T.astype(np.float64)) + slot['kb'][None, :]
    p = softmax_rows(zk)
    speaks = np.array([(l in set(sk)) and l != 'none' and (l != 'person' or 'person' in set(sk)) for l in labels])
    q = np.stack([s[:, sk == l].sum(axis=1) for l in labels], axis=1)
    w = fu['w_kind']
    rule = fu.get('rule', 'product')
    if rule == 'mix':
        A = (p * speaks).sum(axis=1, keepdims=True)
        cc = np.where(speaks[None, :], w * p + (1 - w) * A * q, p)
        tot = cc.sum(axis=1, keepdims=True)
        cc = np.where(tot > 0, cc / np.where(tot > 0, tot, 1), p)
    else:
        g = fu.get('guard', 1e-9)
        sc = np.where(speaks[None, :], w * np.log(np.maximum(p, g)) + (1 - w) * np.log(np.maximum(q, g)), np.log(np.maximum(p, g)))
        cc = softmax_rows(sc)
    kidx = cc.argmax(axis=1)
    kind = np.array(labels)[kidx]
    kp = cc[np.arange(len(cc)), kidx]
    kind_at = fu.get('kind_at') if kind_at_override == 'manifest' else kind_at_override
    sure = np.ones(len(kind), bool) if kind_at is None else (kp >= kind_at)
    top = s.argmax(axis=1)
    topp = s[np.arange(len(s)), top]
    alive = ~np.isin(kind, ['none', 'person'])
    named = alive & sure & (topp >= fu['name_at']) & (sk[top] == kind)
    # offers: three likeliest species of the winning kind, when not named and together >= offer_at
    # the README says offers are worked out whether or not the kind is sure, so `sure` is not applied here
    offered = np.zeros(len(kind), bool)
    for i in np.where(alive & ~named)[0]:
        m = sk == kind[i] if not fu.get('offer_any_kind') else np.ones(len(sk), bool)
        idx = np.where(m)[0]
        if len(idx) == 0:
            continue
        o = idx[np.argsort(-s[i, idx], kind='stable')[:3]]
        if s[i, o].sum() >= fu['offer_at']:
            offered[i] = True
            slot.setdefault('_offers', {})[i] = o  # the caller checks the offers against the truth
    return dict(kind=kind, kp=kp, sure=sure, top=top, topp=topp, named=named, offered=offered, s=s, cc=cc, p=p, q=q)


def score_slot(name, slot, E, month, truth_key, truth_eyes, out, extra=None):
    r = page_rule(slot, E, month)
    keys = np.array(slot['keys'])
    topkey = keys[r['top']]
    right_top = topkey == truth_key
    res = {
        'kind_right': boot(r['kind'] == truth_eyes),
        'kind_asserted': boot(r['sure']),
        'kind_right_when_asserted': boot((r['kind'] == truth_eyes)[r['sure']]),
        'top_species_right': boot(right_top),
        'named': boot(r['named']),
        'named_right': boot(right_top[r['named']]),
        'offered': boot(r['offered']),
        'fusion': slot['man']['fusion'],
    }
    offers = slot.get('_offers', {})
    hold = [truth_key[i] in set(keys[o]) for i, o in offers.items()]
    res['offer_holds_species'] = boot(np.array(hold, bool))
    slot['_offers'] = {}
    # kind_at of none, as EVAL.md's table for the slot reports it
    r0 = page_rule(slot, E, month, kind_at_override=None)
    res['with_kind_at_none'] = {'kind_asserted': boot(r0['sure']), 'named': boot(r0['named']), 'named_right': boot(right_top[r0['named']])}
    slot['_offers'] = {}
    # coin's edge for mix with w_kind 0.5: photos whose winning combined probability is within 0.02 of 0.5
    res['winning_kind_p_within_0.02_of_0.5'] = boot(np.abs(r['kp'] - 0.5) < 0.02)
    out[name] = res
    return r


def main(root, repo, outpath):
    out = {'inputs': {}}
    for f in ('data/_made.txt', 'bc2/_made.txt', 'tc39/_made.txt'):
        try:
            out['inputs'][f] = open(f'{root}/{f}').read().strip().splitlines()[:3]
        except OSError:
            pass
    st = study1(root, out)
    test, ids, row = st['test'], st['ids'], st['row']
    truth_key = np.array([int(row[ids[i]]['key']) for i in test])
    E_bc2 = unit(load_f16_npy(f'{root}/bc2/images/alachua-2025.f16.npy'))[test]
    nat = read_slot(f'{repo}/models/naturalist')
    score_slot('naturalist_as_shipped', nat, E_bc2, st['month'], truth_key, st['teyes'], out)
    # pocket on the vectors a phone computes
    pids = json.load(open(f'{root}/tc39/images/alachua-2025.wasm-int8-per-channel.ids.json'))
    assert pids == ids
    E_pk = unit(load_f16_npy(f'{root}/tc39/images/alachua-2025.wasm-int8-per-channel.f16.npy'))[test]
    pk = read_slot(f'{repo}/models/pocket')
    score_slot('pocket_as_shipped', pk, E_pk, st['month'], truth_key, st['teyes'], out)
    # pocket on the extra set's test photos
    cman = {r['id']: r for r in read_manifest(f'{root}/data/extra/coco-kinds/manifest.csv')}
    cids = json.load(open(f'{root}/tc39/images/coco-kinds.wasm-int8-per-channel.ids.json'))
    Ec = unit(load_f16_npy(f'{root}/tc39/images/coco-kinds.wasm-int8-per-channel.f16.npy'))
    csplit = np.array([cman[x]['split'] for x in cids])
    ceyes = np.array([cman[x]['eyes'] for x in cids])
    tm = csplit == 'test'
    tid = [x for x, k in zip(cids, tm) if k]
    # Two month rules for a COCO photo. EVAL.md says "a calendar month by a hash of its id"; the exact hash
    # (sha256 of "month|" + id, first eight hex digits, modulo 12) was read in tools/eval/kinds.py after the
    # manifest's own month column gave a different answer. Both are kept, because the page uses the phone's clock.
    months = {'hash_month': np.array([int(hashlib.sha256(('month|' + x).encode()).hexdigest()[:8], 16) % 12 for x in tid]),
              'manifest_month': np.array([int(cman[x]['month']) - 1 for x in tid])}
    ce = ceyes[tm]
    sp_names = np.array([r[0] for r in pk['rows']])
    for mname, mo in months.items():
        rc = page_rule(pk, Ec[tm], mo)
        pk['_offers'] = {}
        ex = {'photos': int(tm.sum()), 'kind_right_pooled': boot(rc['kind'] == ce), 'kind_asserted': boot(rc['sure']),
              'kind_right_when_asserted': boot((rc['kind'] == ce)[rc['sure']]), 'species_named': boot(rc['named']),
              'by_kind': {}}
        for k in sorted(set(ce)):
            m = ce == k
            nm = sp_names[rc['top'][m & rc['named']]]
            ex['by_kind'][k] = {'photos': int(m.sum()), 'kind_right': boot(rc['kind'][m] == k), 'species_named': boot(rc['named'][m]),
                                'kind_said': {kk: int(v) for kk, v in zip(*np.unique(rc['kind'][m], return_counts=True))},
                                'names_given': {kk: int(v) for kk, v in zip(*np.unique(nm, return_counts=True))}}
        ex['kind_right_mean_of_five'] = round(float(np.mean([ex['by_kind'][k]['kind_right'][0] for k in ex['by_kind']])), 4)
        # cats named, month by month (the page uses the phone's clock)
        ex['cat_named_by_calendar_month'] = []
        for mo_ in range(12):
            r12 = page_rule(pk, Ec[tm][ce == 'cat'], np.full((ce == 'cat').sum(), mo_))
            pk['_offers'] = {}
            ex['cat_named_by_calendar_month'].append(round(float(r12['named'].mean()), 3))
        out[f'pocket_extra_test_{mname}'] = ex
    json.dump(out, open(outpath, 'w'), indent=1)
    print(json.dumps(out, indent=1)[:6000])


if __name__ == '__main__':
    main(*sys.argv[1:4])
