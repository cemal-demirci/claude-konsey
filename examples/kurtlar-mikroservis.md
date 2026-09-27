# Örnek: Yazılım ekibimiz monolitten mikroservislere şimdi mi geçmeli?

> İstek: `kurtlar konseyi, hızlı mod: Yazılım ekibimiz monolitten mikroservislere şimdi mi geçmeli?`  
> Mod: `hizli` · Tema: `kurtlar` · Bu çıktı `claude plugin eval` çalıştırmasından olduğu gibi alınmıştır.

═══════════════════════════════════════════════════════════════════
                         KURTLAR KONSEYİ
     "Ekip monolitten mikroservislere şimdi mi geçmeli?"
     mod: hızlı · üye: 7
═══════════════════════════════════════════════════════════════════

⚔ TESTERE NECMİ
Bak, lafı dolandırmayacağım: "şimdi mi" diye soruyorsanız cevap çoğunlukla hayırdır. Ortada acı veren somut bir sorun yoksa bunu moda diye yapıyorsunuz. Sektörün bilinen tuzağı "dağıtık monolit"tir. Servisleri ayırırsınız ama hepsi aynı veritabanına bağlı kalır, birlikte deploy edilir. Sonunda iki mimarinin bedelini ödersiniz, faydasını hiçbirinden görmezsiniz. Ekibinizin sayısını, deploy sıklığını ve hangi modülün darboğaz olduğunu bilmiyorum [BİLİNMİYOR]. Bunu bilmeden "geçelim" diyen, kalp ameliyatına tahlil görmeden girer. Önce yaranın nerede olduğunu gösterin.

──────────────────────────────────────────────────────────────────

📈 NİZAMETTİN GÜVENÇ
Masayı okuyalım. Mikroservis teknik bir karar değil, organizasyon kararıdır. Conway Yasası'na göre sisteminiz iletişim yapınızı kopyalar. Birbirini beklemeden teslim yapması gereken birden fazla bağımsız ekibiniz yoksa ayrışmanın stratejik getirisi sıfıra yakındır. Zamanlama da önemli. Ürün-pazar uyumunu ararken altyapıya çeyrekler harcamak, rakibe hediye edilmiş zamandır. Doğru hamle, kapıyı kapatmadan beklemektir.

──────────────────────────────────────────────────────────────────

🔬 İPLİKÇİ NEDİM
Hesap kitap konuşalım. Ölçmediğiniz bir şeyi iyileştiremezsiniz. Dört rakam getirin: deploy sıklığı, değişiklik başına teslim süresi, başarısız deploy oranı ve en yavaş build süresi (DORA metrikleri). Taban oran da ortada [VARSAYIM]: 20–30 mühendisin altındaki ekiplerde mikroservis geçişi genellikle verimliliği önce düşürür. Gözlemlenebilirlik, CI/CD ve servis sahipliği maliyeti her servis için ayrı ayrı ödenir. En ucuz deney şu: en çok değişen tek bir modülü ayırın ve 6–8 hafta metrikleri karşılaştırın. Rakam iyileşirse devam edersiniz, iyileşmezse zarar küçük kalır.

──────────────────────────────────────────────────────────────────

🎨 LAZ ZİYA
Uşağum, soru yanlış sorulmuş da! Mesele "monolit mi, mikroservis mi" değil, "kodun içi düzenli mi" meselesi. Ha bu modüler monolit diye bir yol var. Aynı deploy içinde sınırları net, birbirine yalnızca arayüzden konuşan modüller kurarsınız. Shopify gibi büyükler bu yoldan yürüdü [VARSAYIM]. Sınırları önce kodda çizersiniz. Günü gelince bir modülü dışarı almak, et kesmek gibi değil, kapı açmak gibi kolay olur.

──────────────────────────────────────────────────────────────────

⚙ KILIÇ
Sahada iş başka yürür. Mikroservise geçtiğiniz gün fonksiyon çağrısı ağ çağrısına döner. Zaman aşımı, yeniden deneme, kısmi arıza, dağıtık transaction ve sürüm uyumsuzluğu kapınıza gelir. Tek veritabanını bölmek işin en zor kısmıdır. Veri tutarlılığı için saga ya da outbox kalıbı gerekir. Merkezi loglama, dağıtık izleme (OpenTelemetry) ve servis başına pipeline hazır değilse ilk production arızasında kör uçarsınız. Önce altyapıyı kurun, sonra ayırın. Tersi sırayla yapılırsa gece üçte telefon çalar.

──────────────────────────────────────────────────────────────────

🧘 HÜSREV AĞA
Evlat, ne kazanmak istiyorsunuz? Hız mı, ölçek mi, yoksa özgeçmişe bir satır mı? Ağaç büyümeden dal budanmaz. Bugün aldığınız karar on yıl sonra bakımını yapacak insanlara miras kalır. Bunu gösteriş için değil ihtiyaç için yapın.

──────────────────────────────────────────────────────────────────

❤ POLAT ALEMDAR
Sistemi insanlar taşır. Ekip yorgunsa, bu geçiş onları kırar. Bir servisin sahibi yoksa o servis öksüz kalır. Önce kimin neyi sahipleneceğini belirleyin.

═══════════════════════════════════════════════════════════════════
             KARAR — BARON MEHMET KARAHANLI
═══════════════════════════════════════════════════════════════════

KARAR: Şimdi toptan geçmeyin. Önce monoliti modüler hale getirip ölçüm yapın. Yalnızca metriklerle kanıtlanmış darboğazı olan tek bir modülü dışarı alın.

GÜVEN: %72. Güveni yukarı çeken, Kılıç ile Necmi'nin anlattığı dağıtık sistem maliyetinin iyi bilinen bir olgu olması. Aşağı çeken, ekip büyüklüğünün ve darboğazın bilinmemesi; Nedim'in rakamları gelmeden kesinlik olmaz.
  Dağılım: 7 üye bu yönde (şimdi toptan geçiş yok) / 0 karşı / 0 kararsız · Kanıt: genel sektör bilgisi ağırlıklı, projeye özel olgu yok

──────────────────────────────────────────────────────────────────

KRİTİK RİSKLER
  1. **Dağıtık monolit**: Ortak veritabanı ve birlikte deploy edilen servisler iki mimarinin bedelini birden ödetir.
  2. **Gözlemlenebilirlik açığı**: İzleme ve loglama olmadan yapılan ayrıştırma, ilk arızada kök nedeni bulunamaz hale getirir.
  3. **Sahipsiz servisler**: Ekip sayısından fazla servis çıkarsa bakım yükü ekibi ezer ve teslim hızı düşer.

──────────────────────────────────────────────────────────────────

SONRAKİ ADIMLAR
  1. Son 3 ayın deploy sıklığını, teslim süresini, başarısız deploy oranını ve build süresini çıkarın.
  2. Monolitteki modülleri ve aralarındaki bağımlılıkları bir diyagramda haritalayın.
  3. En sık değişen ve en çok çakışma yaşanan modülü aday olarak seçin.
  4. Merkezi loglama ve dağıtık izlemeyi monolitte şimdiden devreye alın.
  5. Seçilen modülün sınırlarını kod içinde arayüzle netleştirin ve ayırma kararını 8 hafta sonra metriklerle gözden geçirin.

──────────────────────────────────────────────────────────────────

AZINLIK GÖRÜŞÜ: Laz Ziya
"🎨 Uşağum, belki hiç ayırmanız gerekmeyecek da. İyi kurulmuş bir modüler monolit, birçok ekibe yıllarca yeter."

FİKRİMİ DEĞİŞTİRİR: Birbirini bekleyen birden fazla bağımsız ekibin olması ve deploy çakışmalarının teslimi ölçülebilir biçimde yavaşlatıyor olması.

═══════════════════════════════════════════════════════════════════
