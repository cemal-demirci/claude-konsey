# Bir konsey toplantısını çalıştırır ve her olayı zaman damgasıyla kaydeder.
# Kullanım: python3 run.py <eklenti-klasörü> "<soru>" <çıktı.jsonl> <çalışma-klasörü>
import subprocess, sys, time, json
plug, q, out = sys.argv[1], sys.argv[2], sys.argv[3]
cmd=["claude","-p","--plugin-dir",plug,"--setting-sources","project","--output-format","stream-json","--verbose",
     "--allowedTools","Skill","Agent","Read","Glob","Grep","--max-turns","40", "kurtlar konseyi topla: "+q]
t0=time.time()
p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,cwd=sys.argv[4])
with open(out,"w") as f:
    for line in p.stdout:
        f.write(json.dumps({"t":round(time.time()-t0,2),"e":json.loads(line)},ensure_ascii=False)+"\n")
p.wait()
