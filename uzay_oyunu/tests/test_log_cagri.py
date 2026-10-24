import pytest
from uzay_oyunu.araclar import log_cagri
from uzay_oyunu.oyun import galaksi_kur, hedef_menusu


def test_log_cagri_ornek_cikti(capsys):
    @log_cagri
    def yolculuk(hedef, hiz=1):
        return f"{hedef} hiz={hiz}"

    sonuc = yolculuk("orion", hiz=3)
    assert sonuc == "orion hiz=3"

    captured = capsys.readouterr()
    beklenen_cagri = "-> yolculuk('orion', hiz=3)"
    beklenen_donus = "<- yolculuk = 'orion hiz=3'"

    assert beklenen_cagri in captured.out
    assert beklenen_donus in captured.out


def test_hedef_menusu_loglu(capsys):
    hedefler = ["centauri", "sirius"]
    cikti = hedef_menusu(hedefler)

    assert "Nereye gitmek istersin?" in cikti
    captured = capsys.readouterr()
    assert "-> hedef_menusu(['centauri', 'sirius'])" in captured.out
    assert "<- hedef_menusu =" in captured.out


def test_galaksi_kur_loglu(capsys):
    gezegenler = ["dünya", "mars"]
    baglantilar = {"dünya": ["mars"], "mars": ["dünya"]}
    
    galaksi = galaksi_kur(gezegenler=gezegenler, baglantilar=baglantilar, baslangic="dünya", yakit=80)
    assert galaksi["konum"] == "dünya"
    assert galaksi["yakit"] == 80

    captured = capsys.readouterr()
    assert "-> galaksi_kur(" in captured.out
    assert "<- galaksi_kur =" in captured.out
