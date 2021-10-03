PLENAĜULO = 18


class Homo:
    def __init__(self, nomo, aĝo):
        self.nomo = nomo
        self.aĝo = aĝo

    def __str__(self):
        return f"La homo nomiĝas {self.nomo} kaj aĝas {self.aĝo} jarojn."

    def estas_adolto(self):
        # return "Jes" if self.aĝo > 18 else "Ne"
        return (self.aĝo or 0) > PLENAĜULO
