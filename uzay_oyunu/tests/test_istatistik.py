import time
from uzay_oyunu.istatistik import (
    buyuk_harfli_map, buyuk_harfli_comp,
    iki_baglantili_filter, iki_baglantili_comp,
    toplam_baglanti_reduce, toplam_baglanti_sum,
    hizli_yolculuk, zamanlayici
)

def test_istatistikleri_yazdir():
    print("--- İSTATİSTİK SONUÇLARI ---")
    print(f"Büyük Harfli Liste (Map)    : {buyuk_harfli_map}")
    print(f"Büyük Harfli Liste (Comp)   : {buyuk_harfli_comp}")
    print(f"İki Bağlantılılar (Filter)  : {iki_baglantili_filter}")
    print(f"İki Bağlantılılar (Comp)    : {iki_baglantili_comp}")
    print(f"Toplam Bağlantı (Reduce)    : {toplam_baglanti_reduce}")
    print(f"Toplam Bağlantı (Sum)       : {toplam_baglanti_sum}")
    print(f"Partial Fonksiyon Testi     : {hizli_yolculuk('dünya', 'sirius')}")
    print("-" * 30)

def test_bonus_tik_tak():
    print("\n--- BONUS: TİK TAK TESTİ ---")
    tik_ureteci = zamanlayici(2)
    tak_ureteci = zamanlayici(5)
    
    baslangic = time.time()
    print("Süreç başladı (10 saniye sürecek, meşgul bekleme ile test ediliyor)...")
    
    # Döngü tam 10 saniye boyunca sürekli dönecek
    while time.time() - baslangic <= 10:
        if next(tik_ureteci):
            print("tik")
        if next(tak_ureteci):
            print("tak")

if __name__ == "__main__":
    test_istatistikleri_yazdir()
    test_bonus_tik_tak()