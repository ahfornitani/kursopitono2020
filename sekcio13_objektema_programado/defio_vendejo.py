#!/usr/bin/python3

from datetime import datetime

from vendejo import Kliento, Vendisto, Aĉeto


def main():
    kliento = Kliento("Maria", 44)
    vendisto = Vendisto("Petro", 36, 1534)
    aĉeto1 = Aĉeto(kliento, datetime.now(), 567)
    aĉeto2 = Aĉeto(kliento, datetime(2018, 6, 4), 333)
    kliento.registri_aĉeton(aĉeto1)
    kliento.registri_aĉeton(aĉeto2)
    print(f"Kliento: {kliento}", "(adolto: jes)" if kliento.estas_adolto() else "")
    print(f"Vendisto: {vendisto}")

    tuta_kvanto = kliento.tuta_kvanto_aĉetoj()
    kvanto_da_aĉetaĵoj = len(kliento.aĉetaĵoj)
    print(f"Tuta kvanto: {tuta_kvanto} el {kvanto_da_aĉetaĵoj} aĉetaĵoj")

    print(f"Lasta aĉetado: {kliento.ricevi_daton_de_lasta_aĉeto()}")


if __name__ == "__main__":
    main()
