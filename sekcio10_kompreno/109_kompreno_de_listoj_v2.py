# [ esprimo for ero in listo if kondiĉo ]
duoblo_de_paraj = [i * 2 for i in range(10) if i % 2 == 0]
print(duoblo_de_paraj)

# sen kompreno de listoj
duoblo_de_paraj = []
for i in range(10):
    if i % 2 == 0:
        duoblo_de_paraj.append(i * 2)
print(duoblo_de_paraj)
