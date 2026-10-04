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
  Puanlar ve itirazlar karardan önce ayrı bir `ÇAPRAZ SORGU` bölümünde gösterilir.

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
scripts/install.sh --tema kurtlar --mod hizli
```

Betik skill'i, üye alt-ajanını ve komutu `~/.claude` altına kopyalar (hedef `CLAUDE_HOME` ile değiştirilebilir).
Elle kurulumda komutun adı `/konsey-topla`'dır; eklentide `/konsey:topla`. Kurulumdan sonra yeni bir Claude Code
oturumu açın.

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
yazarsanız tartışma o dilde yapılır; Türkçe dışındaki dillerde başlıklar da çevrilir (İngilizcede `VERDICT`,
`CONFIDENCE`, `CRITICAL RISKS`…), kurtlar temasındaki karakter adları aynı kalır.

`--uyeler` ile yalnızca seçtiğiniz üyeler konuşur ve yalnızca onlar için alt-ajan başlatılır. Rol adı
(`eleştirmen` ya da `elestirmen`), İngilizce rol adı (`adversary`) ya da temadaki isim (`Testere Necmi`)
yazabilirsiniz. "üçlü konsey" derseniz konunun en önemli üç sesi seçilir. En az üç üye gerekir.

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

Tema ve mod şu sırayla belirlenir; ilk bulunan geçerlidir:

1. İstekte yazan (`kurtlar konseyi`, `derin mod`, `--tema`, `--mod`)
2. Projenin kökündeki `.claude/konsey.json` (yalnızca o proje için)
3. `CLAUDE.md` ya da hafızadaki bir satır, örneğin `~/.claude/CLAUDE.md` içinde:
   ```
   Konsey teması: kurtlar · Konsey modu: standart
   ```
4. `~/.claude/konsey.json` (`scripts/install.sh --tema kurtlar` bu dosyayı yazar)
5. Varsayılan: `klasik`, `standart`

İki JSON dosyası da aynı biçimdedir; alanlar isteğe bağlıdır:

```json
{ "tema": "kurtlar", "mod": "standart" }
```

Konsey bu dosyaları yalnızca okur. Eklenti, `~/.claude/konsey.json` dosyasını izin sormadan okuyabilmek için
skill'in `allowed-tools` alanında bu tek dosyaya okuma izni ister.

### Karar defteri

Karardan sonra ya da isteğin içinde "kaydet" / "karar defterine yaz" derseniz karar, projenin kökündeki
`KONSEY.md` dosyasının sonuna tarihli bir bölüm olarak eklenir (dosya yoksa oluşturulur):

```
## 2026-10-04 — Kod incelemesi zorunlu olsun mu?
- Mod / tema / üye: hizli / klasik / 7
- Karar: …
- Güven: %70 — …
- Riskler: 1) … 2) … 3) …
- Adımlar: 1) … 2) … 3) … 4) … 5) …
- Azınlık görüşü: …
- Fikrimi değiştirir: …
- Sonuç: (bekleniyor)
```

Sonra "şu karar böyle sonuçlandı, konsey yeniden değerlendirsin" diyebilirsiniz: `Sonuç:` satırı güncellenir, eski
karar ve yeni olgu bağlam dosyasına `[OLGU]` olarak eklenip konsey yeniden toplanır. İstemediğiniz sürece konsey
hiçbir dosya yazmaz; yazabildiği tek dosya `KONSEY.md`'dir.

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
claude plugin validate .             # Claude Code manifest denetimi (CI'da da çalışır)

# davranış testleri (kullanım kotası harcar; tam takım ≈ 5 USD)
claude plugin eval . --ablation none --scaffold --allow-tools Write Edit -j 4
```

`--scaffold`, `varsayilan-*` senaryolarının ayar dosyalarını eval'in geçici çalışma klasörüne ve geçici HOME'una
yazması için;
`--allow-tools Write Edit`, `karar-defteri` senaryosunun `KONSEY.md` yazabilmesi için gerekir. Senaryolar gerçek
`~/.claude` klasörünüze dokunmaz.

### Doğrulama

| Senaryo | Sınadığı özellik | Nasıl |
|---|---|---|
| `tetiklenir` | Konsey isteyince tetiklenme, hızlı mod, karar biçimi, güven gerekçesi | Skill çağrısı, 0 alt-ajan, `KARAR:`/`GÜVEN: %`/`Dağılım:`/`Kanıt:`/`FİKRİMİ DEĞİŞTİRİR:`, LLM hakem |
| `tetiklenmez` | Sıradan kod sorusunda tetiklenmeme | Skill çağrısı yok |
| `standart-alt-ajan` | Standart mod: bağımsız alt-ajanlar, bağlam dosyası | En az 7 alt-ajan, brifinglerde `[OLGU]`/`[VARSAYIM]`/`[BİLİNMİYOR]` |
| `derin-mod` | Çapraz sorgu ve isimsiz sıralama | En az 14 alt-ajan, 7 brifingde `Senin görüşün: Üye X`, çıktıda `ÇAPRAZ SORGU` bölümü, LLM hakem: harflerin yanında isim yok |
| `uyeler-alt-kume` | `/konsey:topla --uyeler` | Tam 3 alt-ajan, `üye: 3`, diğer dört üyenin başlığı yok |
| `kurtlar-tema` | Kurtlar teması | Karakter adları ve başkan |
| `varsayilan-ayar` | `.claude/konsey.json` varsayılanı | Dosya okunuyor, istekte tema/mod yokken kurtlar teması ve hızlı mod (0 alt-ajan) |
| `varsayilan-oncelik` | `~/.claude/konsey.json` ve öncelik sırası | Eval'in geçici HOME'una kullanıcı ayarı (kurtlar, hizli), projeye `klasik` yazılır: tema projeden, mod kullanıcı dosyasından gelir |
| `karar-defteri` | `KONSEY.md` karar defteri | Dosya oluşuyor, tarihli bölümde karar, güven, riskler, adımlar |
| `dil-ingilizce` | Kullanıcının dili | İngilizce etiketler, Türkçe etiket yok, LLM hakem |

Son çalıştırma (2026-10-04, Claude Code 2.1.289, her senaryo 1 çalıştırma, `tetiklenir`/`tetiklenmez` 2):
**10/10 senaryo geçti.** Tam takımda 9/10 geçti; `varsayilan-oncelik` yalnızca kendi hazırlık betiğindeki fazla katı
bir güvenlik denetimi yüzünden başlamadı, betik düzeltilince tek başına çalıştırıldı ve geçti. Aynı yeni senaryolar
2.0.0 sürümünde 5/9 geçiyordu (derin modda çapraz sorgu bölümü yoktu, İngilizce etiketler, karar defteri ve
`konsey.json` varsayılanları çalışmıyordu). Tek çalıştırmalık sonuçlardır; model davranışı çalıştırmadan
çalıştırmaya değişebilir.

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
Use: `/konsey:topla [--mod hizli|standart|derin] [--tema klasik|kurtlar] [--uyeler adversary,engineer,analyst] <question>`,
or just write "council: …".

- **Modes:** `hizli` (one pass, no subagents), `standart` (7 independent subagents, default), `derin` (adds a
  cross-examination round where members rank anonymised opinions; shown as a `CROSS-EXAMINATION` section).
- **Language:** the debate and its labels (`VERDICT`, `CONFIDENCE`, `CRITICAL RISKS`…) follow the language you ask in.
- **Defaults:** request > project `.claude/konsey.json` > a line in `CLAUDE.md` > `~/.claude/konsey.json` >
  `klasik`/`standart`. File format: `{ "tema": "kurtlar", "mod": "hizli" }`.
- **Decision log:** say "save" and the verdict is appended to `KONSEY.md` in the project root; nothing is written
  unless you ask.
- **Verification:** 10 `claude plugin eval` cases cover every feature above (see the table in "Doğrulama").
