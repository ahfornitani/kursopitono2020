# ĵetkubo

from random import randint


def ĵeti_kubon():
    return randint(1, 6)  # 6 inkluzive, Ĉar malsimile al 'range'


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if ĵeti_kubon() == i:
        print("Trafe!", i)
        break

else:
    print("Maltrafe!", i)
