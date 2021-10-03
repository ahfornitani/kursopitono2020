# class Aĉeto(Vendisto):
#     def __init__(self, nomo, aĝo, salajro, dato, prezo):
#         super().__init__(nomo, aĝo, salajro)
#         self.dato = dato
#         self.prezo = prezo

class Aĉeto:
    def __init__(self, vendisto, dato, prezo):
        self.vendisto = vendisto
        self.dato = dato
        self.prezo = prezo
