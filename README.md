# Konsey

**Zor kararlarınızı tek bir yapay zekâya değil, yedi kişilik bir konseye sorun.**

"Ürünü önce ücretsiz mi çıkaralım?", "Mikroservise şimdi mi geçelim?", "Bu teklifi kabul etmeli miyim?"
Tek bir modele sorunca çoğu zaman "bir yandan… öte yandan…" cevabı gelir. Konsey'de ise yedi uzman
(eleştirmen, stratejist, analist, vizyoner, mühendis, filozof, hümanist) **birbirinin cevabını görmeden** kendi
görüşünü yazar; başkan görevleri dağıtır, gerekçeleri tartar ve **taraf tutan** bir hüküm verir:

- tek cümlelik **karar**
- nereden geldiği açıklanan bir **güven yüzdesi**
- **3 kritik risk** ve yarın başlanabilecek **5 somut adım**
- bir **azınlık görüşü** ve kararı tersine çevirecek **tek olgu**

Claude Code eklentisidir. Her şey Claude'un içinde çalışır: dış model, API anahtarı ya da ek ücret yoktur.
İki satırda kurulur, Türkçe ve İngilizce konuşur, MIT lisanslıdır.

```
═══════════════════════════════════════════════════════════════════
                         KURTLAR KONSEYİ
     "Kahve dükkânı ikinci şubeyi şimdi mi açmalı, bir yıl mı beklemeli?"
     mod: standart · üye: 7
═══════════════════════════════════════════════════════════════════

Mehmet Karahanlı · GÖREV DAĞILIMI
  "Konsey açıktır; önümüzde şahısların heyecanı değil, bir dükkânın ikiye bölünmeye hazır olup olmadığı sorusu var — benim için şahıslar değil, sistem önemlidir."
  Testere Necmi → Rakamlar bilinmezken iki dükkânı birden batırabilecek en tehlikeli kusur ne, bunu hangi işaretler önceden gösterir?
  Nizamettin Güvenç → "Kaçabilecek yer" argümanı hangi koşullarda bir yıl beklemenin maliyetinden ağır basar?
  İplikçi Nedim → "Şimdi aç" kararını rasyonel kılacak asgari sayısal eşikler neler?
  Laz Ziya → "Şimdi mi, sonra mı" doğru soru mu, daha az riskli bir yol var mı?
  Kılıç → Dükkân kurucusuz dönsün diye hangi sistemler şart, bunları kurup kanıtlamak kaç ay sürer?
  Hüsrev Ağa → Büyüme amaç mı, araç mı? On yıllık ufukta hangi ilkeye bakarak karar vermeli?
  Polat Alemdar → Kurucunun ikiye bölünmesinin insana yükü ne, devretmeye hazır olduğu hangi işaretlerden anlaşılır?

🔬 İPLİKÇİ NEDİM
Kuzum, hesap kitap konuşalım. Benim asgari eşiklerim şunlar, hepsi varsayım. Kurucu maaşı düşüldükten sonra son 12 ayda istikrarlı net kâr olmalı ve bu kâr yatırımı 24–36 ayda geri ödemeli. Yatırım parası hariç, iki şubenin 6 …

🎨 LAZ ZİYA
Uşağum, herkes "şimdi mi, sonra mı" diye takvime bakıyor da asıl sınav lokasyon değil, dükkânın kurucusuz dönüp dönmediği. Birkaç milyon TL'lik kira, tadilat ve personel yükünü almak yerine küçük bir …

…

KARAR: Konsey, ikinci şubenin şimdi değil bir yıl sonra açılmasına hükmeder. Bu yıl boş geçmeyecek; ilk şubenin kurucusuz dönebildiğini kanıtlamaya ayrılacak.
```

Bu, gerçek bir toplantının kısaltılmış hâlidir; tamamı: [`examples/kurtlar-baskan-kahve-subesi.md`](examples/kurtlar-baskan-kahve-subesi.md).
Tam örnekler için [`examples/`](examples/) klasörüne bakın.

---

## Yeni: başkan görev dağıtır (2.2)

Konsey artık bir **ekip** gibi çalışıyor:

1. **Başkan görev dağıtır.** Konsey toplanınca önce başkan devreye girer (kurtlar temasında Baron Mehmet Karahanlı).
   Soruyu ve bağlam dosyasını okur, kararı gerçekten belirleyecek alt soruları bulur ve **her üyeye ayrı bir görev**
   verir. İki üye aynı soruyla uğraşmaz; cevabı bilinmeyen her nokta bir üyeye zimmetlenir.
2. **Üyeler görevlerini bağımsız yapar.** Yedi üye, başkanın verdiği görevle, birbirini görmeden ayrı alt-ajanlar
   olarak çalışır.
3. **Hükmü başkan verir.** Bütün görüşler başkana döner; başkan oy saymaz, olguya dayanan görüşü öne alır ve kararı yazar.

Başkan **Fable** modelinde ayrı bir alt-ajandır; üyeler kendi modellerinde çalışır. Fable'a erişiminiz yoksa başkanlığı
Claude oturumunun kendisi üstlenir, çıktı aynı kalır. Görev dağılımı çıktının başında `GÖREV DAĞILIMI` bölümünde görünür.

## Kurtlar Konseyi

`kurtlar` teması, aynı yedi uzmanlığı Kurtlar Vadisi'nin Konsey karakterlerine giydirir. Uzmanlık, kanıt ve
dürüstlük kuralları klasik temayla **birebir aynıdır**; değişen, sesin ve bakışın rengidir. Karakterler orijinallerine
bağlı konuşur, ama abartıya kaçmaz: her üye bir konuşmada imza sözlerinden en fazla birini kullanır ve şive birkaç
kelimeyle hissettirilir. Karakterin adı silindiğinde de geriye işe yarar bir görüş kalmalıdır.

| Karakter | Klasikteki rolü | Neye bakar | Nasıl konuşur |
|---|---|---|---|
| ⚔ **Testere Necmi** | Eleştirmen | Planın en tehlikeli kusuru, yanlış varsayım, geri dönüşü olmayan adım | Sert, dobra, kısa cümleler: "Bak, lafı dolandırmayacağım…" |
| 📈 **Nizamettin Güvenç** | Stratejist | Pazar, rakip, zamanlama, birim ekonomisi | Soğukkanlı ve kurnaz; masada görünmeyen hamleyi, iki hamle sonrasını söyler |
| 🔬 **İplikçi Nedim** | Analist | Olgu sanılan varsayımlar, taban oranlar, kâr-zarar | Tüccar ağzıyla: "Kuzum, hesap kitap konuşalım", "Vallahi, Allah seni inandırsın, bu rakam tutmaz canim" |
| 🎨 **Laz Ziya** | Vizyoner | Yanlış sorulmuş soru, yapay kısıtlar, arka kapılar | Karadeniz ağzı; gülüşü harfle yazılmaz, sahne notu olur: *(o meşhur gülüşüyle)* "Uşağum, ha bu işin bir de arka kapısı var da…" |
| ⚙ **Kılıç** | Mühendis | Uygulanabilirlik, ölçekte kırılma, gizli bağımlılık | Sahanın adamı, az konuşur: "Sahada iş başka yürür" |
| 🧘 **Hüsrev Ağa** | Filozof | Neyi optimize ettiğimiz, bedeli kimin ödediği, on yıl sonrası | Yaşlı bilge, atasözlü: "Evlat, büyüğünü bilen büyüğünden büyüktür" |
| ❤ **Polat Alemdar** | Hümanist | İnsanlar, motivasyon, sadakat ve güven | Çok az konuşur; tek, keskin bir yargı cümlesi |
| 👑 **Baron Mehmet Karahanlı** | Başkan | Görev dağıtımı ve son hüküm | Ölçülü, otoriter: "Benim için şahıslar değil, sistem önemlidir" |

Hayran temasıdır: diziden uzun replik alıntılamaz, olay uydurmaz; "sert üslup" yalnızca dildedir, şiddet ya da tehdit
içeren hiçbir öneri üretmez.

## Neden bir konsey?

Tek bir yapay zekâya "sence?" diye sorunca genellikle "bir yandan… öte yandan…" cevabı gelir. Konsey bunu
değiştirir:

- **Bağımsız görüşler.** Her üye ayrı bir alt-ajandır ve diğerlerinin cevabını görmez. Böylece yedi üye aynı
  sesin yedi tonuna dönüşmez.
- **İş bölümü.** Başkan her üyeye kendi alt sorusunu verir; yedi kişi aynı genel soruyu yedi kez cevaplamaz.
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
| `hizli` | Yedi üyeyi ve başkanı tek metinde yazar | 0 | Hızlı bir fikir almak; alt-ajan olmayan ortamlar (claude.ai) |
| `standart` | Başkan görev dağıtır, yedi üye paralel ve bağımsız çalışır, başkan hükmü verir | 7 + 2 başkan | Varsayılan |
| `derin` | Standart + çapraz sorgu ve isimsiz sıralama | 14 + 2 başkan | Geri dönüşü zor, büyük kararlar |

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
agents/konsey-uyesi.md   üye alt-ajanı (yalnızca Read/Grep/Glob)
agents/konsey-baskani.md başkan alt-ajanı (Fable; görev dağıtımı ve hüküm; yalnızca Read/Grep/Glob)
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
| `uyeler-alt-kume` | `/konsey:topla --uyeler` | Tam 3 üye alt-ajanı + başkan, `üye: 3`, diğer dört üyenin başlığı yok |
| `kurtlar-baskan` | Karahanlı görev dağıtır ve hükmü verir; karakter sesleri | Başkana `GÖREV DAĞITIMI` ve `HÜKÜM` çağrıları, 7 üye brifinginde başkanın görevi, çıktıda `GÖREV DAĞILIMI`, LLM hakem: karakterler tanınır ama imza söz tekrarı ve abartı yok |
| `kurtlar-tema` | Kurtlar teması | Karakter adları ve başkan |
| `varsayilan-ayar` | `.claude/konsey.json` varsayılanı | Dosya okunuyor, istekte tema/mod yokken kurtlar teması ve hızlı mod (0 alt-ajan) |
| `varsayilan-oncelik` | `~/.claude/konsey.json` ve öncelik sırası | Eval'in geçici HOME'una kullanıcı ayarı (kurtlar, hizli), projeye `klasik` yazılır: tema projeden, mod kullanıcı dosyasından gelir |
| `karar-defteri` | `KONSEY.md` karar defteri | Dosya oluşuyor, tarihli bölümde karar, güven, riskler, adımlar |
| `dil-ingilizce` | Kullanıcının dili | İngilizce etiketler, Türkçe etiket yok, LLM hakem |

Son çalıştırma (2.2.0, 2026-10-04, Claude Code 2.1.289; her senaryo 1 çalıştırma, `tetiklenir`/`tetiklenmez` 2):
**11/11 senaryo geçti.** `kurtlar-baskan` senaryosunda karakter sesini değerlendiren hakem 3 oydan 3'ünde "geçti" dedi.
Başkanın gerçekten Fable'da çalıştığı ayrıca doğrulandı: başkan alt-ajanı modelini `claude-fable-5-1` olarak
bildiriyor ve oturumun kullanım kaydında ayrı bir Fable kalemi görünüyor. 2.0.0 sürümünde aynı senaryoların 5/9'u
geçiyordu. Tek çalıştırmalık sonuçlardır; model davranışı çalıştırmadan çalıştırmaya değişebilir.

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
without seeing the others. A chair subagent (running on Fable) first hands each member its own sub-question, then
weighs the arguments instead of counting votes. The verdict is a
one-sentence position, a reasoned confidence score, 3 critical risks, 5 next steps and a minority report.
Everything runs inside Claude, with no external models or API keys.

Install: `claude plugin marketplace add cemal-demirci/claude-konsey && claude plugin install konsey@claude-konsey`.
Use: `/konsey:topla [--mod hizli|standart|derin] [--tema klasik|kurtlar] [--uyeler adversary,engineer,analyst] <question>`,
or just write "council: …".

- **Chair:** `konsey-baskani` assigns tasks before the meeting and writes the verdict after it (`TASK ASSIGNMENT`
  section in the output). Without Fable access the main session takes the chair; the output is the same.
- **Kurtlar theme:** the same seven roles voiced by the Kurtlar Vadisi council (Testere Necmi, İplikçi Nedim,
  Laz Ziya…), true to the characters with at most one signature line per speech, never caricature.
- **Modes:** `hizli` (one pass, no subagents), `standart` (7 independent subagents, default), `derin` (adds a
  cross-examination round where members rank anonymised opinions; shown as a `CROSS-EXAMINATION` section).
- **Language:** the debate and its labels (`VERDICT`, `CONFIDENCE`, `CRITICAL RISKS`…) follow the language you ask in.
- **Defaults:** request > project `.claude/konsey.json` > a line in `CLAUDE.md` > `~/.claude/konsey.json` >
  `klasik`/`standart`. File format: `{ "tema": "kurtlar", "mod": "hizli" }`.
- **Decision log:** say "save" and the verdict is appended to `KONSEY.md` in the project root; nothing is written
  unless you ask.
- **Verification:** 11 `claude plugin eval` cases (all passing on 2.2.0) cover every feature above (see the table in "Doğrulama").
