def aĝo_grupo(aĝo):
    if 0 < aĝo < 18:
        return "Neplenaĝulo"
    elif aĝo in range(18, 65):
        return "Plenkreskulo"
    elif aĝo in range(65, 100):
        return "Plej bona aĝo"
    elif aĝo >= 100:
        return "Centjarulo"
    else:
        return "Nevalida aĝo"


# for kaj opo (tuple)
if __name__ == "__main__":
    for aĝo in (17, 35, 87, 113, -2):
        print(f"{aĝo}: {aĝo_grupo(aĝo)}")
