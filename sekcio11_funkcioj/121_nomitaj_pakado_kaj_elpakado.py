# nomita pakado
# **kwargs, pakado
def rezultoj_f1(**podio):
    for pozicio, stiranto in podio.items():
        print(f"{pozicio} -> {stiranto}")


# inverse, elpakado
def rezultoj_f1_elpakado(unua, dua, tria):
    print(f"1) {unua}")
    print(f"2) {dua}")
    print(f"3) {tria}")


if __name__ == "__main__":
    rezultoj_f1(unuaranga="Hamilton", duaranga="Verstappen", triaranga="Vettel")
    # je fuŝa ordo, nur por montri kiel funkcias elpakado
    podio = {"dua": "Verstappen", "unua": "Hamilton", "tria": "Vettel"}
    rezultoj_f1_elpakado(**podio)
