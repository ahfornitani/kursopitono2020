dosiero = open('97_homoj.csv')
datumoj = dosiero.read()
dosiero.close()

for registro in datumoj.splitlines():
    print('Nomo: {}, Aĝo: {}'.format(*registro.split(',')))
