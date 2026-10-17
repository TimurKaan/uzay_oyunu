from itertools import islice, takewhile
from uzay_oyunu.akis import fibonacci

def test_fibonacci_ureteci():
    # 1. next() ile ilk üç değeri alma testi
    g1 = fibonacci()
    assert next(g1) == 0
    assert next(g1) == 1
    assert next(g1) == 1

    # 2. itertools.islice ile ilk 12 değeri alma testi
    beklenen_ilk_12 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(islice(fibonacci(), 12)) == beklenen_ilk_12

    # 3. itertools.takewhile ile 100'den küçük değerleri alma testi
    beklenen_100_alti = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(takewhile(lambda x: x < 100, fibonacci())) == beklenen_100_alti

    # 4. Üretecin tek kullanımlık olduğunun testi
    g2 = fibonacci()
    ilk_liste = list(islice(g2, 5))
    ikinci_liste = list(islice(g2, 5))
    
    assert ilk_liste == [0, 1, 1, 2, 3]

    assert ikinci_liste == [5, 8, 13, 21, 34] 
    assert ilk_liste != ikinci_liste