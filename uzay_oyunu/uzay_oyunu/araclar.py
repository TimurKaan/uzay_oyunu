import time
from functools import wraps


def sure_olc(fonksiyon):
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"{fonksiyon.__name__}: {sure:.4f} sn")
        return sonuc
    return sarmalayici


def hamle_sayaci():
    sayac = 0
    
    def artir():
        nonlocal sayac
        sayac += 1
        return sayac
        
    return artir


def en_bagli_gezegenler(galaksi):
    
    baglantilar = galaksi.get("baglantilar", {})
    
    sirali = sorted(baglantilar.keys(), key=lambda g: (-len(baglantilar[g]), g))
    
    return sirali