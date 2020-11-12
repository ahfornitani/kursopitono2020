import csv
from urllib import request


def legi(url):
    with request.urlopen(url) as enigo:
        print("Elŝutas CSV-n…")
        datumoj = enigo.read().decode("latin1")
        print("Elŝuto finiĝis")
        for urbo in csv.reader(datumoj.splitlines()):
            print(f"{urbo[8]}: {urbo[3]}")


if __name__ == "__main__":
    # legi(r"https://files.cod3r.com.br/curso-ython/desafio-ibge.csv")
    legi(r"105_desafio-ibge.csv")
