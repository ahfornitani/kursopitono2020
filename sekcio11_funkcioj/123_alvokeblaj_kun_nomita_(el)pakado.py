# same ol 122, sed kun nomitaj parametroj
def kalkuli_fina_prezo(neta_prezo, kalkulo_imposto, **params):
    return neta_prezo + neta_prezo * kalkulo_imposto(**params)


def imposto_x(importita):
    return 0.22 if importita else 0.13


def imposto_y(eksplodiga, faktoro_multobligo=1):
    return 0.11 * faktoro_multobligo if eksplodiga else 0


if __name__ == "__main__":
    neta_prezo = 134.98
    fina_prezo = kalkuli_fina_prezo(neta_prezo, imposto_x, importita=True)
    fina_prezo = kalkuli_fina_prezo(
        fina_prezo, imposto_y, eksplodiga=True, faktoro_multobligo=1.5
    )
    print(f"Fina prezo ₷ {fina_prezo}")
