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


def say(fonksiyon):
    """Fonksiyonun çağrı sayısını sarmalayici.cagri niteliğinde tutan dekoratör."""
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri += 1
        return fonksiyon(*args, **kwargs)
    
    sarmalayici.cagri = 0
    return sarmalayici


def log_cagri(fonksiyon):
    """Her çağrıdan önce fonksiyon adını ve argümanlarını, sonra da dönüş değerini yazdıran dekoratör."""
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        konumsal = [repr(a) for a in args]
        adli = [f"{k}={v!r}" for k, v in kwargs.items()]
        tum_argumanlar = ", ".join(konumsal + adli)
        print(f"-> {fonksiyon.__name__}({tum_argumanlar})")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"<- {fonksiyon.__name__} = {sonuc!r}")
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