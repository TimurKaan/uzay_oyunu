KOMUTLAR = {}


def komut(ad, aciklama=""):
    """Fonksiyonu değiştirmeden KOMUTLAR sözlüğüne (fonksiyon, aciklama) olarak kaydeden dekoratör."""
    if ad in KOMUTLAR:
        raise ValueError(f"'{ad}' adlı komut zaten tanımlı!")

    def dekorator(fonksiyon):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' adlı komut zaten tanımlı!")
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon

    return dekorator


@komut("yardim", aciklama="komutları listeler")
def yardim(durum):
    """Tanımlı tüm komutları ve açıklamalarını listeler."""
    satirlar = [f"{ad:<10}{aciklama}" for ad, (_, aciklama) in sorted(KOMUTLAR.items())]
    return "\n".join(satirlar)


@komut("envanter", aciklama="eşyalarını gösterir")
def envanter(durum):
    """Oyuncunun envanterindeki eşyaları gösterir."""
    from uzay_oyunu.oyun import envanter_metni

    return envanter_metni(
        durum.get("credits", False),
        durum.get("engines", False),
        durum.get("copilot", False),
    )


@komut("harita", aciklama="gidebileceğin gezegenleri gösterir")
def harita(durum):
    """Bulunulan konumdan gidilebilecek bağlı gezegenleri listeler."""
    konum = durum.get("konum")
    baglantilar = durum.get("baglantilar", {})
    hedefler = baglantilar.get(konum, [])
    return ", ".join(hedefler)
