# Callable kontrolas, ĉu eblas ruli funkcion aŭ ne
# Pitono permesas havi funkcion kiel parametron! Tre potenca ebleco!
def ruli(funkcio):
    if callable(funkcio):
        funkcio()


def bonan_matenon():
    print("Bonan matenon!")


def bonan_tagon():
    print("Bonan tagon!")


if __name__ == "__main__":
    ruli(bonan_matenon)
    ruli(bonan_tagon)
    ruli(1)  # ne funkcios
