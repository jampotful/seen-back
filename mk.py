import json,sys
CANON={
'bird':["10.1016/j.tree.2018.03.001","10.1242/jeb.246063","10.1007/s10336-007-0213-6","10.1371/journal.pone.0098631","10.1093/molbev/msg108","10.1186/1471-2148-13-36","10.7554/eLife.15675","10.1098/rstb.2009.0044","10.1242/jeb.243129"],
}
def s(**k):
    k.setdefault('level','genus'); k.setdefault('where',['WebSearch','WebFetch']); k.setdefault('date','2026-10-14')
    if isinstance(k.get('canon'),str): k['canon']=CANON[k['canon']]
    open('/tmp/ws10/docs/views/searched/sweep-10.jsonl','a').write(json.dumps(k,ensure_ascii=False)+'\n')
def w(**k):
    for f in('for','rows','views'):
        if f in k: assert isinstance(k[f],list)
    k['records']=int(k.get('records',0)); k['priority']=int(k.get('priority',2)); assert isinstance(k['get'],str)
    open('/tmp/ws10/docs/views/wanted/sweep-10.jsonl','a').write(json.dumps(k,ensure_ascii=False)+'\n')
