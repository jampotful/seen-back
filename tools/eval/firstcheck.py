"""First integrity checks for the evaluation set and its vectors.

Usage: python3 tools/eval/firstcheck.py <root>
<root> is a directory that holds data/ (the published data) and lab/<model>/
(the published vectors), laid out as on the pub/data-alachua and pub/lab-* branches.

It checks that every evaluation row is dated 2025-01-01 or later, that ids are
unique, that each model's vector rows are in manifest order, and it recomputes
BioCLIP 2 species accuracy against scientific names on the test split without
a prior, with a bootstrap interval over photos (2,000 resamples, seed 0).
"""
import sys
import csv, json, os, numpy as np
from collections import Counter
A=sys.argv[1]
rows=list(csv.DictReader(open(f'{A}/data/eval/alachua-2025/manifest.csv')))
print('rows',len(rows),'min date',min(r['date'] for r in rows),'max date',max(r['date'] for r in rows))
print('rows dated before 2025-01-01:',sum(r['date']<'2025-01-01' for r in rows))
print('split',dict(Counter(r['split'] for r in rows)))
print('unique id',len({r['id'] for r in rows}),'gbif_id',len({r['gbif_id'] for r in rows}),'obs_url',len({r['obs_url'] for r in rows}),'photo_url',len({r['photo_url'] for r in rows}))
print('month field equals month of date in',sum(int(r['month'])==int(r['date'][5:7]) for r in rows),'rows')
sp=json.load(open(f'{A}/data/regions/us-fl-alachua/species.json'))['species']
print('species',len(sp),'unique keys',len({s['key'] for s in sp}),'unique sci',len({s['sci'] for s in sp}))
key2i={s['key']:i for i,s in enumerate(sp)}
mid=[r['id'] for r in rows]
for model in sorted(os.listdir(f'{A}/lab')):
    p=f'{A}/lab/{model}/images/alachua-2025'
    try:
        ids=json.load(open(p+'.ids.json'))
        if isinstance(ids,dict): ids=ids.get('ids') or ids.get('rows')
        E=np.load(p+'.f16.npy',mmap_mode='r')
        print(model,'vectors',E.shape,str(E.dtype),'ids',len(ids),'order equals manifest',ids==mid,'same set',set(ids)==set(mid),'skipped',open(p+'.skipped.json').read().strip())
    except Exception as e: print(model,'ERR',e)
# independent recomputation, BioCLIP 2, scientific names, no prior
m='bioclip2-l14'; p=f'{A}/lab/{m}/images/alachua-2025'
ids=json.load(open(p+'.ids.json'))
if isinstance(ids,dict): ids=ids.get('ids') or ids.get('rows')
byid={r['id']:r for r in rows}; R=[byid[i] for i in ids]
E=np.load(p+'.f16.npy').astype(np.float32); print('non-finite image values',int((~np.isfinite(E)).sum())); E/=np.linalg.norm(E,axis=1,keepdims=True)
S=np.load(f'{A}/lab/{m}/text/species_sci.f16.npy').astype(np.float32); S/=np.linalg.norm(S,axis=1,keepdims=True)
L=json.load(open(f'{A}/lab/{m}/text/species_sci.labels.json'))
print('labels type',type(L).__name__, (list(L.keys())[:5] if isinstance(L,dict) else L[:2]))
y=np.array([key2i.get(int(r['key']),-1) for r in R]); te=np.array([r['split']=='test' for r in R]); va=~te
Z=E@S.T; o=np.argsort(-Z,1)[:,:5]
t1=o[:,0]==y; t5=(o==y[:,None]).any(1)
print(m,'species_sci no prior: test n',int(te.sum()),'top1 %.4f top5 %.4f | val n %d top1 %.4f top5 %.4f'%(t1[te].mean(),t5[te].mean(),va.sum(),t1[va].mean(),t5[va].mean()))
print('test rows whose species key is absent from the list: %d of %d (ceiling %.4f)'%((y[te]<0).sum(),te.sum(),(y[te]>=0).mean()))
# text rows that are exact duplicates of another row
u=np.unique(np.round(S,4),axis=0).shape[0]; print('distinct species_sci text rows',u,'of',S.shape[0])
rng=np.random.default_rng(0); n=int(te.sum()); a1=t1[te].astype(np.float32); a5=t5[te].astype(np.float32)
ix=rng.integers(0,n,(2000,n)); b1=a1[ix].mean(1); b5=a5[ix].mean(1)
print('bootstrap over test photos, 2000 resamples: top1 %.4f [%.4f, %.4f]  top5 %.4f [%.4f, %.4f]'%(a1.mean(),*np.percentile(b1,[2.5,97.5]),a5.mean(),*np.percentile(b5,[2.5,97.5])))
dup=[s for s,c in Counter(x['sci'] for x in sp).items() if c>1]
print('scientific names carried by more than one species key:',[(d,[x['key'] for x in sp if x['sci']==d]) for d in dup])
