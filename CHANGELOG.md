# Değişiklik günlüğü

## 2.4.0

- **Lisans GPL-3.0-or-later.** 2.3.0 ve önceki sürümler MIT olarak kalır. Persona dosyalarının geldiği
  Claude-Council-Skill'in MIT bildirimi `NOTICE` dosyasında korunur.
- **Katkıda bulunanlar ve teşekkür:** Hüseyin Eren Çeykel (@huseyinceykel) ve Muammer Yeşilyağcı (@muammer-yesilyagci),
  testleri ve geliştirme önerileri için.
- **README yenilendi:** gerçek toplantı çıktısından ekran görüntüleri (`scripts/ekran.py`), ölçüm grafiği, rozetler.
- 🥚 Konseyin kapısını çalan gizli bir konuk. Kim olduğunu dizi izleyenler bilir.
- Üye ajanı, görev metninde kendi `YANIT` şeması gelirse onu kullanır (konuklar için).

## 2.3.0

- **Varsayılan tema artık `kurtlar`.** Klasik tema `--tema klasik`, "klasik konsey" ya da ayar dosyasıyla seçilir.
- **Kısa brifing, daha hızlı toplantı.** Kurallar, yanıt şeması, rol uzmanlıkları ve yerleşik temaların üslubu/imzaları
  `konsey-uyesi` ajanının tanımına taşındı; brifingde yalnızca isim, görev, soru ve dosya kalıyor (~2.550 → ~1.570
  karakter). Ölçümde brifing + üyeler aşaması 83–91 sn'den 53–67 sn'ye indi. `general-purpose` yedeği için uzun
  brifing `protocol/uye-brifingi.md`'de.
- **Oybirliği kanıt değildir.** Başkan, aynı varsayıma dayanan uzlaşmayla güveni yükseltmez; kritik bilgiler
  bilinmiyorsa güven en fazla %70; azınlık görüşü hükümle gerçekten çatışır. Kör hakem karşılaştırmasında 2.3.0,
  2.2.1'e karşı 6 kararın 5'ini kazandı (kalibrasyon 6,50 → 7,83).
- `bench/`: zaman damgalı toplantı, aşama çözümlemesi ve kör hakem betikleri, ham sonuçlarıyla.
- Düzeltme: `scripts/install.sh` başkan ajanını (`konsey-baskani`) kopyalamıyordu.
- `validate.py`: yerleşik temalar üye ajanı tanımında da birebir aynı olmalı; imza sütunu da karşılaştırılıyor.

## 2.2.1

- Laz Ziya'nın meşhur gülüşü artık harfle yazılmıyor ("Hehehe…" yerine `*(o meşhur gülüşüyle)*` sahne notu):
  gülüşün yazılı karşılığı yok, uydurma bir taklit yerine okuyan onu kendi kafasında duysun. Eval hakemi de buna göre.

## 2.2.0

- **Başkan görev dağıtır.** Yeni `konsey-baskani` alt-ajanı (Fable modeli, salt-okunur): toplantıdan önce her üyeye
  kendi alt sorusunu verir (`GÖREV DAĞILIMI`), toplantıdan sonra hükmü yazar. Ana oturum sekreterdir: görevleri
  iletir, yanıtları toplar, biçimler. Fable erişimi yoksa başkanlığı ana oturum üstlenir.
- Üye brifingine `BAŞKANIN SANA VERDİĞİ GÖREV` satırı; çıktıya `GÖREV DAĞILIMI` bölümü (İngilizcede `TASK ASSIGNMENT`).
- **Kurtlar teması orijinal seslerle:** her karaktere kısa imza sözleri (İplikçi Nedim "kuzum… vallahi, Allah seni
  inandırsın", Laz Ziya "Hehehe… uşağum", Hüsrev Ağa atasözleri, Karahanlı "sistem önemlidir"…) ve abartı ölçüsü:
  konuşma başına en fazla bir imza söz, hafif şive, içerik önce.
- Eval: `kurtlar-baskan` senaryosu (başkan çağrıları, görevli üyeler, karakter sesi için LLM hakem); üye sayan
  ölçütler başkan çağrılarını saymayacak biçimde güncellendi. `validate.py` başkan ajanını da denetliyor.

## 2.1.0

Her özelliğin gerçekten çalıştığını gösteren eval senaryoları eklendi; eksik kalan davranışlar tamamlandı.

- `derin` mod: çapraz sorgu artık çıktıda görünüyor (`ÇAPRAZ SORGU — isimsiz sıralama` bölümü: puanlar, itirazlar,
  fikrini değiştirenler). İkinci tur alt-ajanları paralel başlıyor ve görüş listesinde yalnızca harfler var.
- Varsayılan ayarlar: proje düzeyinde `.claude/konsey.json` desteği. Öncelik: istek > proje dosyası > CLAUDE.md >
  `~/.claude/konsey.json` > varsayılan. Skill, ayar dosyalarını ilk iş olarak okuyor.
- `--uyeler`: yalnızca seçilen üyeler için alt-ajan başlıyor; Türkçe karaktersiz, İngilizce ve tema adları kabul
  ediliyor; azınlık görüşü seçilen üyelerden geliyor.
- Dil: Türkçe dışındaki dillerde başlık ve etiketler de çevriliyor (İngilizce eşlemesi SKILL.md'de).
- Karar defteri: `KONSEY.md` bölüm biçimi tanımlandı (tarih, karar, güven, riskler, adımlar, azınlık, `Sonuç:`);
  "kaydet" konseyi isteyen mesajda da geçebiliyor. Skill yalnızca `KONSEY.md` için yazma izni istiyor.
- `scripts/install.sh`: `/konsey-topla` komutunu da kuruyor, `--tema`/`--mod` değerlerini doğruluyor, `--help`.
- `scripts/validate.py`: eval senaryolarının yapısını da denetliyor.
- CI: `claude plugin validate .` ve geçici klasörde `install.sh` testi eklendi.
- Alt-ajanlar `run_in_background: false` ile başlatılıyor; arka planda çalışan ortamda bir üyenin iki kez
  başlatılması ve karardan sonra gelen tekrar bildirimlerine yanıt yazılması engellendi.
- Yeni eval senaryoları: `derin-mod`, `uyeler-alt-kume`, `karar-defteri`, `varsayilan-ayar`, `varsayilan-oncelik`,
  `dil-ingilizce`;
  `standart-alt-ajan` bağlam etiketlerini, `tetiklenir` güven gerekçesini de sınıyor.

## 2.0.0

- Üyeler artık tek metinde taklit edilmiyor: her üye ayrı bir alt-ajan (`konsey-uyesi`, salt-okunur) olarak
  diğerlerini görmeden görüş yazıyor (`standart` mod).
- `derin` mod: çapraz sorgu turu — üyeler birbirinin anonim görüşlerine itiraz edip sıralıyor.
- `hizli` mod: alt-ajansız, tek metinde (alt-ajan aracı olmayan ortamlar için).
- Bağlam dosyası: karar öncesi proje/sohbet olguları `[OLGU]` / `[VARSAYIM]` / `[BİLİNMİYOR]` etiketleriyle toplanıyor.
- Başkan oy saymıyor; güven yüzdesini pozisyon dağılımı, kanıt oranı ve bilinmeyenlerden türetiyor.
  Kararı tersine çevirecek olguyu ("fikrimi değiştirir") yazıyor.
- Temalar: `klasik` (varsayılan) ve `kurtlar` (Kurtlar Vadisi Konseyi). Varsayılan tema/mod `~/.claude/konsey.json` ile.
- `--uyeler` ile alt küme / üçlü konsey.
- İstenirse karar `KONSEY.md` karar defterine yazılıyor.
- Türkçe arayüz; kullanıcı hangi dilde yazarsa o dilde tartışma.
- Claude Code eklentisi + marketplace, `/konsey:topla` komutu, yapı denetimi (`scripts/validate.py`), CI, eval senaryoları.

## 1.0.0

- [Claude-Council-Skill](https://github.com/itshussainsprojects/Claude-Council-Skill) (MIT): 7 persona, tek metinde tartışma ve karar.
