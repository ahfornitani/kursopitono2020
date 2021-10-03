from .homo import Homo

class Vendisto(Homo):
    def __init__(self, nomo, aĝo, salajro):
        super().__init__(nomo, aĝo)
        self.salajro = salajro