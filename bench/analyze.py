import json, sys, glob, os
# Kullanım: python3 analyze.py <klasör>  (run.py çıktılarının, *.jsonl, bulunduğu klasör)
S=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else "out")
rows=[]
for f in sorted(glob.glob(S+"/*.jsonl")):
    name=os.path.basename(f)[:-6]
    start={}; desc={}; end={}; res=None; final=""
    for line in open(f):
        d=json.loads(line); t=d["t"]; e=d["e"]
        if e.get("type")=="assistant":
            for c in e["message"].get("content",[]):
                if c.get("type")=="tool_use" and c["name"] in ("Agent","Task"):
                    start[c["id"]]=t; desc[c["id"]]=c["input"].get("description","")
                if c.get("type")=="text": final=c["text"]
        if e.get("type")=="user":
            for c in e["message"].get("content",[]) if isinstance(e["message"].get("content"),list) else []:
                if c.get("type")=="tool_result" and c.get("tool_use_id") in start: end[c["tool_use_id"]]=t
        if e.get("type")=="result": res=e
    open(S+f"/{name}.final.md","w").write(final)
    ph={}
    for k in start:
        if k not in end: continue
        dsc=desc[k]; kind="dagitim" if "görev dağıtımı" in dsc else ("hukum" if "hüküm" in dsc.lower() else "uye")
        ph.setdefault(kind,[]).append((start[k],end[k],dsc))
    out={"run":name,"wall_s":round(res["duration_ms"]/1000) if res else None,"cost":round(res.get("total_cost_usd",0),2) if res else None,
         "models":list((res or {}).get("modelUsage",{}).keys())}
    for k,v in ph.items():
        s=min(a for a,_,_ in v); e_=max(b for _,b,_ in v); tot=sum(b-a for a,b,_ in v)
        out[k]={"n":len(v),"wall":round(e_-s),"sum":round(tot),"max":round(max(b-a for a,b,_ in v))}
    rows.append(out)
for r in rows: print(json.dumps(r,ensure_ascii=False))
