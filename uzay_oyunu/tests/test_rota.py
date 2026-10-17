import time
from uzay_oyunu.rota import rota_sayaci

galaksi = {
    "baglantilar": {
        "dünya": ["sirius"],
        "sirius": ["orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "centauri": ["orion"],
        "kara_delik": []
    }
}

def test_rota_dogrulama():
    say = rota_sayaci(galaksi["baglantilar"])
    
    sonuc_3 = say("dünya", 3)
    sonuc_10 = say("dünya", 10)
    sonuc_40 = say("dünya", 40)
    
    print("-" * 40)
    print("ROTA SAYISI SONUÇLARI")
    print("-" * 40)
    print(f"adım=3 için sonuç: {sonuc_3}")
    print(f"adım=10 için sonuç: {sonuc_10}")
    print(f"adım=40 için sonuç: {sonuc_40}")
    print(f"Görev formatı: ({sonuc_3}, {sonuc_10}, {sonuc_40})\n")

def performans_olcumlerini_yap():
    adim_sayisi = 20
    baslangic_gezegeni = "dünya"
    baglantilar = galaksi["baglantilar"]

    print("-" * 40)
    print(f"PERFORMANS ÖLÇÜMÜ (Adım = {adim_sayisi})")
    print("-" * 40)

    say_onbellekli = rota_sayaci(baglantilar)
    baslangic_zamani_cache = time.perf_counter()
    sonuc_onbellekli = say_onbellekli(baslangic_gezegeni, adim_sayisi)
    bitis_zamani_cache = time.perf_counter()
    sure_onbellekli = bitis_zamani_cache - baslangic_zamani_cache
    
    print(f"Önbellekli süre: {sure_onbellekli:.6f} saniye (Hesaplanan: {sonuc_onbellekli})")

    print("\nCache Bilgisi:")
    print(say_onbellekli.cache_info())

if __name__ == "__main__":
    test_rota_dogrulama()
    performans_olcumlerini_yap()