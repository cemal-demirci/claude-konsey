Konsey toplandı, yedi üye de görüşünü verdi ve başkan hükmünü yazdı; şimdi çıktıyı sunuyorum.

═══════════════════════════════════════════════════════════════════
                         KURTLAR KONSEYİ
     "6 kişilik ekip, 40 bin MAU'lu monoliti şimdi mikroservislere bölmeli mi?"
     mod: standart · üye: 7
═══════════════════════════════════════════════════════════════════

Mehmet Karahanlı · GÖREV DAĞILIMI
  "Konsey açıldı; önümüzde 6 kişilik bir ekibin 40 bin kullanıcılı monolitini bölme ya da koruma kararı var ve ben bu kararı kişilerin hevesine değil, dosyanın gösterdiği sisteme göre vereceğim — benim için şahıslar değil, sistem önemlidir."
  Testere Necmi → İki seçeneğin her birinde geri dönüşü en pahalı tek kusur nedir, hangisi daha onarılmaz?
  Nizamettin Güvenç → Hangi büyüme eşiğinde ve takvimde ertelemenin maliyeti bölmenin maliyetini aşar; bugün elde hangi işaret var?
  İplikçi Nedim → "40 bin MAU tek sunucuyla taşınır" varsayımını istek, veri ve tepe yük açısından sına; farklı ölçeklenen bileşen ihtimalini ve gereken ölçümü söyle.
  Laz Ziya → "Bölmek mi kalmak mı" ikilisinin dışındaki hangi soru ekibin gerçek derdini karşılar, sebebe göre nasıl değişir?
  Kılıç → Hangi somut eşikler aşılırsa bölme zorunlu olur; 6 kişinin bölmeyi işletmesi için asgari altyapı nedir?
  Hüsrev Ağa → Uzun vadede öncelik basitlik mi, uyarlanabilirlik mi, geri alınabilirlik mi?
  Polat Alemdar → Bölme isteğinin arkasındaki insani itki nasıl ayırt edilir; nöbet yükünün ekibe etkisi monolitte kalmaya göre nasıldır?

──────────────────────────────────────────────────────────────────

⚔ TESTERE NECMİ
Bak, lafı dolandırmayacağım: şimdi bölmeyin. Bölerseniz geri dönüşü en pahalı kusur veridir; tek veritabanını servislere dağıttığınız gün transaction'ı kaybedersiniz. Yanlış çizilmiş servis sınırı kodda kalmaz, şemaya, ağ çağrısına ve dağıtım hattına gömülür; geri birleştirmek aylar süren veri göçü ister. 6 kişi hem ürünü hem nöbeti hem altyapıyı taşırsa sonuç dağıtık monolittir. Kalmanın kusuru çürümedir, ama o yavaş gelir, görünür ve refactor ile içeriden onarılır. Asıl korkum "kalalım"ın "hiçbir şey yapmayalım"a dönmesi; o zaman iki yıl sonra elinizde bölünemeyen bir yumak kalır. (Güven: %80)

──────────────────────────────────────────────────────────────────

📈 NİZAMETTİN GÜVENÇ
Masada görünen hamle değil, görünmeyen önemlidir. Bölmenin faturası peşindir: 6 kişinin bir kısmı aylarca ürün yerine altyapıya çalışır, rakip o arada özellik çıkarır. Nedim yükü sayıyor; ben bölme kararını kullanıcı sayısına değil ekip büyüklüğüne bağlarım. Eşiğim bir varsayımdır: ekip 15–20 kişiyi, yani üç bağımsız takımı geçerse ya da tek bir bileşen diğerlerinden yaklaşık 10 kat farklı ölçeklenirse. Bugün bu eşiğe yaklaşıldığına dair elde tek işaret yok, çünkü büyüme hızı bilinmiyor. Eşik 12 ay içinde görünüyorsa şimdiden yalnızca modül sınırlarını çizin; kesim sonra. (Güven: %80)

──────────────────────────────────────────────────────────────────

🔬 İPLİKÇİ NEDİM
Kuzum, hesap kitap konuşalım; ama rakamların hepsi benim tahminim, dosyada yok. 40 bin MAU'nun %25'i günlük aktifse 10 bin kişi eder; kişi başı 50 istekle günde 500 bin, ortalama saniyede 6 istek çıkar, tepe 10 kat olsa 60 civarıdır. Kullanıcı başına yılda 1 MB veriyle 40 GB eder; tek veritabanı bunu rahat taşır. Medya ya da ağır arka plan işi bulunma ihtimali %30–40, ama çıksa da ilacı mikroservis değil, aynı kod tabanından ayrı çalışan kuyruk ve işçi sürecidir. İki haftalık ölçüm yeter: uç nokta bazında tepe istek ve p95/p99, tepe saatte CPU, bellek ve bağlantı doygunluğu, iş tipine göre CPU-saniye ve kuyruk derinliği, veritabanı boyutu ve aylık büyümesi. Bugün karar veriyle değil hisle veriliyor canim. (Güven: %80)

──────────────────────────────────────────────────────────────────

🎨 LAZ ZİYA
*(o meşhur gülüşüyle)* Monolitte kalın da; asıl soru "bölelim mi" değil, "hangi ağrı için hangi en küçük ameliyat" sorusudur uşağum. Dağıtım yavaşsa soru "hattı nasıl hızlandırırız"dır. Kod karmaşıksa "sınırları monolitin içinde nasıl çizeriz"dir. Tek bileşen farklı ölçekleniyorsa "yalnız onu ayırsak yeter mi"dir. CV kaygısıysa ha bu teknik değil, insan meselesidir; onu Polat'a sorun. Dördünün hiçbirinde cevap "hepsini böl" çıkmıyor. (Güven: %80)

──────────────────────────────────────────────────────────────────

⚙ KILIÇ
Sahada iş başka yürür. Eşiklerim varsayımdır, ölçülmemiştir:
- **Modül sınırı:** Tek değişiklik düzenli olarak 3'ten fazla modüle dokunuyorsa önce monoliti modülerleştirin.
- **Test kapsamı:** Kritik akışlarda %60'ın altındaysa bölme yasak.
- **Dağıtım:** Haftada 1'den seyrekse ve derleme 30 dakikayı aşıyorsa sinyal var; 6 kişide bu çoğunlukla boru hattı sorunudur, mimari değil.
- **Arıza:** Ayda 2'den fazla olay aynı bileşenden çıkıp tüm sistemi düşürüyorsa yalnızca o bileşeni ayırın.

Bölmeyi işletmek için merkezi log, dağıtık izleme, servis başına CI/CD ve geri alma, ayrı veritabanı, outbox ve nöbet çizelgesi gerekir. Bu, 6 kişide kabaca 1–1,5 kişinin kalıcı mesaisidir. Necmi'nin dediği doğru: paylaşılan veritabanıyla bölerseniz iki tarafın da maliyetini ödersiniz. (Güven: %80)

──────────────────────────────────────────────────────────────────

🧘 HÜSREV AĞA
Evlat, monolitte kalın; sadık kalınacak değer geri alınabilirliktir, basitlik de onun bugünkü yoludur. Bu karar bugünün altı kişisini değil, yarın gelecek olanı da bağlar. Monoliti modüllere ayırmak geri alınır; dağıtılmış veriyi ve ağ sınırlarını toplamak yıllar alır. Dönüşü olmayan kapıdan, sebebini bilmeden geçilmez. Yalnız basitlik bahanesiyle içini çürütürseniz yarın bölmek de imkânsızlaşır. Kurda akıl, güneş doğana kadar lazımdır. (Güven: %75)

──────────────────────────────────────────────────────────────────

❤ POLAT ALEMDAR
Monolitte kalın. Altı kişi, altı servis, tek nöbet listesi; gece uyanan adam sabah gider. Ekibe sorun: "Hangi ölçülebilir acı bitecek?" Cevap rakam değilse sebep sıkıntıdır. Ama kalıp borcu temizlemezseniz yorulan en iyi iki kişi gider. (Güven: %75)

═══════════════════════════════════════════════════════════════════
             KARAR — BARON MEHMET KARAHANLI
═══════════════════════════════════════════════════════════════════

KARAR: Ekip şimdi bölmesin; monolitte kalsın, ancak sınırları monolitin içinde çizerek kalsın ve bölme sorusunu ölçülmüş bir eşiğe bağlasın.

GÜVEN: %78 — Yedi üyenin istisnasız aynı yöne işaret etmesi ve bölmenin geri alınamazlığı yukarı çekiyor; dayanılan yük düzeyinin ölçülmemiş bir varsayım olması ve bölme isteğinin asıl sebebinin bilinmemesi aşağı çekiyor.
  Dağılım: 7 bu yönde / 0 karşı / 0 kararsız · Kanıt: varsayım ağırlıklı; oy birliği ölçüme değil akla dayanıyor, Nedim'in iki haftalık ölçümü bu boşluğu kapatmak için şart.

──────────────────────────────────────────────────────────────────

KRİTİK RİSKLER
  1. **Dağıtık monolit**: Paylaşılan veritabanıyla bölünürse transaction kaybolur, ağ sınırı şemaya gömülür ve geri birleştirmek aylar süren veri göçü ister.
  2. **Sessiz çürüme**: "Kalalım" kararı "hiçbir şey yapmayalım"a dönerse iki yıl sonra bölünecek temiz sınır kalmaz.
  3. **Yanlış derde ilaç**: Bölme isteğinin sebebi ölçek değilse ağrı yerinde kalır, üstüne 1–1,5 kişilik kalıcı altyapı mesaisi ve nöbet yükü biner; yorulan en iyi iki kişi gider.

──────────────────────────────────────────────────────────────────

SONRAKİ ADIMLAR
  1. Sorun ekibe ve yazılı yanıtlatın: "Bölme ile hangi ölçülebilir acı bitecek?" Cevap rakam değilse gündemden düşürün.
  2. Başlatın iki haftalık ölçümü: uç nokta bazında tepe istek ve p95/p99 gecikme, tepe saatte sunucu ve veritabanı CPU/bellek/bağlantı doygunluğu, iş tipine göre CPU-saniye ve kuyruk derinliği, veritabanı boyutu ve aylık büyümesi.
  3. Çıkarın Kılıç'ın dört göstergesini: değişiklik başına dokunulan modül sayısı, kritik akış test kapsamı, haftalık dağıtım sıklığı ve süresi, aylık olay sayısı ve kaynağı.
  4. Çizin modül sınırlarını monolitin içinde; her modüle sahip, açık arayüz ve kendi tablo kümesi verin. Ağır arka plan işi varsa aynı kod tabanından ayrı kuyruk ve işçi süreci olarak çalıştırın.
  5. Yazın bölme eşiğini tek sayfaya ve 6 ayda bir gözden geçirin: tek bileşenin tepe saatte kaynağın %60'ından fazlasını tüketmesi ya da ekibin 12 ayda 15+ mühendise çıkacağının onaylı plana bağlanması.

──────────────────────────────────────────────────────────────────

AZINLIK GÖRÜŞÜ: karşı oy yok; en düşük güvenle konuşan Polat Alemdar ve Hüsrev Ağa'nın çekincesi
"❤ Monolitte kalmak borcu temizlememek değildir. Nöbet listesine bakın; gece uyanan adam sabah gider."
"🧘 Evlat, basitlik bahanesiyle içini çürütürsen yarın bölmek de imkânsızlaşır."

FİKRİMİ DEĞİŞTİRİR: Ölçümle kanıtlanmış, tek başına tepe saatte kaynağın %60'ından fazlasını tüketip diğer isteklerin p99'unu bozan ve ayrı işçi süreciyle çözülemeyen bir bileşen; o halde bile hüküm "hepsini böl" değil "yalnız o parçayı ayır" olur.

═══════════════════════════════════════════════════════════════════