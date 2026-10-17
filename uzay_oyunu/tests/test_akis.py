from itertools import islice, takewhile
from uzay_oyunu.akis import fibonacci, yakit_gostergesi

def test_fibonacci_ureteci():
    # 1. next() ile ilk üç değeri alma testi
    g1 = fibonacci()
    assert next(g1) == 0
    assert next(g1) == 1
    assert next(g1) == 1

    # 2. itertools.islice ile ilk 12 değeri alma testi
    beklenen_ilk_12 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(islice(fibonacci(), 12)) == beklenen_ilk_12

    # 3. itertools.takewhile ile 100'den küçük değerleri alma testi
    beklenen_100_alti = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(takewhile(lambda x: x < 100, fibonacci())) == beklenen_100_alti

    # 4. Üretecin tek kullanımlık olduğunun testi
    g2 = fibonacci()
    ilk_liste = list(islice(g2, 5))
    ikinci_liste = list(islice(g2, 5))
    
    assert ilk_liste == [0, 1, 1, 2, 3]

    assert ikinci_liste == [5, 8, 13, 21, 34] 
    assert ilk_liste != ikinci_liste

    # oyun.py dosyasındaki fonksiyonu içe aktardığınızı varsayıyoruz
# from oyun import yakit_gostergesi

def test_yakit_gostergesi():
    #örnek test senaryosu
    sonuc = list(yakit_gostergesi(100, 30))
    beklenen_cikti = [70, 40, 10, 0]
    
    # Sonucun beklenen çıktıya eşit olup olmadığını kontrol eder
    assert sonuc == beklenen_cikti, f"Test başarısız! Beklenen: {beklenen_cikti}, Alınan: {sonuc}"
    print("Test başarılı! Fonksiyon doğru çıktıyı üretiyor:", sonuc)

if __name__ == "__main__":
    test_yakit_gostergesi()

# 1. Üreteç Fonksiyonları
def satirlari_oku(yol):
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz_satir = satir.strip()
            if temiz_satir and not temiz_satir.startswith("#"):
                yield temiz_satir

def ayristir(satirlar):
    for satir in satirlar:
        parcalar = satir.split()
        kaynak = parcalar[0]
        hedef = parcalar[2]
        yakit = int(parcalar[3])
        yield (kaynak, hedef, yakit)

def uzun_yolculuklar(kayitlar, esik):
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield (kaynak, hedef, yakit)

# 2. Test Kodu
print("--- Yakıt Toplamı Testi ---")
toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku("veri/seyir.txt")))
print(toplam_yakit)

print("\n--- Uzun Yolculuklar Testi ---")
kayitlar = ayristir(satirlari_oku("veri/seyir.txt"))
hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
print(hedefler)    