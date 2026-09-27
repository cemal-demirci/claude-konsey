# Konsey

**Zor bir kararı yedi uzmana tartıştıran, sonunda net bir hüküm veren Claude Code eklentisi.**

Konsey'e bir soru sorarsınız ("Ürünü önce ücretsiz mi çıkaralım?", "Mikroservise şimdi mi geçelim?",
"Bu işi bırakmalı mıyım?"). Yedi üye (eleştirmen, stratejist, analist, vizyoner, mühendis, filozof, hümanist)
**birbirinin cevabını görmeden** kendi görüşünü yazar. Ardından başkan oy saymadan gerekçeleri tartar ve şunları
verir: tek cümlelik karar, gerekçeli bir güven yüzdesi, 3 kritik risk, 5 somut adım ve bir azınlık görüşü.

Her şey Claude içinde çalışır: dış model, API anahtarı ya da ek ücret yoktur.

```
═══════════════════════════════════════════════════════════════════
                         KURTLAR KONSEYİ
      "Ezan Molası önce reklamlı mı, yoksa Pro olarak mı çıksın?"
     mod: standart · üye: 7
═══════════════════════════════════════════════════════════════════

⚔ TESTERE NECMİ
Bak, lafı dolandırmayacağım. İki ayrı paket açarsan kendi adamlarını ikiye bölersin…
```

Tam örnekler için [`examples/`](examples/) klasörüne bakın.

---

## Neden bir konsey?

Tek bir yapay zekâya "sence?" diye sorunca genellikle "bir yandan… öte yandan…" cevabı gelir. Konsey bunu
değiştirir:

- **Bağımsız görüşler.** Her üye ayrı bir alt-ajandır ve diğerlerinin cevabını görmez. Böylece yedi üye aynı
  sesin yedi tonuna dönüşmez.
- **Olgu ile varsayım ayrılır.** Konsey toplanmadan önce projenizden ve sohbetten bir "dosya" hazırlanır. Her bilgi
  `[OLGU]`, `[VARSAYIM]` ya da `[BİLİNMİYOR]` olarak etiketlenir. Başkan, olguya dayanan görüşe daha fazla ağırlık verir.
- **Başkan oy saymaz.** Çoğunluğa rağmen tek bir üyenin haklı olduğuna karar verebilir. Güven yüzdesinin nereden
  geldiğini de söyler: üyelerin dağılımı, kanıtın gücü ve bilinmeyenlerin sayısı.
- **"Fikrimi değiştirir".** Her karar, kendisini tersine çevirecek tek bir olguyu yazar. O olguyu öğrenince
  konseyi yeniden toplayın.
- **Çapraz sorgu (derin mod).** Üyeler birbirinin görüşüne itiraz eder ve isimleri gizlenmiş görüşleri sıralar.

## Kurulum

### Claude Code eklentisi (önerilen)

```bash
claude plugin marketplace add cemal-demirci/claude-konsey
claude plugin install konsey@claude-konsey
```

Ya da Claude Code içinde:

```
/plugin marketplace add cemal-demirci/claude-konsey
/plugin install konsey@claude-konsey
```

### Elle (eklenti sistemi olmadan)

```bash
git clone https://github.com/cemal-demirci/claude-konsey
cd claude-konsey
scripts/install.sh                      # klasik tema, standart mod
scripts/install.sh --tema kurtlar       # varsayılanı Kurtlar Konseyi yap
```

Kurulumdan sonra yeni bir Claude Code oturumu açın.

## Kullanım

Düz metinle:

```
konseyi topla: Uygulamayı önce reklamlı mı yoksa ücretli mi çıkaralım?
kurtlar konseyi: Monolitten mikroservise şimdi mi geçmeli?
konseye sor, derin mod: Bu teklifi kabul etmeli miyim?
```

Ya da komutla:

```
/konsey:topla --tema kurtlar --mod derin Ekibe iki kişi mi alalım, bir kıdemli mi?
/konsey:topla --uyeler eleştirmen,mühendis,analist Postgres'ten ClickHouse'a geçmeli miyiz?
```

Konsey yalnızca açıkça istediğinizde toplanır, sıradan kod işlerinde araya girmez. Soruyu hangi dilde
yazarsanız tartışma o dilde yapılır.

### Modlar

| Mod | Ne yapar | Alt-ajan | Ne zaman |
|---|---|---|---|
| `hizli` | Yedi üyeyi tek metinde yazar | 0 | Hızlı bir fikir almak; alt-ajan olmayan ortamlar (claude.ai) |
| `standart` | Yedi üye paralel ve bağımsız + başkan | 7 | Varsayılan |
| `derin` | Standart + çapraz sorgu ve isimsiz sıralama | 14 | Geri dönüşü zor, büyük kararlar |

Alt-ajan sayısı süreyi ve kullanım kotasını doğrudan etkiler. Derin mod, standart modun yaklaşık iki katı sürer.

### Temalar

| Tema | Üyeler |
|---|---|
| `klasik` (varsayılan) | Eleştirmen, Stratejist, Analist, Vizyoner, Mühendis, Filozof, Hümanist · Başkan |
| `kurtlar` | Testere Necmi, Nizamettin Güvenç, İplikçi Nedim, Laz Ziya, Kılıç, Hüsrev Ağa, Polat Alemdar · Baron Mehmet Karahanlı |

Tema yalnızca isimleri ve konuşma üslubunu değiştirir. Üyelerin uzmanlığı ve dürüstlük kuralları her temada aynıdır.

### Varsayılanları değiştirmek

En kolay yol, `~/.claude/CLAUDE.md` dosyasına tek satır eklemek. Bu dosya her oturumda yüklenir, izin sorulmaz:

```
Konsey teması: kurtlar · Konsey modu: standart
```

Alternatif olarak `~/.claude/konsey.json` dosyası da kullanılabilir. `scripts/install.sh --tema kurtlar` bu dosyayı
yazar:

```json
{ "tema": "kurtlar", "mod": "standart" }
```

### Karar defteri

Karardan sonra "kaydet" derseniz karar, projenin kökündeki `KONSEY.md` dosyasına tarihiyle eklenir. Sonra
"şu karar böyle sonuçlandı, konsey yeniden değerlendirsin" diyebilirsiniz; eski karar ve yeni olgu dosyaya
eklenerek konsey yeniden toplanır. İstemediğiniz sürece konsey hiçbir dosya yazmaz.

## Yeni tema eklemek

`skills/konsey/themes/<ad>.md` dosyası oluşturun ve [`klasik.md`](skills/konsey/themes/klasik.md)
dosyasındaki tabloyu doldurun. Tabloda 7 rol ve başkan olmak üzere 8 satır, ayrıca bir `Banner başlığı:` satırı
bulunmalı. Ardından denetimi çalıştırın:

```bash
python3 scripts/validate.py
```

## Geliştirme

```
.claude-plugin/        plugin.json, marketplace.json
skills/konsey/         SKILL.md, personas/, themes/, protocol/, templates/
agents/konsey-uyesi.md üye alt-ajanı (yalnızca Read/Grep/Glob)
commands/topla.md      /konsey:topla komutu
evals/                 claude plugin eval senaryoları
scripts/               validate.py, install.sh
```

```bash
python3 scripts/validate.py          # yapı denetimi (CI'da da çalışır)
claude plugin validate .             # Claude Code manifest denetimi
claude plugin eval . --ablation none # davranış testleri (kullanım kotası harcar)
```

Değerlendirme senaryoları şunları sınar:
- Konsey istenince tetikleniyor mu, sıradan bir kod sorusunda tetiklenmiyor mu?
- Kurtlar teması doğru isimleri kullanıyor mu?
- Standart mod gerçekten yedi alt-ajan başlatıyor mu?
- Karar biçimi doğru mu?

## Katkı ve teşekkür

- Persona dosyaları ve ilk fikir: [itshussainsprojects/Claude-Council-Skill](https://github.com/itshussainsprojects/Claude-Council-Skill) (MIT).
  Bu proje onun üzerine bağımsız alt-ajan protokolü, çapraz sorgu, bağlam dosyası, gerekçeli güven, temalar ve
  eklenti paketlemesi ekler.
- Bağımsız görüş ve isimsiz sıralama fikri, "LLM council" yaklaşımından esinlenmiştir.
- `kurtlar` teması, Kurtlar Vadisi dizisine yapılmış bir hayran göndermesidir. Dizinin yapımcılarıyla ya da
  oyuncularıyla hiçbir bağı yoktur. Karakterler yalnızca üslup olarak kullanılır ve diziden replik alıntılanmaz.

## Lisans

MIT. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

---

## English

**Konsey** ("council") is a Claude Code plugin that runs a hard decision past seven expert members: adversary,
strategist, analyst, visionary, engineer, philosopher and humanist. Each member is a separate subagent and answers
without seeing the others. A chair then weighs the arguments instead of counting votes. The verdict is a
one-sentence position, a reasoned confidence score, 3 critical risks, 5 next steps and a minority report.
Everything runs inside Claude, with no external models or API keys.

Install: `claude plugin marketplace add cemal-demirci/claude-konsey && claude plugin install konsey@claude-konsey`.
Use: `/konsey:topla [--mod hizli|standart|derin] [--tema klasik|kurtlar] <question>`, or just write "council: …".
The debate is held in the language you ask in.
