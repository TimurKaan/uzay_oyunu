import time
from functools import reduce, partial

galaksi = {
    "baglantilar": {
        "dünya": ["sirius"],
        "sirius": ["orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "centauri": ["orion"],
        "kara_delik": []
    }
}

gezegenler = list(galaksi["baglantilar"].keys())

# 1. YOL: map, filter, reduce KULLANIMI
buyuk_harfli_map = list(map(str.upper, gezegenler))
iki_baglantili_filter = list(filter(lambda g: len(galaksi["baglantilar"][g]) >= 2, gezegenler))
toplam_baglanti_reduce = reduce(lambda acc, g: acc + len(galaksi["baglantilar"][g]), gezegenler, 0)


# 2. YOL: Liste Üreteci ve sum KULLANIMI
buyuk_harfli_comp = [g.upper() for g in gezegenler]
iki_baglantili_comp = [g for g in gezegenler if len(galaksi["baglantilar"][g]) >= 2]
toplam_baglanti_sum = sum(len(baglantilar) for baglantilar in galaksi["baglantilar"].values())

# YAZIM OKUNABİLİRLİĞİ YORUMU
# Liste üreteçleri ve 'sum()' fonksiyonu, Python'da genellikle daha 
# okunaklı. map/filter ile lambda fonksiyonları kullanmak kodu uzatıp karmaşıklaştırırken, 
# liste üreteçleri ne yapılmak istendiğini tek bir satırda, İngilizce bir cümleye
# daha yakın ve doğal bir sözdizimiyle ifade eder. Bu yüzden 2. yolu daha okunaklı buluyorum.

# functools.partial KULLANIMI
def yolculuk(baslangic, hedef, hiz):
    return f"{baslangic} konumundan {hedef} konumuna {hiz} hızıyla gidiliyor."

hizli_yolculuk = partial(yolculuk, hiz=3)

# BONUS: Zamanlayıcı Üreteci
def zamanlayici(aralik):
    """Sürekli çalışan, aralık dolduğunda True, dolmadığında False üreten meşgul bekleme üreteci."""
    son_zaman = time.time()
    while True:
        su_an = time.time()
        if su_an - son_zaman >= aralik:
            son_zaman = su_an
            yield True
        else:
            yield False