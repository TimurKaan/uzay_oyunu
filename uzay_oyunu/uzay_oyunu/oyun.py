import json
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler, log_cagri


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    if not (credits or engines or copilot):
        return ""
    
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motor") 
    if copilot:
        esyalar.append("yetenekli bir pilot")
        
    return f"Sende: {', '.join(esyalar)}"


@log_cagri
def hedef_menusu(hedefler: list[str]) -> str:
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, 1):
        satirlar.append(f"[{i}] {hedef}")
        
    return "\n".join(satirlar)


@log_cagri
def galaksi_kur(gezegenler, baglantilar, baslangic, **kwargs):
    if baslangic not in gezegenler:
        raise ValueError("Başlangıç gezegeni listede yok.")
    
    yakit = kwargs.get("yakit", 50)
    
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }


with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)

galaksi = galaksi_kur(**veri)

durum = {
    "konum": galaksi["konum"],
    "baglantilar": galaksi["baglantilar"],
    "credits": True,
    "engines": False,
    "copilot": True,
}

guncel_sayac = hamle_sayaci()


def travel(planet=None, oyun_durumu=None):
    from uzay_oyunu.komutlar import KOMUTLAR

    current_durum = oyun_durumu if oyun_durumu is not None else durum

    if planet is not None:
        girdi = planet.strip() if isinstance(planet, str) else planet
        if girdi in KOMUTLAR:
            komut_fn, _ = KOMUTLAR[girdi]
            sonuc = komut_fn(current_durum)
            print(sonuc)
            return sonuc
        else:
            current_durum["konum"] = girdi
            galaksi["konum"] = girdi
            yapilan_hamle = guncel_sayac()
            oyun_bitti_mi = False
            if oyun_bitti_mi:
                print(f"Oyunu {yapilan_hamle} hamlede bitirdin!")
            return girdi

    while True:
        hedefler = current_durum["baglantilar"].get(current_durum["konum"], [])
        print(hedef_menusu(hedefler))
        girdi = input("> ").strip()

        if girdi in KOMUTLAR:
            komut_fn, _ = KOMUTLAR[girdi]
            sonuc = komut_fn(current_durum)
            print(sonuc)
            continue

        secilen_gezegen = None
        if girdi.isdigit() and 1 <= int(girdi) <= len(hedefler):
            secilen_gezegen = hedefler[int(girdi) - 1]
        elif girdi in hedefler:
            secilen_gezegen = girdi
        else:
            secilen_gezegen = girdi

        current_durum["konum"] = secilen_gezegen
        galaksi["konum"] = secilen_gezegen
        yapilan_hamle = guncel_sayac()
        oyun_bitti_mi = False
        if oyun_bitti_mi:
            print(f"Oyunu {yapilan_hamle} hamlede bitirdin!")
        return secilen_gezegen
