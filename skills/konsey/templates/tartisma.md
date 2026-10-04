# Tartışma biçimi

`{BANNER}` temanın banner başlığıdır (`KONSEY`, `KURTLAR KONSEYİ`…). Başlıklar temadaki `Başlık` sütunundan gelir.
Çizgiler: üst/alt `═` (67 karakter), üye ayırıcı `─` (66 karakter).

```
═══════════════════════════════════════════════════════════════════
                         {BANNER}
     "{sorunun özü, en fazla 15 kelime}"
     mod: {hizli|standart|derin} · üye: {n}
═══════════════════════════════════════════════════════════════════

{ELEŞTİRMEN BAŞLIĞI}
{3–6 cümle, birinci ağızdan. Bu üyenin 1. tur yanıtına dayanır; en tehlikeli varsayımı adıyla söyler.}

──────────────────────────────────────────────────────────────────

{STRATEJİST BAŞLIĞI}
{…}

──────────────────────────────────────────────────────────────────

(Analist, Vizyoner, Mühendis, Filozof sırasıyla)

──────────────────────────────────────────────────────────────────

{HÜMANİST BAŞLIĞI}
{…}
```

Yalnızca `derin` modda, Hümanist'ten sonra ve başkandan önce:

```
──────────────────────────────────────────────────────────────────

ÇAPRAZ SORGU — isimsiz sıralama
  Puanlar: Üye {harf} ({isim}) {puan} · Üye {harf} ({isim}) {puan} · … (yüksekten düşüğe, hepsi)
  İtirazlar: {isim} → {hedef isim}: {tek cümle} (üye başına bir satır)
  Fikrini değiştiren: {isimler ya da "yok"}
```

Sıralama üyelere harflerle (isimsiz) yaptırılır; isimler bu bölümde açılır.

## Kurallar

- Eleştirmen hep ilk, Hümanist hep son konuşur. Ortadaki sıra konuya göre değişebilir. `--uyeler` ile alt küme
  seçildiyse yalnızca seçilen üyeler konuşur (aynı sıra kuralıyla).
- Her üye birinci ağızdan konuşur ("Eleştirmen düşünüyor ki…" değil).
- Her üye en az bir kez başka bir üyeye adıyla gönderme yapar. Bu göndermeler başkanın eklediği bağlantılardır;
  üyenin pozisyonunu değiştirmez.
- Derin modda pozisyonunu güncelleyen üye bunu açıkça söyler: "…itirazından sonra fikrimi değiştirdim: …".
- `[VARSAYIM]` olan bir şeyi üye ağzından kesin bilgi gibi yazma; "sanıyorum", "doğrulanmadı" gibi işaretle.
