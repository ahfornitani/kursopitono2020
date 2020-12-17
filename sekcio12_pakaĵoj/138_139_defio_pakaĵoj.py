from aplik.util.generilo import nova_nomo
from aplik.komerco import ĉu_nomo_ekzistas
from aplik.komerco.interna import aldoni_nomon


def main():
    while True:
        nomo = nova_nomo()
        if not ĉu_nomo_ekzistas(nomo):
            aldoni_nomon(nomo)
            break
        
    print(f'Kreiĝis nova nomo: "{nomo}"')

if __name__ == "__main__":
    main()
