# Görev 2 – Çağrı Sayacı ve Dekoratör Sırası

Bu belgede, özyinelemeli (recursive) Fibonacci fonksiyonuna uygulanan farklı dekoratör kombinasyonlarının çağrı sayıları ve bu sayıların neden farklı olduğu ayrıntılı olarak açıklanmaktadır.

---

## 1. Çağrı Sonuçları Özeti

`fib(20)` hesaplaması için üç farklı dekoratör diziliminde elde edilen çağrı sayıları:

| Sıralama / Yapı | Dekoratör Dizilimi | Çağrı Sayısı (`cagri`) |
| :--- | :--- | :---: |
| **Durum 1** | Yalnızca `@say` | **21891** |
| **Durum 2** | `@say` üstte, `@lru_cache` altta | **39** |
| **Durum 3** | `@lru_cache` üstte, `@say` altta | **21** |

---

## 2. Python'da Dekoratör Sırası ve Çalışma Mantığı

Python'da dekoratörler tanımlanırken yukarıdan aşağıya yazılır, ancak **aşağıdan yukarıya (içten dışa)** doğru uygulanır:

```python
@dekorator_1
@dekorator_2
def fonksiyon():
    pass
```

Bu sözdizimi arka planda şu işleme denktir:

$$\text{fonksiyon} = \text{dekorator\_1}(\text{dekorator\_2}(\text{fonksiyon}))$$

Dolayısıyla çağrı anında dıştaki sarmalayıcı ilk olarak çalışır, ardından içteki sarmalayıcıya ve nihayetinde asıl fonksiyona geçilir.

---

## 3. Durumların Detaylı Analizi

### Durum 1: Yalnızca `@say` (21.891 Çağrı)

```python
@say
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

- **Neden 21891?**
  - Fonksiyonda herhangi bir önbellekleme (memoization/caching) mekanizması yoktur.
  - Özyinelemeli hesaplamada aynı alt problemler (örneğin `fib(3)`, `fib(4)` vb.) defalarca baştan hesaplanır.
  - $n = 20$ için özyineleme ağacındaki toplam düğüm sayısı $2 \times F_{21} - 1$ formülüyle hesaplanır ($2 \times 10946 - 1 = 21891$).
  - `@say` sarmalayıcısı her tekil özyineleme adımında çalıştığı için sayaç tam olarak **21.891** değerine ulaşır.

---

### Durum 2: `@say` Üstte, `@lru_cache` Altta (39 Çağrı)

```python
@say
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

- **Eşdeğer Yapı:**  
  `fib = say(lru_cache(orijinal_fib))`
- **Neden 39?**
  1. `fib` adı doğrudan dıştaki `@say` sarmalayıcısına işaret eder.
  2. Fonksiyon kendi içinde `fib(n - 1)` ve `fib(n - 2)` özyinelemeli çağrılarını yaptığında, global `fib` fonksiyonunu (yani en dıştaki `@say` sarmalayıcısını) çağırır.
  3. Bu nedenle yapılan **her özyinelemeli çağrıda önce `@say` devreye girer** ve sayacı 1 artırır.
  4. Ardından istek `@lru_cache` katmanına iletilir. Eğer değer daha önce hesaplanmışsa (cache hit), `@lru_cache` sonucu anında döndürür ve asıl fonksiyon gövdesi çalıştırılmaz.
  5. Hesaplama derinliğinde $n=20$'den $n=0$'a inerken her seviye için sol ve sağ dallardan gelen çağrılar toplam $2 \times 20 - 1 = 39$ adet dış çağrı üretir.
  6. `@say` en dış katmanda bulunduğu için, sonucun önbellekten gelip gelmediğine bakılmaksızın yönlendirilen tüm çağrıları sayar.

---

### Durum 3: `@lru_cache` Üstte, `@say` Altta (21 Çağrı)

```python
@lru_cache(maxsize=None)
@say
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

- **Eşdeğer Yapı:**  
  `fib = lru_cache(say(orijinal_fib))`
- **Neden 21?**
  1. `fib` adı bu kez en dış katman olan `@lru_cache` sarmalayıcısına işaret eder.
  2. Yapılan her çağrıda öncelikle `@lru_cache` kontrol edilir.
  3. Eğer parametre (`n`) daha önce hesaplanmışsa (cache hit), `@lru_cache` değeri doğrudan önbellekten döndürür; **alttaki `@say` sarmalayıcısına hiç uğramaz**.
  4. Alttaki `@say` dekoratörü yalnızca önbellek ıskalandığında (cache miss), yani o $n$ değeri ilk defa hesaplanırken devreye girer.
  5. `fib(20)` için $0, 1, 2, \dots, 20$ olmak üzere tam **21 farklı benzersiz argüman** vardır.
  6. Her benzersiz argüman için asıl fonksiyon gövdesi yalnızca 1 kez çalıştırıldığı için `@say` sayacı tam olarak **21** olur.
- **İpucu / Erişim Notu:**  
  `fib` değişkeni doğrudan `lru_cache` fonksiyonunu temsil ettiği için, sarmalanan iç `@say` nesnesine `fib.__wrapped__` üzerinden erişilir ve çağrı sayısına `fib.__wrapped__.cagri` ifadesiyle ulaşılır.
