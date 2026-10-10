def gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler):
    print(f"[{oncelik.upper()}] {baslik}")
    
    for i, adim in enumerate(adimlar, 1):
        print(f" {i}. {adim}")
        
    for anahtar, deger in ekler.items():
        print(f" {anahtar}: {deger}")

if __name__ == "__main__":
    hedef_baslik = "Kara deliğe atla"
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    parametre_sozlugu = {"oncelik": "yüksek", "sorumlu": "Ayşe"}

    print("--- 1. Standart Çağrı ---")
    gorev_kaydi(
        hedef_baslik, 
        "Kredi kazan", "Pilot bul", "Hiperdrive al", 
        oncelik="yüksek", 
        sorumlu="Ayşe"
    )
    
    print("\n--- 2. Liste (*) ve Sözlük (**) Açılarak Yapılan Çağrı ---")
    gorev_kaydi(hedef_baslik, *adimlar_listesi, **parametre_sozlugu)