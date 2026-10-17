from itertools import islice, takewhile

# Sonsuz Fibonacci üreteci
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 1. next() ile ilk üç değeri alma
g = fibonacci()
print("next() ile ilk 3 değer:")
print((next(g), next(g), next(g)))

# 2. itertools.islice ile ilk 12 değeri alma
print("\nislice ile ilk 12 değer:")
print(list(islice(fibonacci(), 12)))

# 3. itertools.takewhile ile 100'den küçük değerleri alma
print("\ntakewhile ile 100'den küçük değerler:")
print(list(takewhile(lambda x: x < 100, fibonacci())))

# 4. Üretecin tek kullanımlık olduğunu gösterme
print("\nÜretecin tek kullanımlık olduğunu gösterme:")
g2 = fibonacci()
print("Birinci islice çağrısı (ilk 5 değer):", list(islice(g2, 5)))

print("İkinci islice çağrısı (sonraki 5 değer):", list(islice(g2, 5)))

def yakit_gostergesi(yakit: int, tuketim: int):
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yakit = 0
        yield yakit

def travel():
    # Testlerin bozulmaması için tüketim küçük seçildi 
    gosterge = yakit_gostergesi(100, 5)
    
    while True:
        yolculuk_yap = input("Yolculuk yapmak istiyor musun? (e/h): ")
        if yolculuk_yap.lower() != 'e':
            print("Yolculuk iptal edildi.")
            break
            
        try:
            kalan_yakit = next(gosterge)
            print(f"Yolculuk başarılı! Kalan yakıt: {kalan_yakit}")
        except StopIteration:
            print("Yakıtın bitti, uzayda sürükleniyorsun...")
            break

if __name__ == "__main__":
    travel()