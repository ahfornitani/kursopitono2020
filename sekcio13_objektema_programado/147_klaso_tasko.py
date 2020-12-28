from datetime import datetime


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
    hejme = []
    hejme.append(Tasko("Gladi"))
    hejme.append(Tasko("Lavi telerojn"))

    # Defio - Lavi telerojn
    for tasko in hejme:
        if tasko.priskribo == "Lavi telerojn":
            print("Jes, mi devas lavi telerojn hejme")

    # ĝusta solvo, fare de la instruisto
    [tasko.fini() for tasko in hejme if tasko.priskribo == "Lavi telerojn"]
    for tasko in hejme:
        print(f"- {tasko}")


if __name__ == "__main__":
    main()
