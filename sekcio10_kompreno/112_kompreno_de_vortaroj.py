vortaro = {f"Ero {i}": i * 2 for i in range(10) if i % 2 == 0}
print(vortaro)

vortaro = {i: i ** 2 for i in range(10) if i % 2 == 0}
print(vortaro)

for numero, duoblo in vortaro.items():
    print(f"{numero} × 2 = {duoblo}")
