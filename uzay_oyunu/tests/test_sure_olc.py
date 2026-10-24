import pytest
from uzay_oyunu.araclar import sure_olc


# 1. Test: Sonuç değişmeden dönüyor mu?
def test_sure_olc_sonuc_degismiyor():
    @sure_olc
    def topla(a, b):
        return a + b

    sonuc = topla(15, 25)
    assert sonuc == 40


# 2. Test: Adlı argümanlarla (keyword arguments) çağrı çalışıyor mu?
def test_sure_olc_adli_argumanlar():
    @sure_olc
    def rota_olustur(baslangic, hedef="orion", adim=5):
        return f"{baslangic} -> {hedef} ({adim} adım)"

    sonuc = rota_olustur(baslangic="dünya", adim=20, hedef="sirius")
    assert sonuc == "dünya -> sirius (20 adım)"


# 3. Test: __name__ ve __doc__ korunuyor mu?
def test_sure_olc_name_ve_doc_korunuyor():
    @sure_olc
    def ornek_fonksiyon(x):
        """Bu fonksiyon verilen sayının iki katını alır."""
        return x * 2

    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
    assert ornek_fonksiyon.__doc__ == "Bu fonksiyon verilen sayının iki katını alır."
