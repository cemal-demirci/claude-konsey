#!/usr/bin/env python3
"""Gerçek bir konsey çıktısını terminal görünümünde PNG'ye çevirir (README ekran görüntüleri).

Kullanım: scripts/ekran.py <çıktı.md> <hedef.png> --komut "<kullanıcının yazdığı>" [--bas "<metin>"] [--son "<metin>"]
          [--atla "<başlangıç metni>|<bitiş metni>" ...]
--bas/--son: alınacak bölümün ilk ve son satırında geçen metin. --atla: aradaki bir kısmı "⋮" ile kısaltır.
Metin değiştirilmez; yalnızca kesilir ve renklendirilir. Google Chrome (headless) gerekir.
"""
import argparse, html, os, re, subprocess, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
RENK = {"⚔": "#ff7b72", "📈": "#79c0ff", "🔬": "#d2a8ff", "🎨": "#ffa657", "⚙": "#8b949e", "🧘": "#7ee787",
        "❤": "#ff9bce", "🎩": "#e3b341"}

def satir_html(s: str) -> str:
    e = html.escape(s)
    t = s.strip()
    if t and set(t) <= set("═─"):
        return f'<span class="cizgi">{e}</span>'
    if t in ("KURTLAR KONSEYİ", "KONSEY") or t.startswith("KARAR —"):
        return f'<span class="baslik">{e}</span>'
    for k, c in RENK.items():
        if t.startswith(k):
            return f'<span class="uye" style="color:{c}">{e}</span>'
    e = re.sub(r"^(\s*)(KARAR:|GÜVEN:|KRİTİK RİSKLER|SONRAKİ ADIMLAR|AZINLIK GÖRÜŞÜ:|FİKRİMİ DEĞİŞTİRİR:|DAYIYA CEVAP:)",
               r'\1<b class="etiket">\2</b>', e)
    e = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e)
    e = re.sub(r"\*(\(.+?\))\*", r'<i class="not">\1</i>', e)
    e = re.sub(r"\[(OLGU|VARSAYIM|BİLİNMİYOR)\]", r'<span class="tag">[\1]</span>', e)
    if "GÖREV DAĞILIMI" in s:
        e = f'<span class="baslik2">{e}</span>'
    return e

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("girdi"); ap.add_argument("hedef")
    ap.add_argument("--komut", default=""); ap.add_argument("--bas"); ap.add_argument("--son")
    ap.add_argument("--atla", action="append", default=[])
    a = ap.parse_args()
    L = open(a.girdi, encoding="utf-8").read().splitlines()
    bi = next(i for i, l in enumerate(L) if a.bas in l) if a.bas else 0
    si = next(i for i, l in enumerate(L) if i >= bi and a.son in l) if a.son else len(L) - 1
    L = L[bi:si + 1]
    for at in a.atla:
        x, y = at.split("|")
        i = next(i for i, l in enumerate(L) if x in l); j = next(j for j, l in enumerate(L) if j > i and y in l)
        L = L[:i] + ["⋮"] + L[j:]
    govde = "\n".join('<span class="atla">⋮</span>' if l == "⋮" else satir_html(l) for l in L)
    komut = f'<span class="komut">❯ {html.escape(a.komut)}</span>\n\n' if a.komut else ""
    sayfa = f"""<!doctype html><meta charset="utf-8"><style>
    body{{margin:0;background:#0d1117;padding:28px}}
    .pen{{background:#161b22;border:1px solid #30363d;border-radius:12px;overflow:hidden;box-shadow:0 12px 40px #0008;width:1180px}}
    .bar{{height:38px;background:#21262d;display:flex;align-items:center;gap:8px;padding:0 14px;color:#8b949e;font:13px -apple-system,sans-serif}}
    .bar i{{width:12px;height:12px;border-radius:50%;display:inline-block}}
    pre{{margin:0;padding:20px 26px 26px;color:#c9d1d9;font:15px/1.55 "SF Mono",Menlo,monospace;white-space:pre-wrap;word-break:break-word}}
    .komut{{color:#7ee787}} .cizgi{{color:#484f58}} .baslik{{color:#e3b341;font-weight:700}} .baslik2{{color:#e3b341}}
    .uye{{font-weight:700}} .etiket{{color:#58a6ff}} .not{{color:#a5d6ff}} .tag{{color:#8b949e}} .atla{{color:#6e7681}}
    </style><div class="pen"><div class="bar"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i>
    <i style="background:#28c840"></i><span style="margin-left:10px">claude — konsey</span></div>
    <pre>{komut}{govde}</pre></div>"""
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(sayfa)
    h = 150 + 25 * (sum(1 + len(l) // 112 for l in L) + (2 if a.komut else 0))
    subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--force-device-scale-factor=2",
                    f"--window-size=1236,{h}", f"--screenshot={os.path.abspath(a.hedef)}", "file://" + f.name],
                   check=True, capture_output=True)
    print(a.hedef, h)

if __name__ == "__main__":
    main()
