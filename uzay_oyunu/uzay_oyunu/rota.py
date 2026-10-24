from functools import lru_cache
from uzay_oyunu.araclar import sure_olc

def rota_sayaci(baglantilar):
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen, adim):
        if adim == 0:
            return 1
        
        toplam_rota = 0
        komsu_gezegenler = baglantilar.get(gezegen, [])
        for komsu in komsu_gezegenler:
            toplam_rota += rota_sayisi(komsu, adim - 1)
            
        return toplam_rota
    
    return rota_sayisi


def rota_sayaci_onbelleksiz(baglantilar):
    
    def _hesapla(gezegen, adim):
        if adim == 0:
            return 1
        
        toplam_rota = 0
        komsu_gezegenler = baglantilar.get(gezegen, [])
        for komsu in komsu_gezegenler:
            toplam_rota += _hesapla(komsu, adim - 1)
            
        return toplam_rota

    @sure_olc
    def rota_sayisi(gezegen, adim):
        """Önbelleksiz rota sayısı hesaplayıcı."""
        return _hesapla(gezegen, adim)
    
    return rota_sayisi
