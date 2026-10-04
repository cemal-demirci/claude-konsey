import json, subprocess, sys, os, re
# Kullanım: python3 judge.py <klasör> <önek-A> <önek-B> <çıktı.json>
# Klasörde {önek}{1,2,3}.final.md dosyaları olmalı (analyze.py üretir). Her çift iki sırayla puanlanır.
S=os.path.abspath(sys.argv[1]); PA,PB,OUT=sys.argv[2],sys.argv[3],sys.argv[4]
RUB="""Sen bağımsız bir karar-kalitesi hakemisin. Aynı soruya iki farklı "konsey" toplantısının tam çıktısı aşağıda (X ve Y).
Üslubu/karakter sesini PUANLAMA; yalnızca karar kalitesini puanla. Her ölçütü 1-10 ver:
1 gorev: görev dağılımı kararı gerçekten belirleyen alt sorulara mı yöneliyor, örtüşme yok mu, bilinmeyenler sahiplenilmiş mi
2 hukum: hüküm kanıtı tartıyor mu (olgu>varsayım), azınlık görüşünü ciddiye alıyor mu, oy saymıyor mu
3 kalibrasyon: güven yüzdesi ve gerekçesi kanıtla tutarlı mı
4 eylem: riskler ve adımlar somut, ölçülebilir, bu soruya özgü mü
5 genel: bir karar verici olarak hangisine daha çok güvenirsin
Yalnızca şu JSON'u yaz, başka hiçbir şey yazma:
{"X":{"gorev":n,"hukum":n,"kalibrasyon":n,"eylem":n,"genel":n},"Y":{...},"kazanan":"X"|"Y"|"berabere","gerekce":"tek cümle"}
"""
res=[]
for i in (1,2,3):
    a=open(f"{S}/{PA}{i}.final.md").read(); b=open(f"{S}/{PB}{i}.final.md").read()
    for order in ("AB","BA"):
        X,Y=(a,b) if order=="AB" else (b,a)
        prompt=RUB+"\n=== X ===\n"+X+"\n\n=== Y ===\n"+Y
        r=subprocess.run(["claude","-p","--setting-sources","project","--model","opus","--tools",""],input=prompt,capture_output=True,text=True,cwd=S)
        m=re.search(r"\{[\s\S]*\}",r.stdout); j=json.loads(m.group(0))
        mapx={"X":order[0],"Y":order[1]}
        out={"soru":i,"sira":order,"A":j["X"] if order=="AB" else j["Y"],"B":j["Y"] if order=="AB" else j["X"],
             "kazanan":mapx.get(j["kazanan"],"berabere"),"gerekce":j.get("gerekce","")}
        print(json.dumps(out,ensure_ascii=False),flush=True); res.append(out)
json.dump(res,open(OUT,"w"),ensure_ascii=False,indent=1)
