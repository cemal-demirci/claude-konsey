# Örnek: Açık kaynak bir CLI aracının lisansı MIT mi olmalı yoksa GPL-3.0 mı?

> İstek: `konseyi topla: Açık kaynak bir CLI aracının lisansı MIT mi olmalı yoksa GPL-3.0 mı?`  
> Mod: `standart` · Tema: `klasik` · Bu çıktı `claude plugin eval` çalıştırmasından olduğu gibi alınmıştır.

═══════════════════════════════════════════════════════════════════
                         KONSEY
     "Açık kaynak CLI aracı: MIT mi, GPL-3.0 mı?"
     mod: standart · üye: 7
═══════════════════════════════════════════════════════════════════

⚔ ELEŞTİRMEN
En tehlikeli yanılgı "GPL-3.0 beni ticari sömürüden korur" varsayımı. Bu koruma iki yerden delinir. Şirketler aracı subprocess ile çağırır, bu da çağıran programı GPL'e bağlamaz. Aracı SaaS olarak sunmak da GPL-3.0'ın kapsamında değildir, o AGPL'in işi. Karşılığında ödenen bedel somut: GPL-3.0 kurumsal politikalarda yasak ya da hukuk onayına bağlı. Yani az koruma alıp çok sürtünme ödüyorsunuz. MIT, %70. Tek uyarım şu: kod kütüphane olarak da sunulacaksa GPL'in koruması gerçekten işe yarar. Kararı ilk dış katkıdan önce kesinleştirin.

──────────────────────────────────────────────────────────────────

📈 STRATEJİST
Yeni bir CLI aracının kıt kaynağı dikkat ve kurulum sayısıdır. Koruma bu aşamada rekabet avantajı sağlamaz. GPL-3.0 kurumsal kullanıcıya giden huniyi daraltır ama asıl korkulan senaryoyu, bulut üzerinden ticari sömürüyü, yine de durdurmaz. Maliyeti yüksek, getirisi düşük bir takas bu. Zamanlama da MIT'ten yana, çünkü dış katkı birikmeden lisansı değiştirmek hâlâ ucuz. Beni ancak iki şey tersine çevirir: çift lisanslı bir iş modeli planı ya da GPL ağırlıklı bir ekosistem (örneğin GNU araç zinciri). MIT, %70.

──────────────────────────────────────────────────────────────────

🔬 ANALİST
Belirleyici olan yazarın hedefi, ama o bilinmiyor. Bu belirsizlikte geri alınması kolay olan seçeneği seçmek gerekir. MIT'li kod, bildirimi korunarak bir GPL-3.0 dağıtımına alınabilir. GPL'den MIT'ye geçmek ise her katkıcının onayını ya da CLA'yı gerektirir. Kurumsal politikalar ve subprocess kuralı [OLGU], tek kişilik ve ticari olmayan proje ise [VARSAYIM]. Güvenim bu yüzden %60'ta kalıyor. Yazar "kapalı ticari çatal istemiyorum" derse GPL-3.0'ı savunurum.

──────────────────────────────────────────────────────────────────

🎨 VİZYONER
Soru yanlış kurulmuş. Bir CLI için ikilem "benimsenme mi, koruma mı" değil, çünkü GPL-3.0 buradaki kapıları zaten kapatmıyor. Gerçek ikilem şu: neyden korunmak istiyorsun? Korkun bulut sömürüsüyse doğru araç GPL değil, AGPL-3.0. Kütüphaneye gömülmekten korkuyorsan GPL-3.0. Korkun yoksa MIT. Varsayılan durum için MIT, %65.

──────────────────────────────────────────────────────────────────

⚙ MÜHENDİS
Aracın asıl kullanım yolu ayrı süreç olarak çağrılmak ve bu yolda copyleft neredeyse hiç devreye girmez. Yani GPL, CLI'da korumadan çok bir onay kuyruğu olarak çalışır. Asıl arıza modu başka yerde. Çekirdek ileride içe alınabilir bir kütüphaneye ayrılırsa o parça kapalı bir ürüne gömülebilir. O noktada lisansı sıkılaştırmak için katkıcı onayı ya da CLA gerekir. MIT, %65.

──────────────────────────────────────────────────────────────────

🧘 FİLOZOF
On yıl sonra bu emeğin ortak mal olarak kalması, bugün hızlı yayılmasından değerlidir. MIT'te bedeli gönüllü geliştirici öder, kazancı kapalı çatal alır. Eleştirmen ve Mühendis "koruma yok" diyor. Ama GPL'in yükü zaten yalnızca kodu alıp dağıtana düşer, aracı çağıran kullanıcıya neredeyse hiç düşmez. GPL-3.0, %55. Araç benimsenmezse koruduğum ortak malın boş kalacağını da kabul ediyorum.

──────────────────────────────────────────────────────────────────

❤ HÜMANİST
Küçük bir projeyi ayakta tutan şey kullanıcı ve katkıcıdır, lisansla kazanılan bir zafer değil. Şirketteki mühendis aracı işte kullanamıyorsa katkı da yapamaz, yazar da ilk ilgiyi orada kaybeder. GPL yazarı lisansın bekçisi yapar ama tek başına birinin bu hakkı zorla uygulatacak ne vakti ne de hukuki gücü vardır [VARSAYIM]. Dürüst olayım: yazarın kimliği özgür yazılım değerlerine dayanıyorsa MIT ters teper. Aracın kapatılıp satıldığını görmek "emeğim çalındı" duygusu yaratır ve insanı projeyi bırakmaya itebilir. Bu kişi için geçerli değilse MIT, %60.

═══════════════════════════════════════════════════════════════════
             KARAR — KONSEY BAŞKANI
═══════════════════════════════════════════════════════════════════

KARAR: MIT seçilmeli. Ancak yazar kapalı çatallara karşı korunmayı açıkça istiyorsa ya da çekirdek kod kütüphane olarak dağıtılacaksa GPL-3.0'a (SaaS kaygısı varsa AGPL-3.0'a) geçilmeli.

GÜVEN: %68. Güveni yükselten iki doğrulanmış olgu var: subprocess çağrısı ve SaaS kullanımı GPL'in dışında kalıyor, GPL-3.0 kurumsal politikalarda takılıyor. Güveni düşüren şey yazarın hedefinin ve kodun kütüphane olarak kullanılıp kullanılmayacağının bilinmemesi.
  Dağılım: 6 MIT / 1 GPL-3.0 / 0 kararsız · Kanıt: lisans mekaniği olgulara dayanıyor, projenin bağlamı varsayım

──────────────────────────────────────────────────────────────────

KRİTİK RİSKLER
  1. **Kütüphaneye gömülme**: Çekirdek kod içe alınabilir hale gelirse MIT'li sürüm kapalı bir ticari ürüne gömülebilir ve bu geri alınamaz.
  2. **Geç lisans değişikliği**: Dış katkılar geldikten sonra lisansı herhangi bir yöne çevirmek tüm katkıcıların onayını ya da CLA'yı gerektirir, eski sürümler de eski lisansta kalır.
  3. **Yazarın küskünlüğü**: Özgür yazılım değerlerine bağlı bir yazar kapalı bir çatal gördüğünde projeyi bırakacak kadar motivasyon kaybedebilir.

──────────────────────────────────────────────────────────────────

SONRAKİ ADIMLAR
  1. Projenin neden açık kaynak olduğunu tek cümleyle yaz: yayılmak için mi, kapalı kullanıma karşı korunmak için mi?
  2. Kodun yalnızca `çalıştırılabilir CLI` olarak mı, yoksa içe alınabilir bir kütüphane/modül olarak da mı dağıtılacağına karar ver.
  3. Aynı dil ekosistemindeki 10 benzer CLI aracının lisansına bak ve ekosistemin normunu not et.
  4. Karar MIT ise kök dizine `LICENSE` dosyasını ekle, kaynak dosyalara da `SPDX-License-Identifier: MIT` başlığını koy.
  5. İlk dış PR gelmeden `CONTRIBUTING.md` içine DCO ya da CLA şartını yaz ki ileride lisans değiştirme seçeneği açık kalsın.

──────────────────────────────────────────────────────────────────

AZINLIK GÖRÜŞÜ: Filozof
"🧘 Bugün hızlı yayılan bir araç, on yıl sonra başkasının kapalı ürününün bir parçası olabilir. GPL, aracı kullanana değil kodu alıp dağıtana yük getirir. Bu yüzden asıl bedeli düşündüğünüzden küçüktür."

FİKRİMİ DEĞİŞTİRİR: Yazarın asıl amacının kapalı ticari çatalları engellemek olması ya da kodun kütüphane olarak dağıtılacak olması.

═══════════════════════════════════════════════════════════════════
