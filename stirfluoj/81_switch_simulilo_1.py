def vivuloj_miahejme(ulo):
    uloj = {1: "Mi", 2: "Pri", 3: "Loki"}
    return uloj.get(ulo, "** nevalide **")


if __name__ == "__main__":
    for ulo in range(0, 5):
        print(f"{ulo}: {vivuloj_miahejme(ulo)}")
