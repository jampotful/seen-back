import json,subprocess,sys
def src(a,y,t,j,doi,url,acc): return {"authors":a,"year":y,"title":t,"journal":j,"doi":doi,"url":url,"access":acc}
def P(taxon,fam,order,trait,value,method,s,where,quote,note="",partial=False,rank="species"):
    r={"taxon":taxon,"rank":rank,"family":fam,"order":order,"trait":trait,"value":value,"units":"","eye":"","method":method,"conditions":"","source":s,"where":where,"quote":quote,"opened":True,"grade":"m","note":note}
    if partial: r["partial"]=True
    return r
def add(L):
    p='/tmp/ws8/pending.jsonl'
    open(p,'w').write("\n".join(json.dumps(x,ensure_ascii=False) for x in L))
    r=subprocess.run("cd /tmp/ws8 && python3 -I tools/senses/addlog.py sweep-8 < pending.jsonl",shell=True,capture_output=True,text=True)
    print(r.stdout,r.stderr)
