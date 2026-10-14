import json,sys
CANON={
'bird':["10.1016/j.tree.2018.03.001","10.1242/jeb.246063","10.1007/s10336-007-0213-6","10.1371/journal.pone.0098631","10.1093/molbev/msg108","10.1186/1471-2148-13-36","10.7554/eLife.15675","10.1098/rstb.2009.0044","10.1242/jeb.243129"],
'plant':["10.1242/jeb.015396","10.1159/000314278","10.3389/fpls.2015.00207","10.1098/rspb.2020.1393","10.5061/dryad.3xsj3txq7","10.1093/acprof:oso/9780199581139.001.0001","10.1017/S0952523813000035","10.1016/j.tree.2009.09.010","10.1111/ele.12205","10.1007/s00239-004-0294-2","10.1038/ncomms8852","10.5061/dryad.5rs50","10.1007/s10265-016-0785-4","10.1038/s41586-019-1693-2"],
}
PT='diel; eye_type; sense_chemical; sense_light_nonvisual'
NOEYE=' eye_type: none in this genus (a plant has no eye; no source states it).'
def s(**k):
    k.setdefault('level','genus'); k.setdefault('where',['WebSearch','WebFetch']); k.setdefault('date','2026-10-14')
    if isinstance(k.get('canon'),str): k['canon']=CANON[k['canon']]
    open('/tmp/ws10/docs/views/searched/sweep-10.jsonl','a').write(json.dumps(k,ensure_ascii=False)+'\n')
def w(**k):
    for f in('for','rows','views'):
        if f in k: assert isinstance(k[f],list)
    k['records']=int(k.get('records',0)); k['priority']=int(k.get('priority',2)); assert isinstance(k['get'],str)
    open('/tmp/ws10/docs/views/wanted/sweep-10.jsonl','a').write(json.dumps(k,ensure_ascii=False)+'\n')
