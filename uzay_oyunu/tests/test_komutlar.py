import pytest
from uzay_oyunu.komutlar import KOMUTLAR, komut, yardim, envanter, harita
from uzay_oyunu.oyun import travel, durum


# Test 1: @komut dekoratörü fonksiyonu değiştirmeden kaydetmeli
def test_komut_kayit_deseni():
    @komut("test_komutu", aciklama="test açıklaması")
    def ornek_komut(d):
        return "test_sonucu"

    # Fonksiyon değiştirilmemeli
    assert ornek_komut(None) == "test_sonucu"
    # KOMUTLAR sözlüğüne (fonksiyon, aciklama) olarak kaydedilmeli
    assert "test_komutu" in KOMUTLAR
    fn, aciklama = KOMUTLAR["test_komutu"]
    assert fn is ornek_komut
    assert aciklama == "test açıklaması"


# Test 2: Aynı adla iki kez komut tanımlanırsa ValueError fırlatılmalı
def test_komut_ayni_ad_value_error():
    with pytest.raises(ValueError):
        @komut("yardim", aciklama="tekrarlanan yardim")
        def kopya_yardim(d):
            return "kopya"


# Test 3: yardim komutu testi
def test_komut_yardim():
    test_durum = {
        "konum": "dünya",
        "baglantilar": {"dünya": ["mars", "sirius"]},
        "credits": True,
        "engines": False,
        "copilot": True,
    }
    cikti = yardim(test_durum)
    assert "envanter" in cikti
    assert "eşyalarını gösterir" in cikti
    assert "harita" in cikti
    assert "gidebileceğin gezegenleri gösterir" in cikti
    assert "yardim" in cikti
    assert "komutları listeler" in cikti


# Test 4: envanter komutu testi
def test_komut_envanter():
    test_durum = {
        "konum": "dünya",
        "baglantilar": {},
        "credits": True,
        "engines": False,
        "copilot": True,
    }
    cikti = envanter(test_durum)
    assert "bol kredi" in cikti
    assert "yetenekli bir pilot" in cikti
    assert "güçlü motor" not in cikti


# Test 5: harita komutu testi
def test_komut_harita():
    test_durum = {
        "konum": "dünya",
        "baglantilar": {
            "dünya": ["orion", "dünya", "kara_delik"],
            "mars": []
        },
        "credits": True,
        "engines": False,
        "copilot": False,
    }
    cikti = harita(test_durum)
    assert cikti == "orion, dünya, kara_delik"


# Test 6: travel() komut girdiğinde komutu çalıştırıp aynı menüyü tekrar göstermeli ve sonra gezegen seçimi yapmalı
def test_travel_komut_ve_gezegen_secimi(monkeypatch, capsys):
    # Sırasıyla 'yardim', 'harita' komutları ve ardından '1' (orion seçimi) giriliyor
    girdiler = iter(["yardim", "harita", "1"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(girdiler))

    test_durum = {
        "konum": "dünya",
        "baglantilar": {"dünya": ["orion", "sirius"]},
        "credits": True,
        "engines": False,
        "copilot": True,
    }

    secilen = travel(oyun_durumu=test_durum)

    assert secilen == "orion"
    assert test_durum["konum"] == "orion"

    captured = capsys.readouterr()
    # yardim çıktısı yazdırılmış olmalı
    assert "envanter" in captured.out
    assert "harita" in captured.out
    # harita komutu sonucu yazdırılmış olmalı
    assert "orion, sirius" in captured.out
