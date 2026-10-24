from functools import lru_cache
import pytest
from uzay_oyunu.araclar import sinirla, hafiza
from uzay_oyunu.oyun import yakit_harca


# 1. Normal değer testi: yakit_harca(30) -> 70
def test_yakit_harca_normal():
    assert yakit_harca(30) == 70


# 2. Sınır değerleri testi: 0 ve 100
def test_yakit_harca_sinir_degerleri():
    # Alt sınır
    assert yakit_harca(0) == 100
    # Üst sınır
    assert yakit_harca(100) == 0


# 3. Aralık dışı değerler testi: negatif ve 100'den büyük
def test_yakit_harca_aralik_disi_buyuk():
    with pytest.raises(ValueError) as excinfo:
        yakit_harca(150)
    assert "yakit_harca: 150 değeri 0-100 aralığında değil" in str(excinfo.value)


def test_yakit_harca_aralik_disi_kucuk():
    with pytest.raises(ValueError) as excinfo:
        yakit_harca(-5)
    assert "yakit_harca: -5 değeri 0-100 aralığında değil" in str(excinfo.value)


# 4. Adlı argüman (kwargs) ile sınır kontrolü
def test_sinirla_adli_arguman():
    with pytest.raises(ValueError):
        yakit_harca(miktar=120)

    assert yakit_harca(miktar=40) == 60


def test_hafiza_lru_cache_karsilastirma():
    """hafiza sonuçlarının functools.lru_cache ile birebir eşleştiğini test eder."""
    @hafiza(maxsize=10)
    def kup_hafiza(n):
        return n ** 3

    @lru_cache(maxsize=10)
    def kup_lru(n):
        return n ** 3

    for sayi in range(30):
        assert kup_hafiza(sayi) == kup_lru(sayi)

    # Tekrar çağrıldığında da sonuçlar aynı kalmalı
    for sayi in range(10, 25):
        assert kup_hafiza(sayi) == kup_lru(sayi)


def test_hafiza_maxsize_en_eskiyi_silme():
    """maxsize dolduğunda en eski kaydın silindiğini ve cache boyutunun aşılmadığını test eder."""
    cagri_sayisi = 0

    @hafiza(maxsize=3)
    def islem(x):
        nonlocal cagri_sayisi
        cagri_sayisi += 1
        return x * 10

    # 1, 2, 3 ekleniyor -> cache: 1, 2, 3
    islem(1)
    islem(2)
    islem(3)
    assert cagri_sayisi == 3
    assert len(islem.cache) == 3

    # 4 eklendiğinde en eski olan 1 silinmeli -> cache: 2, 3, 4
    islem(4)
    assert cagri_sayisi == 4
    assert len(islem.cache) == 3

    # 1 tekrar istendiğinde cache'te olmadığı için tekrar hesaplanmalı
    islem(1)
    assert cagri_sayisi == 5

    # 4 ve 3 cache'te olduğu için tekrar hesaplanmamalı
    islem(4)
    islem(3)
    assert cagri_sayisi == 5


def test_hafiza_sinirsiz_maxsize_none():
    @hafiza(maxsize=None)
    def faktoriyel(n):
        if n <= 1:
            return 1
        return n * faktoriyel(n - 1)

    assert faktoriyel(5) == 120
    assert len(faktoriyel.cache) == 5
