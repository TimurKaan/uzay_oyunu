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


def sinirla(alt, ust):
    """Dekore edilen fonksiyonun ilk argümanının [alt, ust] aralığında olmasını zorunlu kılan dekoratör."""
    def dekorator(fonksiyon):
        @wraps(fonksiyon)
        def sarmalayici(*args, **kwargs):
            if args:
                ilk_arg = args[0]
            elif kwargs:
                ilk_arg = next(iter(kwargs.values()))
            else:
                ilk_arg = None

            if ilk_arg is not None and not (alt <= ilk_arg <= ust):
                raise ValueError(f"{fonksiyon.__name__}: {ilk_arg} değeri {alt}-{ust} aralığında değil")

            return fonksiyon(*args, **kwargs)

        return sarmalayici

    return dekorator


def hafiza(maxsize=None):
    """functools.lru_cache kullanmadan, closure içindeki sözlükle çalışan ve maxsize dolunca en eski girdiyi silen dekoratör."""
    def decorator_generator(max_s):
        def dekorator(fonksiyon):
            cache = {}

            @wraps(fonksiyon)
            def sarmalayici(*args, **kwargs):
                anahtar = (args, tuple(sorted(kwargs.items())))
                if anahtar in cache:
                    deger = cache.pop(anahtar)
                    cache[anahtar] = deger
                    return deger

                sonuc = fonksiyon(*args, **kwargs)
                if max_s is not None and len(cache) >= max_s:
                    en_eski = next(iter(cache))
                    del cache[en_eski]

                cache[anahtar] = sonuc
                return sonuc

            sarmalayici.cache = cache
            return sarmalayici

        return dekorator

    if callable(maxsize):
        func = maxsize
        return decorator_generator(None)(func)
    return decorator_generator(maxsize)





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