from functools import lru_cache

def rota_sayaci(baglantilar):
    """Görevde istenen önbellekli (@lru_cache) versiyon"""
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