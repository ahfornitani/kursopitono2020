# objeto povas aspekti kiel funkcio (iomete)
class Potenco:
    def __init__(self, eksponento):
        self.eksponento = eksponento

    def __call__(self, potencato):
        return potencato ** self.eksponento


if __name__ == "__main__":
    kvadrate = Potenco(2)
    kube = Potenco(3)

    if callable(kvadrate) and callable(kube):
        print(f"3² == {kvadrate(3)}")  # 9
        print(f"5³ == {kube(5)}")  # 125
        print(Potenco(4)(3))  # 81
