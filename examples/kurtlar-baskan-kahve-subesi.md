# Örnek: Kurtlar Konseyi, standart mod — başkan görev dağıtır (2.2)

Soru: `kurtlar konseyi topla: Küçük bir kahve dükkânı ikinci şubeyi şimdi mi açmalı, yoksa bir yıl daha mı beklemeli?`

Gerçek bir çalıştırmanın çıktısıdır (Claude Code 2.1.289, `claude plugin eval` senaryosu `kurtlar-baskan`). Başkan
Baron Mehmet Karahanlı ayrı bir alt-ajan olarak Fable modelinde çalıştı: önce görevleri dağıttı, sonra hükmü yazdı.
Yedi üye, kendilerine verilen görevle birbirini görmeden ayrı alt-ajanlar olarak çalıştı.

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

──────────────────────────────────────────────────────────────────

⚔ TESTERE NECMİ
Bak, lafı dolandırmayacağım: en tehlikeli kusur, iki şubenin aynı kasaya bağlanması. Yeni şube açılışta zarar eder. Bu zararı ilk şubenin nakdi kapatır. Bu arada kurucunun aklı yeni yerdedir, ilk şubede kalite düşer, ciro azalır, kaynak kurur. Tek bir kötü çeyrek ikisini birden götürür. Kredide kişisel kefalet varsa kurucu da gider. Erken uyarı işaretleri şunlar: kurucu iki hafta yokken cironun düşmesi, rezervin iki şubenin 6 aylık sabit giderine yetmemesi, tedarikçiye ya da kiraya geciken ödemeler, kartla ya da kısa vadeli krediyle finansman, son 12 ayda dalgalanan kâr. Bunların hiçbiri bilinmiyor. Şu anda açmak kumar oynamak olur. Fikrimi dört şart birden sağlanırsa değiştiririm: 12 ay istikrarlı kâr, yatırımı ve 6 aylık zararı borçsuz karşılayan rezerv, kendini kanıtlamış bir müdür ve belgelenmiş, kaçırılırsa geri gelmeyecek bir yer. (Güven: %70)

──────────────────────────────────────────────────────────────────

📈 NİZAMETTİN GÜVENÇ
"Kaçabilecek yer" ancak dört şartla beklemenin maliyetini geçer. Birincisi, köşe bir daha çıkmayacak türden olmalı: metro çıkışı, kampüs kapısı gibi. İkincisi, kira piyasanın altında olmalı ve birkaç yıllığına sabitlenebilmeli. İkisi birlikte değilse ekipmanıyla devir de olur. Üçüncüsü, ilk şube kurucusuz dönmeli. Dördüncüsü, yatırım nakitle yapılmalı. Bunlar yoksa şimdi açmanın tek gerekçesi "büyüme ivmesi" kalır. O da bir mekanizma değil, bir histir. İyi köşeler el değiştirir; kötü bir kira sözleşmesi ise insanı 3–5 yıl bağlar. Masada görünen hamle değil, görünmeyen önemlidir: ikinci şubenin asıl maliyeti kira değil, kurucunun bölünen dikkatidir. Necmi'yle aynı yerde duruyorum, yalnız benim çıtam biraz daha düşük: 6 ay kurucusuz kâr ve piyasa altı kiralı somut bir yer bana yeter. (Güven: %65)

──────────────────────────────────────────────────────────────────

🔬 İPLİKÇİ NEDİM
Kuzum, hesap kitap konuşalım. Benim asgari eşiklerim şunlar, hepsi varsayım. Kurucu maaşı düşüldükten sonra son 12 ayda istikrarlı net kâr olmalı ve bu kâr yatırımı 24–36 ayda geri ödemeli. Yatırım parası hariç, iki şubenin 6 aylık sabit giderine yetecek rezerv olmalı. Aylık borç ödemesi gelirin %10–15'ini geçmemeli. Kredi faizi beklenen getirinin altında kalmalı. Dükkân 4 hafta kurucusuz sorunsuz dönmeli. Tek şubeli kafelerin bu eşikleri hangi oranla geçtiğine dair güvenilir bir taban oranım yok canim, rakam da uydurmam. Küçük kafelerin çoğu ince marjla çalışır, o yüzden çoğunun geçemeyeceğini tahmin ediyorum. Hesaplar eşiği geçerse ve kaçacak somut bir yer varsa fikrim döner. (Güven: %65)

──────────────────────────────────────────────────────────────────

🎨 LAZ ZİYA
Uşağum, herkes "şimdi mi, sonra mı" diye takvime bakıyor da asıl sınav lokasyon değil, dükkânın kurucusuz dönüp dönmediği. Birkaç milyon TL'lik kira, tadilat ve personel yükünü almak yerine küçük bir kiosk açın ya da ofislere çekirdek kahve satın. Sermayesi çok daha düşük olur, bu benim varsayımım. Aynı şeyi ölçer: kurucu yokken kalite tutuyor mu, müdür sistemi işletebiliyor mu, marka yeni yerde müşteri çekiyor mu? Tutmazsa kayıp küçük kalır. Tutarsa tam şube bir yıl sonra kanıtla açılır. Ha bu yıl boş geçmesin. Riski de söyleyeyim: kiosk da kurucunun dikkatini dağıtabilir. Hehehe… (Güven: %65)

──────────────────────────────────────────────────────────────────

⚙ KILIÇ
Bekle, ama takvime göre değil, kanıta göre. Kurucu iki hafta yokken dükkânın dönmesi için dört şey şart. Bir: yazılı reçete ve kalibrasyon kartları, açılış-kapanış listeleri. İki: haftalık ölçütler; kasa farkı, fire, stok sayımı, işçilik/ciro oranı. Üç: imza yetkisi olan bir müdür ve yanında yedek bir vardiya sorumlusu, çünkü tek kişi tek arıza noktasıdır. Dört: espresso makinesi, değirmen ve POS için arıza rehberi ve servis numaraları. Bunları kurmak 2–3 ay sürer. Üstüne en az iki ay ölçüt toplanır ve en az bir kez iki haftalık gerçek bir yokluk denemesi yapılır. Toplam 5–7 ay eder, bu benim tahminim. Kanıt bu sürede gelirse yılın dolmasını beklemek gerekmez. Sahada iş başka yürür: müdür giderse, tek kişiye bağlı bir yapıda iki şube birden kilitlenir. (Güven: %70)

──────────────────────────────────────────────────────────────────

🧘 HÜSREV AĞA
Evlat, büyüme amaç değil, araçtır. İkinci şube iki dükkânın yorgunluğu demektir. Kira, tadilat ve personel bağları kolay çözülmez. Dükkân sahibinin elinden çıkınca karakteri de sulanabilir. Bekleyen yıl reçeteleri yazıya döker, bir müdür yetiştirir, kasaya yedek koyar. Sınanmamış dükkân çoğaltılmaz. Yalnız şunu da bil: benim korktuğum şey, bir daha bulunmayacak bir yerin kaçmasıdır. (Güven: %65)

──────────────────────────────────────────────────────────────────

❤ POLAT ALEMDAR
Bizzat işleten kurucu dükkânın kendisidir. İkiye bölünürse iki yerde de yarım kalır. Yük önce aileye, sonra ekibe biner. Ekip bunu "patron artık yok" diye okur. Müdür adayının üç işareti var: sorulmadan sorun çözer, o yokken ciro düşmez, diğerleri ona danışır. Kurucunun hazır olduğunun üç işareti var: iki hafta aramadan tatile çıkabilir mi, tarifinin değiştirilmesine katlanabilir mi, kasa anahtarını verebilir mi? Bekleyiş de bir risk taşır, Laz Ziya'nın kiosku bu yüzden işe yarar: büyüme vaadi verilmezse en iyi barista "burada yükselme yok" deyip gider. Güven devredilmeden şube devredilmez. (Güven: %70)

═══════════════════════════════════════════════════════════════════
             KARAR — BARON MEHMET KARAHANLI
═══════════════════════════════════════════════════════════════════

KARAR: Konsey, ikinci şubenin şimdi değil bir yıl sonra açılmasına hükmeder. Bu yıl boş geçmeyecek; ilk şubenin kurucusuz dönebildiğini kanıtlamaya ayrılacak.

GÜVEN: %75 — Güveni yukarı çeken iki şey var: yedi üyenin tam birliği ve kötü bir kira sözleşmesinin 3–5 yıl geri alınamaması. Aşağı çeken ise kârlılığın, rezervin, borcun ve kurucusuz işleyişin dördünün de bilinmemesi.
  Dağılım: 7 bu yönde / 0 karşı / 0 kararsız · Kanıt: Varsayım ağırlıklı. Birlik bilgiye değil bilgisizliğe dayanıyor, bu yüzden güveni %90'a çıkarmıyorum.

──────────────────────────────────────────────────────────────────

KRİTİK RİSKLER
  1. **Ortak kasa çöküşü**: Yeni şubenin açılış zararı ilk şubenin nakdini emer; tek bir kötü çeyrek ikisini birden götürür.
  2. **Kurucunun bölünmesi**: Kurucu yeni şubeye koşarken ilk şubede kalite ve ciro sessizce düşer, kaynak kurur.
  3. **Kilit çalışanın kaybı**: Büyüme vaadi verilmeden beklenirse en iyi barista gider; tek kişiye bağlı yapı iki şubeyi birden kilitler.

──────────────────────────────────────────────────────────────────

SONRAKİ ADIMLAR
  1. Son 12 ayın aylık net kârını, kurucu maaşı düşülmüş hâliyle, nakit rezervi ve borç ödemeleriyle birlikte tek sayfaya çıkar.
  2. Reçete ve kalibrasyon kartlarını, açılış-kapanış listelerini ve ekipman arıza rehberini yazmaya bu hafta başla.
  3. Haftalık ölçüt kaydını başlat: kasa farkı, fire, stok sayımı, işçilik/ciro oranı.
  4. Müdür adayını belirle, ona büyüme yolunu açıkça söyle; iki haftalık kurucusuz yokluk denemesini takvime koy.
  5. Somut bir lokasyon varsa kira, süre ve devir koşullarıyla belgele; "kaçar" iddiasını hisle değil sözleşmeyle sına.

──────────────────────────────────────────────────────────────────

AZINLIK GÖRÜŞÜ: Kılıç
"⚙ 'Bir yıl' takvim meselesi değil, kanıt meselesi. Sistemler kurulur, ölçütler iki ay bozulmaz, kurucu iki hafta yokken dükkân döner; kanıt beş-yedi ayda gelirse yılın dolmasını beklemek israftır."

FİKRİMİ DEĞİŞTİRİR: İlk şubenin son altı ayda kurucusuz, ölçütleri bozulmadan ve istikrarlı kârla döndüğünün hesaplarla belgelenmesi.

═══════════════════════════════════════════════════════════════════
```
