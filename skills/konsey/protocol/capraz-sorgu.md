# Çapraz sorgu (2. tur, yalnızca `derin` modda)

Amaç: üyelerin birbirinin en zayıf noktasına saldırması ve hangi görüşün en güçlü olduğunu **isim görmeden**
sıralaması. İsimsiz sıralama, başkanın "en çok sevdiğim üye kazandı" önyargısını kırar.

## Hazırlık

1. Birinci turun yanıtlarını karıştırılmış sırayla `Üye A`, `Üye B`… diye etiketle. Hangi harfin kime ait
   olduğunu yalnızca sen bil; üyelere söyleme.
2. Her üyeye kendi yanıtını da içeren listeyi ver, ama hangisinin kendisi olduğunu söyle ("senin görüşün: Üye C").

## Her üyeye gönderilecek metin

```
Sen {TEMA_ISIM} ({ROL}) olarak bir karar konseyindesin. Birinci turda konsey üyeleri aşağıdaki görüşleri yazdı.
İsimler gizli. Senin görüşün: Üye {KENDI_HARFI}.

SORU: {SORU}

GÖRÜŞLER
{ANONIM_GORUSLER}

GÖREV (en fazla 120 kelime, dil: {DIL})
İTİRAZ: <kendin dışındaki en zayıf görüşün harfi ve neden zayıf olduğu; somut ol>
SIRALAMA: <kendin hariç en güçlü iki görüşün harfleri, güçlüden zayıfa>
POZİSYON GÜNCELLEMESİ: <"değişmedi" ya da yeni tek cümlelik pozisyonun ve nedeni>
```

## Başkana aktarım

- Sıralamalardan puan çıkar: 1. sıra 2 puan, 2. sıra 1 puan. En yüksek puanlı görüşü karar bölümünde belirt.
- Pozisyonunu değiştiren üyeleri tartışma bloğunda göster ("…itirazından sonra fikrimi değiştirdim").
- İtirazları, hedef aldıkları üyenin **adıyla** tartışmaya yerleştir (anonimlik yalnızca sıralama içindir).
