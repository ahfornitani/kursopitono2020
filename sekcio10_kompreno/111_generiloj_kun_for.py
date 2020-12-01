# Diferenco inter generator kaj list comprehension:
# generator funkcias "laŭpete" — anstataŭ krei tutan liston
# ĝi funkcias nur post "peto" per "next()"
# tial ĝia memoruzado estas pli malgranda
generilo = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generilo:
    print(numero)
