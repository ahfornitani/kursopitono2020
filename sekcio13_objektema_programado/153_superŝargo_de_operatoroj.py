from datetime import datetime, timedelta


class Projekto:
    def __init__(self, nomo):
        self.nomo = nomo
        self.taskoj = []

    # ne necesas atingi per xxx.taskoj , nure "xxx"
    # rilatas al "ansertipado"
    def __iter__(self):
        return self.taskoj.__iter__()

    # metoda homonimigo
    def __iadd__(self, tasko):
        tasko.posedanto = self
        self._aldoni_taskon(tasko)
        return self

    # oni uzas _ por simuli privatajn metodojn
    def _aldoni_taskon(self, tasko, **kwargs):
        self.taskoj.append(tasko)

    def _aldoni_novan_taskon(self, priskribo, **kwargs):
        self.taskoj.append(Tasko(priskribo, kwargs.get("limdato", None)))

    def aldoni(self, tasko, limdato=None, **kwargs):
        # oni memoru, ke klaso RipetaTasko ja estas Tasko (ĉar heredas de ĝi)
        elektita_funkcio = (
            self._aldoni_taskon
            if isinstance(tasko, Tasko)
            else self._aldoni_novan_taskon
        )
        kwargs["limdato"] = limdato
        elektita_funkcio(tasko, **kwargs)

    def okazontaj(self):
        return [tasko for tasko in self.taskoj if not tasko.farite]

    def serĉi(self, priskribo):
        # Ebla IndexError
        return [tasko for tasko in self.taskoj if tasko.priskribo == priskribo][0]

    def __str__(self):
        return f"{self.nomo} ({len(self.okazontaj())} okazonta(j) tasko(j))"


class Tasko:
    def __init__(self, priskribo, limdato=None):
        self.priskribo = priskribo
        self.farite = False
        self.kreadtempo = datetime.now()
        self.limdato = limdato

    def fini(self):
        self.farite = True

    def __str__(self):
        stato = []
        if self.farite:
            stato.append("(Prete)")
        elif self.limdato:
            if datetime.now() > self.limdato:
                stato.append("(Nevalide, ĉar post limdato)")
            else:
                tagoj = (self.limdato - datetime.now()).days
                stato.append(f"(Nevalidos post {tagoj} tagoj)")

        return f"{self.priskribo} " + " ".join(stato)


# implice, "patra" klaso estas "object"
class RipetaTasko(Tasko):
    def __init__(self, priskribo, limdato, tagoj_kvanto=7):
        super().__init__(priskribo, limdato)
        self.tagoj_kvanto = tagoj_kvanto
        self.posedanto = None

    def fini(self):
        super().fini()
        nova_limdato = datetime.now() + timedelta(days=self.tagoj_kvanto)
        nova_tasko = RipetaTasko(self.priskribo, nova_limdato, self.tagoj_kvanto)
        if self.posedanto:
            self.posedanto += nova_tasko
        return nova_tasko


def main():
    hejmo = Projekto("Hejmtaskoj: ")
    hejmo.aldoni("Gladi", datetime.now())
    hejmo.aldoni("Lavi telerojn", datetime.now() + timedelta(days=3, minutes=12))
    hejmo += RipetaTasko("Ŝanĝi litotukojn", datetime.now(), 6)
    hejmo.serĉi("Ŝanĝi litotukojn").fini()
    print(hejmo)

    hejmo.serĉi("Lavi telerojn").fini()
    for tasko in hejmo:
        print(f"- {tasko}")

    print(hejmo)  # nun nur 1 okazonta tasko

    superbazaro = Projekto("Aĉetumado en superbazaro: ")
    superbazaro.aldoni("Sekaj fruktoj")
    superbazaro.aldoni("Viando")
    superbazaro.aldoni("Tomato", datetime.now() + timedelta(days=3, seconds=1))
    print(superbazaro)

    aĉeti_viandon = superbazaro.serĉi("Viando")
    aĉeti_viandon.fini()

    for tasko in superbazaro:
        print(f"- {tasko}")

    print(superbazaro)  # nur 2 okazontaj


if __name__ == "__main__":
    main()
