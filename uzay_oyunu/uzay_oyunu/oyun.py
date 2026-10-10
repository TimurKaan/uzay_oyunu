def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    if not (credits or engines or copilot):
        return ""
    
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motor") 
    if copilot:
        esyalar.append("yetenekli bir pilot")
        
    return f"Sende: {', '.join(esyalar)}"


def hedef_menusu(hedefler: list[str]) -> str:

    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, 1):
        satirlar.append(f"[{i}] {hedef}")
        
    return "\n".join(satirlar)