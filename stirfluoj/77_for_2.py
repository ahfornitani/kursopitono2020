vorto = "rektangulo"
for litero in vorto:
    print(litero, end=", ")
print("Fino")

aprobitaj = ["Rafaelo", "Petro", "Renato", "Maria"]

for nomo in aprobitaj:
    print(nomo)


for pozicio, nomo in enumerate(aprobitaj):
    print(f"pozicio + 1: {pozicio, nomo}")


tagoj_semajne = ("Dimanĉo", "Lundo", "Mardo", "Merkredo", "Ĵaŭdo", "Vendredo", "Sabato")

for tago in tagoj_semajne:
    print(f"Hodiaŭ estas {tago}")

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
