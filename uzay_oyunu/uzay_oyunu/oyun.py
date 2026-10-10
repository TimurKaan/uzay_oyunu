import json

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


def hedef_menusu(hedefler: list[str]) -> str:

    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, 1):
        satirlar.append(f"[{i}] {hedef}")
        
    return "\n".join(satirlar)

import json

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

def travel(planet):
    destinations = galaksi["baglantilar"][planet] 
    
    pass