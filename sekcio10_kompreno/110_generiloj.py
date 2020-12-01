# Diferenco inter generator kaj list comprehension:
# generator funkcias "laŭpete" — anstataŭ krei tutan liston
# ĝi funkcias nur post "peto" per "next()"
# tial ĝia memoruzado estas pli malgranda
generilo = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generilo))  # eligo: 0
print(next(generilo))  # eligo: 4
print(next(generilo))  # eligo: 16
print(next(generilo))  # eligo: 36
print(next(generilo))  # eligo: 64
print(next(generilo))  # eligo: Eraro
