# class Auto:
#     def __init__(self, maksimuma_rapido=150):
#         self.maksimuma_rapido = maksimuma_rapido

#     def akceli(self, plirapidigo):
#         self.plirapidigo = plirapidigo
#         nuna_rapido = 0
#         if (nuna_rapido + self.plirapidigo) < self.maksimuma_rapido:
#             nuna_rapido += plirapidigo

#         return nuna_rapido

#     def bremsi(self, malplirapidigo):
#         nuna_rapido = self.maksimuma_rapido
#         self.malplirapidigo = malplirapidigo
#         if (nuna_rapido - self.malplirapidigo) > 0:
#             nuna_rapido -= malplirapidigo
#         return nuna_rapido


# if __name__ == "__main__":
#     a1 = Auto(180)

#     for _ in range(25):
#         print(a1.akceli(8))

#     for _ in range(10):
#         print(a1.bremsi(ŝanĝo=20))


class Auto:
    def __init__(self, maksimuma_rapido):
        self.maksimuma_rapido = maksimuma_rapido
        self.nuna_rapido = 0

    def akceli(self, ŝanĝo=5):
        maksimuma = self.maksimuma_rapido
        nova_rapido = self.nuna_rapido + ŝanĝo
        self.nuna_rapido = nova_rapido if nova_rapido <= maksimuma else maksimuma
        return self.nuna_rapido

    def bremsi(self, ŝanĝo=5):
        nova_rapido = self.nuna_rapido - ŝanĝo
        self.nuna_rapido = nova_rapido if nova_rapido >= 0 else 0
        return self.nuna_rapido


if __name__ == "__main__":
    a1 = Auto(180)

    for _ in range(25):
        print(a1.akceli(8))

    for _ in range(10):
        print(a1.bremsi(ŝanĝo=20))
