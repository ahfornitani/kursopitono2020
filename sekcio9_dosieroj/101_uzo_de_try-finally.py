try:
    dosiero = open("97_homoj.csv")
    for registro in dosiero:
        print("Nomo: {}, Aĝo: {}".format(*registro.strip().split(",")))
finally:
    print('finfine')
    dosiero.close()
