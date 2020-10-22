with open('97_homoj.csv') as dosiero:
    for registro in dosiero:
        print("Nomo: {}, Aĝo: {}".format(*registro.strip().split(",")))
    
if dosiero.closed:
    print('Dosiero jam fermita!')
