with open("97_homoj.csv") as dosiero:
    with open("homoj.txt", "w") as eligo:
        for registro in dosiero:
            homo = registro.strip().split(",")
            print("Nomo: {}, Aĝo: {}".format(*homo), file=eligo)

if dosiero.closed:
    print("Dosiero jam fermita!")

if eligo.closed:
    print("Eliga dosiero jam fermita")
