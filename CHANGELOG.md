# Değişiklik günlüğü

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
