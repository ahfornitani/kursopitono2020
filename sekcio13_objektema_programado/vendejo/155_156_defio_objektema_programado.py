class Homo:
    def __init__(self, nomo, aĝo):
        self.nomo = nomo
        self.aĝo = aĝo

    def __str__(self):
        return f"La homo nomiĝas {self.nomo} kaj aĝas {self.aĝo}"

    def estas_adolto(self):
        return "Jes" if self.aĝo > 18 else "Ne"


def main():
    homo = Homo("Jozefo", 19)
    duahomo = Homo("Jesaja", 15)
    print(f"Ĉu {homo.nomo} estas adolto? {homo.estas_adolto()}, ĉar li aĝas {homo.aĝo}")
    print(
        f"Ĉu {duahomo.nomo} estas adolto? {duahomo.estas_adolto()}, ĉar li aĝas {homo.aĝo}"
    )


class Kliento(Homo):
    def __init__(self):
        self.aĉetaĵoj = []

    def registri_aĉeton(Aĉeto):
        # aĉetaĵoj += Aĉeto
        pass

    def ricevi_daton_de_lasta_aĉeto():
        pass

    def tuta_kvanto_aĉetoj():
        pass


class Vendisto(Homo):
    def __init__(self, nomo, aĝo, salajro):
        super().__init__(nomo, aĝo)
        self.salajro = salajro


class Aĉeto(Vendisto):
    def __init__(self, nomo, aĝo, salajro, dato, prezo):
        super().__init__(nomo, aĝo, salajro)
        self.dato = dato
        self.prezo = prezo


if __name__ == "__main__":
    main()
