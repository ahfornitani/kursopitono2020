def sumi_2(a, b):
    return a + b


def sumi_3(a, b, c):
    return a + b + c


def sumi_n(*numeroj):
    print(type(numeroj))  # tuplo
    sumo = 0
    for n in numeroj:
        sumo += n
    return sumo


if __name__ == "__main__":
    print(sumi_2(2, 3))  # 5
    print(sumi_3(1, 2, 3))  # 6

    # pakado
    print(sumi_n(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55

    # elpakado
    tuplo_numeroj = (1, 2, 3)
    print(sumi_3(*tuplo_numeroj))

    listo_numeroj = [1, 2, 3]
    print(sumi_3(*listo_numeroj))
