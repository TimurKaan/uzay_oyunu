def yakit_ekle(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo