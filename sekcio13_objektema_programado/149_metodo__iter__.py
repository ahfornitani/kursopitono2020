from datetime import datetime


class Projekto:
    def __init__(self, nomo):
        self.nomo = nomo
        self.taskoj = []

    # ne necesas atingi per xxx.taskoj , nure "xxx"
    # rilatas al "ansertipado"
    def __iter__(self):
        return self.taskoj.__iter__()

    def aldoni(self, priskribo):
        self.taskoj.append(Tasko(priskribo))

    def okazontaj(self):
        return [tasko for tasko in self.taskoj if not tasko.farite]

    def serĉi(self, priskribo):
        # Ebla IndexError
        return [tasko for tasko in self.taskoj if tasko.priskribo == priskribo][0]

    def __str__(self):
        return f"{self.nomo} ({len(self.okazontaj())} okazonta(j) tasko(j))"


class Tasko:
    def __init__(self, priskribo):
        self.priskribo = priskribo
        self.farite = False
        self.kreadtempo = datetime.now()

    def fini(self):
        self.farite = True

    def __str__(self):
        return self.priskribo + (" (Prete ✔)" if self.farite else "")


def main():
    hejmo = Projekto("Hejmtaskoj: ")
    hejmo.aldoni("Gladi")
    hejmo.aldoni("Lavi telerojn")
    print(hejmo)

    hejmo.serĉi("Lavi telerojn").fini()
    for tasko in hejmo:
        print(f"- {tasko}")

    print(hejmo)  # nun nur 1 okazonta tasko

    superbazaro = Projekto("Aĉetumado en superbazaro: ")
    superbazaro.aldoni("Sekaj fruktoj")
    superbazaro.aldoni("Viando")
    superbazaro.aldoni("Tomato")
    print(superbazaro)

    aĉeti_viandon = superbazaro.serĉi("Viando")
    aĉeti_viandon.fini()

    for tasko in superbazaro:
        print(f"- {tasko}")

    print(superbazaro)  # nur 2 okazontaj


if __name__ == "__main__":
    main()
