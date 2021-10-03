from .homo import Homo


# def ricevi_daton(aĉeto):
#     return aĉeto.dato


class Kliento(Homo):
    def __init__(self, nomo, aĝo):
        super().__init__(nomo, aĝo)
        self.aĉetaĵoj = []

    def registri_aĉeton(self, aĉeto):
        self.aĉetaĵoj.append(aĉeto)

    def ricevi_daton_de_lasta_aĉeto(self):
        return None if not self.aĉetaĵoj else \
            sorted(self.aĉetaĵoj, key=lambda aĉeto: aĉeto.dato)[-1].dato
        # sorted(self.aĉetaĵoj, key=ricevi_daton)[-1].dato

    def tuta_kvanto_aĉetoj(self):
        tuta_kvanto = 0
        for aĉeto in self.aĉetaĵoj:
            tuta_kvanto += aĉeto.prezo
        return tuta_kvanto
