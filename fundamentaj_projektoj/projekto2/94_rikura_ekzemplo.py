def printilo(maksimumo, aktuala):
    if aktuala < maksimumo:
        print(aktuala)
        printilo(maksimumo, aktuala + 1)


printilo(10, 1)
