import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu

def test_envanter_metni():
    assert envanter_metni(True, False, True) == 'Sende: bol kredi, yetenekli bir pilot'
    assert envanter_metni(False, False, False) == ''

def test_hedef_menusu():
    hedefler = ["centauri", "sirius"]
    beklenen_cikti = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    
    assert hedef_menusu(hedefler) == beklenen_cikti