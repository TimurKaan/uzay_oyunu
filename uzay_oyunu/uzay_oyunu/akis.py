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