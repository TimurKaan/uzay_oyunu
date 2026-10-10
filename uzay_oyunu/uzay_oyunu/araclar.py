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